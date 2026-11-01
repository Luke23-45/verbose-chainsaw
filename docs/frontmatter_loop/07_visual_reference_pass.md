# Front-matter visual-reference pass (2026-10-29, after the main-content loop closed)

Krishna's instruction: the pre-Chapter I pages were not acceptable;
make them professional (alignment, spacing, and the rest) using the
downloaded Gurung (2025) MBS dissertation as the visual reference.
Every page below was rendered as a PNG and compared side by side
with the matching reference page. No wording of any front page was
changed except where noted; all fixes are layout.

## Defects found against the reference, and fixes

1. **TOC listed no preliminary pages at all.** The reference TOC
   lists Title Page i through Abstract xi before its chapters;
   ours jumped straight to CHAPTER I. Fixed: every front page
   now registers a TOC entry (Title Page i, Certification ii,
   Research Committee iii, Approval iv, Acknowledgements v,
   Table of Contents vi, List of Tables ix, List of Figures x,
   List of Abbreviations xi, Abstract xiii). Implementation:
   `\addcontentsline` at the top of each front file;
   `\thesisFrontList` now takes the entry text as its first
   argument; Roman numbering now starts before the title page
   so the Title entry records i. TOC stayed 3 pages, so all
   later Roman numerals are unchanged.
2. **TOC called the appendices CHAPTER A/B/C while the body
   says APPENDIX A/B/C.** Fixed: `\thesisAppendixHeadings`
   now writes a `\chaptername` redefinition into the .toc
   file ahead of the appendix entries, so they render as
   APPENDIX A/B/C (takes effect from the second pass; the
   4-pass build covers it). `\chaptername` is used nowhere
   else in the thesis.
3. **Research Committee date rules ended ragged.** The three
   date lines used hardcoded rules of 4.5/5.5/5.8 cm after
   labels of different lengths, so their right ends stepped
   down the page. Fixed: the three lines are now one
   tabular with a shared 5 cm rule column, so all rules
   start and end at the same x (5 cm is the widest rule
   that fits beside the longest label).
4. **Certification signature/date rules ended ragged**
   (5 cm vs 4 cm after different labels). Fixed: same
   tabular treatment, both rules now 5 cm, aligned.
5. **Approval Date rule shorter than the grid rules**
   (5 cm vs 6.5 cm). Fixed: Date rule now 6.5 cm.
6. **Title page foot was a lone date.** The reference and
   Krishna's own proposal title page both carry a place
   line above the date. Fixed: "Pokhara, Nepal" added
   above "October, 2026" (place taken from the proposal
   title page).
7. **List-of-figures entry C.1 collided with its page
   number** ("R1–R8113": title filled the line, so no
   leader dots and no space appeared). Fixed: the figure
   now carries a short caption for the list only
   ("Comparative Coefficient Forest Plot (R1–R8)");
   the printed caption is unchanged. Same treatment for
   Table 4.1 in the List of Tables, which had lost its
   leader dots the same way.

## Checked and deliberately left alone

- Title-page degree line ("for the Master's Degree"):
  FOM 2019 Appendix B prints exactly this, with no
  specialization, so it was NOT extended to "of Business
  Studies". The specialization already appears on the
  Approval Sheet ("Master of Business Studies (MBS)")
  and in the proposal. Adding it to the title page is
  Krishna's call, not a layout fix.
- Bold thesis titles inside the Certification, Research
  Committee, and Approval paragraphs: house style,
  consistent across all three pages, wording FOM-verbatim.
  The reference uses plain capitals; that is a style
  difference, not a defect, so it was kept.
- "submitted" (lowercase) on the title page: matches FOM
  Appendix B verbatim; the reference's capital S is its
  own choice.
- Acknowledgements, List of Tables, List of Figures,
  List of Abbreviations, Abstract: compared page by
  page; no alignment or spacing defect found beyond
  items 7 above (abbreviations header repeats correctly
  on page xii; abstract holds one page with keywords).

## Verification

Rebuilt with the 4-pass script: 127 pages, A4,
0 LaTeX errors, 0 undefined references. Every fixed page
re-rendered and inspected: title foot, certification
rules, research-committee date rules, TOC front entries
and APPENDIX labels, LOT 4.1 dots, LOF C.1 dots.

Files changed (all uncommitted, unpushed): front/
titlepage, authorship, research_committee,
approval_sheet, acknowledgements, abbreviations,
abstract; main.tex; config/preamble.tex;
chapters/chapter_04_results_and_discussion.tex
(short caption only); appendices/appendix_c.tex
(short caption only).

## Follow-up (same day, Krishna's call)

Certification signature block: the two rules were removed
entirely. FOM Appendix B lists only "Name of the
Candidate / Signature / Date of submission" with no
lines, so the block now reads exactly that (name bold,
then the two labels, no rules). Research Committee and
Approval pages keep their rules; only Certification was
changed. Rebuilt after the change: still 127 pages,
0 errors, 0 undefined; page ii re-rendered and checked.

## Research Committee rebuild to FOM p. 25 (same day)

Krishna supplied the FOM Appendix B p. 25 screenshot:
the old page (one supervisor block, stacked date lines
with solid rules) did not match the format at all. The
page was rebuilt as a filled-in copy of p. 25: paragraph
with a dotted blank for the supervisor's name (unknown,
never invented); three rows, each a left signature
block plus a bordered date box on the right; two
supervisor blocks as printed (second block orders
Signature before Position); all blanks dotted.
Two implementation defects found by rendering and
fixed: (1) a bare \dotfill at the start of a line
after \\ renders NOTHING, so the first build's boxes
were empty — fixed with \null\dotfill, verified in
an isolated test; (2) box labels wrapped because the
box was too narrow — widths measured in TeX (longest
box label 193 pt, longest left label 180 pt) and the
columns set to left 0.46 / box parbox 0.46 / gap 0.02;
(3) a tabular p-column put each box level with its
block's LAST line — replaced with side-by-side [t]
parboxes so each box top sits at its block's first
line, as in the template. Final render verified
against FOM p. 25 item by item (see report):
structure, labels, order, boxes, and dots all match;
remaining differences are forced, not defects:
paragraph 7 lines vs 5 (filled title + FOM 1.5
spacing), left dotted runs shorter and boxes wider
in proportion (thesis text width 433 pt vs the
guideline PDF's ~483 pt; Times bold box label needs
199 pt), head-row dots stubby for the same reason.
Rebuild: still 127 pages, 0 errors, 0 undefined.
Approval page NOT changed in this pass: FOM p. 26
shows a vertical signature list while ours uses the
2x2 grid kept deliberately in Round 1 — flagged to
Krishna, change only on his call.

## Full final verification (same day, after Krishna's challenge)

Honest correction: after the last fixes, only the
changed pages had been re-viewed, not all thirteen.
This pass rendered all 13 front pages from the final
build at 150 dpi and viewed each one: title (i,
unprinted), certification (ii, no lines), research
(iii, FOM p. 25 structure), approval (iv, grid
aligned, Date rule matched), acknowledgements (v,
one page), TOC (vi, front entries i-xiii; vii;
viii, APPENDIX labels + References), LOT (ix, dots
on every entry incl. 4.1), LOF (x, C.1 dots fixed),
abbreviations (xi; xii, header repeated, bottom
rule), abstract (xiii, one page with 5 keywords).
Pagination chain i-xiii verified from the footers.
No new defect found. Comparison method: same-dpi
renders checked element by element against the
format pages, plus TeX point measurements where
widths mattered — not a pixel overlay, which is
meaningless here (FOM templates are Word pages in
a different font with a wider text width, and a
blank template against a filled form cannot overlay).
The single open deviation remains the Approval
grid vs FOM's vertical list.
