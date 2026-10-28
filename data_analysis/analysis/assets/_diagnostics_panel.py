"""Shared 2x2 regression-diagnostics panel renderer, used by F5 (Model 1) and
A3 (Model 2): normal Q-Q, residuals vs fitted, scale-location, and Cook's
distance against the 4/n attention threshold.
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from statsmodels.stats.outliers_influence import OLSInfluence

from analysis.common.style import OKABE_ITO
from analysis.stats.diagnostics import cooks_distance, cooks_threshold, qq_data
from analysis.stats.models import FitResult

PANEL_TITLES = ("(a) Normal Q-Q", "(b) Residuals vs fitted", "(c) Scale-location", "(d) Cook's distance")


def render(fig: plt.Figure, axes, fit: FitResult) -> None:
    results = fit.results
    fitted = np.asarray(results.fittedvalues, dtype=float)
    resid = np.asarray(results.resid, dtype=float)
    studentized = np.asarray(OLSInfluence(results).resid_studentized_internal, dtype=float)
    osm, osr, (slope, intercept) = qq_data(results)
    cooks = cooks_distance(results)
    threshold = cooks_threshold(fit.nobs)
    ax_qq, ax_res, ax_scale, ax_cooks = axes.ravel()

    ax_qq.plot(osm, osr, "o", ms=3, color=OKABE_ITO["blue"], alpha=0.85)
    ax_qq.plot(osm, slope * osm + intercept, "-", lw=1.0, color=OKABE_ITO["black"], alpha=0.7)
    ax_qq.set_xlabel("Theoretical quantiles")
    ax_qq.set_ylabel("Ordered residuals")

    ax_res.scatter(fitted, resid, s=18, color=OKABE_ITO["blue"], alpha=0.85, edgecolor="none")
    ax_res.axhline(0.0, color=OKABE_ITO["black"], lw=0.8, alpha=0.6)
    ax_res.set_xlabel("Fitted values")
    ax_res.set_ylabel("Residuals")

    ax_scale.scatter(fitted, np.sqrt(np.abs(studentized)), s=18, color=OKABE_ITO["blue"], alpha=0.85, edgecolor="none")
    ax_scale.set_xlabel("Fitted values")
    ax_scale.set_ylabel(r"$\sqrt{|\mathrm{std.\ resid}|}$")

    markerline, stemlines, _baseline = ax_cooks.stem(np.arange(fit.nobs), cooks, basefmt=" ")
    plt.setp(markerline, ms=2.5, color=OKABE_ITO["blue"])
    plt.setp(stemlines, lw=0.8, color=OKABE_ITO["blue"])
    ax_cooks.axhline(threshold, color=OKABE_ITO["vermillion"], ls="--", lw=0.9)
    ax_cooks.set_xlabel("Observation (bank-year order)")
    ax_cooks.set_ylabel("Cook's D")

    titles = list(PANEL_TITLES)
    titles[3] = f"(d) Cook's distance (dashed: 4/n = {threshold:.3f})"
    for ax, title in zip(axes.ravel(), titles):
        ax.set_title(title, fontsize=8.5)
    fig.tight_layout()
