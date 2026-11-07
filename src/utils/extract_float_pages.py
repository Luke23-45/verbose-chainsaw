#!/usr/bin/env python3
"""
extract_float_pages.py
======================
Extract the PDF pages that contain tables and/or figures from the thesis
build PDF (``src/build/thesis/main.pdf`` by default).

Why this exists
---------------
The thesis build is deterministic: xelatex always writes the PDF, the list of
tables (``main.lot``) and the list of figures (``main.lof``) to the same build
directory.  Those sidecar files already know every float caption, its number
and its printed page.  Hyperref also embeds a named destination for each float
in the PDF, so we can resolve a label to an exact physical PDF page without
scanning the whole document.

Resolution order (cheapest and most reliable first):

1. Named destination from the PDF (``figure.caption.5`` -> page object).
2. Page label written by LaTeX (printed page ``36`` -> physical page 51).
3. Constant printed/physical page offset inferred from resolved floats or
   from ``main.toc``.
4. A caption text search, restricted to the expected page neighbourhood.
5. A full caption scan - only as a last resort and only for unresolved floats.

The script never scans the whole PDF during a normal run.

Output forms
------------
The default is images (``--form img`` -> PNG).  Use ``--form pdf`` for one
PDF per float/page, or ``--form both`` for PDF + PNG.  ``--form jpg`` renders
JPEG instead of PNG.

Output layout (default image form)
----------------------------------
::

    <out>/
      tables/
        table_01_<caption>.png        # single-page table (default)
        table_01_<caption>__p0051.png # each page of a multi-page table
      figures/
        figure_01_<caption>.png
      pages/
        page_0051.png                 # explicit page selection only
      manifest_both.json
      manifest.json                   # copy of the latest run

With ``--form pdf`` the same names end in ``.pdf`` and combined bundles are
written under ``bundles/``.  Per-float files contain the caption page plus any
longtable continuation pages detected by repeated column headers or the
table's ``Note.`` block.  A page that contains two floats is written once per
float (two descriptive names); the manifest records every physical page of
each float (``pdf_pages``).

Examples
--------
::

    python extract_float_pages.py                    # tables + figures, PNG
    python extract_float_pages.py --form pdf         # same, as PDFs
    python extract_float_pages.py -w tables
    python extract_float_pages.py -w tables --only 14
    python extract_float_pages.py -w tables --only "1,14,15"
    python extract_float_pages.py -w tables --only "14-16" --form pdf
    python extract_float_pages.py -w figures
    python extract_float_pages.py -w both --only "1-3" --form both   # PDF + PNG
    python extract_float_pages.py -w pages -p "36,52,66-70"
    python extract_float_pages.py -w pages -p "51,67" --numbering physical
    python extract_float_pages.py -w all
    python extract_float_pages.py --dry-run -v

Dependencies: PyMuPDF (``pip install pymupdf``).
"""

from __future__ import annotations

import argparse
import difflib
import json
import logging
import os
import re
import sys
import time
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

try:
    import pymupdf  # PyMuPDF >= 1.24
except ImportError:  # pragma: no cover - older installations expose "fitz"
    try:
        import fitz as pymupdf  # type: ignore[no-redef]
    except ImportError:
        print(
            "[error] PyMuPDF is required. Install it with:\n"
            "        python -m pip install pymupdf",
            file=sys.stderr,
        )
        sys.exit(3)


# ---------------------------------------------------------------------------
# Constants / small helpers
# ---------------------------------------------------------------------------

SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_DIR = SCRIPT_PATH.parent
REPO_ROOT = SCRIPT_DIR.parents[1]  # src/utils -> src -> thesis
DEFAULT_PDF = REPO_ROOT / "src" / "build" / "thesis" / "main.pdf"
DEFAULT_OUT = REPO_ROOT / "tmp" / "pdf_extracts"

FLOAT_KINDS = ("table", "figure")
KIND_PLURAL = {"table": "tables", "figure": "figures"}

MODE_ALIASES = {
    "table": "tables",
    "tables": "tables",
    "figure": "figures",
    "figures": "figures",
    "both": "both",
    "floats": "both",
    "all": "all",
    "pages": "pages",
    "list": "pages",
}

# A caption such as "Table 19" / "Figure 2:" at the start of a line.  The
# optional dotted number covers appendix-style numbering (Table D.14).
CAPTION_RE = re.compile(
    r"^[ \t]*(?P<kind>Table|Figure)[ \t]+"
    r"(?P<number>[0-9]+(?:\.[0-9]+)?|[A-Za-z]\.[0-9]+)"
    r"[ \t]*[:.]?[ \t]*(?P<title>.*)$"
)

# First word of a false-positive body reference such as "Table 19 shows ...".
REFERENCE_STARTERS = {
    "shows", "show", "presents", "present", "reports", "report", "summarizes",
    "summarise", "summarizes", "lists", "list", "contains", "contain",
    "provides", "provide", "gives", "give", "above", "below", "compares",
    "compare", "details", "detail", "indicates", "indicate", "displays",
    "display", "illustrates", "illustrate", "depicts", "depict",
}

ROMAN_RE = re.compile(r"^[ivxlcdm]+$", re.IGNORECASE)
ROMAN_VALUES = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}

LOG = logging.getLogger("extract_float_pages")

# Captions and manifests contain Unicode (en dashes, math letters).  Make
# Windows consoles behave instead of raising UnicodeEncodeError on --json.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass


def _configure_logging(verbose: bool, quiet: bool) -> None:
    level = logging.DEBUG if verbose else (logging.WARNING if quiet else logging.INFO)
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    LOG.handlers.clear()
    LOG.addHandler(handler)
    LOG.setLevel(level)
    LOG.propagate = False


def _display(path: Path) -> str:
    """Relative path when possible; keeps console output short and stable."""
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except (ValueError, OSError):
        return str(path)


def _read_text(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="latin-1", errors="replace")


def _atomic_replace(tmp: Path, dest: Path) -> None:
    """os.replace with a fallback for locked destination files on Windows."""
    try:
        os.replace(str(tmp), str(dest))
    except PermissionError:
        # Some PDF viewers keep the old file open.  Try once more after a
        # short pause; if it still fails, surface the original error.
        time.sleep(0.2)
        os.replace(str(tmp), str(dest))


def _write_json_atomic(path: Path, payload: Dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.stem}.{os.getpid()}.part.json")
    try:
        tmp.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        _atomic_replace(tmp, path)
    finally:
        if tmp.exists():
            try:
                tmp.unlink()
            except OSError:
                pass


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------


@dataclass
class FloatEntry:
    kind: str                       # "table" | "figure"
    number: str                     # "1", "D.14", ...
    caption: str                    # human-readable caption
    label: str = ""                 # hyperref destination, e.g. figure.caption.5
    printed_page: str = ""          # page as printed in the thesis ("36", "xi")
    pdf_page: Optional[int] = None  # 0-based physical page index
    page_label: str = ""            # PDF page label of the resolved page
    resolution: str = ""            # how pdf_page was resolved
    verified: bool = False          # caption found on the resolved page
    note: str = ""                  # diagnostic shown in the manifest
    span: List[int] = field(default_factory=list)  # all 0-based pages of the float

    @property
    def kind_plural(self) -> str:
        return KIND_PLURAL[self.kind]

    @property
    def pages(self) -> List[int]:
        if self.span:
            return list(self.span)
        return [self.pdf_page] if self.pdf_page is not None else []


@dataclass
class RunResult:
    selection: str
    pdf_path: Path
    out_dir: Path
    total_pdf_pages: int
    output_form: str = "img"
    only_filter: str = ""
    entries: List[FloatEntry] = field(default_factory=list)
    unique_pages: List[int] = field(default_factory=list)
    page_labels: List[str] = field(default_factory=list)
    outputs: List[Dict[str, object]] = field(default_factory=list)
    bundles: List[Path] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    manifest_path: Optional[Path] = None


# ---------------------------------------------------------------------------
# LaTeX sidecar parsing (.lof / .lot / .aux)
# ---------------------------------------------------------------------------


def _skip_space(text: str, pos: int) -> int:
    while pos < len(text) and text[pos] in " \t\r\n":
        pos += 1
    return pos


def _read_group(text: str, pos: int) -> Tuple[str, int]:
    """Read one balanced ``{...}`` group.  ``pos`` must point at ``{``."""
    if pos >= len(text) or text[pos] != "{":
        raise ValueError("expected '{'")

    depth = 0
    out: List[str] = []
    i = pos
    while i < len(text):
        ch = text[i]
        if ch == "\\":
            # Keep escaped characters (including \{ and \}) verbatim.
            if i + 1 < len(text):
                out.append(text[i : i + 2])
                i += 2
                continue
            out.append(ch)
            i += 1
            continue
        if ch == "{":
            depth += 1
            if depth > 1:
                out.append(ch)
            i += 1
            continue
        if ch == "}":
            depth -= 1
            if depth == 0:
                return "".join(out), i + 1
            out.append(ch)
            i += 1
            continue
        out.append(ch)
        i += 1

    raise ValueError("unbalanced braces")


def _iter_contentslines(text: str) -> Iterable[Tuple[str, str, str, str]]:
    """Yield (kind, body, page, label) from every ``\\contentsline``."""
    cursor = 0
    needle = "\\contentsline"
    while True:
        start = text.find(needle, cursor)
        if start < 0:
            return
        pos = _skip_space(text, start + len(needle))
        try:
            if pos >= len(text) or text[pos] != "{":
                raise ValueError
            kind, pos = _read_group(text, pos)

            pos = _skip_space(text, pos)
            if pos >= len(text) or text[pos] != "{":
                raise ValueError
            body, pos = _read_group(text, pos)

            pos = _skip_space(text, pos)
            if pos >= len(text) or text[pos] != "{":
                raise ValueError
            page, pos = _read_group(text, pos)

            label = ""
            pos = _skip_space(text, pos)
            if pos < len(text) and text[pos] == "{":
                label, pos = _read_group(text, pos)

            yield kind.strip(), body, page.strip(), label.strip()
            cursor = pos
        except ValueError:
            cursor = start + len(needle)


def _latex_to_text(raw: str) -> str:
    """Convert the subset of LaTeX found in .lof/.lot captions to text."""
    s = raw.replace("\n", " ")
    s = re.sub(r"\\protect\b", " ", s)
    s = re.sub(r"\\(?:ignorespaces|unskip|relax|nobreakspace)\b", " ", s)

    # Protect escaped specials so the command stripper cannot eat them.
    sentinels = {
        r"\%": "\x00PCT\x00",
        r"\&": "\x00AMP\x00",
        r"\#": "\x00HASH\x00",
        r"\_": "\x00UND\x00",
        r"\$": "\x00DLR\x00",
        r"\textbackslash": "\x00BSL\x00",
    }
    restore = {
        "\x00PCT\x00": "%",
        "\x00AMP\x00": "&",
        "\x00HASH\x00": "#",
        "\x00UND\x00": "_",
        "\x00DLR\x00": "$",
        "\x00BSL\x00": "\\",
    }
    for source, sentinel in sentinels.items():
        s = s.replace(source, sentinel)

    s = s.replace("$", " ")

    # \command{argument} -> argument (handles \mathit{MPS}, \textbf{...}, ...)
    for _ in range(6):
        stripped = re.sub(r"\\[A-Za-z@]+\*?\s*\{([^{}]*)\}", r"\1", s)
        if stripped == s:
            break
        s = stripped

    s = re.sub(r"\\[A-Za-z@]+\*?", " ", s)
    s = s.replace("{", " ").replace("}", " ")
    s = s.replace("~", " ")
    s = s.replace("---", "\u2014").replace("--", "\u2013")

    for sentinel, value in restore.items():
        s = s.replace(sentinel, value)

    s = re.sub(r"\s+", " ", s).strip()
    return s


def _parse_float_body(body: str) -> Tuple[str, str]:
    """Return (number, caption) from the second argument of \\contentsline."""
    match = re.search(r"\\numberline\s*", body)
    if not match:
        return "", _latex_to_text(body)

    pos = _skip_space(body, match.end())
    number = ""
    if pos < len(body) and body[pos] == "{":
        number, pos = _read_group(body, pos)
        number = _latex_to_text(number)

    pos = _skip_space(body, pos)
    caption = ""
    if pos < len(body) and body[pos] == "{":
        caption, pos = _read_group(body, pos)
    else:
        caption = body[pos:]

    return number.strip(), _latex_to_text(caption)


def _entries_from_sidecar(path: Path, forced_kind: Optional[str] = None) -> List[FloatEntry]:
    """Parse a .lof/.lot file (or .aux containing the same writefile lines)."""
    entries: List[FloatEntry] = []
    seen: Set[Tuple[str, str, str]] = set()

    for kind, body, page, label in _iter_contentslines(_read_text(path)):
        kind = kind.lower()
        if kind not in FLOAT_KINDS:
            continue
        if forced_kind and kind != forced_kind:
            continue

        number, caption = _parse_float_body(body)
        if not caption and not number:
            continue

        key = (kind, number, caption)
        if key in seen:
            continue
        seen.add(key)
        entries.append(
            FloatEntry(
                kind=kind,
                number=number,
                caption=caption,
                label=label,
                printed_page=page,
            )
        )

    return entries


def _load_sidecar_entries(
    pdf_path: Path,
    lof_override: Optional[Path],
    lot_override: Optional[Path],
) -> Tuple[List[FloatEntry], List[str], Dict[str, str]]:
    """Load float metadata from .lof/.lot, falling back to .aux."""
    entries: List[FloatEntry] = []
    warnings: List[str] = []
    sources: Dict[str, str] = {}

    lof_path = lof_override or pdf_path.with_suffix(".lof")
    lot_path = lot_override or pdf_path.with_suffix(".lot")
    aux_path = pdf_path.with_suffix(".aux")

    # Preferred: the explicit lists written by \listoftables / \listoffigures.
    for kind, path in (("figure", lof_path), ("table", lot_path)):
        if path and path.is_file():
            try:
                found = _entries_from_sidecar(path, forced_kind=kind)
            except Exception as exc:  # malformed sidecar: do not abort the run
                warnings.append(f"Could not parse {path.name}: {exc}")
                found = []
            if found:
                entries.extend(found)
                sources[kind] = path.name
                LOG.debug("Loaded %d %s(s) from %s", len(found), kind, path.name)
            else:
                warnings.append(f"{path.name} exists but contained no {kind} entries.")

    # Fallback: the .aux file stores the same \contentsline records.
    missing_kinds = [k for k in FLOAT_KINDS if k not in sources]
    if missing_kinds and aux_path.is_file():
        try:
            aux_entries = _entries_from_sidecar(aux_path)
        except Exception as exc:
            warnings.append(f"Could not parse {aux_path.name}: {exc}")
            aux_entries = []
        for kind in missing_kinds:
            found = [e for e in aux_entries if e.kind == kind]
            if found:
                LOG.debug("Recovered %d %s(s) from %s", len(found), kind, aux_path.name)
                entries.extend(found)
                sources[kind] = aux_path.name

    # Warn when sidecars are older than the PDF: page numbers are checked
    # against PDF anchors later, so this is informational only.
    try:
        pdf_mtime = pdf_path.stat().st_mtime
        for kind, path in (("figure", lof_path), ("table", lot_path)):
            if path and path.is_file() and path.stat().st_mtime + 2 < pdf_mtime:
                warnings.append(
                    f"{path.name} is older than {pdf_path.name}; "
                    "page numbers will be verified against the PDF."
                )
    except OSError:
        pass

    return entries, warnings, sources


# ---------------------------------------------------------------------------
# PDF access helpers
# ---------------------------------------------------------------------------


def _open_pdf(path: Path) -> "pymupdf.Document":
    if not path.is_file():
        raise FileNotFoundError(f"PDF not found: {path}")
    if path.stat().st_size == 0:
        raise ValueError(f"PDF is empty: {path}")

    doc = pymupdf.open(str(path))
    if doc.needs_pass:
        doc.close()
        raise ValueError(f"PDF is password protected: {path}")
    if doc.page_count <= 0:
        doc.close()
        raise ValueError(f"PDF has no pages: {path}")
    return doc


def _safe_page_text(doc: "pymupdf.Document", index: int) -> str:
    try:
        return doc[index].get_text("text")
    except Exception as exc:  # pragma: no cover - defensive
        LOG.debug("Text extraction failed on page %d: %s", index + 1, exc)
        return ""


def _page_label(doc: "pymupdf.Document", index: int) -> str:
    try:
        return doc[index].get_label() or ""
    except Exception:
        return ""


def _max_numeric_label(doc: "pymupdf.Document") -> Optional[int]:
    values: List[int] = []
    for index in range(doc.page_count):
        label = _page_label(doc, index)
        if label.isdigit():
            values.append(int(label))
    return max(values) if values else None


def _build_label_map(doc: "pymupdf.Document") -> Dict[str, List[int]]:
    """Map printed page labels to physical 0-based indices."""
    mapping: Dict[str, List[int]] = {}
    for index in range(doc.page_count):
        label = _page_label(doc, index)
        if label:
            mapping.setdefault(label, []).append(index)
    return mapping


def _apply_source_page_labels(
    src_doc: "pymupdf.Document",
    dest_doc: "pymupdf.Document",
    source_indices: Sequence[int],
) -> None:
    """Copy the original page labels onto an extracted PDF.

    ``insert_pdf`` copies page content but not the page-label tree, so without
    this an extracted "page 137" would display an empty label.  Each extracted
    page becomes its own label range, preserving non-contiguous bundles too.
    """
    try:
        ranges = src_doc.get_page_labels()
    except Exception:
        return
    if not ranges:
        return

    try:
        ranges = sorted(ranges, key=lambda item: int(item.get("startpage", 0)))
    except Exception:
        return

    labels: List[Dict[str, object]] = []
    for dest_index, source_index in enumerate(source_indices):
        covering = None
        for item in ranges:
            try:
                if int(item.get("startpage", 0)) <= source_index:
                    covering = item
                else:
                    break
            except (TypeError, ValueError):
                continue
        if covering is None:
            continue

        try:
            first = int(covering.get("firstpagenum", 1))
            start = int(covering.get("startpage", 0))
        except (TypeError, ValueError):
            first, start = 1, 0

        labels.append(
            {
                "startpage": dest_index,
                "prefix": str(covering.get("prefix", "") or ""),
                "style": str(covering.get("style", "D") or "D"),
                "firstpagenum": source_index - start + first,
            }
        )

    if not labels or labels[0]["startpage"] != 0:
        return
    try:
        dest_doc.set_page_labels(labels)
    except Exception as exc:  # pragma: no cover - PyMuPDF version differences
        LOG.debug("Could not copy page labels: %s", exc)


def _resolve_named_destinations(doc: "pymupdf.Document") -> Dict[str, int]:
    """Return hyperref destination name -> 0-based page index."""
    try:
        names = doc.resolve_names()
    except Exception as exc:
        LOG.debug("resolve_names() unavailable: %s", exc)
        return {}

    resolved: Dict[str, int] = {}
    for name, target in names.items():
        try:
            page = target.get("page") if isinstance(target, dict) else None
            if isinstance(page, int) and 0 <= page < doc.page_count:
                resolved[name] = page
        except Exception:
            continue
    return resolved


def _roman_to_int(value: str) -> Optional[int]:
    if not ROMAN_RE.fullmatch(value):
        return None
    total = 0
    previous = 0
    for ch in reversed(value.lower()):
        current = ROMAN_VALUES[ch]
        if current < previous:
            total -= current
        else:
            total += current
            previous = current
    return total


def _normalise_match_text(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def _caption_words(caption: str) -> List[str]:
    return [w for w in _normalise_match_text(caption).split() if len(w) > 1][:14]


def _page_contains_float(text: str, entry: FloatEntry) -> bool:
    """Lenient check that the caption for ``entry`` is on this page."""
    haystack = _normalise_match_text(text)
    if not haystack:
        return False

    marker = f"{entry.kind} {entry.number}".lower().strip()
    marker_norm = _normalise_match_text(marker)
    if marker_norm and marker_norm not in haystack:
        return False

    words = _caption_words(entry.caption)
    if not words:
        return True
    present = sum(1 for word in words if word in haystack)
    return present / len(words) >= 0.6


def _toc_offset(doc: "pymupdf.Document", pdf_path: Path) -> Optional[int]:
    """Infer printed->physical offset by matching main.toc with PDF bookmarks."""
    toc_path = pdf_path.with_suffix(".toc")
    if not toc_path.is_file():
        return None

    printed_by_title: Dict[str, str] = {}
    try:
        for kind, body, page, _label in _iter_contentslines(_read_text(toc_path)):
            if kind not in ("chapter", "section"):
                continue
            number, caption = _parse_float_body(body)
            title = _normalise_match_text(caption)
            if title and page:
                printed_by_title[title] = page
    except Exception:
        return None

    try:
        bookmarks = doc.get_toc(simple=True)
    except Exception:
        return None

    offsets: List[int] = []
    for _level, title, physical_1based in bookmarks:
        title_norm = _normalise_match_text(title or "")
        if not title_norm:
            continue
        for printed_title, printed_page in printed_by_title.items():
            if not printed_page.isdigit():
                continue
            score = difflib.SequenceMatcher(None, title_norm, printed_title).ratio()
            if score >= 0.85:
                offsets.append((int(physical_1based) - 1) - int(printed_page))
                break

    if not offsets:
        return None
    return Counter(offsets).most_common(1)[0][0]


# ---------------------------------------------------------------------------
# Page selection ("printed" labels vs physical PDF pages)
# ---------------------------------------------------------------------------


def _parse_page_spec(spec: str, total_pages: int) -> List[int]:
    """Parse ``"1, 3-5, 8-"`` into 1-based page numbers."""
    tokens = [t for t in re.split(r"[,\s]+", spec.strip()) if t]
    if not tokens:
        raise ValueError("empty page specification")

    pages: List[int] = []
    for token in tokens:
        lowered = token.lower()
        if lowered in ("all", "*"):
            pages.extend(range(1, total_pages + 1))
            continue

        range_match = re.fullmatch(r"(\d+)?-(\d+)?", token)
        if range_match:
            start_text, end_text = range_match.groups()
            start = int(start_text) if start_text else 1
            end = int(end_text) if end_text else total_pages
            if start < 1 or end < 1:
                raise ValueError(f"page numbers start at 1: {token!r}")
            if start > total_pages or end > total_pages:
                raise ValueError(
                    f"page range {token!r} exceeds the document ({total_pages} pages)"
                )
            if start > end:
                raise ValueError(f"reversed page range: {token!r}")
            pages.extend(range(start, end + 1))
            continue

        if token.isdigit():
            value = int(token)
            if value < 1 or value > total_pages:
                raise ValueError(f"page {value} is outside 1..{total_pages}")
            pages.append(value)
            continue

        # Roman/alpha page labels are accepted as exact single-page tokens.
        pages.append(token)  # type: ignore[arg-type]

    # Deduplicate while preserving order.
    result: List[int] = []
    seen: Set[object] = set()
    for page in pages:
        if page not in seen:
            seen.add(page)
            result.append(page)
    return result  # type: ignore[return-value]


def _parse_only_spec(spec: str) -> Tuple[Set[str], List[Tuple[int, int]]]:
    """Parse a float-number filter such as ``"14"``, ``"1,14,15"``, ``"1-5"``."""
    exact: Set[str] = set()
    ranges: List[Tuple[int, int]] = []

    for token in (t for t in re.split(r"[,\s]+", spec.strip()) if t):
        range_match = re.fullmatch(r"(\d+)-(\d+)", token)
        if range_match:
            start, end = int(range_match.group(1)), int(range_match.group(2))
            if start < 1 or end < 1:
                raise ValueError(f"float numbers start at 1: {token!r}")
            if start > end:
                raise ValueError(f"reversed float range: {token!r}")
            ranges.append((start, end))
        else:
            exact.add(token.strip().lower())

    if not exact and not ranges:
        raise ValueError("--only needs at least one float number or range.")
    return exact, ranges


def _filter_only(entries: List[FloatEntry], spec: str) -> List[FloatEntry]:
    exact, ranges = _parse_only_spec(spec)
    selected: List[FloatEntry] = []
    for entry in entries:
        number = entry.number.strip().lower()
        if number in exact:
            selected.append(entry)
            continue
        try:
            numeric = int(number)
        except ValueError:
            continue
        if any(start <= numeric <= end for start, end in ranges):
            selected.append(entry)
    return selected


def _printed_pages_to_indices(
    tokens: Sequence[object],
    label_map: Dict[str, List[int]],
    offset: Optional[int],
    total_pages: int,
) -> List[int]:
    """Convert printed page tokens to 0-based physical indices."""
    indices: List[int] = []
    for token in tokens:
        if isinstance(token, int):
            label = str(token)
            candidates = label_map.get(label, [])
            if len(candidates) == 1:
                indices.append(candidates[0])
                continue
            if candidates:
                # Duplicate label (rare): take the first in document order.
                indices.append(candidates[0])
                continue
            if offset is not None:
                index = token - 1 + offset
                if 0 <= index < total_pages:
                    indices.append(index)
                    continue
            raise ValueError(
                f"No printed page label {label!r} in the PDF. "
                "Use --numbering physical or pass --pdf with a labelled build."
            )

        text = str(token)
        candidates = label_map.get(text, [])
        if len(candidates) == 1:
            indices.append(candidates[0])
            continue
        if candidates:
            indices.append(candidates[0])
            continue

        roman = _roman_to_int(text)
        if roman is not None and offset is not None:
            index = roman - 1 + offset
            if 0 <= index < total_pages:
                indices.append(index)
                continue

        raise ValueError(f"Unknown page label: {text!r}")

    # Deduplicate while preserving order.
    result: List[int] = []
    seen: Set[int] = set()
    for index in indices:
        if index not in seen:
            seen.add(index)
            result.append(index)
    return result


# ---------------------------------------------------------------------------
# Float -> physical page resolution
# ---------------------------------------------------------------------------


def _resolve_entries(
    entries: List[FloatEntry],
    doc: "pymupdf.Document",
    pdf_path: Path,
    deep_scan: bool,
) -> List[str]:
    """Fill ``pdf_page`` for every entry.  Returns warnings."""
    warnings: List[str] = []
    names = _resolve_named_destinations(doc)
    label_map = _build_label_map(doc)

    # Pass 1: exact hyperref destination (best possible source).
    for entry in entries:
        if entry.label and entry.label in names:
            entry.pdf_page = names[entry.label]
            entry.resolution = "named-destination"

    # Pass 2: printed page label.
    for entry in entries:
        if entry.pdf_page is not None or not entry.printed_page:
            continue
        candidates = label_map.get(entry.printed_page.strip(), [])
        if len(candidates) == 1:
            entry.pdf_page = candidates[0]
            entry.resolution = "page-label"
        elif candidates:
            entry.pdf_page = candidates[0]
            entry.resolution = "page-label-first-match"
            entry.note = f"duplicate page label {entry.printed_page!r}"

    # Pass 3: infer the constant offset from already-resolved entries.
    offsets: List[int] = []
    for entry in entries:
        if entry.pdf_page is not None and entry.printed_page.isdigit():
            offsets.append(entry.pdf_page - int(entry.printed_page))
    offset = Counter(offsets).most_common(1)[0][0] if offsets else _toc_offset(doc, pdf_path)

    for entry in entries:
        if entry.pdf_page is not None or not entry.printed_page.isdigit():
            continue
        if offset is None:
            continue
        index = int(entry.printed_page) - 1 + offset
        if 0 <= index < doc.page_count:
            entry.pdf_page = index
            entry.resolution = "offset"

    # Verify named/page-label results by looking for the caption on the page.
    for entry in entries:
        if entry.pdf_page is None:
            continue
        text = _safe_page_text(doc, entry.pdf_page)
        entry.page_label = _page_label(doc, entry.pdf_page)
        entry.verified = _page_contains_float(text, entry)
        if not entry.verified:
            entry.note = (entry.note + "; " if entry.note else "") + "caption not found on mapped page"

    # Pass 4: targeted caption search around the expected page.
    unresolved = [e for e in entries if e.pdf_page is None]
    if unresolved:
        LOG.info("Resolving %d float(s) by caption search ...", len(unresolved))
        for entry in unresolved:
            expected = None
            if entry.printed_page.isdigit() and offset is not None:
                expected = int(entry.printed_page) - 1 + offset
            index = _search_near(doc, entry, expected, radius=4)
            if index is not None:
                entry.pdf_page = index
                entry.resolution = "caption-search-nearby"
                entry.page_label = _page_label(doc, index)
                entry.verified = True

    # Pass 5: full scan, but only for entries still unresolved.
    unresolved = [e for e in entries if e.pdf_page is None]
    if unresolved and deep_scan:
        LOG.info("Sidecars did not resolve %d float(s); scanning captions once ...", len(unresolved))
        body_pages = _body_page_indices(doc)
        text_cache: Dict[int, str] = {}
        for index in body_pages:
            text_cache[index] = _safe_page_text(doc, index)

        for entry in unresolved:
            best_index = None
            best_score = 0.0
            for index in body_pages:
                score = _caption_score(text_cache[index], entry)
                if score > best_score:
                    best_score = score
                    best_index = index
            if best_index is not None and best_score >= 0.6:
                entry.pdf_page = best_index
                entry.resolution = "full-caption-scan"
                entry.page_label = _page_label(doc, best_index)
                entry.verified = True

    for entry in entries:
        if entry.pdf_page is None:
            warnings.append(
                f"Could not find {entry.kind} {entry.number or '?'} "
                f"({entry.caption[:70]!r}) in the PDF."
            )

    return warnings


def _caption_score(page_text: str, entry: FloatEntry) -> float:
    """Similarity of a page's caption text to the sidecar caption."""
    if not page_text:
        return 0.0
    haystack = _normalise_match_text(page_text)
    marker = _normalise_match_text(f"{entry.kind} {entry.number}")
    if marker and marker not in haystack:
        return 0.0

    words = _caption_words(entry.caption)
    if not words:
        return 1.0 if marker and marker in haystack else 0.0

    joined = " ".join(words)
    if joined and joined in haystack:
        return 1.0

    present = sum(1 for word in words if word in haystack) / len(words)
    # Blend token coverage with a sequence ratio for short captions.
    ratio = difflib.SequenceMatcher(None, joined, haystack[: max(len(joined) * 3, 200)]).ratio()
    return max(present, ratio)


def _search_near(
    doc: "pymupdf.Document",
    entry: FloatEntry,
    expected: Optional[int],
    radius: int,
) -> Optional[int]:
    if expected is None:
        return None

    lower = max(0, expected - radius)
    upper = min(doc.page_count - 1, expected + radius)
    order = [expected] + [i for d in range(1, radius + 1) for i in (expected - d, expected + d)]
    for index in order:
        if index < lower or index > upper:
            continue
        if index < 0 or index >= doc.page_count:
            continue
        if _page_contains_float(_safe_page_text(doc, index), entry):
            return index
    return None


def _body_page_indices(doc: "pymupdf.Document") -> List[int]:
    """Physical indices of the arabic-numbered body pages (or every page)."""
    arabic = [
        index
        for index in range(doc.page_count)
        if _page_label(doc, index).isdigit()
    ]
    if arabic:
        return arabic
    return list(range(doc.page_count))


def _meaningful_lines(text: str) -> List[str]:
    """Non-empty content lines with the printed page number removed."""
    lines: List[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.isdigit():
            continue
        if len(line) <= 6 and ROMAN_RE.fullmatch(line):
            continue
        lines.append(line)
    return lines


def _starts_with_new_float_or_heading(line: str) -> bool:
    if re.match(r"^(?:Table|Figure)\s+[0-9A-Z]", line):
        return True
    if line.upper().startswith("APPENDIX"):
        return True
    if re.match(r"^[A-Z]\.\d", line):
        return True
    if re.match(r"^\d+(?:\.\d+)*\s+[A-Z]", line):
        return True
    return False


def _looks_like_table_continuation(candidate_text: str, start_text: str) -> bool:
    """Detect a longtable continuation page by its repeated header lines."""
    candidate_lines = _meaningful_lines(candidate_text)
    if not candidate_lines:
        return False
    if _starts_with_new_float_or_heading(candidate_lines[0]):
        return False

    start_normalised = _normalise_match_text(start_text)
    significant: List[str] = []
    for line in candidate_lines[:12]:
        normalised = _normalise_match_text(line)
        if len(normalised) >= 6:
            significant.append(normalised)

    if len(significant) < 3:
        return False

    present = sum(1 for line in significant if line in start_normalised)
    return present >= 3 and present / len(significant) >= 0.6


def _resolve_table_spans(doc: "pymupdf.Document", entries: List[FloatEntry]) -> None:
    """Expand table entries over their longtable continuation pages.

    Only the next page or two are read per table, and only when the next page
    repeats the table header or carries the table's "Note." block.  Prose
    pages, section headings and the next float stop the span.
    """
    starts = sorted({entry.pdf_page for entry in entries if entry.pdf_page is not None})

    for entry in entries:
        if entry.pdf_page is None:
            entry.span = []
            continue
        if entry.kind != "table":
            entry.span = [entry.pdf_page]
            continue

        start = entry.pdf_page
        start_text = _safe_page_text(doc, start)
        later_starts = [index for index in starts if index > start]
        limit = later_starts[0] if later_starts else doc.page_count

        span = [start]
        index = start + 1
        while index < doc.page_count and index <= limit:
            text = _safe_page_text(doc, index)
            lines = _meaningful_lines(text)

            # A table note belongs to the table and ends its span.
            if lines and lines[0].lower().startswith("note."):
                span.append(index)
                break

            if _looks_like_table_continuation(text, start_text):
                span.append(index)
                index += 1
                continue
            break

        entry.span = span


# ---------------------------------------------------------------------------
# PDF caption scan (only for missing sidecars / unresolved floats)
# ---------------------------------------------------------------------------


def _scan_pdf_captions(doc: "pymupdf.Document", wanted: Set[str]) -> List[FloatEntry]:
    entries: List[FloatEntry] = []
    seen: Set[Tuple[str, str]] = set()

    for index in _body_page_indices(doc):
        text = _safe_page_text(doc, index)
        if not text:
            continue
        head = text[:1200]
        if "List of Tables" in head or "List of Figures" in head:
            continue

        lines = [line.strip() for line in text.splitlines()]
        for line_index, line in enumerate(lines):
            match = CAPTION_RE.match(line)
            if not match:
                continue

            kind = match.group("kind").lower()
            if kind not in wanted:
                continue
            number = match.group("number").strip()
            title = match.group("title").strip()

            # "Table 19" on one line, caption on the next.
            if not title and line_index + 1 < len(lines):
                title = lines[line_index + 1].strip()

            if not title:
                continue
            starter = title.split()[0].lower().strip(":,.;")
            if starter in REFERENCE_STARTERS:
                continue
            # A body reference such as "Table 17 defines every variable ..."
            # starts with a lowercase word; real captions are title-cased here.
            if title[0].isalpha() and title[0].islower() and ":" not in line:
                continue

            key = (kind, number)
            if key in seen:
                continue
            seen.add(key)
            entries.append(
                FloatEntry(
                    kind=kind,
                    number=number,
                    caption=title,
                    printed_page=_page_label(doc, index),
                    pdf_page=index,
                    page_label=_page_label(doc, index),
                    resolution="pdf-caption-scan",
                    verified=True,
                )
            )

    return entries


# ---------------------------------------------------------------------------
# Naming / output helpers
# ---------------------------------------------------------------------------


def _slugify(value: str, max_length: int = 64) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value).strip("_")
    if len(value) > max_length:
        value = value[:max_length].rsplit("_", 1)[0].strip("_")
    return value or "untitled"


def _float_stem(entry: FloatEntry) -> str:
    number = _slugify(entry.number, 16)
    if number.isdigit():
        number = number.zfill(2)
    caption = _slugify(entry.caption)
    parts = [entry.kind, number, caption]
    return "_".join(part for part in parts if part)


def _page_stem(index: int) -> str:
    return f"page_{index + 1:04d}"


def _unique_stem(base: str, used: Set[str], page_index: Optional[int]) -> str:
    if base not in used:
        used.add(base)
        return base
    suffix = f"_p{page_index + 1:04d}" if page_index is not None else "_dup"
    candidate = base + suffix
    counter = 2
    while candidate in used:
        candidate = f"{base}{suffix}_{counter}"
        counter += 1
    used.add(candidate)
    return candidate


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------


def _write_pdf_pages(
    doc: "pymupdf.Document",
    page_indices: Sequence[int],
    dest: Path,
    overwrite: bool,
) -> bool:
    if dest.exists() and not overwrite:
        LOG.info("Skip existing %s", _display(dest))
        return False

    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_name(f".{dest.stem}.{os.getpid()}.part{dest.suffix or '.pdf'}")
    new_doc = None
    try:
        new_doc = pymupdf.open()
        indices = list(page_indices)
        for index in indices:
            new_doc.insert_pdf(doc, from_page=index, to_page=index)
        _apply_source_page_labels(doc, new_doc, indices)
        new_doc.save(str(tmp), garbage=4, deflate=True)
        new_doc.close()
        new_doc = None
        _atomic_replace(tmp, dest)
        return True
    finally:
        if new_doc is not None:
            new_doc.close()
        if tmp.exists():
            try:
                tmp.unlink()
            except OSError:
                pass


def _write_page_image(
    doc: "pymupdf.Document",
    page_index: int,
    dest: Path,
    dpi: int,
    overwrite: bool,
) -> bool:
    if dest.exists() and not overwrite:
        LOG.info("Skip existing %s", _display(dest))
        return False

    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_name(f".{dest.stem}.{os.getpid()}.part{dest.suffix}")
    try:
        pix = doc[page_index].get_pixmap(dpi=dpi, alpha=False)
        pix.save(str(tmp))
        _atomic_replace(tmp, dest)
        return True
    finally:
        if tmp.exists():
            try:
                tmp.unlink()
            except OSError:
                pass


def _output_forms(form: str) -> Tuple[bool, Optional[str]]:
    """Return (write_pdf, image_format_or_None) for a CLI form value."""
    if form == "pdf":
        return True, None
    if form == "both":
        return True, "png"
    if form in ("img", "image", "png"):
        return False, "png"
    if form in ("jpg", "jpeg"):
        return False, "jpg"
    raise ValueError(f"unsupported form: {form}")


def _normalise_form_label(form: str) -> str:
    if form in ("img", "image"):
        return "image (png)"
    if form in ("jpg", "jpeg"):
        return "image (jpg)"
    if form == "both":
        return "pdf + png"
    return form


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------


def _resolve_selection(
    mode: str,
    pages_spec: Optional[str],
    numbering: str,
    doc: "pymupdf.Document",
    entries: List[FloatEntry],
    pdf_path: Path,
) -> Tuple[List[FloatEntry], List[int], str]:
    """Return (float entries, explicit page indices, normalised mode)."""
    total_pages = doc.page_count

    if mode == "pages":
        if not pages_spec:
            raise ValueError("--what pages requires --pages (e.g. -p '36,52,66-70').")

        # "all" is unambiguous: every physical page of the PDF.
        if pages_spec.strip().lower() in ("all", "*"):
            return [], list(range(total_pages)), "pages"

        if numbering == "physical":
            tokens = _parse_page_spec(pages_spec, total_pages)
            indices = [int(token) - 1 for token in tokens if isinstance(token, int)]
            if len(indices) != len(tokens):
                raise ValueError("--numbering physical only accepts numeric page numbers.")
        else:
            # Open ranges refer to the last printed page, not the last physical
            # page (front matter is roman-numbered and comes first).
            max_printed = _max_numeric_label(doc) or total_pages
            tokens = _parse_page_spec(pages_spec, max_printed)
            label_map = _build_label_map(doc)
            offsets = [
                entry.pdf_page - int(entry.printed_page)
                for entry in entries
                if entry.pdf_page is not None and entry.printed_page.isdigit()
            ]
            offset = Counter(offsets).most_common(1)[0][0] if offsets else _toc_offset(doc, pdf_path)
            indices = _printed_pages_to_indices(tokens, label_map, offset, total_pages)
        return [], indices, "pages"

    if mode == "all":
        return [], list(range(total_pages)), "all"

    if mode == "tables":
        wanted = {"table"}
    elif mode == "figures":
        wanted = {"figure"}
    elif mode == "both":
        wanted = {"table", "figure"}
    else:
        raise ValueError(f"unsupported selection: {mode}")

    selected = [entry for entry in entries if entry.kind in wanted]
    return selected, [], mode


def _run(args: argparse.Namespace) -> RunResult:
    pdf_path = Path(args.pdf).expanduser().resolve() if args.pdf else DEFAULT_PDF
    if not pdf_path.is_file():
        raise FileNotFoundError(
            f"Build PDF not found: {pdf_path}\n"
            f"        Run  .\\build.ps1 -Target thesis  first, or pass --pdf <path>."
        )

    out_dir = Path(args.out).expanduser().resolve() if args.out else DEFAULT_OUT
    mode = MODE_ALIASES[args.what]
    overwrite = not args.no_overwrite
    make_pdf, image_format = _output_forms(args.form)

    started = time.time()
    result = RunResult(
        selection=mode,
        pdf_path=pdf_path,
        out_dir=out_dir,
        total_pdf_pages=0,
        output_form=_normalise_form_label(args.form),
    )

    doc = _open_pdf(pdf_path)
    try:
        result.total_pdf_pages = doc.page_count
        LOG.info("Source: %s (%d pages)", _display(pdf_path), doc.page_count)

        entries: List[FloatEntry] = []
        if mode in ("tables", "figures", "both"):
            entries, warnings, sources = _load_sidecar_entries(
                pdf_path,
                Path(args.lof).expanduser().resolve() if args.lof else None,
                Path(args.lot).expanduser().resolve() if args.lot else None,
            )
            result.warnings.extend(warnings)
            if sources:
                LOG.info(
                    "Sidecars: %s",
                    ", ".join(f"{kind}={name}" for kind, name in sorted(sources.items())),
                )

            entries = _dedupe_entries(entries)

            # If a whole float type has no sidecar entries, recover it from
            # the PDF text (this is the only "scan" path in a normal run).
            wanted_kinds: Set[str] = set()
            if mode == "tables":
                wanted_kinds = {"table"}
            elif mode == "figures":
                wanted_kinds = {"figure"}
            elif mode == "both":
                wanted_kinds = {"table", "figure"}

            missing_kinds = {
                kind for kind in wanted_kinds if not any(e.kind == kind for e in entries)
            }
            if missing_kinds:
                LOG.info(
                    "No %s metadata found in sidecars; scanning PDF captions ...",
                    "/".join(sorted(missing_kinds)),
                )
                scanned = _scan_pdf_captions(doc, missing_kinds)
                entries.extend(scanned)
                entries = _dedupe_entries(entries)

            result.warnings.extend(
                _resolve_entries(
                    entries,
                    doc,
                    pdf_path,
                    deep_scan=not args.no_deep_scan,
                )
            )
            entries = [e for e in entries if e.pdf_page is not None]

        selected, page_indices, mode = _resolve_selection(
            mode, args.pages, args.numbering, doc, entries, pdf_path
        )
        result.selection = mode
        result.only_filter = args.only or ""

        if mode in ("tables", "figures", "both") and args.only:
            selected = _filter_only(selected, args.only)
            if not selected:
                message = f"No floats matched --only {args.only!r}."
                LOG.warning(message)
                result.warnings.append(message)

        result.entries = selected if mode in ("tables", "figures", "both") else []
        if mode in ("tables", "figures", "both"):
            _resolve_table_spans(doc, selected)

        if mode == "pages" or mode == "all":
            result.unique_pages = page_indices
            result.page_labels = [_page_label(doc, index) for index in page_indices]
        else:
            result.unique_pages = sorted(
                {page for entry in selected for page in entry.pages}
            )

        if not selected and not page_indices:
            message = "No tables or figures matched the selection."
            LOG.warning(message)
            result.warnings.append(message)

        # ---------------------------------------------------------------
        # Write per-float / per-page outputs
        # ---------------------------------------------------------------
        if mode in ("tables", "figures", "both"):
            grouped: Dict[str, List[FloatEntry]] = {"table": [], "figure": []}
            for entry in selected:
                if entry.pdf_page is None:
                    continue
                grouped[entry.kind].append(entry)

            for kind in FLOAT_KINDS:
                kind_entries = grouped[kind]
                if not kind_entries:
                    continue
                folder = out_dir / KIND_PLURAL[kind]
                used_stems: Set[str] = set()

                for entry in kind_entries:
                    stem = _unique_stem(_float_stem(entry), used_stems, entry.pdf_page)
                    pdf_path_out = folder / f"{stem}.pdf"
                    entry_pages = entry.pages

                    record: Dict[str, object] = {
                        "type": kind,
                        "number": entry.number,
                        "caption": entry.caption,
                        "label": entry.label,
                        "printed_page": entry.printed_page or entry.page_label,
                        "pdf_page": (entry.pdf_page or 0) + 1,
                        "pdf_pages": [page + 1 for page in entry_pages],
                        "page_count": len(entry_pages),
                        "page_label": entry.page_label,
                        "resolution": entry.resolution,
                        "verified": entry.verified,
                        "note": entry.note,
                    }

                    if make_pdf:
                        if not args.dry_run:
                            wrote = _write_pdf_pages(
                                doc, entry_pages, pdf_path_out, overwrite
                            )
                        else:
                            wrote = True
                        if wrote:
                            record["pdf"] = _display(pdf_path_out)
                            LOG.info(
                                "%-6s %-4s p.%-4s (%d page%s) -> %s",
                                kind,
                                entry.number,
                                entry.printed_page or entry.page_label or "?",
                                len(entry_pages),
                                "" if len(entry_pages) == 1 else "s",
                                _display(pdf_path_out),
                            )

                    if image_format:
                        image_paths: List[str] = []
                        for page_index in entry_pages:
                            if len(entry_pages) == 1:
                                image_name = f"{stem}.{image_format}"
                            else:
                                image_name = f"{stem}__p{page_index + 1:04d}.{image_format}"
                            image_path_out = folder / image_name
                            if not args.dry_run:
                                wrote = _write_page_image(
                                    doc, page_index, image_path_out, args.dpi, overwrite
                                )
                            else:
                                wrote = True
                            if wrote:
                                image_paths.append(_display(image_path_out))
                        if image_paths:
                            record["images"] = image_paths
                            record["image"] = image_paths[0]

                    result.outputs.append(record)

        elif mode in ("pages", "all"):
            folder = out_dir / "pages"

            if mode == "pages":
                used_stems: Set[str] = set()
                for index in page_indices:
                    stem = _unique_stem(_page_stem(index), used_stems, index)
                    pdf_path_out = folder / f"{stem}.pdf"
                    image_path_out = folder / f"{stem}.{image_format}" if image_format else None
                    record: Dict[str, object] = {
                        "type": "page",
                        "pdf_page": index + 1,
                        "page_label": _page_label(doc, index),
                    }
                    if make_pdf:
                        if not args.dry_run:
                            _write_pdf_pages(doc, [index], pdf_path_out, overwrite)
                        record["pdf"] = _display(pdf_path_out)
                        LOG.info(
                            "page %-4d (label %-4s) -> %s",
                            index + 1,
                            _page_label(doc, index) or "-",
                            _display(pdf_path_out),
                        )
                    if image_path_out is not None:
                        if not args.dry_run:
                            _write_page_image(
                                doc, index, image_path_out, args.dpi, overwrite
                            )
                        record["image"] = _display(image_path_out)
                    result.outputs.append(record)

            bundle_name = "_all_pages.pdf" if mode == "all" else "_selected_pages.pdf"
            bundle_pdf = out_dir / "bundles" / bundle_name

            if make_pdf and page_indices and not args.no_bundle:
                if not args.dry_run:
                    _write_pdf_pages(doc, page_indices, bundle_pdf, overwrite)
                result.bundles.append(bundle_pdf)
                LOG.info("Bundle -> %s (%d pages)", _display(bundle_pdf), len(page_indices))
                if mode == "all":
                    result.outputs.append(
                        {
                            "type": "bundle",
                            "pages": len(page_indices),
                            "pdf": _display(bundle_pdf),
                        }
                    )

            # "-w all --form img/png/jpg/both" renders every page.  This is
            # explicit (the user asked for images), so it is not a silent
            # full-document scan.
            if mode == "all" and image_format:
                for index in page_indices:
                    image_path = folder / f"{_page_stem(index)}.{image_format}"
                    if not args.dry_run:
                        _write_page_image(doc, index, image_path, args.dpi, overwrite)
                    result.outputs.append(
                        {
                            "type": "page",
                            "pdf_page": index + 1,
                            "page_label": _page_label(doc, index),
                            "image": _display(image_path),
                        }
                    )

        # ---------------------------------------------------------------
        # Bundles for float selections
        # ---------------------------------------------------------------
        if mode in ("tables", "figures", "both") and make_pdf and not args.no_bundle:
            bundles_dir = out_dir / "bundles"
            per_kind = {
                "table": sorted(
                    {page for e in selected if e.kind == "table" for page in e.pages}
                ),
                "figure": sorted(
                    {page for e in selected if e.kind == "figure" for page in e.pages}
                ),
            }
            for kind, indices in per_kind.items():
                if not indices:
                    continue
                bundle = bundles_dir / f"_{KIND_PLURAL[kind]}.pdf"
                if not args.dry_run:
                    _write_pdf_pages(doc, indices, bundle, overwrite)
                result.bundles.append(bundle)
                LOG.info(
                    "Bundle -> %s (%d unique pages)",
                    _display(bundle),
                    len(indices),
                )

            if mode == "both":
                all_indices = sorted(
                    {page for e in selected for page in e.pages}
                )
                if all_indices:
                    bundle = bundles_dir / "_floats.pdf"
                    if not args.dry_run:
                        _write_pdf_pages(doc, all_indices, bundle, overwrite)
                    result.bundles.append(bundle)
                    LOG.info(
                        "Bundle -> %s (%d unique pages)",
                        _display(bundle),
                        len(all_indices),
                    )

    finally:
        doc.close()

    # ---------------------------------------------------------------
    # Manifest
    # ---------------------------------------------------------------
    if not args.dry_run:
        # Keep one manifest per selection so running "tables" and then
        # "figures" does not silently erase the first run's metadata.  A
        # filtered run gets its own file so it cannot replace the full list.
        manifest_stem = f"manifest_{result.selection}"
        if result.only_filter:
            manifest_stem += f"_only_{_slugify(result.only_filter, 24)}"
        result.manifest_path = out_dir / f"{manifest_stem}.json"
        manifest = _build_manifest(result, started)
        _write_json_atomic(result.manifest_path, manifest)

        latest = out_dir / "manifest.json"
        if latest != result.manifest_path:
            _write_json_atomic(latest, manifest)

    return result


def _dedupe_entries(entries: List[FloatEntry]) -> List[FloatEntry]:
    """Drop duplicate (kind, number, caption) records, keeping the first."""
    result: List[FloatEntry] = []
    seen: Set[Tuple[str, str, str]] = set()
    for entry in entries:
        key = (entry.kind, entry.number, entry.caption)
        if key in seen:
            continue
        seen.add(key)
        result.append(entry)
    return result


def _build_manifest(
    result: RunResult,
    started: float,
) -> Dict[str, object]:
    counts = Counter(entry.kind for entry in result.entries)
    if not result.entries:
        counts = Counter()

    float_records = []
    for entry in result.entries:
        if entry.pdf_page is None:
            continue
        float_records.append(
            {
                "type": entry.kind,
                "number": entry.number,
                "caption": entry.caption,
                "label": entry.label,
                "printed_page": entry.printed_page,
                "pdf_page": entry.pdf_page + 1,
                "pdf_pages": [page + 1 for page in entry.pages],
                "page_count": len(entry.pages),
                "page_label": entry.page_label,
                "resolution": entry.resolution,
                "verified": entry.verified,
                "note": entry.note,
            }
        )

    return {
        "tool": "extract_float_pages.py",
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "duration_seconds": round(time.time() - started, 3),
        "selection": result.selection,
        "only": result.only_filter or None,
        "output_form": result.output_form,
        "source_pdf": str(result.pdf_path),
        "source_pages": result.total_pdf_pages,
        "output_dir": str(result.out_dir),
        "counts": {
            "tables": counts.get("table", 0),
            "figures": counts.get("figure", 0),
            "unique_pages": len(result.unique_pages),
            "outputs": len(result.outputs),
        },
        "floats": float_records,
        "pages": [index + 1 for index in result.unique_pages]
        if result.selection in ("pages", "all")
        else None,
        "page_labels": result.page_labels if result.selection in ("pages", "all") else None,
        "bundles": [_display(path) for path in result.bundles],
        "warnings": result.warnings,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="extract_float_pages.py",
        description=(
            "Extract the pages containing tables and/or figures from the thesis "
            "build PDF. Uses main.lof/main.lot (and PDF named destinations) first; "
            "only scans the PDF when metadata is missing."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  python extract_float_pages.py                 # PNG images\n"
            "  python extract_float_pages.py --form pdf      # PDFs\n"
            "  python extract_float_pages.py -w tables\n"
            "  python extract_float_pages.py -w tables --only 14\n"
            "  python extract_float_pages.py -w tables --only \"1,14,15\"\n"
            "  python extract_float_pages.py -w figures --form both --dpi 300\n"
            "  python extract_float_pages.py -w pages -p \"36,52,66-70\"\n"
            "  python extract_float_pages.py -w pages -p \"51,67\" --numbering physical\n"
            "  python extract_float_pages.py -w all\n"
            "  python extract_float_pages.py --dry-run -v\n"
        ),
    )
    parser.add_argument(
        "-w",
        "--what",
        choices=sorted(MODE_ALIASES),
        default=None,
        help="What to extract: tables, figures, both/floats, pages, or all.",
    )
    parser.add_argument(
        "-p",
        "--pages",
        metavar="SPEC",
        default=None,
        help="Page list for -w pages: '36,52,66-70' or 'all' (1-based).",
    )
    parser.add_argument(
        "--only",
        metavar="SPEC",
        default=None,
        help=(
            "Only these float numbers, e.g. '14', '1,14,15' or '14-16'. "
            "Works with -w tables/figures/both (not with pages/all)."
        ),
    )
    parser.add_argument(
        "--numbering",
        choices=("printed", "physical"),
        default="printed",
        help=(
            "Interpret -p pages as printed thesis page labels (default) or "
            "physical PDF page numbers."
        ),
    )
    parser.add_argument(
        "--pdf",
        metavar="PATH",
        default=None,
        help=f"Source PDF (default: {_display(DEFAULT_PDF)}).",
    )
    parser.add_argument(
        "-o",
        "--out",
        metavar="DIR",
        default=None,
        help=f"Output directory (default: {_display(DEFAULT_OUT)}).",
    )
    parser.add_argument(
        "--form",
        "--format",
        dest="form",
        choices=("img", "image", "png", "pdf", "jpg", "jpeg", "both"),
        default="img",
        help=(
            "Final output format: img/png (default), pdf, jpg, or both "
            "(PDF + PNG)."
        ),
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=200,
        help="Rasterization DPI for image forms (default: 200).",
    )
    parser.add_argument(
        "--lof",
        metavar="PATH",
        default=None,
        help="Override the .lof sidecar path.",
    )
    parser.add_argument(
        "--lot",
        metavar="PATH",
        default=None,
        help="Override the .lot sidecar path.",
    )
    parser.add_argument(
        "--no-bundle",
        action="store_true",
        help="Do not create combined _all_*.pdf bundles.",
    )
    parser.add_argument(
        "--no-overwrite",
        action="store_true",
        help="Keep existing output files instead of replacing them.",
    )
    parser.add_argument(
        "--no-deep-scan",
        action="store_true",
        help="Never fall back to a full caption scan for unresolved floats.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Resolve and print the plan without writing files.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the machine-readable manifest to stdout.",
    )
    parser.add_argument(
        "--fail-on-empty",
        action="store_true",
        help="Exit with status 4 when nothing matched.",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose logging.")
    parser.add_argument("-q", "--quiet", action="store_true", help="Only warnings/errors.")
    return parser


def _print_summary(result: RunResult, dry_run: bool) -> None:
    kind_counts = Counter(entry.kind for entry in result.entries)
    print()
    print("=" * 68)
    print("  FLOAT PAGE EXTRACTION")
    print("=" * 68)
    print(f"  Source   : {_display(result.pdf_path)} ({result.total_pdf_pages} pages)")
    print(f"  Mode     : {result.selection}")
    if result.only_filter:
        print(f"  Only     : {result.only_filter}")
    print(f"  Format   : {result.output_form}")
    if result.selection in ("tables", "figures", "both"):
        print(
            f"  Found    : {kind_counts.get('table', 0)} table(s), "
            f"{kind_counts.get('figure', 0)} figure(s)"
        )
    print(f"  Pages    : {len(result.unique_pages)} unique page(s)")
    if result.selection in ("pages", "all") and result.page_labels:
        preview = ", ".join(result.page_labels[:12])
        if len(result.page_labels) > 12:
            preview += ", ..."
        print(f"  Labels   : {preview}")
    print(f"  Output   : {_display(result.out_dir)}")
    if dry_run:
        print("  Dry run  : no files written")
    if result.manifest_path:
        print(f"  Manifest : {_display(result.manifest_path)}")
    print("=" * 68)
    if result.bundles:
        print("  Bundles:")
        for bundle in result.bundles:
            print(f"    - {_display(bundle)}")
    if result.warnings:
        print("  Warnings:")
        for warning in result.warnings:
            print(f"    ! {warning}")
    print()


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    _configure_logging(args.verbose, args.quiet)

    # --pages without --what implies pages mode.
    if args.what is None:
        args.what = "pages" if args.pages else "both"
    if args.pages and MODE_ALIASES[args.what] != "pages":
        parser.error("--pages can only be used with -w pages (or without -w).")
    if MODE_ALIASES[args.what] == "pages" and not args.pages:
        parser.error("-w pages requires --pages, e.g. -p '36,52,66-70'.")
    if args.only and MODE_ALIASES[args.what] in ("pages", "all"):
        parser.error("--only can only be used with -w tables, -w figures, or -w both.")
    if args.only:
        try:
            _parse_only_spec(args.only)
        except ValueError as exc:
            parser.error(str(exc))

    if args.dpi < 50 or args.dpi > 1200:
        parser.error("--dpi must be between 50 and 1200.")

    try:
        result = _run(args)
    except FileNotFoundError as exc:
        LOG.error("%s", exc)
        return 3
    except (ValueError, RuntimeError) as exc:
        LOG.error("%s", exc)
        return 2
    except Exception as exc:  # pragma: no cover - defensive
        LOG.error("Unexpected failure: %s", exc, exc_info=args.verbose)
        return 1

    if args.json:
        # Reconstruct the same manifest shape that was written to disk.
        manifest_path = result.manifest_path
        if args.dry_run or manifest_path is None:
            print(json.dumps(_build_manifest(result, time.time()), indent=2))
        else:
            print(manifest_path.read_text(encoding="utf-8"))
    else:
        _print_summary(result, args.dry_run)

    if args.fail_on_empty and not result.outputs and not result.unique_pages:
        return 4
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:  # e.g. piping --json into `head`
        try:
            sys.stdout.close()
        except OSError:
            pass
        sys.exit(0)
