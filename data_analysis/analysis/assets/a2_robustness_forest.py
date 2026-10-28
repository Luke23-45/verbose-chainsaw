"""A2: robustness coefficient forest for the EPS channel — earnings
coefficient (left panel) and the EPS x Post interaction delta_E (right panel)
across the EPS-based robustness specifications, with 95% HC3 confidence
intervals.  Visual companion to T5.

R3 (ROA replaces EPS) is omitted from this figure: ROA is measured in
percentage points, so its coefficient is not on the NPR-per-NPR scale of the
other specifications and would flatten every other row (its estimate is in
T5, row R3).
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from analysis.common.style import OKABE_ITO, paper_style
from analysis.dataset import AnalysisDataset
from analysis.render.figures import save
from analysis.stats.robustness import build_runs

EPS_RUN_IDS = ("R1", "R2", "R4", "R5", "R6", "R7", "R8")
SHORT_LABELS = {
    "R1": "R1 Model 1 (baseline)",
    "R2": "R2 Model 2 (baseline)",
    "R4": "R4 + DPS",
    "R5": "R5 excl. transition FY2079-80",
    "R6": "R6 excl. FY2078-79",
    "R7": "R7 bonus-adjusted BVPS",
    "R8": "R8 restated EPS",
}


def generate(dataset: AnalysisDataset) -> list:
    runs = {run.id: run for run in build_runs(dataset)}
    labels = [SHORT_LABELS[rid] for rid in EPS_RUN_IDS]
    y = np.arange(len(EPS_RUN_IDS), dtype=float)[::-1]

    earnings_est = [runs[rid].earnings().coef for rid in EPS_RUN_IDS]
    earnings_lo = [runs[rid].earnings().ci_low for rid in EPS_RUN_IDS]
    earnings_hi = [runs[rid].earnings().ci_high for rid in EPS_RUN_IDS]

    delta_ids = [rid for rid in EPS_RUN_IDS if "eps:post" in runs[rid].result.term_map()]
    y_delta = y[[EPS_RUN_IDS.index(rid) for rid in delta_ids]]
    delta_est = [runs[rid].result.term("eps:post").coef for rid in delta_ids]
    delta_lo = [runs[rid].result.term("eps:post").ci_low for rid in delta_ids]
    delta_hi = [runs[rid].result.term("eps:post").ci_high for rid in delta_ids]

    with paper_style():
        fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.9), sharey=True)
        for ax in axes:
            ax.axvline(0.0, color=OKABE_ITO["black"], lw=0.8, alpha=0.6, zorder=1)
        axes[0].hlines(y, earnings_lo, earnings_hi, color=OKABE_ITO["blue"], lw=1.3, zorder=2)
        axes[0].scatter(earnings_est, y, s=24, color=OKABE_ITO["blue"], zorder=3)
        axes[0].set_xlabel("beta(EPS), 95% CI (NPR per NPR)")
        axes[1].hlines(y_delta, delta_lo, delta_hi, color=OKABE_ITO["orange"], lw=1.3, zorder=2)
        axes[1].scatter(delta_est, y_delta, s=24, color=OKABE_ITO["orange"], zorder=3)
        axes[1].set_xlabel("delta(EPS x Post), 95% CI (NPR per NPR)")
        for ax in axes:
            ax.set_yticks(y)
            ax.set_yticklabels(labels, fontsize=7)
        axes[0].set_ylim(-0.6, len(EPS_RUN_IDS) - 0.4)
        fig.suptitle("Robustness suite: EPS-channel estimates (n = 28 unless noted in T5)")
        fig.text(
            0.01,
            -0.02,
            "R3 (ROA replaces EPS) is omitted: ROA is measured in percentage points and is "
            "not on this scale; its estimates are in T5. R1 has no interaction terms.",
            fontsize=6.5,
            color="#404040",
        )
        fig.tight_layout()
    return save(fig, "figures/appendix/A2_robustness_forest")
