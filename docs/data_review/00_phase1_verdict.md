# Phase 1 data review: verdict

Thesis: VALUE RELEVANCE OF ACCOUNTING INFORMATION BEFORE AND AFTER THE
BANKING CONSOLIDATION WAVE: EVIDENCE FROM NEPALESE COMMERCIAL BANKS.
Repository state at audit time: HEAD e2b6a96, 2026-10-28.
Review directory: `docs/data_review/` (new, separate from the earlier
thesis-chapter review directory, which the author deleted after its
items were addressed; nothing from that directory was restored here).

## One-line verdict

The data that feed the thesis are, with the exceptions listed below,
correct. The accounting panel, the DPS series, and the MPS_RD price
series recompute exactly from the files in the repository, and the
analysis tables reproduce exactly from the joined panel under an
independent implementation. No invented value, no silent imputation, and
no mixed price definition was found in the analysis sample. The data
are strong enough to carry the thesis as an exploratory, disclosed
value-relevance study. They are not strong enough to carry it as an
official-NEPSE-close study, and that limit is still the single most
important data fact in the thesis.

## 10-pass loop (2026-10-28, after the first pass)

The first pass alone was not accepted as sufficient, and it should
not have been: the loop that followed found things the first pass
missed. Full evidence is in `07_loop_log.md` (passes 1-10, each
against the sources). Headline: no panel value, price, DPS value,
regression coefficient, or table number was found wrong in any
pass. What the loop did find is one wrong number in the thesis
text itself (item 6 below, HBL EPS 29.80, which must be 28.07),
one Group-column extraction error that does not touch the thesis
numbers (item 7), one unlisted small restatement (item 8),
misleading suspension wording surviving in Chapters 1 and 4
(items 9-10), and two reproducibility items (items 11-12). The
fix list below is therefore items 1-5 from Phase 1 plus items
6-12 from the loop. The reviews are finalized on that list.
Finalization means the review is complete, not that the fixes
are applied: every fix still needs the author's approval for
the actual edit, in both the Markdown and the LaTeX version
where the error appears in both.

## What was actually done (so this verdict can be checked)

- Source inventory: every file under `data/reports/` listed, magic
  bytes checked, sizes recorded, page counts taken with `pdfinfo`
  (not with the earlier discovery script).
- Panel recomputation: for all 30 rows, balance-sheet identity
  (assets minus liabilities minus equity), BVPS (equity divided by
  year-end shares), and ROA (PAT divided by average total assets)
  recomputed from the panel's own component columns and compared to
  the panel's stated identity difference, recomputed BVPS, and
  recomputed ROA.
- Joined-panel cross-check: every EPS, DPS, BVPS, and ROA value in
  `mps_rd_joined_panel.csv` compared to the accounting panel.
- Analysis recomputation: Model 1, Model 2, joint Wald test,
  descriptives, correlations, and Cook's distance recomputed from the
  joined panel with an independent NumPy OLS/HC3 implementation using
  Student's t on residual degrees of freedom, and compared to tables
  T1, T2, T3, T4, T5, T6, A4, A5, and A6.
- Figure audit: generation code read for F1-F6 and A1-A3, rendered
  PNGs viewed for F3, F4, and F6, and F3 bivariate slopes recomputed
  per period and compared to the Model 2 slopes.
- Spot checks against PDF text: GBIME FY2081/82 total assets, KBL
  FY2080/81 EPS sequence, and the NMB Nepali report's text layer.
- DPS config check: all 30 entries in `config/dps.json` counted and
  status-counted; one entry's quotation inspected.

## What was NOT done (stated here so it is never misread as done)

- I did not re-read all 5,663 report pages in this audit. The full
  manual verification is the original 2026-10-27 extraction work; this
  audit recomputes from its outputs and spot-checks pages. Anyone who
  claims this audit re-read every page is misrepresenting it.
- I did not re-fetch Merolagani, ShareSansar, FinancialNotices, or
  NEPSE live in this audit. The price-verification record is the
  2026-10-27 A4 table and verification files; live pages today would
  not prove values recorded then.
- I did not independently re-read the Nepali NMB FY2079/80 statement
  pages. Their text layer is legacy-font gibberish, and the panel
  correctly labels that row's DPS method as visual_page_read.
- I did not review the local uncommitted modifications to
  `source_register.md` / `build_source_register.py` in this audit.
  They remain uncommitted and unverified by this review.

## Confirmed correct (with numbers)

1. Reports: 30 bank-years, 5 series x 6 fiscal years, 314 MB, 5,663
   pages by `pdfinfo`. 31 files on disk: 30 real PDFs plus one dead
   399-byte S3 NoSuchKey XML (NMB FY2079/80 English path) plus the
   usable Nepali PDF for that bank-year. The dead file is not used
   as a source; the panel correctly cites the _NP.pdf.
2. Identities: maximum absolute identity difference 1 NPR across all
   30 rows. BVPS and ROA recompute exactly (within 0.01) for all 30.
3. Joined vs panel: zero mismatches in EPS, DPS, BVPS, or ROA across
   all 30 joined rows.
4. DPS: 30 entries, 18 proposed, 12 documented-nil. No zero-fill
   beyond documented nils. No DPS value is missing in the analysis
   sample.
5. MPS_RD: 30 candidate rows, 28 clean under the 5-day window, 13
   pre and 15 post, 2 excluded (HBL FY2077/78 gap 54 days, NIMB
   FY2077/78 gap 47 days), 4 entity-mismatch rows (all four merged
   banks, FY2078/79 only, NMB correctly not flagged).
6. Analysis: Model 1 EPS 2.095 (SE 4.096, p = 0.616), BVPS 0.219
   (SE 1.858, p = 0.908), R-squared 0.948, df 16; Model 2 pre-EPS 5.577
   (SE 3.560, p = 0.140), pre-BVPS 0.100 (SE 1.306, p = 0.940),
   delta_E -3.124 (SE 4.003, p = 0.448), delta_B -1.758 (SE 1.231,
   p = 0.175), joint Wald F(2, 14) = 2.954, p = 0.085; all descriptives
   and correlations reproduce exactly (third-decimal rounding only).
   R6 delta_B SE 1.517 in T5 matches the independent recomputation.
7. MPS_post: still settled 2/30 only (GBIME FY2081/82 240.00,
   NIMB FY2081/82 193.00), 3 pending, 25 unavailable. The original
   design remains dead, correctly, and no regression is run on it.

## Must fix or clarify in the data outputs (not in the thesis chapters,
## which were already fixed)

1. **A4 note still misattributes the NMB price.** Table A4's note says
   the NMB FY2076/77 cell "was resolved by a third source at 437.00".
   The "third source" is ShareSansar's own full daily record, which is
   the dataset's own source, not an independent third source. Chapter 3
   now says this correctly; A4 does not. Fix A4's note to match
   Chapter 3 word for word: dataset 437.00, Merolagani LTP 436.00,
   retained on ShareSansar's record, NEPSE close unverified.
2. **F3 lines are not Model 2 slopes, and one sign flips.** F3's
   per-period bivariate OLS slopes are: pre EPS 4.175, pre BVPS 2.269,
   post EPS 0.305, post BVPS 0.803. Model 2's two-way FE slopes are:
   pre EPS 5.577, pre BVPS 0.100, post EPS 2.453, post BVPS -1.658.
   The post-BVPS sign flip is the year-fixed-effects absorption story,
   not a contradiction, but the F3 caption only says "OLS regression
   lines" and does not warn the reader that these are descriptive
   bivariate lines, not the Table 4.4 estimates. Add one sentence to
   the F3 caption and to the Chapter 4 figure note: "Lines are
   descriptive bivariate OLS fits, not the two-way fixed-effects
   estimates in Table 4.4; the post-BVPS sign difference is the
   effect of absorbing year effects."
3. **EPS denominator timing in the merger year, undisclosed.** Reported
   EPS uses weighted-average shares; BVPS uses year-end shares. In
   FY2079/80, the post-merger year, EPS denominators mix pre- and
   post-merger share counts (for example GBIME reported EPS 22.06
   versus PAT divided by year-end shares 18.71; NIMB 13.92 versus
   10.90; HBL 9.18 versus 7.22), while BVPS uses merged year-end
   shares throughout. This is not a data error: reported EPS is the
   correct printed figure. But the thesis discloses the
   fundamentals-versus-price entity mismatch and does not disclose
   this EPS-versus-BVPS denominator mismatch in the post period. Add
   one disclosure sentence in Chapter 3 and in the A6 dataset note.
4. **NIMB printed NAV rounding, unexplained.** Recomputed BVPS differs
   from printed NAV by 0.28-0.40 in five NIMB rows (190.70 vs 191.00,
   198.28 vs 198.00, 185.67 vs 186.00, 176.31 vs 176.00, 190.40 vs
   190.00) because the printed NAVs are integer-rounded. The analysis
   correctly uses recomputed BVPS. Add one sentence stating the
   printed NAVs are integer-rounded, so an examiner does not read
   these five rows as discrepancies. This does not explain NMB
   FY2081/82 (175.18 vs 174.49, both with decimals, gap 0.69), which
   remains correctly flagged as an unexplained printed-versus-
   recomputed difference and must stay flagged.
5. **Generation manifest paths are Windows paths.** The analysis
   generation manifest records outputs under
   C:\Users\Hellx\Documents\... . On any other machine, the manifest
   alone does not reproduce the outputs. Regenerate the manifest with
   relative paths, or add a note that it records the generating
   machine's paths. Minor reproducibility item, not a numbers error.
6. **WRONG NUMBER in Chapter 3 (loop pass 7, both versions).**
   Chapter 3's R8 paragraph says HBL FY2077/78 was "reported 29.80,
   restated 27.60". The raw files prove Bank EPS as printed is
   28.07 (Group 29.24, next report's previous Bank column 27.60);
   29.80 appears nowhere in the HBL raw extraction in any year.
   Correct text: "reported 28.07, restated 27.60". The R8 regression
   itself is unaffected (it uses the correct 27.60, and the HBL row
   is window-excluded anyway), but this is a wrong number in the
   methodology chapter and must be fixed in both the Markdown and
   the LaTeX chapter before submission. GBIME 17.99 to 15.33 and
   NMB 16.66 to 14.76 in the same paragraph are correct.
7. **GBIME Group equity omits non-controlling interest (loop
   pass 1).** GBIME Group total equity in the raw files equals
   equity attributable to equity holders, so the Group identity
   fails for all 6 GBIME years by the NCI amount (proven FY2076/77:
   gap 211,277,477, matching the SOFP NCI line to the rupee; other
   years' gaps 504,706,906 / 562,092,282 / 669,443,650 / 599,656,913 /
   686,311,598 are consistent but not individually verified here).
   Bank columns, the panel, and all regressions are unaffected.
   Fix the raw Group equity (attributable plus NCI) or state
   plainly that the panel is Bank-only and Group equity is not used.
   Do not claim both Group and Bank columns are fully verified
   while this stands.
8. **KBL small restatement, previously unlisted (loop pass 2).**
   KBL FY2077/78 to FY2078/79 total assets differ by 9,587,393
   (0.005%) between own current and next previous columns. Immaterial,
   but add it to the restatement list so the list is complete.
9. **"During merger negotiations" wording survives in Chapters 1
   and 4 (loop pass 8).** Chapter 3 was fixed, but Chapter 1 (twice)
   and Chapter 4 still say trading was suspended "during merger
   negotiations". The HBL-NIB merger was rejected 14 January 2022,
   months before the April-June 2022 suspension window. Change all
   three to "merger-related suspension" in both Markdown and LaTeX.
10. **Unverified NEPSE halt mechanism claim (loop pass 8).**
    Chapter 4 asserts NEPSE regulations "historically enforced"
    extended halts during merger negotiations, with no rule or
    order cited for the HBL/NIB post-rejection suspension. Either
    cite the specific rule or soften to "trading remained
    suspended" without attributing a mechanism.
11. **R7 bonus timing, undisclosed (loop pass 5).** R7's bonus% is
    that fiscal year's proposed bonus, issued in the following year,
    so BVPS_adj is a pro-forma forward adjustment, not a restated
    year-end BVPS. Add one sentence saying so.
12. **File and reproducibility hygiene (loop passes 3 and 10).**
    The DPS announcement CSV has a malformed NIMB FY2081/82 row
    (unquoted comma splits the note; dates and flags are correct).
    And the analysis test suite cannot run in this VM's venv:
    dataset tests pass 11/11, but stats/registry tests fail at
    collection for missing scipy/statsmodels. Document the required
    dependencies alongside the manifest; do not claim the suite
    passes until it runs in a complete venv.

## Open data limits (unchanged, and still decisive for framing)

- NEPSE official-close verification: never done for any MPS_RD row.
  Prices remain cross-checked aggregator prices (ShareSansar via the
  dataset, Merolagani LTP, FinancialNotices only for FY2081/82).
- Per-bank-year disclosure-before-deadline proof: never done row by
  row. The Chaitra deadline is a legal-requirement argument, not a
  per-row publication proof.
- Supervisor approval of the aggregator-price definition: still the
  gate for presenting the analysis as final rather than draft,
  disclosed, exploratory analysis. No data fix in this review changes
  that gate.

## Phase 1 conclusion (after the 10-pass loop)

Phase 1 passes, with the twelve items above. The data are honest,
recomputable, and internally consistent, and no data value was
found wrong in ten passes. But the loop proved the first pass
was incomplete: it missed a wrong number in the thesis text
(item 6), and that number must be fixed before submission, along
with items 1-4, 7, and 9-10. Items 5, 8, 11, and 12 can wait for
the next regeneration, but item 6 cannot. Phase 2
(thesis-chapter review against these data) can proceed on this
foundation without re-extraction, using the loop fix list as
its starting checklist.
