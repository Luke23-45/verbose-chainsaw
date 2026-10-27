"""Market data — deliberately a stub, and deliberately separate.

MPS_post (post-disclosure market price per share) is defined in the
proposal as the NEPSE closing price on the first trading day strictly
after the NEPSE disclosure date of that bank-year's audited statements.
No PDF contains it, so no PDF parser may emit it.

This module is the placeholder for that separate input. Its fields
are filled from NEPSE records only, with disclosure date, trading
date, listed security and source logged per bank-year. Until those
records are collected, MPS_post is None (unavailable), and any
bank-year without it is excluded from the regression sample — it is
never estimated, interpolated or borrowed from another date.
"""

FEASIBILITY_FIELDS = [
    "nepse_disclosure_date",
    "first_trading_date_after_disclosure",
    "mps_post_npr",
    "listed_security",
    "market_source",
]
