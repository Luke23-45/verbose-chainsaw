# MPS_RD blocker audit v2 — data-only, supervisor ignored by instruction, 2026-10-27

Purpose: prove or kill the new MPS_RD direction on DATA grounds
alone, so that even if a supervisor selects it, no hidden
blocker like the MPS_post wall appears later. Every check
below uses data already in the workspace unless marked
browser-pending. Nothing here is a thesis result; all
regressions are exploratory.

## BLOCKERS CLEARED (with evidence)

1. Share-capital continuity / hidden rights or splits:
   PASS with two flags. Share-capital growth equals the
   previous year's bonus % exactly (to 0.00pp) in 20 of
   25 bank-year transitions. The four large deviations
   are exactly the Jan-Feb 2023 mergers: GBIME +47.33pp,
   HBL +58.99pp, KBL +78.27pp, NIMB +82.42pp above bonus.
   No other rights issue, split, or unexplained jump
   hides in the sample. This means no other share-basis
   event needs adjusting beyond bonus and the mergers.

2. Price-date volume and continuity: PASS for all 28
   clean rows. Traded quantity on clean price dates
   ranges 12,241 to 516,887 shares, amounts NPR 2.2
   million to 146 million. No clean price is a
   thin-trade artefact. Largest move from previous
   close on a clean date is +2.97% (HBL 2021-04-13);
   no clean date carries an ex-bonus cliff. The two
   delayed rows FAIL this test, which is why they stay
   missing: HBL 2022-06-06 quantity only 1,710 and
   -9.99%, NIB 2022-05-30 quantity 9,320 and -9.99%
   (resumption limit-down days, not deadline prices).

3. Outliers and influence: PASS, with a warning.
   Lowest EPS rows are real, not errors: KBL FY2080-81
   EPS 0.02 (price 206.03), HBL FY2081-82 EPS 0.60
   (price 208.50), KBL FY2079-80 EPS 1.97. Cook's
   distance in Model 2 FE is at most 0.490 (KBL
   FY2076-77), below the conventional 1.0 threshold;
   no single row dominates. Dropping KBL FY2080-81
   leaves Model 2 essentially unchanged (delta_E
   -3.10 vs -3.12, delta_B -1.74 vs -1.76); dropping
   HBL FY2081-82 also leaves it essentially unchanged.
   Low EPS is a real economic fact (profit collapse),
   not a data error to delete.

4. Bonus adjustment: CHECKED, does not change the
   story. BVPS_adj and EPS_restated variants give
   delta_E -3.91 to -4.04 and delta_B -1.53 to -1.76,
   same direction, still not HC3-significant. No
   mechanical restatement rule may be invented:
   HBL FY2077-78 restates 28.07 to 27.60 despite a
   21.38% bonus, so use printed/restated values only.

5. Sensitivity to transition years: CHECKED.
   Excluding FY2078-79 alone and FY2079-80 alone
   both leave delta_B negative and similar in size.
   Excluding both leaves df = 6 and HC3 errors in
   the hundreds: that sample cannot support both
   exclusions, and must not be presented as a result.

## BLOCKERS FOUND — NEW, not in the earlier audit

6. NMB is NOT a clean unmerged control before 2023.
   NMB share-capital growth FY2076-77 to FY2077-78
   is 17.02% against a 13.00% bonus, a +4.02pp gap.
   Cause found in the NMB FY2077-78 annual report:
   Chairman's statement, PDF page 8: NMB commenced
   unified operations post-acquisition of Kanchan
   Development Bank Ltd. from 23 August 2020. That
   acquisition's shares explain the extra ~0.57
   billion NPR of share capital. Consequence for
   MPS_RD: NMB FY2076-77 fundamentals end July
   2020 (pre-Kanchan), but its April 2021 price
   follows the August 2020 acquisition. The
   contamination is small (about 4% of share
   capital, versus 50-86% for the 2023 mergers)
   and must be disclosed, but it does NOT kill
   the design. Dropping NMB entirely collapses
   precision (Model 2 df falls to 9, HC3 t for EPS
   falls to 0.32) because NMB is the only
   never-merged-in-2023 bank; keep NMB with the
   Kanchan disclosure, do not drop it silently.

7. NIMB small unexplained gap: NIB share-capital
   growth FY2076-77 to FY2077-78 is 14.09% against
   a 13.00% bonus, +1.09pp (about 0.16 billion NPR).
   No cause found yet in this pass. Small, not a
   design killer, but it must be investigated or
   explicitly listed as an unexplained 1.09pp
   before thesis submission, not ignored.

8. SPECIFICATION FRAGILITY — the serious warning.
   The FE specification is not the only defensible
   one, and other specifications flip signs:
   - Bank + year FE (recommended): EPS pre 5.58
     (HC3 t 1.57), BVPS pre 0.10 (t 0.08),
     delta_E -3.12 (t -0.78), delta_B -1.76
     (t -1.43).
   - Pooled, no FE: EPS -4.72 (t -0.21), BVPS
     2.60 (t 1.20), delta_E +3.39 (t 0.15),
     delta_B -1.15 (t -0.48).
   - Bank FE only: EPS -9.06 (t -0.29), BVPS
     5.23 (t 1.58), delta_E +5.43 (t 0.20),
     delta_B -2.64 (t -0.86).
   The year FE absorbs the market-wide price
   level, which is why FE and pooled differ so
   sharply. This does NOT make the direction
   undoable, but it DOES mean the thesis cannot
   claim a robust interaction finding: the
   interaction is negative in the FE model and
   in every FE sensitivity, but it is never
   HC3-significant, and pooled/bank-only models
   disagree on the baseline slopes. Presenting
   only the FE model without this fragility
   table would be the next wall.

## STILL PENDING (browser loop, not stopped)

9. DPS proposal/announcement dates row by row vs
   each April price date (Merolagani dividend
   announcement check, browser task running).
   Until it lands, DPS robustness is indicative
   only. DPS timing for MPS_RD is structurally
   better than for year-end prices (proposals
   normally precede April), but that is not proof
   per row.

10. FinancialNotices Close check for the five
    2026-04-13 rows (browser task running).
    This is the only Close-labelled check in the
    MPS_RD window that FinancialNotices covers
    (its history starts 2025-10-28).

11. NIMB +1.09pp share-capital gap (item 7 above):
    investigate in the NIB FY2077-78 report or
    list as unexplained.

12. NEPSE official closes: still not verified for
    any row, by design of this audit. The
    direction is doable ONLY under the
    cross-checked aggregator price definition
    (dataset close, Merolagani LTP-checked,
    ShareSansar-checked for the disputed row),
    disclosed as such. If a future examiner
    demands official NEPSE closes, that is a
    new blocker, and it must be named now, not
    discovered later.

## VERDICT, data-only

DOABLE to build, run, and defend as an EXPLORATORY
value-relevance study with a clearly negative but
not HC3-significant interaction, full fragility
disclosure, and the Kanchan and FY2078-79 entity
limitations stated. NOT doable as a study claiming
a significant, robust merger-driven change in
value relevance, and NOT doable as an official-
NEPSE-close study, on the data in hand. No other
hidden share-capital event, thin-trade price,
outlier, or bonus artefact was found in this pass
that would kill the design outright. The loop
continues on items 9-11; items 9 and 10 are
browser tasks already running.

## UPDATE 2026-10-27 — FinancialNotices Close check, COMPLETED

All five FY2081-82 MPS_RD rows (2026-04-13) match
FinancialNotices CLOSE exactly: GBIME 238, HBL 208.5,
KBL 229, NIMB 210.7, NMB 248.4. No blocked rows, no
nearby date substituted. This matters because
FinancialNotices labels its column CLOSE, unlike
Merolagani's LTP label, so for these five rows the
dataset close is confirmed under a Close label by a
second aggregator. It is still NOT an official NEPSE
Close Price record, and that limit stands for all
rows, but the FY2081-82 price year is now the
strongest-verified year in the MPS_RD sample.

## UPDATE 2026-10-27 — NIMB +1.09pp gap, RESOLVED

NIB FY2077-78 equity statement, Group, PDF p46:
Balance at 1 Shrawan 2077 share capital
14,248,954,500; transactions in FY2077-78:
Business Combination 120,000,000 + Share issued
36,010,915 + Bonus shares issued 1,852,364,085
= total contributions 2,008,375,000; balance at
Ashad 2078 16,257,329,500, exactly matching the
panel. Bonus alone is 1,852,364,085 / 14,248,954,500
= 13.00% exactly. The 1.09pp gap is therefore
156,010,915 of non-bonus share capital (120,000,000
business combination + 36,010,915 share issued),
not an error and not a hidden rights issue of
material size. Item 11 is closed. Remaining open
loop item is DPS proposal dates only.

## UPDATE 2026-10-27 — DPS announcement dates, COMPLETED, LOOP CLOSED

Merolagani announcement check, all 30 rows, no blocked
rows, no not-found rows: every announcement date is
BEFORE its MPS_RD price date. 26 dividend declarations
+ 4 AGM-only fallbacks. Full file:
mps_rd_dps_announcement_dates.csv.

That means DPS is eligible for the MPS_RD robustness
model on all 30 rows by announcement timing (for the
28 clean rows, and also for the 2 delayed rows, whose
announcements are also before their April targets).
This is a genuine advantage of MPS_RD over MPS_YE:
with year-end prices DPS was not yet proposed; with
April prices it was, in every case checked.

Caveats recorded, not hidden:
- AGM-only rows: HBL FY2076-77 (2020-12-20, AGM detail
  shows 6% cash / 14% bonus) and NMB FY2076-77
  (2020-12-23, AGM detail shows 3.2% / 13%) do carry
  the dividend in the AGM detail itself. HBL FY2081-82
  (2025-12-24) and NIMB FY2081-82 (2025-12-24) are
  nil-DPS rows; their nil status comes from the panel
  DPS extraction, not from the AGM date alone. For
  NIMB FY2081-82, the 2025-12-22 no-dividend letter
  was correctly NOT used as a Merolagani FY81-82
  announcement because its detail fiscal-year field
  reads 080-081.
- NIMB FY2077-78: first declaration 2021-10-04
  (11.24% / 4.76%) was corrected 2021-10-20 to
  12.611% / 3.389%; the panel uses the corrected
  3.389. Effective proposal date for timing is
  2021-10-20, still before 2022-04-13.
- KBL FY2080-81: Merolagani announcement 2025-01-03
  supersedes the panel's old BOD-date note
  (2024-01-02, which predates the fiscal year) for
  TIMING only; the DPS value stays nil.
- HBL FY2079-80, HBL FY2080-81, NMB FY2079-80,
  NMB FY2080-81: Merolagani % fields were blank,
  but announcement dates are before price dates
  and panel DPS values (all 0) come from annual
  reports, so timing eligibility holds.
- Symbol trap avoided: a Himalayan Distillery
  (HBL) entry on 2025-12-23 was correctly excluded
  from HBL bank FY2081-82.

LOOP STATUS: with this check, every data-only loop
item is now closed or disclosed. The only remaining
limits are the ones that cannot be closed by data
work alone: NEPSE official closes (direction is
doable only under the disclosed aggregator-price
definition), specification fragility (interaction
never HC3-significant), and the FY2078-79 / Kanchan
entity disclosures. No further data blocker was
found in this loop.
