# Front-matter loop — Round 6 review (real XeLaTeX compile, loop closes)

Build: full thesis compiled in a copy (workspace/frontmatter_build/
work/) with XeLaTeX → BibTeX → XeLaTeX → XeLaTeX, the only change in
the copy being the main font (Times New Roman is not installed on
this machine, so TeX Gyre Termes, its metric-compatible counterpart,
was substituted). Output: 124 pages, A4, zero LaTeX errors.

## Page-by-page verdict (visually inspected as rendered PNGs)

- p1 Title: one page, title in four centred lines, submission
  sentence, by, name, roll, registration, campus, date at the foot,
  no printed page number. Clean.
- p2 Certification of Authorship: one page, Roman ii, signature block
  with rules. Clean.
- p3 Report of Research Committee: one page, Roman iii. Clean.
- p4 Approval Sheet: one page, Roman iv, 2×2 signatory grid. Clean.
- p5 Acknowledgements: one page, Roman v, signature at the right.
  The Round 4 fit-driven spacing is confirmed by the compile.
- p6–p8 Table of Contents: three pages (generated list, normal).
- p9 List of Tables, p10 List of Figures: one page each.
- p11–p12 List of Abbreviations: TWO pages (p11 ends at P/E, p12
  runs PEAD–VIF with the header repeated). See decision below.
- p13 Abstract: one page, Roman xiii, keywords on the same page.
  The Round 4 fit-driven spacing is confirmed by the compile.
- p14 Chapter I, Arabic page 1. Pagination chain verified end to
  end: i (unprinted) → ii → iii → iv → v → vi–viii → ix → x →
  xi–xii → xiii → 1.

## Decision: abbreviations on two pages is accepted, not fixed

Measured from the PDF, longtable rows run at ≈ 14.75 pt each, not
the 12 pt the Round 5 analytic model assumed, so 48 rows cannot fit
one page at 12 pt. Forcing one page would require shrinking the list
below FOM's uniform 12 pt, or deleting entries that are actually
used — both worse than a two-page list. FOM requires the abstract
to be one page; it imposes no one-page rule on a list, and this
document's own TOC already spans three pages. The repeated header
on page 12 is exactly what longtable is for. Round 5's one-page
claim for this list is corrected here; the list itself is unchanged.

## Noted, not fixed (judgement recorded)

- Front-form overfulls of 3–7 pt on the bold all-caps title lines
  (authorship, research committee, approval sheet): about 1–2.5 mm
  on one line per page, invisible in the rendered pages. The fixes
  available would be worse than the defect — \sloppy would loosen
  spacing across whole paragraphs, and rewording the title is
  forbidden. Left as is.
- One undefined reference, `tab:model2_vr` (Chapter IV, p. 70):
  pre-existing, in a chapter, outside this phase's scope. Recorded
  for a later phase, not touched here.

## Loop status: CLOSED

Rounds 1–6 found and fixed: heading/paragraph consistency where it
did not break fit, signature-rule alignment, tabular blank lines,
abbreviations matched to actual use, and two fit-driven spacing
exceptions that the loop itself first got wrong and then corrected.
The compile review finds no further fixable front-matter defect.
Remaining items are decisions, not defects: commit/push, supervisor
name, title-page name confirmation.
