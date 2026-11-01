# Thesis guidelines reference — provenance and hierarchy

Saved 2026-10-29. This folder is a reference set only. It does not change the
thesis, and none of these files has been committed or pushed.

## Hierarchy: what governs what

1. **Governing format for a TU Faculty of Management MBS dissertation:
   file 01, the FOM 2019 guideline.** Where any other document in this folder
   conflicts with file 01 on margins, fonts, pagination, preliminary order,
   chapter names, or citation style, file 01 wins for this thesis, unless your
   own campus or supervisor gives you a written campus rule that overrides it.
   Confirm any campus override with your supervisor before using it.
2. **Process supplements: files 02 and 03 (Birendra Campus, 2082).** These add
   campus procedure (proposal eligibility and defence, plagiarism testing,
   viva presentation, copies, records). They explicitly defer dissertation
   format to the FOM 2019 guideline, so they do not replace file 01.
3. **Comparative only: file 04 (Lumbini Banijya Campus, MBS-F).** Do not import
   its chapter names, word count, or table font into this thesis. See conflicts.
4. **Not a university guideline: docs/instructions/instructions_for_paper.md.**
   That file is the research-quality standard used for the finalized review
   (econometric traps, synthesis matrix, hypothesis table, table notes, prose
   rules). It is stricter than FOM 2019 in places and useful, but it is not a
   TU document and must not be cited as one.

## What was found, and what was NOT found

- **No newer TU FOM master's dissertation guideline was found in public search
  on 2026-10-29.** Searches covered the TU portal, FOM-related sites, TU
  campus sites, and copies of the guideline circulating online. Every copy
  found is the 2019 guideline. The Birendra 2082 documents, the newest
  TU-affiliated campus guidelines found, both say to follow the FOM 2019
  guideline for format. That is evidence that 2019 is still the referenced
  standard, not proof that no newer internal FOM document exists. If your
  campus holds a newer printed guideline, that campus copy would supersede
  this search result.
- **Kathmandu University's general master's thesis guidelines were NOT saved.**
  The public link returned "Invalid Token or token expired" on access and on
  reload, so no KU document was obtained, verified, or included. Do not cite
  KU guidelines from this folder.
- SlideShare, CourseHero, and Scribd copies were deliberately excluded as
  sources. Only campus and university domains, plus a campus-hosted copy of
  the FOM document, were used.

## Files

### 01_TU-FOM_Masters-Dissertation-Guidelines-2019.pdf
- Issuer: Office of the Dean, Faculty of Management, Tribhuvan University,
  Kathmandu, Nepal. Effective from 2019. 28 pages.
- Source: https://spacampus.edu.np/public/uploads/downloads/e3ce3b941aa305662605c049e67c9c988cce22bf.pdf
- SHA-256: 9d9aca09586d0373d8221466af03b4e36ffd14637901115cbe01ce62e943b446
- Verification: extracted text is identical to the copy already in this repo
  at src/proposal/format/Master_Dissertation_writing_guideline_2019.pdf
  (different file size and hash, same author, same 28 pages, same text).
  Citation style stated in the document is APA, sixth edition. Typography
  stated in the document is Times New Roman 12 point, 1.5 spacing, with the
  left margin wider than the other three for binding.
- Contents in outline: introduction and purpose, research ethics, requirements
  (including proposal and dissertation structure), paper and typography,
  evaluation, and appendices giving the preliminary-material formats and
  table/figure guidance.

### 02_Birendra-Campus_Dissertation-Guidelines-2082_May2025.pdf
- Issuer: Birendra Bidhya Mandir Campus, Tikapur, Kailali, Faculty of
  Management, affiliated to Tribhuvan University. Guideline year 2082.
  21 pages. PDF created 2025-05-08.
- Source: https://www.birendracampus.edu.np/wp-content/uploads/2025/05/BMC-Dissertation-Proposal-Guidelines-2082.pdf
- SHA-256: abaca9b7ba7c6714d15e6cb3a86d0d55cfc11d7f5d0eb4e304b965c917f4eb68
- Language: mostly Nepali. Use: proposal and dissertation procedure,
  plagiarism testing, viva, copies, and record-keeping. Format is deferred
  to FOM 2019 inside the document itself.

### 03_Birendra-Campus_Dissertation-Guidelines-2082_Jul2025-revision.pdf
- Same issuer and guideline year as file 02. 21 pages. PDF created 2025-07-24.
- Source: https://www.birendracampus.edu.np/wp-content/uploads/2025/07/MBS-Proposal-GL-333-2082-1.pdf
- SHA-256: 9e2c67464fa56c4d646db204358d55dc8d1edd93845ab54278a5625ad3bdc359
- This is a later revision of file 02, not a different guideline. Extracted
  text differs only in small wording additions. Where files 02 and 03 differ,
  file 03 (July) is the later one.

### 04_Lumbini-Banijya-Campus_MBS-F-Dissertation-Format_2025.pdf
- Issuer as shown inside the document: Lumbini Banijya Campus, Faculty of
  Management, under the autonomous programme of Tribhuvan University.
  16 pages. PDF created 2025-03-19.
- Source: https://lbc.edu.np/storage/download/01KA6B1XPRG9RQYAA9D6Z28X98.pdf
- SHA-256: 67e4377f1ac5ff0f15a396564fc32723df5c999d79324b19234510cf343bf92f
- Warning: this is an MBS-F (finance) format document, not the general FOM
  format. Its chapter structure, word range, and table typography differ from
  file 01. Use it only to compare how another TU campus presents a
  dissertation. Do not copy its chapter titles, its word range, or its table
  font into this thesis.

## Conflicts to watch (file 01 wins unless a campus rule says otherwise)

- Citation edition: file 01 states APA sixth edition. A newer APA edition
  guide must not be substituted silently.
- Chapter names: file 01 uses Results and Discussion followed by Summary and
  Conclusion. File 04 uses Analysis and Results followed by Discussion,
  Conclusions and Implications. Keep file 01's names for this thesis.
- Preliminary order: file 01's order is the one the thesis front matter
  already follows. File 04 orders some preliminary items differently.
- Declaration: file 01's preliminary list is headed by certification of
  authorship, followed by the research committee report and approval sheet.
  Whether your campus additionally requires a separate Declaration page is
  still an open question for your supervisor to confirm; do not add or
  remove a front-matter page on the basis of files 02-04 alone.

## What FOM 2019 does not cover (the "main things" gap)

FOM 2019 covers format, ethics, chapter contents in outline, typography,
evaluation, and preliminary/table/figure formats. It does not, by itself,
specify: econometric reporting standards (estimator, standard errors,
degrees of freedom, joint tests), literature synthesis-table columns,
hypothesis decision-table format, sample-coverage disclosure, table-note
completeness rules, or prose-vocabulary rules. Those standards in this
project come from docs/instructions/instructions_for_paper.md, which is a
research-quality standard, not a university guideline. Keep the two kinds of
document distinct when citing them.
