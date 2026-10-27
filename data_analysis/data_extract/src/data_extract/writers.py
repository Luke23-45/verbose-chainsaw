"""Writers: the only modules allowed to create files under output/.

- output/raw/<SERIES>_<FY>.json — one file per PDF, values + provenance.
- output/tidy/bank_year_panel.csv/.json — one row per bank-year.
- output/audit/* — inventory, validation failures, missingness.
- output/manual_review/* — human queue.

A writer refuses a panel row that contains a value without
provenance. That refusal is a feature: it is what keeps an
un-sourced number out of the thesis.
"""

from __future__ import annotations

import csv
import json
import pathlib


def write_json(path: pathlib.Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)


def write_csv(path: pathlib.Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({f: row.get(f) for f in fields})
