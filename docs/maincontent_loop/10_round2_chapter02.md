# Main-content loop — Round 2, Chapter II review (fresh re-review)

Reviewer: independent re-review of the CURRENT files (after Round 1
fixes). No files edited by the reviewer. Compile evidence:
127 pages, A4; log segment isolated by file-open markers.

## MUST-FIX: none

Table 2.1 verified end to end by the reviewer:
- Longtable with repeated header (lines 302–311); caption is the
  first row; label immediately after caption (lines 304–305).
- Columns fit: 0.85 \textwidth = 368.2 pt + 60 pt tabcolsep =
  428.2 pt inside 433.13 pt; zero overfull in lines 302–356;
  no "Float too large" anywhere.
- No rows lost: all 22 rows print — caption + first rows on
  PDF p. 49 (Pradhan 2003 through Pradhan 2016), continuation
  p. 50 (Bajracharya through Pant 2024), final rows p. 51
  (Chaudhari, Dahal, Gurung & Dahal, Timalsina, Bhandari,
  Adhikari); header repeats on pp. 49, 50, 51; note follows the
  final row on p. 51; Research Gap starts p. 52.
- Margins respected: pure table page p. 50 max word right edge
  514.7 pt vs 523.3 pt body edge (the one word past the margin
  on p. 49, "frame-", belongs to body prose, see M1).
- Note present (lines 359–363) in the chapters' table-note
  pattern; LOT entry resolves.
- Headings: chapter → 5 sections → subsections only, runs
  continuous (2.2.1–2.2.6, 2.3.1–2.3.3, 2.4.1–2.4.5,
  2.5.1–2.5.5); body "CHAPTER II" (PDF p. 30) and TOC
  "CHAPTER II:" (p. 6) consistent with prose.
- Lists: all five enumerates now carry the identical bold-label
  option (lines 27, 108, 186, 204, 284) — BAFIA list fixed.
- Equations: 16 equation + 1 align, balanced, auto-numbered,
  none labelled/cited by number (consistent with other chapters).
- References: all 6 \ref targets and all 55 citation keys
  resolve; zero undefined in the chapter's log segment.
- Footnote line 271 uses \citet after printed names — no
  duplication renders.
- Balance: braces 391/391, environments balanced, 114 `$` even.

## MINOR (disposition)

- M1: body overfulls ≤ 7.31 pt (incl. "frame-" at lines
  298–299) — RECORDED, tolerance decision only.
- M2: justified narrow p-columns stretched word spacing +
  header hyphenation ("Sample & Pe-riod") — FIXED by parent
  in Round 2 fixes: all five longtable columns changed to
  raggedright (widths unchanged), rebuilt (127 pages, 0
  errors, 0 undefined, no longtable overfull), visually
  verified on p. 50: "Sample & Period" intact, "Joshi et
  al." no longer stretched, cells read naturally. M2 CLOSED.
- M3: EY/MTB expansions still unverified (reviewer confirmed
  no expansion exists in thesis or draft) — OPEN CONTENT ITEM
  for Krishna (check against the Dahal paper); not guessed.
- M4: P/E identity `=` (lines 158, 366) vs `\equiv` (line
  289) — NOTATION PASS.
- M5: plain-superscript $MPS^{RD}$ (3×) vs $\mathit{MPS}^{RD}$
  elsewhere — NOTATION PASS.
- M6: local \captionsetup duplicate (line 301) — FLOATS
  CLEANUP PASS.
