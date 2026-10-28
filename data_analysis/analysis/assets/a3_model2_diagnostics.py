"""A3: diagnostics panel for Model 2 (companion to F5, which covers Model 1)."""
from __future__ import annotations

import matplotlib.pyplot as plt

from analysis.assets._diagnostics_panel import render
from analysis.dataset import AnalysisDataset
from analysis.render.figures import paper_style, save
from analysis.stats.models import fit_model2


def generate(dataset: AnalysisDataset) -> list:
    fit = fit_model2(dataset.panel, "Model 2")
    with paper_style():
        fig, axes = plt.subplots(2, 2, figsize=(6.6, 4.6))
        render(fig, axes, fit)
        fig.suptitle("Model 2 diagnostics (n = 28)", y=1.02, fontsize=9.5)
    return save(fig, "figures/appendix/A3_model2_diagnostics")
