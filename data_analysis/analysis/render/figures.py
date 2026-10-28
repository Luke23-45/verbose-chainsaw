"""Figure rendering: paper_style save helper plus shared plot primitives.

save(fig, relative) resolves against paper_root and writes the PDF/PNG twin
pair (vector + 300 DPI, fonts embedded).  coef_forest() is the shared
coefficient-plot primitive so F4, A2 and any future forest share one look.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from analysis.common import config
from analysis.common.style import paper_style


def save(fig: plt.Figure, relative: str) -> list[Path]:
    base = config.paper_root() / relative
    base.parent.mkdir(parents=True, exist_ok=True)
    pdf = base.with_suffix(".pdf")
    png = base.with_suffix(".png")
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(png, bbox_inches="tight")
    plt.close(fig)
    return [pdf, png]


def coef_forest(
    ax: plt.Axes,
    labels: list[str],
    estimates: list[float],
    ci_low: list[float],
    ci_high: list[float],
    colors: list[str] | None = None,
) -> None:
    """Horizontal forest plot of point estimates with CI whiskers."""
    y = np.arange(len(labels), dtype=float)[::-1]
    if colors is None:
        colors = ["#0072B2"] * len(labels)
    ax.hlines(y, ci_low, ci_high, color=colors, linewidth=1.4, zorder=2)
    ax.scatter(estimates, y, s=26, color=colors, zorder=3)
    ax.axvline(0.0, color="#000000", linewidth=0.8, alpha=0.6, zorder=1)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)


__all__ = ["coef_forest", "paper_style", "save"]
