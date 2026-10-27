"""Primary reader: the PDF text layer via PyMuPDF.

Returns page text plus a flag for whether the page has a usable text
layer at all. Pages without one are OCR candidates, not failures.
"""

from __future__ import annotations

import pathlib

try:
    import pymupdf as fitz
except ImportError:  # pragma: no cover - older PyMuPDF
    import fitz


def read_pages(path: pathlib.Path) -> list[dict]:
    doc = fitz.open(path)
    pages = []
    for i, page in enumerate(doc, start=1):
        text = page.get_text()
        pages.append(
            {
                "page": i,
                "text": text,
                "has_text_layer": len(text.strip()) >= 50,
                "method": "text_layer",
            }
        )
    return pages
