# data_extract — PDF extraction pipeline

Turns the 30 audited annual reports in `../../data/reports/` into a
validated tidy bank-year panel. Deterministic rules first, human review
second, no silent guessing anywhere.

## Run it

```bash
cd data_analysis/data_extract
pip install -r requirements.txt
python -m data_extract.cli discover   # inventory + text/scanned classification
python -m data_extract.cli extract    # per-PDF raw JSON -> tidy panel (parsers fill in here)
python -m data_extract.cli validate   # cross-checks + missingness report
```

Run from this directory, or set `PYTHONPATH=src`. Outputs always land
under `output/` — never back into `../../data/`.

## Pipeline stages

1. **discover** (`discovery.py`) — scan `data/reports/`, hash every PDF,
   record pages and whether each page has a usable text layer. This is
   the only stage that needs to touch all 30 files at once.
2. **read** (`pdf/`) — three readers, in strict order of trust:
   `text_reader` (PyMuPDF text layer) → `table_reader` (pdfplumber,
   for the ruled NFRS statement tables) → `ocr_reader` (Tesseract,
   scanned pages only, flagged low-confidence). A page never silently
   falls back; the method used is recorded per value.
3. **parse** (`parsers/`) — locate the statement pages by keyword
   anchors, then pull one statement at a time. One module per statement,
   so a fix to the balance sheet cannot break the dividend parser.
4. **normalize** (`normalize.py`) — NPR '000 → NPR, Nepali FY →
   AD year, merger-transition flag for FY 2079/80, reporting
   institution (acquirer pre-merger, consolidated post-merger).
5. **derive** (`parsers/per_share.py`) — EPS, BVPS and ROA are
   recomputed from their audited inputs and cross-checked against any
   reported ratio. A mismatch goes to manual review, it does not get
   averaged away.
6. **validate** (`validate.py`) — accounting identities
   (assets = liabilities + equity), PAT consistency across statements,
   recomputed-vs-reported checks, and a missingness report. Failures
   are listed, not hidden.
7. **write** (`writers.py`) — `output/raw/` (one JSON per PDF, with
   provenance), `output/tidy/` (panel CSV/JSON/Parquet),
   `output/audit/` (inventory, validation, missingness),
   `output/manual_review/` (cells a human must confirm, with the
   source page cited).

## Outputs

| Output | What it is |
|---|---|
| `output/raw/<SERIES>_<FY>.json` | Everything pulled from one PDF, values + provenance |
| `output/tidy/bank_year_panel.csv` | One row per bank-year, one column per variable |
| `output/tidy/bank_year_panel.json` | Same panel, machine-readable |
| `output/tidy/variables_long.csv` | Long form, for plotting / checking |
| `output/audit/inventory.csv` | All 30 PDFs, hash, pages, text/scanned |
| `output/audit/validation_failures.csv` | Every failed cross-check |
| `output/audit/missingness.csv` | Every unavailable variable, by bank-year |
| `output/audit/extraction_report.md` | The gate report for `../analysis/` |
| `output/manual_review/*.csv` | Human review queue — the only place a value may be hand-filled, with a cited source page |

## Tools, and why each one

| Tool | Job | Why it, not an alternative |
|---|---|---|
| PyMuPDF (`fitz`) | Text layer, page text, metadata | Fastest reliable text extraction; also classifies text vs scanned pages |
| pdfplumber | Ruled statement tables | NFRS statements are ruled tables; pdfplumber reads cell structure, not just text order |
| pandas | Tidy panel, validation, export | The panel is a table; do not hand-roll CSV logic |
| Tesseract (+ ocrmypdf) | OCR fallback only | Scanned pages exist in this set (e.g. some covers/first pages are image-only). OCR is flagged low-confidence and never overwrites a text layer |
| PyYAML | Config | Bank/merger/variable definitions live in YAML, not in code, so a correction is a config edit, not a code change |
| pytest | Tests | Pure functions (FY mapping, unit conversion, ROA, identities) are tested; parsers are tested on fixture pages, not on live PDFs |

Deliberately **not** used as a source of record: Camelot/Tabula
(Java dependency, no gain over pdfplumber here), and any LLM-based
extraction (no auditable page-level provenance, and a wrong number
would look exactly like a right one). An LLM may suggest a candidate
for the manual-review queue; it may never write a value into the panel.

## Known hard cases in this exact set

- **Scanned/image-only pages** — several PDFs have image-only pages;
  OCR is required, and those cells start at low confidence.
- **Nepali legacy font (NMB FY 2079/80 Nepali edition)** — its text
  layer is not Unicode Devanagari, it is a legacy font encoding, so
  naive text extraction returns garbled Latin-looking text. That file
  is OCR-or-manual-review only; see `pdf/legacy_font.py`. Never
  "convert" it by guessing a mapping.
- **Merger transition year FY 2079/80** — four series change reporting
  boundary here. Every value from that year carries the transition
  flag and the reporting institution name.
- **Market price is out of scope here** — see `market.py`. No PDF
  parser may emit `MPS_post`.
