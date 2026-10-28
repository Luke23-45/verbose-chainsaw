# Data review 1: source reports

## Question

Are the 30 audited annual reports actually present, actually PDFs,
actually the right bank-years, and actually complete?

## Method

- Listed every file under `data/reports/` (31 files).
- Checked the first 5 bytes of every file (PDF magic `%PDF-` versus
  XML).
- Recorded file sizes.
- Took page counts with `pdfinfo` for every PDF, independently of the
  earlier discovery script, and summed them.
- Compared the file list to the `data/README.md` checklist (5 series,
  6 fiscal years, merger-transition year FY2079/80).

## Findings

- **Count: PASS.** 5 series (GBIME, HBL, KBL, NIMB, NMB) x 6 fiscal
  years (FY2076/77-FY2081/82) = 30 bank-years, all present.
- **Files on disk: 31.** The extra file is the known dead file:
  `NMB/FY2079-80/NMB_FY2079-80_annual_report.pdf`, 399 bytes, first
  bytes `<?xml` (an S3 NoSuchKey error document, not a PDF). The
  usable report for that bank-year is the adjacent Nepali edition
  `..._NP.pdf` (150 pages, valid PDF). The accounting panel correctly
  cites the _NP.pdf as its source file for NMB FY2079/80. The dead
  file must not be deleted silently without a note, because its
  presence is itself evidence of a failed fetch that was caught; but
  it must never be counted as a report. Any future inventory that
  counts files instead of bank-years will overcount by one.
- **Total size: 314 MB.** Matches the earlier record.
- **Total pages: 5,663 by `pdfinfo`.** Matches the earlier discovery
  total exactly (5,663 pages, of which 579 were earlier recorded as
  image-only). Per-file page counts range from 122 (HBL FY2076/77) to
  352 (GBIME FY2081/82). No file is a stub: the smallest real PDF is
  3.16 MB (HBL FY2076/77, 122 pages).
- **Bank-year identity: PASS on the checklist, with two caveats that
  are already disclosed in the thesis and must stay disclosed.**
  (a) HBL reports came via Wayback captures because the live HBL site
  refused connections on 2026-10-27; the README maps 28th-33rd annual
  reports to FY2076/77-FY2081/82. This audit did not re-verify the
  Wayback provenance of each HBL file; it verified presence and
  readability only. (b) NIMB pre-merger years are Nepal Investment
  Bank Ltd reports, and FY2079/80 onward are Nepal Investment Mega
  Bank reports; the series is continuous by construction, not by
  corporate identity, and the thesis correctly treats FY2078/79 as
  the entity-mismatch year for NIMB as for the other merged banks.
- **Language: PASS under the author's rule.** 29 English reports plus
  1 Nepali fallback (NMB FY2079/80). The author's 2026-10-27 rule
  (English or Nepali both count; Nepali is the fallback) is satisfied,
  and the fallback is exactly one bank-year, not a systematic language
  gap.

## What this review does not prove about the reports

- That each PDF is the final audited version rather than a draft or a
  summary: the panel's page citations (SOFP/SOPL pages per bank-year)
  are the evidence for that, and this audit checked identities and
  spot pages, not every statement page.
- That the HBL Wayback files are byte-identical to the live-site
  originals: Wayback provenance was not re-checked here.
- That no report was superseded by a later corrigendum: no corrigendum
  search was run in this audit.

## Verdict for this file

Source reports: PASS, with the dead XML file and the Nepali fallback
explicitly carried as known, disclosed exceptions. Do not "clean up"
the dead file without recording why it was there.
