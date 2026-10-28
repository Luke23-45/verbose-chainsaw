"""Shared visual language: Okabe-Ito palette, paper rcParams, period colors.

Every figure renders inside paper_style() so all assets share one look:
colorblind-safe Okabe-Ito hues, clean spines, embedded fonts (pdf.fonttype 42)
and 300-DPI PNG twins.  matplotlib runs headless on Agg.  Period colors are
fixed across all assets: pre-consolidation = blue, post = vermillion.
"""
from __future__ import annotations

import contextlib
from typing import Iterator

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OKABE_ITO = {
    "black": "#000000",
    "orange": "#E69F00",
    "sky_blue": "#56B4E9",
    "bluish_green": "#009E73",
    "yellow": "#F0E442",
    "blue": "#0072B2",
    "vermillion": "#D55E00",
    "reddish_purple": "#CC79A7",
}

PERIOD_COLORS = {"pre": OKABE_ITO["blue"], "post": OKABE_ITO["vermillion"]}


def period_color(period: str) -> str:
    try:
        return PERIOD_COLORS[period]
    except KeyError:
        raise KeyError(
            f"Unknown period {period!r}; expected one of {sorted(PERIOD_COLORS)}"
        ) from None


@contextlib.contextmanager
def paper_style() -> Iterator[None]:
    from analysis.common import config  # deferred: keeps the import graph flat

    style_cfg = config.get_config().get("style", {})
    with plt.rc_context(
        {
            "figure.dpi": 110,
            "savefig.dpi": style_cfg.get("dpi", 300),
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "font.size": 9,
            "axes.titlesize": 9.5,
            "axes.labelsize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.25,
            "grid.linewidth": 0.5,
            "axes.axisbelow": True,
            "axes.prop_cycle": matplotlib.cycler(
                color=list(OKABE_ITO.values())[1:]
            ),
        }
    ):
        yield
