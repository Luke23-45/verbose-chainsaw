"""F2: Pearson correlation heatmap of the value-relevance variables
(methodology step 1).  Diverging Okabe-Ito colour scale, annotated cells.
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

from analysis.common.style import OKABE_ITO, paper_style
from analysis.dataset import AnalysisDataset
from analysis.render.figures import save

RENAME = {"price_rd": "MPS_RD", "eps": "EPS", "bvps": "BVPS", "dps": "DPS", "roa": "ROA"}


def generate(dataset: AnalysisDataset) -> list:
    frame = dataset.panel[list(RENAME)].rename(columns=RENAME)
    corr = frame.corr(method="pearson")
    cmap = LinearSegmentedColormap.from_list(
        "okabe_div", [OKABE_ITO["blue"], "#FFFFFF", OKABE_ITO["vermillion"]]
    )
    with paper_style():
        fig, ax = plt.subplots(figsize=(4.6, 3.9))
        sns.heatmap(
            corr,
            annot=True,
            fmt=".2f",
            annot_kws={"size": 7.5},
            cmap=cmap,
            vmin=-1.0,
            vmax=1.0,
            square=True,
            linewidths=0.6,
            linecolor="white",
            cbar_kws={"shrink": 0.85},
            ax=ax,
        )
        ax.set_title(f"Pearson correlations (n = {len(frame)})")
        ax.tick_params(axis="x", rotation=0)
        ax.tick_params(axis="y", rotation=0)
        ax.grid(False)
    return save(fig, "figures/main/F2_correlation_heatmap")
