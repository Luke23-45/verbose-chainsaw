# Main-content loop — Round 1, Chapter IV review (reviewer report + disposition)

Reviewer: per-chapter format review, no files edited. Parent verified
MF1, MF2, MF4 (including TOC) against source, log, and compiled PDF.

## MUST-FIX

### MF1 — Undefined reference `tab:model2_vr` renders as "??"
- Line 296 (Figure 3 note, fig:value_relevance): "not the two-way
  fixed-effects estimates in Table~\ref{tab:model2_vr}".
- Grep-verified: `tab:model2_vr` occurs ONLY at line 296; no such
  label exists anywhere. Compile log: "Reference 'tab:model2_vr'
  on page 70 undefined". This is the thesis's one undefined ref.
- Intended target CONFIRMED by parent: `tab:t4_model2` (line 226),
  the Model 2 table ("Model 2: Value Relevance Regime Shift
  Across Consolidation"), described at line 219 as the Model 2
  estimation results. Fix: change the line-296 reference to
  `tab:t4_model2`. No other change.

### MF2 — Table 4.4 declares 7 columns, every row has 6 cells
- Line 227: `\begin{tabular}{lcccccc}` (7 columns); header line
  229 has 6 cells; section rows use `\multicolumn{6}{l}` and
  diagnostics rows `label & \multicolumn{5}{c}` (= 6). LaTeX pads
  a phantom empty 7th column. Fix: spec to `lccccc` (6 columns).
  This also removes part of Table 4.4's 18 pt overfull.

### MF3 — Six of eight tables wider than the text width (433 pt)
Log-corroborated overfulls, all from unwrappable centered `c`
columns holding full sentences:
- Table 4.3 Model 1 (lines 177–192): +52.30 pt.
- Table 4.4 Model 2 (lines 227–252): +18.00 pt (partly MF2).
- Table 4.5 Hypotheses (lines 325–338): +172.82 pt — `Inference`
  column holds sentences ("Positive slope; insignificant under
  $t(16)$." etc.).
- Table 4.6 Robustness (lines 375–389): +105.77 pt.
- Table 4.7 Diagnostics (lines 434–444): +49.51 pt.
- Table 4.8 Specification comparison (lines 482–491): +237.41 pt
  — `Assessment` column holds sentences ("Rigorously absorbs
  bank and year shocks; preferred benchmark." etc.).
- Tables 4.1 and 4.2 fit (no overfull). Fix: rework column types
  to wrapping p-columns with widths summing ≤ 0.86 \textwidth
  (plus tabcolsep ≤ text width); shrinking font alone cannot
  close a 237 pt gap. Per-table widths to be set at fix time
  from the actual cell contents, then compile-verified.

### MF4 — Chapter headings render Arabic, thesis prose uses Roman
- Body headings render `CHAPTER 4 / RESULTS AND DISCUSSION`
  (all five chapters render CHAPTER 1–5); prose uses `Chapter~I`
  … `Chapter~IV` throughout.
- CORRECTION to the Chapter I reviewer's note: the TOC does NOT
  render Roman. Verified in the compiled PDF: TOC line reads
  `CHAPTER 1: Introduction`. Both body (preamble line 73:
  `\MakeUppercase{\chaptertitlename\ \thechapter}`) and TOC
  (line 98: `\thecontentslabel`) use Arabic `\thechapter`.
- Fix scope (reviewer's warning respected): do NOT apply a bare
  global `\renewcommand{\thechapter}{\Roman{chapter}}`, which
  would renumber sections (IV.1), tables, figures, and equations
  and break `Section~4.x` references. The Roman form must reach
  the body title label AND the TOC chapter line while sections
  (4.1), tables (4.1), figures (4.1), and equations (4.1) stay
  Arabic and appendix headings stay Alph. Implementation to be
  verified at fix time by compile: body titleformat label to
  `\Roman{chapter}`, TOC chapter line to Roman, with explicit
  Arabic counter definitions for section/table/figure/equation
  and Alph handling in the appendix block.

## MINOR (disposition)

- m1 — Introduction Results list titles mismatch actual subsection
  titles (4 of 7, lines 10–16 vs 162/207/312/364). FIX in Round 1:
  align the intro list items verbatim to the actual subsection
  headings (headings are the source of truth; Discussion list
  lines 21–25 is prose, not flagged, left alone).
- m2 — Local \captionsetup repeated in all 8 tables, absent from
  figures. DEFERRED to the document-wide floats cleanup pass
  (removal + compile diff), not a Chapter IV-only edit.
- m3 — Caption N inconsistency (Tables 4.2/4.3/4.4 carry
  `(N = 28)`; 4.1/4.5/4.6/4.7/4.8 leave it to the note; trends
  figure note lacks explicit N). DEFERRED to the
  notation/consistency pass.
- m4 — Table 4.2 header: $\mathit{MPS}^{RD}$ is the only header
  not wrapped in \textbf. FIX in Round 1: wrap it, matching EPS/
  BVPS/DPS/ROA headers.
- m5 — Body overfulls (two ~30 pt: lines 79–80, 274–275; rest
  ≤ 17 pt). RECORDED, not fixed by rewording. Document-wide
  tolerance decision (e.g. emergencystretch) to be evaluated
  after the table fixes, with a compile check.
- m6 — Notation micro-variants (unspaced +, $F=2.95$ without df,
  $\delta_{ROA}$ form, bare $\mathit{MPS}$ line 550, unhatted
  table parameters vs hatted prose). NOTATION PASS, not Round 1.
- m7 — \subsubsection at line 473 is TOC-orphaned (tocdepth 2).
  KEPT as-is unless the campus requires deeper TOC; text cites
  the parent Section 4.2.7 correctly. Not a defect to fix
  unilaterally (changing tocdepth changes the whole TOC).
- m8 — Figure widths 0.92/0.88/0.72, all ≤ text width, no figure
  overfull. OBSERVATION only; 0.72 heatmap plausibly
  aspect-driven. No change (floats pass may document the
  pattern).
- m9 — Figure notes carry codebase-asset tags; table notes do
  not. MINOR, deferred to consistency pass (tags are internal
  provenance, not reader-facing content; removing them is a
  content decision, not format).
- m10 — Model-table header naming differs (4.3 separate Parameter
  / Coefficient; 4.4 merged "Model Parameter / Term"). MINOR,
  consistency pass.
- m11 — Loose note lines (underfull, badness 1178–2538, lines
  308–309, 469–470). COSMETIC, no action.

## Passes (reviewer, accepted)

Caption position correct for all 15 floats (tables above,
figures below); labels immediately after captions (15/15);
numbering sequential, no hardcoded Table/Figure numbers; all
floats `[!htbp]`, first referenced before their environment;
all labels resolve except MF1; no duplicate labels; all 20
citation keys resolve; notes present on all 15 floats with
consistent \vspace (4pt tables, 2pt figures); \small tables,
\footnotesize notes, \centering everywhere; environments
balanced; braces 647/647; equations well-formed (Model 1, Model 2
aligned, Ohlson, Wald); all 7 figure PDFs exist and the asset
map matches.
