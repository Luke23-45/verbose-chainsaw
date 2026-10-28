"""F3: value-relevance scatter panels — MPS_RD against EPS and against BVPS,
points and per-period OLS fit lines coloured by consolidation period.  Makes
the H3/H4 slope comparison visible before Model 2 formalises it.
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import seaborn as sns

from analysis.common.style import OKABE_ITO, paper_style
from analysis.dataset import AnalysisDataset
from analysis.render.figures import save

PANELS = (("eps", "EPS (NPR)"), ("bvps", "BVPS (NPR)"))
PERIOD_STYLE = {
    "pre": {"color": OKABE_ITO["blue"], "label": "Pre-consolidation"},
    "post": {"color": OKABE_ITO["vermillion"], "label": "Post-consolidation"},
}


def generate(dataset: AnalysisDataset) -> list:
    frame = dataset.panel
    with paper_style():
        fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.1), sharey=True)
        for ax, (xcol, xlabel) in zip(axes, PANELS):
            for period, style in PERIOD_STYLE.items():
                subset = frame[frame["period"] == period]
                ax.scatter(
                    subset[xcol],
                    subset["price_rd"],
                    s=24,
                    color=style["color"],
                    alpha=0.85,
                    edgecolor="none",
                    label=style["label"],
                )
                sns.regplot(
                    data=subset,
                    x=xcol,
                    y="price_rd",
                    scatter=False,
                    ax=ax,
                    truncate=True,
                    line_kws={"color": style["color"], "linewidth": 1.3, "alpha": 0.9},
                )
            ax.set_xlabel(xlabel)
            ax.set_ylabel("MPS_RD (NPR)")
        axes[0].legend(frameon=False, loc="upper left", fontsize=7.5)
        fig.suptitle(
            "MPS_RD against accounting fundamentals, pre vs post consolidation (n = 28)"
        )
        fig.tight_layout()
    return save(fig, "figures/main/F3_value_relevance")
