"""Table reader: pdfplumber, for ruled NFRS statement tables.

Text order alone scrambles a balance sheet (year columns, notes
columns, subtotals). Tables are read as cells, with the header row
kept, so a parser can match a row label to the correct year column
instead of to the nearest number on the page.
"""

from __future__ import annotations

import pathlib

import pdfplumber


def read_tables(path: pathlib.Path, page_number: int) -> list[list[list[str | None]]]:
    with pdfplumber.open(path) as pdf:
        page = pdf.pages[page_number - 1]
        return page.extract_tables() or []
