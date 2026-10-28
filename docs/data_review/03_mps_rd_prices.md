# Data review 3: MPS_RD prices and the dead MPS_post design

## Question

Are the prices used in the regression the prices the design claims
they are, and is the abandoned MPS_post design really abandoned?

## Method

- Compared every joined-panel price, price date, gap, post flag, and
  entity-mismatch flag to the accounting panel and to table A6.
- Counted clean versus excluded rows under the 5-day window rule.
- Read table A4 (30-row verification table) against the joined panel
  and against Chapter 3's corrected price-reconciliation text.
- Checked the panel's MPS_post columns (settled / pending /
  unavailable) against the thesis's claim that no regression is run
  on MPS_post.

## Findings: MPS_RD construction

- **Count: PASS.** 30 candidate rows in the joined panel; 28 clean
  (gap 0, 0, 0, or 2 days); 13 pre, 15 post; 2 excluded, never imputed:
  HBL FY2077/78 (first dataset close 2022-06-06, gap 54 days) and
  NIMB FY2077/78 (2022-05-30, gap 47 days). Both gaps are merger-
  related suspensions, and both rows stay missing in the analysis
  sample. No carried-forward, no interpolated, no stale price is
  used anywhere in the analysis sample.
- **Targets: PASS.** Chaitra-end targets 2021-04-13, 2022-04-13,
  2023-04-13, 2024-04-12 (Friday; first trading day Sunday
  2024-04-14, gap 2), 2025-04-13, 2026-04-13. All clean rows sit on
  the target date except the FY2079/80 cohort, which sits on
  2024-04-14 by the Friday rule. No clean row is more than 2 days
  from its target.
- **Entity mismatch: PASS.** Exactly four rows flagged, all
  FY2078/79, all merged banks (GBIME, HBL, KBL, NIMB). NMB FY2078/79
  is correctly not flagged. The flag means what the thesis says it
  means: April 2023 prices are post-merger entity prices paired
  with pre-merger standalone fundamentals, and those rows sit in
  the pre period. R6 (drop FY2078/79) is the correct sensitivity
  for this flag, and it is reported as a sensitivity, not as the
  baseline.
- **Symbol handling: PASS.** NIMB-series rows use NIB for FY2076/77
  and FY2077/78 windows and NIMB from FY2078/79, matching the
  listing history (Nepal Investment Bank became Nepal Investment
  Mega Bank on merger). Table A4's note states this; the joined
  panel's bank column uses NIMB throughout for series identity,
  which is correct for a series panel and must not be mistaken for
  a claim that the ticker was NIMB in 2021.
- **Dataset origin: PASS, with the limit stated.** The price dataset
  is the nepse-data-check clone (372 CSVs, present in the workspace),
  whose scraper pulls from ShareSansar, not from NEPSE. Prices are
  therefore ShareSansar dataset closes, cross-checked against
  Merolagani LTPs. They are not NEPSE official closes, and this
  review finds no place in the analysis outputs where they are
  claimed to be, except for the one A4 note issue below.

## Findings: verification table A4

- **Agreement: 29 of 30 match, 1 mismatch, as stated.** Dataset close
  equals Merolagani LTP on every row except NMB FY2076/77 (dataset
  437.00, Merolagani 436.00). The A4 table itself is correct on the
  numbers.
- **MUST FIX: A4's note.** A4's note says the NMB cell "was resolved
  by a third source at 437.00". The resolving record is ShareSansar's
  own full daily record (open 432, high 439, low 428, close 437.00).
  Because ShareSansar is the dataset's source, that record proves
  scrape accuracy, not independent agreement, and it is not a
  "third source" in the sense an examiner will read it (a source
  independent of both the dataset and Merolagani). Chapter 3 now
  states this correctly and explicitly. A4 must be corrected to
  match Chapter 3 exactly. Until then, A4 and Chapter 3 contradict
  each other on the single most scrutinised price cell, and an
  examiner who reads A4 first will conclude the thesis overclaims
  its verification.
- **FinancialNotices scope: PASS.** FinancialNotices Close checks
  cover only FY2081/82 (all five rows match exactly), because the
  FinancialNotices window reaches back only to 2025-10-28. The thesis
  does not claim FinancialNotices coverage for earlier years. Any
  future claim that FinancialNotices "verifies" the full price
  series would be false.

## Findings: MPS_post (the abandoned design)

- **Status: PASS (correctly dead).** Panel MPS_post: settled 2
  (GBIME FY2081/82 240.00, label LTP; NIMB FY2081/82 193, label
  Close), pending 3 (HBL, KBL, NMB FY2081/82 candidates, held by
  the author's 2026-10-27 decision, never promoted), unavailable 25.
  No analysis table, figure, or regression uses MPS_post. The
  joined panel does not contain MPS_post at all. The thesis's
  statement that MPS_post is not estimable (n = 2, df = -3 for a
  five-parameter model) is arithmetically correct.
- **Label honesty: PASS, with a standing caveat.** GBIME's settled
  240.00 is labelled LTP, not Close, and the panel note states
  openly that NEPSE Close was not verified for it. If 240.00 cannot
  be verified as the NEPSE close, the MPS_post appendix sample falls
  to n = 1. That caveat is stated in the panel and must stay stated
  wherever the settled pair is mentioned.

## Verdict for this file

MPS_RD prices: PASS, with one table-note fix (A4). MPS_post:
correctly dead, correctly labelled, correctly unused. The price
series is the weakest link in the thesis only because of its source
(aggregator cross-checks, not NEPSE official closes), not because
of any error in its construction, which recomputes cleanly.
