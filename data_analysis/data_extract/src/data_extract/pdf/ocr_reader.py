"""OCR fallback only, for scanned/image-only pages.

OCR output is always flagged ``method="ocr", confidence="low"`` in
provenance, and any value taken from OCR goes to the manual-review
queue for a human check against the page image. OCR never overwrites
a text-layer value, and it is never run on a page that already has
a usable text layer.
"""

from __future__ import annotations

import pathlib


def ocr_page(path: pathlib.Path, page_number: int, lang: str = "eng") -> dict:
    """Stub interface — implemented when the first scanned statement
    page is hit. Requires system Tesseract (``tesseract-ocr``) and,
    for Nepali pages, ``tesseract-ocr-nep`` if available.

    Returns {"page", "text", "method": "ocr", "confidence": "low"}.
    """
    raise NotImplementedError(
        "OCR reader is a fallback interface, not yet wired: install "
        "tesseract-ocr, then implement ocr_page() with pytesseract on "
        "a rendered page image. Until then, scanned statement pages "
        "go to output/manual_review/ instead of being guessed."
    )
