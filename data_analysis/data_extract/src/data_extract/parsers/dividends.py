"""Dividend recommendation parser.

DPS is not a statement-table number. It comes from the board report /
AGM notice: the cash dividend per share *recommended for that fiscal
year*, disclosed by the MPS observation date. A documented decision
to recommend no cash dividend is DPS = 0. If no recommendation can
be established by that date, DPS is unavailable — it is never set
to 0 by default, and a later approval/payment is never backdated.

Also records: bonus share percent, and any share-capital action
between year-end and the price date (needed for per-share
comparability in per_share.py).
"""


def parse(pages):
    raise NotImplementedError(
        "Dividend parser: implement against real board-report / AGM "
        "pages, with recommendation source and status recorded."
    )
