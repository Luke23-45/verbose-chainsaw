# `extract_float_pages.py`

Extract the pages of the thesis build PDF that contain **tables**, **figures**, or
**specific page numbers**, as **PNG images** (default), **PDFs**, **JPGs**, or both.

The script reads `main.lof` / `main.lot` (and hyperref named destinations) first,
so it knows every caption, float number, and printed page without scanning the
whole document. A full caption scan is used only as a last resort.

- **Source PDF:** `src/build/thesis/main.pdf` (159 pages)
- **Output folder:** `tmp/pdf_extracts/`
- **Default output form:** `img` → PNG

---

## Requirements

```bash
python -m pip install pymupdf
```

Works with either `pymupdf` (1.24+) or the older `fitz` import.

---

## Quick start

From the repository root:

```bash
# All tables + figures as PNG images (default)
python src/utils/extract_float_pages.py

# Only tables, as PNG images
python src/utils/extract_float_pages.py -w tables

# Only Table 14, as PNG images
python src/utils/extract_float_pages.py -w tables --only 14
```

Windows PowerShell/CMD: the commands above work as-is. Quote specs containing
commas or ranges so the shell does not split them:

```powershell
python src/utils/extract_float_pages.py -w tables --only "1,14,15"
python src/utils/extract_float_pages.py -w tables --only "14-16"
```

---

## Selecting a specific table (the important part)

Use `--only` together with `-w tables`:

```bash
# One table
python src/utils/extract_float_pages.py -w tables --only 14

# Several tables
python src/utils/extract_float_pages.py -w tables --only "1,14,15"

# A range (inclusive)
python src/utils/extract_float_pages.py -w tables --only "14-16"

# Mixed range and single numbers
python src/utils/extract_float_pages.py -w tables --only "1, 5-7, 14"

# Figures use the same filter
python src/utils/extract_float_pages.py -w figures --only 2

# Tables and figures together (numbers are matched per kind)
python src/utils/extract_float_pages.py -w both --only "1-3"
```

`--only` accepts:

| Form | Meaning |
| :--- | :--- |
| `14` | Table/Figure 14 only |
| `1,14,15` | Exactly those numbers |
| `14-16` | Inclusive range 14, 15, 16 |
| `1, 5-7, 14` | Mixed list and ranges |
| `D.14` | Appendix-style numbers (exact, not range) |

Notes:

- `--only` works **only** with `-w tables`, `-w figures`, or `-w both`. It is
  rejected for `-w pages` and `-w all` (use `-p` for explicit pages instead).
- Matching is on the float number, not the PDF page.
- With `-w both`, `--only 1` means "Table 1 and Figure 1".
- Multi-page tables still produce one image per page (see naming below).

### How do I know the table number?

- Look at `src/build/thesis/main.lot` (the list of tables) or the thesis itself.
- Or list what the script can see without writing anything:

```bash
python src/utils/extract_float_pages.py -w tables --dry-run
```

The summary prints how many tables matched. To inspect every resolved entry
(number, caption, page), add `--json`:

```bash
python src/utils/extract_float_pages.py -w tables --dry-run --json
```

---

## What gets written

Default image form (`--form img`):

```text
tmp/pdf_extracts/
  tables/
    table_14_annual_report_identification_register_30_reports__p0135.png
    table_14_annual_report_identification_register_30_reports__p0136.png
    table_14_annual_report_identification_register_30_reports__p0137.png
  figures/
    figure_02_....png
  pages/                  # only for -w pages
    page_0051.png
  manifest_tables.json    # one per selection
  manifest.json           # copy of the latest run
```

PDF form (`--form pdf`):

```text
tmp/pdf_extracts/
  tables/table_14_....pdf
  figures/figure_02_....pdf
  bundles/_tables.pdf
  bundles/_figures.pdf
  bundles/_floats.pdf     # only for -w both
```

File naming:

- Single-page float: `<kind>_<number>_<caption>.png`
- Multi-page float: `<kind>_<number>_<caption>__p<physical_page>.png`
- Explicit pages: `page_<physical_page>.png`

A page shared by two floats is written once per float (two descriptive names).
The manifest records every physical page of each float in `pdf_pages`.

---

## Commands and options

### Selection (`-w` / `--what`)

| Value | Aliases | Extracts |
| :--- | :--- | :--- |
| `tables` | `table` | Every table |
| `figures` | `figure` | Every figure |
| `both` | `floats` | Tables and figures |
| `pages` | `list` | Explicit pages from `-p` |
| `all` | — | Every page in the PDF |

Default when `-w` is omitted:

- `-w pages` if `-p/--pages` is given.
- Otherwise `-w both`.

### Pages (`-p` / `--pages`)

Only valid with `-w pages` (or by itself, which implies pages mode).

```bash
# Printed thesis page numbers (default)
python src/utils/extract_float_pages.py -w pages -p "36,52,66-70"

# Physical PDF page numbers (1-based; ignores printed labels)
python src/utils/extract_float_pages.py -w pages -p "51,67" --numbering physical

# Open-ended and "all"
python src/utils/extract_float_pages.py -w pages -p "100-"
python src/utils/extract_float_pages.py -w pages -p all
```

| Spec | Meaning |
| :--- | :--- |
| `36` | One page |
| `36,52` | Two pages |
| `66-70` | Inclusive range |
| `100-` | From 100 to the last printed page |
| `-120` | From page 1 to 120 |
| `all` / `*` | Every page |

Printed page numbers are resolved via the PDF page labels (`--numbering printed`,
the default). Use `--numbering physical` when you mean the PDF's own page index.

### Output form (`--form` / `--format`)

| Value | Writes |
| :--- | :--- |
| `img` / `image` / `png` | PNG images (**default**) |
| `pdf` | One PDF per float/page + bundles |
| `jpg` / `jpeg` | JPEG images |
| `both` | PDF **and** PNG |

```bash
python src/utils/extract_float_pages.py -w tables --form pdf
python src/utils/extract_float_pages.py -w tables --form both --dpi 300
python src/utils/extract_float_pages.py -w tables --form jpg --dpi 150
```

### Other options

| Option | Description |
| :--- | :--- |
| `--only SPEC` | Filter float numbers (`14`, `1,14,15`, `14-16`). Float selections only. |
| `--dpi N` | Rasterization DPI for images. Default `200`; allowed 50–1200. |
| `--pdf PATH` | Use a different source PDF. |
| `-o`, `--out DIR` | Different output directory. |
| `--lof PATH` | Override the `.lof` sidecar (list of figures). |
| `--lot PATH` | Override the `.lot` sidecar (list of tables). |
| `--numbering printed\|physical` | Interpret `-p` values as printed labels (default) or physical pages. |
| `--no-bundle` | Do not write combined `bundles/*.pdf`. |
| `--no-overwrite` | Keep existing files instead of replacing them. |
| `--no-deep-scan` | Never fall back to a full caption scan for unresolved floats. |
| `--dry-run` | Resolve and print the plan; write nothing. |
| `--json` | Print the manifest as JSON (useful with `--dry-run`). |
| `--fail-on-empty` | Exit with status `4` when nothing matched. |
| `-v`, `--verbose` | Verbose logging. |
| `-q`, `--quiet` | Warnings/errors only. |

---

## Full example set

```bash
# Default: tables + figures, PNG, 200 DPI
python src/utils/extract_float_pages.py

# All tables only
python src/utils/extract_float_pages.py -w tables

# One table
python src/utils/extract_float_pages.py -w tables --only 14

# Several tables
python src/utils/extract_float_pages.py -w tables --only "1,14,15"

# Table range
python src/utils/extract_float_pages.py -w tables --only "14-16"

# Tables as PDFs
python src/utils/extract_float_pages.py -w tables --only 14 --form pdf

# Tables as PDF + PNG at print resolution
python src/utils/extract_float_pages.py -w tables --only "1,14,15" --form both --dpi 300

# All figures as PNGs
python src/utils/extract_float_pages.py -w figures

# One figure
python src/utils/extract_float_pages.py -w figures --only 2

# Explicit printed pages
python src/utils/extract_float_pages.py -w pages -p "36,52,66-70"

# Explicit physical pages
python src/utils/extract_float_pages.py -w pages -p "51,67" --numbering physical

# Every page as PNG (large!)
python src/utils/extract_float_pages.py -w all --form img

# Preview without writing
python src/utils/extract_float_pages.py -w tables --only 14 --dry-run -v

# Machine-readable plan
python src/utils/extract_float_pages.py -w tables --dry-run --json

# Custom source and destination
python src/utils/extract_float_pages.py --pdf path/to/other.pdf -o tmp/other_extracts
```

---

## How floats are resolved

The script avoids full-document scans and resolves each float in this order:

1. **Named destination** embedded by hyperref (e.g. `table.caption.14` → exact page).
2. **Page label** written by LaTeX (printed page `135` → physical page 149).
3. **Offset inference** from already-resolved floats or from `main.toc`.
4. **Targeted caption search** within a few pages of the expected page.
5. **Full caption scan** — only for still-unresolved floats, and only if
   `--no-deep-scan` was not passed.

Each resolved float is verified by checking that its caption appears on the
page. The result is recorded in the manifest as `resolution` and `verified`.

### Multi-page tables

Long tables (`longtable`) are detected by a repeated column header or the table's
`Note.` block on the following page. Their continuation pages are included in
`span`, and image mode writes one image per page. Prose pages, section headings,
and the next float stop the span.

---

## Manifest

Each run writes:

- `manifest_<selection>.json` — e.g. `manifest_tables.json`
- `manifest_<selection>_only_<spec>.json` — e.g. `manifest_tables_only_14.json`
  for a `--only` run (so a filtered run does not replace the full manifest)
- `manifest.json` — a copy of the latest run

Useful fields:

| Field | Meaning |
| :--- | :--- |
| `selection` | `tables`, `figures`, `both`, `pages`, or `all` |
| `only` | The `--only` spec used, or `null` |
| `output_form` | `image (png)`, `pdf`, `pdf + png`, … |
| `counts` | Tables, figures, unique pages, outputs |
| `floats[]` | `type`, `number`, `caption`, `printed_page`, `pdf_page`, `pdf_pages`, `page_label`, `resolution`, `verified`, `note` |
| `pages` | Physical page numbers for `pages`/`all` selections |
| `bundles` | Combined PDFs written |
| `warnings` | Sidecar, resolution, or validation problems |

`pdf_page` / `pdf_pages` are **physical** 1-based PDF page numbers, not printed
thesis page numbers. `printed_page` is the number printed in the thesis.

---

## Exit codes

| Code | Meaning |
| :---: | :--- |
| `0` | Success |
| `1` | Unexpected failure |
| `2` | Invalid usage or resolution error (bad spec, unknown label, …) |
| `3` | Source PDF missing or unreadable |
| `4` | `--fail-on-empty` and nothing matched |

---

## Troubleshooting

| Problem | Fix |
| :--- | :--- |
| `Build PDF not found` | Run the thesis build, or pass `--pdf <path>`. |
| `pymupdf` import error | `python -m pip install pymupdf` |
| Wrong page for a float | Check `printed_page` vs `pdf_page` in the manifest; try `--numbering physical` for `-p` selections. |
| Old captions/pages | Rebuild the thesis so `main.lof`/`main.lot` match `main.pdf`. |
| `--only` matched nothing | Check the number against `main.lot`; run with `--dry-run --json` to list what exists. |
| Existing files not updated | Remove `--no-overwrite`, or delete the old files. |
