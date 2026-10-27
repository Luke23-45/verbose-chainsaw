"""Derived per-share variables. Pure functions, fully tested.

EPS, BVPS and ROA are computed from audited inputs, then compared
with any reported ratio. A reported ratio is a check, not the value:
if recomputed and reported disagree beyond tolerance, the bank-year
goes to manual review with both numbers cited.
"""

from __future__ import annotations


def eps(profit_attributable_npr: float, weighted_avg_shares: float) -> float:
    return profit_attributable_npr / weighted_avg_shares


def bvps(equity_npr: float, shares_outstanding: float) -> float:
    return equity_npr / shares_outstanding


def roa_percent(
    profit_after_tax_npr: float,
    assets_opening_npr: float,
    assets_closing_npr: float,
) -> float:
    average_assets = (assets_opening_npr + assets_closing_npr) / 2
    return profit_after_tax_npr / average_assets * 100
