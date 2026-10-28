# Supervisor review: Chapter III, Research Methodology

Draft file: `docs/draft/thesis/chapter_03_research_methodology.md`
Verdict: The design is sound and the price table is correct. This chapter
contains the two most serious source-attribution errors in the thesis, plus
two claims (zero error, Stata/SPSS cross-validation) that cannot be
substantiated from the record. Both source errors must be fixed before
submission; neither requires new data, because the correct attribution
already exists in Table A4.

## Strengths

- The sampling criteria, bank profiles, merger dates, and swap ratios are
  correct and complete, including the NMB-Kanchan note.
- Table 3.1 (realized MPS_RD prices) matches the verified price table exactly,
  cell by cell, including the two missing rows, the FY 2078/79 entity-timing
  superscripts on the four merged banks only (not on NMB), and the
  Friday 12 April 2024 to Sunday 14 April 2024 footnote.
- The 5-day freshness rule, the post indicator, the absorption of the
  standalone Post effect by year fixed effects, and the degrees-of-freedom
  accounting (Model 1: 28 - 12 = 16; Model 2: 28 - 14 = 14; DPS model: 13)
  are all correct.
- The DPS timing rule (only dividends declared on or before the price date;
  documented nil = 0) is correctly stated and is consistent with the
  announcement-date record (all 30 announcement dates before their price
  dates).

## Must fix

1. **Price reconciliation reversed, and a false NEPSE attribution
   (section 3.4.3, step 3).** The chapter states: "the single minor
   discrepancy (NMB FY 2076/77, Merolagani 437.00 vs. ShareSansar 436.00) was
   arbitrated and verified at NPR 437.00 based on NEPSE floor trading
   archives." Every part of that sentence after "discrepancy" is wrong
   against the project's own verification record:
   - The dataset (ShareSansar) close is 437.00; the Merolagani last traded
     price is 436.00. The chapter has them reversed.
   - The tie-breaker was ShareSansar's own full daily record for that date
     (open 432, high 439, low 428, close 437.00), which matches the dataset on
     every field. That proves scrape accuracy against ShareSansar, not
     independent agreement, because ShareSansar is the dataset's own source.
   - No NEPSE floor trading archive was used, and no NEPSE official close
     was verified for any MPS_RD row. Table A4 states this correctly:
     "NEPSE official-close verification remains open."
   Correct text: "NMB FY 2076/77: dataset (ShareSansar) close 437.00,
   Merolagani LTP 436.00. The 437.00 value was retained on the basis of
   ShareSansar's full daily record; because ShareSansar is the dataset's
   source, this is not an independent verification, and the NEPSE official
   close for 2021-04-13 remains unverified." This is a must-fix because it
   is a source misattribution in the methodology chapter, the chapter an
   examiner trusts most.
2. **"Verified against NEPSE trading records" (Table 3.1 note).** The table
   note says prices were "retrieved from capital market data aggregators
   (ShareSansar and Merolagani; cross-checked against FinancialNotices for
   FY 2081/82) and verified against NEPSE trading records." Delete the final
   clause. The correct note is the aggregator cross-check alone, with the
   explicit statement that NEPSE official closes were not verified. The
   same correction applies to any other sentence in this chapter that
   implies NEPSE verification. Section 3.4.2, which lists aggregators as
   primary sources and NRB/SEBON/MoF as contextual sources, is correct and
   should be the model for the table note.
3. **"Zero data transcription error" (section 3.4.3, introduction).** The
   chapter claims the protocol ensures "zero data transcription error".
   No audit protocol can prove zero error, and this project itself retains
   flagged discrepancies that are not transcription errors but are real
   data features (for example, NMB FY 2081/82 recomputed BVPS 175.18 versus
   printed NAV 174.49, and the EPS restatement flags). Replace "zero data
   transcription error" with the actual claim the audit supports: "every
   value was extracted from the audited report, recomputed where the
   definition requires it, and flagged where recomputation disagreed with
   a printed figure, rather than overwritten". That is a stronger, true claim.
4. **"Cross-validation in Stata and SPSS" (section 3.6.7).** The chapter says
   modelling was done in Python (statsmodels, linearmodels, seaborn,
   matplotlib), "with cross-validation in Stata and SPSS". No Stata or SPSS
   output, log, or script is present in the analysis folder, which contains
   only the Python pipeline, and this review found no record of a Stata or
   SPSS run. Either produce the Stata/SPSS outputs and cite them, or delete
   the clause. A methods claim with no artefact behind it is worse than no
   claim, because an examiner will ask to see the output.
5. **"Tripartite merger negotiations" (section 3.3.4).** The chapter says HBL
   trading was suspended "during complex tripartite merger negotiations with
   Nepal Investment Bank". The verified record, re-checked against
   contemporaneous reporting in the second review pass, is a bilateral
   HBL-NIB memorandum of understanding signed 13 May 2021, rejected at
   HBL's 29th annual general meeting on 14 January 2022 (75% approval
   required; about 42% voted against, including the Employees Provident
   Fund, after a due-diligence dispute over the swap ratio: DDA 1:1
   versus EPF's independent 1:0.78). No third party to a tripartite
   negotiation is named anywhere in that record. Delete "tripartite" or
   cite a source that names the third party. Two further refinements from
   the same check: (a) the merger was already rejected in January 2022,
   so describing the April-June 2022 suspension as "during merger
   negotiations" is misleading; use "merger-related suspension" (the
   wording the proposal already uses) for the April-June window, and do
   not imply negotiations were still open then unless a source proves it;
   (b) one contemporaneous digest notes that under NRB's Merger Bylaw
   2011, banks that fail to unify after signing an MoU can face dividend,
   branch, and share-transaction restrictions, which is a plausible
   mechanism for a post-rejection suspension, but it is not proven for
   HBL/NIB in this thesis and must not be stated as the cause without a
   specific NRB order or notice. The dates, the 54-day and 47-day delays,
   and the missing coding are all correct; only the "tripartite"
   adjective and the "during negotiations" timing are unsupported.

## Clarify

- **Intercept plus full fixed effects (sections 3.6.1-3.6.2).** The equations
  show an intercept alpha plus bank effects mu_i plus year effects lambda_t.
  With full dummy sets, the intercept is not separately identified; the
  pipeline correctly uses reference categories (GBIME, FY 2076/77), and
  section 3.6.1 states the reference categories for Model 1. State the same
  reference categories in the equation notes for Model 2, and in one sentence
  say that "5 bank parameters" in the degrees-of-freedom count means the
  intercept plus 4 bank dummies, and "5 year parameters" means 5 year dummies
  with FY 2076/77 as reference. The arithmetic (14 parameters, 14 residual df)
  is correct; the wording is ambiguous.
- **R8 rows (section 3.6.5).** The robustness list says R8 uses "retrospective
  audited basic EPS restatements" without naming the rows. Name them:
  GBIME FY 2076/77 (15.33, replacing 17.99) and NMB FY 2077/78 (14.76, replacing
  16.66) are the rows that change in the analysis sample (n = 28). The
  pipeline configuration also flags HBL FY 2077/78 (27.60), but that row is
  window-excluded, so it does not affect any R8 estimate. Table A6 flags all
  three rows in the full 30-row dataset, which is correct for the full
  dataset and confusing without this sentence. Add it.
- **DPS "missing" wording (section 3.5.2, DPS).** The chapter says
  "unannounced dividends are treated as missing". In the analysis sample,
  every row has a DPS value (a documented nil is 0, and all 28 rows have a
  declared or documented-nil value). Clarify that no DPS value is missing
  in the analysis sample, and that the "missing" rule applies to a dividend
  that was never announced, which does not occur in this sample. Otherwise
  a reader will think the DPS model has missing DPS rows.
- **Sampling criterion 4 (section 3.3.2).** "Continuous active listing with
  trading records that satisfy the freshness window" reads as if all five
  banks satisfy the window in all years. Two rows do not. Reword to "active
  listing, with row-level freshness applied" and point to section 3.3.4,
  which already handles this correctly.
- **BAFIA operationalization (section 3.5.2, dependent variable).** This
  section correctly says the deadline is "operationalized at the end of
  Chaitra". Keep this wording, and make Chapter 2 match it (see Chapter 2
  review, item 2).

## Verified in this chapter

- All 30 price cells in Table 3.1, the two missing rows, the 13/15 split,
  and the 5-day rule.
- EPS own-current rule, BVPS recomputation rule, ROA definition (PAT /
  average total assets), DPS cash-only rule (bonus shares excluded).
- Model specifications, Post definition, interaction definitions, and
  degrees of freedom for Models 1, 2, and the DPS model.

## Overall for this chapter

Moderate revision, but items 1 and 2 are submission-blocking. They are the
only places in the thesis where the price source is misattributed, and they
sit in the methodology chapter. Fix them, delete the two unsubstantiated
claims (items 3 and 4), and this chapter is the strongest in the thesis.
