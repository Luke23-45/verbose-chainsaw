"""F5: diagnostics panel for Model 1 (methodology step 5).  Q-Q plot,
residuals vs fitted, scale-location, and Cook's distance per observation.
"""
from __future__ import annotations

import matplotlib.pyplot as plt

from analysis.assets._diagnostics_panel import render
from analysis.dataset import AnalysisDataset
from analysis.render.figures import paper_style, save
from analysis.stats.models import fit_model1


def generate(dataset: AnalysisDataset) -> list:
    fit = fit_model1(dataset.panel, "Model 1")
    with paper_style():
        fig, axes = plt.subplots(2, 2, figsize=(6.6, 4.6))
        render(fig, axes, fit)
        fig.suptitle("Model 1 diagnostics (n = 28)", y=1.02, fontsize=9.5)
    return save(fig, "figures/main/F5_diagnostics")
