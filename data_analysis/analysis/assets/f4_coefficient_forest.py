"""F4: coefficient forest for Model 2 — pre slopes (beta), consolidation
interactions (delta) and the implied post slopes (beta + delta) with 95%
HC3 confidence intervals.  This is the H1-H4 visual: zero inside the CI
means no rejection.
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

from analysis.common.style import OKABE_ITO, paper_style
from analysis.dataset import AnalysisDataset
from analysis.render.figures import coef_forest, save
from analysis.stats.models import TermEstimate, fit_model2


def _combo(fit, constraint: str) -> TermEstimate:
    test = fit.results.t_test(constraint)
    effect = float(np.asarray(test.effect, dtype=float).ravel()[0])
    se = float(np.asarray(test.sd, dtype=float).ravel()[0])
    ci = np.asarray(test.conf_int(), dtype=float).ravel()
    return TermEstimate(
        term=constraint, coef=effect, se=se, tvalue=effect / se,
        pvalue=float(np.asarray(test.pvalue, dtype=float).ravel()[0]),
        ci_low=float(ci[0]), ci_high=float(ci[1]),
    )


def generate(dataset: AnalysisDataset) -> list:
    fit = fit_model2(dataset.panel, "Model 2")
    rows = [
        ("EPS (pre; beta)", fit.term("eps"), OKABE_ITO["blue"]),
        ("BVPS (pre; beta)", fit.term("bvps"), OKABE_ITO["blue"]),
        ("EPS x Post (delta)", fit.term("eps:post"), OKABE_ITO["orange"]),
        ("BVPS x Post (delta)", fit.term("bvps:post"), OKABE_ITO["orange"]),
        ("EPS (post; beta+delta)", _combo(fit, "eps + eps:post = 0"), OKABE_ITO["vermillion"]),
        ("BVPS (post; beta+delta)", _combo(fit, "bvps + bvps:post = 0"), OKABE_ITO["vermillion"]),
    ]
    labels = [name for name, _est, _color in rows]
    estimates = [est.coef for _name, est, _color in rows]
    ci_low = [est.ci_low for _name, est, _color in rows]
    ci_high = [est.ci_high for _name, est, _color in rows]
    colors = [color for _name, _est, color in rows]

    with paper_style():
        fig, ax = plt.subplots(figsize=(5.8, 2.9))
        coef_forest(ax, labels, estimates, ci_low, ci_high, colors=colors)
        ax.set_xlabel("HC3 estimate with 95% CI")
        ax.set_title("Model 2 coefficients with 95% HC3 confidence intervals (n = 28)")
        handles = [
            Line2D([], [], marker="o", ls="", color=OKABE_ITO["blue"], label="pre slope"),
            Line2D([], [], marker="o", ls="", color=OKABE_ITO["orange"], label="interaction (delta)"),
            Line2D([], [], marker="o", ls="", color=OKABE_ITO["vermillion"], label="implied post slope"),
        ]
        ax.legend(handles=handles, frameon=False, loc="lower right", fontsize=7)
    return save(fig, "figures/main/F4_coefficient_forest")
