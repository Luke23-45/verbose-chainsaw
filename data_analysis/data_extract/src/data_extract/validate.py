"""Validation. Every check returns a failure record or nothing;
failures are listed in output/audit/, never averaged away.

Checks implemented here (pure, tested):
- accounting identity: total assets == total liabilities + equity
- ROA/EPS/BVPS recomputation tolerance is applied by the caller,
  which holds both the recomputed and the reported value.
"""

from __future__ import annotations


def check_identity(
    assets: float, liabilities: float, equity: float, tolerance_npr: float = 1_000_000
) -> str | None:
    """Return a failure message, or None if the identity holds.

    Tolerance defaults to NPR 1m (i.e. 1,000 in '000 units) to absorb
    rounding in published statements; tighten it only with a reason
    recorded in the audit report.
    """
    if abs(assets - (liabilities + equity)) > tolerance_npr:
        return (
            f"identity failed: assets {assets:,.0f} != liabilities "
            f"{liabilities:,.0f} + equity {equity:,.0f}"
        )
    return None


def missingness(panel_rows: list[dict], required: list[str]) -> list[dict]:
    """One row per missing variable per bank-year. Missing is a
    report, not a gap to fill: the analysis stage excludes incomplete
    bank-years on the basis of this file."""
    out = []
    for row in panel_rows:
        for field in required:
            if row.get(field) is None:
                out.append(
                    {
                        "series": row["series"],
                        "fiscal_year": row["fiscal_year"],
                        "missing_field": field,
                    }
                )
    return out
