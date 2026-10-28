"""T2: Pearson correlation matrix (methodology step 1).

Variables: MPS_RD, EPS, BVPS, DPS, ROA on the analysis sample; lower triangle
with two-tailed significance stars.  EPS and ROA are shown for transparency
only — they correlate at r ~ 0.97 and are never co-included in a model.
"""
from __future__ import annotations

from scipy import stats as sps

from analysis.dataset import AnalysisDataset
from analysis.render.tables import Table, save_table

VARIABLES = (
    ("price_rd", "MPS_RD"),
    ("eps", "EPS"),
    ("bvps", "BVPS"),
    ("dps", "DPS"),
    ("roa", "ROA"),
)


def _stars(p: float) -> str:
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    return ""


def generate(dataset: AnalysisDataset) -> list:
    frame = dataset.panel
    columns = [column for column, _ in VARIABLES]
    names = [label for _, label in VARIABLES]
    corr = frame[columns].corr(method="pearson")
    rows = []
    for i, (column_i, name_i) in enumerate(zip(columns, names)):
        cells = []
        for j, column_j in enumerate(columns):
            if j > i:
                cells.append("")
            elif j == i:
                cells.append("1.000")
            else:
                r = float(corr.loc[column_i, column_j])
                p = float(sps.pearsonr(frame[column_i], frame[column_j]).pvalue)
                cells.append(f"{r:.3f}{_stars(p)}")
        rows.append((name_i, *cells))
    table = Table(
        id="T2_correlations",
        caption="Pearson correlations among the value-relevance variables (analysis sample)",
        headers=("Variable", *names),
        rows=tuple(rows),
        notes=(
            "* p < 0.05, ** p < 0.01 (two-tailed). EPS and ROA correlate at r ~ 0.97 "
            "(variance inflation ~ 30), so ROA never appears alongside EPS in any "
            "specification; P/E is excluded by construction (mechanical MPS/EPS overlap)."
        ),
    )
    return save_table(table, "tables/T2_correlations")
