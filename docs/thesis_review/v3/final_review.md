# Final independent pre-submission review of the thesis (v3)

**Thesis:** *Value Relevance of Accounting Information Before and After the Banking Consolidation Wave: Evidence from Nepalese Commercial Banks* — Asmita Subedi, Triveni International College, Master of Business Studies (MBS), Tribhuvan University (TU), Faculty of Management (FOM). November 2026.

**Repo:** `~/workspace/verbose-chainsaw`. **HEAD reviewed:** `2b4e10f` ("Add independent data-analysis review (v1)", 2026-11-14). **Version reviewed:** the working tree as it stands (HEAD plus uncommitted changes, including the v2 fix loop's patches). **Review date:** 18 November 2026. **Review file:** `docs/thesis_review/v3/final_review.md` (this file).

**How this review was produced.** A coordinator ran six independent scope reviews in parallel (front matter + Chapter I; Chapter II + references; Chapter III + Appendices A/D; Chapter IV; Chapter V + Appendices B/C/E; criteria/compliance + deliberately-untouched items + figure captions + language), each writing its own file in `docs/thesis_review/v3/` (`review_front_ch1.md`, `review_ch2_refs.md`, `review_ch3_method.md`, `review_ch4_results.md`, `review_ch5_back.md`, `review_criteria_compliance.md`). This file consolidates them: findings are deduplicated into one consolidated ID per issue, contradictions reconciled, and the consequential claims spot-verified by the coordinator against the thesis source before inclusion (see §12). The test suite was re-run by the coordinator read-only-safe (36/36 pass).

**What this review is and is not.** It is a fresh, independent, read-only pre-submission review. It verifies the v2 fix loop's work (Part A: all 85 v2 findings, using the hallucination audit's corrected versions) and it reads the whole thesis fresh (Part B: any remaining issue, including new issues introduced by the loop's patches). It does not re-audit the data or the statistics (v1's remit); it checks only that the text reports and interprets the analysis consistently with the code and outputs. It does not check plagiarism and makes no judgement about authorship or AI-tool use.

**Status vocabulary (exactly one per finding):** VERIFIED (how is stated), INFERRED (basis stated), UNVERIFIED / CANNOT DETERMINE (reason stated). **Fix verdicts (Part A):** FIXED / PARTIALLY FIXED / NOT FIXED / INCORRECTLY FIXED / FALSE FINDING. **Severity:** Critical / Major / Minor / Suggestion. **Revision scale:** Narrow (a sentence, paragraph, note, label, or mechanical change) / Substantive (reworking a section or table, or adding material that only the author can supply) / Fundamental (reformulating aims or hypotheses, a new study or analysis). No finding in this review requires a Fundamental revision.

**Plagiarism checking is not covered by this review.** No judgement is made about authorship or AI-tool use.

---

## 1. Scope, assumptions, and ground rules

### 1.1 What was reviewed

The whole thesis as it stands in the working tree: front matter (title page, Certification of Authorship, Report of Research Committee, Approval Sheet, Acknowledgements, Table of Contents, List of Tables, List of Figures, Abbreviations, Abstract), Chapters I–V, References (`src/thesis/references.bib`, 75 entries), Appendices A–E, the LaTeX configuration (`src/thesis/main.tex`, `src/thesis/config/`), the in-repo guideline material (`docs/thesis_guidelines_reference/`, `docs/instructions/instructions_for_paper.md`), and the v1 review (`docs/thesis_review/v1/data_analysis_review.md`) for follow-up context only. Every chapter, table, figure, appendix, and claim in the abstract and conclusion is either REVIEWED in §5 or listed as NOT REVIEWED in §5.6 with a reason.

### 1.2 What was not reviewed (out of scope by the task)

- The extracted data are treated as correct and are not audited. The 30 annual reports (5,663 pages) were not re-read; extracted figures, merger dates, swap ratios, restatements, and DPS announcement dates were not verified against the reports (except where a scope reviewer checked a printed value against its named source file inside the repo).
- The statistical and methodological correctness of the analysis is v1's remit and is not re-audited. This review checks only that the thesis text reports and interprets the analysis consistently with the code, the outputs, and v1.
- Things not observable from the repository (the candidate's research process, supervision, oral defence performance) are listed as NOT ASSESSABLE where the criteria touch them (§11).
- No plagiarism check was run.

### 1.3 Working-tree state (verified by the coordinator, 18 Nov 2026)

- `git rev-parse HEAD` = `2b4e10f8949c834dde3a3d3c674e2c86f828a9fc`.
- `git status --short`: **42 entries — 39 modified files + 3 untracked paths** (`docs/thesis_review/v2/`, `docs/thesis_supervisor/ohlson-value-relevance-pivot-2026-10-27.md`, `pytest.ini`), plus the new `docs/thesis_review/v3/` files created by this review. The 39 modified files are the accumulated uncommitted changes (the 2026-11-16 passes, the 17-round loop, and the v2 fix loop). No commit was made by this review.
- Tests: re-run by the coordinator read-only-safe (`PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`, no files written): **36 passed, 0 failed**.

### 1.4 Read-only compliance

No thesis, code, data, config, or v1/v2 file was modified, renamed, deleted, or reformatted by this review. The thesis was **not built or compiled** (the author builds the PDF manually); all formatting/compliance checks are source-level only. All scratch work was confined to `/tmp`. The only files created are the seven review files in `docs/thesis_review/v3/` (the six scope reviews plus this consolidation). A final `git status` check is recorded in §12.

### 1.5 Prior material — used as claims to check, never as evidence

The v2 review (`docs/thesis_review/v2/content_review.md`, 85 findings), the hallucination audit (`docs/thesis_review/v2/verification_audit.md`, 65 CONFIRMED / 20 CORRECTED / 0 REFUTED), and the fix-loop log (`~/workspace/review-audit-scratch/loop-v2/LOOP_STATUS.md` and `ROUND_*.md`) were read only to know what was claimed. No finding in this review rests on their authority: every verdict below rests on a grep, count, read, or recomputation re-run against the thesis source in this task, by a scope reviewer or by the coordinator. Where a scope reviewer and the coordinator disagree, the coordinator's own check governs and the disagreement is stated (see s06, §8; abstract word count, §10/§12).

### 1.6 Assumptions stated, not assumed silently

- The institution, level, and thesis type were **discovered from the repository, not assumed**: TU FOM MBS dissertation from Triveni International College (title page, `src/thesis/front/titlepage.tex`; `src/thesis/main.tex:4` names the 2019 FOM Guidelines as the format source). The thesis type is a **monograph dissertation** (single sustained study, five chapters, no compilation of papers) — INFERRED from its structure; nothing in the repo suggests a compilation or practice-based format.
- The submitting author's name is taken from the thesis itself (Asmita Subedi, Roll No. 67514/24, Regd. No. 7-2-48-1060-2018). Whether that name is correct against the college record was **not verified** by this review (see §11).
- Supervisor and chairperson names are unknown in the source (dotted blanks, never invented); this review does not supply them.
- The governing guideline is taken to be TU FOM *Master's Degree Dissertation Guidelines 2019* as held in the repo (see §3). Its currency was not independently verified against a live TU source beyond the checks in §3 (see §11, open question).

---

## 2. Understanding of the thesis: problem, aims, questions, hypotheses, contribution, structure, type and level

### 2.1 Problem and motivation

Nepalese commercial banks underwent a consolidation wave in early 2023 (five combinations commencing joint operations January–February 2023) after a 2015/16 NRB capital mandate (paid-up capital NPR 2bn → 8bn) cut the licensed population from an apex of 32 banks (FY 2011/12) to 20 by mid-October 2023. Prior Nepalese studies of share-price determinants are, the thesis argues, static (pooled OLS / static panels assuming parameter stationarity), circular (they regress market price on the price-to-earnings ratio, which embeds the dependent variable), mistimed (they price shares at fiscal-year-end, months before audited disclosure), and silent on degrees of freedom and small-cluster inference. The thesis tests whether the value relevance of EPS and BVPS changed across the consolidation divide, under Ohlson (1995) residual income valuation (RIV) with clean-surplus accounting. (Locations: `src/thesis/chapters/chapter_01_introduction.tex` lines 7–41; `src/thesis/chapters/chapter_02_literature_review.tex` §§2.2–2.5.)

### 2.2 Aims, research questions, hypotheses

- **General objective** (Ch1:52): to examine the value relevance of EPS and BVPS among Nepalese commercial banks and whether the valuation relationships underwent a structural regime shift following the 2023 consolidation wave.
- **Specific objectives** (Ch1:56–67): (1) estimate baseline value relevance of EPS/BVPS in a two-way fixed-effects framework; (2) test whether valuation slopes differed pre- vs post-consolidation via interaction parameters (δ_E, δ_B) and a joint Wald test; (3) evaluate robustness across seven specification variants (ROA substitution; DPS inclusion; FY 2079/80 transition-year exclusion; FY 2078/79 entity-timing exclusion; bonus-adjusted metrics; restated EPS; NMB FY 2076/77 Kanchan-exclusion).
- **Research questions** (Ch1:44–47): RQ1 — are EPS/BVPS associated with post-reporting-deadline prices (MPS^RD)? RQ2 — did the associations differ between pre-consolidation (FY 2076/77–2078/79) and post-consolidation (FY 2079/80–2081/82)? RQ3 — are the baseline and interaction findings robust to alternative profitability specifications, dividend inclusion, bonus adjustment, earnings restatements, and exclusion of structural transition periods, **and sensitivity analysis excluding the NMB FY 2076/77 bank-year with the Kanchan acquisition timing mismatch** (added by the loop; Ch1:46).
- **Hypotheses** (Ch1:70–136): H1 (β_E = 0), H2 (β_B = 0), H3 (δ_E = 0), H4 (δ_B = 0), plus a joint hypothesis (δ_E = δ_B = 0); two-tailed tests at α = 0.05. RQ3 has no corresponding hypothesis (stated explicitly at Ch1:75: it "is answered by the robustness suite R3–R9 (Chapter IV), not by a hypothesis test"). H1/H2 are stated for Model 1 and re-examined in Model 2 (Ch1:75).
- **Design** (Ch1:13, Ch3:29): purposive sample of five bank series (four merged: GBIME, HBL, KBL, NIMB; one unmerged benchmark: NMB) over six fiscal years FY 2076/77–2081/82; target 30 bank-years, clean sample N = 28 (13 pre / 15 post) after two observations were dropped for merger-related trading suspensions (HBL and NIMB FY 2077/78, 54 and 47 days late). Prices measured at the first trading session on/after the BAFIA §59(2) nine-month reporting deadline (MPS^RD), with a five-day freshness window and no imputation. Models: Model 1 (baseline two-way fixed effects); Model 2 (regime interactions); nine-specification robustness suite R1–R9; HC3 heteroskedasticity-robust inference on Student's t residual df.

### 2.3 Claimed contribution and novelty

The thesis claims two legs (Ch1:15, Ch1:148–150): (a) an **empirical** contribution — the first formal regime-shift test of EPS/BVPS value relevance across the 2023 consolidation wave in Nepal ("No empirical study identified in the literature reviewed in Chapter II has formally evaluated whether the valuation coefficients … shifted … using an explicit regime-interaction econometric framework", Ch1:30); and (b) a **methodological** contribution — the MPS^RD deadline-based pricing protocol, exclusion of circular P/E regressors, and HC3 discipline with disclosed degrees of freedom. The empirical leg returns null results (all four hypotheses fail to reject; joint Wald F(2,14) = 2.954, p = 0.085), so as written the contribution rests mainly on the protocol leg — whose key premise (actual publication dates) is verified in only 2 of 30 bank-years (Ch1:148, 185–186). The abstract now states this qualification ("although actual publication dates were verified in only 2 of 30 bank-years", abstract:15) and no longer claims the study "resolves" the limitations (abstract:15 now reads "addresses").

### 2.4 Main conclusions

No statistically significant EPS or BVPS association in Model 1 (β_E = 2.095, p = 0.616; β_B = 0.219, p = 0.908; R² = 0.948); no significant pre-consolidation slopes or interactions in Model 2 (pre β_E = 5.577, p = 0.140; pre β_B = 0.100, p = 0.940; δ_E = −3.124, p = 0.448; δ_B = −1.758, p = 0.175; implied post 2.453, p = 0.298; −1.658, p = 0.161); joint test fails to reject at 5% under HC3 (F(2,14) = 2.954, p = 0.085) — a result specific to HC3 (all eight joint tests R2–R9 reject under classical/HC0/HC1/HC2; only R6 rejects under HC3, unadjusted p = 0.021, Holm-adjusted p = 0.169). The evidence for a regime shift is therefore sensitivity-dependent, not conclusive. Results are reported as calendar-period associations, not as an established causal merger impact. Policy implications are drawn for asset-quality reviews, trading-halt limits, and centralised electronic filings, heavily hedged in Chapter V.

### 2.5 Structure and type

Five chapters (I Introduction; II Literature Review; III Research Methodology; IV Results and Discussion; V Summary and Conclusion), References, Appendices A–E. Intended audience: the TU FOM examiners and the Nepalese banking/accounting research community. Level: master's dissertation (MBS). Type: monograph (INFERRED from structure — a single study, not a compilation of papers).

### 2.6 What changed since v2 (verified in this review — see §8 for the full table)

- **Chapter I:** RQ3 now names the Kanchan exclusion (M02); the headline-results paragraph moved out of §1.1 Background to the end of the chapter at Ch1:212, now carrying all five headline figures (M03/M04); the abstract no longer overstates (M05); two new Limitations bullets — estimator-dependence (M06) and power/within-bank independence (m04); HC3 reworded so it is not presented as the small-cluster answer (M12, Ch1 limb); abbreviations DP/DYR removed (m02); Kanchan figures cited (m08); H1/H2 re-examination in Model 2 stated (m07).
- **Abstract:** "resolves" → "addresses"; 2-of-30 qualification added; "without establishing whether book-value substitution occurred". Length grew by ~23–30 words (see §10, V3-N01 — the loop's "~12 words" claim is wrong).
- **Chapter II:** Table 2.1 sample-size flags now match the audit's corrected counts (m17); all six flagged variables now in the prose (m18); formal value-relevance definition plus Barth/Holthausen–Watts paragraph added with two new bib entries (m19); Ohlson DOI added (m12); Wilkinson 53-author list (m14); 40 article + 16 book/techreport/misc titles sentence-cased (m13, one miss remaining); new `nmb2021report` bib entry.
- **Chapter III + App D:** R5/R6 df now derived (m24); ROA averaging defined (m25); two new App D tables — 30-row DPS announcement-dates table (m26) and 30-value bonus-ratios table (m27/m51) — both verified 30/30 against their sources; restatement locators added (m28); NRB bullet reworded, BSD circulars removed (m29); full-design VIFs added (m31); 328.30 → 328.31 MB (m32); AEA disclaimer tightened (m33); Table 3.1 note reworded (m34); unlisted 20th bank named (m38); R7 one-sided flag (m39); ethics sentence (s11); "prominent" removed from Ch3 (s12).
- **Chapter IV:** Table 4.6 note carries the Holm caveat (M07); §4.3.2 rewritten to flag the DPS–price correlation (M08, partial); all four Model 2 CIs now in the text (M09); hypothesis table standardised (m41); dividend-associations bullet added (m43); FE-only derivations added (m44, partial); Table 4.1 note discloses unrounded computation (m45, partial); detectable effects stated (s13); bootstrap p now 0.0625 (s16).
- **Chapter V + App B/C/E:** RQ3 restatement names Kanchan (M02); limitations restatement added (M10); Table 5.1 R6 cell now "Sensitivity only — no decision (Holm-adjusted p = 0.169)" (M13); bare `$MPS^{RD}$` eliminated thesis-wide (m48 — true total was 14, not the loop's 10); App E note expansions added (m49, partial); App C coverage corrected and notes added (m52); LOT/LOF single-spaced (m55); new App E table `tab:app_postslopes` (implied post-consolidation slopes, R2/R5/R6) computed from the frozen `results.pkl` — all six rows independently recomputed exactly by the Ch5 scope reviewer.
- **Figures:** all 11 figure environments are now caption-below; preamble `position=below` (M11).
- **References:** 72 → 75 entries (new: `barth2001`, `holthausen2001`, `nmb2021report`); 75 bib keys / 75 cited keys / 0 orphans (re-run by the Ch2 scope reviewer).
- **Deliberately unchanged:** M01 (Prabhu–Century, no reason stated anywhere — verified by the coordinator: "Prabhu" occurs exactly twice in the whole thesis, Ch1:30 and Ch3:31); the SEBON/MoF bullets (Ch3:160–161); the other accepted limitations; the §11 supervisor items.

---

## 3. Review criteria used, where each came from, and whether they are the institution's own or a proxy

### 3.1 The institution's own rules (governing)

**Tribhuvan University, Faculty of Management, *Master's Degree Dissertation Guidelines — 2019* (Office of the Dean, FOM, TU).** Source opened: the repo copy `docs/thesis_guidelines_reference/01_TU-FOM_Masters-Dissertation-Guidelines-2019.pdf` (28 pages; SHA-256 matches `00_README.md`). The criteria scope read the full extracted text (1,103 lines); other scope reviews read the chapters relevant to them. The thesis itself names the 2019 guideline as its format source (`src/thesis/main.tex:4`). The key rules applied (FOM 2019, with locations) — all re-verified by the criteria scope reviewer in this task:

| Rule | Content (paraphrase; exact wording quoted in the criteria scope, §1.1) |
|---|---|
| R-01 (p. 9) | Prefatory order: Title page; Certification of authorship; Report of Research Committee; Approval sheet; Acknowledgments; Table of contents; List of tables; List of figures; Abbreviations; Abstract. |
| R-02 (p. 10) | Abstract: "usually a paragraph or two and always less than a page … Limit the abstract in one page"; keywords "not more than five"; contents: purpose/objectives, methods briefly, major findings, conclusions and implications; "Do not include information that does not appear in the body of the report". |
| R-03 (pp. 10–15) | Five chapters (I Introduction; II Literature Review; III Research Methodology; IV Results and Discussion; V Summary and Conclusion); chapter contents may be altered "upon the advice of the supervisor; but that must be justified by the need of the study". |
| R-04 (pp. 11–12) | Chapter I: Background (guide 2–3 pp.), Problem statement (2–4 pp., ends by raising research questions), Objectives (general + specific, action verbs), Hypotheses (if any), Rationale, Limitations (distinguish scope from limitations). |
| R-05 (pp. 12–13) | Chapter II: introduction linking Ch. I, theoretical review, empirical review, policy/regulation literature; "should clearly establish with evidence that there exists research gap"; guide 10–20 pp.; APA 6th edition citation and referencing. |
| R-06 (p. 13) | Chapter III: introduction + (i) research design, (ii) population and sample, (iii) nature and sources of data, (iv) methods of analysis, (v) research framework and definition of variables. |
| R-07 (pp. 14–15) | Chapter IV: Results (answer RQs / test hypotheses; for inferential tests "include the obtained value of the test statistic, the degree of freedom, etc."); Discussion (interpret against theory and prior findings; care for bias, imprecision, sample size, limitations). |
| R-08 (p. 15) | Chapter V: Summary, Conclusion ("draw the conclusion only from the findings of the study"), Implications (policy makers, practitioners, academic community; recommendations and future research under Implications). |
| R-09 (pp. 15–16) | References (only sources cited) after the main text, then appendices; APA 6th. |
| R-11/R-12 (pp. 20–21) | 1.5 line spacing; margins top/bottom/right 2.54 cm, left 3.18 cm; Times New Roman 12 pt. (Note: FOM p. 20 contradicts itself on spacing — quotations and references appear in both the 1.5 and the single-spacing lists; see V2-s20.) |
| R-13 (p. 21) | Pagination: main body Arabic at top right from Chapter I; front matter lowercase Roman at bottom centre; title page counted but unnumbered. |
| R-14 (p. 21; App. C pp. 27–28) | "Figures must have numbers and captions under the figures. Tables have their titles and numbers above the tables." Appendix C: table notes below the table; abbreviations in tables explained below the table. |
| R-15 (p. 8) | Title: concise, significant variables and their relationship; avoid abbreviations; "generally suggested to limit the length of the title within 12 words" (proposal-writing passage, phrased as a suggestion). |
| R-16 (pp. 5–6) | Research ethics (Ch. II): fabrication, falsification, plagiarism are misconduct; duties: data retention and sharing, plagiarism/permission, confidentiality. No ethics-approval, consent, conflict-of-interest, funding, or AI-disclosure rule appears. |
| R-17 (p. 24) | Certification of Authorship template (not submitted elsewhere; assistance acknowledged; all sources cited). |
| R-18/R-19 (pp. 23–26) | Title-page and Research Committee / Approval Sheet templates. |
| R-20 (pp. 4, 7, 22) | Dissertation standard: "a substantial document presenting independent research that makes a contribution to the current body of knowledge"; "Correct grammar, punctuation, and spelling always should be used"; English only. |

**What FOM 2019 does not contain (VERIFIED by full-text search in this task):** no examiner rubric, no marking criteria, no outcome categories, no pass mark, no per-criterion weights. On evaluation (p. 21) it gives only a two-step process and a weighting: college step (supervisor, internal examiner, invited experts, viva) at 25%, FOM Dean's Office step (two experts) at 75%. Appendix A (p. 22) lists **12** conditions (the audit's correction of v2's "11" is confirmed by the criteria scope reviewer's own count; the twelfth is college record-keeping). No total page or word limit for the dissertation; no abstract word limit (only "less than a page"); no required declarations beyond Certification of Authorship. One caveat, carried from v2: FOM p. 7 directs students to "updated regulations available at the official website of the FOM" for the grade — currency of the 2019 edition therefore remains UNVERIFIED in the strict sense (see §11).

### 3.2 Proxy criteria (labelled as such, never as TU's rules)

**University of Essex, *Principal Regulations for Research Degrees 2025–26*, §4.33** — outcome categories used ONLY as a labelled yardstick for revision scale, never as TU's rules. Re-verified verbatim from the live regulations by the criteria scope reviewer in this task: (a) "Pass subject to no corrections"; (b) "Pass subject to typographical/presentational corrections"; (c) "Pass subject to minor corrections to be made within three months. … Minor corrections should not require the candidate to conduct further research or undertake substantial further work. These include typographical errors, clarifying points, rephrasing, editing/adding paragraphs, correcting references, etc."; (d) "Pass subject to major corrections to be made within six months. … Major corrections require the candidate to undertake substantial further work but the corrected thesis should not require re-examination. Such major corrections include more extensive editorial revisions, the addition of substantial new material, re-writing of substantial parts of the thesis, re-analysis of existing data, etc."; (e) "Referral for re-examination in up to 12 months"; (f)–(j) lower-award outcomes (omitted from v2's summary — selective, not false); (k) "Fail." Reg. 4.19: "The thesis will include a summary or abstract of the work not exceeding 300 words in length." Reg. 4.1 + footnote 1 confirm "Masters by Dissertation" and that "'Thesis' includes dissertations submitted for the degree of Masters by Dissertation."

**Nearest proxy category for this thesis:** see §13.

---

## 4. Inventory, claims register, traceability matrix, and bookend check

### 4.1 Inventory (verified in this task)

| Item | Count / state | Verified by |
|---|---|---|
| Chapters | 5 (I–V), all present | All scopes |
| Tables | 11 table environments, all with captions above the tabular (9 Ch IV, 1 Ch III, 1 Ch II longtable) | Criteria scope |
| Figures | 11 figure environments, all caption-below (1 Ch III TikZ, 7 Ch IV, 1 App A, 2 App C) | Criteria scope (per-figure table) |
| References | 75 entries; 75 cited keys; 0 cited-but-missing; 0 uncited | Ch2 scope (re-run) |
| Table 2.1 | 26 rows; 19 flagged "Circular P/E inclusion"; 15 studies test both EPS and BVPS; 10 rows carry "not stated" flags | Ch2 scope (re-run) |
| Appendix E tables | 13 (was 12; new `tab:app_postslopes`) | Ch5 scope |
| Abbreviations | 95 entries; no duplicates; DP/DYR rows removed | Front + criteria scopes |
| Abstract | 2 body paragraphs; 5 keywords; word count method-sensitive (see §10, V3-N01) | Coordinator (§12) |
| Appendices | A (price verification, 30 rows), B (dataset, 30 rows), C (diagnostics/forest), D (sources/reproducibility), E (estimation outputs) | Ch3/Ch5 scopes |

### 4.2 Claims register (headline claims, verified in this task)

| # | Claim | Location | Status |
|---|---|---|---|
| K-01 | Five combinations commenced joint operations Jan–Feb 2023 | Ch1:30 | VERIFIED as stated (cited to `nrb2023bsr`); the fifth (Prabhu–Century) is listed but not sampled — V2-M01 |
| K-02 | Population 20 licensed banks; sample 5 series = 25.0% | Ch3:28–31 | VERIFIED arithmetically; "19 listed" count UNVERIFIED (sources not opened) |
| K-03 | Clean sample N = 28 (13 pre / 15 post); 2 delayed rows missing | Ch1:175–176, Ch3, App A | VERIFIED (Table 3.1 vs App A agree cell-for-cell; Ch3 scope) |
| K-04 | MPS^RD protocol: first session on/after the BAFIA nine-month deadline; 5-day window; no imputation | Ch3:93, Ch3:223 | VERIFIED as written; five-day rationale still un-derived (m35 partial); Chaitra-end calendar source still uncited (m30 partial) |
| K-05 | Model 1: EPS 2.095 (p = 0.616), BVPS 0.219 (p = 0.908), R² = 0.948 | Ch4:211–215, Ch1:212, abstract | VERIFIED (text vs App E; Ch4 scope t-stats re-checked) |
| K-06 | Model 2: pre EPS 5.577 (p = 0.140), pre BVPS 0.100 (p = 0.940); δ_E −3.124 (p = 0.448), δ_B −1.758 (p = 0.175); post 2.453 (p = 0.298), −1.658 (p = 0.161) | Ch4:286–298, Ch1:212, abstract | VERIFIED (all four CIs now in text and matched to App E 4-dp limits; Ch4 scope) |
| K-07 | Joint Wald F(2,14) = 2.954, p = 0.085; HC3-specific | Ch4:303, Ch5:93, Ch1:181–182 | VERIFIED; estimator-dependence now disclosed in Ch1 Limitations (M06 fixed) |
| K-08 | R6: F(2,10) = 5.818, p = 0.021 unadjusted; Holm-adjusted p = 0.169 | Ch4:478–479, Ch5:97–102, Table 4.6 note, Table 5.1 | VERIFIED in prose and Table 4.6 note (M07) and Table 5.1 (M13); Table 4.7 note still lacks the Holm caveat (new issue V3-N16) |
| K-09 | No flight-to-book-value (post BVPS slope −1.658) | Ch4:625–627, Ch5 | VERIFIED as a non-finding |
| K-10 | Publication dates verified in only 2 of 30 bank-years | Ch1:148, 185–186, abstract:15, Ch5:180 | VERIFIED (now disclosed in abstract and Ch5) |
| K-11 | DPS–price correlation r = 0.082, p = 0.679 | Ch4:118, 133, 616; Ch5:191 | VERIFIED; now flagged in §4.3.2 (M08 partial — §4.3.3 still unflagged) |
| K-12 | Detectable effects at 80% power: 10.73 / 12.06 / 3.71 NPR | Ch3:367, Ch4:303, Ch5:108 | VERIFIED (stated identically in all three) |
| K-13 | Wild-cluster bootstrap p = 0.0625 (2/32) for Model 2 and R6 | Ch4:486, Ch5:132 | VERIFIED (s16 fixed) |
| K-14 | "No empirical study identified in the literature reviewed in Chapter II has formally evaluated whether the valuation coefficients shifted" | Ch1:30 | VERIFIED as scoped ("identified in the literature reviewed in Chapter II"); completeness beyond the reviewed corpus UNVERIFIED |
| K-15 | Five-day inclusion changes the joint test to F(2,16) = 4.762 (p = 0.024); stale-price Fs 3.870/3.821; interacted-DPS F = 2.85 | Ch4:476–488, Ch5 | UNVERIFIED from any table source (m44 remainder — text-only; needs new model runs) |
| K-16 | ROA SD change +97.49% | Ch4:71 note, :81 | UNVERIFIED from any printed value (m45 remainder — recomputation gives +100.00% from Table 4.1, +97.99% from App B) |

### 4.3 Traceability matrix (aims → RQs → hypotheses → results)

| Aim / RQ / Hypothesis | Tested / answered where | Status |
|---|---|---|
| General objective (Ch1:52) | Ch4 §4.2–§4.3, Ch5 §5.2–§5.3 | VERIFIED — answered (null result) |
| Specific objective 1 / RQ1 / H1, H2 | Model 1, Ch4:211–215; Table 5.1 | VERIFIED — tested, fail to reject |
| Specific objective 2 / RQ2 / H3, H4, joint | Model 2, Ch4:286–308; Table 5.1 | VERIFIED — tested, fail to reject (joint p = 0.085) |
| Specific objective 3 / RQ3 / R3–R9 | Ch4 §4.2.6–§4.2.7, App E | VERIFIED — RQ3 now names all seven variants including Kanchan (M02 fixed); R3–R9 reported |
| RQ3 → no hypothesis | Ch1:75 states it explicitly | VERIFIED (s05 fixed) |
| H1/H2 in Model 2 | Ch1:75 states re-examination; Ch5 reports both | VERIFIED (m07 fixed as corrected) |

### 4.4 Bookend check (abstract ↔ Chapter I ↔ Chapter V)

- **Headline figures agree across abstract, Ch1:212, Ch4, and Ch5** (Model 1 β_E 2.095 p = 0.616, β_B 0.219 p = 0.908, R² = 0.948; Model 2 pre-EPS 5.577 p = 0.140, pre-BVPS 0.100 p = 0.940, post 2.453 p = 0.298, −1.658 p = 0.161; joint F(2,14) = 2.954 p = 0.085; R6 F(2,10) = 5.82 p = 0.021, Holm-adjusted p = 0.169). VERIFIED by the front scope (hand-checked arithmetic: 5.577 + (−3.124) = 2.453; 0.100 + (−1.758) = −1.658) and by the coordinator's greps. No numeric disagreement was found anywhere.
- **Limitations agree across Ch1 and Ch5** (M10 fixed — both limbs restated at Ch5:180), with one trimming: the Ch5 restatement drops the "development banks, finance companies, or non-financial listed sectors" clause from the Ch1:173 boundary (new issue V3-N23).
- **RQ3 agrees across Ch1:46 and Ch5:33** (both now name the Kanchan exclusion). VERIFIED.
- **The abstract's claims are all present in the body** (FOM R-02): the 2-of-30 qualification, the Holm-adjusted p, and the estimator-specificity are all in Ch1/Ch4/Ch5. VERIFIED.

### 4.5 What was NOT reviewed in this section

Rendered output (no build); figure plotted contents (only `fig:value_relevance` was visually checked, by v2); the 30 annual reports; 14 of 26 tabulated studies' full texts (see §12).

---

## 5. Component-by-component review

### 5.1 Front matter — **Ready with minor revisions**

Order matches FOM 2019 exactly (verified against the criteria scope's own extraction); title identical in all four places; degree line MBS; date November 2026; 5 keywords (FOM maximum). Remaining items are supervisor-confirmation items (Research Committee labels, approval-sheet date rule, authorship "declare" vs FOM "corroborate", place line, Declaration page), submission-time blanks (all still blank, none invented), and build-dependent checks (abstract/acknowledgements one-page fit, TOC/LOT/LOF contents). LOT/LOF now single-spaced (m55 fixed). Abbreviations: 95 entries, no duplicates. (Front scope; criteria scope concurs.)

### 5.2 Chapter I — Introduction — **Needs major revision — on V2-M01 alone**

All other v2 Majors in scope are verified fixed; the Limitations section is now genuinely strong (eight bullets disclosing the scope boundary, attrition, finite-sample fragility, estimator-dependence, power/detectable effects and within-bank independence, non-causal interpretation, entity-timing mismatch, and the 2-of-30 publication-date limit). RQ3/Objective 3 traceability is now exact, item-for-item, including Kanchan. Every headline figure in the abstract is now verifiable from Chapter I alone. The remaining blocker is V2-M01 alone: the Prabhu–Century exclusion is still stated nowhere in Chapter I with a reason, and the reason can only be supplied by the author. That single finding still changes the sampling claim, so the chapter cannot be called submission-ready on content grounds; but the scale of remaining Chapter I work has narrowed from five substantive Majors in v2 to one unfixable-by-editing item. Three narrow defects remain in the loop's own moved paragraph at Ch1:212 (V3-N03–N05: R2–R9 mislabelled as "robustness specifications"; structurally orphaned placement; definitions after use). (Front scope; coordinator concurs — see §13.)

### 5.3 Chapter II — Literature Review — **Ready with minor revisions**

The literature chapter substantiates the flaws it alleges (P/E-circularity algebra shown; 19 of 26 tabulated studies flagged; Bhattarai's fiscal-year-end pricing verified against the source full text). Table 2.1 is now accurate against the audit's corrected counts (10 "not stated" flags; Pradhan 2003 correctly unflagged; Kwon flagged). The value-relevance definition is verbatim Barth et al. (2001, p. 79) with the Barth/Holthausen–Watts exchange present. Citations are clean (75/75, 0 orphans). Remaining: M12 is only partially fixed (the Ch2:407 lead clause still says the small-cluster gap is addressed "by implementing HC3"); one title-casing miss (Wilkinson); one uncited sentence (L300 Bhattarai); one loop-introduced label change (Almumani "DP" → "DPR"); m37 "168 obs" still unverified; s09 (NFRS 9 / competing explanations) still open. (Ch2 scope.)

### 5.4 Chapter III — Research Methodology — **Ready with minor revisions**

All assigned Chapter III fixes are present except the two deliberately untouched standing limitations (M01; the five-day rationale, m35, where no rationale was invented) and two partial fixes (m30 calendar citation; s10 exact versions). The two new Appendix D tables reproduce their sources exactly (m26 DPS dates 30/30 vs the announcement CSV; m27/m51 bonus ratios 30/30 vs dps.json and the bonusadj CSV). The methodology description is complete and internally consistent; Table 3.1 agrees cell-for-cell with Appendix A. Remaining defects are narrow: the DPS table's price-date column disagrees with Appendix A for the two excluded rows (V3-N11); "Restatements are exactly three" reads against Ch3's five balance-sheet restatements (V3-N12); Kanchan figures still lack a page locator (V3-N13). (Ch3 scope.)

### 5.5 Chapter IV — Results and Discussion — **Ready with minor revisions**

All three Majors in scope are addressed at least in their core defect (M07 and M09 fully; M08 in its §4.3.2 limb, with a residual in §4.3.3). All eight Model 1/2 t-statistics re-check against coef/SE; R3–R6 p-values match App E; R6 arithmetic (29.5%, critical value 4.103) checks; the covariance-sensitivity table reproduces Table 4.6; diagnostics are internally consistent. No new finding requires re-estimation, changes any hypothesis decision, or reverses any headline conclusion. Remaining work is narrow: Table 4.7 still stars R6 with no Holm caveat (V3-N16); Chapter IV never cites the new post-slopes table (V3-N17); two NPR differences don't reproduce from printed means (V3-N14); the ROA SD +97.49% is still not reproducible from any printed value (m45 remainder); the interacted-DPS and N=30/stale-price Fs still have no table source (m44 remainder). (Ch4 scope.)

### 5.6 Chapter V — Summary and Conclusion — **Ready with minor revisions**

The three assigned Majors are all fixed in the text (M02, M10, M13). Conclusions follow only from the findings; the hedging recorded by v2 is intact (e.g. Ch5:123 "Results are reported as associations across calendar periods, not as an established causal merger impact"; Ch5:191 flags the DPS non-result). Table 5.1's eight rows re-check against App E. What remains is one unpatched count wording (E-03/M01 Ch5 limb — the fifth combination still unmentioned), one trimmed limitations clause (V3-N23), and a missing pointer to Appendix B (V3-N22). (Ch5 scope.)

### 5.7 Appendices A–E — **Ready with minor revisions**

- **Appendix A:** unchanged in substance except the M11 caption move; its 30-cell price audit still agrees cell-for-cell with Chapter III Table 3.1 (re-checked programmatically by the Ch3 scope). (Ch3 scope.)
- **Appendix B:** prints 30 data rows with the two excluded rows flagged and footnoted. One new false sentence (V3-N20): the note claims the R7 bonus ratios "are not printed in this thesis" while Appendix D now prints them — a loop-introduced contradiction, one clause to fix. One pre-existing 0.01 rounding difference (V3-N21: BVPS post mean 161.97 vs 161.98 recomputed). (Ch5 scope.)
- **Appendix C:** now referenced from Chapter IV, correctly framed (eight plotted specifications, R3 omission explained), with notes on both figures. One residual nit: the appendix label `\ref{app:diagnostics_robustness}` is still never referenced in the body (the appendix is reachable by the textual mention and figure refs). (Ch5 scope.)
- **Appendix D:** register arithmetic re-checks exactly (5,663 pages; 328.31 MB); the two new tables match their sources 30/30; the sample log reconciles 30 → 28. (Ch3 scope.)
- **Appendix E:** the new post-slopes table reproduces its frozen source exactly (all six rows independently recomputed from `results.pkl` by the Ch5 scope reviewer, without importing the generator); R2 rows match the Model 2 note; R5/R6 values match `test_stats.py` and Ch4 prose; the R9 df correction (14→13) is in. Residual: the `tab:app_m1full` note still lacks EPS/BVPS expansion (V3-N24, residue of m49). (Ch5 scope.)

### 5.8 References — **Ready with minor revisions**

75 entries; 75 cited keys; 0 cited-but-missing; 0 uncited (re-run by the Ch2 scope reviewer). All 50 article titles verified sentence case except one miss (Wilkinson "Guiding Principles", V3-N06). The 16 changed book/techreport/misc titles are sentence case with proper nouns preserved; the 4 official titles are preserved as published. Braces 627/627 balanced. The Wilkinson 53-author list is correct. Two DOIs remain unverified (Holthausen — fetch failed, not retried; Bajracharya HEAD DOI — no confirming record found). (Ch2 scope.)

### 5.9 Compliance (criteria/compliance scope) — **Ready with minor revisions**

The institution's own rules govern (FOM 2019, verified rule-by-rule); the Essex proxy is verified verbatim as a yardstick only. All 11 figures caption-below; all 11 tables caption-above; front-matter order matches FOM p. 9; spacing/margins/font match FOM pp. 20–21 in source; pagination matches FOM p. 21 in source. New issues in this scope: the abstract word count (V3-N01) and the stale one-page-fit comment (V3-N02, merged with front N-05); the Kumari retitle is undocumented in the loop log (V3-N25). Rendered output cannot be determined without a build. (Criteria scope.)

### 5.10 What was NOT REVIEWED (component gaps)

- Figure plotted contents (only `fig:value_relevance` was visually checked, by v2; no figure was visually inspected in v3).
- Rendered output of any kind (no build): abstract/acknowledgements one-page fit, TOC/LOT/LOF contents and page numbers, rendered APA 6th formatting, longtable pagination, caption placement as rendered.
- Cited external sources for most cited facts (only m08/m36 were re-verified against repo-held reports by the Ch2 scope reviewer; m26/m27/m51 tables were verified against their repo source files by the Ch3 scope reviewer).
- The statistics themselves (v1's remit; data treated as correct).

---

## 6. Cross-cutting issues

### 6.1 The loop's patches introduced new defects (7 loop-introduced issues)

The v3 read found 29 distinct new issues (see §10); at least 7 were introduced by the loop's own patches:
- **V3-N03/N04/N05/N19 (front scope):** the moved results paragraph at Ch1:212 mislabels R2–R9 as "the eight robustness specifications", sits structurally orphaned after §1.7's closing matter, and defines R2–R9/Holm after first use; the inserted 2-of-30 clause in abstract:15 breaks the sentence's parallel structure.
- **V3-N08 (Ch2 scope):** Almumani's source variable "DP" was standardised to "DPR" in prose (Ch2:228) and Table 2.1 (Ch2:330) without noting the relabelling.
- **V3-N20 (Ch5 scope):** Appendix B:84 now falsely claims the R7 bonus ratios "are not printed in this thesis" while Appendix D (added by another loop scope) prints them — a cross-scope contradiction.
- **V3-N01 (criteria scope):** the abstract grew by ~23–30 words (not "~12" as the loop log states), pushing it to or over the Essex proxy 300-word cap.
None of these changes any claim or conclusion; all are narrow text fixes. But they are the reason the loop's "zero new issues" convergence claim does not hold up (see §13.3).

### 6.2 Partial fixes cluster in two patterns

- **The second limb was left:** M08 (§4.3.3 bullet), M12 (Ch2 lead clause), m49 (m1full note), m51 (App B sentence), m42 (Assessment cells), s15 (Ch1/Ch2/Ch4 limbs). In each case the loop fixed the finding's headline instance but left a second instance of the same defect elsewhere. The pattern suggests scope-by-scope patching without a final cross-chapter sweep for the same defect.
- **The fix needs a source the thesis does not hold:** m30 (calendar source for Chaitra-end dates), m35 (five-day rationale), s10 (exact installed software versions), m37 ("168 obs"), m44 remainder (interacted-DPS and N=30/stale-price Fs), m45 remainder (ROA SD +97.49%). These are not patchable by editing alone; they need an external source, a new model run, or the unrounded output.

### 6.3 The abstract is now longer and its fit comment is stale

The abstract grew by +23/+26/+29 words by the coordinator's hand-verified count (295/310/334 across three counting methods; HEAD 272/284/305), not "~12 words" as the loop log states. The in-file comment still asserts it "fits with about one line to spare" (abstract.tex:6–10) but was written about the pre-loop abstract. The one-page fit (FOM R-02) cannot be determined without a build. See V3-N01/V3-N02 (§10).

### 6.4 Estimator-dependence is now disclosed consistently — except in Table 4.7

The HC3-specificity of the headline non-rejection is now stated in the abstract, Ch1 Limitations (M06), Ch4 prose, Ch5, and the Table 4.6 note (M07) and Table 5.1 (M13). The one remaining place it is absent is the Table 4.7 note, which still stars R6 with only "* Significant at p < 0.05" (V3-N16). A reader who reads only Table 4.7 takes away an unqualified significant R6 result.

### 6.5 Unverifiable numbers cluster in Chapter IV's prose

Four groups of numbers in Chapter IV prose still have no table source anywhere in the thesis: the interacted-DPS F(2,12) = 2.85, the N = 30 F(2,16) = 4.762, the stale-price Fs 3.870/3.821 (and the N = 30 pre-period BVPS slope 0.709), and the ROA SD change +97.49%. They are repeated in Chapter V, which is repetition, not independent verification. Settling them needs new model runs or the unrounded analysis output (m44/m45 remainders).

### 6.6 The deliberately-untouched items are untouched — with two bib-title notes

The SEBON/MoF bullets (Ch3:160–161 — the task brief's ":158–159" was wrong; :158 is `\begin{itemize}`), Roll/Reg numbers, "Pokhara, Nepal", the R9 extension (not run), the Declaration absence, zero "ethic" matches, the four-section Ch5, the 17-word title, the place line, the spacing contradiction, the authorship wording, and the dotted-blank supervisor/chair names are all VERIFIED unchanged. Two notes: (a) the Kumari SGM bib title was reworded from "Minutes of the Special General Meeting, FY 2079/80" to a neutral descriptive title — the rewording honours the limitation but is undocumented in the loop log (V3-N25); (b) the Sharma DPS-sign conflict's referent cannot be located in the thesis — the prose (Ch2:228) and the synthesis row (Ch2:326) agree (DPS positive in both), so the limitation as worded cannot be tied to any specific textual inconsistency (UNVERIFIED).

---

## 7. What is correct and strong (verified)

1. **The Limitations section (Ch1:164–196)** now discloses estimator-dependence, power/detectable effects, within-bank independence, the scope boundary, attrition, non-causal interpretation, entity-timing mismatch, and the 2-of-30 publication-date limit — the v2 gaps are closed with figures that check out against Chapters IV–V.
2. **RQ3/Objective 3 traceability is now exact**, item-for-item, including the Kanchan exclusion in both Chapter I (Ch1:46) and the Chapter V restatement (Ch5:33).
3. **Every headline figure in the abstract is now verifiable from Chapter I alone**, and the implied-slope arithmetic checks out by hand (5.577 + (−3.124) = 2.453; 0.100 + (−1.758) = −1.658).
4. **The new Appendix D tables are exact:** the 30-row DPS announcement-dates table matches the announcement CSV 30/30 (all dates precede their price dates); the 30-value bonus-ratios table matches dps.json and the bonusadj CSV 30/30 (0 mismatches).
5. **The new Appendix E post-slopes table is exact:** all six rows independently recomputed from the frozen `results.pkl` by the Ch5 scope reviewer (without importing the generator); R2 rows match the Model 2 note; R5/R6 values match `test_stats.py` and Ch4 prose.
6. **Citation integrity is clean:** 75 bib entries / 75 cited keys / 0 orphans (re-run by the Ch2 scope reviewer); Table 2.1 counts reconcile (26 rows, 19 P/E flags, 15 both-EPS-and-BVPS studies).
7. **Chapter IV's numbers check out:** all eight Model 1/2 t-statistics, R3–R6 p-values vs App E, R6 arithmetic (29.5%, critical value 4.103), the covariance-sensitivity table, diagnostics (tolerance = 1/VIF for all six rows), and the leave-one-out p-range all reproduce.
8. **The criteria work is solid:** all 20 FOM rules verified page-by-page against the full extracted text; the "no rubric" claim verified by zero-hit search; the 25%/75% viva weighting verified; the Appendix A count corrected to 12 by hand count; the Essex proxy verified verbatim from the live regulations.
9. **Restraint where restraint was required:** no reason for the Prabhu–Century exclusion was invented anywhere (M01); the "168 obs" figure was not silently replaced or re-justified (m37); the SEBON/MoF bullets were left as the author decided; no supervisor or chairperson name was invented.

---

## 8. Follow-up on ALL v2 findings (85 rows)

One row per v2 finding: v2 ID, audit verdict, loop's claimed fix (short), this review's verification, evidence. Fix vocabulary: FIXED / PARTIALLY FIXED / NOT FIXED / FALSE FINDING. "By design" = deliberately left untouched per the author's accepted limitations or supervisor-confirmation items.

### 8.1 Majors (13)

| ID | Audit | Loop's claimed fix | v3 verification | Evidence |
|---|---|---|---|---|
| V2-M01 Prabhu exclusion, no reason | CONFIRMED | Deliberately untouched (standing limitation; inventing a reason forbidden) | **NOT FIXED (by design)** | "Prabhu" occurs exactly twice in the whole thesis (Ch1:30; Ch3:31, "is not sampled"); no reason stated anywhere. Coordinator re-ran the grep. |
| V2-M02 RQ3 narrower than Objective 3 | CORRECTED (narrow to Kanchan) | RQ3 reworded to name Kanchan | **FIXED** | Ch1:46 ends "…sensitivity analysis excluding the NMB FY 2076/77 bank-year with the Kanchan acquisition timing mismatch?"; Ch5:33 agrees. |
| V2-M03 Abstract figures absent from Ch1 | CORRECTED (gap wider: 5.577 also absent; abstract never prints 0.100) | Results paragraph moved to end of Ch1 carrying all figures | **FIXED** | Ch1:212 carries R² 0.948, pre-EPS 5.577, pre-BVPS 0.100, post 2.453/−1.658 with p-values; arithmetic hand-checked. |
| V2-M04 Headline results front-loaded into Background | CONFIRMED | Paragraph moved out of §1.1 to end of Ch1 | **FIXED** | Paragraph occurs once, at Ch1:212, after §1.7; §1.1 (lines 4–17) contains no results. Residual placement defects are new issues V3-N03/N04/N05 (§10). |
| V2-M05 Abstract overstates | CONFIRMED | "resolves"→"addresses"; 2-of-30 qualification; "without establishing…" | **FIXED** | "resolves" 0 hits thesis-wide; abstract:15 "addresses … although actual publication dates were verified in only 2 of 30 bank-years"; abstract:17 "without establishing whether book-value substitution occurred". |
| V2-M06 Ch1 Limitations omit estimator-dependence | CORRECTED (Ch5 location is :93) | New Limitations bullet (Ch1:181) | **FIXED** | Ch1:181–182 "Estimator Dependence of the Headline Non-Rejection" states the HC3-specificity and the classical/HC0/HC1/HC2 reversal for all eight joint tests, citing `tab:cov_sensitivity` (exists at Ch4:442); agrees with Ch4:392 and Ch5:93. |
| V2-M07 Table 4.6 stars R6, no Holm note | CONFIRMED | Holm caveat added to Table 4.6 note | **FIXED** | Ch4:434 "R6 is significant only at the unadjusted 5% level; Holm-adjusted p = 0.169"; R6 star still present at Ch4:420. (Table 4.7 still lacks it — new issue V3-N16.) |
| V2-M08 Dividend-cessation mechanism contradicts DPS–price r = 0.082 | CONFIRMED | §4.3.2 bullet reframed as hypothesis with r = 0.082 | **PARTIALLY FIXED** | §4.3.2 bullet now flags r = 0.082, p = 0.679 (Ch4:616). But the §4.3.3 signalling bullet (Ch4:634–635) still presents the mechanism with no caveat — verified by the coordinator. |
| V2-M09 Model 2 CI promise unkept in text | CONFIRMED | Four Model 2 CIs printed in text at 3 dp | **FIXED** | Ch4:292–298: δ_E [−11.710, 5.462], δ_B [−4.398, 0.882], post-EPS [−2.412, 7.319], post-BVPS [−4.059, 0.744] — each matches App E 4-dp limits rounded to 3 dp. |
| V2-M10 No limitations restatement in Ch5 | CONFIRMED | Restatement added (Ch5:180) | **FIXED** | Ch5:180 restates both limbs (generalizability boundary; 2-of-30 limit). Trimming noted as new issue V3-N23 (three excluded sectors dropped). |
| V2-M11 Figure captions above figures | CORRECTED (11 figures, not 8) | All 11 caption-below; preamble `position=below` | **FIXED** | Criteria scope verified each of the 11 environments line by line (graphic line precedes caption line in all 11); `config/preamble.tex:74` sets `position=below`; `\thesisfigure` macro still unused. |
| V2-M12 HC3 presented as the small-cluster answer | CONFIRMED | Reworded Ch1:39 and Ch2:407 | **PARTIALLY FIXED** | Ch1 limb FIXED (Ch1:39 now says HC3 "addresses heteroskedasticity rather than within-bank correlation"). Ch2 limb partial: Ch2:407 adds the qualification sentence, but the lead clause still says the gap is addressed "by implementing MacKinnon-White HC3". |
| V2-M13 Table 5.1 opposite decisions for same joint null | CONFIRMED | R6 cell "Sensitivity only — no decision (Holm-adjusted p = 0.169)" | **FIXED** | Ch5:160 reads exactly that, below the baseline row at :158–159 ("Fail to Reject H₀"); prose at :177 still resolves it; no "Reject H₀" remains for the joint null in the table. |

### 8.2 Minors (52)

| ID | Audit | Loop's claimed fix | v3 verification | Evidence |
|---|---|---|---|---|
| V2-m01 Research Committee labels | CONFIRMED | Not patched (supervisor) | **NOT FIXED (by design)** | `research_committee.tex:28, 32` still bare dotted rules with role names only. |
| V2-m02 DP/DYR duplicates | CONFIRMED | DP/DYR rows removed; body standardised | **FIXED** | `abbreviations.tex` DPR :50, DY :52; 95 rows; no DP/DYR hits thesis-wide. |
| V2-m03 Acknowledgements name neither supervisor nor chair | CORRECTED (lines 16/18) | Not patched (names unknown) | **NOT FIXED (by design)** | `acknowledgements.tex:16, 18` still name neither. |
| V2-m04 Power/within-bank bullet missing | CONFIRMED | New Limitations bullet (Ch1:184) | **FIXED** | Ch1:184–185 gives detectable effects 10.73/12.06/3.71 NPR and states within-bank independence untested; agrees with Ch5:108 and Ch5:66. |
| V2-m05 HC3 undefined on first use; R2–R9/Holm undefined | CONFIRMED | HC3 expanded; R2–R9/Holm defined in moved paragraph | **FIXED** | First HC3 at Ch1:39 expanded; Ch1:212 defines R2–R9 and Holm (ordering defect is new issue V3-N05). |
| V2-m06 "Five" ambiguous (sample vs combinations) | CONFIRMED | "five" qualified; Ch1:173 rewritten | **FIXED** | Ch1:17 "five sampled commercial bank series"; Ch1:173 "four merged series … alongside an unmerged benchmark". |
| V2-m07 H1/H2 model ambiguity | CORRECTED (inverted defect) | Hypotheses intro states Model 2 re-examination | **FIXED (as corrected)** | Ch1:75 states H1/H2 are stated for Model 1 and re-examined in Model 2; Ch5 reports both evaluations. |
| V2-m08 NMB–Kanchan figures uncited | CONFIRMED | New `nmb2021report` bib; `\citep` added | **FIXED** | Cited at Ch1:15, Ch2:211, Ch3:80; entry at `references.bib:326`; Ch2 scope re-verified all four figures against the repo-held NMB FY 2077/78 report (23 Aug 2020; NPR 496,765,500; swap 1:0.85; 13% bonus). |
| V2-m09 "(in the 2023 wave)" parenthetical | CONFIRMED | Parenthetical removed; Ch1:173 rewritten | **FIXED** | "(in the 2023 wave)" 0 hits in Ch1. |
| V2-m10 Footnote repeats author names | CONFIRMED | Hand-typed names removed, `\citet` kept | **FIXED** | Ch2:275 footnote now reads `\citet{gurungdahal2025}` … `\citet{dahal2025}`; doubling gone. |
| V2-m11 Redundant parenthetical citation + repeated sentence | CONFIRMED | Redundant `\citep` removed; repetition removed | **PARTIALLY FIXED** | Redundancy and repetition gone, but Ch2:300 "Bhattarai (2014) measures equity share prices…" is now plain text with no `\citet` at all (new issue V3-N07). |
| V2-m12 Ohlson 1995 DOI omitted | CONFIRMED | DOI added | **FIXED** | `references.bib` `ohlson1995` carries `doi = {10.1111/j.1911-3846.1995.tb00461.x}`. |
| V2-m13 Article-title capitalisation inconsistent | CONFIRMED | 40 article + 16 book/techreport/misc titles sentence-cased; 4 official titles preserved; braces 627/627 | **PARTIALLY FIXED** | All titles verified individually by the Ch2 scope reviewer; one miss remains — `wilkinson2016fair` still "The {FAIR} Guiding Principles…" (new issue V3-N06). |
| V2-m14 Wilkinson "and others" | CONFIRMED | Full 53-author list | **FIXED** | 53 authors counted by script; first six and last (Mons, Barend) as claimed; "and others" 0 hits. |
| V2-m15 Collins "empirical panel" | CONFIRMED | Reworded to "sequence of annual cross-sectional regressions" | **FIXED** | Ch2:117 new wording; "forty-one-year empirical panel" 0 hits. |
| V2-m16 2011 Merger Bylaws cited for 2022–23 forbearance | CONFIRMED | `nrb2011` removed from that citation | **FIXED** | Ch2:202 cites `\citep{tht2023nrbmerger}` only; `nrb2011` still cited at the 2011 bullet. |
| V2-m17 Table 2.1 rows give no sample size | CORRECTED (10 lack obs count; 4 lack any size; Pradhan wrongly listed; Kwon omitted) | Flags added per corrected counts | **FIXED** | "not stated in the reviewed source" occurs 10× in Table 2.1, exactly the audit's list; Pradhan 2003 keeps "29 companies, 93 obs"; Kwon flagged. |
| V2-m18 Table 2.1 variables the prose never mentions | CONFIRMED | Every flagged variable mentioned in prose | **FIXED (thesis-internal; source accuracy partly UNVERIFIED)** | All six prose additions present (Sharma L228, Almumani L228, Bajracharya L241, Niroula L250, Gyawali L252, Gurung & Subedi L262). Source accuracy not re-verified for five of the six (sources not opened); Almumani checked — label issue is new issue V3-N08. |
| V2-m19 No formal "value relevance" definition; Barth/Holthausen–Watts absent | CONFIRMED | Definition + paragraph added; new entries `barth2001`, `holthausen2001` | **FIXED** | Ch2:105–107 definition is verbatim Barth et al. (2001, p. 79), confirmed against the published text by the Ch2 scope reviewer; both entries present, cited, bibliographically correct (Holthausen DOI direct resolution UNVERIFIED — fetch failed). |
| V2-m24 R5/R6 residual df = 10 underivable from Ch3 | CONFIRMED | Ch3 R6 bullet now derives df = 10 | **FIXED** | Ch3:380 "the parameter count falls from K = 14 to K = 13 and residual degrees of freedom are 23 − 13 = 10"; App D §D.6 agrees. |
| V2-m25 ROA "average total assets" undefined in Ch3 | CORRECTED (App D line is 246) | Ch3 ROA definition states the averaging | **FIXED** | Ch3:258 "Average total assets is the mean of the current and previous fiscal year-end total assets"; matches App D:246 codebook row. |
| V2-m26 DPS announcement dates asserted but never printed | CONFIRMED | New 30-row DPS dates table in App D (from the announcement CSV) | **FIXED** | App D `tab:app_dps_dates` (:295): all 30 announcement dates and all 30 price dates match the CSV exactly; all 30 precede their price dates. NIMB FY 2077/78 corrected declaration 2021-10-20 confirmed via the CSV note and dps.json. |
| V2-m27 Bonus-ratio source and units unstated | CORRECTED (cited line 248 is the DPS row) | Source + units stated in Ch3, App D codebook, App D §D.6; new bonus-ratios table | **FIXED** | Ch3:381, App D:250, App D:403 state source and units; table values verified 30/30 vs dps.json and the bonusadj CSV (0 mismatches). |
| V2-m28 Five balance-sheet restatements have amounts but no locators | CONFIRMED | Each restatement now carries its SOFP locator | **FIXED** | All five locators at Ch3:171 checked against App D Table D.2 and agree. |
| V2-m29 Contextual sources listed but never cited/used | CORRECTED ("never cited" false for Merger Bylaws and NRB stats) | NRB bullet reworded; BSD circulars removed; SEBON/MoF bullets untouched | **FIXED (corrected scope)** | Ch3:159 NRB bullet now ties each item to its actual use; "Bank Supervision Department" 0 hits in Ch3; SEBON/MoF bullets at Ch3:160–161 byte-identical to v2 (untouched, as required). |
| V2-m30 Five-day window has no stated rationale — disclosed, not hidden | CONFIRMED | Deadline sentence reworded to state it checks gap arithmetic only | **PARTIALLY FIXED** | App D:182 now disclaims independent verification (circularity cured). But no calendar source for the Chaitra-end dates is cited anywhere in App D. |
| V2-m31 Full-design VIFs not reported in Ch3 | CONFIRMED | Full-design VIFs added at Ch3:364 | **FIXED** | Ch3:364 values match Ch4:540 (Table 4.8 note) verbatim, including the largest year-dummy VIF 118.21. |
| V2-m32 Register size 328.30 MB | CONFIRMED | 328.30 → 328.31 MB | **FIXED** | App D:10 "328.31 MB and 5,663 pages"; recomputed exactly from the register rows. |
| V2-m33 AEA-invocation sentence | CORRECTED (AEA sentence is App D:4) | AEA sentence tightened; no code deposited | **FIXED** | App D:4 "modelled on that standard as an aspiration for documentation structure only and is not a claim of compliance with it; in particular, no analysis code is shared (Section D.8)." |
| V2-m34 Table 3.1 note misdescribes Merolagani as a retrieval source | CONFIRMED | Table 3.1 note reworded | **FIXED** | Ch3:126 now reads "from the ShareSansar series via the nepse-data dataset (the dataset close), cross-checked against Merolagani last traded prices…". |
| V2-m35 Five-day window: no rationale, no sensitivity | CONFIRMED | Consequence sentence added; no rationale invented | **PARTIALLY FIXED** | Ch3:93 now states the consequence (including the two delayed observations changes the joint test to F(2,16) = 4.762, p = 0.024). No rationale and no window-sensitivity analysis added. |
| V2-m36 HBL/NIMB swap ratios unverified | UNVERIFIED (v2) | Closed by verification, no patch | **FIXED (verified correct; no patch needed)** | Ch2 scope re-verified both ratios against the repo-held FY 2079/80 reports (HBL 100:80.28; NIMB 100:90). |
| V2-m37 Pradhan & Dahal "168 obs" unconfirmed | UNVERIFIED (v2) | Not patchable — left unverified for the author | **NOT FIXED (deliberately; standing item)** | "168 obs" still at Ch2:338; arithmetically consistent (14 × 12) but unconfirmed; no invented number substituted. |
| V2-m38 Unlisted 20th bank unnamed | CONFIRMED | Unlisted bank named | **FIXED** | Ch3:28 "the one unlisted institution is Rastriya Banijya Bank Limited". (The "19 listed" count itself remains UNVERIFIED — sources not opened.) |
| V2-m39 R7 one-sided implication not flagged | CORRECTED (flagged at Ch4:480; only unflagged in Ch3/App D) | One-sided flag added in Ch3 and App D §D.6 | **FIXED** | Ch3:381 and App D:403 both carry the flag in Ch4's wording. |
| V2-m40 Overstatement sentences (Ch4 framing) | CONFIRMED | Both sentences reworded | **FIXED** | Old phrasings 0 hits in Ch4; Ch4:283 and :609 reworded. |
| V2-m41 Hypothesis table directional language | CONFIRMED | All six Inference cells standardised | **FIXED** | All six rows now read "Insignificant under t(df)"; joint row keeps "Marginal at 10%; fails 5% threshold" (different decision, justified). |
| V2-m42 "Below screen" with VIF threshold only in Ch3 | CONFIRMED | Threshold added to Table 4.8 note | **PARTIALLY FIXED** | Threshold now in the Table 4.8 note (Ch4:539–540: "The screening threshold is VIF > 5"). Assessment cells still read bare "Below screen" (:520–521). |
| V2-m43 EPS–DPS / ROA–DPS correlations never interpreted; W statistics only in App E (false) | CORRECTED (W also at Ch3:364, Ch4:548) | New "Dividend Associations" bullet; Table 4.2 note extended | **FIXED** | Ch4:136 interprets both correlations (r = 0.612, 0.595, p < 0.01); Table 4.2 note (:127) gives the W locations (verified: Ch3:364, Ch4:548, App E:534). |
| V2-m44 Open questions needing unrounded output | CORRECTED (FE-only F 2.23 and 93.9% derivable from printed Table 4.9) | Derivations added; new App E post-slopes table; remainder needs new model runs | **PARTIALLY FIXED** | FE limbs: derivations in text, arithmetic re-run ✓ (F = 2.23; 93.9%). R5/R6 slopes: in App E `tab:app_postslopes`, all 8 values match Ch4 exactly — but Ch4 never cites that table (new issue V3-N17). Remainder NOT fixed: interacted-DPS F 2.85, N = 30 F 4.762, stale-price Fs 3.870/3.821, N = 30 BVPS 0.709 — text-only, no table source. |
| V2-m45 Descriptive percentage changes not reproducible | CORRECTED (three of four are rounding artefacts; only ROA SD unexplained) | Table 4.1 note discloses unrounded computation | **PARTIALLY FIXED** | Disclosure is in the note (Ch4:71). ROA SD +97.49% is still not reproducible from any printed value (+100.00% from Table 4.1; +97.99% from App B; unrounded SDs printed nowhere). |
| V2-m46 "establish" overstatement (Ch4) | CONFIRMED | "establish" → "report" | **PARTIALLY FIXED** | "These studies establish" 0 hits. But the sentence (Ch4:658–659) still carries no P/E caveat itself (the circularity is discussed earlier at :645). |
| V2-m47 "forced" / "widening standard errors" | CONFIRMED | "forced" → "coincided with"; "widening standard errors" removed | **FIXED** | Both wordings 0 hits in Ch4. |
| V2-m48 Two renderings of MPS^RD | CONFIRMED | 10 bare `$MPS^{RD}$` → `$\mathit{MPS}^{RD}$` | **FIXED** | Coordinator re-ran the grep: 0 bare occurrences thesis-wide now. (The loop's "10" was only the cross-file part; the true HEAD total was 14 including Appendix B's 4; now 0 bare, 72 mathit.) |
| V2-m49 Table-note abbreviation expansion missing | CONFIRMED | Expansion sentences added to two App E note strings; regenerated | **PARTIALLY FIXED** | Robustness sentence appears once (App E:176); Model 2 sentence appears twice (:105, :207) — not "exactly once" as the loop claimed; `tab:app_m1full` note (:59) still lacks EPS/BVPS expansion (new issue V3-N24). |
| V2-m50 Four-section Ch5 vs Guidelines' three sections | CONFIRMED | Disclosed deviation, supervisor confirmation, NOT a patch | **NOT FIXED (correctly)** | Ch5:6 still discloses the deviation; all three required sections present; no silent "fix" applied. |
| V2-m51 Appendix B not self-contained for R7/R8 inputs | CONFIRMED (audit: R7 inputs absent, not merely unverified) | R8 values pointed to App D §D.4; R7 ratios cross-referenced | **PARTIALLY FIXED** | R8 pointer checks out (values at App D:263). R7 definition pointer checks out (App D §D.6). BUT the App B sentence now asserts the bonus ratios "are not printed in this thesis" (App B:84) while App D prints them (Table `tab:app_bonus_ratios`, :271–288) — verified by the coordinator. One limb is now incorrectly stated (new issue V3-N20). |
| V2-m52 Appendix C unreferenced, overstates coverage, figures carry no notes | CORRECTED (coverage sentences are App C lines 4 and 6) | Coverage corrected; notes added; body pointer added | **FIXED** | App C:4 now says "eight plotted EPS-channel specifications (R1, R2, and R4 through R9); R3 is omitted because ROA is on a different scale"; notes at :15 and :28; body pointer at Ch4:508. Residual nit: the appendix label itself is still never `\ref`'d in the body. |
| V2-m53 Title length (17 words vs 12 suggested) | CONFIRMED | Not patched (supervisor item) | **NOT FIXED** | Title still 17 words (criteria scope re-counted); FOM p. 8 suggestion in the proposal passage. |
| V2-m54 `\parskip` in abstract/acknowledgements vs global 10 pt | CORRECTED (abstract:14 / ack:13) | Not patched (build-dependent) | **NOT FIXED (by design)** | `\parskip` 3 pt still at abstract.tex:14 and acknowledgements.tex:13. |
| V2-m55 LOT/LOF at 1.5 spacing vs single-spaced TOC | CORRECTED (citation `main.tex:48, 55–59`) | LOT/LOF set single-spaced | **FIXED** | `main.tex:56, 59` call `\thesisFrontList` with no spacing argument; default stretch is 1 (`config/preamble.tex:277`). |
| V2-m56 Appendix entries hidden from TOC | CONFIRMED (UNVERIFIED whether compliant) | Not patchable (loop record) | **NOT FIXED** | `main.tex:118–119` byte-identical to HEAD; compliance remains UNVERIFIED (FOM does not specify appendix TOC treatment; rendered TOC not seen). |

### 8.3 Suggestions (20)

| ID | Audit | Loop's claimed fix | v3 verification | Evidence |
|---|---|---|---|---|
| V2-s01 Approval-sheet date rule added | CONFIRMED | Not patched (supervisor) | **NOT FIXED (by design)** | `approval_sheet.tex:40` still has the added date rule. |
| V2-s02 Authorship "declare" vs FOM "corroborate" | CONFIRMED | Not patched (supervisor) | **NOT FIXED (by design)** | `authorship.tex:9` still reads "declare". |
| V2-s03 Title-page place line "Pokhara, Nepal" | CONFIRMED | Not patched (supervisor/campus) | **NOT FIXED (by design)** | `titlepage.tex:27–28` still carries the place line; FOM template shows none. |
| V2-s04 Abstract one-page fit | CONFIRMED | Not patched (build check) | **NOT FIXED (by design)** | Rendered fit CANNOT DETERMINE without a build; the in-file comment is now stale (new issue V3-N02). |
| V2-s05 RQ3 has no corresponding hypothesis | CONFIRMED | Stated explicitly (Ch1:75) | **FIXED** | Ch1:75 "Research Question 3 has no corresponding hypothesis; it is answered by the robustness suite R3–R9 (Chapter IV), not by a hypothesis test." |
| V2-s06 "Organization of the Study" extra section, no justification | CONFIRMED | Justification sentence added (Ch1:200) | **FIXED** | Ch1:200 "The Organization of the Study section is included to orient the reader to the five-chapter structure of the dissertation:" — verified by the coordinator. (Reconciliation note: the Ch5 scope reviewer recorded this as PARTIALLY FIXED on the ground that supervisor confirmation of the FOM justification route remains open. The coordinator governs: the finding asked for a justification to be stated, and one is stated; the supervisor-confirmation route is a separate open item, recorded in §11. No supervisor-advice claim is made in the text, correctly.) |
| V2-s07 20-licensed vs 19-listed gap unexplained | CORRECTED (false premise) | Closed as a false finding; no patch | **FALSE FINDING — correctly closed** | Ch3:26 "Of these 20 licensed institutions, 19 are listed on NEPSE; the one unlisted institution is Rastriya Banijya Bank Limited." |
| V2-s08 Language and clarity (Ch1) | CONFIRMED | Patched in part | **PARTIALLY FIXED** | "ensures" fixed; British spellings standardised; two paragraph splits done. "mathematically closed" (Ch1:7) and the evaluative adjectives (Ch1:11) untouched (readability-only). |
| V2-s09 Alternative perspectives thin (NFRS 9, scale, conservatism) | CONFIRMED | Not patched (author input) | **NOT FIXED** | "NFRS 9" occurs once in Ch2 (L112, harmonisation task only); "scale effect", "conservatism", "omitted" (omitted-variables sense): 0 hits. |
| V2-s10 Software versions not recorded | CONFIRMED | Versions added in Ch3 §3.6.6 and App D §D.6 | **PARTIALLY FIXED** | Versions now stated and agree with `requirements.txt`; but only statsmodels is exact, the rest are minimums, pytest is omitted, and no installed-version record exists (no lockfile). |
| V2-s11 No ethics statement anywhere | CONFIRMED | One-sentence ethics statement (Ch3:23) | **FIXED** | Ch3:23 "This study uses only published secondary data (audited annual reports and public price series); no human participants were involved." (COI/funding/AI statements were not added; those are supervisor items, not part of this finding.) |
| V2-s12 "Prominent" sampling criterion not operationalized | CONFIRMED | "Prominent" removed from Ch3 | **FIXED** | "prominent" 0 hits in Ch3/App A/App D. (Still used in Ch1:13/30 and Ch5 — new issue V3-N27.) |
| V2-s13 No detectable-effect / power statement in Ch4 | CONFIRMED | Sentence added to joint-Wald bullet | **FIXED** | Ch4:303 states all three figures (10.73/12.06/3.71 NPR at 80% power), matching Ch3:367 and Ch5:108. |
| V2-s14 Figure file names non-sequential | CONFIRMED | No change (cosmetic) | **NOT FIXED (intentional; cosmetic)** | Files still F6, F1, F2, F3, F4, A2, F5 in presentation order; compiled numbering unaffected. |
| V2-s15 Abbreviations first appear unexpanded | CONFIRMED | Ch5 limbs fixed (ICAN, ESG); Ch4 limb not patched | **PARTIALLY FIXED** | Ch5 limbs FIXED (ICAN Ch5:201; ESG Ch5:244–245). Ch4 limb NOT FIXED (OLS first use unexpanded at Ch4:16; NPR unexpanded throughout). Ch1/Ch2 limbs NOT FIXED — verified by the coordinator: OLS first appears unexpanded at Ch1:30 ("pooled OLS"); VIF first appears unexpanded at Ch1:206; NFRS first appears unexpanded at Ch2:112 ("under NFRS 9 / IFRS 9"). |
| V2-s16 Bootstrap p reported as 0.062; exact fraction 2/32 = 0.0625 | CONFIRMED | Both Ch4 bootstrap p-values 0.062 → 0.0625 | **FIXED** | Ch4:486 and Ch5:132 both now read 0.0625 with the exact fraction stated. |
| V2-s17 Causal verb "exerts" in H2 conclusion sentence | CONFIRMED | Ch5 wording changed | **FIXED** | "exerts" 0 hits in Ch5; Ch5:174 "Book value per share shows no statistically significant incremental pricing effect in the baseline specification." |
| V2-s18 Separate Declaration page | CONFIRMED | Not patched (supervisor) | **NOT FIXED (by design)** | No Declaration input in `main.tex`; FOM p. 9 does not require one. |
| V2-s19 Front-matter blanks completion checklist | CONFIRMED | Not patched (submission-time) | **NOT FIXED (by design)** | All signature/name/date fields still blank placeholders. |
| V2-s20 FOM spacing-list contradiction | CONFIRMED | Not patched (guideline problem) | **NOT FIXED (guideline problem, not thesis problem)** | FOM p. 20 contradicts itself; no supervisor note in the thesis confirming which list it follows. |

### 8.4 Follow-up tally

| | FIXED | PARTIALLY FIXED | NOT FIXED | FALSE FINDING | Total |
|---|---|---|---|---|---|
| Majors | 10 | 2 | 1 | 0 | 13 |
| Minors | 35 | 10 | 7 | 0 | 52 |
| Suggestions | 7 | 3 | 9 | 1 | 20 |
| **Total** | **52** | **15** | **17** | **1** | **85** |

Reading of the tally: 52 of 85 findings are fully fixed; 15 are partially fixed (all Narrow residues — a second instance of the same defect, or a limb needing a source the thesis does not hold); 17 are not fixed, of which 13 are deliberately untouched by design (standing limitations, supervisor-confirmation items, submission-time blanks, build-dependent checks, or intentionally cosmetic), 2 are open author items (m37 "168 obs"; s09 alternative perspectives), 1 is an open suggestion left intentionally (s14 figure file names), and 1 is the standing limitation M01. One finding (s07) was a false finding, correctly closed with no patch. **No finding was incorrectly fixed as a whole** — the single incorrectly-stated limb (m51's App B sentence, now false) is recorded under m51 as PARTIALLY FIXED with the new issue V3-N20, not as a whole-finding incorrect fix.

---

## 9. Examiner's likely questions

(Adapted from v2 §9, updated for the v3 state. Questions the thesis can now answer are marked ANSWERED; questions that remain open are marked OPEN.)

| # | Likely question | Status | Where the answer now sits (or why it is still open) |
|---|---|---|---|
| Q1 | Why is Prabhu–Century, the fifth 2023 combination, excluded from the sample? | **OPEN** | No reason is stated anywhere in the thesis (V2-M01). The thesis states only the fact of non-sampling (Ch3:31). This is the single most likely examiner question and the thesis has no answer to it. |
| Q2 | Is the headline non-rejection robust to the covariance estimator? | **ANSWERED** | Yes, honestly answered: the abstract, Ch1 Limitations (new bullet), Ch4, Ch5, Table 4.6 note, and Table 5.1 all state the result is HC3-specific and that all eight joint tests reject under classical/HC0/HC1/HC2. (Table 4.7's note still lacks the caveat — V3-N16.) |
| Q3 | Why does R6 reject when the baseline does not? | **ANSWERED** | Ch4:478–479 and Ch5:97–102 fence R6 as a sensitivity finding (unadjusted p = 0.021; Holm-adjusted p = 0.169; leave-one-bank collapse F = 0.615–1.309). Table 5.1 no longer gives a "Reject" decision for it. |
| Q4 | What exactly is the contribution — an empirical finding or a methodological protocol? | **PARTLY ANSWERED** | The abstract now qualifies the protocol leg (2-of-30 verification) and no longer claims to "resolve" the limitations. But Ch1 still claims both legs without ranking them, and the empirical leg is null. An examiner may still press on what the thesis contributes. |
| Q5 | Do the conclusions travel beyond the five series? | **ANSWERED** | Ch1:173 states the boundary; Ch5:180 now restates it (with the three excluded sectors trimmed — V3-N23). |
| Q6 | Why is RQ3 narrower than Objective 3? | **ANSWERED** | It is no longer narrower: RQ3 (Ch1:46) and the Ch5 restatement (Ch5:33) now name the Kanchan exclusion. |
| Q7 | Does Chapter II substantiate the prior flaws (P/E circularity, Ashadh-end pricing)? | **ANSWERED** | Yes, in substance (verified in v2 and unchanged): the P/E-circularity algebra is shown; 19 of 26 tabulated studies are flagged; Bhattarai's fiscal-year-end pricing was verified against the source full text. |
| Q8 | Why is the five-day freshness window five days? | **OPEN** | Ch3:93 now states the consequence (including the two delayed observations changes the joint test to F(2,16) = 4.762, p = 0.024) but no rationale for five days rather than another window is stated, and no window-sensitivity analysis was added (m35 partial). |
| Q9 | What calendar source fixes the Chaitra-end reporting deadlines? | **OPEN** | App D:182 now states the deadline check is gap arithmetic only, not independent verification; no calendar source is cited (m30 partial). |
| Q10 | Where do the interacted-DPS F (2.85), the N = 30 F (4.762), and the stale-price Fs (3.870/3.821) come from? | **OPEN** | They appear only in Chapter IV prose (and repeated in Ch5); no table source exists in the thesis (m44 remainder). An examiner who asks for the table will not find one. |
| Q11 | How is the ROA standard-deviation change (+97.49%) computed? | **OPEN** | The Table 4.1 note discloses unrounded computation, but the unrounded SDs are printed nowhere; recomputation from printed values gives +100.00% (Table 4.1) or +97.99% (App B) (m45 remainder). |
| Q12 | What is the exact title of the Kumari SGM document, and why does the bibliography give a descriptive title? | **OPEN** | The bib title is now a neutral descriptive title (no exact title asserted), which honours the limitation — but the exact title still needs the author to open the PDF once. |
| Q13 | Is the "168 obs" for Pradhan & Dahal (2016) correct? | **OPEN** | Still at Ch2:338, arithmetically consistent (14 × 12) but unconfirmed against the source (m37). |
| Q14 | Does Almumani (2014) cover 7 banks / 49 observations? | **OPEN** | A secondary source asserts it; v2 (which opened the full text) records the bank count as not stated; the thesis keeps the "not stated" flag. Unresolved. |
| Q15 | Why do the two excluded rows show a price date in the App D DPS table but none in Appendix A? | **OPEN (new)** | App D's DPS table shows the target deadline (2022-04-13) for HBL/NIMB FY 2077/78 while Appendix A shows the actual resumption dates (2022-06-06 / 2022-05-30). The eligibility claim holds under either date, but the same column label means two different things (V3-N11). |
| Q16 | Why does Appendix B say the R7 bonus ratios "are not printed in this thesis" when Appendix D prints them? | **OPEN (new)** | A loop-introduced contradiction (V3-N20). One clause fixes it, but an examiner who spots it will ask. |

---

## 10. Findings summary table (new issues found in this review)

Twenty-nine distinct new issues (0 Critical, 0 Major, 19 Minor, 10 Suggestion). The six scope reviews reported 31 Part B items; two were duplicates (Ch2 N5 = the M01 Ch2 instance, already counted in §8; criteria N2 = front N-05, the same stale comment), giving 29. Four of the twenty-nine are the residual limbs of PARTIALLY FIXED v2 findings (V3-N07 = m11; V3-N29 = M08; V3-N20 = m51; V3-N24 = m49); they are listed here so the fix list is complete, and cross-referenced to §8. One further language inconsistency (the "behaviour" 7× vs "behavior" 1× spelling split, criteria scope §4.2) is recorded in §15 as a language item rather than numbered here.

| ID | Finding | Location | Severity / Scale | Status |
|---|---|---|---|---|
| V3-N01 | Abstract word count: 295 (maths removed) / 310 (maths = 1 token) / 334 (maths as words) by the coordinator's hand-verified count; HEAD 272/284/305; growth +23/+26/+29 words, not "~12" as the loop log states. Exceeds the Essex proxy 300-word cap under the one-token and keep methods; just under (295) under the strictest maths-removed method. (The criteria scope counted 316/331; its para-2 count of 167 does not reproduce the coordinator's hand count of 149 for that paragraph — see §12.) v2's 206/217 is wrong under every method. FOM sets no word limit, so no FOM breach. | `front/abstract.tex:15, 17` | Minor / Narrow | VERIFIED (coordinator's hand count) |
| V3-N02 | The in-file one-page-fit comment ("fits with about one line to spare", abstract.tex:6–10) now predates the lengthened abstract; rendered fit CANNOT DETERMINE without a build. | `front/abstract.tex:6–10` | Minor / Narrow | VERIFIED |
| V3-N03 | The moved results paragraph mislabels R2–R9 as "the eight robustness specifications", while its own parenthetical says R1–R2 are baselines. R2 is a baseline joint test; the robustness variants are R3–R9 only. Introduced by the loop's patch. | `chapter_01_introduction.tex:212` | Minor / Narrow | VERIFIED |
| V3-N04 | The moved results paragraph is structurally orphaned: the chapter's final paragraph, outside any section, after §1.7's closing References/Appendices paragraph (line 210). | `chapter_01_introduction.tex:212` | Minor / Narrow | VERIFIED |
| V3-N05 | R2–R9 and Holm are defined in the last sentence of Ch1:212, after first use in the same paragraph. | `chapter_01_introduction.tex:212` | Minor / Narrow | VERIFIED |
| V3-N06 | Wilkinson (2016) article title still in Title Case after the m13 sentence-casing pass: "The {FAIR} Guiding Principles for scientific data management and stewardship" — "Guiding Principles" should be lowercase. The only remaining article-title casing defect. | `src/thesis/references.bib` (`wilkinson2016fair`) | Minor / Narrow | VERIFIED |
| V3-N07 | The Bhattarai (2014) sentence at Ch2:300 is now plain text with no citation command at all (residue of m11). | `chapter_02_literature_review.tex:300` | Minor / Narrow | VERIFIED |
| V3-N08 | Almumani's source variable "DP" (regression table B = 0.016, p = 0.803) was standardised to "DPR" in prose (Ch2:228) and Table 2.1 (Ch2:330) without noting the relabelling. Substance (insignificant) is correct; only the label departs from the source. Introduced by the loop's patch. | `chapter_02_literature_review.tex:228, 330` | Minor / Narrow | VERIFIED |
| V3-N09 | Two plain-text author-year mentions without a citation command: "Employing the Ohlson (1995) valuation framework" (L224, pre-existing) and the Bhattarai sentence (L300). Both works are cited elsewhere, so no claim is unsupported at chapter level. | `chapter_02_literature_review.tex:224, 300` | Suggestion / Narrow | VERIFIED |
| V3-N10 | `bajracharya2019` has no DOI although HEAD carried 10.3126/njmsr.v2i1.36868; web search returned no confirming record. Whether the DOI is valid (removal a loss) or invalid (removal correct) could not be established. Pre-existing removal, not a loop action. | `src/thesis/references.bib` (`bajracharya2019`) | Suggestion / Narrow | UNVERIFIED |
| V3-N11 | App D's DPS table shows the target deadline (2022-04-13) as the "MPS^RD Price Date" for the two excluded rows (HBL/NIMB FY 2077/78), while Appendix A shows the actual resumption dates (2022-06-06 / 2022-05-30). The eligibility claim still holds under either date, so this is presentational, not substantive. | `appendices/appendix_d.tex:295` (table `tab:app_dps_dates`) | Minor / Narrow | VERIFIED |
| V3-N12 | "Restatements are exactly three" (App D:263) is unqualified and reads against Ch3:171's five balance-sheet restatements; in context it means the three EPS restatements. Pre-existing wording, not loop-introduced. | `appendices/appendix_d.tex:263` | Minor / Narrow | VERIFIED |
| V3-N13 | Kanchan figures at Ch3:80 still have no page locator; the register pointer is report-level only and now redundant beside the `\citep`. | `chapter_03_research_methodology.tex:80` | Suggestion / Narrow | VERIFIED |
| V3-N14 | NPR differences in §4.2.1 don't reproduce from printed means (104.99 vs text 105.00; 3.86 vs 3.87) — same unrounded class as m45, but the Table 4.1 note's disclosure covers only percentage changes. | `chapter_04_results_and_discussion.tex:71–72, 74` | Minor / Narrow | VERIFIED |
| V3-N15 | §4.3.2 asset-quality bullet calls the earnings-slope drop "the observed drop" although the drop is not significant (δ_E = −3.124, p = 0.448). | `chapter_04_results_and_discussion.tex:614` | Suggestion / Narrow | VERIFIED |
| V3-N16 | Table 4.7 still stars R6 with no multiplicity caveat in its note (:456, :468) — the M07 fix covered only Table 4.6. A reader who reads only Table 4.7 takes away an unqualified significant R6 result. | `chapter_04_results_and_discussion.tex:456, 468` | Minor / Narrow | VERIFIED |
| V3-N17 | Chapter IV never explicitly cites the new Appendix E post-slopes table (0 hits for `app_postslopes` in Ch4); only the range reference at :504 spans it implicitly. | `chapter_04_results_and_discussion.tex:476–480, 504` | Minor / Narrow | VERIFIED |
| V3-N18 | §4.3.2 capital-expansion bullet states the paid-up equity expansion without a Chapter IV source or cross-reference (the supporting figures are in Ch1:15 and Ch3:80). | `chapter_04_results_and_discussion.tex:615` | Suggestion / Narrow | VERIFIED |
| V3-N19 | The inserted 2-of-30 clause in abstract:15 breaks the sentence's parallel structure ("reducing… although…, and using…"). Introduced by the loop's patch. | `front/abstract.tex:15` | Minor / Narrow | VERIFIED |
| V3-N20 | Appendix B note now falsely claims the R7 bonus ratios "are not printed in this thesis" — Appendix D prints them (Table `tab:app_bonus_ratios`, :271–288). Loop-introduced cross-scope contradiction; one clause → a pointer fixes it. (Residue of m51, §8.) | `appendices/appendix_b.tex:84` | Minor / Narrow | VERIFIED (coordinator read the sentence and confirmed the App D table exists) |
| V3-N21 | BVPS post-consolidation mean printed 161.97 (Ch5:76) vs 161.976 → 161.98 recomputed from the 28 realised Appendix B rows; SD change −15.31% vs printed −15.30%. Consistent with unrounded computation, but the unrounded values are not printed, so it cannot be determined whether this is a rounding artefact or an error. Pre-existing. | `chapter_05_summary_and_conclusion.tex:76` | Minor / Narrow | VERIFIED (recomputation from printed data) |
| V3-N22 | Chapter V still contains no pointer to Appendix B (or to any appendix) — zero "Appendix" mentions in the whole chapter. | `chapter_05_summary_and_conclusion.tex` (whole chapter) | Suggestion / Narrow | VERIFIED |
| V3-N23 | The new M10 limitations restatement (Ch5:180) drops the "development banks, finance companies, or non-financial listed sectors" clause from the Ch1:173 boundary it claims to restate. | `chapter_05_summary_and_conclusion.tex:180` vs `chapter_01_introduction.tex:173` | Minor / Narrow | VERIFIED |
| V3-N24 | Table `tab:app_m1full`'s own note (App E:59) still does not expand EPS/BVPS below that table; coverage relies on the appendix-intro sentence at :4. (Residue of m49, §8.) | `appendices/appendix_e.tex:59` | Minor / Narrow | VERIFIED |
| V3-N25 | The Kumari SGM bib-title rewording ("Minutes of the Special General Meeting, FY 2079/80" → "Extraordinary general meeting document, FY 2079/80 (merger proposals and share swap ratio)") is undocumented in the loop log. The rewording itself honours the limitation; the issue is record-keeping only. | `src/thesis/references.bib:296–301` (`kumari2022sgm`) | Suggestion / Narrow | VERIFIED |
| V3-N26 | RQ3 is a single ~70-word question whose item order differs from Objective 3 (content now matches item-for-item). | `chapter_01_introduction.tex:46` vs `:56–66` | Suggestion / Narrow | VERIFIED |
| V3-N27 | "Prominent" is still the sampling descriptor in Ch1:13/30 with no threshold stated in Chapter I. | `chapter_01_introduction.tex:13, 30` | Suggestion / Narrow | VERIFIED |
| V3-N28 | Two abbreviation entries still have (at most) incidental body use: DiD once outside the list (App D:12), FAIR once (Ch5:243), AQR only as plural "AQRs" (Ch5:189). Substantive use UNVERIFIED. | `front/abbreviations.tex:49, 58` | Suggestion / Narrow | VERIFIED (counts); UNVERIFIED (substantive use) |
| V3-N29 | §4.3.3 dividend-signalling bullet still presents the verification mechanism without the DPS–price caveat (residue of M08). | `chapter_04_results_and_discussion.tex:634–635` | Minor / Narrow | VERIFIED (coordinator read the bullet) |

**Summary counts (new issues only): 0 Critical, 0 Major, 19 Minor, 10 Suggestion = 29 total.**

## 11. Open questions for the author and items that could not be determined or assessed

### 11.1 Open questions needing the author (not text changes on present evidence)

1. **M01 — Prabhu–Century exclusion reason.** No reason is stated anywhere. The author must either supply the factual reason or consciously submit with the limitation (already accepted once, 2026-11-17). An examiner will ask (Q1).
2. **m37 — Pradhan & Dahal "168 obs".** Still unverified; the author must confirm it against the source.
3. **Almumani discrepancy.** A secondary source asserts 7 banks / 49 observations; v2 (which opened the full text) records the bank count as not stated. The author must confirm against the full text.
4. **Kumari SGM exact title.** The bib title is now a neutral descriptive title; the exact title still needs the author to open the PDF once.
5. **Roll No. 67514/24, Registration No. 7-2-48-1060-2018, "Pokhara, Nepal".** Match the proposal title page exactly; unverified against the college record.
6. **R9 extension to n = 26.** Not run; optional estimation.
7. **Sharma DPS-sign conflict.** The limitation's referent cannot be located in the thesis (prose and synthesis row agree, DPS positive in both); the author/supervisor must clarify what the conflict is, or the limitation should be reworded.
8. **GBIME 16th AGM minutes PDF.** Never read (process fact); the minutes support a profile detail (paid-up capital); the 9 Jan 2023 date is verified independently via NRB BSR.
9. **Four PAT deletions unconfirmed.** The author's action at github.com/settings/tokens.
10. **Supervisor-guidance origin unconfirmed.** The thesis does not cite the five pasted messages; nothing in them counts as granted approval.
11. **New analyses (v1 residues F17/F18/F20, F10, F03, F08).** Analysis, not prose; need the author's call. The m44/m45 remainders (interacted-DPS F, N = 30/stale-price Fs, ROA SD +97.49%) also need new model runs or the unrounded output.

### 11.2 Open questions needing supervisor confirmation

Declaration page; ethics/COI/funding/AI statements; four-section Chapter V (disclosed deviation); 17-word title (FOM suggests 12, in the proposal passage); place line "Pokhara, Nepal" (FOM template shows none); spacing-list contradiction (FOM p. 20 contradicts itself); authorship wording ("declare" vs FOM's "corroborate"); Research Committee labels and approval-sheet date rule; whether the "Organization of the Study" justification satisfies the FOM supervisor-advice route (s06); whether the appendix TOC treatment (single bold "Appendix" entry) complies (FOM does not specify).

### 11.3 Items that could not be determined or assessed

- All rendered output (no build): abstract/acknowledgements one-page fit, TOC/LOT/LOF contents and page numbers, rendered APA 6th formatting, longtable pagination, figure/table numbering as rendered, caption placement as rendered.
- Figure plotted contents (only `fig:value_relevance` was visually checked, by v2).
- FOM 2019 currency (no newer edition found in the repo or in public search; a campus-held newer copy would supersede it).
- The exact installed software versions (no lockfile); the Chaitra-end calendar source; the five-day window's rationale.
- Source accuracy of the loop's added prose sentences for Sharma (2011), Bajracharya (2019), Niroula (2021), Gyawali (2022), and Gurung & Subedi (2024) (m18 — thesis-internal consistency verified; sources not opened in v3).
- The Holthausen & Watts (2001) DOI direct resolution (fetch failed, not retried); the validity of the HEAD Bajracharya DOI (V3-N10).
- Whether the single DiD/FAIR occurrences outside the abbreviations list are substantive uses (V3-N28).

---

## 12. Verification log

### 12.1 What was checked, and how

- **Six independent scope reviews**, each reading its area in full from the thesis source and re-running every grep/count: front matter + Ch1 (212 lines + 8 front files); Ch2 (410 lines) + references.bib (75 entries); Ch3 (395 lines) + App A (96 lines) + App D (425 lines); Ch4 (678 lines); Ch5 (251 lines) + App B (86) + App C (30) + App E (651); criteria/compliance (FOM 2019 full extraction, 1,103 lines; Essex live regulations; per-figure caption checks; untouched-items diff checks; language counts).
- **Coordinator's independent spot-checks** (re-run against the thesis source, not taken from the scope reviews): "Prabhu" occurs exactly twice thesis-wide (Ch1:30, Ch3:31); Ch1:197–200 (s06 justification sentence present); Ch1:212 opening and figures; Ch4:634–635 (§4.3.3 bullet, no caveat); Ch2:407 paragraph exists; App B:84 false sentence read + App D bonus table exists (4 hits for `app_bonus_ratios`); Table 4.7 R6 row (bold starred 5.818 (0.021)*); `tab:app_postslopes` label exists at App E:185; bare `$MPS^{RD}$` 0 hits thesis-wide; OLS first use unexpanded at Ch1:30, VIF at Ch1:206, NFRS at Ch2:112; abstract word count hand-verified (see below); test suite re-run read-only-safe (36/36 pass).
- **Abstract word count — coordinator's hand verification.** Two body paragraphs (abstract.tex:15, 17) counted by hand, sentence by sentence, under three methods: maths removed = 295 words (para 1: 146; para 2: 149); maths as one token each = 310; maths contents as words = 334. HEAD: 272 / 284 / 305. Growth: +23 / +26 / +29 words. The criteria scope counted 316/331; its para-2 count (167) does not reproduce the coordinator's hand count for that paragraph (149 — verified sentence by sentence above in the coordinator's working notes: 28+30+25+19+29+18 = 149). The discrepancy (18 words) is in the criteria scope's implementation, not in the thesis text; the conclusion is therefore stated as a range in §10 (V3-N01), and the exceedance of the Essex 300-word cap is method-sensitive (exceeded under the one-token and keep methods; 295, just under, under the strictest maths-removed method). v2's 206/217 is wrong under every method; the loop's "~12 words" is wrong under every method.
- **Recomputations:** App E post-slopes table — all six rows independently recomputed from the frozen `results.pkl` by the Ch5 scope reviewer (own script, linear combination through the HC3 covariance; generator never imported); App D DPS table 30/30 vs the announcement CSV and bonus table 30/30 vs dps.json and the bonusadj CSV (Ch3 scope, programmatic); Table 3.1 vs App A cell-for-cell (Ch3 scope, programmatic); App D register 5,663 pages / 328.31 MB recomputed from the printed rows (Ch3 scope); Ch4 t-statistics, R6 arithmetic, FE-only derivations, VIF/tolerance pairs (Ch4 scope); BVPS post mean recomputed from the 28 realised App B rows (Ch5 scope: 161.976 → 161.98).
- **External sources opened in v3:** repo-held NMB FY 2077/78, HBL FY 2079/80, NIMB FY 2079/80 annual reports (Ch2 scope, m08/m36); Barth et al. (2001) full text via search (definition verbatim, p. 79); Almumani (2014) full text via search (DP B = 0.016, p = 0.803); Chhetri (2023) NepJOL page; Essex Principal Regulations live PDF; FOM 2019 PDF (repo copy, SHA-256 matched).
- **Git status (final, run by the coordinator):** HEAD `2b4e10f`; 39 modified files + 3 pre-existing untracked paths + the new `docs/thesis_review/v3/` files (7 files: six scope reviews + this consolidation). No other file was created, modified, or built. Tests 36/36 (re-run read-only-safe by the coordinator).

### 12.2 What could not be verified (and why)

Listed in §11.3. The largest gaps are rendered output (no build, per the task), figure plotted contents, most cited facts against their external sources, FOM 2019 currency, and the m44/m45 text-only numbers (which need new model runs or the unrounded output).

### 12.3 Disagreements between reviewers, and how they were resolved

- **s06 (FIXED vs PARTIALLY FIXED):** the front scope recorded FIXED (justification sentence exists at Ch1:200); the Ch5 scope recorded PARTIALLY FIXED (supervisor confirmation of the FOM route remains open). The coordinator read Ch1:197–200 and governs: the finding asked for a justification to be stated, and one is stated — FIXED. The supervisor-confirmation route is a separate open item (§11.2), not part of the finding.
- **Abstract word count (316/331 vs 295/310/334):** the criteria scope counted 316 (maths removed) / 331 (maths as one token); the coordinator's hand count gives 295 / 310 / 334. The para-1 counts agree closely (146 vs 148); the para-2 counts do not (149 hand-verified vs 167). Recorded as a range with the method sensitivity stated (§10, V3-N01); the growth and the v2/loop errors are robust under every method.
- **m51 (FIXED App D part vs PARTIALLY FIXED overall):** the Ch3 scope verified the App D bonus table (FIXED); the Ch5 scope recorded PARTIALLY FIXED because the App B sentence is now false. Consolidated as PARTIALLY FIXED with the incorrect limb as new issue V3-N20.
- **m48 count (loop's "10" vs true 14):** the Ch5 scope counted 14 bare occurrences at HEAD (10 cross-file + 4 in Appendix B); the coordinator re-ran the grep and confirms 0 bare now. Recorded as FIXED with the count correction.
- **m49 "exactly once":** the loop claimed the Model 2 expansion sentence appears exactly once in the assembled App E; the Ch5 scope found it twice (:105 and :207, by design — the post-slopes note reuses the same expansion). Recorded as PARTIALLY FIXED with the count correction.

---

## 13. Overall submission-readiness verdict, nearest institutional category, and blocking issues

### Verdict: **Ready with minor revisions** — subject to the accepted standing limitation V2-M01

**How component results combine:** FOM 2019 states no rule for combining component results into an overall result, so no such rule was applied. The overall verdict follows the task's rationale and the Essex proxy's definitions: every component except Chapter I is "Ready with minor revisions"; Chapter I is "Needs major revision — on V2-M01 alone". V2-M01 is not an editorial defect — it is a missing fact (the reason for the Prabhu–Century exclusion) that cannot be supplied by revision, only by the author. The user already accepted it once as a standing limitation (2026-11-17, "skip all"). The remaining editable work is entirely Narrow: 19 Minor and 10 Suggestion new issues, plus the narrow residues of two partially-fixed Majors (M08, M12) and one partially-fixed Minor (m51). Under the Essex proxy, that is "pass subject to minor corrections" — corrections that "should not require the candidate to conduct further research or undertake substantial further work" (typographical errors, clarifying points, rephrasing, editing/adding paragraphs, correcting references). Nothing in v3 requires re-writing substantial parts of the thesis, re-analysis, or new data.

**The verdict is conditional in exactly one way:** it stands as long as M01 stands as an accepted limitation. If the supervisor requires the Prabhu–Century exclusion to be answered rather than accepted, the verdict reverts to "Needs major revision" on that single item — not because the thesis needs re-writing, but because the sampling claim would need a factual answer the thesis does not currently have.

### Blocking issues (must be resolved before submission)

1. **V2-M01 (Major, standing limitation) — author decision required.** Prabhu–Century is listed (Ch1:30) yet silently excluded from the sample, with no reason anywhere in the thesis. The author must either supply the factual reason or consciously submit with the limitation, knowing an examiner will ask (Q1). No edit can fix this.
2. **V2-M08 residue (Major, partial) — one clause.** The §4.3.3 dividend-signalling bullet (Ch4:634–635) still presents the verification mechanism without the DPS–price caveat (r = 0.082, p = 0.679) that §4.3.2 now carries. Narrow fix.
3. **V2-M12 residue (Major, partial) — one clause.** The Ch2:407 lead clause still says the small-cluster gap is addressed "by implementing MacKinnon-White HC3", although the qualification sentence now follows it. Narrow fix.
4. **V2-m51 limb (Minor, now incorrectly stated) — one clause.** Appendix B:84 falsely claims the R7 bonus ratios "are not printed in this thesis" while Appendix D prints them. Narrow fix (point at Table `tab:app_bonus_ratios`).

### Not blocking (for the avoidance of doubt)

The 19 Minor and 10 Suggestion new issues (§10) — all narrow text fixes, none changing a claim or conclusion; the v1 residues needing analysis (F17/F18/F20, F10, F03, F08 — see §11.1); the open questions in §11 that require supervisor confirmation rather than text changes; and anything that can only be settled by a build (rendered fits, TOC contents, figure pixels).

### 13.3 Does the loop's "zero new issues" convergence claim hold up?

**No — not in substance.** The loop's log records that its Round 2 re-review found "ZERO new issues" from the Round 1 patches and its Round 4 re-review found "ZERO new issues" from the Round 3 patches, and on that basis the loop declared convergence. This independent read found **29 distinct new issues** (§10), of which **at least 7 were introduced or caused by the loop's own patches** (V3-N01 abstract word growth; V3-N03/N04/N05 the moved Ch1:212 paragraph and V3-N19 the abstract clause; V3-N08 the Almumani relabelling; V3-N20 the Appendix B contradiction; V3-N02 the stale fit comment is a consequence of the lengthening). The loop also misstated three of its own results: the abstract grew by +23/+26/+29 words, not "~12"; the m48 total was 14 bare occurrences, not 10; the m49 Model 2 expansion sentence appears twice in the assembled App E, not "exactly once".

**Why the loop missed them:** its re-review rounds (Rounds 2–4) were conducted directly by its coordinator, not by fresh independent reviewers — subagent spawning had failed for it ("subagent bootstrap is no longer authorized"), a caveat the loop itself flagged. The re-reviews were therefore not independent fresh-eyes checks, and the misses are concentrated exactly where fresh eyes matter: cross-scope contradictions (App B vs App D), second instances of a fixed defect (Table 4.7 vs Table 4.6; §4.3.3 vs §4.3.2), and the side effects of the loop's own edits (the moved paragraph, the lengthened abstract).

**What this does and does not mean.** It does not mean the loop's fixes were wrong in substance: 52 of 85 findings are fully fixed, no finding was incorrectly fixed as a whole, no new issue is Critical or Major, and no new issue changes a claim, a conclusion, or a hypothesis decision. The loop's convergence claim fails on the count of new issues, not on the quality of the fixes. But "zero new issues" is not an accurate description of the thesis as it now stands, and the remaining work (§14) should be done before submission.

---

## 14. Recommended actions, prioritized and NOT applied

*None of the actions below has been applied. This review is read-only; the author (or a further fix pass on the author's instruction) applies them.*

### Priority 1 — Blocking (resolve before submission)

1. **M01:** author decision — supply the Prabhu–Century exclusion reason, or consciously submit with the limitation (and be ready for Q1 at the viva).
2. **M08 residue:** add the DPS–price caveat to the §4.3.3 bullet (Ch4:634–635) — one clause ("the sample itself shows no dividend–price association (r = 0.082); this is a theoretical mechanism, not a corroborated finding").
3. **M12 residue:** correct the Ch2:407 lead clause so the small-cluster gap is not attributed to implementing HC3 (e.g. "addresses this gap by disclosing … and reporting sensitivity …, using HC3 as the heteroskedasticity-robust estimator").
4. **m51 limb:** fix App B:84 — replace "the per-bank-year bonus ratios used in R7 are not printed in this thesis" with a pointer to Table `tab:app_bonus_ratios`.

### Priority 2 — New Minor issues (narrow fixes, before submission)

5. Table 4.7 note: add the Holm caveat (V3-N16).
6. Chapter IV: cite `tab:app_postslopes` at :476/:480 or in the :504 pointer (V3-N17).
7. Ch1:212: fix the R2–R9 label ("the eight joint tests", V3-N03); give the paragraph a home (a short closing subsection, or place it before §1.7 — V3-N04); move the definition sentence to the front of the paragraph (V3-N05).
8. Abstract: re-punctuate the 2-of-30 clause into its own sentence (V3-N19); trim ~20–35 words to sit safely inside 300 under any counting method (V3-N01); update or delete the stale fit comment (V3-N02).
9. App D DPS table: footnote or rename the price-date column for the two excluded rows (V3-N11).
10. App D:263: qualify "Restatements are exactly three" as "EPS restatements are exactly three" (V3-N12).
11. Ch5:180: restore the three excluded sectors to the restated boundary (V3-N23).
12. Table 4.1 note: extend the unrounded-values disclosure to the NPR differences (V3-N14).
13. `wilkinson2016fair`: "Guiding Principles" → "guiding principles" (V3-N06).
14. Ch2:300: replace plain-text "Bhattarai (2014)" with `\citet{bhattarai2014}` (V3-N07).
15. Almumani: restore the source label "DP" in prose and Table 2.1, or add a note that the thesis standardises DP to DPR (V3-N08).
16. App E `tab:app_m1full` note: add the EPS/BVPS expansion below that table (V3-N24).
17. Ch5:76: check the BVPS post mean (161.97 vs 161.98 recomputed) and the SD change (−15.30% vs −15.31%) against the unrounded pipeline values (V3-N21).

### Priority 3 — New Suggestions (narrow, before submission if time allows)

18. Reorder RQ3's items to follow Objective 3 (V3-N26).
19. State a threshold for "prominent" in Ch1, or drop the descriptor there (V3-N27).
20. Run the abbreviation list against the full text; remove or retain DiD/FAIR/AQR on the evidence (V3-N28).
21. Convert the two plain-text author-year mentions to `\citet` (V3-N09).
22. Check the Bajracharya DOI against the journal record (V3-N10).
23. Add a page locator for the Kanchan figures, or drop the redundant register pointer (V3-N13).
24. Reword "the observed drop in the earnings slope" to "the point-estimate attenuation" (V3-N15).
25. Add a cross-reference for the capital-expansion bullet's equity-base premise (V3-N18).
26. Add a pointer to Appendix B/E in Chapter V §5.2.2 (V3-N22).
27. Record the Kumari SGM retitle in the review notes (V3-N25).
28. Choose one spelling convention and apply it: "behaviour" → "behavior" (7 sites) or the reverse (see §15 item 7).

### Priority 4 — Author / supervisor items (not text changes on present evidence)

29. §11.1 author items (m37, Almumani, Kumari title, Roll/Reg/Pokhara, R9 extension, Sharma referent, GBIME minutes, PAT deletions, supervisor-guidance origin, new analyses).
30. §11.2 supervisor items (Declaration, ethics/COI/funding/AI, four-section Ch5, title length, place line, spacing-list choice, authorship wording, committee labels, date rule, s06 route, appendix TOC treatment).
31. m44/m45 remainders: new model runs (interacted-DPS F, N = 30/stale-price Fs) or the unrounded output (ROA SD); m30 calendar source; m35 five-day rationale or window-sensitivity analysis; s10 exact installed versions (lockfile).

### Priority 5 — Build checks (author's manual v37 build)

32. Abstract and Acknowledgements one-page fits (FOM R-02); TOC/LOT/LOF contents and page numbers; rendered APA 6th formatting; Table 2.1 longtable pagination; figure pixels (only `fig:value_relevance` has ever been visually checked); caption placement as rendered.

---

## 15. Appendix: minor language, typographic, and formatting items with locations (not applied)

*Items already numbered as findings in §10 are cross-referenced, not repeated. This appendix holds the remaining language-only observations.*

1. **Long sentences (pattern VERIFIED; counts method-sensitive).** By the criteria scope's stated method (maths removed): Ch. I 22 sentences > 45 words; Ch. V 24; Abstract 1. v2's counts (22/28/2) reproduce only for Ch. I. Longest Ch. I sentences include the 93-word Alternative Hypothesis item and the 77-word Ch. IV-preview item. Suggestion — sentence-level edits only.
2. **"Mathematically closed" unexplained** (Ch1:7): "provides an analytically rigorous and mathematically closed foundation linking financial accounting numbers directly to equity share prices" — the term is never defined. Suggestion (v2-s08 residue).
3. **Evaluative adjectives** (Ch1:11): "profound structural…", "severe institutional proliferation… cutthroat lending competition", "historic fourfold capital expansion mandate" — v2-s08 residue, readability-only. Suggestion.
4. **"Central" doing quiet selection work** (Ch1:173): "four merged series from the central corporate combinations of the 2023 consolidation wave" — which combinations count as "central" is not defined in Chapter I. Suggestion; this must not be read as a reason for the Prabhu–Century exclusion.
5. **"Moral suasion" and "big mergers"** (Ch2:202): the thesis's own characterisations, not the cited news article's words (established by v2). Not raised as a finding; recorded as a statement of fact.
6. **"Standardise" in source comments only** (`front/abstract.tex:7`, `front/acknowledgements.tex:7`): British spelling in comments, not body text. Cosmetic.
7. **"Favour/favoured" (3×) and "centre" (2× prose)** with no American counterpart — consistently British, so not mixed; only "behaviour" (7×) vs "behavior" (1×) is a live inconsistency.
8. **Figure file names non-sequential** (F6, F1, F2, F3, F4, A2, F5 in presentation order) — cosmetic, compiled numbering unaffected (V2-s14, intentionally unchanged).
9. **Appendix C label orphan:** `\ref{app:diagnostics_robustness}` (App C:2) is still never referenced in the body; the appendix is reachable by the textual "Appendix C" mention and the two figure refs (m52 residue).

---

*End of review — final independent pre-submission review (v3). Overall verdict: **Ready with minor revisions**, subject to the accepted standing limitation V2-M01. See §13 for the blocking issues and §14 for the prioritized actions, none of which has been applied.*
