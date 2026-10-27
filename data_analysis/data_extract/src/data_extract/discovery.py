"""Stage 1: inventory every PDF under data/reports/.

For each file: series, fiscal year, SHA-256, page count, and a
text-vs-scanned classification per PDF (a page counts as 'text' if its
extracted text layer holds at least 50 characters). No values are read
here; this stage only proves the corpus is complete and tells the
readers which pages will need OCR.
"""

from __future__ import annotations

import hashlib
import pathlib

try:
    import pymupdf as fitz  # PyMuPDF, current API
except ImportError:  # pragma: no cover - older PyMuPDF
    import fitz

from .config import REPORTS_DIR, fiscal_year_map

EXPECTED = {
    (series, fy)
    for series in ("GBIME", "HBL", "KBL", "NIMB", "NMB")
    for fy in fiscal_year_map()
}


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def classify(path: pathlib.Path) -> dict:
    # Known corpus quirk: NMB FY 2079/80 also ships a 4 KB S3 NoSuchKey
    # XML file with a .pdf name. It must be inventoried as not-a-PDF,
    # not crash the run, and never count as that year's report (the
    # real report is the *_NP.pdf next to it).
    if path.read_bytes()[:4] != b"%PDF":
        return {
            "pages": 0,
            "text_pages": 0,
            "scanned_or_image_pages": 0,
            "is_pdf": False,
        }
    doc = fitz.open(path)
    text_pages = 0
    for page in doc:
        if len(page.get_text().strip()) >= 50:
            text_pages += 1
    return {
        "pages": len(doc),
        "text_pages": text_pages,
        "scanned_or_image_pages": len(doc) - text_pages,
        "is_pdf": True,
    }


def discover(reports_dir: pathlib.Path = REPORTS_DIR) -> list[dict]:
    rows: list[dict] = []
    for path in sorted(reports_dir.glob("*/*/*.pdf")):
        series, folder = path.parent.parent.name, path.parent.name
        info = classify(path)
        rows.append(
            {
                "series": series,
                "fiscal_year_folder": folder,
                "file": str(path),
                "sha256": sha256(path),
                **info,
            }
        )
    return rows


def missing(rows: list[dict]) -> set[tuple[str, str]]:
    found = {(r["series"], r["fiscal_year_folder"]) for r in rows}
    return EXPECTED - found
