# Candidate price table — NOT the panel, NOT a method change

File: `mps_candidate_price_table.csv` (30 rows, built 2026-10-27 from the
verified accounting panel + the GitHub nepse-data dataset).

## What it is
A preparation table for the fixed-date idea in the plan pasted 2026-10-27:
- Ashadh-end price: last dataset close on or before the Ashadh-end
  target date for that fiscal year.
- Poush-end price: last dataset close on or before the Poush-end
  target date (mid-year check).
- Disclosure price: only the two settled panel rows (GBIME, NIMB
  FY2081-82) and the three pending candidates, marked as such.
Fundamentals (EPS, DPS, BVPS, ROA) are copied from
`output/tidy/accounting_panel.csv`. Nothing in this file has been
merged into the panel. Using Ashadh-end or Poush-end as the primary
dependent variable would change the proposal's MPS_post definition
and needs the supervisor's approval first.

## Target dates used (BS -> AD conversions, confirm against a Nepali
calendar before thesis use)
Ashadh-end: FY2076-77 2020-07-15, FY2077-78 2021-07-15,
FY2078-79 2022-07-16, FY2079-80 2023-07-16, FY2080-81 2024-07-15,
FY2081-82 2025-07-16.
Poush-end: 14 January of the second calendar year of each FY
(2020, 2021, 2022, 2023, 2024, 2025). A +/-1 day target shift only
changes a price if a trading day falls between the two dates.

## Dataset provenance (verified 2026-10-27, clone in ~/workspace/nepse-data-check)
- Source: https://github.com/Aabishkar2/nepse-data, 372 company CSVs,
  README columns published_date/open/high/low/close/per_change/
  traded_quantity/traded_amount/status. No statement in the README
  or code about raw vs adjusted prices.
- Origin chain: the scraper code pulls from ShareSansar
  (sharesansar.com/company-price-history and /today-share-price),
  NOT directly from NEPSE. Cite ShareSansar via the dataset, not
  NEPSE directly, unless a price is spot-checked on NEPSE itself.
- Duplicate dates exist in the files (e.g. GBIME 2012-10-01 twice);
  this table dedupes by date (first row kept).
- Raw, not adjusted: verified on NABIL 2017-09-12, close 1191.0 vs
  previous close 1630.0, per_change -26.93% (the plan's 26.9% claim).
  Spot check verified: NABIL Jul 2015–Jul 2019 max close 2700.0,
  min close 682.0, max high 2794.0, min low 678.0 — exactly the
  plan's four numbers.

## Gaps and flags (read before using any price)
- Gap days >5 are flagged in the `flags` column. A price more than
  5 days before its target is stale, not a target-date price.
- HBL and NIB have a dataset gap May 2021–mid 2022 (HBL: last
  2021-05-12 at 487.0, next 2022-06-06 at 358.9; NIB: last 2021-05-12
  at 453.0, next 2022-05-30 at 367.7). A year-long halt for a major
  bank is implausible as a market suspension and looks like a
  scrape gap — do NOT use dataset prices inside that window
  without a Merolagani/NEPSE check.
- GBIME gap 2022-06-15 (251.4) to 2022-12-07 (221.4), 175 days:
  consistent with the Bank of Kathmandu merger suspension, but
  the reason was not verified from a merger notice in this pass.
  This corrects the earlier Nov–Dec-only gap description: the
  suspension starts in June, not November.
- GBIME gap 2019-07-04 to 2020-01-20 (200 days): Poush Jan 2020
  price is absent from the dataset.
- 2020 Mar–Jun gaps (51 + 47 days) appear for all five banks:
  consistent with COVID market closures.
- NIMB pre-merger years use NIB; NIMB file starts 2023-02-23,
  NIB ends 2023-01-10. The NIMB FY2079-80 Poush price is
  unavailable in the NIMB file and must not be filled with the
  pre-merger NIB price (swap 100:90).

## Share-basis scan (2026-10-27, file mps_share_basis_scan.csv)
For each candidate price, the scan records the price-day and next-day
percentage change and any drop of -9% or worse in the next 20
TRADING days. Trading-day windows mislead inside gaps, so read
them with calendar dates attached: the -9.99% drops in June 2022
for HBL/NIMB and the -9.29% GBIME drop on 2022-12-07 are
resumption drops after the long suspensions above, not clean
ex-bonus drops the day after a price date. The August 6, 2024
-9% drops for HBL/NIMB are market-wide-looking, not bank-specific.
No clean ex-bonus-style drop was found immediately after a
candidate price date in calendar terms. This scan does NOT replace
checking each bonus ex-date against each price date from bonus
announcements — that announcement check is still open.

## HBL/NIB gap check on Merolagani (2026-10-27, browser check, Q1 only)
Merolagani price history shows the SAME gap as the dataset, so the
gap is not a GitHub-only scrape error:
- HBL: no rows on 2021-07-15, 2021-10-15, 2021-12-15, 2022-01-14,
  2022-03-15, 2022-05-15. Boundary rows match the dataset exactly:
  2021-05-12 LTP 487.00 and 2022-06-06 LTP 358.90.
- NIB: no rows on 2021-07-15 and 2022-01-14. Merolagani table jumps
  from 2021-05-13 LTP 460.00 directly to 2022-05-30 LTP 367.70.
- Announcement titles reviewed give NO reason for a year-long
  halt. Relevant items, titles only: HBL 2022-01-03 adjusted price
  398.75 for 21.38% bonus on a previous close of 484.00
  (484 x 100/121.38 = 398.75, exact); HBL 2022-06-06 "Transactions
  Release Except Basic Shareholders"; NIB 2021-11-22 adjusted
  price 408.49 for 12.611% bonus on a previous close of 460.00
  (exact); NIB 2022-02-15 listing of those bonus shares;
  NIB 2022-05-30 "Transaction Release" on the resumption date.
  The reason for the preceding halt was NOT stated in the titles
  reviewed and is NOT guessed here. Merolagani alone does not
  prove a real suspension, but two independent aggregators
  showing the same gap makes a dataset-only error unlikely.
- ShareSansar price-history check and the NEPSE daily report for
  GBIME on 2022-11-16 were NOT completed in that browser session
  (session ended first) and remain open.

## Gap check completed (2026-10-27, continuation)
- ShareSansar price history now also checked: HBL no rows on
  2021-07-15, 2022-01-14, 2022-03-15 (3,273 total entries, control
  2026-10-26 Ltp 202.00 returns a row); NIB no rows on 2021-07-15,
  2022-01-14, 2022-03-15 (2,338 total entries). Correction to
  earlier wording: the dataset IS a ShareSansar scrape, so this
  is two aggregator sources (Merolagani and ShareSansar), not
  three independent ones. The gap is still not unique to the
  dataset, but it does not by itself prove a real suspension,
  and no announcement title reviewed gives a reason.
- NIB Transaction Release detail (2022-05-30) was viewed: it
  concerns release of securities trading except for basic
  shareholders effective 2079/02/16 and states no merger or
  other reason for the preceding halt. HBL's 2022-06-06
  Transactions Release detail was NOT opened (optional).
- GBIME on 2022-11-16 from NEPSE: NOT VERIFIED. NEPSE Today's
  Price filter did not apply the 2022-11-16 date (table stayed
  on Oct 26, 2026); calendar-picker clicks on the 2022 cell did
  not change the dialog in four attempts; Downloads pages 1-2
  contain general documents only, no daily market report for
  that date identified; Floor Sheet shows current-day contracts
  only and cannot select 2022-11-16. So NEPSE shows no GBIME
  close, no suspended status, and no omission finding for that
  date in this check. The GBIME Jun-Dec 2022 gap and Dec 7
  close 221.4 remain dataset/Merolagani context, not NEPSE
  findings.

## Correction from Krishna's own dataset check (2026-10-27)
Verified against the local dataset clone, all symbols counted:
- 2022-01-14: 0 symbols traded. Market-wide closure, NOT an
  HBL/NIB gap date. Remove it from the gap evidence list; the
  Merolagani/ShareSansar "no row" on that date is expected.
- 2021-07-15: 177 symbols traded, KBL/NMB/GBIME present,
  HBL and NIB absent. Stock-specific absence, confirmed.
- 2022-03-15: 190 symbols traded, KBL/NMB/GBIME present,
  HBL and NIB absent. Stock-specific absence, confirmed.
- 2022-11-16: 199 symbols traded, HBL/NMB/NABIL present,
  GBIME and KBL absent. Market was open, GBIME had no trade
  row that day in the dataset. This is still NOT a NEPSE
  finding on whether NEPSE lists a close for GBIME that day.

## CORRECTIONS from third-party critique verification (2026-10-27, news sources)
- HBL/NIB halt reason NOW VERIFIED (was "no announcement title reviewed
  states it" — that scope was titles reviewed, not all sources):
  HBL and NIB signed a merger MoU/agreement 13 May 2021; NEPSE
  suspended trading of both from 13 May 2021; HBL shareholders
  rejected the proposal at the 4 Jan 2022 AGM; NIB trading resumed
  30 May 2022 and HBL trading resumed 6 Jun 2022, in both cases to
  the general public except basic/core shareholders. Sources:
  Himalayan Times 14 Jan 2022, Khabarhub Jun 2022, ShareSansar
  30 May 2022. Minor discrepancy noted, not hidden: news reports
  give HBL last price 484 as of 13 May 2021, while the dataset's
  last HBL row is 12 May 2021 at 487.00 — the suspension date and
  the reason are consistent; the one-day/one-price difference is
  not resolved here.
- GBIME Nov 2022 suspension NOW VERIFIED in substance: GBIME and
  Bank of Kathmandu signed a merger MoU 16 Jun 2022 (swap 1:1) and
  trading was suspended; trading resumed 7 Dec 2022 except basic
  shareholders. So 16 Nov 2022 had no GBIME trade and no close is
  expected. This is a news-source finding, NOT a NEPSE daily-report
  record — the NEPSE filter check itself still failed, as stated.
  One ShareSansar item says halted "from 15 Oct 2022", which does
  not match the dataset (no GBIME rows Jun-Dec); the June MoU
  suspension is the one consistent with the dataset.
- NMB Nepal Samacharpatra Mangsir 26 claim NOT VERIFIED: a search
  found no such notice, and Mangsir 26, 2082 is about 12 Dec 2025
  (Mangsir 1 = 17 Nov 2025), not 16 Dec 2025 (Poush 1). A Mangsir 26
  notice, even if it existed, would not prove the 16 Dec summary
  statement publication. The cover-letter-only status stands.
- GBIME FY2077/78 book close 29 Nov 2021 VERIFIED (Merolagani
  announcement id 40885: book close 2021/11/29, cash 3.5%, bonus
  10%). Note: book close is not itself the ex-date; the ex-date
  still needs the settlement rule applied. NMB FY2076/77 book
  close 31 Dec 2020 and NIMB FY2076/77 book close were NOT
  verified in this pass.
