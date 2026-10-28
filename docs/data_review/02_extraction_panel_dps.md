# Data review 2: extraction, accounting panel, and DPS

## Question

Are the extracted accounting values correct, are the recomputed
values actually recomputed, and is DPS complete without invention?

## Method

- Recomputed, for all 30 panel rows: identity (assets - liabilities
  - equity) versus the panel's identity_diff_npr; BVPS (equity
  divided by year-end shares) versus bvps_recomputed; ROA (PAT
  divided by average total assets, current plus previous divided by
  two) versus roa_percent_recomputed.
- Compared EPS, DPS, BVPS, and ROA in the joined MPS_RD panel to the
  accounting panel, row by row.
- Counted DPS statuses in the panel and in `config/dps.json`.
- Checked visual overrides: count, method labels, SHA-256 presence,
  and identity checks recorded in the override file.
- Spot-checked PDF text for GBIME FY2081/82 total assets and KBL
  FY2080/81 EPS, and inspected the NMB Nepali report's text layer.

## Findings: accounting panel

- **Identities: PASS.** Maximum absolute identity difference is
  1 NPR across all 30 rows. The three rows at exactly 1 NPR are
  rounding, not error, and are recorded as 1 in the panel, not hidden.
- **BVPS: PASS.** Recomputed BVPS matches the panel's
  bvps_recomputed within 0.01 for all 30 rows. The panel correctly
  uses recomputed BVPS (equity / year-end shares) as the analysis
  variable, not printed NAV.
- **ROA: PASS.** Recomputed ROA matches within 0.01 percentage points
  for all 30 rows, including the two rows whose opening assets came
  from visual reads (HBL FY2076/77, KBL FY2076/77), because those
  visual reads carry exact identity checks for both columns.
- **Printed NAV gaps: two kinds, do not conflate them.**
  (a) NIMB: recomputed differs from printed NAV by 0.28-0.40 in five
  rows (190.70 vs 191.00; 198.28 vs 198.00; 185.67 vs 186.00; 176.31 vs
  176.00; 190.40 vs 190.00). Printed NAVs here are integer-rounded;
  recomputed values are more precise. This is rounding, and the
  thesis should say so in one sentence (see verdict file, item 4).
  (b) NMB FY2081/82: recomputed 175.18 vs printed 174.49, gap 0.69,
  both with decimals. This is not rounding. It remains correctly
  flagged in the panel and must stay flagged. HBL FY2076/77
  (187.67 vs 187.72, gap 0.05) is likewise correctly flagged.
- **Prior-year continuity: PASS with disclosed restatements.**
  Restatements that change a previous column (GBIME FY2078/79
  previous TA differing by 718,438,769; HBL FY2080/81 previous by
  1,877,083,471, Civil merger; KBL FY2079/80 previous by
  1,047,386,219, NCC merger) are recorded, not overwritten into the
  own-year values. The panel rule (each year uses its own current
  column) is followed, including the KBL FY2076/77 case where the
  own-report visual read supersedes the FY2077/78 previous column by
  7,369,687,548, explained in the override file as derivative lines.
- **EPS: reported, not recomputed from year-end shares, correctly.**
  Reported EPS differs from PAT divided by year-end shares by more
  than 0.05 in eight rows, with the largest gaps in merger years
  (GBIME FY2079/80: reported 22.06 vs PAT/year-end 18.71; NIMB
  FY2079/80: 13.92 vs 10.90; HBL FY2079/80: 9.18 vs 7.22) and in
  GBIME FY2076/77 (17.99 vs 15.33) and KBL FY2076/77 (12.08 vs 9.25).
  This is expected: basic EPS uses weighted-average shares, not
  year-end shares, and bonus/merger share issuance mid-year moves
  the two denominators apart. The thesis correctly uses reported
  EPS. The undisclosed consequence is the EPS-versus-BVPS
  denominator mismatch in the post-merger year (see verdict file,
  item 3): BVPS always uses year-end shares, EPS does not. That
  mismatch is a definition limit to disclose, not a panel error.
- **Share-capital continuity: PASS with explained deviations.**
  Growth equals the prior year's bonus percentage exactly in 20 of
  25 transitions. Deviations are: the four 2023 merger jumps
  (GBIME +50.33%, HBL +66.99%, KBL +78.27%, NIMB +86.42%, all versus
  small prior bonuses, all merger-explained); NIMB FY2076/77 to
  FY2077/78 (+14.09% vs 13.00% bonus, the 156,010,915 NPR non-bonus
  capital already resolved in the blocker audit); and NMB
  FY2076/77 to FY2077/78 (+17.02% vs 13.00% bonus, the Kanchan
  acquisition, about 0.57 billion NPR extra capital). No unexplained
  share-capital jump remains.

## Findings: visual overrides

- Three overrides in `config/visual_overrides.json` (HBL FY2076/77,
  KBL FY2076/77, plus the KBL FY2077/78 restatement comparison).
  Each carries a SHA-256, PDF and printed page numbers, the method
  label `visual_page_read`, and exact identity checks for current
  and previous columns. Rendered page images are kept under
  `output/manual_review/visual/`. The method is never disguised as
  text extraction in the panel (method column says visual_page_read
  where applicable). This is the correct way to handle legacy-font
  text layers, and it is auditable.
- The NMB Nepali FY2079/80 row's DPS method is likewise
  visual_page_read, consistent with its text layer being legacy-font
  gibberish (confirmed by extracting text from pages 37-38, which
  returns encoded characters, not Nepali text). This audit did not
  independently re-read those Nepali pages.

## Findings: DPS

- **Completeness: PASS.** `config/dps.json` has 30 entries; the
  panel has 30 DPS values; statuses match exactly: 18 proposed,
  12 documented-nil.
- **No zero-fill beyond documented nils.** Every zero in the panel
  carries status documented-nil, and every proposed value carries a
  source page and, in the config, a quotation (inspected for GBIME
  FY2076/77: Board proposal 2.00% cash / 14.00% bonus, with the
  previous year's 12.75/12.75 explicitly not used).
- **Traps already handled, and correctly:** NMB FY2080/81's 17% cash
  figure on page 22 is a subsidiary's dividend, not NMB's, and is
  not used; NIMB FY2078/79's note (7.00%) wins over its summary
  table (swapped 4.0%); NMB FY2077/78's Board section and AGM
  notice (3.30%) win over the Chairman's statement (3.50%). These
  are the kind of traps that, if missed, would corrupt DPS by
  several percentage points on single rows. They were not missed.
- **Timing eligibility: PASS on the record.** The DPS announcement
  date file records all 30 announcement dates before their MPS_RD
  price dates (26 declarations plus 4 AGM-only fallbacks). This
  audit verified the claim's existence in the file and the panel's
  DPS values, not each announcement date against its primary source.

## Verdict for this file

Extraction, panel, and DPS: PASS. The only additions needed are
disclosure sentences (EPS denominator timing, NIMB NAV rounding),
not value corrections. No panel value was found to be wrong in this
audit.
