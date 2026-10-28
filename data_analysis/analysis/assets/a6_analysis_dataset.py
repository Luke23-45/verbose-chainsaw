"""A6: the full analysis dataset, one row per bank-year (30 intended), with
the analysis-sample flags made explicit: window-excluded prices (never
imputed), FY2078-79 entity mismatch, and the rows affected by the restated-EPS
robustness variant.  The data appendix behind every table and figure.
"""
from __future__ import annotations

from analysis.common import config
from analysis.dataset import AnalysisDataset
from analysis.render.tables import Table, save_table


def _fmt(value: float) -> str:
    return f"{value:,.2f}"


def generate(dataset: AnalysisDataset) -> list:
    restated_keys = {
        (bank, fy)
        for bank, by_fy in config.get_config()["analysis"].get("eps_restated", {}).items()
        for fy in by_fy
    }
    rows = []
    for row in dataset.panel_all.sort_values(["bank", "fy"]).itertuples():
        notes = []
        if not row.in_sample:
            notes.append(f"price outside 5-day window (gap {row.gap:.0f}d) - excluded, never imputed")
            price_cell = "n/a"
        else:
            price_cell = _fmt(row.price_rd)
        if row.in_sample and row.entity_mismatch:
            notes.append("entity mismatch (pre-merger fundamentals), kept in baseline")
        if (row.bank, row.fy) in restated_keys:
            notes.append("EPS restated in variant R8")
        rows.append((
            row.bank,
            row.fy,
            "Post" if row.post == 1 else "Pre",
            price_cell,
            _fmt(row.eps),
            _fmt(row.bvps),
            _fmt(row.dps),
            _fmt(row.roa),
            "; ".join(notes) if notes else "",
        ))
    coverage = dataset.coverage
    table = Table(
        id="A6_analysis_dataset",
        caption=(
            "Analysis dataset: accounting fundamentals and MPS_RD by bank-year, "
            f"five Nepalese commercial banks, FY2076/77-FY2081/82 ({coverage.realized} of "
            f"{coverage.intended} bank-years realized)"
        ),
        headers=("Bank", "FY", "Period", "MPS_RD (NPR)", "EPS (NPR)", "BVPS (NPR)", "DPS (NPR)", "ROA (%)", "Note"),
        rows=tuple(rows),
        notes=(
            "MPS_RD is the closing price on the first trading session following the reporting "
            "deadline (5-day window). BVPS is recomputed from balance-sheet components; DPS is "
            "the eligible cash dividend declared on or before the price-observation date. "
            "Reported basic EPS shown; variant R8 substitutes the restated values flagged above."
        ),
    )
    return save_table(table, "tables/A6_analysis_dataset")
