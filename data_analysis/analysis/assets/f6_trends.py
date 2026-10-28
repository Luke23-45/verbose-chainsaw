"""F6: variable trends by bank series across the six fiscal years, one panel
per variable, with the post-consolidation years shaded.  Describes the panel
before modelling: the price collapse after the merger wave, the post-merger
earnings drop, and the dividend halt are all visible here.
"""
from __future__ import annotations

import matplotlib.pyplot as plt

from analysis.common.style import OKABE_ITO, paper_style
from analysis.dataset import AnalysisDataset
from analysis.render.figures import save

PANELS = (
    ("price_rd", "MPS_RD (NPR)"),
    ("eps", "EPS (NPR)"),
    ("bvps", "BVPS (NPR)"),
    ("dps", "DPS (NPR)"),
    ("roa", "ROA (%)"),
)
BANK_STYLE = {
    "GBIME": {"color": OKABE_ITO["blue"], "marker": "o"},
    "HBL": {"color": OKABE_ITO["vermillion"], "marker": "s"},
    "KBL": {"color": OKABE_ITO["bluish_green"], "marker": "^"},
    "NIMB": {"color": OKABE_ITO["orange"], "marker": "D"},
    "NMB": {"color": OKABE_ITO["reddish_purple"], "marker": "v"},
}


def generate(dataset: AnalysisDataset) -> list:
    frame = dataset.panel_all  # all 30 bank-years
    banks = [b for b in dict.fromkeys(frame["bank"])]
    fys = [f for f in dict.fromkeys(frame["fy"])]
    post_fys = set(frame.loc[frame["post"] == 1, "fy"])
    post_start = min(i for i, fy in enumerate(fys) if fy in post_fys)

    with paper_style():
        fig, axes = plt.subplots(2, 3, figsize=(7.2, 4.4), sharex=True)
        for ax, (column, ylabel) in zip(axes.ravel(), PANELS):
            ax.axvspan(post_start - 0.5, len(fys) - 0.5, color="#808080", alpha=0.10, zorder=0)
            for bank in banks:
                style = BANK_STYLE[bank]
                subset = frame[frame["bank"] == bank].sort_values("fy")
                x = range(len(subset))
                if column == "price_rd":
                    # Window-excluded prices are missing by rule; the raw price
                    # is drawn as an open marker so the gap stays auditable.
                    y_values = subset["price"].to_numpy(dtype=float)
                    excluded = ~subset["in_sample"].to_numpy(dtype=bool)
                    ax.plot(x, y_values, color=style["color"], marker=style["marker"],
                            ms=3.5, lw=1.1, label=bank)
                    if excluded.any():
                        ax.plot([i for i, flag in enumerate(excluded) if flag],
                                y_values[excluded],
                                linestyle="none", marker=style["marker"], ms=6,
                                mfc="none", mec=style["color"], zorder=4)
                    continue
                ax.plot(x, subset[column].to_numpy(dtype=float),
                        color=style["color"], marker=style["marker"], ms=3.5, lw=1.1,
                        label=bank)
            ax.set_ylabel(ylabel)
            ax.set_xticks(range(len(fys)))
            ax.set_xticklabels([fy.replace("FY", "") for fy in fys],
                               rotation=45, ha="right", fontsize=7)
        top = axes[0, 0].get_ylim()[1]
        axes[0, 0].text(post_start - 0.35, top, "post-consolidation",
                        fontsize=6.5, color="#606060", ha="left", va="top")
        axes[1, 2].axis("off")
        handles, labels = axes[0, 0].get_legend_handles_labels()
        axes[1, 2].legend(handles, labels, loc="center", frameon=False,
                          fontsize=8, title="Bank series")
        fig.suptitle(
            "Variable trends by bank series, FY2076/77-FY2081/82 "
            "(shaded: post-consolidation years)"
        )
        fig.text(
            0.01,
            -0.02,
            "Open markers: raw prices observed outside the 5-day window (HBL, NIMB FY2077/78) - "
            "excluded from the analysis sample, never imputed.",
            fontsize=6.5,
            color="#404040",
        )
        fig.tight_layout()
    return save(fig, "figures/main/F6_trends")
