# Main-content loop — Round 2, Chapter IV review (from scratch, no files edited)

Reviewer: independent re-review of the CURRENT files (after Round 1
fixes). Compile evidence: 127 pages, A4; log from a build newer
than the chapter's mtime. Prose, argument, and numbers not judged.

## MUST-FIX: none

- All 8 tables fit: zero overfulls in any Chapter IV tabular
  range; row-vs-spec count script: zero mismatches (4.1
  `llccccc`, 4.2 `lccccc`, 4.3 `p{0.17\textwidth}cccccc`, 4.4
  `p{0.26\textwidth}ccccc` incl. all `\multicolumn` rows, 4.5
  seven p/c columns, 4.6 seven p/c columns, 4.7
  `p{0.22\textwidth}cccc`, 4.8 six p/c columns).
- Figure-note reference resolves: line 296 now points at
  `tab:t4_model2` (line 226); zero undefined references
  document-wide.
- Roman chapter / Arabic sections, tables, figures verified
  in PDF: body "CHAPTER IV / RESULTS AND DISCUSSION"
  (PDF p. 72), TOC "CHAPTER IV:" (p. 7), sections "4.1",
  "4.2.7", "Table 4.1"–"Table 4.8", "Figure 4.1"–"Figure 4.7".
- Introduction Results list matches all 7 subsection titles
  verbatim; Discussion list is descriptive prose;
  sections 4.3.1–4.3.5 all exist.
- Caption/label placement correct on all 15 floats; figure
  widths 0.92 (×4), 0.88 (×2), 0.72 (×1); all 7 figure PDFs
  exist.
- All 15 `\ref` targets resolve; all 15 floats first
  referenced before their environments; all 20 citation keys
  resolve; no duplicate labels; no `\eqref`.
- Balance: braces 675/675 (naive count shows a false 5-brace
  gap; `\%` and `\{`/`\}` protected); `$` 732, even;
  environments balanced; no TODO, no `??`.

## MINOR (disposition)

- m1 — body overfulls: 31.90 pt (lines 79–80), 30.12 pt
  (274–275), 23.10 pt (332–333), 16.17 pt (heading, line
  514), smaller ones ≤ 8 pt. FIXED by parent in Round 2
  fixes, without any wording change: (a) preamble
  `\emergencystretch` 1em → 2em removed the two ~30 pt
  lines and the Ch I 16.62 pt line; (b) Table 4.5
  rebalanced (Inference 0.12 → 0.17, Hypothesis/Model/
  Decision 0.13/0.12/0.13 → 0.11, total p-width still
  0.61) cut the 23.10 pt "Indistinguishable" overflow to
  1.36 pt; (c) `\sloppy` in the subsection before-code let
  the 4.3.2 title wrap ("Post-" / "Consolidation"),
  removing the 16.17 pt heading overfull. Remaining Ch IV
  overfulls after all three: 3.78 pt, 1.36 pt (≤ 1.3 mm,
  accepted as negligible). Page count unchanged at 127.
  m1 CLOSED except the ≤ 1.3 mm residuals.
- m2 — enumerate label split document-wide (Ch I/II bold,
  Ch III/IV/V plain): NOT a defect, needs one document-wide
  decision — FLAGGED for Krishna in the loop-close report,
  not changed unilaterally.
- m3 — local `\captionsetup` ×8 — FLOATS CLEANUP PASS.
- m4 — caption-N inconsistency (4.2/4.3/4.4 carry N = 28;
  others leave N to the note; trends figure note lacks
  explicit N) — CONSISTENCY PASS.
- m5 — notation micro-variants — NOTATION PASS.
- m6 — `\subsubsection` line 473 invisible in TOC
  (tocdepth 2) — campus decision, KEPT.
- m7 — model-table header naming differs — CONSISTENCY
  PASS.
- m8 — figure-note codebase-asset tags, table notes none
  — CONSISTENCY PASS.
- m9 — hardcoded `Section~4.x` literals (16, all verified
  correct) — CONSISTENCY PASS.
- m10 — local `\tabcolsep` 4pt in Tables 4.6/4.8 only,
  scoped inside their floats, harmless — NOTED.
- m11 — badness-10000 underfulls in Table 4.3/4.4 first
  columns — normal cost of the width fixes, NOT a defect.
