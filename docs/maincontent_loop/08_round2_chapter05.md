# Main-content loop — Round 2, Chapter V review (fresh re-review)

Reviewer: independent re-review of the CURRENT files (after Round 1
fixes). No repo files edited (one extra xelatex pass was run in
the build COPY only, see M6). Final build: 127 pages, A4, 0 `??`
in the PDF text.

## MUST-FIX: none

Table 5.1 verified in detail: caption above (line 139), label
immediately after (line 140), Table 5.1 sequential; widths
0.21/0.17/0.14/0.19/0.14 sum 0.85 \textwidth = 368.2 pt + 60 pt
tabcolsep = 428.2 pt inside 433.13 pt; log confirms no overfull
in lines 141–159; visually the right rule ends exactly at the
body margin (max content x1 = 523.28 pt); every row exactly 5
cells; note present in the Chapter III/IV pattern; both
\ref{tab:hyp_decisions} uses resolve.

## MINOR (disposition)

- M1: 15 body overfulls, largest 27.36 pt (ESG paragraph, lines
  238–240) — RECORDED, document-wide tolerance decision only.
- M2: header hyphenation ("Hypothe-sis", "Param-eter",
  "Hypoth-esis") and justified stretching in Table 5.1 cells —
  COSMETIC per reviewer, but the parent will fix it in Round 2
  fixes the same way as Table 4.5: raggedright p-columns. The
  headers fit their columns at word boundaries once ragged
  (widest header word "Hypothesis" ~55 pt < 91 pt first column;
  "Parameter" ~50 pt < 74 pt second; "Hypothesis" < 61 pt
  third; "Empirical" ~55 pt < 61 pt fifth), so raggedright
  removes the hyphenation with no downside. Verify by compile
  + visual after the change.
- M3: notation variants (plain MPS, $F$ without df, rounded
  5.58/0.10/2.45/-1.66 vs full precision, unspaced $H_0$,
  math-vs-text %) — NOTATION PASS.
- M4: hardcoded section numbers, all correct — document-wide
  style note, no action.
- M5: local \captionsetup duplicate — FLOATS CLEANUP PASS.
- M6: build-pass observation — the 3-pass build log ends with
  "Label(s) may have changed" (longtable width stabilization);
  one extra xelatex pass in the copy cleared it with page count
  unchanged at 127. CONSEQUENCE: the loop's final verification
  build must use 4 xelatex passes (script + 1), not 3, and the
  build script should be updated to 4 passes for future runs.

## Out of scope, noted for the appendices phase
Two large overfulls after the Chapter V block in the log
(76.57 pt and 62.19 pt, appendix lines 14–55) belong to the
appendices, not this chapter. They are the first known targets
of the appendices + references phase, not Round 2 main-content
fixes.

## Round 2 fix applied by parent (M2) + verification
- Table 5.1 spec changed to raggedright p-columns (same widths).
  Rebuilt with the updated 4-pass build script: 127 pages, 0
  errors, 0 undefined references, 0 "Label(s) may have changed"
  warnings, no overfull in lines 141–159. Visual check (PDF
  p. 112): headers now break at word boundaries only
  ("Research / Hypothesis", "Model / Parameter", "Null /
  Hypothesis", "Estimate (SE) / Stat.", "Empirical /
  Decision"), no mid-word hyphenation; margins and note intact.
  M2 is therefore CLOSED, not merely cosmetic-accepted.

## PASSES (Round 2, accepted)
Headings (5.1–5.5 + subsections, no skip); lists balanced;
equations auto-numbered (Model 1, Model 2 aligned, R6 Wald), no
dangling refs; all 16 citation keys resolve; hardcoded
formatting only in the table block; braces 219/219, dollars
310 even, all environments balanced.
