# Front-matter loop — Round 3 review (full re-read, source level)

Method: full re-read of all front files after the Round 2 fixes, plus
programmatic checks (heading gaps, paragraph gaps, signature rules,
abbreviations count, front-matter order in main.tex, blank lines in
tables). This round looked for new defects, not just for confirmation
that earlier fixes held.

## Findings: zero new defects at source level

- Blank lines inside tables: 0 in all three front tables.
- Heading gaps: 1.5 cm on every front page except abbreviations at
  0.8 cm (documented fit exception, unchanged).
- Local 3 pt paragraph gaps: none remain.
- Research Committee signature rules: all 7.5 cm (date rules 4.5 /
  5.5 / 5.8 cm, intentionally graduated, unchanged).
- Abbreviations: 48 rows, alphabetical, additions and removals intact.
- Front-matter order in main.tex: titlepage, authorship,
  research_committee, approval_sheet, acknowledgements, tableofcontents,
  listoftables, listoffigures, abbreviations, abstract — FOM order,
  unchanged by this loop.
- No chapter, appendix, bibliography, or config file was changed by
  this loop (the config/main/titlepage diffs in git status belong to
  the earlier config phase, not to this loop).

## Gate still open: visual compile

Source-level cleanliness is not visual proof. The loop stops only when
an actual compile renders the front pages and shows: each form page
and the abstract on one page, the abbreviations list on one page,
headings and signature rules where the source says they are, and
Roman numerals bottom-centre. That compile is pending on a TeX
installation (apt update was still running when this round was
written). If the compile shows a spill or a misplaced rule, that
becomes Round 4; if it shows clean pages, the loop closes and this
file is amended to say so.
