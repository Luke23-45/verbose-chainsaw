"""Robust NFRS statement parser, built from the actual PDFs.

Key facts from inspection (all five banks, FY 2080/81 pilot):
- Columns, in order: Group current, Group previous, Bank current,
  Bank previous. Verified from statement headers, not assumed.
- Note numbers are language-independent: SOFP 4.1-4.28, SOPL
  4.29-4.41. NIMB writes 4.01/4.02, normalised to 4.1/4.2 here.
  This makes the parser work on Nepali editions (Kumari, NMB
  Nepali) where labels are in a legacy font.
- Some PDFs are two printed pages per PDF page (Global IME:
  1190pt wide). Those are split at the midpoint before row
  reconstruction, or left/right rows merge into 8-number rows.
- Labels wrap across lines; subtotal rows sometimes repeat each
  number twice in the word stream. Both are handled.
- EPS/NAV rows are small decimals with a decimal point; date
  header rows (31, 2081) are integers and must never be mistaken
  for EPS.
- Nothing is guessed: a target not found is reported missing.
"""

from __future__ import annotations

import re
from pathlib import Path

try:
    import pymupdf as fitz
except ImportError:  # pragma: no cover
    import fitz  # type: ignore

NUM_RE = re.compile(r"^\(?[\d,]+(\.\d+)?\)?$")
NOTE_RE = re.compile(r"^4\.\d{1,2}$")


def _norm_note(tok: str) -> str | None:
    if not NOTE_RE.match(tok):
        return None
    head, frac = tok.split(".")
    return f"{head}.{int(frac)}"


def _is_number(tok: str) -> bool:
    return tok in ("-", "--") or bool(NUM_RE.match(tok))


def _parse_number(tok: str) -> float | None:
    if tok in ("-", "--"):
        return None
    neg = tok.startswith("(") and tok.endswith(")")
    try:
        val = float(tok.strip("()").replace(",", ""))
    except ValueError:
        return None
    return -val if neg else val


def word_rows(page) -> list[str]:
    """Reconstruct rows by y-coordinate, splitting spread pages."""
    words = page.get_text("words")
    width = page.rect.width
    halves = [0, 1] if width > 900 else [0]
    rows: list[str] = []
    for half in halves:
        if width > 900:
            mid = width / 2
            ws = [w for w in words if (w[0] < mid) == (half == 0)]
        else:
            ws = words
        clusters: dict[int, list] = {}
        for w in ws:
            clusters.setdefault(round(w[1] / 3) * 3, []).append(w)
        for y in sorted(clusters):
            ordered = sorted(clusters[y], key=lambda w: w[0])
            rows.append(" ".join(w[4] for w in ordered))
    return rows


def join_rows(rows: list[str]) -> list[dict]:
    """Join wrapped labels to the row carrying their numbers."""
    out: list[dict] = []
    buffer: list[str] = []
    pending_note: str | None = None
    for row in rows:
        toks = row.split()
        note = None
        kept: list[str] = []
        for t in toks:
            n = _norm_note(t)
            if note is None and n is not None:
                note = n
            else:
                kept.append(t)
        toks = kept
        num_toks = [t for t in toks if _is_number(t)]
        if not num_toks:
            if any(c.isalpha() for c in row) and len(row.strip()) > 1:
                # A wrapped label may itself carry the note
                # ("Income Tax Expense 4.41" on its own line).
                if note is not None:
                    pending_note = note
                buffer.append(" ".join(kept).strip())
            continue
        if note is None:
            note = pending_note
        pending_note = None
        first_num = next(i for i, t in enumerate(toks) if _is_number(t))
        label = " ".join(buffer + toks[:first_num]).strip()
        buffer = []
        nums = [_parse_number(t) for t in num_toks]
        if len(nums) == 8 and nums[0] == nums[1] and nums[2] == nums[3] \
                and nums[4] == nums[5] and nums[6] == nums[7]:
            nums = [nums[0], nums[2], nums[4], nums[6]]
        out.append({"label": label, "note": note, "numbers": nums,
                    "raw": row, "has_decimal": any("." in t and not t.startswith("4.") for t in num_toks)})
    return out


def _is_total_label(label: str) -> bool:
    low = label.lower()
    return ("total" in low or "s'n" in low or 's"n' in low
            or "hDdf" in low or "k\"n" in low)


def _is_nci_label(label: str) -> bool:
    low = label.lower()
    return "non" in low or "lgolGqt" in low or "u}/" in low


def _find_total(rows: list[dict], after_note: str) -> dict | None:
    """First no-note 4-number row after after_note.

    In SOFP sections that row is the total by construction: every
    component row carries its note, the total row does not. Label
    wording varies by language and font (Total / s'n / hDdf), so
    position, not label, is the anchor here.
    """
    started = False
    for r in rows:
        if r["note"] == after_note:
            started = True
            continue
        if started and r["note"] is None and len(r["numbers"]) == 4:
            return r
    return None


def page_rows(page) -> list[str]:
    """Choose the row reconstruction that actually yields statements.

    Word-coordinate rows win on normal pages and on spreads.
    Plain text lines win on pages whose word geometry is broken
    (e.g. NMB FY 2076/77, where word rows merge columns into
    17-number rows while the text layer is clean).
    """
    def score(rows: list[str]) -> int:
        joined = join_rows(rows)
        good = sum(1 for r in joined if r["note"] and len(r["numbers"]) == 4)
        bad = sum(1 for r in joined if len(r["numbers"]) > 6)
        return good * 10 - bad * 20 + sum(1 for r in joined if len(r["numbers"]) == 4)

    word = word_rows(page)
    text = [ln for ln in page.get_text().splitlines() if ln.strip()]
    if score(text) > score(word):
        return text
    return word


def _row_by_note(rows: list[dict], note: str) -> dict | None:
    for r in rows:
        if r["note"] == note and len(r["numbers"]) == 4:
            return r
    return None


def _bank_group(row: dict | None) -> dict:
    if row is None:
        return {"group_current": None, "group_previous": None,
                "bank_current": None, "bank_previous": None}
    n = row["numbers"]
    if len(n) == 2:
        # Bank-only row (Global IME prints EPS/NAV for Bank only).
        return {"group_current": None, "group_previous": None,
                "bank_current": n[0], "bank_previous": n[1]}
    return {"group_current": n[0], "group_previous": n[1],
            "bank_current": n[2], "bank_previous": n[3]}


def extract_bank_year(pdf_path: Path) -> dict:
    doc = fitz.open(pdf_path)
    # Row stream from the first SOFP page onward, in reading order.
    stream: list[dict] = []
    stream_pages: list[int] = []
    started = False
    for i, page in enumerate(doc, start=1):
        text = page.get_text()
        if "interim" in text.lower() and "condensed" in text.lower():
            continue
        rows = join_rows(page_rows(page))
        if not started:
            notes = {r["note"] for r in rows if r["note"]}
            # Audited SOFP first page carries 4.1 and 4.2 together
            # plus several more asset notes. Summary tables and
            # note-detail pages do not (GBIME FY 2077/78, NMB
            # FY 2077/78). 4.3 itself may be wrapped onto a
            # fragment line in Nepali editions, so it is not
            # required individually.
            if {"4.1", "4.2"} <= notes and len(notes) >= 5:
                started = True
            else:
                continue
        for r in rows:
            r = dict(r)
            r["page"] = i
            stream.append(r)
        stream_pages.append(i)
        # Stop once SOPL EPS is in the stream.
        if any(r["note"] == "4.29" for r in rows) and any(
                "earnings per share" in r["label"].lower() or
                "earning per share" in r["label"].lower() for r in stream):
            break
        if len(stream_pages) >= 8:
            break

    # Split stream at SOPL start (first 4.29 row).
    sopl_idx = next((i for i, r in enumerate(stream) if r["note"] == "4.29"), None)
    sofp_rows = stream[:sopl_idx] if sopl_idx is not None else stream
    sopl_rows = stream[sopl_idx:] if sopl_idx is not None else []

    total_assets = _find_total(sofp_rows, "4.16")
    total_liab = _find_total(sofp_rows, "4.25")
    # Equity attributable: after reserves (4.27), the first
    # no-note 4-number row. That is attributable by position;
    # NCI and Total Equity follow it.
    equity_attr = _find_total(sofp_rows, "4.27")
    total_equity = None
    if equity_attr is not None:
        idx = sofp_rows.index(equity_attr)
        for r in sofp_rows[idx + 1:]:
            if r["note"] is None and len(r["numbers"]) == 4:
                if _is_nci_label(r["label"]):
                    continue
                # Liabilities+Equity (= total assets) ends the equity
                # section: if we reach it, there is no separate
                # Total Equity row (NCI is zero), so stop.
                if total_assets and r["numbers"] == total_assets["numbers"]:
                    break
                total_equity = r
                break
        if total_equity is None:
            # Total Equity row may print only Group numbers
            # (Global IME) or equal attributable when NCI is zero:
            # in both cases Bank total equity = Bank attributable.
            total_equity = equity_attr
    share_cap = _row_by_note(sofp_rows, "4.26")

    # EPS: first row with 'earnings per share' in label and 4 decimal
    # numbers, or, for Nepali, first decimal row after profit rows.
    eps_row = None
    for r in sopl_rows:
        low = r["label"].lower()
        if "earnings per share" in low or "earning per share" in low:
            if len(r["numbers"]) in (2, 4) and r["has_decimal"]:
                eps_row = r
                break
    if eps_row is None:
        # Nepali EPS: decimal row after the profit section, before
        # any statement-of-comprehensive-income repeat.
        for r in sopl_rows:
            if len(r["numbers"]) in (2, 4) and r["has_decimal"] and all(
                    v is not None and abs(v) < 200 for v in r["numbers"]):
                eps_row = r
                break

    # Profit: first profit-labelled row after tax note 4.41, then
    # the attributable row after it.
    pat = None
    attributable = None
    if sopl_rows:
        after_tax = False
        profit_rows = []
        for r in sopl_rows:
            if r["note"] == "4.41":
                after_tax = True
                continue
            if not after_tax:
                continue
            low = r["label"].lower()
            if len(r["numbers"]) == 4 and (
                    "profit" in low or "d'gfkmf" in low or "gfkmf" in low):
                # Exclude tax sub-rows and comprehensive-income repeats
                # that appear after EPS.
                if eps_row is not None and r is eps_row:
                    break
                profit_rows.append(r)
        # PAT is the first profit row; attributable is the next profit
        # row containing an attributable marker, else PAT itself.
        if profit_rows:
            pat = profit_rows[0]
            attributable = pat
            for r in profit_rows[1:]:
                low = r["label"].lower()
                if "attributable" in low or "aFf8kFmf8" in low or "equity holders" in low:
                    attributable = r
                    break

    # NAV per share: small row in SOFP after total equity section.
    # NIMB prints it as integers (178, 165), others as decimals.
    nav = None
    for r in reversed(sofp_rows):
        if len(r["numbers"]) in (2, 4) and all(
                v is not None and abs(v) < 1000 for v in r["numbers"]):
            low = r["label"].lower()
            if "per share" in low or "value" in low or "v'b" in low:
                nav = r
                break

    return {
        "source_file": str(pdf_path),
        "sofp_pages": sorted({r["page"] for r in sofp_rows}),
        "sopl_pages": sorted({r["page"] for r in sopl_rows}),
        "total_assets": _bank_group(total_assets),
        "total_liabilities": _bank_group(total_liab),
        "total_equity_attributable": _bank_group(equity_attr),
        "total_equity": _bank_group(total_equity),
        "share_capital": _bank_group(share_cap),
        "profit_after_tax": _bank_group(pat),
        "profit_attributable": _bank_group(attributable),
        "eps_reported": _bank_group(eps_row),
        "nav_per_share_reported": _bank_group(nav),
        "eps_label": eps_row["label"] if eps_row else None,
        "pat_label": pat["label"] if pat else None,
    }
