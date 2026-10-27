"""CLI: discover | extract | validate.

- discover: inventory + text/scanned classification for all PDFs.
  This is the only command that is fully working today.
- extract: per-PDF parsing -> raw JSON -> tidy panel. Wired up
  statement by statement; parsers that are still stubs will fail
  loudly rather than emit a partial panel.
- validate: cross-checks + missingness on whatever panel exists.
"""

from __future__ import annotations

import argparse
import sys

from .config import OUTPUT_DIR
from .discovery import discover, missing
from .writers import write_csv, write_json


def cmd_discover() -> int:
    rows = discover()
    audit_dir = OUTPUT_DIR / "audit"
    write_csv(
        audit_dir / "inventory.csv",
        rows,
        ["series", "fiscal_year_folder", "file", "sha256",
         "pages", "text_pages", "scanned_or_image_pages", "is_pdf"],
    )
    gaps = missing(rows)
    real_reports = [r for r in rows if r["is_pdf"]]
    print(f"Files inventoried: {len(rows)} ({len(real_reports)} real PDFs)")
    print(f"Bank-years covered: {30 - len(gaps)}/30")
    if gaps:
        print(f"Missing bank-years: {sorted(gaps)}")
        return 1
    print("Inventory written to output/audit/inventory.csv")
    return 0


def cmd_extract() -> int:
    print(
        "extract: parsers are scaffolded (balance_sheet, "
        "income_statement, dividends) but not yet implemented against "
        "real pages. Implement one statement at a time, with fixture "
        "tests, before running this on the corpus. Refusing to emit "
        "a partial panel."
    )
    return 2


def cmd_validate() -> int:
    print(
        "validate: needs a tidy panel from `extract` first. "
        "See validate.py for the checks it will run."
    )
    return 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="data_extract")
    parser.add_argument("command", choices=["discover", "extract", "validate"])
    args = parser.parse_args(argv)
    return {"discover": cmd_discover, "extract": cmd_extract,
            "validate": cmd_validate}[args.command]()


if __name__ == "__main__":
    sys.exit(main())
