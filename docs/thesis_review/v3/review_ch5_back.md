# Independent pre-submission review (v3) — Chapter V + Appendices B, C, E

**Thesis:** "Value Relevance of Accounting Information Before and After the Banking
Consolidation Wave: Evidence from Nepalese Commercial Banks" — Asmita Subedi,
Triveni International College, MBS, Tribhuvan University, FOM. November 2026.
**Repo:** `~/workspace/verbose-chainsaw`. **HEAD:** `2b4e10f` (working tree as it
stands, including uncommitted loop changes; no commit, no build).
**Review date:** 18 November 2026. **Reviewer role:** scope reviewer, read-only.
No repo file was modified, renamed, deleted, or reformatted; no build was run.
The only file created is this one:
`docs/thesis_review/v3/review_ch5_back.md`.

**Scope.** In full: `src/thesis/chapters/chapter_05_summary_and_conclusion.tex`
(Ch5, 251 lines), `src/thesis/appendices/appendix_b.tex` (86 lines),
`src/thesis/appendices/appendix_c.tex` (30 lines),
`src/thesis/appendices/appendix_e.tex` (651 lines), and, only to check that
generated tables match their generator inputs,
`src/thesis/generators/appendix_e/` (`gen_tables_e.py`, `assemble_e.py`,
`appendix_e_prose.tex`, `tables_e_fragment.tex`, `results.pkl`).
For traceability checks only: `src/thesis/chapters/chapter_01_introduction.tex`
(RQ3, hypotheses, limitations — cited locations only),
`src/thesis/chapters/chapter_04_results_and_discussion.tex` (cited locations
only: Ch4:303, 434, 469, 477, 480, 483, 486, 488, 508; figure order),
`src/thesis/appendices/appendix_d.tex` (cited locations only: bonus-ratios
table, restated-EPS values, section numbering), and `src/thesis/main.tex`
(lines 44–62, 110–122) plus `src/thesis/config/preamble.tex`
(`\thesisFrontList` definition, line 277).

**Status vocabulary.** VERIFIED = I read the text, opened the source, or
re-ran the grep/count/computation myself. INFERRED = the basis is stated and
the claim goes beyond what was directly observed. UNVERIFIED = I could not do
the check, and why is stated. **Fix vocabulary.** FIXED / PARTIALLY FIXED /
NOT FIXED / INCORRECTLY FIXED / FALSE FINDING, each with file:line and an
exact excerpt as evidence. Severities: Critical / Major / Minor / Suggestion.
Revision scales: Narrow / Substantive / Fundamental.

**Method and independence.** The v2 review
(`docs/thesis_review/v2/content_review.md` §10 and
`docs/thesis_review/v2/review_ch5_back.md`), the hallucination audit
(`docs/thesis_review/v2/verification_audit.md`), and the fix-loop log
(`~/workspace/review-audit-scratch/loop-v2/LOOP_STATUS.md` and `ROUND_*.md`)
were read ONLY to know what was claimed to have been done. No finding below
rests on their authority: every grep, count, and recomputation was re-run by
me against the thesis source, and every quoted excerpt was copied from a file
I opened. Where the loop log and my own count disagree, my count governs and
the disagreement is stated. Statistics were NOT re-audited (data treated as
correct, per the task); the one exception is arithmetic I re-derived myself
from the frozen `results.pkl` and from the printed Appendix B rows, which is
text-consistency checking, not re-estimation.

## Verdicts (exactly one each)

| Item | Verdict |
|---|---|
| (i) Chapter V (Summary, Conclusion, and Implications) | **Ready with minor revisions** |
| (ii) Appendices B, C, E together | **Ready with minor revisions** |

*Rationale in one line each.* (i) The three assigned Majors in Chapter V are
all fixed in the text (M02, M10, M13), the conclusions still follow only from
the findings, and the implications remain hedged; what remains in Chapter V
is one unpatched count wording (E-03, author input required), one trimmed
limitations clause (N-04), and a missing pointer to Appendix B (N-03).
(ii) Appendix C is now referenced, correctly framed, and noted; the new
Appendix E post-slopes table reproduces its frozen source exactly; what
remains is one false sentence in the Appendix B note (N-01, introduced by the
loop itself), one 0.01 rounding difference (N-02, pre-existing), and a
residual table-note expansion gap (N-05).

## 1. Part A — Verification of the loop's fixes for the v2 findings in scope

Assigned findings: 3 Majors (M02, M10, M13), 7 Minors (m48–m52, m55, m56),
4 Suggestions (s05, s06, s13, s14) = **14**. Outcome: **8 FIXED, 3 PARTIALLY
FIXED, 3 NOT FIXED**. (The E-03/M01 Chapter V limb and the scope-adjacent
s15/s16/s17 checks are reported separately below the table and are not counted
in the 14.)

### 1.1 Verification table

| v2 ID (scope ID) | Audit verdict | Loop's claimed fix | MY verification | Evidence (file:line + exact excerpt) |
|---|---|---|---|---|
| V2-M02 (E-02) — RQ3 restatement omits Kanchan | CORRECTED (narrow to the Kanchan limb; the FY 2078/79 limb is covered by RQ3's "exclusion of structural transition periods") | RQ3 restatement names Kanchan | **FIXED.** VERIFIED | `chapter_05_summary_and_conclusion.tex:33`: "How sensitive are the estimated valuation coefficients to transition-year effects, entity-timing mismatches, operating profitability substitutions, inclusion of eligible dividend disclosures, bonus share adjustments, restated earnings, and sensitivity analysis excluding the NMB FY 2076/77 bank-year with the Kanchan acquisition timing mismatch?" The Ch1 RQ3 itself was also reworded (other scope): `chapter_01_introduction.tex:46` now ends "…and sensitivity analysis excluding the NMB FY 2076/77 bank-year with the Kanchan acquisition timing mismatch?" so Ch5 and Ch1 now agree. |
| V2-M10 (E-01) — No consolidated limitations restatement in Ch5 | CONFIRMED | Limitations restatement added in Ch5 | **FIXED.** VERIFIED, with one trimming noted as new issue N-04 | `chapter_05_summary_and_conclusion.tex:180` (new paragraph at the end of §5.3, before §5.4): "Two limits stated in Chapter~I bear on how far these conclusions travel. First, the sample of five purposively selected bank series cannot be generalized to the entire commercial banking industry; the findings apply directly to the selected institutions and their specific consolidation contexts. Second, actual publication dates were verified in the reviewed records for only 2 of the 30 bank-years; for the remaining observations, the statutory deadline does not establish when the information became public, so the post-reporting-deadline pricing protocol rests on the deadline as an operational rule rather than on verified publication in each case." Both limbs are present: the generalizability boundary and the 2-of-30 publication-date limit. Wording checked against Ch1: `chapter_01_introduction.tex:173` ("the sample cannot be generalized to the entire commercial banking industry, development banks, finance companies, or non-financial listed sectors. Findings apply directly to the selected institutions and their specific consolidation contexts.") and `:194` ("Actual publication dates were verified in the reviewed records for only 2 of the 30 bank-years; for the remaining observations, the statutory deadline does not establish when the information became public."). |
| V2-M13 (E-04) — Table 5.1 gives opposite decisions for the same joint null in adjacent rows | CONFIRMED | Table 5.1 R6 cell now reads "Sensitivity only — no decision (Holm-adjusted p = 0.169)" | **FIXED.** VERIFIED | `chapter_05_summary_and_conclusion.tex:160`: "(Composite Test) & R6 Joint Wald (Sens.) & $H_0: \delta_E=\delta_B=0$ & $F(2, 10) = 5.818, p = 0.021$ & Sensitivity only --- no decision (Holm-adjusted $p = 0.169$) \\\\" — directly below the baseline row at `:158`–`:159` ("Joint Regime Shift & Model 2 Joint Wald & $H_0: \delta_E=\delta_B=0$ & $F(2, 14) = 2.954, p = 0.085$ & Fail to Reject $H_0$"). The surrounding prose still resolves it: `:177` "The evidence for a regime shift is therefore sensitivity-dependent and not conclusive." No "Reject $H_0$" decision remains anywhere in the table's Empirical Decision column for the joint null (grep for "Reject $H_0$" in the table returns only "Fail to Reject $H_0$" rows plus the new sensitivity-only cell). |
| V2-m48 (E-07) — Two renderings of $MPS^{RD}$ | CONFIRMED | 10 bare `$MPS^{RD}$` → `$\mathit{MPS}^{RD}$` | **FIXED.** VERIFIED — but the loop's "10" is only part of the count; the true total is 14 | I counted occurrences (not lines) in every `.tex` file under `src/thesis/` at HEAD and now. HEAD: **14** bare `$MPS^{RD}$` occurrences, **54** `$\mathit{MPS}^{RD}$` occurrences. Now: **0** bare, **72** `$\mathit{MPS}^{RD}$` occurrences. The 14 bare break down as Ch1 4, Ch2 3, Ch3 1, abstract 1, abbreviations 1 (= the loop's 10, cross-file) plus Appendix B 4 (fixed in this scope). The remaining +4 mathit occurrences (72 − 54 − 14) are new `$\mathit{MPS}^{RD}$` mentions added by other scopes' new sentences/tables in Appendix D (+3) and Chapter IV (+1) — e.g. the new DPS announcement-dates table header `appendix_d.tex:272`–`:288` area ("$\mathit{MPS}^{RD}$ Price Date", appearing in both the firsthead and head), all in the correct form. No bare occurrence remains anywhere in the thesis. Appendix B now reads `appendix_b.tex:6` "($\mathit{MPS}^{RD}$)" and `:84` "$\mathit{MPS}^{RD}$ represents the NEPSE secondary market closing price…". |
| V2-m49 (E-08b) — Table-note abbreviation expansion missing in scope tables | CONFIRMED | Expansion sentences added to the two App E note strings in `gen_tables_e.py` and regenerated via `assemble_e.py` | **PARTIALLY FIXED.** VERIFIED, with two qualifications | (a) The two generator strings exist: `gen_tables_e.py:110–111` ("Dependent variable: $\\mathit{MPS}^{RD}$. EPS is earnings per share; BVPS is book value per share; SE is standard error.") for the Model 2 note, and `:234–235` ("fixed effects. ROA is return on assets; EPS is earnings per share; BVPS is book value per share; DPS is cash dividend per share.") for the robustness note. Both appear in the assembled `appendix_e.tex` — the robustness sentence exactly once (`:176`), the Model 2 sentence **twice**, not once: `:105` (Table `tab:app_m2full` note) and `:207` (new Table `tab:app_postslopes` note, `gen_tables_e.py:410–411`, which reuses the same expansion). The task's "exactly once" premise is therefore not met for that sentence; the duplication is by design (the loop's Round 4 record says so) and is harmless, but it is a count discrepancy, not a defect. The appendix-intro expansion is present once (`appendix_e.tex:4`): "In the tables, EPS is earnings per share, BVPS is book value per share, DPS is cash dividend per share, ROA is return on assets, SE is standard error, and LSDV denotes the least-squares dummy-variable fit." (b) Ch5 side fixed: `chapter_05_summary_and_conclusion.tex:167` note now reads "SE denotes standard error."; `appendix_b.tex:84` note now reads "EPS is earnings per share, BVPS is book value per share, DPS is cash dividend per share, and ROA is return on assets." (c) Residual gap (new issue N-05): Table `tab:app_m1full`'s own note (`appendix_e.tex:59`) still does not expand EPS/BVPS below that table — it reads "Dependent variable: $\mathit{MPS}^{RD}$. Bank fixed effects include 4 dummies…" with no EPS/BVPS expansion; it relies on the intro sentence at `:4`. The same reliance applies to the `tab:app_robust_inf` / fixed-effect tables' notes. |
| V2-m50 (E-12) — Four-section Ch5 vs the Guidelines' three-section organisation | CONFIRMED | Disclosed deviation needing supervisor confirmation, NOT a patch | **NOT FIXED — correctly so.** VERIFIED as still a disclosed deviation | `chapter_05_summary_and_conclusion.tex:6`: "The \textit{Master's Degree Dissertation Guidelines} (2019, p.~15) of the Faculty of Management, Tribhuvan University organize the concluding chapter into three sections---Summary, Conclusion, and Implications, with recommendations and areas for future research reported under Implications. This chapter follows that structure and, for clarity of presentation, separates the recommendations and future-research material into its own section. It is therefore organized into four core functional sections:" followed by the four-item enumerate (`:7`–`:13`). The deviation is still disclosed in the text, all three required sections are present, and no silent "fix" was applied. Supervisor confirmation is still outstanding — no supervisor confirmation is recorded in the thesis source. I did not re-open the Guidelines PDF itself; the disclosure wording is as quoted above. |
| V2-m51 (E-06) — Appendix B not self-contained for the R7/R8 robustness inputs | CONFIRMED (absence); audit §6.2 #15 later claimed bonus ratios are printed nowhere in the thesis | R8 values pointed to App D §D.4; R7 ratios cross-referenced | **PARTIALLY FIXED, and one limb is now INCORRECTLY stated (see N-01).** VERIFIED | `appendix_b.tex:84`: "Variant R8 substitutes restated basic EPS for GBIME FY 2076/77 and NMB FY 2077/78; the restated values are given in Appendix~D, Section~D.4. Variant R7 uses bonus-adjusted BVPS (BVPS divided by one plus the bonus ratio), as defined in Appendix~D, Section~D.6; the per-bank-year bonus ratios used in R7 are not printed in this thesis." The R8 pointer checks out: the values are at `appendix_d.tex:263` ("Global IME Bank FY 2076/77 reported EPS 17.99, restated 15.33; NMB Bank FY 2077/78 reported 16.66, restated 14.76; Himalayan Bank FY 2077/78 reported 28.07, restated 27.60"), inside §D.4 Variable Codebook (4th `\section`, `appendix_d.tex:224`). The R7 definition pointer also checks out (§D.6 Estimation Recipe, `appendix_d.tex:389`; R7 defined at `:403`). BUT the final clause is now false: the per-bank-year bonus ratios ARE printed in the thesis, in `appendix_d.tex:271`–`:288`, Table `tab:app_bonus_ratios`, caption "Bonus Ratios by Bank-Year (R7 Inputs; Percent of Paid-Up Capital)", populated 5 series × 6 fiscal years (e.g. "GBIME & 14.00 & 10.00 & 3.00 & 1.00 & 5.50 & 0.00", "NMB & 13.00 & 12.50 & 0.00 & 0.00 & 0.00 & 5.00"). That table did not exist at HEAD (`git show HEAD:…appendix_d.tex` contains 0 occurrences of `app_bonus_ratios`); it was added by the loop (another scope) after the Appendix B sentence was written. The audit's "printed nowhere" claim is therefore also now false. |
| V2-m52 (E-05) — Appendix C unreferenced, overstates coverage, figures carry no notes | CORRECTED (audit: coverage sentences are App C lines 4 and 6, not 5 and 7) | Coverage sentences corrected; notes added; body pointer added | **FIXED.** VERIFIED, with one residual nit | (i) Coverage: `appendix_c.tex:4` now reads "This appendix presents additional graphical diagnostic evaluations for Model~2 and the comparative earnings-channel robustness forest across eight plotted EPS-channel specifications (R1, R2, and R4 through R9); R3 is omitted because ROA is on a different scale." — eight, not nine; the R3 reason is now stated here. `:6` reads "Figure~\ref{fig:app_robustness_forest} presents the coefficient forest plot contrasting parameter estimates and 95\% HC3 confidence intervals across the eight plotted EPS-channel specifications (R1, R2, and R4 through R9)." No "full ninefold suite" wording remains (grep: 0 hits for "ninefold" in App C). (ii) Notes: forest note at `:15` ("Forest plot of the EPS-channel estimates (earnings coefficient and EPS $\times$ Post interaction) with 95\% HC3 confidence intervals across eight plotted specifications: two baselines (R1--R2) and six variants (R4--R9). R3 is omitted because ROA is on a different scale. Samples are $N = 28$, $N = 27$, or $N = 23$.") and diagnostics note at `:28` ("Four-panel diagnostic suite for Model~2 residuals: Normal Q-Q plot assessing error normality, Residuals vs.\ Fitted values assessing linearity, Scale-Location plot assessing homoskedasticity, and Cook's distance across observations identifying influential observations against the $4/N = 0.143$ attention threshold ($N = 28$)."). (iii) Body pointer: `chapter_04_results_and_discussion.tex:508`: "The Model~2 residual diagnostics and the robustness forest are printed in Appendix~C (Figures~\ref{fig:app_robustness_forest} and ~\ref{fig:app_model2_diagnostics})." Both figure labels exist in App C (`:11`, `:25`). Residual nit: the appendix label itself, `\ref{app:diagnostics_robustness}` (`appendix_c.tex:2`), is still never referenced anywhere in the body — the appendix is reachable by the textual "Appendix~C" mention and the two figure refs, so the orphan is cured in substance, but a strict label-reference still does not exist. |
| V2-m55 — LOT/LOF at 1.5 spacing vs single-spaced TOC | CORRECTED (audit: correct citation is `main.tex:48, 55–59`, not 59–64) | LOT/LOF now single-spaced | **FIXED.** VERIFIED | HEAD `main.tex:56` read `\thesisFrontList[1.5]{List of Tables}` and `:59` `\thesisFrontList[1.5]{List of Figures}`. Now `main.tex:55`–`:59` read "% List of Tables (single-spaced per the instructions standard, §9.3)" / `\thesisFrontList{List of Tables}{\listoftables}` and "% List of Figures (single-spaced per the instructions standard, §9.3)" / `\thesisFrontList{List of Figures}{\listoffigures}`. The mechanism checks out: `config/preamble.tex:277` defines `\newcommand{\thesisFrontList}[3][1]{%` with `\setstretch{#1}`, so the bare call uses stretch 1 (single). The TOC call at `main.tex:48` was already bare at HEAD. I verified the mechanism in the source; I did not re-open the instructions document §9.3 itself, and rendered spacing cannot be checked without a build. |
| V2-m56 — Appendix entries hidden from the TOC (single bold "Appendix" entry) | CONFIRMED (UNVERIFIED whether compliant; FOM does not specify) | Not patchable (loop record) | **NOT FIXED.** VERIFIED (no change) | `main.tex:118`–`:119` are byte-identical to HEAD (the `git diff HEAD -- main.tex` touches only lines 55–59): `\addcontentsline{toc}{chapter}{\bfseries Appendix}` and `\addtocontents{toc}{\protect\setcounter{tocdepth}{-1}}`. The five appendix chapters still keep body headings but only one bold "Appendix" entry appears in the TOC. Compliance remains UNVERIFIED: FOM 2019 does not specify appendix TOC treatment (per v2/audit), and the rendered TOC cannot be checked without a build. No supervisor decision is recorded in the source. |
| V2-s05 — RQ3 has no corresponding hypothesis | CONFIRMED (recorded, not a defect) | — (no patch expected) | **FIXED (addressed by explicit statement).** VERIFIED | No hypothesis was added for RQ3, correctly. Instead Ch1 now states it explicitly: `chapter_01_introduction.tex:75`: "Research Question~3 has no corresponding hypothesis; it is answered by the robustness suite R3--R9 (Chapter~IV), not by a hypothesis test." (Ch1-scope patch; verified in the Ch1 source.) Chapter V is unchanged on this point and needs no change. |
| V2-s06 — "Organization of the Study" is an extra section beyond the FOM Chapter I list, no justification stated | CONFIRMED | — | **PARTIALLY FIXED.** VERIFIED | The section still exists: `chapter_01_introduction.tex:197` `\section{Organization of the Study}`. A purpose sentence was added at `:200`: "This dissertation is organized into five chapters, structured in accordance with the \textit{Master's Degree Dissertation Guidelines (2019)} of the Faculty of Management, Tribhuvan University. The Organization of the Study section is included to orient the reader to the five-chapter structure of the dissertation:" Whether that stated purpose satisfies the Guidelines' justification/supervisor-advice route is still a supervisor-confirmation matter, not something the text alone settles. |
| V2-s13 — No detectable-effect / power statement in Chapter IV | CONFIRMED | — (Ch5 already stated them) | **FIXED (in Chapter IV).** VERIFIED | `chapter_04_results_and_discussion.tex:303` now reads: "A post hoc design-sensitivity calculation gives approximate detectable effects at 80\% power of 10.73 NPR for the pre-period EPS slope, 12.06 NPR for the EPS interaction, and 3.71 NPR for the BVPS interaction, so these non-rejections do not rule out effects smaller than those magnitudes." — the same three figures Chapter V states at `chapter_05_summary_and_conclusion.tex:108`. (Ch4-scope patch; verified in the Ch4 source.) |
| V2-s14 — Figure file names non-sequential relative to presentation order | CONFIRMED | — (cosmetic only) | **NOT FIXED.** VERIFIED | Presentation order in Ch4 by `\includegraphics` line is unchanged: `chapter_04_results_and_discussion.tex:88` F6_trends, `:145` F1_scatter_matrix, `:157` F2_correlation_heatmap, `:313` F3_value_relevance, `:325` F4_coefficient_forest, `:494` A2_robustness_forest, `:556` F5_diagnostics. Files exist as `F1`–`F6`, `A1`–`A3` in `src/thesis/figures/`. Compiled figure numbers follow LaTeX order and are unaffected; this is a file-naming artefact only, as v2 stated. |

### 1.2 Scope-adjacent items verified in passing (not counted in the 14)

| Item | Verification |
|---|---|
| V2-s16 / E-10 — Wild-cluster bootstrap p reported as 0.062; exact fraction 2/32 = 0.0625 | **FIXED.** VERIFIED. `chapter_05_summary_and_conclusion.tex:132` now reads "gives $p = 0.0625$ for both the baseline and R6 … with 32 patterns the smallest attainable $p$-value is $2/32 = 0.0625$"; `chapter_04_results_and_discussion.tex:486` likewise reads "the bootstrap $p$-value is $0.0625$ (2 of 32 patterns)". "0.062" no longer occurs in either chapter for this check (grep for `0.062` in Ch4/Ch5 returns only the `0.0625` occurrences). |
| V2-s17 / E-13 — Causal verb "exerts" in the H2 conclusion sentence | **FIXED.** VERIFIED. `chapter_05_summary_and_conclusion.tex:174` now reads "Book value per share shows no statistically significant incremental pricing effect in the baseline specification." The word "exerts" occurs 0 times in Chapter V. |
| V2-s15 / E-09 — Abbreviations first appear unexpanded (Ch5 limbs: ICAN, ESG) | **FIXED on the Ch5 limbs.** VERIFIED. `chapter_05_summary_and_conclusion.tex:201`: "The Accounting Standards Board (ASB) of Nepal and the Institute of Chartered Accountants of Nepal (ICAN) could consider…"; `:244`: "Investigation of Non-Financial Disclosure and Environmental, Social, and Governance (ESG) Metrics:" with `:245` expanding it again in the body text. (HC3/OLS/VIF/NFRS/NPR first uses are in Ch1/Ch2, outside this scope.) |
| V2-M01 / E-03 (Ch5 limb) — "Four amalgamated series representing the major corporate combinations" omits the unsampled fifth combination | **NOT FIXED.** VERIFIED. `chapter_05_summary_and_conclusion.tex:41` is byte-identical to HEAD: "Four amalgamated banking series representing the major corporate combinations of the early-2023 wave: Global IME Bank Limited (GBIME, absorbed Bank of Kathmandu), Himalayan Bank Limited (HBL, acquired Civil Bank), Kumari Bank Limited (KBL, absorbed NCC Bank), and Nepal Investment Mega Bank Limited (NIMB, amalgamation of Nepal Investment Bank and Mega Bank Nepal); and". The fifth combination (Prabhu–Century) is still never mentioned in Chapter V. This was expected: the exclusion reason is author-supplied only (standing limitation), and the narrow "four of the five" rewording was not applied either. No reason for the exclusion is stated anywhere in Chapter V; I did not search the whole thesis for a reason, per the standing instruction not to invent one. |

### 1.3 New Appendix E table `tab:app_postslopes` — existence, placement, values

**Existence and placement: VERIFIED.** `appendix_e.tex:184`–`:213`:
`\caption{Implied Post-Consolidation Slopes for the Baseline and Year-Drop Specifications}`
(`:184`), `\label{tab:app_postslopes}` (`:185`). It sits in the Robustness
Estimates section, immediately after Table `tab:app_robustfull` (`:148`) and
before Table `tab:app_robust_inf` (`:215`). It is introduced in the section
prose at `:141`: "Table~\ref{tab:app_postslopes} prints the implied
post-consolidation slopes for the baseline (R2) and the two year-drop
specifications (R5, R6), with full inference; the R5 and R6 implied slopes are
the values Chapter IV discusses." The label is defined once and referenced
once in the appendix (plus the generator template). The appendix now has 13
tables (was 12); no prose anywhere states a table count, so no stale "twelve"
remains (grep for "twelve"/"Twelve" in `appendix_e.tex` and
`appendix_e_prose.tex`: 0 hits).

**Values — recomputed by me from the frozen `results.pkl`: VERIFIED exactly.**
I did NOT import the generator (it writes files on import). I wrote an
independent script (`/tmp/recompute_postslopes.py`, scratch only) that loads
`src/thesis/generators/appendix_e/results.pkl` read-only and applies the
linear-combination arithmetic from first principles (coef = level +
interaction; SE = √(V_bb + V_dd + 2·V_bd) from the stored HC3 covariance;
two-sided t p-value and 95% CI on the stored residual df). All six rows
reproduce the printed table to the printed precision, including SEs, t, p,
CIs, N, and df:

| Row (appendix_e.tex) | My recomputation from results.pkl | Match |
|---|---|---|
| R2 Post EPS `:221`: $2.4534$ ($2.2687$), $1.08$, $0.298$, $[-2.4124, 7.3192]$, 28, 14 | 2.4534 / 2.2687 / 1.08 / 0.298 / [−2.4124, 7.3192], N=28, df=14 | Yes, exact |
| R2 Post BVPS `:223`: $-1.6576$ ($1.1198$), $-1.48$, $0.161$, $[-4.0593, 0.7441]$, 28, 14 | −1.6576 / 1.1198 / −1.48 / 0.161 / [−4.0593, 0.7441], N=28, df=14 | Yes, exact |
| R5 Post EPS `:229`: $3.4149$ ($3.8912$), $0.88$, $0.401$, $[-5.2552, 12.0849]$, 23, 10 | 3.4149 / 3.8912 / 0.88 / 0.401 / [−5.2552, 12.0849], N=23, df=10 | Yes, exact |
| R5 Post BVPS `:231`: $-2.0806$ ($1.9685$), $-1.06$, $0.315$, $[-6.4668, 2.3055]$, 23, 10 | −2.0806 / 1.9685 / −1.06 / 0.315 / [−6.4668, 2.3055], N=23, df=10 | Yes, exact |
| R6 Post EPS `:233`: $1.8997$ ($2.6492$), $0.72$, $0.490$, $[-4.0032, 7.8026]$, 23, 10 | 1.8997 / 2.6492 / 0.72 / 0.490 / [−4.0032, 7.8026], N=23, df=10 | Yes, exact |
| R6 Post BVPS `:235`: $-1.8091$ ($1.3573$), $-1.33$, $0.212$, $[-4.8334, 1.2152]$, 23, 10 | −1.8091 / 1.3573 / −1.33 / 0.212 / [−4.8334, 1.2152], N=23, df=10 | Yes, exact |

Cross-checks (all VERIFIED): the R2 rows match the note to Table
`tab:app_m2full` exactly (`appendix_e.tex:105`: "implied post-consolidation
slopes are EPS $2.4534$ (SE $2.2687$, $t = 1.08$, $p = 0.298$, 95\% CI
$[-2.4124, 7.3192]$) and BVPS $-1.6576$ (SE $1.1198$, $t = -1.48$, $p = 0.161$,
95\% CI $[-4.0593, 0.7441]$)"); the R5/R6 coef/p match
`data_analysis/analysis/tests/test_stats.py:130`–`:150`
(`test_robustness_post_slopes_match_review_recomputation`: 3.415/0.401,
−2.081/0.315, 1.900/0.490, −1.809/0.212); and the R5/R6 values including SEs
match the Chapter IV prose (`chapter_04_results_and_discussion.tex:477`:
"$\hat{\beta}_E + \hat{\delta}_E = 3.415$ (SE $= 3.891$, $p = 0.401$) for EPS
and $\hat{\beta}_B + \hat{\delta}_B = -2.081$ (SE $= 1.969$, $p = 0.315$) for
BVPS"; `:480`: "The implied post-consolidation slopes are
$\hat{\beta}_E + \hat{\delta}_E = 1.900$ (SE $= 2.649$, $p = 0.490$) and
$\hat{\beta}_B + \hat{\delta}_B = -1.809$ (SE $= 1.357$, $p = 0.212$)").
The generator fragment agrees too: `tables_e_fragment.tex:225`–`:235` print
identical values. The table's note (`appendix_e.tex:207`) states "No post
slope is significant at 5\%." — correct: all six p-values are 0.161–0.490.
Caveat: this verifies the linear-combination arithmetic from the frozen
`results.pkl` (beta, HC3 covariance V, df); the underlying estimation that
produced `results.pkl` was NOT re-audited, per the task (data treated as
correct).

**Regeneration pull-ins claimed by the loop: VERIFIED.** (1) Appendix-intro
abbreviation expansion: `appendix_e.tex:4` now ends "In the tables, EPS is
earnings per share, BVPS is book value per share, DPS is cash dividend per
share, ROA is return on assets, SE is standard error, and LSDV denotes the
least-squares dummy-variable fit." — the same sentence is in the prose
template `appendix_e_prose.tex:4`, and it appears exactly once in the
assembled appendix (grep count 1). (2) R9 df corrected 14→13:
`appendix_e.tex:10` now reads "R3, R7, and R8 carry 14 parameters and 14
degrees of freedom; R9 carries 14 parameters and 13 degrees of freedom
(N = 27)." — the same sentence is in `appendix_e_prose.tex:10`; it matches
Ch4 (`chapter_04_results_and_discussion.tex:434`: "Residual degrees of
freedom: R1 16; R2, R3, R7, R8 14; R4, R9 13; R5, R6 10."; `:483`: "Dropping
the single bank-year … (NMB FY 2076/77, $N = 27$, residual df = 13) … with
joint Wald $F(2, 13) = 1.79$ ($p = 0.205$)") and the robustness table itself
(`appendix_e.tex:173`, R9 row: N 27, df 13). The superseded HEAD wording
("All other robustness specifications carry 14 parameters and 14 degrees of
freedom") no longer occurs in Appendix E.

## 2. Part B — Fresh read of Chapter V + Appendices B, C, E as they now stand

I read all four files in full as they now stand (Ch5 251 lines, App B 86,
App C 30, App E 651) and re-checked the headline numbers against each other
and against the cited Chapter IV locations. Conclusions follow only from the
findings; the hedging recorded by v2 is intact (e.g. Ch5:123 "Results are
reported as associations across calendar periods, not as an established causal
merger impact"; §5.4/§5.5 name what was not measured before recommending
anything on that topic). No conclusion overreaches the null results: every
non-rejection carries its exact statistic and p-value, and the R6 sensitivity
is fenced on every appearance (Ch5:97–102, 119, 123, 132, 160, 177). Table
5.1's eight rows re-check against App E Tables `tab:app_m1full` /
`tab:app_m2full` / `tab:app_robustfull` (2.095/0.616, 5.577/0.140, 0.219/0.908,
0.100/0.940, −3.124/0.448, −1.758/0.175, F(2,14) = 2.954/0.085,
F(2,10) = 5.818/0.021). Appendix B prints 30 data rows (5 banks × 6 fiscal
years; counted by regex over the bank-year rows), with the two excluded rows
flagged and footnoted with the delayed prices (NPR 358.90 / 367.70). Appendix
E's df/R² accounting re-checks (Model 1 K=12/df=16, Model 2 K=14/df=14,
R4 df=13, R5/R6 df=10, R9 df=13; R² 0.948/0.978 in the baseline notes).

### 2.1 New issues found

#### N-01 — Appendix B note now makes a false claim about the R7 bonus ratios (loop-introduced contradiction)

- **Location:** `src/thesis/appendices/appendix_b.tex:84`.
- **Severity:** Minor. **Revision scale:** Narrow (one clause → a pointer).
- **Status:** VERIFIED.
- **Evidence:** Appendix B note: "the per-bank-year bonus ratios used in R7 are not printed in this thesis." Appendix D, Table `tab:app_bonus_ratios`
  (`appendix_d.tex:271`–`:288`, caption "Bonus Ratios by Bank-Year (R7 Inputs; Percent of Paid-Up Capital)"), prints exactly those ratios, 5 series × 6
  fiscal years (e.g. "GBIME & 14.00 & 10.00 & 3.00 & 1.00 & 5.50 & 0.00",
  "NMB & 13.00 & 12.50 & 0.00 & 0.00 & 0.00 & 5.00"), and
  `appendix_d.tex:265` states "Table~\ref{tab:app_bonus_ratios} prints the
  bonus ratios used in Specification R7". The table did not exist at HEAD (0
  occurrences of `app_bonus_ratios` in the HEAD Appendix D); it was added by
  the loop after the Appendix B sentence was written, so the two patches
  contradict each other. The fix is one clause: point Appendix B at Table
  `tab:app_bonus_ratios` instead of asserting absence. No estimate or
  conclusion depends on it. (This is the R7 limb of V2-m51, now INCORRECTLY
  FIXED rather than merely unpatched.)

#### N-02 — BVPS post-consolidation mean printed as 161.97; the printed Appendix B rows give 161.976 → 161.98 (pre-existing, still present in Ch5)

- **Location:** `src/thesis/chapters/chapter_05_summary_and_conclusion.tex:76`
  (and Ch4 Table 4.1, per the v2 audit's incidental find — Ch4 is outside
  this scope, so the Ch5 occurrence is the finding here).
- **Severity:** Minor. **Revision scale:** Narrow (one number, if it is an error).
- **Status:** VERIFIED (recomputation from the printed data).
- **Evidence:** Ch5:76: "Mean BVPS increased by 2.45\% from NPR 158.11 to NPR 161.97, while its SD declined by 15.30\% (NPR 19.10 to NPR 16.18)." I recomputed from the 28 realised Appendix B rows with a script
  (`/tmp/check_bvps3.py`, sample SD, ddof=1, realised rows only — the two
  `Excluded` rows omitted): pre mean 158.1077 → 158.11 ✓, post mean **161.9760
  → 161.98**, post SD 16.1754 → 16.18 ✓, SD change **−15.31\%** (thesis
  −15.30\%). The +2.45\% mean change reproduces either way. The 0.01
  differences are consistent with computation from unrounded pipeline values,
  but the unrounded values are not printed, so I cannot determine whether this
  is a rounding artefact or an error — the same position v2 took on the
  parallel ROA figure (E-14), which Chapter V does not repeat. No conclusion
  depends on 0.01 NPR.

#### N-03 — Chapter V still contains no pointer to Appendix B (or to any appendix)

- **Location:** `src/thesis/chapters/chapter_05_summary_and_conclusion.tex`
  (whole chapter); contrast `chapter_04_results_and_discussion.tex:508`,
  which now points to Appendix C.
- **Severity:** Suggestion. **Revision scale:** Narrow (one pointer sentence
  in §5.2.2).
- **Status:** VERIFIED — grep for "Appendix" in Chapter V returns 0 hits.
- **Evidence:** Chapter V never mentions "Appendix" at all, so a reader of
  the concluding chapter alone has no route to the complete dataset printed in
  Appendix B (or to the estimation outputs in Appendix E). Chapter IV already
  points to Appendix B, so this is a usability gap, not a defect. (V2 noted
  the same gap as an unnumbered suggestion; the loop did not add a pointer.)

#### N-04 — The new M10 limitations restatement trims the generalizability boundary (drops the three excluded sectors named in Ch1)

- **Location:** `src/thesis/chapters/chapter_05_summary_and_conclusion.tex:180`;
  contrast `src/thesis/chapters/chapter_01_introduction.tex:173`.
- **Severity:** Minor. **Revision scale:** Narrow (add one clause).
- **Status:** VERIFIED.
- **Evidence:** Ch1:173: "the sample cannot be generalized to the entire commercial banking industry, development banks, finance companies, or non-financial listed sectors." Ch5:180: "the sample of five purposively selected bank series cannot be generalized to the entire commercial banking industry; the findings apply directly to the selected institutions and their specific consolidation contexts." The "development banks, finance companies, or non-financial listed sectors" clause is dropped, so the restated boundary is narrower than the Chapter I boundary it claims to restate ("Two limits stated in Chapter~I bear on how far these conclusions travel"). The second limit (2-of-30) is restated faithfully. No conclusion changes, but an examiner comparing the two passages will notice the trimming.

#### N-05 — Table `tab:app_m1full`'s own note still does not expand EPS/BVPS below that table (residual of V2-m49)

- **Location:** `src/thesis/appendices/appendix_e.tex:59` (note to Table
  `tab:app_m1full`).
- **Severity:** Minor. **Revision scale:** Narrow (one sentence in the note,
  or a generator change in `gen_tables_e.py:103`).
- **Status:** VERIFIED.
- **Evidence:** The note reads "Dependent variable: $\mathit{MPS}^{RD}$. Bank fixed effects include 4 dummies (reference: GBIME); fiscal-year fixed effects include 5 dummies (reference: FY 2076/77). $N = 28$; parameters $K = 12$; residual degrees of freedom $= 16$; $R^2$ (LSDV) $= 0.948$…" — the Variable column lists EPS and BVPS as row labels, but neither is expanded below this table. Coverage currently relies on the appendix-intro sentence at `:4` ("In the tables, EPS is earnings per share, BVPS is book value per share…"). Under a strict reading of the Guidelines rule quoted by v2 ("abbreviations in tables must be explained below the table"), that is one remove away from the table. The same reliance applies to the `tab:app_robust_inf` and fixed-effect tables' notes, which carry no expansions of their own.

### 2.2 Things checked in the fresh read and found sound (no new issue)

- **Table 5.1 vs prose (M13 follow-through):** the R6 cell change did not
  break the prose resolution — Ch5:177 still reads "The evidence for a regime
  shift is therefore sensitivity-dependent and not conclusive", and Ch5:119
  (Answer to RQ3) and Ch5:123 (§5.3.2) still carry the Holm-adjusted p = 0.169
  alongside the unadjusted p = 0.021.
- **Post-slopes note claim:** "the R5 and R6 rows are the values Chapter IV
  discusses" (`appendix_e.tex:207`) — verified against Ch4:477/480 (see §1.3).
  "No post slope is significant at 5\%." — verified (p = 0.161–0.490).
- **Appendix C forest note sample sizes:** "Samples are $N = 28$, $N = 27$,
  or $N = 23$" (`appendix_c.tex:15`) — correct: R1/R2/R3/R4/R7/R8 N=28, R9
  N=27, R5/R6 N=23, matching `tab:app_robustfull`.
- **Appendix C diagnostics threshold:** "$4/N = 0.143$ attention threshold
  ($N = 28$)" (`appendix_c.tex:28`) — correct arithmetic (4/28 = 0.142857).
- **Stale-price wording:** Ch5:132 "Carrying forward the 12 May 2021
  panel-series prices for HBL/NIB ($487/453$)" matches Ch4:488 ("using the
  last prices in the panel-series files for HBL (NPR 487) and NIB/NIMB
  (NPR 453), both dated 12 May 2021"). "NIB" is the pre-merger name of the
  NIMB constituent; the two chapters use it identically.
- **No new overreach in §5.4/§5.5:** the loop's patches did not add any
  implication; the hedges recorded by v2 are verbatim intact (e.g. Ch5:191
  "though DPS was never shown to anchor valuation (its correlation with price
  is $r = 0.082$, $p = 0.679$)"; Ch5:201 "this study does not establish that
  current reporting is non-uniform, so the recommendation rests on
  transparency grounds rather than on a documented deficiency").
- **M10 paragraph placement:** the new paragraph sits at the end of §5.3
  (after the itemised hypothesis decisions, `:180`–`:181`, before §5.4 at
  `:182`) — a sensible place for a limitations restatement; it does not
  duplicate anything else in Chapter V.
- **No duplicate labels introduced:** `tab:app_postslopes` is defined once
  (`appendix_e.tex:185`) and referenced once in the appendix prose (`:141`);
  all 13 Appendix E table labels are distinct (grep count of
  `\label{tab:app_` = 13).
- **No other loop-introduced contradiction found in scope** beyond N-01: the
  Ch5 diff was read in full (90 changed lines); the only other substantive
  Ch5 changes are the M02/M10/M13/s16/s17 fixes verified in §1.

## 3. What I could not verify (and why)

- **Rendered output:** no build was run (per the task). LOT/LOF single
  spacing (m55), the TOC appendix entry (m56), table/figure numbering, and
  the abstract/one-page fits are source-level checks only. m56 in particular
  remains UNVERIFIED for compliance because FOM 2019 does not specify
  appendix TOC treatment and the rendered TOC was not seen.
- **Figure contents:** the two Appendix C figure PDFs
  (`figures/A2_robustness_forest.pdf`, `figures/A3_model2_diagnostics.pdf`)
  were not opened or rendered; only their existence (directory listing, as in
  v2) and the surrounding text/notes were checked. Whether the plotted
  contents match their captions is UNVERIFIED.
- **Underlying estimation:** the frozen `results.pkl` (beta, HC3 covariance
  V, df) is taken as correct, per the task. My post-slopes recomputation
  verifies the linear-combination arithmetic from those stored values, not
  the regressions that produced them. No estimation code was run.
- **Guidelines and instructions documents:** I did not re-open the FOM 2019
  Guidelines PDF or the instructions standard §9.3; m50's "disclosed
  deviation" status rests on the thesis's own quotation at Ch5:6, and m55's
  fix rests on the `\thesisFrontList` default-argument mechanism in
  `config/preamble.tex:277`. Supervisor confirmations (m50, m56, s06) remain
  open questions for the author/supervisor — nothing in the thesis source
  records them.
- **Chapters II and Appendix D in full:** consulted by targeted search only
  (bonus-ratios table, restated-EPS values, section numbering). The Appendix D
  bonus-ratios values themselves (e.g. HBL FY 2077/78 21.38, NIMB FY 2077/78
  12.611) were NOT verified against annual reports; only their presence in
  the thesis and their contradiction with the Appendix B note were checked.
- **Tests:** the loop log claims 36/36 tests pass after its rounds; I did not
  re-run the test suite (read-only review; running tests was not in my task
  and could write cache files). The test-file expectations I cite
  (`test_stats.py:130`–`:150`) were read, not executed.

## 4. Read-only compliance and git status confirmation

- No thesis, code, data, config, v1, or v2 file was modified, renamed,
  deleted, or reformatted during this review. All scratch work (recomputation
  scripts `/tmp/recompute_postslopes.py`, `/tmp/check_bvps*.py`) ran in `/tmp`
  only. The thesis was not built or compiled. The generator was never
  imported or executed (it writes files on import); `results.pkl` was opened
  read-only.
- `git status` was run at the end of the task: the modified-tracked-file list
  is unchanged from the pre-existing loop state (39 modified files + the same
  untracked entries); the only new file in the repo from this task is this
  one, `docs/thesis_review/v3/review_ch5_back.md`, created in the already
  existing `docs/thesis_review/v3/` directory alongside sibling reviewers'
  files (`review_ch4_results.md`, `review_front_ch1.md`), which I did not
  read, modify, or overwrite. HEAD is `2b4e10f` as at the start.

## 5. Summary counts

- **Part A (14 assigned findings): 8 FIXED** (M02, M10, M13, m48, m52, m55,
  s05, s13), **3 PARTIALLY FIXED** (m49, m51, s06), **3 NOT FIXED** (m50 —
  disclosed deviation by design; m56 — no change; s14 — cosmetic, no change).
  Additionally verified in passing: s16 FIXED, s17 FIXED, s15 Ch5 limbs FIXED;
  E-03/M01 Ch5 limb NOT FIXED (author input required).
- **Part B (new issues): 5** — N-01 Minor (false Appendix B sentence on R7
  bonus ratios, loop-introduced), N-02 Minor (BVPS post mean 161.97 vs 161.98
  recomputed, pre-existing), N-03 Suggestion (no Appendix pointer in Ch5),
  N-04 Minor (M10 restatement drops the three excluded sectors), N-05 Minor
  (Table `tab:app_m1full` note still lacks EPS/BVPS expansion).
- **Post-slopes table:** exists, correctly placed, and all six rows reproduce
  exactly from the frozen `results.pkl` by independent recomputation; R2 rows
  match the Model 2 note; R5/R6 values match `test_stats.py` and Ch4 prose.
- **No Critical finding.** Nothing in scope invalidates a conclusion or
  requires re-analysis. The remaining work in scope is narrow text fixes
  (N-01, N-02, N-04, N-05, E-03 wording) plus supervisor confirmations
  (m50, m56, s06) and the unbuilt rendered checks listed in §3.
