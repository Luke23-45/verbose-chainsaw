"""Loaders for the manual-review inputs produced by the data_extract stage.

Files (all under data_extract/output/manual_review/):
- mps_rd_joined_panel.csv          30 bank-years, accounting + MPS_RD price
- mps_rd_joined_panel_bonusadj.csv same frame + bonus-adjusted BVPS columns
- mps_rd_candidate_price_table.csv per-cell price status (clean / DELAYED)
- mps_rd_merolagani_verification.csv independent price cross-check

The analysis never reads PDFs; these CSVs are the only inputs.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from analysis.common import config
from analysis.common.io import read_csv_strict, to_bool_strict, to_numeric_strict

PANEL_REQUIRED = (
    "bank",
    "fy",
    "post",
    "price",
    "price_date",
    "gap",
    "eps",
    "bvps",
    "dps",
    "roa",
    "entity_mismatch",
)
PANEL_NUMERIC = ("post", "price", "gap", "eps", "bvps", "dps", "roa")
BONUS_REQUIRED = (*PANEL_REQUIRED, "bvps_adj", "bonus")
BONUS_NUMERIC = (*PANEL_NUMERIC, "bvps_adj", "bonus")
STATUS_REQUIRED = ("series", "fy", "price_date", "close_dataset", "gap_days", "status")
STATUS_NUMERIC = ("close_dataset", "gap_days")
MEROLAGANI_REQUIRED = ("symbol", "price_date", "dataset_close", "merolagani_ltp", "outcome")
MEROLAGANI_NUMERIC = ("dataset_close", "merolagani_ltp")
MEROLAGANI_OUTCOMES = frozenset({"match", "MISMATCH"})


def load_panel(path: Path | None = None) -> pd.DataFrame:
    path = path if path is not None else config.data_file("panel")
    frame = read_csv_strict(path, PANEL_REQUIRED)
    frame = to_numeric_strict(frame, PANEL_NUMERIC, path)
    frame = to_bool_strict(frame, "entity_mismatch", path)
    frame["price_date"] = pd.to_datetime(frame["price_date"], format="%Y-%m-%d")
    return frame


def load_bonusadj(path: Path | None = None) -> pd.DataFrame:
    path = path if path is not None else config.data_file("bonusadj")
    frame = read_csv_strict(path, BONUS_REQUIRED)
    frame = to_numeric_strict(frame, BONUS_NUMERIC, path)
    frame = to_bool_strict(frame, "entity_mismatch", path)
    frame["price_date"] = pd.to_datetime(frame["price_date"], format="%Y-%m-%d")
    return frame


def load_price_status(path: Path | None = None) -> pd.DataFrame:
    path = path if path is not None else config.data_file("price_status")
    frame = read_csv_strict(path, STATUS_REQUIRED)
    frame = to_numeric_strict(frame, STATUS_NUMERIC, path)
    return frame


def load_merolagani(path: Path | None = None) -> pd.DataFrame:
    path = path if path is not None else config.data_file("merolagani")
    frame = read_csv_strict(path, MEROLAGANI_REQUIRED)
    frame = to_numeric_strict(frame, MEROLAGANI_NUMERIC, path)
    bad = ~frame["outcome"].isin(MEROLAGANI_OUTCOMES)
    if bad.any():
        first = bad.idxmax()
        raise ValueError(
            f"{path}: outcome column line {int(first) + 2}: "
            f"expected one of {sorted(MEROLAGANI_OUTCOMES)}, got {frame.loc[first, 'outcome']!r}"
        )
    return frame
