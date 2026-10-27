"""Statement of Financial Position parser.

Target raw inputs: total_assets_closing, total_assets_opening (prior
year column of the same statement, cross-checked against the prior
year's own report), total_liabilities, ordinary_shareholders_equity.
Opening assets for a merger transition year must be read from the
transition-year statement itself, with its restatement note recorded,
not assumed to equal the prior year's closing assets.
"""


def parse(tables, year_columns):
    """Implement against real pages. Returns dict of Values
    (value, unit_as_read, page, method, confidence)."""
    raise NotImplementedError(
        "Balance-sheet parser: implement row-label matching against "
        "real statement tables, then wire it into cli extract."
    )
