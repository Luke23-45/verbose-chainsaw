# Verification audit of the v2 independent content review (hallucination audit)

**Review audited:** `docs/thesis_review/v2/content_review.md` (752 lines; 85 findings: 0 Critical, 13 Major, 52 Minor, 20 Suggestion) plus the six scope reviews (`review_front_ch1.md`, `review_ch2_refs.md`, `review_ch3_method.md`, `review_ch4_results.md`, `review_ch5_back.md`, `review_criteria_compliance.md`) and `pass_a_note.md`.
**Thesis audited against:** `src/thesis/` working tree as it stands; HEAD `2b4e10f`. **Audit date:** 17 November 2026.
**Method:** six independent verifiers, one per area (Majors; Minors m01–m19 + m24–m39; Minors m40–m56 + Suggestions; Criteria + verification log + strengths; Counts + Pass A + inventory; v1 follow-up). Each verifier read the review's cited locations in the primary source and recorded a verdict per finding. The coordinator independently spot-checked the consequential corrections (M03, M11, m29, s07, m17, the abstract figures, S1, S3, the floats macro) by re-running the greps and reads itself. Partial reports: `/tmp/hallucination-audit/` (`majors.md`, `minors_a.md`, `minors_b_suggestions.md`, `criteria_log_strengths.md`, `counts_passa_inventory.md`, `v1_followup.md`).
**Rules:** read-only throughout; no thesis, code, data, config, v1, or v2 file modified; no build; `~/workspace/review-audit-scratch/` not read; no finding taken on the v2 review's own authority — every verdict below rests on a primary source the verifier opened.

**Verdict vocabulary:** CONFIRMED (claim accurate as stated) / CORRECTED (claim partly wrong — the true state is given) / REFUTED (claim false at its core, or the location does not say what the review claims). A finding whose location or excerpt is wrong is at minimum CORRECTED; REFUTED is reserved for a false core claim.

## 1. Method

For each of the 85 numbered findings the assigned verifier opened the cited thesis location (file + line/section/table/figure) and checked (a) the location exists, (b) any quoted excerpt matches the file exactly, (c) the claim about the thesis is accurate, (d) the severity and revision scale are justified. Criteria (§3) were checked against the FOM 2019 guideline extracted per page and the Essex proxy PDF opened live. The v1 follow-up (§8) was checked item by item against the v1 review and the current thesis text. Counts (§10) were recounted from the table rows. Strengths (§7), the Pass A comparison (§2.6), the inventory (§4.1), and the verification log (§12) were checked against the thesis source, the scope files, and `git` output. What was not re-run is listed in §7.

## 2. Per-finding verdicts

### 2.1 Major findings (13): 9 CONFIRMED, 4 CORRECTED, 0 REFUTED

| ID | Verdict | Evidence |
|---|---|---|
| V2-M01 | CONFIRMED | Prabhu–Century listed Ch1:30, "is not sampled" Ch3:29; "Prabhu" occurs exactly twice in the whole thesis; no reason stated anywhere. |
| V2-M02 | CORRECTED | Kanchan limb solid (R9 reported, no RQ asks for it). But the FY 2078/79 limb is overstated: RQ3's "exclusion of structural transition periods" fairly covers it, and Ch5:33 names "entity-timing mismatches". Narrow to the Kanchan gap. Still Major. |
| V2-M03 | CORRECTED | Core right: R² = 0.948 and 0.100 are absent from Ch1 (zero grep hits — independently re-run by the coordinator). But the review's evidence is wrong in two ways: (i) it claims Ch1:17 contains the pre-EPS slope 5.577 and "the EPS leg does check out from Chapter I alone: 5.577 + (−3.124) = 2.453" — Ch1 contains no `5.577`/`5.58`/`2.453`/`1.658` anywhere, so the EPS leg is *also* unverifiable from Ch1 and the gap is wider than M03 states; (ii) §9 Q3 says "Your abstract reports … a pre-consolidation BVPS slope of 0.100" — the abstract never prints 0.100 (it prints implied post −1.658; 0.100 is a Ch4/Ch5 figure). Still Major; the §13 blocking item 13 should also add the pre-EPS slope (5.577) and the implied post slopes to Ch1, not only R² and 0.100. |
| V2-M04 | CONFIRMED | Results paragraph is Ch1:17, last paragraph of §1.1 Background; RQs at L44–47; R2–R9/Holm occur in Ch1 only at L17. |
| V2-M05 | CONFIRMED | Abstract "resolves" (L15) vs Ch1 "directly addresses" (L15); "resolves" 0× in Ch1; 2-of-30 qualification (Ch1:148, 185–186) absent from abstract; Ch5:125–127 "do not establish whether this theoretical substitution occurred". |
| V2-M06 | CORRECTED | Core confirmed (Ch1 Limitations contain zero hits for classical/HC0/HC1/HC2/estimator; the reversal is stated Ch4:391 and Ch5:93). But the cited location Ch5:100–101 is wrong — those lines are the R6 F-equation; the reversal statement is at **Ch5:93**. Also an internal scale inconsistency: §10.1 says Narrow, A-06 says Substantive, §11 counts M06 among the five substantive Majors. Still Major. |
| V2-M07 | CONFIRMED | Ch4:420 R6 cell is `\textbf{5.818 (0.021)\textsuperscript{*}}`; note L433 says only "* Significant at p < 0.05", no Holm; prose qualification at Ch4:478 (Holm p = 0.169). |
| V2-M08 | CONFIRMED | L614/L634 mechanism bullets vs DPS–price r = 0.082, p = 0.679 (Ch4:118, 133); "0.082" occurs nowhere else in Ch4; Ch5:191 does flag it. (Caveat: "contradicts" is strong wording for a bivariate correlation, but all factual limbs are exact.) |
| V2-M09 | CONFIRMED | Ch4:230 promises CIs "reported in the text"; the only numeric CIs in Ch4 text are the two pre-slopes (L286, L383); no numeric CI for δ_E, δ_B or either implied slope; all four are in App E (δ_E [−11.7096, 5.4622], δ_B [−4.3975, 0.8816], implied [−2.4124, 7.3192] / [−4.0593, 0.7441]). |
| V2-M10 | CONFIRMED | Ch5 has zero hits for generaliz/verified/publication-date/limitation; neither the generalizability boundary (Ch1:171) nor the 2-of-30 limit (Ch1:185–186) appears in §§5.3–5.5. |
| V2-M11 | CORRECTED | Core confirmed: FOM p.21 "Figures must have numbers and captions under the figures"; App C p.28 "Put them below the figure"; `config/preamble.tex:74` sets `position=above`. But the count is wrong: **11 figure environments, all caption-above** (7 Ch4 + 1 Ch3 TikZ + 1 App A + 2 App C), not 8 — verified by the coordinator's own line-by-line check (caption line precedes graphic line in every one of the 11). The review also contradicts itself (§6.4 says "nine figures"). The `\thesisfigure` macro (`config/floats.tex:42`) puts `\includegraphics` before `\caption` (caption below) but is never used. Fix scope is 11 figures, not 8. Still Major. |
| V2-M12 | CONFIRMED | Ch2:405 "addresses this gap by implementing MacKinnon-White HC3" and Ch1:39 present HC3 as the small-cluster answer; Ch3:346 and Ch5:66 state the distinction correctly. |
| V2-M13 | CONFIRMED | Ch5:158 "Fail to Reject H₀" (baseline joint) directly above Ch5:160 "Reject H₀ (unadjusted; sensitivity only)" (R6) for the same null; prose at L177 resolves it. |

### 2.2 Minor findings (52): 37 CONFIRMED, 15 CORRECTED, 0 REFUTED

Confirmed: m01, m02, m04, m05, m06, m08, m09, m10, m11, m12, m13, m14, m15, m16, m18, m19, m24, m26, m28, m30, m31, m32, m34, m35, m36, m37, m38, m40, m41, m42, m46, m47, m48, m49, m50, m51, m53. (Strongest re-checks: m02 duplicates exact at `abbreviations.tex` ll. 50–51, 53–54, with body counts recomputed DP 1, DPR 9, DY 9, DYR 2; m24 arithmetic 23−14=9 vs stated df 10; m32 register sum recomputed 328.31 MB vs stated 328.30, pages 5,663 exact; m42 "Below screen" with VIF > 5 threshold only in Ch3:361 and full-design Model 1 BVPS 12.32 in the Table 4.8 note; m36/m37 UNVERIFIED labels honest.)

| ID | Verdict | Evidence / correction |
|---|---|---|
| V2-m03 | CORRECTED | Wrong lines — cited 13–15; the unnamed supervisor/chair are at ll. 16, 18. Core true. |
| V2-m07 | CORRECTED | H1/H2 *do* state their model (Category A heading "Model 1" + "in the baseline two-way fixed-effects model"); the real defect is inverted — Ch5 tests them in Model 2 as well. |
| V2-m17 | CORRECTED | Most serious Minor error. Pradhan 2003's Table 2.1 row gives "29 companies, 93 obs" (`chapter_02_literature_review.tex:332`) yet is listed among rows giving "no sample size"; Lamsal/Adhikari give 7-bank counts. True counts: 10 rows lack an observation count, 4 lack any sample size; Kwon 2020 ("N … not stated") is omitted from the list entirely. |
| V2-m25 | CORRECTED | Wrong App D lines — cited 226–235; the ROA codebook row is App D:246. Core true. |
| V2-m27 | CORRECTED | Wrong App D line — cited 248 is the DPS codebook row, not bonus-ratio material. Core true. |
| V2-m29 | CORRECTED | "Never cited or used anywhere" is false. The Merger Bylaws (`nrb2011`) are cited at Ch1:11, Ch2:198, Ch2:200; NRB Banking and Financial Statistics (`nrb2013stats`) at Ch1:11, Ch3:26 — independently re-run by the coordinator. True only for SEBON publications, MoF Economic Survey, and BSD circulars. |
| V2-m33 | CORRECTED | Wrong App D lines — the AEA-invocation sentence is App D:4, not within 6–14. Core true. |
| V2-m39 | CORRECTED | The R7 one-sided implication *is* flagged, at Ch4:480 ("one-sided rescaling of BVPS, not a full bonus-dilution adjustment"); it is only unflagged in Ch3/App D. |
| V2-m43 | CORRECTED | False supporting detail: "(W statistics only in Appendix E)" is wrong — W = 0.925/0.922 also appear at Ch3:364 and Ch4:548. Core claim (EPS–DPS 0.612** and ROA–DPS 0.595** never interpreted) stands. |
| V2-m44 | CORRECTED | Overstated open question. The FE-only classical F(4,16) = 2.23 and the 93.9% dummies-only R² are arithmetically derivable from printed Table 4.9 R²/within-R² values (F = ((0.948−0.919)/4)/((1−0.948)/16) = 2.23; (0.948−0.152)/(1−0.152) = 93.9%), so they do not "require the unrounded analysis output". The other m44 items (interacted-DPS F 2.85; R5/R6 implied-slope SEs/p-values; N = 30/stale-price Fs) genuinely have no table source in Ch4 or App E. |
| V2-m45 | CORRECTED | UNVERIFIED label partly wrong. Recomputed from the printed Table 4.1 values (confirming the review's recomputed column exactly) AND from the Appendix B dataset: EPS SD +63.95% and DPS SD −16.62% reproduce exactly from App B data, ROA mean −46.37% vs thesis −46.38% — three of four are verified rounding artefacts. Only ROA SD +97.49% remains unexplained (App B gives +97.99%, Table 4.1 gives +100.00%; ddof=0 gives +99.09%, N=30 gives +74.44%). |
| V2-m52 | CORRECTED | Line-number slips — the coverage sentences are App C lines 4 and 6, not 5 and 7. Core true (unreferenced; coverage overstatement; no notes). |
| V2-m54 | CORRECTED | `\parskip` is at abstract:14 / ack:13, outside the cited ranges. Core true. |
| V2-m55 | CORRECTED | Correct citation is `main.tex:48, 55–59`, not 59–64. Core true. |
| V2-m56 | CORRECTED | Operative lines are `main.tex:118–119`, not 111–117. Core true. |

Minor precision notes (verdict unchanged, all CONFIRMED): m01's cited range omits the chairperson block (ll. 32–33) and role labels do exist under the dotted lines; m08 conflates "~0.50bn" (Ch1/Ch2) with "496.77m" (Ch3 only); m18's line list includes L332 (Pradhan 2003), whose variables are all in the prose at Ch2:233; s12's "prominent" first occurs at Ch3:29, bullet at Ch3:33–34.

### 2.3 Suggestion findings (20): 19 CONFIRMED, 1 CORRECTED, 0 REFUTED

Confirmed: s01, s02, s03, s04, s05, s06, s08, s09, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20. (Strongest re-checks: s11 zero "ethic" matches in the whole `src/thesis/` tree, re-run; s16 2/32 = 0.0625 exact, thesis reports 0.062 while also stating 2/32 = 0.0625; s01/s02 FOM App. B bare "Date" p.26 and "I hereby corroborate" p.24 confirmed from the extracted guideline.)

| ID | Verdict | Evidence / correction |
|---|---|---|
| V2-s07 | CORRECTED | False premise. The "unexplained" 20-licensed vs 19-listed gap *is* explained in the thesis at `chapter_03_research_methodology.tex:26`: "Of these 20 licensed institutions, 19 are listed on NEPSE \citep{bhandari2026}." — independently re-read by the coordinator. Also cites Ch5:237; the line is 241. |

## 3. Count reconciliation

Recounted from the §10 table rows: **13 Major (M01–M13), 52 Minor, 20 Suggestion, 0 Critical = 85.** Confirmed exact. Minor IDs run m01–m19 and m24–m56 with m20–m23 confirmed absent (zero hits for V2-m20–m23 in the whole review file). No duplicates: 91 distinct scope IDs across 85 consolidated rows, none in two rows. Scope-tally discrepancies: the Ch4 scope's count line ("2 Major, 8 Minor, 3 Suggestion" vs headings 3/8/2) and the Ch2 scope's header ("13 Minor, 2 Suggestion" vs headings 14/1) are both confirmed exactly as §10 states. **One exception:** the §10 header's Ch5 premise is unsupported — no "9 Minor, 4 Suggestion" header/count line exists anywhere in `review_ch5_back.md`; the heading tally (10 Minor, 3 Suggestion) is correct, but the attributed header statement is not in the file. §12.2 line counts (A 346, B 362, C 830, D 287, E 982, F 384; `pass_a_note.md` 61 lines) all confirmed by `wc -l`.

## 4. Criteria verification (§3)

- **FOM 2019 rules R-01–R-20: all CONFIRMED** against per-page `pdftotext` extracts (prefatory order p.9; abstract p.10; five chapters pp.10–15; Ch1 pp.11–12; Ch2 pp.12–13; Ch3 p.13; Ch4 pp.14–15; Ch5 p.15; references pp.15–16; spacing/margins/font pp.20–21; pagination p.21; captions p.21 + App. C pp.27–28; title p.8; ethics pp.5–6; authorship p.24; templates pp.23–26; standard pp.4/7/22). The p.20 spacing self-contradiction (quotations/references in both the 1.5 and single-spacing lists) is real.
- **"FOM 2019 contains no rubric, marking criteria, outcome categories, pass mark, or per-criterion weights": CONFIRMED.** `rubric` 0, `criteria` 0, `pass` 0 hits in the 1,103-line extraction; `outcome` only 2 generic hits; `mark` only "Mark Twain" + "final marks".
- **25% college / 75% FOM viva weighting: CONFIRMED** (FOM p.21, verbatim).
- **Appendix A conditions: CORRECTED.** The review lists 11; FOM p.22 has **12** bullets. The omitted one is college record-keeping (proposal registration/submission/viva dates + topic).
- **Essex proxy: CONFIRMED.** Live PDF checked: reg. 4.1 "Masters by Dissertation (MA or MSc)" + "'Thesis' includes dissertations…"; reg. 4.19 300-word abstract cap; reg. 4.33 (a)–(e) and (k) quoted accurately, including the minor/major correction definitions verbatim. Note: the review omits the lower-award outcomes (f)–(j) from its list — selective, not false.
- **Other §3 claims:** the Birendra/Lumbini/instructions documents are correctly labelled non-governing; APA 6th is correctly identified as the FOM-required style (snippet-only OWL check is honestly labelled as such by the review).

## 5. v1 follow-up verification (§8)

All 20 items CONFIRMED (v1 finding existence and severity confirmed in every case; the quoted current-text states verified against the working tree). Tally recount CONFIRMED: **addressed 8** (F01, F06, F07, F11, F12, F13, F14, F16), **partially addressed 8** (F02, F03, F04, F05, F08, F09, F10, F15), **appears unaddressed 3** (F17, F18, F20), **appears addressed but unverified in execution 1** (F19). V1 metadata confirmed: date 14 Nov 2026, commit `2d195bf` (git-confirmed), 20 findings (1 Critical / 9 Major / 8 Minor / 2 Suggestion). The §8 reading paragraph is fair: F01 is addressed at disclosure level, and the partially-addressed group is indeed dominated by disclosure fixes while table cells (F02/F05/F15) and methods (F03/F08/F10) stay unchanged. Minor line-citation slips only, none verdict-changing: F01 "Ch. V:93–94" is line 93 only and "Ch. III:352" is actually line 351; F05 narrative ":546" is line 545 and "Ch. V:82–83" is line 81; F03 "Ch. IV (~:485)" is vague but line 485 is correct; F07's quote is condensed (omits the −1.658 parenthetical and trailing clause) but verbatim in its quoted core.

## 6. Summary

### 6.1 Tally

| Scope | CONFIRMED | CORRECTED | REFUTED | Total |
|---|---|---|---|---|
| Majors (M01–M13) | 9 | 4 | 0 | 13 |
| Minors (m01–m56) | 37 | 15 | 0 | 52 |
| Suggestions (s01–s20) | 19 | 1 | 0 | 20 |
| **Total numbered findings** | **65** | **20** | **0** | **85** |

**No numbered finding was refuted.** No quoted excerpt was invented or misquoted anywhere in the 85 findings — every excerpt checked matches the thesis file verbatim. The errors are wrong locations, wrong counts, overstated scope, and false sub-claims inside otherwise true findings.

### 6.2 Every hallucination / error found, with specifics

**False sub-claims (the core finding stands, but part of what the review asserts is false):**
1. **M03 / AC-05 / §2.6 Q4 — the 5.577 error (three places).** The review claims Ch1:17 contains the pre-consolidation EPS slope 5.577 and that "the EPS leg does check out from Chapter I alone: 5.577 + (−3.124) = 2.453" (A-03, C-05, AC-05). Ch1 contains no `5.577`/`5.58`/`2.453`/`1.658` anywhere (coordinator re-ran the grep: 0 hits). The EPS leg is *also* unverifiable from Ch1, so the M03 gap is wider than stated — a third abstract figure (5.577) is absent from Ch1, not two. The finding's substance stands (strengthened). §9 Q3 compounds it by attributing 0.100 to the abstract — the abstract never prints 0.100 (it prints implied post −1.658).
2. **m29 — "never cited or used anywhere" is false.** The Merger Bylaws are cited at Ch1:11, Ch2:198, Ch2:200; NRB Banking and Financial Statistics at Ch1:11, Ch3:26. True only for SEBON publications, MoF Economic Survey, and BSD circulars.
3. **s07 — false premise.** The 20-licensed vs 19-listed gap *is* explained at Ch3:26 ("Of these 20 licensed institutions, 19 are listed on NEPSE"). Also cites Ch5:237; the line is 241.
4. **m07 — inverted defect.** H1/H2 *do* state their model (Category A heading "Model 1"); the real defect is the reverse — Ch5 tests them in Model 2 as well.
5. **m39 — already flagged.** The R7 one-sided implication *is* flagged at Ch4:480; only unflagged in Ch3/App D.
6. **m43 — false supporting detail.** "(W statistics only in Appendix E)" is wrong: W = 0.925/0.922 also appear at Ch3:364 and Ch4:548.
7. **S3 (§7 strength) — overstatement.** R6 p = 0.021 is not "always accompanied by the leave-one-bank collapse" (F = 0.615–1.309, p = 0.329–0.572); that range appears only in Ch4 §4.2.6 prose and Ch5:97–102. Holm p = 0.169 + the sensitivity label do accompany every prose appearance.
8. **S1 (§7 strength) — false coverage claim.** "Every headline figure agrees across … Chapter I …" is false: pre-β_E = 5.577, R² = 0.948, and pre-β_B = 0.100 appear in abstract/Ch4/Ch5 but not in Ch1. No numeric disagreement was found anywhere — the error is coverage/attribution, not a wrong number.
9. **§15 "organisations" example — REFUTED.** The word occurs 0 times anywhere in the thesis; the thesis uses American "organizations" 6× in exactly those chapters (Ch1, Ch2, Ch5). The mixed-spelling pattern is real, but this example is backwards.

**Wrong counts:**
10. **M11 / §6.4 — figure count.** "All 8 figure environments" (and "nine figures" in §6.4) are wrong. The true total is **11** figure environments, all caption-above (7 Ch4 + 1 Ch3 TikZ + 1 App A + 2 App C), verified by the coordinator's line-by-line check. The `\thesisfigure` macro (`config/floats.tex:42`) puts caption below but is never used. Fix scope is 11 figures, not 8.
11. **m17 — wrong counts.** True counts: 10 Table 2.1 rows lack an observation count, 4 lack any sample size; Pradhan 2003 ("29 companies, 93 obs") is wrongly listed among rows giving "no sample size"; Kwon 2020 is omitted from the list.
12. **§3.1 Appendix A conditions — 11 listed, 12 in FOM p.22** (omitted: college record-keeping).
13. **m45 — UNVERIFIED label partly wrong.** Three of four percentage changes are verified rounding artefacts (EPS SD +63.95%, DPS SD −16.62% reproduce exactly from App B data; ROA mean −46.37% vs thesis −46.38%). Only ROA SD +97.49% remains unexplained.
14. **m44 — overstated open question.** FE-only classical F(4,16) = 2.23 and 93.9% dummies-only R² are derivable from printed Table 4.9 values; they do not "require the unrounded analysis output".
15. **m51 — UNVERIFIED label resolvable.** Full-tree grep confirms no numeric per-bank-year bonus ratio is printed anywhere in the thesis; the R7 inputs are absent, not merely unverified.

**Wrong locations (core claims true):** M06 (reversal at Ch5:93, not Ch5:100–101); m03 (ll. 16, 18, not 13–15); m25 (App D:246, not 226–235); m27 (cited line 248 is the DPS row); m33 (AEA sentence at App D:4, not within 6–14); m52 (App C lines 4 and 6, not 5 and 7); m54 (abstract:14 / ack:13); m55 (`main.tex:48, 55–59`, not 59–64); m56 (`main.tex:118–119`, not 111–117); F01/F05 line slips in §8 (see §5); M02's FY 2078/79 limb (overstated — RQ3's "exclusion of structural transition periods" fairly covers it; narrow to Kanchan).

**Unsupported / unconfirmed (not numbered findings):** §10 header's Ch5 premise — no "9 Minor, 4 Suggestion" header exists in `review_ch5_back.md`; §15 long-sentence counts 22/28/2 — no counting method reproduces all three (closest 23/27/2), method unpublished, treat as approximate; §3.2 Essex list omits lower-award outcomes (f)–(j) — selective, not false; M06 scale inconsistency (§10.1 Narrow vs A-06 Substantive vs §11 counting it among five substantive Majors).

**Incidental find (not in the review, not a review error):** Table 4.1 prints BVPS post mean 161.97 while the Appendix B rows sum to 161.976 (→ 161.98) — a trivial 0.01 rounding difference, for the author to note.

### 6.3 Does the overall verdict stand?

**Yes.** "Needs major revision — not ready for submission as it stands" still stands. No Major was refuted and no severity needs downgrading: the four corrected Majors (M02, M03, M06, M11) all remain Major after correction. Two corrections strengthen the review's case rather than weaken it (M03's gap is wider than stated — three abstract figures absent from Ch1, not two; M11's fix scope is 11 figures, not 8). The Chapter I framing defects (M01, M02, M04, M05, M06) are all confirmed in substance. One caveat on the verdict's arithmetic: the review says five Majors are substantive (M01, M02, M04, M06, M08), but M06's scale is inconsistent across the review itself (Narrow in §10.1, Substantive in A-06 and §11). Even counting M06 as Narrow, four substantive Majors plus the Chapter I framing problem are enough for "major revision" under the Essex proxy's own definition ("more extensive editorial revisions… re-writing of substantial parts of the thesis"), so the verdict is unaffected. The blocking set is unchanged: all 13 Majors, with M03's blocking item 13 corrected to also add the pre-EPS slope (5.577) and the implied post slopes to Chapter I.

### 6.4 What the audit confirms is strong in the v2 review

The criteria work is solid (all 20 FOM rules verified page-by-page; the "no rubric" claim verified by zero-hit search; the Essex proxy verified against the live PDF). The verification log is accurate (HEAD, diff stat, git status, and all 14 re-run spot-checks confirmed). The counts are exact (0/13/52/20 = 85, no duplicates). The v1 follow-up is accurate in all 20 items. The Pass A comparison, the inventory, and the citation cross-check (72/72/299/0) all reproduce exactly. The strengths that were re-checked are real (cov-sensitivity table, Ch1 Limitations numbers, App D register arithmetic, the 15/19 synthesis counts). No quoted excerpt in the 85 findings was invented or misquoted.

## 7. What could not be verified (and why)

- The 15-reference sample verification in §4.1 (13 fully confirmed, 2 partial) was not re-run: it requires opening external publisher/DOI/library sources. The Counts verifier confirmed the scope file's §6.2 table is 15 rows = 13 VERIFIED + 2 PARTIAL and that the every-6th-entry positions in `.bib` order verify exactly — so the sample's structure is verified, but the external confirmations themselves were not re-opened.
- The S6 code leg (R1–R9 match `robustness.py`; HC3 pre-specification real) and the S8 reference-sample leg were not re-run (noted by the Criteria verifier); only the price/integrity legs were spot-checked.
- This audit is a coordinator-consolidated verification: each finding was verified by an assigned verifier against the primary source, and the coordinator independently spot-checked the consequential corrections (M03, M11, m29, s07, m17, the abstract figures, S1, S3, the floats macro, the §10 count). The coordinator did not re-verify every Minor/Suggestion excerpt character-by-character itself; it relied on the verifiers' reports, which record file, line, and exact excerpts.
- Rendered output, figure pixels, and anything requiring a build remain unverified (no build, per the task) — as in the v2 review itself.
