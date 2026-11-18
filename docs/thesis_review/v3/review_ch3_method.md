# Final independent pre-submission review (v3) — Chapter III + Appendices A & D

**Thesis:** *Value Relevance of Accounting Information Before and After the Banking
Consolidation Wave: Evidence from Nepalese Commercial Banks* — Asmita Subedi,
Triveni International College, MBS, Tribhuvan University, FOM, November 2026.
**Repo:** `~/workspace/verbose-chainsaw`, HEAD `2b4e10f`, working tree as it stands
(uncommitted changes present; the three in-scope files differ from HEAD — see §1).
**Review date:** 18 November 2026.
**Review file:** `docs/thesis_review/v3/review_ch3_method.md` (the only file created
by this review).

## 0. Scope and method

- **Scope.** Chapter III in full
  (`src/thesis/chapters/chapter_03_research_methodology.tex`, 395 lines),
  Appendix A in full (`src/thesis/appendices/appendix_a.tex`, 96 lines),
  Appendix D in full (`src/thesis/appendices/appendix_d.tex`, 425 lines).
  Other chapters, appendices, code, and data were consulted only where Chapter III
  or Appendix D points at them, and only to check that a pointer resolves or that
  a printed value matches its named source. Statistics were **not** re-audited;
  data values are treated as correct except where this review checks a printed
  table against its named source file (text-vs-source consistency only).
- **Part A** verifies the fix loop's patches for the v2 findings in this scope,
  extracted from `docs/thesis_review/v2/content_review.md` §10 and
  `docs/thesis_review/v2/review_ch3_method.md`, using the hallucination audit's
  corrected versions (`docs/thesis_review/v2/verification_audit.md`) where they
  exist. The loop's claim log (`~/workspace/review-audit-scratch/loop-v2/`) was
  read **only** to know what the loop claims it did; it is never used as evidence
  for any thesis fact. Every verdict below rests on a grep, count, or comparison
  re-run by this reviewer against the thesis source (or, for the two new tables,
  against the named source files).
- **Part B** is a fresh read of Chapter III + Appendices A and D as they now stand,
  including new issues introduced by the loop's patches.
- **Status vocabulary.** VERIFIED — established by reading the cited file, opening
  the cited source, or cross-checking two locations; INFERRED — follows from
  verified facts plus an explicit argument; UNVERIFIED — could not be checked with
  the access available, and no position is taken on the underlying fact.
  Fix verdicts: FIXED / PARTIALLY FIXED / NOT FIXED / INCORRECTLY FIXED /
  FALSE FINDING.
- **Severity.** Critical = invalidates or materially re-frames a headline claim;
  Major = substantially weakens a reported result or misstates the method;
  Minor = local error, inconsistency, or omitted caveat that does not reverse a
  conclusion; Suggestion = improvement, not a defect.
- **Revision scale.** Narrow = a sentence, a number, or a citation; Substantive =
  a reworked paragraph, table, or section; Fundamental = a redesign of the method.
- **Rules observed.** Read-only throughout: no thesis, code, data, config, v1, or
  v2 file was modified, renamed, deleted, or reformatted. No PDF build, no commit,
  no push, no supervisor-bound text, nothing sent. No reason, judgement, or fact
  is attributed to the researcher that she did not state; where no reason is given,
  this review says so plainly.
- **Line references.** `ch3` = chapter 3 file, `app_a` = Appendix A, `app_d` =
  Appendix D. Line numbers are 1-based lines of the working-tree files as read.
  Working-tree diff for the three in-scope files vs HEAD `2b4e10f`:
  `appendix_a.tex` 4 lines changed, `appendix_d.tex` 119 lines changed,
  `chapter_03_research_methodology.tex` 69 lines changed (139 insertions,
  53 deletions across the three files).

## 1. Verdicts

### (i) Chapter III — **Ready with minor revisions**

All assigned Chapter III fixes are present except the two deliberately untouched
standing limitations (M01; the five-day rationale, m35, where no rationale was
invented) and two partial fixes (m30 calendar citation; s10 exact versions).
The two new Appendix D tables reproduce their sources exactly (m26, m27/m51).
The remaining defects in scope are narrow: two partial fixes, one presentational
inconsistency between the two new/existing price-date columns (N-01), and one
ambiguous sentence (N-02).

### (ii) Appendices A and D together — **Ready with minor revisions**

Appendix A is unchanged in substance except the M11 caption move; its 30-cell
price audit still agrees cell-for-cell with Chapter III Table 3.1 (re-checked
programmatically, §4). Appendix D's register arithmetic re-checks exactly
(5,663 pages; 328.31 MB), its two new tables match their sources 30/30, and its
sample log still reconciles 30 → 28.

## 2. Part A — Verification of the loop's fixes for the v2 findings in scope

Assigned findings: V2-M01 (Ch3:29 limb only), m24–m35, m38, m39, m51 (App D
part only; the App B part is another scope's), s10–s12. Two further in-scope
v2 items the loop also patched are verified here as extras: m08 (Ch3 part) and
M11 (Ch3/App A caption part). Tally for the 19 assigned findings: **15 FIXED,
3 PARTIALLY FIXED, 1 NOT FIXED (deliberately, as a standing limitation),
0 INCORRECTLY FIXED, 0 FALSE FINDINGS.**

| ID | Audit verdict | Loop's claimed fix | My verification | Evidence (file:line + exact excerpt) |
|---|---|---|---|---|
| V2-M01 (Ch3 limb) | CONFIRMED | NOT PATCHED (standing limitation; no reason to be invented) | **NOT FIXED — by design.** The exclusion sentence is untouched and no reason for excluding Prabhu–Century is stated anywhere in Ch3 or the appendices. VERIFIED. | ch3:31: "(the fifth, Prabhu Bank's acquisition of Century Commercial Bank \citep{nrb2023bsr}, is not sampled)". `grep -c Prabhu` across all five appendices: 0; in ch3: 1 hit (this sentence). No sentence in §3.3 gives a reason for the exclusion. |
| V2-m24 | CONFIRMED | Ch3 R6 bullet now derives df = 10 | **FIXED.** VERIFIED. | ch3:380: "In both R5 and R6 the excluded fiscal year also removes its fiscal-year dummy, so the parameter count falls from $K = 14$ to $K = 13$ and residual degrees of freedom are $23 - 13 = 10$." Arithmetic re-checked: 23 − 13 = 10. App D §D.6 states df 10 for R5/R6, consistent. |
| V2-m25 | CORRECTED (App D line is 246, not 226–235; core true) | Ch3 ROA definition now states the averaging | **FIXED.** VERIFIED. | ch3:258: "Average total assets is the mean of the current and previous fiscal year-end total assets." This matches App D codebook row (app_d:246): source "Own SOPL and SOFP (current and previous year)". |
| V2-m26 | CONFIRMED | New 30-row DPS announcement-dates table in App D, from the announcement CSV (not dps.json) | **FIXED.** VERIFIED by programmatic comparison against `data_analysis/data_extract/output/manual_review/mps_rd_dps_announcement_dates.csv` (30 rows). All 30 announcement dates and all 30 price dates match the CSV; all 30 announcement dates precede their price dates; CSV `before_price_date` is `yes` for all 30. Two documented deviations, both disclosed in the table note (see below). | app_d:295 (`\label{tab:app_dps_dates}`), rows e.g. "GBIME & FY 2076/77 & 2020-10-28 & Dividend declaration & 2021-04-13". Note: "NIMB FY 2077/78 uses the corrected declaration of 2021-10-20 (12.611\% bonus, 3.389\% cash), which superseded the first declaration of 2021-10-04". The CSV's own note for that row confirms it: "First declaration 11.24%/4.76%; corrected 2021-10-20 to 12.611%/3.389% (panel uses corrected); both before price date", and `dps.json` records bonus 12.611 / cash 3.389 for NIMB FY2077/78. Second deviation: the CSV's type label "AGM only" is rendered "AGM detail" in the table for the 4 AGM rows (HBL FY2076/77, HBL FY2081/82, NIMB FY2081/82, NMB FY2076/77); dates identical, term defined in the table note. The loop's source correction is confirmed: `grep -c announcement data_analysis/data_extract/config/dps.json` = 0; the dates live only in the announcement CSV. |
| V2-m27 | CORRECTED (cited App D line 248 is the DPS row; core true) | Bonus-ratio source + units stated in Ch3, App D codebook, App D §D.6; new bonus-ratios table | **FIXED.** VERIFIED. Source and units now stated in three places; table values verified 30/30 against two independent sources (see §4). | ch3:381: "The bonus ratio is the board-proposed bonus share percentage for that fiscal year, taken from the board proposal in the annual report (Appendix~\ref{app:reproducibility}, Table~\ref{tab:app_locators} dividend pages; values in Appendix~\ref{app:reproducibility}, Table~\ref{tab:app_bonus_ratios}), expressed as a percentage of paid-up capital and divided by 100 to give a proportion." app_d:250 (codebook "Bonus ratio" row) and app_d:403 (§D.6 R7 clause) state the same. |
| V2-m28 | CONFIRMED | Each of the five restatements now carries its carrying-report SOFP locator | **FIXED.** VERIFIED. All five locators at ch3:171 were checked against App D Table D.2 (`tab:app_locators`) and agree: GBIME FY2078/79 pp. 83–84; HBL FY2080/81 pp. 54–55; KBL FY2079/80 p. 42; KBL FY2077/78 p. 34 (own-current KBL FY2076/77 p. 49); KBL FY2078/79 p. 32 (own-current KBL FY2077/78 p. 34). | ch3:171: "Global IME Bank FY 2078/79 (NPR 718.44 million; restated previous column in the GBIME FY 2078/79 report, Statement of Financial Position, PDF pp.~83--84)". (Amounts themselves are data, treated as correct and not re-audited.) |
| V2-m29 | CORRECTED (Merger Bylaws ARE cited at Ch1:11, Ch2:198, Ch2:200; NRB stats at Ch1:11, Ch3:26; true only for SEBON, MoF Economic Survey, BSD circulars) | NRB bullet reworded to the cited uses; BSD circulars removed; SEBON/MoF bullets untouched per standing limitation | **FIXED (corrected scope).** VERIFIED. NRB bullet now ties each item to its actual use; "Bank Supervision Department" occurs 0 times in ch3; SEBON and MoF bullets are byte-identical to the v2 quotation (untouched, as required). | ch3:159: "\textit{Nepal Rastra Bank (NRB):} Annual Banking and Financial Statistics and licensed financial institution directories (the population counts in Section~3.3) and the Bank and Financial Institutions Merger Bylaws (the regulatory architecture for the consolidation wave, cited in Chapter~I)." ch3:160 (SEBON bullet) and ch3:161 (MoF bullet) unchanged. The audit's correction is confirmed by the text: the Bylaws bullet now says "cited in Chapter~I" rather than implying a Ch3 use. |
| V2-m30 | CONFIRMED | Deadline sentence reworded to state it checks gap arithmetic only | **PARTIALLY FIXED.** VERIFIED. The circularity is cured: the sentence now states what was actually checked and disclaims independent verification. The second half of the v2 fix — cite the calendar source for the Chaitra-end dates — was not done: no calendar source for the target deadlines (13 April 2021 etc.) is cited anywhere in App D; the statute table's NEPSE-calendar row covers trading sessions only ("Session dates are established from the dataset's own trading rows"). | app_d:182: "Each deadline is consistent with the recorded gap subtracted from the observation date in Table~\ref{tab:mps_rd}; this checks the recorded gap arithmetic, it does not independently verify the deadline against a separate source." Statute table (app_d:194–198): "NEPSE trading calendar | Trading sessions including Sundays during the study window; holidays and suspension gaps | Session dates are established from the dataset's own trading rows and the resumption dates in this appendix". |
| V2-m31 | CONFIRMED | Full-design VIFs added at Ch3:364 | **FIXED.** VERIFIED. Values match Chapter IV Table 4.8 note (ch4:540) verbatim, including the largest year-dummy VIF. | ch3:364: "On the full fitted design, including the fixed-effect dummies, the VIFs are $5.70$ (EPS) and $12.32$ (BVPS) for Model~1, and $14.82$ (EPS), $12.46$ (BVPS), $27.34$ (EPS $\times$ Post) and $259.32$ (BVPS $\times$ Post) for Model~2, with the largest year-dummy VIF $118.21$ (Chapter~IV, Table~\ref{tab:t6_diagnostics} note)." ch4:540 carries the identical numbers. |
| V2-m32 | CONFIRMED | 328.30 → 328.31 MB | **FIXED.** VERIFIED by recomputation from the register rows as printed: 30 rows, 5,663 pages (exact), 328.31 MB (exact). | app_d:10: "The 30 reports, 328.31 MB and 5,663 pages in total, cannot be printed in a thesis." |
| V2-m33 | CORRECTED (AEA sentence is App D:4, not 6–14; core true) | AEA sentence tightened; no code deposited (author decision) | **FIXED.** VERIFIED. The sentence now states the aspiration framing and the no-code fact in one place. The v2 finding's own options were depositing code (substantive) or keeping the accurate disclaimer (no change); the loop took the disclaimer option and strengthened it. | app_d:4: "It is modelled on that standard as an aspiration for documentation structure only and is not a claim of compliance with it; in particular, no analysis code is shared (Section~D.8)." |
| V2-m34 | CONFIRMED | Table 3.1 note reworded | **FIXED.** VERIFIED. | ch3:126: "Prices are expressed in Nepalese Rupees (NPR) per ordinary share, from the ShareSansar series via the nepse-data dataset (the dataset close), cross-checked against Merolagani last traded prices and against FinancialNotices Close for FY 2081/82." |
| V2-m35 | CONFIRMED | Consequence sentence added at the five-day statement; no rationale invented | **PARTIALLY FIXED.** VERIFIED. The consequence is now stated at the point of the claim, and no rationale was invented (correct — none is verifiable). But neither of the v2 fix options was completed: no substantive rationale for five days (vs another window) is stated, and no window-sensitivity analysis (e.g. 3-day / 10-day) was added. The added sentence repeats the N = 30 inclusion consequence already printed at ch3:223. | ch3:93: "The five-day length is an un-derived operational choice; no substantive rationale for five days rather than another window is recorded in this thesis. The choice is consequential for the headline result: including the two delayed observations changes the Model~2 joint test to $F(2,16)=4.762$ ($p=0.024$), against $F(2,14)=2.954$ ($p=0.085$) in the 28-row sample (Section~3.5.2)." The cross-reference resolves: the same F(2,16) = 4.762 statement is at ch3:223 in §3.5.2. |
| V2-m38 | CONFIRMED | Unlisted 20th bank named | **FIXED.** VERIFIED. Underlying "19 listed" count remains UNVERIFIED (v2 K-02): the cited sources were not opened and the thesis gives no further evidence for the count itself. | ch3:28: "Of these 20 licensed institutions, 19 are listed on NEPSE \citep{bhandari2026}; the one unlisted institution is Rastriya Banijya Bank Limited \citep{nrb2023list}." |
| V2-m39 | CORRECTED (implication IS flagged at Ch4:480; only unflagged in Ch3/App D) | One-sided flag added in Ch3 and App D §D.6 | **FIXED.** VERIFIED in both places, using the Chapter IV wording. | ch3:381: "Only BVPS is adjusted; EPS and price remain on the original share base, so this is a one-sided rescaling of BVPS, not a full bonus-dilution adjustment of the valuation relation." app_d:403: "only BVPS is adjusted, so this is a one-sided rescaling of BVPS, not a full bonus-dilution adjustment of the valuation relation". |
| V2-m51 (App D part) | CONFIRMED (audit: R7 inputs absent, not merely unverified — no numeric per-bank-year bonus ratio printed anywhere) | New 30-value bonus-ratios table in App D | **FIXED.** VERIFIED by programmatic comparison: all 30 values match `data_analysis/data_extract/config/dps.json` `bonus_percent` exactly (0 mismatches) and match the `bonus` column of `data_analysis/data_extract/output/manual_review/mps_rd_joined_panel_bonusadj.csv` exactly (0 mismatches). | app_d:272 (`\label{tab:app_bonus_ratios}`), e.g. "NIMB & 13.00 & 12.611 & 4.00 & 0.00 & 0.00 & 0.00". Note: "0.00 means no bonus was proposed for that fiscal year." (App B part of m51 is another scope's.) |
| V2-s10 | CONFIRMED | Software versions added in Ch3 §3.6.6 and App D §D.6 | **PARTIALLY FIXED.** VERIFIED. Versions are now stated and agree with `data_analysis/analysis/requirements.txt` (pandas>=2.2, numpy>=1.26, scipy>=1.11, statsmodels==0.14.6, seaborn>=0.13, matplotlib>=3.8, PyYAML>=6.0, pytest>=8.0). But only statsmodels is an exact version; the rest are recorded as minimums ("2.2 or later"), pytest is omitted from both version lists, and no record of the versions actually installed/used exists in the thesis or the repo (no lockfile found; only the two `requirements.txt` files). The v2 ask was to record "the versions actually used". | ch3:394: "Software versions are those in the analysis requirements: \texttt{statsmodels} 0.14.6 (pinned); \texttt{pandas} 2.2 or later, \texttt{numpy} 1.26 or later, \texttt{scipy} 1.11 or later, \texttt{seaborn} 0.13 or later, \texttt{matplotlib} 3.8 or later, and \texttt{PyYAML} 6.0 or later." app_d:401 states the same. |
| V2-s11 | CONFIRMED | One-sentence ethics statement added at end of §3.2 | **FIXED.** VERIFIED. (The sentence contains no form of the word "ethic", so a full-tree "ethic" search still returns no matches — correctly, since the statement is a data statement, not an ethics-section heading.) COI / funding / AI statements were not added; those are supervisor-confirmation items, not part of this finding. | ch3:23: "This study uses only published secondary data (audited annual reports and public price series); no human participants were involved." |
| V2-s12 | CONFIRMED | "Prominent" removed from Ch3 | **FIXED.** VERIFIED. `grep -ri prominent` over ch3, app_a, app_d returns 0 hits. | ch3:31 now reads "the four commercial banking consolidations of the early-2023 wave (plus the unmerged benchmark series)"; ch3:33 bullet reads "Commercial bank series that executed horizontal statutory amalgamations…". (Note: "prominent" still occurs 2× in Chapter V, outside this scope and outside the s12 fix as assigned.) |

### Extras verified (in-scope v2 items the loop also patched)

| ID | Audit verdict | My verification | Evidence |
|---|---|---|---|
| V2-m08 (Ch3 part) | CONFIRMED | **FIXED.** The NMB–Kanchan figures are now cited with a proper `\citep`, and the bibliography entry exists. Residual (Suggestion-level, see N-03): the four figures still have no page locator; the appended register pointer identifies the report, not the page. | ch3:80: "…alongside a 13\% bonus share distribution of NPR 1,878.21 million computed on the enlarged post-acquisition capital \citep{nmb2021report}; source register, Appendix~\ref{app:reproducibility}, Table~\ref{tab:app_register}." `references.bib:326`: `@techreport{nmb2021report,` — "Annual report 2020/21", NMB Bank Limited, 2021 (the FY 2077/78 report, matching the figures' fiscal year). |
| V2-M11 (Ch3/App A part) | CORRECTED (11 figures, not 8) | **FIXED for the two in-scope figures.** Captions now follow the graphics in both. The preamble setting is also now `position=below`. | ch3:205–206: `\end{tikzpicture}` immediately followed by `\caption{Research Framework: Two-Way Fixed-Effects Valuation Model}`. app_a:93–94: `\includegraphics[…]{figures/A1_coverage_map.pdf}` immediately followed by its `\caption`. `src/thesis/config/preamble.tex:74`: `\captionsetup[figure]{labelfont=it,textfont=normalfont,position=below}`. |

## 3. Part B — New issues found on a fresh read

### N-01 — DPS table's "MPS^RD Price Date" disagrees with Appendix A for the two excluded rows
- **Location:** app_d:295 table (`tab:app_dps_dates`), rows HBL FY 2077/78 and NIMB FY 2077/78.
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED — programmatic comparison of the two tables.
- **Evidence:** App D DPS table: "HBL & FY 2077/78 & 2021-10-08 & Dividend declaration & 2022-04-13" and "NIMB & FY 2077/78 & 2021-10-20 & Dividend declaration & 2022-04-13". Appendix A Table A.1 gives the same rows' price dates as 2022-06-06 (HBL, 358.90) and 2022-05-30 (NIMB, 367.70). The DPS table's price-date column therefore shows the target deadline, not the recorded price date, for exactly the two rows where the two differ.
- **Impact:** The table's own claim ("Every announcement date precedes its $\mathit{MPS}^{RD}$ price date") still holds under either convention — verified: 2021-10-08 < 2022-06-06 and 2021-10-20 < 2022-05-30 — so no eligibility error follows. But the same column label means two different things in the two appendices, and for these two rows there is strictly no $\mathit{MPS}^{RD}$ price at all (the rows are missing), so the column is really the deadline. Fix: rename the column for these rows or add a footnote stating the price date shown is the target deadline where the row is window-excluded. (The DPS table faithfully reproduces its source CSV, which also records 2022-04-13 for these rows — the inconsistency is between the thesis tables, not between the table and its source.)

### N-02 — "Restatements are exactly three" is unqualified and reads against Chapter III's five balance-sheet restatements
- **Location:** app_d:263 (§D.4).
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED — read in context; pre-existing wording, not loop-introduced.
- **Evidence:** "Restatements are exactly three, and their treatment is fixed. Global IME Bank FY 2076/77 reported EPS 17.99, restated 15.33; NMB Bank FY 2077/78 reported 16.66, restated 14.76; Himalayan Bank FY 2077/78 reported 28.07, restated 27.60." Chapter III (ch3:171) documents "Five balance-sheet restatements".
- **Impact:** In context the paragraph is about EPS restatements (all three values are EPS), so a careful reader can resolve it — but the bare sentence states a count that contradicts the only other restatement count in the thesis unless the reader supplies the qualifier "EPS" herself. Fix: "EPS restatements are exactly three".

### N-03 — Kanchan figures still have no page locator
- **Location:** ch3:80 (NMB profile bullet).
- **Severity:** Suggestion. **Revision scale:** Narrow.
- **Status:** VERIFIED.
- **Evidence:** ch3:80 ends "…\citep{nmb2021report}; source register, Appendix~\ref{app:reproducibility}, Table~\ref{tab:app_register}." The register (app_d:22–94) identifies the NMB FY 2077/78 report (160 pages, 3.62 MB) but gives no page for the four figures (August 2020; NPR 496.77 million; 85% swap; 13% / NPR 1,878.21 million). The register pointer is also redundant now that a proper `\citep` exists.
- **Impact:** A reader can find the report but not the figures within it without searching a 160-page PDF. Fix: add the report page(s), or drop the redundant register pointer.

## 4. Re-checks performed (strengths confirmed, not new findings)

All re-run programmatically by this reviewer unless stated:

1. **Table 3.1 vs Appendix A prices:** all 28 numeric cells agree; the 2 missing cells (HBL/NIMB FY 2077/78) correspond to Appendix A late prices 358.90 (6 Jun 2022) and 367.70 (30 May 2022). VERIFIED.
2. **Appendix A price audit:** 30 rows; 29 exact dataset-vs-Merolagani matches; the single difference is NMB FY 2076/77, 437.00 vs 436.00, disclosed in the note at app_a:85. VERIFIED.
3. **Appendix D register:** 30 rows; pages sum to 5,663 (exact vs app_d:10); sizes sum to 328.31 MB (exact); all 30 SHA-256 12-character prefixes mutually distinct. VERIFIED (SHA values themselves not recomputed against the report files).
4. **DPS completeness counts:** `dps.json` statuses are 18 `proposed` + 12 `documented-nil`, matching app_d:263 ("18 proposed cash dividends and 12 documented nil decisions"). HBL/NIMB FY 2081/82 are `documented-nil`; HBL/NMB FY 2076/77 are `proposed`. VERIFIED.
5. **Locators DPS pages:** all 30 DPS pages in App D Table D.2 match `dps.json` PDF/printed pages exactly (0 mismatches). VERIFIED.
6. **m28 locators:** all five Ch3:171 SOFP locators agree with App D Table D.2 (see m28 row, §2). VERIFIED.
7. **Labels:** every `\ref` used by the new/changed text resolves — `tab:app_bonus_ratios`, `tab:app_dps_dates`, `tab:app_locators`, `tab:app_register`, `app:reproducibility`, `tab:t6_diagnostics`, `tab:app_codebook`, `tab:app_sample`, `tab:app_statute`, `tab:app_price_verification`, `tab:mps_rd`, `fig:framework` — each defined exactly once in the thesis source. VERIFIED.
8. **Sample arithmetic:** 30 → 28, 13 pre / 15 post, stated identically in ch3:82–100, app_d:267–272 (Table D.5), and app_a:85. VERIFIED.
9. **Deadline/observation consistency:** App D §D.3 target deadlines (13 April 2021/2022/2023, 12 April 2024, 13 April 2025/2026) match Ch3 Table 3.1 observation dates, with FY 2079/80 observed 14 April 2024 (gap 2, Sunday session) as the Table 3.1 note ^d states. VERIFIED.
10. **M01 standing limitation re-confirmed:** "Prabhu" occurs exactly twice in the whole thesis source (Ch1:30, Ch3:31); 0 times in any appendix; no reason for the exclusion is stated in Ch3 or the appendices. VERIFIED.

## 5. What could not be verified

1. **Underlying external counts.** Whether 19 of the 20 licensed banks are listed on NEPSE (v2 K-02), and whether Rastriya Banijya Bank Limited is in fact the unlisted one, rest on `bhandari2026` and `nrb2023list`; neither source was opened. The thesis now names the bank (m38 FIXED as a documentation matter); the count itself stays UNVERIFIED.
2. **Report-file facts.** SHA-256 values were not recomputed against the PDF files; restatement amounts, swap ratios, merger dates, and the NMB Kanchan figures were not checked against the annual reports (data treated as correct per the task). The locators were checked for internal agreement between Ch3 and App D, not against the reports.
3. **Rendered output.** No PDF build was run, so caption placement, table pagination (including the two new longtables), and the one-page fit of any element were not checked visually.
4. **Installed software versions.** No lockfile or installed-version record exists in the repo, so the exact versions of the unpinned dependencies cannot be recovered from the thesis alone (see s10, PARTIALLY FIXED).
5. **Calendar source for Chaitra-end dates.** No Nepali-calendar authority for the specific target deadlines (13 April 2021 etc.) was located in the thesis (see m30, PARTIALLY FIXED). Whether such a source exists outside the thesis was not investigated.
6. **The five-day window's rationale.** None is stated anywhere in the thesis, and none was invented by the loop; whether a defensible rationale exists (e.g. in the proposal or pipeline notes) was not investigated beyond the thesis source (see m35, PARTIALLY FIXED).

## 6. Summary counts

- **Part A (19 assigned findings):** 15 FIXED (m24, m25, m26, m27, m28, m29, m31, m32, m33, m34, m38, m39, m51, s11, s12); 3 PARTIALLY FIXED (m30, m35, s10); 1 NOT FIXED by design as a standing limitation (M01, Ch3 limb); 0 INCORRECTLY FIXED; 0 FALSE FINDINGS.
- **Extras verified:** m08 (Ch3 part) FIXED with a page-locator residual (N-03); M11 (Ch3/App A part) FIXED.
- **Part B new issues:** 2 Minor (N-01, N-02), 1 Suggestion (N-03). No new Critical or Major issue. No loop patch introduced a wrong value: both new tables match their sources 30/30, and no DPS date precedes-or-follows error was found.
