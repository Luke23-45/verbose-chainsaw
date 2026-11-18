# Independent Review — Chapter III (Research Methodology) and Appendices A & D

**Dissertation:** *Value Relevance of Accounting Information Before and After the Banking
Consolidation Wave: Evidence from Nepalese Commercial Banks*
**Reviewed artifact:** repository `~/workspace/verbose-chainsaw`, HEAD `2b4e10f`
("Add independent data-analysis review (v1)", 2026-11-14), **working tree as it stands**
— i.e. HEAD plus the uncommitted changes present at review time. This review covers
only the working-tree text; where the working tree differs from the commit the v1
review examined (`2d195bf`), the difference is noted explicitly (§8).
**Review date:** 17 November 2026
**Review file:** `docs/thesis_review/v2/review_ch3_method.md` (new; the only file
created by this review)
**Mode:** read-only, independent content review of the methodology *description*.
The analysis itself is not re-audited here; that is v1's remit
(`docs/thesis_review/v1/data_analysis_review.md`).

## 0. How to read this review

- **Scope.** Chapter III in full
  (`src/thesis/chapters/chapter_03_research_methodology.tex`, 392 lines),
  Appendix A in full (`src/thesis/appendices/appendix_a.tex`, 96 lines),
  Appendix D in full (`src/thesis/appendices/appendix_d.tex`, 342 lines).
  Other chapters, appendices, and the proposal are consulted only where Chapter III
  or Appendix D points at them (cross-references, the pre-specification claim,
  the Chapter IV covariance table), and only to check that the pointer resolves.
- **Status vocabulary (exactly one per finding).**
  - **VERIFIED** — established by reading the cited file, opening the cited source,
    or cross-checking two locations; the "how" is stated in each finding.
  - **INFERRED** — follows from verified facts plus an explicit argument, but was
    not itself directly observed or computed.
  - **UNVERIFIED / CANNOT DETERMINE** — could not be checked with the access and
    time available; the review takes no position on the underlying fact.
- **Severity.** Critical = invalidates or materially re-frames a headline claim;
  Major = substantially weakens a reported result or misstates the method;
  Minor = local error, inconsistency, or omitted caveat that does not reverse a
  conclusion; Suggestion = improvement, not a defect.
- **Revision scale.** Narrow = a sentence, a number, or a citation; Substantive =
  a reworked paragraph, table, or section; Fundamental = a redesign of the
  method itself. No finding in this review requires a Fundamental revision.
- **No hallucination rule applied.** Every thesis quotation below was copied from
  a file opened during this task; every external claim comes from a source opened
  during this task (§10). Plagiarism checking is **not** covered by this review.
  No judgement is made about authorship or AI-tool use.

## 1. Verdicts (exactly one each)

### (i) Chapter III — **Ready with minor revisions**

The methodology description is complete enough for a reader to reconstruct the
sample, the price measure, the variables, the two models, and the nine-specification
suite, and its internal arithmetic and its agreement with the pipeline code and
with v1 check out (see §6 and §7). The gaps are narrow and local: one sampling
exclusion with no stated reason (C-01), two pieces of missing derivation/detail
(C-02, C-03), three pieces of unpublished supporting detail (C-04, C-05, C-06),
listed sources with no visible use (C-07), and uncited profile figures (C-08).
None of them changes a model, a sample count, or a stated result; each is fixed
by adding a sentence, a citation, or a locator.

### (ii) Appendices A and D together — **Ready with minor revisions**

Appendix A is a complete 30-cell price audit that agrees cell-for-cell with
Chapter III's Table 3.1. Appendix D is a thorough reproducibility record whose
register arithmetic I verified (5,663 pages exact; 30 mutually distinct SHA-256
prefixes; §6). Its weaknesses are narrow: one circular "verification" sentence
(C-09), a 0.01 MB rounding difference in a stated total (C-10), the disclosed
absence of any shared code against the AEA standard it invokes as a model
(C-11), and two pieces of supporting detail kept out of the printed record
(C-04, C-05). The appendix is candid about its own limits (§D.8), and that
candour is accurate.

## 2. Inventory — what was reviewed

### Chapter III sections

| Location | Element | Status |
|---|---|---|
| ch3:3–12 | §3.1 Introduction (roadmap of §§3.2–3.6) | REVIEWED |
| ch3:13–22 | §3.2 Research Design | REVIEWED |
| ch3:23–134 | §3.3 Population, Sample, and Sampling Procedure | REVIEWED |
| ch3:25–27 | §3.3.1 Population of the Study | REVIEWED |
| ch3:28–37 | §3.3.2 Sampling Method and Selection Criteria | REVIEWED |
| ch3:39–80 | §3.3.3 Profile of the Sampled Commercial Banks | REVIEWED |
| ch3:82–134 | §3.3.4 Sample Size, Missingness Protocol, and Realized Observations | REVIEWED |
| ch3:103–134 | Table 3.1 (`tab:mps_rd`): MPS^RD dates, prices, trading status | REVIEWED |
| ch3:135–173 | §3.4 Nature and Sources of Data, and Data Collection Procedure | REVIEWED |
| ch3:137–145 | §3.4.1 Nature of Data | REVIEWED |
| ch3:146–160 | §3.4.2 Sources of Data Collection | REVIEWED |
| ch3:162–172 | §3.4.3 Data Audit, Extraction, and Reconciliation Protocol | REVIEWED |
| ch3:174–266 | §3.5 Research Framework and Definition of Variables | REVIEWED |
| ch3:176–214 | §3.5.1 Conceptual Framework | REVIEWED |
| ch3:179–214 | Figure 3.1 (`fig:framework`): TikZ research-framework diagram | REVIEWED (code read in full; the rendered graphic was not visually inspected) |
| ch3:215–266 | §3.5.2 Operational Definition and Measurement of Variables | REVIEWED |
| ch3:217–221 | Dependent variable MPS^RD | REVIEWED |
| ch3:223–239 | Primary independent variables EPS, BVPS | REVIEWED |
| ch3:240–248 | Moderating variable Post_t | REVIEWED |
| ch3:249–260 | Supplementary variables ROA, DPS | REVIEWED |
| ch3:261–266 | Strict exclusion of P/E multiples | REVIEWED |
| ch3:267–392 | §3.6 Methods of Analysis and Econometric Specification | REVIEWED |
| ch3:270–290 | Model 1 (baseline) | REVIEWED |
| ch3:292–330 | Model 2 (regime shift), incl. Post-absorption note | REVIEWED |
| ch3:331–357 | Estimation, degrees of freedom, HC3 inference, bootstrap | REVIEWED |
| ch3:358–367 | Diagnostic battery; post-hoc MDE calculation | REVIEWED |
| ch3:369–381 | Nine-specification suite R1–R9 | REVIEWED |
| ch3:383–389 | Specification comparison (pooled OLS, bank-FE-only) | REVIEWED |
| ch3:390–392 | Computational tools and implementation | REVIEWED |

### Appendix A tables and figures

| Location | Element | Status |
|---|---|---|
| app_a:5–7 | Introductory prose (scope: 30 planned bank-years) | REVIEWED |
| app_a:11–83 | Table A.1 (`tab:app_price_verification`): dataset Close vs Merolagani LTP, 30 rows | REVIEWED |
| app_a:85 | Table note (29/30 agreement; NMB resolution; exclusions; mismatch; FY 2079/80 Sunday session) | REVIEWED |
| app_a:90–94 | Figure A.1 (`fig:app_coverage_map`): panel coverage map | REVIEWED (caption and cross-reference checked; file `src/thesis/figures/A1_coverage_map.pdf` confirmed present; the plotted image itself was not visually inspected) |

### Appendix D sections and tables

| Location | Element | Status |
|---|---|---|
| app_d:6–14 | §D.1 Data Availability | REVIEWED |
| app_d:16–99 | §D.2 Source Register (incl. note at :96) | REVIEWED |
| app_d:22–23 | Table D.1 (`tab:app_register`): 30 reports | REVIEWED |
| app_d:101–175 | Table D.2 (`tab:app_locators`): SOFP/SOPL/DPS/indicators pages | REVIEWED |
| app_d:178–222 | §D.3 Price Provenance (incl. statute table) | REVIEWED |
| app_d:194–198 | Table D.3 (`tab:app_statute`): statute and calendar sources | REVIEWED |
| app_d:224–261 | §D.4 Variable Codebook (incl. notes at :257, restatements at :261) | REVIEWED |
| app_d:230–235 | Table D.4 (`tab:app_codebook`) | REVIEWED |
| app_d:263–302 | §D.5 Sample Construction Log | REVIEWED |
| app_d:267–272 | Table D.5 (`tab:app_sample`) | REVIEWED |
| app_d:306–320 | §D.6 Estimation Recipe | REVIEWED |
| app_d:322–338 | §D.7 Replication Checklist | REVIEWED |
| app_d:340–342 | §D.8 Limits of Reproducibility | REVIEWED |

"ch3" = `src/thesis/chapters/chapter_03_research_methodology.tex`;
"app_a" = `src/thesis/appendices/appendix_a.tex`;
"app_d" = `src/thesis/appendices/appendix_d.tex`. Line numbers are 1-based
lines of the working-tree files as read.

## 3. Assessment against the brief's questions (a)–(h)

**(a) Replication sufficiency.** Largely sufficient. From Chapter III alone a
reader can reconstruct: the target sample (30 bank-years, 5 series × 6 years),
the realized sample (28; 13 pre, 15 post), the MPS^RD rule (first session on or
after the Chaitra-end deadline, 5-day window, never impute), all six variable
definitions with formulae, both models with reference categories and parameter
counts, the HC3/t(df) inference rule, the four diagnostics, and all nine
specifications with their sample sizes. Appendix D closes the remaining gaps
for most items (report locators, codebook rules, estimation recipe, checklist).
The exceptions are C-02 (R5/R6 residual df), C-03 (ROA averaging), C-04 (DPS
announcement dates), C-05 (bonus-ratio source/units), and C-06 (restatement
locators). A reader who wants to *re-execute* rather than *reconstruct* cannot
do so from the thesis alone: Appendix D states this plainly (§D.8, app_d:342:
"no code is shared; a reader who wants to re-execute rather than reconstruct
must reimplement the recipe in Section D.6").

**(b) Justification of design choices.** Justifications are stated for: purposive
sampling (focus on the 2023 consolidations + longitudinal continuity, ch3:29);
the unmerged benchmark (separating sector trends from merger shifts, ch3:31);
own-current reporting (information set at the deadline, ch3:169); recomputed
BVPS (decimal precision, ch3:232–239); EPS/ROA never co-included (r = 0.975,
VIF ≈ 20, ch3:249–257); P/E exclusion (circularity, ch3:261–266, citing
§2's proof); two-way fixed effects (omitted-variable bias, ch3:20); HC3
(pre-specification + small-sample properties, ch3:351); the 5-day rule — **not**
justified, and the text says so itself (C-16). The "prominent" sampling
criterion is not operationalized (C-18).

**(c) Consistency with v1 and with code/outputs.** The description matches v1's
verified account and the pipeline code on every point I cross-checked (§6):
sample counts, freshness rule, price rule, variable definitions, R1–R9
definitions, df accounting for R1–R4/R9, the HC3 column values, the bootstrap
floor. Two deltas *relative to v1* improve consistency (§8): the Chapter IV
covariance-sensitivity table v1 found missing now exists in the working tree,
and the Appendix D "no repository" sentence v1 flagged is gone.

**(d) Data selection and handling.** Sampling criteria are stated (ch3:31–37);
the five series are profiled with merger dates and swap ratios (ch3:39–80);
exclusions are named (HBL and NIMB FY 2077/78, ch3:93–100) with a stated rule
and stated delays. Exclusions with **no stated reason**: the Prabhu–Century
combination (C-01) and, at a smaller scale, the unlisted 20th bank (C-17).
Treatments that are *not* exclusions are explicitly separated from exclusions
in Appendix D Table D.5 (app_d:267–302).

**(e) Data sources listed vs used/cited.** Primary empirical sources (audited
reports; ShareSansar via nepse-data; Merolagani; FinancialNotices) are used and
traceable. Of the *contextual* sources listed in ch3:152–160, several are never
cited or used anywhere in the thesis (C-07). Every citation key used in the
three in-scope files exists in `src/thesis/references.bib` (§6).

**(f) Ethical considerations.** There is **no** ethics statement, ethics section,
or ethics discussion in Chapter III, Appendix A, or Appendix D — verified by a
full-text search for "ethic" across all three files and across the whole thesis
source tree, which returned no matches. Whether one is required is assessed in
C-14 against the TU Guidelines text I opened: Chapter II of the Guidelines
imposes duties of honest reporting, citation, data retention/sharing, and
confidentiality, and no IRB-style approval requirement appears in the chapter
text I read. The applicable duties are largely met through Appendix D; an
explicit one-sentence statement (no human subjects; public secondary data only)
is still the cheap, correct addition.

**(g) Limitations acknowledged in Chapter III itself.** Chapter III is unusually
candid. Limitations stated in the chapter itself include: the 5-day window is
un-derived (ch3:91); the price rule "does not verify the public release date
for every bank-year or rule out earlier information leakage" and disclosure
dates were investigated for only five bank-years (ch3:217–221); NEPSE official
closes are unverified (ch3:124); the NMB FY 2076/77 price retention "does not
represent independent verification" (ch3:166–168); two BVPS/NAV variances stay
flagged as unresolved (ch3:232–239); serial independence is assumed and
untested (ch3:352); the wild-cluster bootstrap "cannot produce a 5% rejection"
(ch3:352); MDEs are post hoc and optimistic (ch3:367); no prospective power
analysis was specified (ch3:367). The known FY 2078/79 entity-timing mismatch
is disclosed in Table 3.1 note ^c (ch3:124) and handled by R6.

**(h) Appendices A and D — complete, internally consistent, consistent with
Chapter III?** Yes, with the narrow exceptions in C-04, C-05, C-09, C-10, and
C-11. Cross-checks performed: all 28 numeric cells of Table 3.1 match Appendix
A exactly (§6); the two "Missing" cells match Appendix A's late resumption
prices; Appendix D's register sums to the stated page total; its sample log
reconciles 30 → 28; its codebook rules match Chapter III's definitions; its
estimation recipe reproduces Chapter III's models and df (except C-02).

## 4. Claims register — substantive methodological claims in Chapter III

| # | Claim (location) | Evidence in the thesis / check performed | Status |
|---|---|---|---|
| K-01 | Population is all 20 NRB-licensed Class `A' banks; 32 in FY 2011/12 → 20 by mid-Oct 2023 (ch3:26) | Cited `nrb2013stats`, `nrb2023list`; both entries exist in `references.bib`. The NRB sources themselves were not opened. | UNVERIFIED (underlying count not checked) |
| K-02 | 19 of the 20 are listed on NEPSE (ch3:26) | Cited `bhandari2026` (Bhandari, Pradhan & Ghimire 2026, *Int. Res. J. MMC* 7(1), 190–205). The article was not opened; whether it states "19 listed" was not checked. | UNVERIFIED |
| K-03 | Five series = exactly 25.0% of the population (ch3:29) | Arithmetic 5/20 = 25.0%, recomputed. | VERIFIED |
| K-04 | Sample covers four of the five early-2023 combinations plus an unmerged benchmark (ch3:29) | Stated in text; the fifth (Prabhu–Century) is named with citation `nrb2023bsr`. No reason for its exclusion is stated (C-01). | VERIFIED (as a description of the sample); reason UNVERIFIED |
| K-05 | Merger dates and swap ratios per bank (ch3:39–80) | Each bullet carries a citation to the bank's report/AGM/SGM except NMB (C-08). The underlying reports were not opened; extraction is out of scope per v1. | UNVERIFIED |
| K-06 | Target 30 bank-years; realized clean N = 28 (13 pre, 15 post) (ch3:82–100) | Counted the frozen panel CSV: 30 rows; 28 with gap ≤ 5; 13 pre / 15 post. Matches `dataset.py:6–12`. | VERIFIED |
| K-07 | Five-day freshness rule; failures coded missing, never imputed (ch3:85–91) | Implemented at `dataset.py:137` (`price_rd = price.where(gap <= freshness)`); freshness = 5 from config. The two excluded rows have gaps 54 and 47 in the CSV. | VERIFIED |
| K-08 | HBL FY 2077/78 resumed 6 Jun 2022, 54 days late; NIMB 30 May 2022, 47 days late (ch3:93–100) | Date arithmetic confirmed (`date -d`: 13 Apr 2022 + 54 days = 2022-06-06; + 47 days = 2022-05-30). Suspension-cause confirmation against NEPSE's own notices is stated as outstanding (app_d:342). | VERIFIED (dates); cause UNVERIFIED (as the thesis itself states) |
| K-09 | MPS^RD = first-session close on/after the nine-month BAFIA §59(2) deadline, operationalized as Chaitra-end (ch3:217–221; app_d:182) | Statute text opened (kaanun.app, §59): two duties confirmed, including "make public the audited balance-sheet … within nine months of the next fiscal year". The statute does not name Chaitra; the thesis discloses that the Chaitra mapping is its own operationalization. | VERIFIED (duties + disclosure); the Chaitra mapping itself is the thesis's stated operationalization |
| K-10 | All 28 Table 3.1 prices are the dataset closes (ch3:103–134) | All 28 numeric cells match Appendix A Table A.1 exactly (programmatic comparison, 0 mismatches); the 2 missing cells match Appendix A's late prices (HBL 358.90, NIMB 367.70). | VERIFIED |
| K-11 | 29 of 30 prices match Merolagani LTP exactly; NMB FY 2076/77 differs by NPR 1.00 and is retained on ShareSansar's full daily record (ch3:166–168; app_a:85) | Appendix A Table A.1 shows 29 "Match" and one "Resolved" (437.00 vs 436.00). The thesis states this is not independent verification. | VERIFIED (as a description of the comparison) |
| K-12 | EPS, BVPS, ROA, DPS definitions and formulae (ch3:223–260) | Formulae as printed; EPS/BVPS share-base divergence explained with worked examples (GBIME 22.06 vs 18.71 etc.). ROA averaging defined only in Appendix D (C-03). | VERIFIED (definitions as written) |
| K-13 | Post_t is absorbed by year fixed effects; standalone Post must not be estimated (ch3:292–330) | Algebra as stated (Post = sum of the three post-year dummies). `models.py:23–24` builds year dummies with FY 2076/77 as reference; the proposal (§7, lines 187–200) states the same absorption. | VERIFIED |
| K-14 | Parameter counts and residual df: M1 K=12/df 16; M2 K=14/df 14; R4 K=15/df 13; R9 df 13 (ch3:270–330, 376–380) | Arithmetic recomputed (28−12=16; 28−14=14; 28−15=13; 27−14=13). R5/R6 df 10 is stated in Appendix D but not derivable from Chapter III (C-02). | VERIFIED (except C-02) |
| K-15 | HC3 with t(df) reference; HC3 retained on pre-specification and small-sample properties (ch3:331–357) | Proposal `src/proposal/sections/07_methodology/07_methodology.tex:187,200` pre-specifies HC3 and states HC3 "do[es] not account for arbitrary within-bank dependence … and [is] not a correction for the small number of clusters". Chapter IV Table `tab:cov_sensitivity` (ch4:441) reports all five estimators; values match v1's recomputed table (§8). | VERIFIED |
| K-16 | Diagnostic values: VIFs 1.16 / 10.33 / 2.28 / 15.15 / 24.13; Cook's thresholds and flagged counts; Shapiro–Wilk W = 0.925/0.922, p = 0.045/0.038 (ch3:358–367) | Numbers as printed in Chapter III. v1 recomputed all of them and matched (§M12–M15); I did not re-derive them. The VIF scope (FE dummies excluded) is disclosed at ch3:361; full-design VIFs are not reported (C-13). | VERIFIED (via v1 recomputation; not re-derived here) |
| K-17 | MDEs 10.73 / 12.06 / 3.71 NPR, post hoc, optimistic (ch3:367) | Numbers as printed; v1 recomputed and matched (§M16). Chapter III labels the calculation post hoc and the MDEs optimistic upper bounds. | VERIFIED (via v1 recomputation; not re-derived here) |
| K-18 | Wild-cluster bootstrap floor: 32 patterns, minimum p = 2/32 = 0.0625, cannot produce a 5% rejection (ch3:352) | Arithmetic 2^5 = 32 confirmed; v1 re-enumerated all 32 patterns and reproduced p = 2/32 for baseline and R6 (§M09). Chapter III states the floor candidly. | VERIFIED |
| K-19 | R1–R9 as defined (ch3:369–381) | Each definition matches `data_analysis/analysis/stats/robustness.py:57–168` (`build_runs`): R1/R2 baselines; R3 ROA substitution; R4 +DPS; R5/R6 year exclusions; R7 bonus-adjusted BVPS only; R8 restated EPS; R9 NMB FY 2076/77 exclusion. | VERIFIED |
| K-20 | "The five-day length is an un-derived operational choice" (ch3:91) | Direct quotation; no rationale appears anywhere in Chapter III or Appendix D. The consequence is disclosed: including the two delayed observations changes the Model 2 joint test to F(2,16) = 4.762 (p = 0.024) vs F(2,14) = 2.954 (p = 0.085) (ch3:217–221). | VERIFIED |
| K-21 | Appendix D follows the AEA Data and Code Availability Policy structure and FAIR R1.1/R1.2 (app_d:12) | AEA policy opened (Feb 2026 version, aeaweb.org): it requires data, code, and details sufficient to permit replication, deposited in an openly accessible trusted repository; code must be made public even where data cannot be shared. FAIR paper opened (Wilkinson et al. 2016, *Sci. Data* 3:160018): Box 2 states R1.1 "(meta)data are released with a clear and accessible data usage license" and R1.2 "(meta)data are associated with detailed provenance". Appendix D's paraphrases match. Appendix D states it is "modelled on that standard and is not a claim of compliance with it" — accurate framing (C-11). | VERIFIED (wording match); compliance is expressly disclaimed by the thesis |

## 5. Findings

### C-01 — Prabhu–Century combination excluded with no stated reason
- **Location:** ch3:29 (§3.3.2).
- **Severity:** Major. **Revision scale:** Narrow.
- **Status:** VERIFIED — read the full §3.3; no sentence anywhere in Chapter III
  (or Appendix D) gives a reason for excluding the fifth combination.
- **Evidence:** "these five institutions comprise four of the five Class `A'
  commercial bank combinations executed during the early-2023 wave (the fifth,
  Prabhu Bank's acquisition of Century Commercial Bank \citep{nrb2023bsr}, is
  not sampled) alongside an unmerged private commercial bank benchmark".
- **Impact:** Sampling is the load-bearing design choice of a purposive-sample
  thesis, and the TU Guidelines (Chapter III, opened during this task) require
  the sampling technique to be appropriate and the sample to be representative
  of the population. A reader cannot tell whether the fifth combination was
  excluded for a principled reason (e.g. data availability, listing status,
  timing) or for convenience. Fixing it — one sentence stating the reason —
  changes the assessability of the sample, not any estimate.

### C-02 — R5/R6 residual degrees of freedom (10) cannot be derived from Chapter III
- **Location:** ch3:376–377 (R5, R6); app_d:320 (§D.6).
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED — read Chapter III's parameter accounting (K = 14 for
  Model 2, ch3:331–345) and Appendix D's df statement; read `models.py:23–24`
  (year dummies built with `C(fy, Treatment(reference='FY2076-77'))`, so
  dropping a fiscal year drops one estimable year dummy, K = 13, df = 23 − 13
  = 10); v1 verified the R6 joint test as F(2,10) (§M07, traceability row 19).
- **Evidence:** Chapter III gives only "($n = 23$)" for R5 and R6, while
  Appendix D states "(residual degrees of freedom 10)" with no derivation.
  A reader applying Chapter III's own rule (N − K = 23 − 14) gets 9, not 10.
- **Impact:** Replication confusion only — Appendix D and Chapter IV both state
  df = 10, so a replicator using the appendices gets the right number. One
  sentence ("excluding a fiscal year removes its year dummy, so K falls to 13")
  in Chapter III §3.6.5 or Appendix D §D.6 closes it.

### C-03 — ROA's "average total assets" is not defined in Chapter III
- **Location:** ch3:249–257 (ROA definition, eq. `eq:roa_def`); app_d:226–235
  (codebook).
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED — read both passages. Chapter III defines ROA as profit
  after tax divided by "Average Total Assets" without saying what is averaged;
  Appendix D's codebook supplies it: "Own SOPL and SOFP (current and previous
  year)".
- **Evidence:** "Operating profitability expressed as net profit after tax
  divided by average total assets, expressed as a percentage".
- **Impact:** A reader reconstructing from Chapter III alone cannot reproduce
  ROA exactly (current-year assets vs mean of current and previous year-end
  assets differ). Appendix D repairs it, so the fix is a parenthetical in
  Chapter III.

### C-04 — DPS announcement dates are asserted but never printed
- **Location:** ch3:259 (DPS eligibility rule); app_d:261 (§D.4), app_d:322–338
  (§D.7 checkpoint 4).
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED — read the passages; searched Appendix B
  (`appendix_b.tex`) for "announce" (no matches) and confirmed no announcement
  date appears in Chapter III, Appendix A, or Appendix D.
- **Evidence:** Chapter III: "including only eligible cash dividends that were
  officially declared on or prior to the $\mathit{MPS}^{RD}$ observation date";
  Appendix D: "every announcement date precedes its $\mathit{MPS}^{RD}$ price
  date"; §D.7 checkpoint 4 requires the replicator to check that "every
  announcement date precedes its $\mathit{MPS}^{RD}$ price date".
- **Impact:** The eligibility rule is stated but the dates needed to apply or
  audit it are not in the thesis, so the §D.7 checkpoint cannot be executed
  from the thesis alone. The counts are consistent (I counted the frozen panel
  CSV: 12 zero-DPS rows of 30, i.e. 18 proposed + 12 nil as Appendix D states),
  so this is a documentation gap, not a detected error. Fix: print the 30
  announcement dates (or their source pages) in Appendix D or Appendix B.

### C-05 — Bonus-ratio source and units are not stated in Chapter III or Appendix D
- **Location:** ch3:378 (R7); app_d:320 (§D.6); app_d:248 (codebook DPS row).
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED — read both passages; read the frozen bonus-adjusted
  panel CSV, whose `bonus` column holds percentage values (e.g. GBIME
  FY 2076/77: 14.0), and `robustness.py:123–135`, which computes
  `bvps / (1 + bonus/100)`.
- **Evidence:** Chapter III: "$\mathit{BVPS}_{\text{adj}} = \mathit{BVPS} /
  (1 + \text{bonus ratio})$". Neither Chapter III nor Appendix D says where the
  bonus ratios come from (board proposals in the annual reports, per the DPS
  locators) or that the "ratio" in the code is a percentage divided by 100.
- **Impact:** A replicator must infer the units and the source; a reader who
  takes "bonus ratio" as a proportion (0.14) vs a percentage (14) gets the same
  result only if they also divide by 100, which the text never says. Narrow
  fix: name the source and the units in one sentence.

### C-06 — The five balance-sheet restatements have amounts but no locators
- **Location:** ch3:169 (§3.4.3, step 5); cf. app_d:261 (only the three EPS
  restatements are documented in Appendix D).
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED — read ch3:169 in full; searched the thesis source for
  the five amounts (718.44; 1,877.08; 1,047.39; −7,369.69; 9.59) — they occur
  only in Chapter III.
- **Evidence:** "Five balance-sheet restatements arising from mid-year mergers
  and accounting alignments were documented: Global IME Bank FY 2078/79 (NPR
  718.44 million), Himalayan Bank FY 2080/81 (Civil Bank merger, NPR 1,877.08
  million), Kumari Bank FY 2079/80 (NCC Bank merger, NPR 1,047.39 million),
  Kumari Bank FY 2077/78 (derivative line alignment, NPR -7,369.69 million),
  and a minor asset reclassification in Kumari Bank FY 2078/79 (NPR 9.59
  million, or 0.005\%) — each labelled by the annual report whose
  previous-year comparative column carries the restatement."
- **Impact:** The amounts cannot be located from the thesis: no report page is
  given, and Appendix D's locators give statement pages, not restatement
  columns. The own-current rule itself is clearly stated, so estimation is
  unaffected; this is provenance completeness. Fix: add the comparative-column
  report and page for each of the five.

### C-07 — Contextual sources listed in Chapter III are never cited or used
- **Location:** ch3:152–160 (§3.4.2, "Contextual and Regulatory Data Sources").
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED — read §3.4.2; searched all thesis chapters and
  appendices for citations to SEBON publications, the Ministry of Finance
  *Economic Survey*, NRB *Annual Banking and Financial Statistics*, the Merger
  Bylaws, and BSD circulars. No citation to any of them exists anywhere in the
  thesis. (`references.bib` does contain a Merger Bylaws entry — "Bank and
  Financial Institutions Merger Bylaws, 2068" — but it is never cited.)
  By contrast, the NRB *Bank Supervision Report 2022/23* (`nrb2023bsr`) is
  cited, but for the Prabhu–Century combination, not as a contextual source.
- **Evidence:** "Nepal Rastra Bank (NRB): Annual Banking and Financial
  Statistics, licensed financial institution directories, Bank and Financial
  Institutions Merger Bylaws, and circulars issued by the Bank Supervision
  Department. … Securities Board of Nepal (SEBON): Annual reports, Capital
  Market Trends publications, and corporate disclosure directives. …
  Ministry of Finance (MoF), Government of Nepal: Economic Survey
  publications (FY 2076/77 through FY 2081/82)."
- **Impact:** Listing sources that play no visible role in the analysis overstates
  the evidentiary base and leaves a reader unable to tell whether they informed
  any decision. Fix: either cite them where they were actually used, or delete
  them from the sources list (one paragraph either way). This does not affect
  any estimate.

### C-08 — NMB profile figures are uncited, unlike the other four bank profiles
- **Location:** ch3:78 (NMB bullet, "Corporate History Note").
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED — read §3.3.3 in full. GBIME, HBL, KBL, and NIMB bullets
  each cite an annual report, AGM, or SGM; the NMB bullet cites nothing.
- **Evidence:** "NMB acquired Kanchan Development Bank Limited in August 2020
  (Bhadra 2077 BS), adding NPR 496.77 million to share capital in FY 2077/78
  (new shares issued to Kanchan shareholders at the 85\% swap ratio), alongside
  a 13\% bonus share distribution of NPR 1,878.21 million computed on the
  enlarged post-acquisition capital."
- **Impact:** Four specific figures with no source pointer. The figures are
  consistent with the thesis's own bonus data read in the other direction (the
  frozen bonus CSV records a 13.0% bonus for NMB FY 2076/77, proposed in that
  year and issued in FY 2077/78, matching Chapter III's statement that the bonus
  ratio "represents that fiscal year's proposed bonus issued in the subsequent
  fiscal year", ch3:378), so no inconsistency is alleged — only a missing
  citation. Fix: cite the NMB FY 2077/78 annual report.

### C-09 — Appendix D's deadline "verification" is circular
- **Location:** app_d:182 (§D.3).
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED — read the sentence; the gap is defined in the same
  appendix (app_d:180–188 and `dataset.py`) as observation date minus deadline,
  so subtracting it from the observation date returns the deadline by
  construction.
- **Evidence:** "Each deadline was verified by subtracting the recorded gap
  from the observation date in Table~\ref{tab:mps_rd}."
- **Impact:** The sentence claims a verification that cannot verify anything:
  it checks internal arithmetic, not the deadline dates themselves. The
  deadlines (FY-end mid-July + nine months = mid-April; 13 April, 12 April in
  2024) follow from the statute reading the thesis discloses, but the specific
  Chaitra-end day for each year has no cited calendar source in Appendix D
  (the statute table cites the NEPSE calendar only via "the dataset's own
  trading rows", app_d:194–198). Fix: reword to state what was actually checked
  (internal consistency), and cite the calendar source for the Chaitra-end dates.
  This does not change any price: the observation dates themselves are verified
  against Merolagani in Appendix A.

### C-10 — Appendix D's stated report total is 0.01 MB below the register sum
- **Location:** app_d:10 (§D.1) vs app_d:22–94 (Table `tab:app_register`).
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED — summed the 30 register rows programmatically from the
  file as read: 5,663 pages (matches the stated 5,663 exactly) and 328.31 MB
  (stated: 328.30 MB).
- **Evidence:** "The 30 reports, 328.30 MB and 5,663 pages in total, cannot be
  printed in a thesis."
- **Impact:** Trivial — 0.01 MB on 328 MB, consistent with rounding of
  per-file sizes (each given to two decimals) or a total computed from
  unrounded sizes. Fix: state 328.31 MB or add "(rounded)". No claim or
  conclusion depends on it.

### C-11 — Appendix D invokes the AEA standard as a model while providing no code
- **Location:** app_d:6–14 (§D.1); app_d:342 (§D.8).
- **Severity:** Minor. **Revision scale:** Substantive (to fix by depositing code;
  Narrow to fix by keeping the current disclaimer).
- **Status:** VERIFIED — opened the AEA Data and Code Availability Policy
  (February 2026 version, https://www.aeaweb.org/journals/data/data-code-policy):
  authors "must provide the data, code, and other details of the computations
  sufficient to permit replication", materials "must be made available and
  retained in an openly accessible trusted data repository", and where data
  cannot be made public, authors must still "(iii) make the code publicly
  available" and "(iv) publicly document the source of the data". Appendix D
  provides the data (printed panel, Appendix B) and documents the sources, but
  states "no code is shared" and the thesis is "not … re-runnable from the
  thesis alone".
- **Evidence:** "The documentation follows the structure of the Data and Code
  Availability Policy of the American Economic Association … It is modelled on
  that standard and is not a claim of compliance with it." (app_d:6–14).
- **Impact:** None on the results — the thesis is explicit that it does not
  claim compliance, so there is no misrepresentation. The gap matters only for
  the standard the appendix itself invokes: under the AEA policy as opened, the
  code would have to be public even though the underlying data are public
  anyway. The honest options are to deposit the pipeline (substantive) or to
  keep the current, accurate disclaimer (no change). Not a submission blocker
  on its own terms.

### C-12 — Chapter III gives no software versions; most dependencies are unpinned
- **Location:** ch3:390–392 (§3.6.6); app_d:318 (§D.6);
  `data_analysis/analysis/requirements.txt`.
- **Severity:** Suggestion. **Revision scale:** Narrow.
- **Status:** VERIFIED — read §3.6.6 ("Data extraction, audit reconciliation,
  and panel assembly are executed in Python (pandas, numpy). Econometric
  modelling … using Python (statsmodels, seaborn, matplotlib)") — no versions
  anywhere in Chapter III. Appendix D names only "statsmodels 0.14.6, as pinned
  in the analysis requirements". The requirements file pins only
  `statsmodels==0.14.6`; pandas, numpy, scipy, seaborn, matplotlib, PyYAML,
  and pytest are `>=` ranges.
- **Evidence:** "Estimation was performed in Python using statsmodels 0.14.6,
  as pinned in the analysis requirements. No code is printed in this thesis."
  (app_d:318).
- **Impact:** A future reimplementation may land on different library versions;
  combined with C-11 (no code shared), exact re-execution is doubly out of
  reach. Recording the versions actually used (one line in §3.6.6 or §D.6)
  costs nothing.

### C-13 — Full-design VIFs are not reported; Chapter III reports substantive-only VIFs
- **Location:** ch3:361 (§3.6.4); `data_analysis/analysis/stats/diagnostics.py:25–36`.
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED (for the description gap) — read ch3:361 and the code:
  `vif_table` builds its design from "the substantive regressors (not the FE
  dummies)" (docstring, `diagnostics.py:25`). Chapter III discloses the
  exclusion ("Fixed-effect dummies are excluded from these VIF calculations").
  The full-design values (Model 1 BVPS 12.32; Model 2 BVPS×Post 259.32) are
  v1's recomputation (§M15, v1 finding F05); I did **not** independently
  re-derive them, and I do not present them as my own computation.
- **Evidence:** "Model~1 EPS and BVPS VIFs are approximately $1.16$. Model~2
  VIFs are $10.33$ (EPS), $2.28$ (BVPS), $15.15$ (EPS $\times$ Post), and
  $24.13$ (BVPS $\times$ Post). Fixed-effect dummies are excluded from these
  VIF calculations."
- **Impact:** Chapter III is transparent about the scope, so this is not a
  misstatement — but a reader reconstructing from Chapter III alone cannot see
  that the estimated design is far more collinear than the reported VIFs
  suggest, and the precision of δ_B (the object of H_4) is correspondingly
  harder to interpret. Fix: add the full-design VIFs (or a condition number)
  in one line. The analysis-level concern is v1's F05; this finding covers
  only the Chapter III description.

### C-14 — No ethics statement anywhere in scope (or in the thesis)
- **Location:** ch3 (whole file), app_a (whole file), app_d (whole file).
- **Severity:** Suggestion. **Revision scale:** Narrow.
- **Status:** VERIFIED (for the absence) — full-text search for "ethic" across
  the three in-scope files and across the whole thesis source tree returned no
  matches. The TU *Master's Degree Dissertation Guidelines (2019)*, Chapter II
  ("Research Ethics"), was opened and read during this task: its stated duties
  are honest reporting, acknowledgement of sources (plagiarism as misconduct),
  data retention and sharing ("the researcher must produce every bit of data to
  the supervisor … and keep them ready at the time of viva voce"), and
  confidentiality. No IRB-style approval requirement appears in the chapter
  text I read. I did not read the remaining pages of the Guidelines PDF
  (evaluation, appendices), so a further campus-level requirement cannot be
  excluded — see open question Q-3.
- **Evidence:** Absence verified as above; no quotation is possible for an
  absence.
- **Impact:** Low for this study — it uses public secondary data with no human
  subjects, so no approval would ordinarily be the applicable outcome — but the
  Guidelines' data-retention duty makes an explicit statement valuable, and
  Appendix D is the natural place for it. One sentence ("This study uses only
  published secondary data; no human participants, personal data, or
  confidential information were involved") closes it. This finding makes no
  claim about research misconduct of any kind.

### C-15 — Table 3.1's note misdescribes Merolagani as a retrieval source
- **Location:** ch3:124 (note to Table 3.1).
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED — read the note and Appendix D §D.3 (app_d:180), which
  states the dataset's scraper pulls from ShareSansar and Merolagani is the
  cross-check.
- **Evidence:** "Prices are expressed in Nepalese Rupees (NPR) per ordinary
  share, retrieved from capital market data aggregators (ShareSansar and
  Merolagani; cross-checked against FinancialNotices for FY 2081/82)."
- **Impact:** A reader could infer prices were retrieved from both aggregators;
  in fact the dataset close comes from ShareSansar via nepse-data and
  Merolagani supplies the LTP cross-check (29/30 exact matches). The same
  note immediately and correctly discloses that NEPSE official closes are
  unverified, so the substance is honest; the wording is imprecise. Fix:
  "retrieved from ShareSansar (via the nepse-data dataset) and cross-checked
  against Merolagani (all 30 cells) and FinancialNotices (FY 2081/82)".

### C-16 — The five-day window has no stated rationale (disclosed, not hidden)
- **Location:** ch3:91 (§3.3.4).
- **Severity:** Minor. **Revision scale:** Narrow (to add a rationale) or
  Substantive (to add a window-sensitivity analysis).
- **Status:** VERIFIED — read the sentence and searched Chapter III and
  Appendix D for any other justification; none exists.
- **Evidence:** "The five-day length is an un-derived operational choice; no
  substantive rationale for five days rather than another window is recorded
  in this thesis."
- **Impact:** The window is consequential by the thesis's own account:
  including the two delayed observations changes the Model 2 joint test to
  F(2,16) = 4.762 (p = 0.024), against F(2,14) = 2.954 (p = 0.085) in the
  28-row sample (ch3:217–221; v1 verified the N = 30 sensitivity, §M18).
  Stating the absence of a rationale is honest; it does not supply one. A
  one-paragraph sensitivity note (e.g. 3-day and 10-day windows) or a stated
  operational reason would convert a disclosed arbitrariness into a defended
  choice. This is a description finding, not a re-analysis: v1 already
  established the numerical consequence.

### C-17 — The unlisted 20th bank is not named
- **Location:** ch3:26 (§3.3.1).
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED — read §3.3.1; the bank is not named anywhere in
  Chapter III or Appendix D.
- **Evidence:** "Of these 20 licensed institutions, 19 are listed on NEPSE
  \citep{bhandari2026}."
- **Impact:** Small. The population is defined as licensed banks, not listed
  banks, so the unlisted bank is inside the population but outside the
  tradeable set; naming it (one clause) would let a reader check whether its
  exclusion from the price sample is mechanical (unlisted → no price) rather
  than a choice. The underlying "19 listed" count itself is UNVERIFIED (K-02).

### C-18 — "Prominent" (sampling criterion) is not operationalized
- **Location:** ch3:31 (§3.3.2, first criterion).
- **Severity:** Suggestion. **Revision scale:** Narrow.
- **Status:** VERIFIED — read the criteria list; no threshold (assets, deposits,
  branches, market capitalization) is given for "prominent".
- **Evidence:** "Participation in the 2023 Consolidation Wave: Prominent
  commercial bank series that executed horizontal statutory amalgamations or
  major corporate acquisitions that commenced joint commercial operations
  during the early-2023 consolidation wave (January--February 2023 /
  mid-FY 2079/80)."
- **Impact:** A reader cannot independently apply the criterion to the 20-bank
  population and recover the same five series; in practice the criterion is
  doing little work beyond "participated in the wave", since the wave itself
  had only five combinations. One clarifying clause (e.g. "all five
  combinations were candidates; four were selected because…", tied to C-01)
  would fix both findings together.

### C-19 — R7's one-sided adjustment is described accurately but its implication is not flagged
- **Location:** ch3:378 (R7); app_d:320 (§D.6).
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED — read ch3:378 and `robustness.py:123–135`: only BVPS
  is adjusted (`bvps_adj = bvps / (1 + bonus/100)`); EPS and price are
  untouched. Chapter III's wording ("using bonus-adjusted book value per
  share") matches the code, so the description is accurate; neither Chapter III
  nor Appendix D states that EPS and price remain on the old share base, or
  what that implies. The design-level criticism is v1's F08; I do not re-argue
  it here.
- **Evidence:** "Re-estimates Model~2 using bonus-adjusted book value per
  share ($\mathit{BVPS}_{\text{adj}} = \mathit{BVPS} / (1 + \text{bonus
  ratio})$) to evaluate parameter stability against share dilutions ($n =
  28$). Because the bonus ratio represents that fiscal year's proposed bonus
  issued in the subsequent fiscal year, $\mathit{BVPS}_{\text{adj}}$
  represents a pro-forma forward capitalization adjustment rather than a
  restated year-end book value."
- **Impact:** A reader could mistake R7 for a full bonus-dilution adjustment of
  the valuation relation; it is a one-regressor rescaling. One sentence
  ("EPS and MPS^RD are left unadjusted") makes the scope explicit. Whether R7
  should be rebuilt as a consistent adjustment is v1's F08, an analysis
  decision outside this review's remit.

**Finding counts (19 total):** 0 Critical; **1 Major** (C-01); **15 Minor**
(C-02–C-11, C-13, C-15–C-17, C-19); **3 Suggestion** (C-12, C-14, C-18).
1 + 15 + 3 = 19.

## 6. VERIFIED strengths in scope

| # | Strength | How verified |
|---|---|---|
| S-01 | Sample arithmetic is exact and consistent everywhere: 30 → 28, 13 pre / 15 post. | Counted the frozen panel CSV (`mps_rd_joined_panel.csv`): 30 rows, 28 with gap ≤ 5, 13 pre / 15 post; matches ch3:82–100, app_d:263–302, and `dataset.py:6–12`. |
| S-02 | All 28 numeric Table 3.1 prices match Appendix A exactly; the 2 missing cells match Appendix A's late prices. | Programmatic comparison of ch3 Table 3.1 against app_a Table A.1: 28 numeric cells, 0 mismatches; missing cells HBL/NIMB FY 2077/78 correspond to Appendix A prices 358.90 (6 Jun 2022) and 367.70 (30 May 2022). |
| S-03 | Price audit is complete: 30/30 cells, 29 exact Merolagani matches, 1 disclosed NPR 1.00 difference. | Read app_a Table A.1 in full (30 rows); note at app_a:85 states the resolution and that it "does not represent independent verification". |
| S-04 | The freshness rule is implemented exactly as described, with exclusion rather than imputation. | Read `dataset.py:6–12, 137` and the CSV gaps (54, 47 days); v1 independently counted the same 28 rows (§3, traceability row 1). |
| S-05 | Variable definitions are complete and internally consistent between Chapter III and Appendix D (EPS own-current rule; BVPS recomputed; DPS zero only for documented nils; Post absorbed). | Read ch3:217–266 against app_d:224–261 (codebook + four governing rules + restatement paragraph); all agree, including the three restated EPS values (GBIME 17.99→15.33; NMB 16.66→14.76; HBL 28.07→27.60). |
| S-06 | R1–R9 definitions in Chapter III match the pipeline code exactly. | Read `robustness.py:57–168` (`build_runs`) end to end and compared each run's label, sample, and regressor against ch3:369–381. |
| S-07 | Degrees-of-freedom accounting is correct where Chapter III states it (M1 16, M2 14, R4 13, R9 13). | Arithmetic recomputed from ch3:270–330, 376–380; Appendix D §D.6 and Chapter IV's Table 5 note agree (R1 16; R2/R3/R7/R8 14; R4/R9 13; R5/R6 10). |
| S-08 | HC3 is correctly described as heteroskedasticity-robust, explicitly *not* cluster-robust, and its pre-specification is real. | Read ch3:346 ("Cluster-robust covariance estimators are distinct from HC3…") and proposal `07_methodology.tex:187, 200` (HC3 pre-specified; "not a correction for the small number of clusters"). |
| S-09 | The covariance sensitivity that v1 found missing is now reported and matches v1's recomputation. | Read Chapter IV Table `tab:cov_sensitivity` (ch4:441–470) in the working tree: all 40 cells (R2–R9 × classical/HC0/HC1/HC2/HC3) match v1's §M07 table, including the note "Under the classical, HC0, HC1 and HC2 covariances, all eight joint tests R2–R9 reject at 5%; under HC3, only R6 rejects." Chapter III §3.6.3 (ch3:351) points to it accurately. See §8. |
| S-10 | Limitations are disclosed in Chapter III itself, not deferred to Chapter V. | §3(g) above lists nine candid limitations stated in Chapter III, each with its location; the serial-independence assumption and the bootstrap floor (ch3:352) and the post-hoc MDEs (ch3:367) are the clearest examples. |
| S-11 | Appendix D's register is internally verifiable: 30 rows, page total exact, SHA-256 prefixes mutually distinct. | Summed the register from the file as read: 5,663 pages (exact match to app_d:10); 30 SHA-256 12-character prefixes, all distinct; all 30 DPS pages fall within their files' page counts per the locators note (app_d:175). (SHA values themselves were not recomputed against the report files — see §10.) |
| S-12 | Appendix D states its own limits honestly, including that the study is "reproducible as a cross-checked aggregator-price study, not as an official-exchange-close study" (app_d:342). | Read §D.8 in full; the four limits (live-page drift, no verified NEPSE close, unconfirmed suspensions, printed rounding) match the disclosures in Chapter III and Appendix A. |
| S-13 | TU Guidelines Chapter III structure is followed: the chapter contains all five required elements (research design; population and sample; nature and sources of data; methods of analysis; research framework and definition of variables). | Compared ch3 §§3.2–3.6 against the Guidelines Chapter III text opened during this task (see §10, source 1), which lists exactly those five elements. Order differs trivially (framework §3.5 precedes methods §3.6; the Guidelines list methods fourth and framework fifth). |

## 7. Limitations acknowledged in Chapter III itself (inventory)

For reference, the limitations Chapter III states about its own design (all
VERIFIED by reading the cited lines; this is an inventory, not new findings):

1. Five-day window un-derived (ch3:91).
2. Price rule does not verify release dates or rule out leakage; disclosure
   dates investigated for only five bank-years, two settled, three pending,
   25 with no date recorded (ch3:217–221; app_d:188–192).
3. NEPSE official closes unverified against exchange floor records (ch3:124;
   app_a:85; app_d:342).
4. NMB FY 2076/77 price retention is not independent verification (ch3:166–168).
5. Two BVPS/NAV variances flagged as unresolved (HBL FY 2076/77 gap 0.05;
   NMB FY 2081/82 gap 0.69) (ch3:232–239; app_d:257).
6. Entity-timing mismatch FY 2078/79 retained in baselines (ch3:124 note ^c;
   handled by R6).
7. Serial independence assumed, untested; HC3 does not correct it (ch3:352).
8. Wild-cluster bootstrap cannot produce a 5% rejection (ch3:352).
9. No prospective power analysis; MDEs post hoc and optimistic (ch3:367).
10. HC3 is the designated estimator "not because the alternative estimators
    agree" (ch3:351).
11. Aggregate sector asset/market-cap shares "not claimed or evaluated"
    (ch3:29).

## 8. Changes relative to the v1 review (working tree vs commit 2d195bf)

v1 reviewed commit `2d195bf`. This review covers the working tree at HEAD
`2b4e10f` plus uncommitted changes. Two v1 findings are **no longer true as
stated** in the working tree, and both are improvements:

- **v1 F01 (Critical) — covariance sensitivity withheld.** In the working tree,
  Chapter IV now contains Table `tab:cov_sensitivity` (ch4:441–470) reporting
  all five estimators for R2–R9, with a note stating the HC3-specificity
  plainly, and Chapter III §3.6.3 (ch3:351) points to it. I verified all 40
  cells against v1's §M07 recomputed table (S-09). The underlying
  estimator-dependence v1 identified is unchanged; the *reporting* defect is
  fixed. This is the single largest change since v1.
- **v1 F16 (Minor) — Appendix D "submitted without any accompanying repository
  or code".** That sentence is gone from the working tree. Appendix D §D.1 now
  reads "This appendix is the reproducibility record for the analysis in this
  thesis" (app_d:4), and §D.8 states the no-code position precisely ("no code
  is shared", app_d:342). The residual issue is C-11, which is narrower.

All other v1 findings that touch Chapter III's *description* remain as v1
stated them where I checked: the VIF scope disclosure (F05 → C-13), the
serial-correlation omission disclosed in text (F10 → §7 item 7), the R7
one-sided adjustment (F08 → C-19), the post-hoc MDEs (F14 → §7 item 9), and
the bootstrap floor (F03 → S-10/K-18). I did not re-audit v1's statistical
findings; where I rely on a v1 recomputation (K-16, K-17, K-18, C-13's
full-design VIF values), I say so explicitly.

## 9. Open questions

1. **Prabhu–Century exclusion (C-01).** Was the fifth combination excluded for
   a substantive reason (data, listing, timing) or by default? Only the author
   can answer; the thesis gives no reason.
2. **BAFIA deadline arithmetic.** The statute text I opened confirms the two
   duties and the nine-month publication duty, and the thesis discloses its
   Chaitra-end operationalization. Whether "within nine months of the next
   fiscal year" must be read as FY-end + 9 months (the thesis's reading) rather
   than another anchor is a legal-reading question I cannot settle; the
   thesis's reading is disclosed, not hidden. (v1 open question 1, narrowed.)
3. **Institutional requirements beyond the Guidelines text I read.** I read the
   TU Guidelines PDF lines 0–423 of 967 (Chapters I–III and the start of the
   documentation section), including Chapter II (Research Ethics) in full.
   A campus-level requirement outside that span (e.g. in the evaluation or
   appendix pages) cannot be excluded. UNVERIFIED / CANNOT DETERMINE.
4. **Underlying factual claims I did not open.** The NRB population counts
   (K-01), the "19 listed" claim (K-02), and the merger dates/swap ratios
   (K-05) rest on sources I did not open; the 30 annual reports were not
   re-read (extraction treated as ground truth, per v1's scope decision).
   UNVERIFIED / CANNOT DETERMINE.
5. **Whether the author will deposit the code (C-11).** A supervisor/institution
   decision, not something this review can determine.

## 10. Verification log

### What was read in full (this task)

- `src/thesis/chapters/chapter_03_research_methodology.tex` (392 lines).
- `src/thesis/appendices/appendix_a.tex` (96 lines).
- `src/thesis/appendices/appendix_d.tex` (342 lines).
- `docs/thesis_review/v1/data_analysis_review.md` (694 lines, in full,
  including §§9–10) — for context on what v1 covered; used only to avoid
  re-auditing the analysis and to attribute v1 recomputations where relied on.
- `src/proposal/sections/07_methodology/07_methodology.tex` lines 187–206
  (HC3 pre-specification) — read to check Chapter III's pre-specification claim.
- `src/thesis/chapters/chapter_04_results_and_discussion.tex` lines 425–470
  (Table `tab:t5_robustness` note and Table `tab:cov_sensitivity`) — read only
  to verify Chapter III's cross-reference resolves and the values match v1.
- `data_analysis/analysis/dataset.py` (freshness rule, lines 1–15, 128–190),
  `data_analysis/analysis/stats/robustness.py:57–168` (`build_runs`),
  `data_analysis/analysis/stats/diagnostics.py:20–40` (`vif_table`),
  `data_analysis/analysis/stats/models.py:20–30` (FE formula construction),
  `data_analysis/analysis/requirements.txt` — read to check text-vs-code
  consistency only.
- `data_analysis/data_extract/output/manual_review/mps_rd_joined_panel.csv`
  and `..._bonusadj.csv` — counted programmatically (30 rows; 28 clean;
  13 pre / 15 post; gaps 54/47; DPS zeros 12/30; bonus column in percent).
- `src/thesis/references.bib` — checked that every citation key used in the
  three in-scope files exists (all 15 Chapter III keys, all 7 Appendix D keys;
  Appendix A cites nothing). Checked the `aea2026datacode`,
  `wilkinson2016fair`, `bhandari2026`, `nrb2023list`, `nrb2023bsr` entries
  in full.
- `docs/thesis_review/v2/pass_a_note.md` — read because it sits in the output
  directory; it is a prior examiner's first-look note written before reading
  Chapters II–IV. It was **not** used as evidence for any finding: every
  finding above rests on a file I opened and cite directly. (Its question
  about the Prabhu exclusion coincides with C-01, which I verified
  independently from ch3:29.)

### What was counted or computed (scratch only, in /tmp or via read-only commands)

- Panel CSV counts (sample, pre/post, gaps, DPS zeros, bonus values).
- Appendix D register sums (5,663 pages; 328.31 MB; 30 distinct SHA-256 prefixes).
- Table 3.1 vs Appendix A price comparison (28 numeric cells, 0 mismatches).
- Date arithmetic for the 54- and 47-day delays.
- VIF ≈ 20.25 from r = 0.975 (1/(1−r²)); Cook's threshold 4/28 ≈ 0.143.
- Citation-presence greps across all thesis chapters and appendices
  (SEBON/MoF/Economic Survey/Merger Bylaws/circulars: no citations found;
  "ethic": no matches in the whole thesis source tree).
- No repository file was modified, built, or compiled at any point.

### Sources consulted (external)

1. **Tribhuvan University, Faculty of Management, *Master's Degree Dissertation
   Guidelines — 2019* (Office of the Dean, FOM, TU).**
   URL: https://spacampus.edu.np/public/uploads/downloads/e3ce3b941aa305662605c049e67c9c988cce22bf.pdf
   — **Fully read, lines 0–423 of 967** (Chapters I–III, incl. Chapter II
   Research Ethics and the Chapter III methodology-contents list). Used for:
   the five required Chapter III elements (S-13); the ethics duties (C-14);
   the representativeness expectation (C-01). Lines 424–967 not read.
2. **American Economic Association, *Data and Code Availability Policy*
   (February 2026 version).**
   URL: https://www.aeaweb.org/journals/data/data-code-policy
   — **Fully read** (178 lines). Used for C-11 and K-21.
3. **Wilkinson, M. D. et al. (2016), "The FAIR Guiding Principles for
   scientific data management and stewardship", *Scientific Data* 3, 160018,
   doi:10.1038/sdata.2016.18.**
   URL: http://pure.manchester.ac.uk/ws/files/57031836/sdata201618.pdf
   — **Fully read in part**: lines 0–304 read directly, plus a targeted find
   for "R1.1" confirming Box 2 (R1.1 licence; R1.2 provenance). Used for K-21.
4. **Banks and Financial Institutions Act, 2073 (2017), Section 59
   (Nepal Gazette text, via kaanun.app).**
   URL: https://kaanun.app/en/section/Balance-sheet, Profit And Loss__i6459d1e6d955a55e248d2bd1
   — **Fully read** (28 lines). Used for K-09. The Nepal Law Commission
   repository text and the NRB English rendering were *not* opened; the thesis
   cites the Gazette text via the Law Commission repository, which I did not
   independently open.
5. **v1 review** (`docs/thesis_review/v1/data_analysis_review.md`) — read in
   full; treated as context and as the source of attributed recomputations
   (K-16, K-17, K-18, C-13 values), never as a substitute for reading the
   thesis files themselves.

No other external source was used for any claim in this review. In particular,
no claim is made about the contents of the NRB lists, the Bhandari et al.
(2026) article, any bank annual report, Ohlson (1995), Kwon (2020), MacKinnon
& White (1985), or Cameron & Miller (2008) beyond what the thesis text and
the v1 review state; those are marked UNVERIFIED above where relevant.

### What could not be done, and why

- **Re-reading the 30 annual reports** (5,663 pages) to verify extracted
  figures, merger dates, swap ratios, restatements, or DPS announcement dates:
  not done — extraction is out of scope per v1, and the reports were not
  re-opened. Findings C-04, C-05, C-06, C-08 are about the *absence* of
  locators/dates/citations in the text, which was verified, not about the
  underlying figures.
- **Recomputing SHA-256 values** against the report files: not done; the
  register's internal consistency (distinct prefixes, page/size sums) was
  checked instead. Whether the files on disk match the register is therefore
  UNVERIFIED by this review.
- **Re-deriving statistics** (coefficients, VIFs, diagnostics, MDEs,
  bootstrap): not done — that is v1's remit. Where this review states such
  numbers match, the match is v1's recomputation, attributed as such.
- **Visually inspecting rendered figures**: Figure 3.1 (TikZ code read) and
  Figure A.1 (file existence confirmed) were not rendered or visually checked.
  The thesis was not built or compiled, per the task rules.
- **Live verification of report URLs, Wayback captures, or aggregator pages**:
  not done; access dates and routes are taken as stated in Appendix D.
- **TU Guidelines lines 424–967**: not read (see open question 3).

### Read-only confirmation

`git status` was run at the start of this task (before any file was created)
and again at the end, after this file was written. Both runs show the same 33
pre-existing modified files (uncommitted working-tree changes present on
arrival, including `src/thesis/chapters/chapter_03_research_methodology.tex`,
`src/thesis/appendices/appendix_a.tex`, and `src/thesis/appendices/appendix_d.tex`)
and the same pre-existing untracked paths (`docs/thesis_supervisor/`,
`pytest.ini`). No pre-existing file was modified, renamed, deleted, or
reformatted by this review, and the thesis was not built or compiled.

The only file created by this review is
`docs/thesis_review/v2/review_ch3_method.md`. The directory
`docs/thesis_review/v2/` also contains `pass_a_note.md` (pre-existing on
arrival, read but not used as evidence) and four other `review_*.md` files
(`review_ch4_results.md`, `review_ch5_back.md`,
`review_criteria_compliance.md`, `review_front_ch1.md`) that appeared during
this session and were created by other parallel reviewers, not by this review.
All scratch work (CSV counts, register sums, price comparison, greps) was done
with read-only commands; nothing was written outside this one file.
