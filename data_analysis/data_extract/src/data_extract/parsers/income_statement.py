"""Statement of Profit or Loss parser.

Target raw inputs: profit_after_tax, profit_attributable_to_equity
holders, and the reported basic EPS (kept only as a cross-check
against the recomputed EPS in per_share.py, never as the panel value
on its own).
"""


def parse(tables, year_columns):
    raise NotImplementedError(
        "Income-statement parser: implement against real pages, "
        "same interface as balance_sheet.parse()."
    )
