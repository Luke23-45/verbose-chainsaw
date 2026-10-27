# MPS_RD candidate price table — PREPARATION ONLY, NOT a thesis dataset

Built 2026-10-27 from the local nepse-data dataset clone
(~/workspace/nepse-data-check, ShareSansar scrape, NOT NEPSE-direct).

Rule tested: first dataset close on or after the approximate
Chaitra-end target in the fiscal year following the accounting
year (BAFIA Section 59(2) nine-month publication deadline,
Shrawan to Chaitra = nine months).

WARNINGS, all of which must be resolved before this table is
locked as a thesis dataset:
1. Chaitra-end AD dates here are APPROXIMATIONS (2021-04-13,
   2022-04-13, 2023-04-13, 2024-04-12, 2025-04-13, 2026-04-13).
   Confirm each against a Nepali calendar before thesis use.
   A +/-1 day shift changes almost nothing here (most gaps are
   0 or 2 days), but the dates must still be confirmed.
2. Prices are DATASET closes, not verified NEPSE official closes.
   Spot-check against NEPSE/Merolagani before calling any row
   a verified NEPSE close.
3. Two rows are DELAYED outside any short window: HBL FY2077-78
   (54 days, resumption 2022-06-06) and NIMB FY2077-78 (47 days,
   resumption 2022-05-30), both failed-merger suspensions.
   Under a 5-day window rule they are MISSING, giving n=28,
   not 30.
4. FY2078-79 price-entity mismatch: fundamentals are pre-merger
   entities, but April 2023 prices are post-merger entities for
   GBIME, HBL, KBL, and NIMB (mergers completed Jan-Feb 2023).
   NMB is unmerged and unaffected. This row needs a supervisor
   decision (keep with disclosure, or exclude as sensitivity),
   not a silent fix.
5. Disclosure-before-deadline is NOT proven by this table.
   A legal deadline does not prove a bank disclosed by it.
   Late-disclosure checks per bank-year are still open.
