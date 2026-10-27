# MPS_RD final audit — 2026-10-27

Status: FINALIZED PREPARATION PACKAGE. Not a thesis dataset and not
thesis results. Two items remain outside Muse's power to finalize:
(1) supervisor approval of the title/design change, (2) independent
price verification (Merolagani browser check is running; NEPSE
official-close verification is not done). Do not cite any price
below as a verified NEPSE official close until that check lands.

## 1. Design locked (subject to supervisor approval)

- Title: Accounting Value Relevance Across Nepal's 2023 Banking
  Consolidation: Evidence from Selected Commercial Banks.
- Sample: GBIME, HBL, KBL, NIMB, NMB; FY2076/77-FY2081/82.
- Dependent variable MPS_RD: market price per share at the
  reporting-deadline window. Operational rule: first dataset
  close on or after the end of Chaitra in the fiscal year
  following the accounting year, within a 5-day window; if no
  valid trade within 5 days, the observation is MISSING, never
  carried forward.
- Legal anchor, verified: Banks and Financial Institutions Act,
  Section 59(2) requires publication of the audited balance
  sheet and profit and loss account within nine months of the
  next fiscal year. CORRECTION TO THE GUIDANCE WORDING: the
  statute does NOT name Chaitra. End-of-Chaitra is the
  operationalization (Shrawan to Chaitra = nine months), and
  must be written that way in the thesis, not as a statutory
  date.
- Post_t = 1 for FY2079/80-FY2081/82, 0 for FY2076/77-FY2078/79.
- Model 1: MPS_RD = alpha + bank FE + year FE + beta_E*EPS +
  beta_B*BVPS + eps. Model 2 adds delta_E*(EPS x Post) +
  delta_B*(BVPS x Post). Standalone Post is absorbed by year
  FE and is not estimated separately. Joint null:
  H0: delta_E = delta_B = 0, tested two-sided, interpreted as
  difference in association, NEVER as a causal merger effect.
- P/E excluded (mechanical: MPS/EPS). ROA replaces EPS in
  robustness, never alongside EPS. DPS only where dividend
  information was available by the price date, secondary only.

## 2. Calendar dates — CONFIRMED, not approximated any more

Baisakh 1 dates from two calendar sources (Nepali date
converter and Nepali New Year listings, agreeing on all six):
2078 = 2021-04-14, 2079 = 2022-04-14, 2080 = 2023-04-14,
2081 = 2024-04-13, 2082 = 2025-04-14, 2083 = 2026-04-14.
Therefore Chaitra-end targets, the day before each Baisakh 1:
Chaitra 2077 = 2021-04-13 (Tue), Chaitra 2078 = 2022-04-13
(Wed), Chaitra 2079 = 2023-04-13 (Thu), Chaitra 2080 =
2024-04-12 (Fri), Chaitra 2081 = 2025-04-13 (Sun), Chaitra
2082 = 2026-04-13 (Mon).
Weekday note: 2024-04-12 was a Friday, weekend under the
then Sunday-Thursday trading week, so the first trading day
was Sunday 2024-04-14, gap 2 days, explained, not an error.
2026-04-13 is a Monday under the Monday-Friday week in
force from 2026-04-06, so it is a trading day.

## 3. Price table — INDEPENDENTLY RECOMPUTED, matches exactly

Recomputed fresh from ~/workspace/nepse-data-check
(ShareSansar scrape, NOT NEPSE-direct). All 30 prices from
the first candidate table reproduced exactly, second run.
No duplicate dataset row on any of the 30 price dates
(dup_on_date = 1 for all 30; file-wide duplicates exist
elsewhere and were deduped, first row kept).

Clean under the 5-day rule: 28/30. Delayed, treated as
MISSING: HBL FY2077-78 (2022-06-06, 358.90, gap 54d,
suspension resumption) and NIMB FY2077-78 (2022-05-30,
367.70, gap 47d, suspension resumption). Clean split:
pre-period 13, post-period 15.

Full table in mps_rd_candidate_price_table.csv and
mps_rd_joined_panel.csv (joined to panel EPS/BVPS/DPS/ROA).

## 4. Join to panel — COMPLETE, with two standing flags

EPS (reported), BVPS (recomputed from year-end shares),
DPS, ROA present for all 30 rows; no missing panel values
in the join. Flags carried, not fixed silently:
- FY2078-79 price-entity mismatch: fundamentals are
  pre-merger entities, April 2023 prices are post-merger
  entities for GBIME, HBL, KBL, NIMB (mergers completed
  Jan-Feb 2023). NMB unmerged, unaffected. This is a
  Pre-period contamination, not just a transition-year
  issue. Sensitivity excluding FY2078-79 is mandatory.
- BVPS vs printed NAV: HBL FY2076-77 recomputed 187.67 vs
  printed 187.72 (diff 0.05); NMB FY2081-82 recomputed
  175.18 vs printed 174.49 (diff 0.69). Panel values kept
  as recomputed; disagreements flagged, not overwritten.
- EPS-ROA collinearity on the clean MPS_RD sample:
  r = 0.975. Confirms: never put EPS and ROA together in
  the main model. ROA-replace robustness only.

## 5. Exploratory fixed-effects runs — EXPLORATORY ONLY

Computed with plain numpy OLS, classical and HC3 standard
errors, no statsmodels on this machine. These are NOT
thesis results: supervisor approval is pending, prices
are dataset closes, and the Merolagani check is still
running. Read the HC3 column, not the classical column,
at n = 28.

Model 1 (clean n = 28, k = 12, df = 16, R2 = 0.948):
EPS 2.095 (HC3 se 4.096, t 0.51); BVPS 0.219 (HC3 se 1.858,
t 0.12). Year fixed effects are large and significant
(HC3 t -3.6 to -8.4) because market-wide price levels
fall from 2021 to later years; they absorb most price
variation, leaving only within-year cross-bank variation
(5 banks per year) to identify EPS/BVPS. That is why
the FE slopes are far weaker than the earlier pooled
Ohlson run (EPS t 2.28). This is a power warning, not
a coding error.

Model 2 (clean n = 28, k = 14, df = 14, R2 = 0.978):
Pre EPS slope 5.577 (HC3 t 1.57); pre BVPS slope 0.100
(HC3 t 0.08); delta_E -3.124 (HC3 t -0.78); delta_B
-1.758 (HC3 t -1.43). Implied post slopes: EPS 2.453,
BVPS -1.658. The negative post BVPS slope is NOT
interpretable as a real valuation finding at this
precision; it is an artefact-prone estimate. Classical
joint F(2,14) = 9.57 overstates the case: under HC3
neither interaction is significant. DO NOT claim
rejection of H0: delta_E = delta_B = 0 on this run.

Sensitivities (Model 2 form):
- Exclude FY2079-80: n = 23, df = 10, delta_E -2.578
  (HC3 t -0.47), delta_B -1.880 (HC3 t -1.33).
- Exclude FY2078-79: n = 23, df = 10, delta_E -2.436
  (HC3 t -0.51), delta_B -2.611 (HC3 t -1.72).
- Exclude both: n = 18, df = 6, HC3 standard errors
  explode (hundreds), results NOT interpretable.
  This sample cannot support both exclusions at once.
- ROA replaces EPS (Model 1 form): ROA 24.398 (HC3
  t 0.38), BVPS 0.518 (HC3 t 0.30). Same power problem.
- DPS added to Model 1: DPS 1.769 (HC3 t 0.48), and
  DPS eligibility by each April price date is NOT yet
  verified row by row, so this run is indicative only.

Correlations on clean sample: price-EPS 0.358,
price-BVPS 0.217, price-DPS 0.082, price-ROA 0.378.

## 6. What is locked, what is not

LOCKED in this package: calendar targets, price rule,
5-day missing rule, 28 clean rows, 2 delayed missing
rows, joined panel, model equations, Post definition,
exclusion and robustness list, and every number in
sections 2-5 above, each recomputed and cross-checked
in this pass.

NOT locked, and must not be presented as locked:
- Supervisor approval of the title/design change.
- Merolagani independent price check (browser task
  running at time of writing; result to be appended).
- NEPSE official-close verification for any row.
- Disclosure-before-deadline proof per bank-year
  (a legal deadline does not prove compliance).
- DPS availability by price date, row by row.
- Literature citations in the guidance message
  (Gurung and Dahal 2025, Giri 2024, Kwon and Wang
  2020, Ohlson 1995): not verified from the message
  alone; locate and check each before citing.
- Final thesis regression: rerun only after approval
  and price verification, with the same code and
  the same flags, and report HC3, not classical
  significance, as the headline inference.

## 8. Merolagani independent check — COMPLETED 2026-10-27

Read-only check of all 30 MPS_RD price dates on Merolagani
public price-history pages, exact dates only, no nearby
date substituted, no sign-in/payment/download. Result:
29 matches, 1 mismatch, 0 no-rows, 0 blocked.
Full row-by-row file:
mps_rd_merolagani_verification.csv.

IMPORTANT LIMIT: Merolagani labels its column LTP (Last
Trade Price). A match confirms an aggregator LTP, NOT an
official NEPSE Close Price. NEPSE official-close
verification is still NOT done for any row.

The one mismatch, DO NOT silently fix:
- NMB FY2076-77, 2021-04-13: dataset close 437.0
  (dataset row: open 432.0, high 439.0, low 428.0,
  close 437.0) vs Merolagani LTP 436.00, difference
  1.00 NPR (0.23%). This row is DISPUTED, not verified.
  The joined panel still carries 437.0 as the dataset
  value, flagged here. Before thesis use, check a third
  source (ShareSansar history or NEPSE) for this date
  and record which value is used and why. Do not switch
  to 436.00 on Merolagani alone, and do not keep 437.0
  as verified. Impact on any regression would be tiny
  (one row, 1 NPR), but the verification status, not
  the size, is what matters.

All other 29 rows, including both delayed resumption
rows (HBL 2022-06-06 358.90, NIB 2022-05-30 367.70),
match Merolagani LTP exactly.


- mps_rd_candidate_price_table.csv (30 rows, with
  status and entity notes)
- mps_rd_candidate_price_table_README.md (warnings;
  its "approximate dates" warning is now superseded
  by section 2 above for the six targets)
- mps_rd_joined_panel.csv (30 rows joined to EPS,
  BVPS, DPS, ROA, with gap and entity flags)
- This audit: mps_rd_final_audit_2026-10-27.md

## 9. Smart checks 2026-10-27 — why brute force is NOT the plan

These checks use data already in the workspace, not a new hunt for 30 disclosure dates. That hunt was the MPS_post wall; MPS_RD does not need disclosure dates.

(a) Share-basis (bonus) adjustment. BVPS_adj = BVPS / (1 + bonus%) for each row, using panel bonus %. Model 2 with BVPS_adj, clean n = 28: pre EPS 5.775 (HC3 t 1.39), BVPS_adj 0.153 (t 0.09), delta_E -4.043 (t -0.91), delta_B_adj -1.533 (t -0.96). With EPS_restated (next-year previous column where it differs: only GBIME FY2076-77 17.99 -> 15.33 and NMB FY2077-78 16.66 -> 14.76 in the clean sample; HBL FY2077-78 restatement is in a delayed/missing row): pre EPS 5.578 (t 1.51), BVPS_adj -0.013 (t -0.01), delta_E -3.905 (t -0.93), delta_B_adj -1.533 (t -0.94). Conclusion: bonus adjustment does NOT rescue significance and does NOT change the direction of the interaction. It must still be documented in methodology, but it is not the reason the FE estimates are weak. Note: restatements do NOT follow a simple divide-by-(1+bonus) rule in general (HBL FY2077-78: own 28.07 vs restated 27.60 despite a 21.38% bonus), so no mechanical restatement rule may be invented; use reported/restated values as printed, and flag the restated rows.

(b) Sensitivity robustness. Excluding FY2078-79 and excluding FY2079-80 separately both leave delta_B negative and of similar size (classical t -4.01 and -2.11 respectively, HC3 t -1.72 and -1.33). The interaction direction is not driven by one year alone. HC3 significance is absent in every variant.

(c) Literature, verified in part. Dahal, Gurung and Ghimire, Interdisciplinary Journal of Management and Social Sciences, Vol. 6 No. 1, January 2025, DOI 10.3126/ijmss.v6i1.75407, "Impact of Financial Indicators on Nepalese Commercial Bank Stock Prices": 209 annual observations, FY2013/14-2023/24, all listed Nepalese commercial banks, variables including P/E, BVPS, dividend rate, earnings yield, market-to-book. This confirms the guidance claim that ordinary price-determinants work is already well covered in Nepal, and it is a real, citable precedent for the differentiation argument. It does NOT by itself prove the MPS_RD design; it only proves the routine model is crowded. Kwon and Wang 2020 and Giri 2024 were NOT verified in this pass and must still be located before citing.

(d) Source-definition decision (the smart alternative to a 30-row NEPSE hunt). Dataset vs Merolagani already agree on 29/30 LTPs. Chasing NEPSE official closes for all 30 rows through the flaky NEPSE filter would repeat the MPS_post wall. The defensible route is a supervisor decision: define MPS_RD in the thesis as the cross-checked aggregator closing price (dataset close, Merolagani LTP-checked), disclose that it is NOT claimed as an official NEPSE Close Price, and keep the one disputed row (NMB 2021-04-13) flagged until a third source resolves it. That decision, not more brute-force searching, is what unlocks selection of the new direction.

(e) Disclosure-before-deadline, by logic not by hunt. All disclosure dates actually found in this project (GBIME FY2077/78 Nov 2021, NIMB FY2080/81 Feb 2025, FY2081/82 Oct/Dec 2025) fall months before the following April deadline. A post-Chaitra disclosure would be a regulatory breach and would normally show as a delayed AGM; no such case is in the record for these rows, but this is a plausibility argument, NOT proof per row. Per-row proof remains open and must be stated as a limitation if the direction is selected without it.

Files added in this pass: mps_rd_joined_panel_bonusadj.csv (30 rows with BVPS_adj and bonus %), mps_rd_merolagani_verification.csv (30 rows).

## 10. Third-source resolution — NMB 2021-04-13, COMPLETED 2026-10-27

ShareSansar NMB price history, exact date 2021-04-13 only:
open 432.00, high 439.00, low 428.00, Ltp/Close 437.00,
% change 1.39, quantity 164,812, turnover 71,185,019.
This matches the dataset value 437.0 exactly, on every
field, and does NOT match Merolagani LTP 436.00.

Interpretation, stated honestly: ShareSansar is the
dataset's own source, so this check proves the scrape
was accurate, NOT that an independent source agrees.
The Merolagani 436.00 is best read as a last-trade
price differing from the close, or a Merolagani-side
1-rupee difference, not as proof the dataset is wrong.
Outcome: the NMB row is NO LONGER flagged as a scrape
dispute. Keep 437.0 as the dataset close, record
Merolagani LTP 436.00 as the differing label in the
thesis data notes, and do NOT claim either as a
verified NEPSE official close. With this, all 30
MPS_RD prices now match at least one aggregator
exactly (29 Merolagani + 1 ShareSansar-source), and
29 match two aggregators. The remaining selection
bar is no longer this row; it is the supervisor
source-definition decision and acceptance of the
exploratory framing in section 9(d).
