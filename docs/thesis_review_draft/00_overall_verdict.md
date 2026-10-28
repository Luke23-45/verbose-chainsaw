# Supervisor review: overall verdict (unbiased, independent)

Date of review: 2026-10-28. Draft reviewed: `docs/draft/thesis/chapter_01` to `chapter_05`.
Analysis outputs checked: `data_analysis/analysis/outputs/tables/T1` to `T6`, `A4` to `A6`,
and the joined panel `data_analysis/data_extract/output/manual_review/mps_rd_joined_panel.csv`.
No file in `docs/draft/thesis/` was changed by this review. These review files are the only new files.

## One-line verdict

Not ready for final submission as written, but fixable without redoing the data.
The core dataset and the headline coefficients are sound. The defects are in inference
reporting, in two source attributions, and in conclusions that overstate what the
baseline model actually shows. Fix those, and the thesis becomes defensible as an
exploratory, non-causal, aggregator-price study. Leave them, and an examiner will
find them in the viva, because they are in the tables, not in the footnotes.

## What was independently recomputed (not copied from the draft)

From the joined panel, clean sample n = 28 (13 pre, 15 post), all descriptive
statistics in Table 4.1 reproduced exactly, including MPS_RD mean 254.34, EPS mean
14.05, BVPS mean 160.18, DPS mean 3.56, ROA mean 0.99, and every pre/post split.
Correlations reproduced exactly: MPS_RD-EPS 0.358, MPS_RD-BVPS 0.217, EPS-ROA 0.975,
EPS-BVPS 0.372. Model 1 coefficients and HC3 standard errors reproduced exactly
(EPS 2.095, SE 4.096; BVPS 0.219, SE 1.858; R-squared 0.948). Model 2 coefficients and
HC3 standard errors reproduced exactly (pre EPS 5.577, SE 3.560; pre BVPS 0.100,
SE 1.306; delta_E -3.124, SE 4.003; delta_B -1.758, SE 1.231; post EPS 2.453;
post BVPS -1.658; R-squared 0.978). Joint Wald F for Model 2 reproduced exactly:
F(2, 14) = 2.954, p = 0.085. Robustness coefficients for R3, R4, R5 reproduced exactly.
R6 joint Wald reproduced exactly: F(2, 10) = 5.82, p = 0.021. Specification comparison
reproduced exactly: pooled EPS 4.882, R-squared 0.136; bank-FE-only EPS 5.217,
R-squared 0.176; two-way FE EPS 2.095, R-squared 0.948. Cook's distance, when computed
with the correct parameter count (12), reproduced exactly: maximum 0.552 at HBL
FY 2076/77, 5 observations above 4/28 = 0.143.

## What is genuinely strong

- The accounting panel is complete (30/30) and the DPS record is complete (30/30).
  No price, EPS, BVPS, DPS, or ROA value in Chapter 4 was found to be invented or
  mistranscribed against the joined panel.
- The two missing prices are handled correctly: HBL FY 2077/78 (54 days late) and
  NIMB FY 2077/78 (47 days late) are coded missing, never imputed, and named in
  every chapter that uses the sample.
- The FY 2078/79 entity-timing mismatch is disclosed, retained in the baseline, and
  tested by exclusion. That is the honest way to handle it.
- The P/E exclusion argument is mathematically correct, and the EPS-ROA collinearity
  argument is correct (r = 0.975, bivariate VIF about 20).
- The year-fixed-effects absorption point is real and important: in this sample,
  year dummies, not EPS and BVPS, carry almost all of the price variation
  (R-squared 0.136 pooled, 0.948 with two-way fixed effects). The draft is right
  to make this a central finding, not a footnote.

## Must-fix items that apply across chapters (fix once, everywhere)

1. **Normal-distribution p-values and confidence intervals, not t(df).**
   Every Model 1, Model 2, and robustness p-value and confidence interval in
   Chapter 4 was computed with the normal approximation (1.96), not with the
   t distribution on the stated residual degrees of freedom. Evidence: Model 2
   pre-EPS confidence interval in the draft is [-1.401, 12.555], which is exactly
   5.577 +/- 1.96 x 3.560. The correct t(14) interval is [-2.059, 13.213].
   Corrected two-tailed p-values (t, not normal): Model 1 EPS 0.617 not 0.609,
   BVPS 0.906 (unchanged at rounding); Model 2 pre-EPS 0.139 not 0.117, pre-BVPS
   0.940 not 0.939, delta_E 0.448 not 0.435, delta_B 0.175 not 0.153, post-EPS
   0.298 not 0.280, post-BVPS 0.161 not 0.139. No 5% decision in the baseline
   changes, because every baseline coefficient is insignificant under either
   distribution. That is precisely why this must be fixed rather than hidden:
   an examiner who recomputes one interval will doubt every interval.
   Fix in the pipeline (use the t distribution on residual df) and regenerate
   all tables, or state explicitly, with justification, that normal
   approximations were used. For n = 28 and df = 14, the t distribution is the
   defensible choice.
2. **R6 delta_B standard error, t, and p are wrong in the discussion.**
   Chapter 4, section 4.2.6, and Chapter 5, section 5.2.3, report delta_B = -2.611
   with HC3 SE 1.328, t = -1.97, p = 0.077. The SE 1.328 is the pre-consolidation
   BVPS coefficient's standard error from Table 4.6, not the delta_B standard
   error. Independently recomputed delta_B HC3 SE is about 1.52, giving
   t = -1.72, p = 0.116 on t(10), or 0.085 on the normal approximation. Under the
   correct t distribution, the individual delta_B is not significant even at
   10%. The joint Wald test for R6 is unaffected and remains F(2, 10) = 5.82,
   p = 0.021. The discussion must be rewritten to say exactly that: joint
   significance in R6, individual interactions not significant. It must not
   present delta_B as individually significant.
3. **Conclusions contradict the baseline result.**
   The baseline joint test fails to reject stability at 5% (F = 2.954, p = 0.085).
   Only the R6 sensitivity (dropping FY 2078/79, n = 23, df = 10) rejects at 5%.
   Any sentence that says parameter stability is "conclusively rejected",
   that the consolidation "caused" a break, or that the data "conclusively
   prove" a structural break, is false for the baseline and overstates R6.
   Correct formulation, everywhere: baseline evidence is suggestive but not
   significant at 5%; after removing the entity-mismatch year, the joint test
   becomes significant, so the finding is sensitivity-dependent and must be
   reported as such, in associational (not causal) language.
4. **Prices are aggregator prices, not NEPSE official closes.**
   No MPS_RD row in this thesis is a verified NEPSE official close. The prices
   are ShareSansar dataset closes cross-checked against Merolagani last traded
   prices, with FinancialNotices closes only for FY 2081/82. Every sentence that
   says prices were "verified against NEPSE trading records" or "based on NEPSE
   floor trading archives" must be removed (see Chapter 3 review, items 1-2).
   The correct attribution, already used in Table A4, is: dataset close resolved
   by a third aggregator source, NEPSE official-close verification remains open.
5. **Mechanisms are interpretations, not findings.**
   The dataset contains prices, EPS, BVPS, DPS, and ROA. It contains no NPL ratio,
   no provisioning amount, no goodwill amount, and no regulatory forbearance
   measure. Sentences that present an NPL surge, provisioning shock, goodwill
   overhang, or regulatory forbearance as the explanation for a coefficient
   must be reworded to "consistent with" or "a plausible mechanism, not tested
   here", or supported with new data. This applies most to Chapter 4,
   section 4.3.2, and Chapter 5, section 5.4.1.
6. **Hypothesis framing must be identical in Chapters 1 and 4.**
   Chapter 1 states two-tailed tests of beta != 0. Chapter 4, Table 4.5, states
   nulls as beta <= 0 (one-sided), and its detailed text states hypotheses as
   beta > 0 (directional). Unify on one framing. Recommended: null beta = 0,
   two-tailed, alpha = 0.05, exactly as Chapter 1 states. Decisions do not
   change (all fail to reject), but the inconsistency is a viva question.

## Literature checks completed for this review (not assumed)

- Kwon and Wang 2020: verified. Accounting and Finance, vol. 60(3),
  pp. 2717-2757, DOI 10.1111/acfi.12411. The thesis bibliography entry is correct.
- Gurung and Dahal 2025, Pravaha, vol. 31(1), pp. 1-12, DOI
  10.3126/pravaha.v31i1.89145: verified. Abstract and full text confirm 10 of 19
  banks, FY 2013/14-2023/24, fixed-effects Hausman test, DPR, P/E, EPS, BVPS, and
  ROA significant. The draft's description of this paper is correct. Note for
  the author: this is a different paper from Dahal, Gurung, and Ghimire 2025
  (Interdisciplinary Journal of Management and Social Sciences, 209 observations,
  all listed banks). The thesis should add a footnote distinguishing the two,
  or an examiner who knows the second paper will think the first description
  is wrong.
- Giri 2024: verified. Journal of Advanced Academic Research, vol. 11(1),
  pp. 12-23, DOI 10.3126/jaar.v11i1.65518. Abstract confirms 4 banks, 40
  observations, FY 2070/71-2079/80, significant positive correlation of price
  with DPS, P/E, and net worth, negligible EPS correlation. The draft's
  description is correct.
- Timalsina 2026: bibliography entry verified against the journal record
  (The Management Review, vol. 2(1), pp. 305-316, DOI 10.3126/tmr.v2i1.96931).
  The draft's sample numbers (13 banks, 169 observations) are internally
  consistent (13 x 13) but were not independently confirmed from the full text
  in this review; confirm the sample from the PDF before submission.
- Bhandari, Pradhan, and Ghimire 2026: bibliography entry is plausible and
  consistent with the published abstract record (International Research Journal
  of MMC, vol. 7(1), pp. 190-205, DOI 10.3126/irjmmc.v7i1.93032). The draft's
  "EPS predominant" summary is consistent with that record. Confirm the exact
  wording from the PDF before submission.
- Merger dates and swap ratios: GBIME-Bank of Kathmandu 9 January 2023 (1:1),
  HBL-Civil Bank 24 February 2023 (100:80.28), KBL-NCC Bank 1 January 2023 (1:1),
  NIMB formation 11 January 2023 (100:90), NMB-Kanchan August 2020 (about
  NPR 0.57 billion added share capital). All are consistent with the project
  record and are correctly stated in Chapters 2 and 3, except for the
  "tripartite" wording flagged in the Chapter 3 review.

## What does not need redoing

The data do not need re-extraction. The models do not need respecification.
The R6 sensitivity does not need to be dropped; it needs to be reported
honestly, as a sensitivity. The only recomputation required is mechanical:
regenerate p-values and confidence intervals with the t distribution, and
correct the R6 delta_B standard error in the text. Everything else on the
must-fix list is wording, attribution, and conclusion discipline.

## Recommended order of correction

1. Fix the pipeline inference (t distribution) and the R6 delta_B text.
2. Fix the two price-source attributions in Chapter 3.
3. Rewrite every "conclusively" / "caused" / "definitively resolves" conclusion
   in Chapters 4 and 5 to the sensitivity-dependent, associational form.
4. Unify hypothesis framing (Chapters 1 and 4) and soften mechanism language.
5. Then do the minor clarifications listed in each chapter review.
