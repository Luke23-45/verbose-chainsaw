"""T1: descriptive statistics per variable and period (methodology step 1).

Rows: MPS_RD, EPS, BVPS, DPS, ROA x {full sample, pre, post}; columns: n,
mean, SD, min, max.  Computed on the analysis sample (price_rd non-missing).
"""
from __future__ import annotations

import numpy as np

from analysis.dataset import AnalysisDataset
from analysis.render.tables import Table, save_table

VARIABLES = (
    ("price_rd", "MPS_RD (NPR)"),
    ("eps", "EPS (NPR)"),
    ("bvps", "BVPS (NPR)"),
    ("dps", "DPS (NPR)"),
    ("roa", "ROA (%)"),
)
PERIODS = (
    ("all", "Full"),
    ("pre", "Pre"),
    ("post", "Post"),
)


def _fmt(value: float) -> str:
    return f"{value:,.2f}"


def generate(dataset: AnalysisDataset) -> list:
    frame = dataset.panel
    rows = []
    for column, label in VARIABLES:
        for period_key, period_label in PERIODS:
            subset = frame if period_key == "all" else frame[frame["period"] == period_key]
            values = subset[column].to_numpy(dtype=float)
            values = values[~np.isnan(values)]
            if values.size < 2:
                raise ValueError(f"T1: variable {column!r} period {period_key!r} has n < 2")
            rows.append((
                label,
                period_label,
                str(values.size),
                _fmt(float(values.mean())),
                _fmt(float(values.std(ddof=1))),
                _fmt(float(values.min())),
                _fmt(float(values.max())),
            ))
    table = Table(
        id="T1_descriptives",
        caption=(
            "Descriptive statistics of the value-relevance variables, five Nepalese "
            "commercial bank series, FY2076/77-FY2081/82"
        ),
        headers=("Variable", "Period", "n", "Mean", "SD", "Min", "Max"),
        rows=tuple(rows),
        notes=(
            "Analysis sample: bank-years whose MPS_RD falls within the 5-day window of the "
            "reporting deadline; the two window-excluded observations (HBL, NIMB FY2077/78) "
            "are dropped, never imputed. Pre = FY2076/77-FY2078/79 (n = 13); "
            "post = FY2079/80-FY2081/82 (n = 15)."
        ),
    )
    return save_table(table, "tables/T1_descriptives")
