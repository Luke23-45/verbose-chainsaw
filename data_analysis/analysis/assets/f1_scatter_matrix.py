"""F1: scatter matrix of MPS_RD, EPS and BVPS, coloured by consolidation
period (methodology step 1: "scatter matrices").  Seaborn pairplot on the
analysis sample.
"""
from __future__ import annotations

import seaborn as sns

from analysis.common.style import OKABE_ITO, paper_style
from analysis.dataset import AnalysisDataset
from analysis.render.figures import save

VARS_RENAME = {"price_rd": "MPS_RD", "eps": "EPS", "bvps": "BVPS"}


def generate(dataset: AnalysisDataset) -> list:
    frame = dataset.panel.rename(columns=VARS_RENAME)
    frame["period"] = frame["period"].map({"pre": "Pre-consolidation", "post": "Post-consolidation"})
    with paper_style():
        grid = sns.pairplot(
            frame,
            vars=list(VARS_RENAME.values()),
            hue="period",
            hue_order=("Pre-consolidation", "Post-consolidation"),
            palette={
                "Pre-consolidation": OKABE_ITO["blue"],
                "Post-consolidation": OKABE_ITO["vermillion"],
            },
            diag_kind="kde",
            plot_kws={"s": 20, "alpha": 0.85, "edgecolor": "none"},
            height=1.9,
        )
        grid.figure.suptitle(
            "MPS_RD, EPS and BVPS by consolidation period (n = 28)",
            y=1.02,
            fontsize=10,
        )
    return save(grid.figure, "figures/main/F1_scatter_matrix")
