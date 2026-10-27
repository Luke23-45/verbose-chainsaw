"""Load YAML config. Config is data, not code: bank names, merger dates
and variable definitions change here, never by editing a parser."""

from __future__ import annotations

import pathlib

import yaml

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parents[2]
CONFIG_DIR = PACKAGE_ROOT / "config"
REPORTS_DIR = PACKAGE_ROOT.parents[1] / "data" / "reports"
OUTPUT_DIR = PACKAGE_ROOT / "output"


def load_yaml(name: str) -> dict:
    with open(CONFIG_DIR / name, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def fiscal_year_map() -> dict[str, dict]:
    """Folder code -> {nepali, ad, transition_year}."""
    variables = load_yaml("variables.yaml")
    return {
        row["folder"]: row
        for row in variables["fiscal_years"]
    }


def banks() -> dict[str, dict]:
    return {
        row["code"]: row
        for row in load_yaml("banks.yaml")["series"]
    }


def reporting_institution(series: str, folder: str) -> tuple[str, bool]:
    """Return (institution name, is_transition_year) for a bank-year.

    Pre-merger years use the acquiring institution, post-merger years
    the consolidated institution, and FY 2079/80 is flagged as the
    transition year for merged series.
    """
    bank = banks()[series]
    fy = fiscal_year_map()[folder]
    transition = bool(fy.get("transition_year", False)) and bank["merged"]
    if folder in ("FY2076-77", "FY2077-78", "FY2078-79"):
        name = bank["pre_merger_name"]
    else:
        name = bank["post_merger_name"]
    return name, transition
