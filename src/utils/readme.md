
# PDF Extraction & Rasterization Pipeline

A robust, dependency-free Python tool to batch-extract PDF pages or render high-resolution page images (PNG, JPEG) driven by a declarative JSON configuration.

Powered by [`PyMuPDF`](https://github.com/pymupdf/PyMuPDF) with **zero OS-level binary dependencies** (no Poppler required).

---

## Table of Contents

- [Features](#features)
- [Architecture Overview](#architecture-overview)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration Reference (`tasks.json`)](#configuration-reference-tasksjson)
  - [Supported `pages` Formats](#supported-pages-formats)
  - [Supported `output_form` Options](#supported-output_form-options)
- [CLI Usage](#cli-usage)
- [Programmatic API (Python)](#programmatic-api-python)
- [Error Handling & Edge Cases](#error-handling--edge-cases)
- [Project Structure](#project-structure)

---

## Features

- **No System Binaries Needed:** Uses `PyMuPDF` instead of `pdf2image`, removing the need to install external packages like `poppler-utils`.
- **Flexible Page Syntax:** Supports ranges (`"3-10"`), lists (`[1, 2, 5]`), open-ended ranges (`"5-"`), mixed expressions (`"1, 3-5, 8"`), or full documents (`"all"`).
- **Human-Friendly 1-Based Indexing:** Page `1` represents the first page of the document.
- **Dual Output Modes:**
  - **PDF Extraction:** Creates a compressed, clean PDF containing only selected pages.
  - **Image Rasterization:** Renders pages to PNG or JPEG at configurable DPI (defaults to crisp 200 DPI).
- **Batch Isolation:** If one task in your JSON fails (e.g., missing file or out-of-bounds page), subsequent tasks continue running safely.
- **Smart Color Rendering:** Automatically strips alpha channels for JPEG outputs to prevent distorted or black backgrounds.
- **CLI & Module Ready:** Can be executed directly from terminal or imported into an existing Python codebase.

---

## Architecture Overview

```
tasks.json ──► Config Validator ──► Task Orchestrator
                                          │
            ┌─────────────────────────────┴─────────────────────────────┐
            ▼                                                           ▼
     Page Resolver                                              Filesystem Manager
  (Normalizes 1-based                                        (Sanitizes filenames,
   ranges to 0-based indices)                                 creates parent dirs)
            │                                                           │
            └─────────────────────────────┬─────────────────────────────┘
                                          │
                                          ▼
                               Processing Engine (PyMuPDF)
                                          │
                   ┌──────────────────────┴──────────────────────┐
                   ▼                                             ▼
            [ "pdf" Mode ]                               [ "images" Mode ]
       - Lossless page copy                         - High-res rasterization (DPI)
       - Compressed PDF streams                     - PNG / JPEG auto-formatting
```

---

---

## Quick Start

### 1. Create a `tasks.json` File
```json
{
  "extract_contract_pages": {
    "src": "docs/agreement.pdf",
    "pages": {
      "range": "1-3"
    },
    "output_form": "pdf",
    "output_dir": "dist/contracts"
  },
  "render_diagram_images": {
    "src": "docs/manual.pdf",
    "pages": {
      "list": [5, 8, 12]
    },
    "output_form": "images",
    "format": "png",
    "dpi": 300,
    "output_dir": "dist/diagrams"
  }
}
```

### 2. Run the Pipeline
```bash
python pdf_pipeline.py tasks.json
```

---

## Configuration Reference (`tasks.json`)

Each top-level key represents a **Task ID** (e.g., `"pdf1"`, `"contract_task"`).

| Field | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `src` | `string` | **Yes** | — | Path to the input PDF file. |
| `pages` | `dict` / `list` / `str` | No | `"all"` | Page selection rule (see details below). |
| `output_form` | `string` | No | `"pdf"` | `"pdf"` to extract as PDF, or `"images"` / `"png"` / `"jpg"` to render images. |
| `output_dir` | `string` | No | `output/<task_id>` | Custom target directory for output files. |
| `output_name` | `string` | No | `<task_id>` | Custom base filename without extension. |
| `format` | `string` | No | `"png"` | Target image format when `output_form: "images"` (`"png"` or `"jpg"`). |
| `dpi` | `integer` | No | `200` | Rasterization resolution for images (e.g., `150`, `200`, `300`). |

---

### Supported `pages` Formats

The parser accommodates multiple ways to specify pages (all 1-based):

```json
// Option A: Dictionary with range
"pages": { "range": "3-10" }

// Option B: Dictionary with list
"pages": { "list": [1, 2, 5, 9] }

// Option C: Both range and list combined
"pages": { "range": "3-6", "list": [10, 12] }

// Option D: Direct array
"pages": [1, 2, 4, 8]

// Option E: Standard string expression
"pages": "1, 3-5, 8, 11-"

// Option F: All pages (extract entire document)
"pages": "all"
```

---

### Supported `output_form` Options

1. **PDF Extraction (`"pdf"` or `"pdf_extracted"`):**
   * Produces a single merged PDF containing the selected pages.
   * File name pattern: `<output_dir>/<output_name>.pdf`.

2. **Image Rendering (`"images"`, `"image"`, `"png"`, or `"jpg"`):**
   * Renders each chosen page into a discrete image.
   * File name pattern: `<output_dir>/<base_name>_page_<0000>.<format>`.

---

## CLI Usage

### Basic Execution
```bash
python pdf_pipeline.py tasks.json
```

### Specifying a Default Output Base Directory
If individual tasks do not define `output_dir`, use `-o` or `--output-dir` to change the default base location:
```bash
python pdf_pipeline.py tasks.json -o /var/data/pdf_output
```

### CLI Help
```bash
python pdf_pipeline.py --help
```

### Example Terminal Output
```text
2026-10-29 17:00:00 [INFO] Loaded config from tasks.json with 2 task(s).
2026-10-29 17:00:00 [INFO] ==> Processing Task: [extract_contract_pages] (Source: agreement.pdf)
2026-10-29 17:00:00 [INFO]     Document loaded: 12 total pages.
2026-10-29 17:00:00 [INFO]     Pages selected (3): [1, 2, 3]
2026-10-29 17:00:01 [INFO]     Saved PDF -> dist/contracts/extract_contract_pages.pdf

============================================================
                     EXECUTION SUMMARY
============================================================
[PASSED] Task ID : extract_contract_pages
         Status  : Successfully extracted 3 pages.
         Outputs : 1 file(s) generated
                   - dist/contracts/extract_contract_pages.pdf
------------------------------------------------------------
Total: 1 | Succeeded: 1 | Failed: 0
============================================================
```

---

## Programmatic API (Python)

You can import `PDFPipeline` directly into your application:

```python
from pathlib import Path
from pdf_pipeline import PDFPipeline

# Initialize the pipeline
pipeline = PDFPipeline(default_output_dir=Path("./dist"))

# Run using a JSON config file
results = pipeline.run_from_config("tasks.json")

# Process results
for res in results:
    if res.success:
        print(f"Task '{res.task_id}' finished successfully.")
        for out_file in res.output_files:
            print(f"  -> Generated: {out_file}")
    else:
        print(f"Task '{res.task_id}' failed: {res.message}")
```

---

## Error Handling & Edge Cases

| Scenario | Behavior |
| :--- | :--- |
| **Missing `src` file** | Task fails with a clear `FileNotFoundError`, logs error, and continues the batch. |
| **Out-of-bounds page (e.g. page 25 of 10)** | Task safely aborts with `ValueError("Requested page 25 exceeds total pages (10)")`. |
| **Corrupted or invalid JSON** | Pipeline aborts immediately with line/column syntax error. |
| **Transparent PDF to JPEG conversion** | PyMuPDF disables the alpha channel when saving as JPEG to prevent black backgrounds. |
| **Duplicate page requests (e.g. `[1, 1, 2]`)** | Deduplicated automatically while preserving sequence. |
| **Missing target directories** | Directories are created automatically using `mkdir(parents=True, exist_ok=True)`. |

---

## Project Structure

```
.
├── pdf_pipeline.py    # Main pipeline engine and CLI entry point
├── tasks.json         # Task configuration definitions
├── README.md          # Project documentation
├── output/            # Default output folder (generated at runtime)
└── samples/           # Sample input PDFs (optional)
```
