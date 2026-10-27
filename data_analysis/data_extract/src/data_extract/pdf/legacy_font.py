"""Nepali legacy-font trap — read this before touching NMB FY 2079/80.

The Nepali edition (``NMB_FY2079-80_annual_report_NP.pdf``) renders
Nepali text with a legacy, non-Unicode font. Its text layer therefore
decodes to Latin-looking gibberish (e.g. Nepali words appearing as
ASCII strings) instead of Devanagari. That gibberish is *not* data,
and there is no safe automatic mapping to invent: a guessed mapping
would produce plausible-looking but wrong numbers and words.

Rule for this file, and any file like it:
1. Do not use its text layer for any value.
2. Extract from it by OCR (Nepali language data, if available) or by
   human reading of the page image, both flagged low-confidence.
3. Record ``legacy_font: True`` in that bank-year's provenance.

The English edition for the same year is not a substitute source:
its file in the repo is a dead S3 link (see discovery.py).
"""

LEGACY_FONT_FILES = {
    "NMB_FY2079-80_annual_report_NP.pdf",
}


def is_legacy_font(filename: str) -> bool:
    return filename in LEGACY_FONT_FILES
