# Main-content loop — Round 2, Chapter III review (fresh re-review)

Reviewer: independent re-review of the CURRENT files (after Round 1
fixes). No files edited. Compile evidence: 0 LaTeX errors,
0 undefined references, 0 "Float too large" warnings. Both floats
rendered and visually inspected (PDF pp. 61, 64).

## MUST-FIX: none

- Figure 3.1 caption BELOW the diagram (FOM-correct), source
  order verified (tikzpicture → caption → label → end figure);
  rendered p. 64 confirms the bold caption under the diagram.
- Figure 3.1 geometry CLEAN on independent visual inspection:
  all five boxes and both labels render without overlap —
  "Fundamental Independent Variables" clear above the Fixed
  Effects Control box (the Round 1 overlap fix confirmed by
  fresh eyes), "Dependent Variable" clear below MPS,
  "Moderating / Interaction Effect" clear above Post; arrow
  labels adjacent to, not struck through by, the arrows; no
  overfull in the figure region.
- Table 3.1 FOM-correct and fits: caption above (line 104),
  label immediately after, complete title; all 6 data rows
  exactly 7 cells against `llccccc`; rendered p. 61 inside
  both margins with the note below; footnote markers ^a–^d
  all explained; no overfull in the table region.
- Zero dangling references: tab:mps_rd, fig:framework,
  Section 3.3.4, Section 2.2.6 (Chapter II line 151) all
  resolve; all 11 citation keys resolve; all 9 labels defined
  here occur exactly once thesis-wide.
- Quote single-spacing PASS: the thesis's only \begin{quote}
  (line 86) is covered by preamble line 47
  (\AtBeginEnvironment{quote}{\singlespacing}); verified
  thesis-wide no other quote block exists.

## MINOR (all deferred, none a Chapter III fix)

- m-1: Table 3.1 caption plain $MPS^{RD}$ vs body
  $\mathit{MPS}^{RD}$ (7×) — NOTATION PASS.
- m-2: $N = 28$ (5×) vs $n = 28$ (5×; Round 1 counted 6× — the
  notation pass will grep the exact count) — NOTATION PASS
  (convention: N totals, n subsamples).
- m-3: seven labelled equations never cross-referenced — KEPT
  (dead labels, not dangling).
- m-4: local \captionsetup duplicates (lines 103, 175) —
  FLOATS CLEANUP PASS.
- m-5: body overfulls 0.27–10.02 pt, none in floats —
  RECORDED, tolerance decision only.
- m-6: P/E identity upright typeface (line 253) vs
  $\mathit{…}$ forms elsewhere — NOTATION PASS (note: the
  `=` form here, not `≡`, consistent within the chapter).
- m-7: bank-profile sub-list lengths (4/4/4/4/2) — NOT a
  defect (benchmark bank content).

## PASSES (Round 2, accepted)
Headings (3.1–3.6, subsections, subsubsections only under
3.5.2; roadmap titles match verbatim); lists balanced with
consistent lead-ins, including the new bold lead-in at line
253; equations numbered 3.1–3.13 sequentially; hardcoded
formatting all justified except m-4; braces 398/398, all
environments balanced, $ parity per line.
