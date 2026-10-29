# Front-matter loop — Round 2 review (unbiased re-read)

Method: re-read every front file from scratch, in FOM order, without
reusing the Round 1 list as a checklist first. Round 1 fixes were then
checked against the fresh findings, so a Round 1 fix that introduced a
new problem would be caught here, not carried forward.

## Fresh findings

### R2-1. Blank line inside two tabular environments (compile hygiene).
- research_committee.tex: one blank line inside the signature
  tabular, between the supervisor rows and the Head row.
- approval_sheet.tex: one blank line inside the signatory tabular,
  between the first and second signatory rows.
A blank line is a paragraph break token. Inside a tabular it is
fragile: depending on column type and engine it is ignored, or it
breaks the table. It adds nothing visually — row separation is already
given by `\\[1.2cm]` and `\\[2.0cm]`. Fix: delete both blank lines.
No other table in front matter has one (abbreviations longtable: 0).

### R2-2. Round 1 fixes verified, no regression.
- Heading gaps now: authorship 1.5, research 1.5, approval 1.5,
  acknowledgements 1.5, abstract 1.5, abbreviations 0.8 (documented
  fit exception). No other gap changed.
- Paragraph gaps: no local 3 pt setting remains in front matter
  (the two 0 pt settings that remain are inside the title page and
  inside the abbreviations table group, where they are correct).
- Research Committee signature rules: all 7.5 cm now.
- Abbreviations: 48 rows, alphabetical with punctuation ignored
  (checked programmatically), six additions present, eight removals
  absent, BFI plural. Re-checked the removals against the full printed
  text: CBS, CCyB, MIS, PPA, SGM, TOC, FOM, TU have no printed use
  outside the list itself. (SGM appears only as a bibliography key;
  a key is not printed text.)

## Re-checked and passed (fresh, not carried from Round 1)

- Order: Title, Certification, Research Committee, Approval,
  Acknowledgements, TOC, LOT, LOF, Abbreviations, Abstract — FOM p. 9.
- Title page: template blocks in template order, date at the foot.
- Authorship, Research Committee, Approval wording: substance matches
  FOM Appendix B templates. "Acknowledgements" spelling matches the
  Appendix B heading (FOM p. 9 list spells it without the e; the
  template heading spells it with the e — the thesis uses the template
  heading, which is the right one to copy).
- Abstract: two paragraphs, ≈ 350 words, one page by estimate,
  exactly five keywords. Numbers match Chapter IV.
- Pagination: title i unprinted, front Roman bottom-centre from ii,
  body Arabic top-right from Chapter I page 1.
- TOC/LOT/LOF single-spaced.
- Redundant `\setstretch{1.5}` in each front file: harmless (global
  value is already 1.5), left alone — removing it would be churn with
  zero visual effect, and churn in a loop is how new defects enter.
- Abstract's "Ohlson (1995)" written as text rather than a citation
  command: noted, not changed. It renders identically, the reference
  is cited elsewhere, and changing citations is outside a format loop.

## Round 2 fix list

R2-1 only. After it, Round 3 is a full re-read; the loop stops when a
full re-read finds zero new defects.
