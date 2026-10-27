# Exploratory analysis — CANDIDATE Ashadh-end prices ONLY, NOT the thesis analysis

Status: exploratory preparation for the fixed-date idea. It does NOT
change the proposal's MPS_post definition, it is NOT merged into
the panel, and it must NOT be presented as the thesis result
without the supervisor's approval of the fixed-date primary rule.

Sample: Ashadh-end prices from mps_candidate_price_table.csv,
clean rows only (price date within 5 days of the Ashadh-end
target): n=26/30. Excluded for staleness: GBIME FY2078-79 (31d
early), HBL FY2077-78 (64d), NIMB FY2077-78 (64d),
NIMB FY2078-79 (36d). Target dates are the BS->AD conversions
documented in mps_candidate_price_table_README.md.

Headline results (full output in mps_exploratory_analysis.txt):
- Price vs EPS r=0.530, vs ROA r=0.557, vs BVPS r=0.242,
  vs DPS r=0.286.
- EPS vs ROA r=0.974 — near-perfect collinearity. VIF in the
  extended model: EPS 30.87, ROA 27.52, BVPS 1.60, DPS 1.52.
  Consequence: EPS and ROA must NOT sit in the same regression
  without addressing this. The EPS coefficient flips sign when
  ROA is added (primary model +8.14, t=2.28 HC3; extended
  -13.54, t=-0.69). The extended model as specified in the pasted
  plan is therefore not credible on this sample.
- Primary model Price ~ EPS + BVPS: R2=0.285, adj R2=0.223.
  EPS coef 8.14 (HC3 se 3.58, t=2.28); BVPS coef 0.41
  (se 1.25, t=0.33, not distinguishable from zero here).
- Extended model Price ~ EPS + BVPS + DPS + ROA: R2=0.348,
  adj R2=0.224 — no meaningful gain over the primary model,
  and every coefficient is insignificant under HC3 once
  collinearity is present.
- Log-price primary model gives the same pattern
  (EPS t=2.41, BVPS t=0.39).

EPS restatement audit (panel, prev column in year t+1 vs current
in year t, blank prev excluded):
- GBIME FY2076-77: 17.99 vs next-year prev 15.33 — restated.
- HBL FY2077-78: 28.07 vs next-year prev 27.60 — restated.
- NMB FY2077-78: 16.66 vs next-year prev 14.76 — restated.
These rows need a share-basis note in any write-up: the panel
uses each year's own current EPS, per gate G5, so a restatement
does not overwrite an earlier year, but it does mean the EPS
series is not on a single unchanging share base across years.

Share-basis flags (Ashadh -> Poush price change, bonus % from
the panel): rows with bonus >=10% and a fall >5% are flagged
for an ex-date check (GBIME FY2077-78, NIMB FY2076-77,
NMB FY2076-77). Large Ashadh->Poush rises for HBL/NIMB
FY2078-79 (+62.8% / +70.9%) are dataset-gap artifacts: the
Poush price used there is the stale May 2021 pre-gap price,
not a January 2022 price. The bonus ex-date check against
announcements is still open.
