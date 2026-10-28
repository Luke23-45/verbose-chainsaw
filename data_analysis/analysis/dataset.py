"""AnalysisDataset: load the frozen inputs once, apply the frozen rules, and
expose typed accessors for the asset modules.

Analysis-sample rules (proposal 07_methodology, fixed here once so no asset
can re-derive them differently):
- Short-window rule: MPS_RD observed more than ``price_freshness_days`` (5)
  days from the reporting deadline is missing, never imputed.  The raw price
  column is preserved in ``price``; the rule-clean column is ``price_rd``.
- The regression frame therefore holds 28 realized bank-years (13 pre, 15
  post) of the 30 intended (5 banks x 6 fiscal years).
- FY2078-79 entity-mismatch rows stay in the baseline; only the mandated
  robustness variants drop years.

Fail-closed: structural problems (duplicate cells, unknown bank/fy, post-flag
disagreement, bonusadj misalignment, price-table disagreement) raise naming
the offending file or cell.  Absent bank-years raise in strict mode and are
reported otherwise; window-excluded cells are expected and only reported.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

from analysis.common import config
from analysis.loaders import panel as panel_loaders


@dataclass(frozen=True)
class Cell:
    bank: str
    fy: str


@dataclass(frozen=True)
class CoverageReport:
    intended: int
    realized: int
    realized_pre: int
    realized_post: int
    absent_cells: tuple[Cell, ...]
    window_excluded_cells: tuple[Cell, ...]
    entity_mismatch_cells: tuple[Cell, ...]

    def summary(self) -> str:
        lines = [
            f"coverage: intended {self.intended}, realized {self.realized} "
            f"(pre {self.realized_pre}, post {self.realized_post})"
        ]
        if self.absent_cells:
            lines.append("absent cells: " + ", ".join(f"{c.bank}/{c.fy}" for c in self.absent_cells))
        if self.window_excluded_cells:
            lines.append(
                "window-excluded cells: "
                + ", ".join(f"{c.bank}/{c.fy}" for c in self.window_excluded_cells)
            )
        if self.entity_mismatch_cells:
            lines.append(
                "entity-mismatch cells (kept in baseline): "
                + ", ".join(f"{c.bank}/{c.fy}" for c in self.entity_mismatch_cells)
            )
        return "\n".join(lines)


class AnalysisDataset:
    """Immutable-by-convention container built once per pipeline run."""

    def __init__(
        self,
        *,
        panel_all: pd.DataFrame,
        bonusadj_all: pd.DataFrame,
        price_status: pd.DataFrame,
        merolagani: pd.DataFrame,
        coverage: CoverageReport,
        expected_cells: frozenset[Cell],
        sources: dict[str, Path],
    ) -> None:
        self.panel_all = panel_all
        self.panel = panel_all.loc[panel_all["in_sample"]].copy()
        self.bonusadj_all = bonusadj_all
        self.bonusadj = bonusadj_all.loc[bonusadj_all["in_sample"]].copy()
        self.price_status = price_status
        self.merolagani = merolagani
        self.coverage = coverage
        self.expected_cells = expected_cells
        self.sources = sources
        self.restated = self._build_restated()

    def cell(self, bank: str, fy: str) -> pd.Series:
        rows = self.panel_all[(self.panel_all["bank"] == bank) & (self.panel_all["fy"] == fy)]
        if len(rows) != 1:
            raise KeyError(f"cell bank={bank!r} fy={fy!r}: expected 1 row, found {len(rows)}")
        return rows.iloc[0]

    def _build_restated(self) -> pd.DataFrame:
        """Panel with restated EPS substituted where the config declares it.

        Values are used as printed (audit note a): no mechanical restatement
        rule is applied, and ``eps_is_restated`` flags the substituted rows so
        table notes can disclose them.
        """
        overrides = config.get_config()["analysis"].get("eps_restated", {})
        frame = self.panel.copy()
        eps = frame["eps"].to_numpy(dtype=float).copy()
        flagged = np.zeros(len(frame), dtype=bool)
        for i, (bank, fy) in enumerate(zip(frame["bank"], frame["fy"])):
            value = overrides.get(bank, {}).get(fy)
            if value is not None:
                eps[i] = float(value)
                flagged[i] = True
        frame["eps"] = eps
        frame["eps_is_restated"] = flagged
        return frame


def build_dataset(strict: bool = True) -> AnalysisDataset:
    acfg = config.get_config()["analysis"]
    banks = list(acfg["banks"])
    fys = list(acfg["fys"])
    post_fys = set(acfg["post_fys"])
    freshness = int(acfg["price_freshness_days"])

    sources = {
        "panel": config.data_file("panel"),
        "bonusadj": config.data_file("bonusadj"),
        "price_status": config.data_file("price_status"),
        "merolagani": config.data_file("merolagani"),
    }
    panel_all = panel_loaders.load_panel(sources["panel"])
    _validate_panel(panel_all, banks, fys, post_fys, sources["panel"])

    # Short-window rule: outside the freshness window the price is missing,
    # never imputed.  The raw price is kept in ``price`` for traceability.
    panel_all["price_rd"] = panel_all["price"].where(panel_all["gap"] <= freshness)
    panel_all["in_sample"] = panel_all["price_rd"].notna()
    panel_all["period"] = np.where(panel_all["post"] == 1, "post", "pre")

    keys = {Cell(bank, fy) for bank, fy in zip(panel_all["bank"], panel_all["fy"])}
    expected = frozenset(Cell(bank, fy) for bank in banks for fy in fys)
    absent = tuple(
        sorted((c for c in expected - keys), key=lambda c: (c.fy, c.bank))
    )
    window_excluded = tuple(
        sorted(
            (Cell(r.bank, r.fy) for r in panel_all.loc[~panel_all["in_sample"]].itertuples()),
            key=lambda c: (c.fy, c.bank),
        )
    )
    entity_mismatch = tuple(
        sorted(
            (Cell(r.bank, r.fy) for r in panel_all.loc[panel_all["entity_mismatch"]].itertuples()),
            key=lambda c: (c.fy, c.bank),
        )
    )
    in_sample = panel_all["in_sample"]
    coverage = CoverageReport(
        intended=len(expected),
        realized=int(in_sample.sum()),
        realized_pre=int((in_sample & (panel_all["post"] == 0)).sum()),
        realized_post=int((in_sample & (panel_all["post"] == 1)).sum()),
        absent_cells=absent,
        window_excluded_cells=window_excluded,
        entity_mismatch_cells=entity_mismatch,
    )
    if strict and absent:
        names = ", ".join(f"{c.bank}/{c.fy}" for c in absent)
        raise ValueError(f"{sources['panel']}: absent bank-year cells in strict mode: {names}")

    bonusadj_all = panel_loaders.load_bonusadj(sources["bonusadj"])
    _validate_aligned_frame(bonusadj_all, panel_all, sources["bonusadj"])
    in_sample_keys = set(zip(panel_all.loc[in_sample, "bank"], panel_all.loc[in_sample, "fy"]))
    bonusadj_all["in_sample"] = [
        (bank, fy) in in_sample_keys
        for bank, fy in zip(bonusadj_all["bank"], bonusadj_all["fy"])
    ]

    price_status = panel_loaders.load_price_status(sources["price_status"])
    _validate_price_status(price_status, panel_all, sources["price_status"])

    merolagani = panel_loaders.load_merolagani(sources["merolagani"])

    return AnalysisDataset(
        panel_all=panel_all,
        bonusadj_all=bonusadj_all,
        price_status=price_status,
        merolagani=merolagani,
        coverage=coverage,
        expected_cells=expected,
        sources=sources,
    )


def _validate_panel(
    frame: pd.DataFrame,
    banks: list[str],
    fys: list[str],
    post_fys: set[str],
    source: Path,
) -> None:
    unknown_banks = sorted(set(frame["bank"]) - set(banks))
    unknown_fys = sorted(set(frame["fy"]) - set(fys))
    if unknown_banks or unknown_fys:
        raise ValueError(
            f"{source}: unknown bank/fy values: banks={unknown_banks} fys={unknown_fys}"
        )
    duplicated = frame[frame.duplicated(subset=["bank", "fy"], keep=False)]
    if not duplicated.empty:
        names = ", ".join(f"{r.bank}/{r.fy}" for r in duplicated.itertuples())
        raise ValueError(f"{source}: duplicate bank-year cells: {names}")
    bad_post = frame["post"].astype(bool) != frame["fy"].isin(post_fys)
    if bad_post.any():
        row = frame.loc[bad_post].iloc[0]
        raise ValueError(
            f"{source}: post flag disagrees with fy for {row['bank']}/{row['fy']}"
        )


def _validate_aligned_frame(other: pd.DataFrame, panel_all: pd.DataFrame, source: Path) -> None:
    """Every panel bank-year must be present in the aligned frame; extra rows
    in the aligned frame are tolerated (the panel row may be absent in lenient
    mode).  Accounting values must agree wherever both frames have the cell."""
    keys_other = set(zip(other["bank"], other["fy"]))
    keys_panel = set(zip(panel_all["bank"], panel_all["fy"]))
    missing = keys_panel - keys_other
    if missing:
        raise ValueError(
            f"{source}: primary-panel bank-years missing from the aligned frame "
            f"(missing={sorted(missing)})"
        )
    merged = other[["bank", "fy", "eps", "bvps"]].merge(
        panel_all[["bank", "fy", "eps", "bvps"]],
        on=["bank", "fy"],
        suffixes=("", "_panel"),
    )
    for column in ("eps", "bvps"):
        drift = (merged[column] - merged[f"{column}_panel"]).abs() > 1e-9
        if drift.any():
            row = merged.loc[drift].iloc[0]
            raise ValueError(
                f"{source}: {column} disagrees with the primary panel for {row['bank']}/{row['fy']}"
            )


def _validate_price_status(status: pd.DataFrame, panel_all: pd.DataFrame, source: Path) -> None:
    delayed = status["status"].astype(str).str.upper().str.startswith("DELAYED")
    status_delayed = set(zip(status.loc[delayed, "series"], status.loc[delayed, "fy"]))
    panel_delayed = set(
        zip(
            panel_all.loc[~panel_all["in_sample"], "bank"],
            panel_all.loc[~panel_all["in_sample"], "fy"],
        )
    )
    if status_delayed != panel_delayed:
        raise ValueError(
            f"{source}: DELAYED cells disagree with the short-window rule applied to the panel "
            f"(panel={sorted(panel_delayed)}, price_table={sorted(status_delayed)})"
        )
    joined = status[["series", "fy", "gap_days"]].merge(
        panel_all[["bank", "fy", "gap"]],
        left_on=["series", "fy"],
        right_on=["bank", "fy"],
    )
    drift = joined["gap_days"] != joined["gap"]
    if drift.any():
        row = joined.loc[drift].iloc[0]
        raise ValueError(f"{source}: gap disagrees with the panel for {row['series']}/{row['fy']}")
