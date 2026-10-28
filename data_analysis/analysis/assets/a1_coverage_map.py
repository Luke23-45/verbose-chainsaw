"""A1: data coverage map — one cell per bank-year (5 x 6 = 30 intended).

Colours: realized (green), realized with entity mismatch, kept in baseline
(yellow), window-excluded price, never imputed (vermillion), absent (grey).
Makes the realised n = 28 (13 pre, 15 post) auditable at a glance.
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import BoundaryNorm, ListedColormap
from matplotlib.patches import Patch

from analysis.common.style import OKABE_ITO, paper_style
from analysis.dataset import AnalysisDataset
from analysis.render.figures import save

CODE_REALIZED = 0
CODE_MISMATCH = 1
CODE_EXCLUDED = 2
CODE_ABSENT = 3

COLORS = [
    OKABE_ITO["bluish_green"],
    OKABE_ITO["yellow"],
    OKABE_ITO["vermillion"],
    "#BFBFBF",
]
LABELS = [
    "realized (n = 28)",
    "realized, entity mismatch (kept)",
    "excluded: price outside 5-day window",
    "absent",
]


def generate(dataset: AnalysisDataset) -> list:
    banks = [b for b in dict.fromkeys(dataset.panel_all["bank"])]
    fys = [f for f in dict.fromkeys(dataset.panel_all["fy"])]
    matrix = np.full((len(banks), len(fys)), CODE_ABSENT, dtype=float)
    annotations = [[""] * len(fys) for _ in banks]
    for row in dataset.panel_all.itertuples():
        i, j = banks.index(row.bank), fys.index(row.fy)
        if not row.in_sample:
            matrix[i, j] = CODE_EXCLUDED
            annotations[i][j] = f"gap {row.gap:.0f}d"
        elif row.entity_mismatch:
            matrix[i, j] = CODE_MISMATCH
            annotations[i][j] = "mis."
        else:
            matrix[i, j] = CODE_REALIZED

    coverage = dataset.coverage
    with paper_style():
        fig, ax = plt.subplots(figsize=(6.6, 2.9))
        cmap = ListedColormap(COLORS)
        norm = BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5], cmap.N)
        ax.imshow(matrix, cmap=cmap, norm=norm, aspect="auto")
        ax.grid(False)
        ax.set_xticks(np.arange(len(fys)), labels=fys)
        ax.set_yticks(np.arange(len(banks)), labels=banks)
        ax.set_xticks(np.arange(-0.5, len(fys), 1), minor=True)
        ax.set_yticks(np.arange(-0.5, len(banks), 1), minor=True)
        ax.grid(which="minor", color="white", linewidth=1.4)
        ax.tick_params(which="minor", length=0)
        for i in range(len(banks)):
            for j in range(len(fys)):
                if annotations[i][j]:
                    ax.text(j, i, annotations[i][j], ha="center", va="center", fontsize=6.5)
        ax.set_title(
            f"Bank-year coverage: {coverage.realized} of {coverage.intended} realized "
            f"({coverage.realized_pre} pre, {coverage.realized_post} post)"
        )
        handles = [Patch(facecolor=color, label=label) for color, label in zip(COLORS, LABELS)]
        fig.legend(handles=handles, loc="lower center", ncol=2, frameon=False, fontsize=7)
        fig.tight_layout(rect=(0, 0.16, 1, 1))
    return save(fig, "figures/appendix/A1_coverage_map")
