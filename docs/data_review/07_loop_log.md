# Data review: 10-pass loop log (2026-10-28)

The first Phase 1 pass was not enough to sign off a thesis that decides
a degree. On the author's instruction, the whole audit was run again as
a loop: 10 separate passes, each against the sources, each checking a
different layer. A pass is only counted when it actually ran and
produced evidence. This file is the log. Findings are numbered L1-L12
and are carried into `00_phase1_verdict.md`. Nothing in this log was
fixed in the thesis: the thesis chapters, tables, figures, and data
were not changed to write it. Fixes still need the author's approval
for the actual edit, in both the Markdown and the LaTeX version where
the error appears in both.

## Pass 1: Group vs Bank columns in the raw extraction

Method: every raw JSON in `data_extract/output/raw/` (30 files),
Group and Bank current-column balance-sheet identity recomputed,
panel Bank values compared to raw Bank values where raw is present,
attributable-vs-total equity compared.

Result: Bank identities exact, panel Bank matches raw where raw is
present. Two real findings:

- L1 (extraction field error, Group only): GBIME Group total equity
  in the raw files equals equity attributable to equity holders and
  omits non-controlling interest (NCI). Group identity therefore
  fails for all 6 GBIME years by exactly the NCI amount. Proven for
  FY2076/77: gap 211,277,477, and the SOFP text layer on pp. 81-82
  shows an NCI line of exactly 211,277,477. The other five gaps
  (504,706,906; 562,092,282; 669,443,650; 599,656,913; 686,311,598)
  are consistent in magnitude but were NOT individually verified
  against their NCI lines in this pass, and are not claimed as
  proven. Bank columns, the panel, and every regression value are
  unaffected, because the thesis uses Bank columns. What is affected
  is any claim that both Group and Bank columns are fully verified:
  for GBIME Group equity, that claim is false as the raw files stand.
  Fix: correct GBIME Group total equity to attributable plus NCI in
  the raw files, or state plainly that the panel is Bank-only and
  Group equity is not used.
- L2 (not an error, recorded so it is not misread): HBL and NMB
  Group rows DO separate NCI (attributable != total in 8 Group rows),
  and their Group identities pass. Raw None cells are confined to
  the known manual-correction rows (HBL/KBL FY2076/77,
  NMB FY2076/77 previous columns, NMB FY2077/78 and FY2079/80
  previous PAT), where the panel value comes from the documented
  manual correction, not from raw.

## Pass 2: Prior-year continuity and EPS restatements, all transitions

Method: for all 25 bank transitions, next-year previous column
compared to prior-year own current column, for total assets, PAT,
and EPS, from raw JSONs and the panel.

Result: PAT continuity exact wherever raw is present. Total assets:
19/25 exact zero, 6 deviations. Five were already disclosed
(GBIME FY2078/79 718,438,769; HBL FY2080/81 1,877,083,471 Civil
merger; KBL FY2079/80 1,047,386,219 NCC merger; KBL FY2076/77
-7,369,687,548, where the own-report visual read supersedes the
next report's previous column). One was not previously listed:

- L3 (small, previously unlisted restatement): KBL FY2077/78 to
  FY2078/79 total assets differ by 9,587,393 (0.005%). Immaterial,
  but it belongs in the restatement list so the list is complete.
- EPS restatements: exactly 3 in the 30-row dataset, no others
  hidden. GBIME FY2076/77 17.99 to 15.33, HBL FY2077/78 28.07 to
  27.60, NMB FY2077/78 16.66 to 14.76. Every other transition has
  own EPS equal to next-year previous EPS. This confirms the R8
  substitution set (2 in-sample rows, HBL out-of-sample) is
  complete, and that the blank previous-EPS cell for NMB FY2076/77
  is correctly left blank, not invented.

## Pass 3: DPS, all 30 entries, quotes, pages, announcement dates

Method: every entry in `config/dps.json` inspected (cash, bonus,
DPS, status, PDF page, printed page, method, quotation length);
every row of `mps_rd_dps_announcement_dates.csv` checked against
its MPS_RD price date.

Result: 30 entries, every quotation present (length 63-302
characters), 2 visual reads (HBL FY2076/77, NMB FY2079/80), rest
text reads. All 30 announcement dates precede their price dates.
Two notes:

- L4 (file hygiene, no value impact): the announcement CSV has a
  malformed row. The NIMB FY2081/82 note contains an unquoted
  comma, so a CSV reader splits it into an extra field and
  truncates the note. The date, price date, and before-price flag
  are correct; only the note text is truncated. Quote the field
  or remove the comma.
- Timing for nil DPS rows is not load-bearing: a documented-nil
  DPS is 0 regardless of announcement date, so the timing check
  matters for the 18 proposed rows, and all 18 pass. The NIMB
  FY2077/78 corrected declaration (12.611% bonus, 3.389% cash,
  2021-10-20) is the panel value, not the first declaration
  (11.24% / 4.76%); both precede the price date.

## Pass 4: MPS_RD calendar, volumes, dataset vs Merolagani file

Method: every joined price date checked for weekday and trading-day
status; every dataset close re-read directly from the
`nepse-data-check` CSVs (ShareSansar scrape, 372 files) for the
6 target dates per symbol; Merolagani verification file read
in full.

Result: no new error. All 30 price dates fall on Nepal trading
days (Sunday-Friday, no Saturday). The 2024-04-14 Sunday dates
are correct: Chaitra-end 2024-04-12 was a Friday, so Sunday is
the first trading session, gap 2. Dataset closes match the
joined panel on every target date, with traded quantities
present (so these are traded days, not carried-forward closes).
Merolagani file: 29 matches, 1 mismatch (NMB 2021-04-13,
437.00 vs 436.00), exactly as recorded. Symbol handling is
correct: NIB for NIMB FY2076/77-2077/78, NIMB from FY2078/79,
NIB file empty on later target dates. This pass does NOT change
the standing limit: matching a ShareSansar scrape against
Merolagani LTP is cross-aggregator agreement, not NEPSE
official-close verification, which has still never been done.

## Pass 5: Analysis pipeline code vs tables

Method: `stats/models.py`, `stats/wald.py`,
`stats/robustness.py`, `dataset.py`, and `loaders/panel.py` read
line by line; formulas, fixed effects, df accounting, and
robustness definitions compared to tables T3, T4, T5, A5.

Result: code is correct. `_fit` uses `fit(cov_type="HC3",
use_t=True)` in every specification. Model 1 formula
`price ~ eps + bvps + C(bank) + C(fy)` (k = 12, df 16); Model 2
adds `eps:post + bvps:post` (k = 14, df 14); Post main effect
absorbed by year dummies, as stated. Wald uses `f_test` on the
two interaction terms under the fitted HC3 covariance. R3/R4/R5/
R6/R7/R8 definitions in code match their T5 notes, including
R4 df 14 to 13 and R6 excluding FY2078/79. One conceptual note:

- L5 (clarification, not a numeric error): R7 divides BVPS by
  (1 + bonus%) where bonus% is that fiscal year's proposed
  bonus, which is issued in the following year. BVPS_adj is
  therefore a pro-forma forward adjustment, not a restated
  year-end BVPS. Add one sentence saying so, or the reader
  will assume the bonus was already in the year-end share count.

## Pass 6: All figures F1-F6 and A1-A3, code vs rendered vs captions

Method: generation code read for all 9 figures; sample used by
each figure checked (panel n = 28 vs panel_all n = 30).

Result: no new numeric error. F1 and F2 use the clean panel
(n = 28). F4 refits Model 2 and builds post slopes by
`t_test("eps + eps:post = 0")` under the HC3-t fit, so its
intervals are t-based. A2 correctly omits R3 (ROA scale) with
the omission stated in its footnote, and its title's "n = 28
unless noted in T5" covers R5/R6 (n = 23). F6 uses all 30 rows
with open markers for the 2 excluded prices and a footnote
stating the exclusion; its price line does connect through the
open markers, which is the only visual softness, already noted
in Phase 1. F5/A3 diagnostics refit Model 1 / Model 2 on the
clean panel. The F3 warning from Phase 1 stands unchanged.

## Pass 7: Thesis chapters Ch1-Ch5 numbers vs analysis tables

Method: every headline number in the Markdown chapters grepped
and compared to T1-T5 and the joined panel; DPS collapse,
descriptives, and R6 values recomputed from the panel.

Result: one genuine text value error, and all other headline
numbers confirmed. DPS means recompute exactly: pre 6.06
(0 zeros), post 1.40 (12 zeros), full 3.56; reduction 76.90%.
Model 1, Model 2, Wald F = 2.954 p = 0.085, R6 F = 5.82
p = 0.021 with delta_B SE 1.517, all match T3/T4/T5. The error:

- L6 (WRONG NUMBER IN THE THESIS TEXT, both versions): Chapter 3
  section on R8 says HBL FY2077/78 was "reported 29.80, restated
  27.60". The raw files prove otherwise. HBL FY2077/78 Bank EPS
  as printed is 28.07 (raw `bank_current`), Group EPS is 29.24,
  and the next report's previous Bank column is 27.60. The
  value 29.80 appears nowhere in the raw extraction for HBL in
  any year. Correct text: "reported 28.07, restated 27.60".
  Impact is contained, and must be stated plainly: the R8
  regression itself uses the correct restated value 27.60 from
  `configs/base.yaml`, and the HBL row is window-excluded
  anyway, so no table changes. But the sentence as written is
  a wrong number in the methodology chapter, exactly the kind
  of error an examiner catches, and it must be fixed in both
  the Markdown and the LaTeX chapter before submission.
  No other restatement number in that paragraph is wrong:
  GBIME 17.99 to 15.33 and NMB 16.66 to 14.76 both check out.

## Pass 8: Cross-file contradiction sweep

Method: full-text grep across `docs/draft/thesis/` and
`src/thesis/chapters/` for NEPSE-verification claims, causal /
conclusive language, "merger negotiations", "tripartite",
"zero error", Stata/SPSS, and the A4 note.

Result: NEPSE language in Chapter 3 is now correct in both
versions (aggregators named, official closes stated unverified).
Causal language in Chapter 2 is theory (Ohlson, Miller-Modigliani),
not a claim about the thesis results, and Chapter 4 correctly
says the patterns are "not as proven causal effects". No
"tripartite", "zero error", Stata, or SPSS claim remains. Three
wording items survive, because Chapter 3 was fixed but Chapters
1 and 4 were not:

- L7 (wording, Chapters 1 and 4): "trading suspended during
  merger negotiations" appears in Chapter 1 (twice: the SEBON/
  NEPSE implications bullet and the sample paragraph) and
  Chapter 4 ("NEPSE regulations historically enforced extended
  trading halts during merger negotiations"). The HBL-NIB merger
  was rejected at the 29th AGM on 14 January 2022, months before
  the April-June 2022 suspension window, so "during merger
  negotiations" misdates the suspension. Change all three to
  "merger-related suspension", matching Chapter 3.
- L8 (unverified institutional claim, Chapter 4): the same
  Chapter 4 sentence asserts NEPSE regulations "historically
  enforced" extended halts during merger negotiations. No NRB
  order or NEPSE rule is cited for the HBL/NIB post-rejection
  suspension in this thesis. Either cite the specific rule or
  soften to "trading remained suspended" without attributing a
  regulatory mechanism.

## Pass 9: LaTeX tables and chapters vs Markdown

Method: numeric sets extracted from every T/A table in .md and
.tex and compared; chapter spot numbers compared across versions.

Result: table numeric sets are identical for T1, T2, T3, T4, T5,
T6, A4, A5, and A6 (no md-only or tex-only decimal in any table).
Chapter numbers match across versions, including the error:
the 29.80 error (L6) is present in BOTH the Markdown and the
LaTeX Chapter 3, and the "merger negotiations" wording (L7) is
present in BOTH versions of Chapters 1 and 4. Any fix must
therefore be applied in both versions, as was done for the
four minor items in e2b6a96. No LaTeX-only or Markdown-only
numeric divergence was found in this pass.

## Pass 10: Pipeline tests and independent rerun

Method: analysis test suite run in the available venv; dataset
tests run separately; descriptives recomputed from the joined
panel with plain statistics, not the thesis pipeline.

Result: descriptives recompute exactly (pre DPS 6.06, post 1.40,
full 3.56; pre price mean 310.59, post 205.60, full 254.34;
pre EPS mean 17.90, post 10.72). Test suite status, stated
honestly:

- L9 (reproducibility, not a numbers error): the full analysis
  test suite cannot run in this VM's venv. `test_dataset.py`
  passes 11/11, but `test_stats.py` and `test_registry.py`
  fail at collection because `scipy` (and `statsmodels`) are
  not installed in that venv. The pipeline code was still
  verified by reading it (Pass 5) and by the independent NumPy
  recomputation (Phase 1), but a future reproducer needs a
  venv with the analysis dependencies installed, and that
  requirement is not documented in the repo alongside the
  manifest. This joins the Windows-path manifest item (Phase 1
  item 5): reproduction from the manifest alone is not possible
  on another machine.

## Loop verdict

Ten passes, ten sets of evidence. The loop found what the first
pass missed: one wrong number in the thesis text (L6), one
Group-column extraction error (L1), one unlisted small
restatement (L3), surviving misleading wording in Chapters 1
and 4 (L7, L8), two clarifications (L5, and the DPS timing note
in Pass 3), and two file/reproducibility items (L4, L9).
No panel value, no price, no DPS value, no regression
coefficient, and no table number was found wrong in any pass.
The data still pass, and the thesis text now has a corrected
fix list that is longer and more honest than the first pass
produced. The reviews are finalized on this basis: the fix
list in `00_phase1_verdict.md` (items 1-5 from Phase 1 plus
items 6-12 from this loop) is the complete list this loop
produced, and no further pass in this loop found anything
beyond it. Finalization means the review is complete, not
that the fixes are applied: every fix still needs the
author's approval for the actual edit.
