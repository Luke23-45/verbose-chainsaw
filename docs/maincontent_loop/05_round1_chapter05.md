# Main-content loop — Round 1, Chapter V review (reviewer report + disposition)

Reviewer: per-chapter format review, no files edited. Parent
verified F1 arithmetic against the table spec and log.

## MUST-FIX

### F1 — Table 5.1 exceeds the text width by ~16.5 pt
- Lines 135–165; tabular spec line 142: five p-columns summing
  0.90 \textwidth = 389.8 pt, plus 60 pt tabcolsep = 449.8 pt
  against a 433.13 pt text width.
- Log: `Overfull \hbox (16.51483pt too wide) lines 141--159`;
  PDF p. 109: right rule ~16 pt past the body margin; header
  words hyphenate badly ("Hypothe-sis", "Parame-ter",
  "Hypoth-esis", "De-cision") and justified cells stretch.
- Fix: narrow the five widths to sum 0.85 \textwidth
  (0.21/0.17/0.14/0.19/0.14 → 368.2 + 60 = 428.2 pt, inside
  433.13 pt), keeping all content and the \small size. Do not
  just shrink the font.

## MINOR (disposition)

- M1 — 15 body overfulls (largest 27.36 pt, lines 238–240 ESG
  paragraph). RECORDED, not fixed by rewording; same
  document-wide tolerance decision as Chapter IV m5, to be
  evaluated after the table fixes.
- M2 — Notation variants (plain MPS line 24 vs math line 127;
  $F$ without df line ~114; table $F(2,10) = 5.818$ vs text 5.82;
  $\hat{\beta}_E = 5.58$ vs 5.577; unspaced $H_0$ in table;
  $94.8\%$ math vs 33.80\% text). NOTATION PASS.
- M3 — Hardcoded section numbers (lines 8–11, 113, 133;
  "Section~5.2" etc., "Chapter~I"). Correct today. DEFERRED
  style note (document-wide, same as Chapter IV's 16 ×
  "Section~" literals); converting to \ref requires checking
  that every section carries a label first.
- M4 — Local \captionsetup line 138 identical to global.
  FLOATS CLEANUP PASS (document-wide).

## Passes (reviewer, accepted)

Caption above tabular, label after caption, Table 5.1 sequential
(only table; LOT entry matches); booktabs rules present;
\addlinespace groups; every row exactly 5 cells; note present
with the Chapter III/IV pattern and ending at the correct
margin; headings 5.1–5.5 with subsections, no skip; lists
balanced (12 enumerate + 6 itemize); equations auto-numbered
(Model 1, Model 2 aligned, R6 Wald), no dangling equation refs;
\ref{tab:hyp_decisions} ×2 resolves; all 16 citation keys
resolve; hardcoded formatting only in the table block; braces
219/219, all environments balanced.
