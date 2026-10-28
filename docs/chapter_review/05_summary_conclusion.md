# Chapter 5 review: Summary, Conclusion, and Implications

- Chapter reviewed, in full: `docs/draft/thesis/chapter_05_summary_and_conclusion.md` (174 lines), repo HEAD `9a46350`.
- LaTeX counterpart, spot-checked only: `src/thesis/chapters/chapter_05_summary_and_conclusion.tex`.
- Evidence sources used: `docs/draft/thesis/chapter_01_introduction.md` (research questions, objectives, hypotheses), `docs/draft/thesis/chapter_03_research_methodology.md`, `docs/draft/thesis/chapter_04_results_and_discussion.md`, and `data_analysis/analysis/outputs/tables/T3_model1.md`, `T4_model2.md`, `T5_robustness.md`.
- This review changes nothing in the thesis. It is a review file only.
- Line numbers below are lines of the Markdown Chapter 5 unless stated otherwise. Every issue is quoted verbatim.

## Passes run (loop, as assigned)

- **Pass 1 — full read:** does the summary restate Chapter 4 faithfully, does the conclusion follow from Chapter 4 (including the sensitivity-dependent Wald result), and do recommendations and future work follow from actual limitations or introduce new claims?
- **Pass 2 — line-by-line proofread:** grammar, duplicated words, broken sentences, inconsistent terms. Method actually used: full read plus a scripted duplicate-word scan (no duplicated word found) and a trailing-space scan.
- **Pass 3 — every number:** every number restated in Chapter 5 checked against Chapter 4 and tables T3/T4/T5, plus an independent recomputation of the descriptive means, standard deviations, and percentage changes from `data_analysis/data_extract/output/manual_review/mps_rd_joined_panel.csv` (clean sample, gap ≤ 5 days, n = 28).
- **Pass 4 — objective-by-objective:** each Chapter 1 research question, specific objective, and hypothesis checked against what Chapter 5 actually says, with quotes on both sides.
- **Pass 5 — slop hunt:** meta comments, filler, verbatim repetition of Chapter 4, generic concluding praise, deletable sentences. Method actually used: full read plus a normalised long-sentence comparison of Chapter 5 against Chapter 4 (no long sentence copied verbatim; see Pass 5).
- **Pass 6 — LaTeX sync (spot-check only):** the passages flagged in this review were grepped in the `.tex` file. This is NOT a full LaTeX diff, and it is not claimed as one.

## Verdict

Chapter 5 is numerically faithful to Chapter 4 and to tables T3, T4, and T5, and its headline conclusion — that the regime-shift evidence is sensitivity-dependent, not conclusive in the baseline — is stated correctly. It is **not yet submittable as written**, for three substantive reasons, not for its arithmetic:

1. It says the robustness suite "verified parameter stability" (line 81), when the suite's own headline sensitivity, R6, rejects stability. That sentence contradicts the chapter's own correct R6 paragraph and its own correct conclusion in section 5.3.1.
2. It never names hypotheses H1–H4 and never states their decisions, although Chapter 1 sets them and Chapter 4 decides them. A conclusion chapter that leaves the hypothesis loop unclosed by name is incomplete.
3. It introduces at least one new factual premise with no source in Chapters 1–4: that public dissemination "remains dispersed across corporate websites and print media" (line 124).

Fix the numbered list at the end in priority order. Everything else in this review is minor wording or explicitly confirmed correct.

## Pass 1 — faithfulness of summary, conclusion, recommendations

### Correct: the sensitivity-dependent conclusion

Chapter 5 states the central qualification correctly, twice, and in the same terms as Chapter 4 (Chapter 4, line 421, in substance: baseline suggestive, R6 significant, association not causal effect). Chapter 5, line 95:

> "In the baseline model, the joint test does not reject structural stability at the 5% level ($F = 2.954, p = 0.085$). However, after excluding the entity-mismatch fiscal year (Specification R6), the joint test rejects parameter stability at the 5% level ($F = 5.82, p = 0.021$). The evidence for a regime shift is therefore sensitivity-dependent rather than conclusive in the baseline; it is documented as an empirical association across calendar periods, rather than as an established causal merger impact."

That passage is correct and must not be weakened or strengthened. The same qualification is correctly repeated in the R6 paragraph, line 84:

> "While the individual interaction coefficient is not significant at 10% under Student's $t(10)$, the joint test indicates that excluding the transition mismatch reveals a statistically significant joint structural difference across the calendar regimes."

### Correct: no causal merger claim is made from the regressions

Chapter 5 never says the mergers caused the slope changes. It says "coinciding with" (line 67), "plausible economic interpretation" (line 98), and "empirical association" (line 95). That restraint matches Chapter 4's own framing and is a strength of the chapter, not a gap.

### Correct: BAFIA operationalisation is not overstated here

Chapter 5, line 44:

> "Section 59(2) of the Banks and Financial Institutions Act, 2017 (BAFIA) legally mandates that commercial banks publish their audited annual balance sheets and profit and loss accounts within nine months into the subsequent fiscal year—operationalized at the end of Chaitra (mid-April) of the subsequent fiscal year."

This does not claim the statute names Chaitra. That distinction was a known earlier correction, and Chapter 5 preserves it.

### Correct: recommendations and future work are, with one exception, proposals, not disguised findings

Policy recommendations (section 5.5.1) and future-work items (section 5.5.2) are framed as "should" proposals. That is legitimate for a conclusion chapter. The one exception is the factual premise flagged as MUST-FIX M3 below (line 124). The DiD proposal, the long-horizon proposal, and the intraday proposal introduce no result claim; they are directions, and they are not counted as errors for being unestimated.

## Pass 3 — numbers (checked, with recomputation)

All headline numbers in Chapter 5 match Chapter 4 and tables T3/T4/T5 exactly. No coefficient, standard error, t-value, p-value, R-squared, or Wald statistic in Chapter 5 differs from its table. Checked in full:

- Model 1 (Chapter 5, line 73; T3): EPS 2.095 (SE 4.096, t = 0.51, p = 0.616, df 16); BVPS 0.219 (SE 1.858, t = 0.12, p = 0.908); R-squared 0.948, adjusted 0.912.
- Model 2 (Chapter 5, lines 76–79; T4): pre-EPS 5.577 (SE 3.560, t = 1.57, p = 0.140); pre-BVPS 0.100 (SE 1.306, t = 0.08, p = 0.940); delta-E −3.124 (SE 4.003, t = −0.78, p = 0.448); delta-B −1.758 (SE 1.231, t = −1.43, p = 0.175); post-EPS 2.453 (t = 1.08, p = 0.298); post-BVPS −1.658 (t = −1.48, p = 0.161); joint Wald F(2, 14) = 2.954, p = 0.085.
- R6 (Chapter 5, lines 82–84; T5): F(2, 10) = 5.82, p = 0.021, n = 23, delta-B −2.611 (SE 1.517, t = −1.72, p = 0.116).
- R4 residual df = 13 (Chapter 5, line 81; T5 note: df 14 → 13). Correct.
- Pooled comparison (Chapter 5, lines 74, 86; Chapter 4, Table 4.8): pooled EPS 4.882, R-squared 0.136, t = 1.58, p = 0.126; two-way FE R-squared 0.948. Correct.
- Correlations (Chapter 5, lines 70–71; Chapter 4, Table 4.2): EPS–ROA r = 0.975, p < 0.01; EPS–BVPS r = 0.372, p = 0.051; VIF = 1.16 for both EPS and BVPS (Chapter 4, lines 310–311). Correct as values; see MINOR-2 on the word "exactly".
- Sample and degrees of freedom (Chapter 5, lines 46, 51, 54): 28 clean of 30 intended, 13 pre, 15 post; HBL FY 2077/78 54 days late, NIMB FY 2077/78 47 days late; Model 1 df 16, Model 2 df 14. Correct.
- Descriptive means and standard deviations (Chapter 5, lines 65–68), independently recomputed from the joined panel: price pre 310.59 (SD 119.46), post 205.60 (SD 33.45); EPS pre 17.90 (SD 3.99), post 10.72 (SD 6.53); BVPS pre 158.11, post 161.97; DPS pre 6.06, post 1.40, 12 of 15 post years zero. All match.
- Percentage changes (Chapter 5, lines 65–68): 33.80%, 40.11%, 63.66% (EPS SD), 2.44%, 76.90%. These reproduce exactly from Chapter 4's rounded means and SDs, and Chapter 5 introduces no drift relative to Chapter 4. Transparency note, not an error: computed from unrounded panel values, the same changes are −33.81% (price mean), −40.13% (EPS mean), and +63.95% (EPS SD). The largest gap, 0.29 percentage points on the EPS SD change, is a rounding-of-inputs artefact shared with Chapter 4, not a Chapter 5 mistake. No fix is required unless the author wants one consistent rounding rule stated in Chapter 4.
- "32 to 20" (Chapter 5, line 116): Chapter 3, line 30, gives the dated version — "from an apex of 32 institutions in FY 2011/12 to 20 commercial banks by mid-October 2023 (Asoj 2080 BS) (NRB, 2023)". Chapter 5 compresses out the dates. That compression is not a wrong number, and it is not flagged as an error.
- NMB Kanchan note (Chapter 5, line 42): "adding approximately NPR 0.57 billion to share capital in FY 2077/78". Consistent with the Chapter 3 account of the August 2020 acquisition. No discrepancy found.

No number drift was found in Chapter 5. The MUST-FIX items below are about strength of claim and completeness, not arithmetic.

## Pass 4 — objective-by-objective check

### Research questions (Chapter 1, lines 37–41)

**RQ1 — "Are fundamental accounting measures—specifically earnings per share (EPS) and book value per share (BVPS)—statistically associated with post-reporting-deadline market share prices ($\\mathit{MPS}^{RD}$) among the selected Nepalese commercial banks?" — ANSWERED, with a negative answer at 5%.**

Chapter 5, line 74, gives the answer, even though it does not label it RQ1:

> "Both coefficients were positive, consistent with valuation theory, but neither was statistically significant at the 5% level once macro-year price movements were absorbed by $\\lambda_t$."

That is the correct answer to RQ1 under Model 1. The pooled specification is also insignificant (line 86: t = 1.58, p = 0.126), so the negative answer is not an artefact of fixed effects alone, as Chapter 4 also states.

**RQ2 — "Did the estimated valuation associations of EPS and BVPS with market share prices differ significantly between the pre-consolidation period (FY 2076/77–2078/79) and the post-consolidation period (FY 2079/80–2081/82)?" — PARTIALLY ANSWERED, honestly qualified.**

Chapter 5, line 95 (quoted in full in Pass 1): baseline does not reject at 5% (F = 2.954, p = 0.085); R6 rejects at 5% (F = 5.82, p = 0.021); evidence is "sensitivity-dependent rather than conclusive in the baseline". That is the correct, complete answer available from the data. "Partially" here is not a criticism of Chapter 5; it is the state of the evidence. Chapter 5 must not be edited to make this a clean yes or a clean no.

**RQ3 — "Are the baseline and consolidation-interaction findings robust to alternative operating profitability specifications, inclusion of eligible dividend disclosures, adjustment for bonus share capitalization, retrospective earnings restatements, and the econometric exclusion of structural transition periods?" — ANSWERED.**

Chapter 5, lines 81–84, covers all six elements named in Chapter 1's RQ3 and specific objective 3: ROA substitution (R3), DPS inclusion (R4), transition-year exclusion (R5), entity-timing exclusion (R6), bonus adjustment (R7), restated EPS (R8). The R6 result is reported separately and correctly. The wording fault in line 81 is about the word "verified", flagged as MUST-FIX M1; it does not make RQ3 unanswered.

Chapter 5's own restatement of the questions, lines 30–32, matches Chapter 1's questions, with one harmless compression: Chapter 5's question 3 lists "dividend exclusions" where Chapter 1 says "inclusion of eligible dividend disclosures". In context (R4 adds DPS), the meaning is clear, and it is not flagged as an error.

### Specific objectives (Chapter 1, lines 49–61)

1. **Baseline value relevance (Model 1, two-way FE, MPS-RD)** — DONE and reported (Chapter 5, lines 73–74).
2. **Test whether slopes differed pre/post via interactions and joint Wald test** — DONE and reported with the sensitivity qualification (Chapter 5, lines 76–79, 95).
3. **Robustness across ROA, DPS, transition-year exclusion, entity-timing exclusion, bonus adjustment, restated EPS** — DONE and reported (Chapter 5, lines 81–84).

### Hypotheses (Chapter 1, lines 69–96) — NOT CLOSED BY NAME IN CHAPTER 5

Chapter 1 defines, two-tailed at 5%:

- H1: EPS associated with price in Model 1 (null: beta-E = 0).
- H2: BVPS associated with price in Model 1 (null: beta-B = 0).
- H3: EPS slope differs pre/post (null: delta-E = 0).
- H4: BVPS slope differs pre/post (null: delta-B = 0).
- Joint null: delta-E = delta-B = 0.

Chapter 4 decides all of them (Chapter 4, lines 229–234): H1 fail to reject (Model 1 p = 0.616; Model 2 pre p = 0.140), H2 fail to reject (p = 0.908; pre p = 0.940), H3 fail to reject (p = 0.448), H4 fail to reject (p = 0.175), joint baseline fail to reject (p = 0.085), joint R6 reject (p = 0.021).

Chapter 5 never uses the labels H1, H2, H3, or H4 anywhere (grep over both the Markdown and the LaTeX chapter returns no match), and never writes a sentence of the form "H1 is not rejected". A reader can infer the decisions from the p-values in section 5.2.3, but inference is not closure. This is MUST-FIX M2: add one short hypothesis-decision paragraph or table in section 5.3, stating fail-to-reject for H1–H4 and for the joint baseline test at 5%, and reject for the joint test only under R6, with the sensitivity qualification already in line 95.

## MUST-FIX issues

### M1. "Verified parameter stability" contradicts the chapter's own R6 result (line 81)

Chapter 5, line 81:

> "The robustness suite (R1–R8) verified parameter stability across ROA substitution (R3), cash dividend inclusion (R4, residual $\\text{df} = 13$), transition-year removal (R5), bonus share dilution (R7), and restated basic earnings (R8)."

Why this is wrong, not just loose: (a) failure to reject a null in R3, R4, R5, R7, and R8 does not verify stability — it is absence of rejection at 5% in small samples (n = 28, and n = 23 for R5); (b) the suite as a whole does not verify stability, because R6, in the same suite and the very next paragraph, rejects stability at 5% (F = 5.82, p = 0.021). A reader who stops at line 81 takes away the opposite of the chapter's conclusion. Fix: replace "verified parameter stability" with "did not reject parameter stability at the 5% level" and add "except under R6, reported below" — or delete the sentence and let the R6 paragraph carry the suite's message. This wording also appears in the LaTeX chapter (line 97 of the `.tex` file), so fix both versions.

### M2. Hypotheses H1–H4 are never decided by name in Chapter 5

Evidence: Chapter 1, lines 69–96, defines H1–H4 and the joint null; Chapter 4, lines 229–234, decides them; Chapter 5 contains no occurrence of H1, H2, H3, or H4. Fix: add an explicit decision statement in section 5.3 (a paragraph or a small table): H1 fail to reject, H2 fail to reject, H3 fail to reject, H4 fail to reject, joint baseline fail to reject at 5% (p = 0.085), joint R6 reject at 5% (p = 0.021, sensitivity-dependent). Do not change any decision; only state the decisions Chapter 4 already made.

### M3. New factual premise about dissemination channels, with no source in Chapters 1–4 (line 124)

Chapter 5, line 124:

> "Under Section 59(2) of BAFIA, commercial banks are legally mandated to publish audited financial statements within nine months into the subsequent fiscal year. However, public dissemination remains dispersed across corporate websites and print media."

The BAFIA sentence is correct. The second sentence is a new factual claim about how dissemination currently works. A grep of Chapters 1, 3, and 4 for "dispersed", "print media", "corporate websites", "centralized electronic", and "digital filings" returns no supporting passage. The recommendation that follows (a centralised portal) is legitimate as a proposal, but its premise must not be presented as an established fact without a source. Fix, in either order: cite a source for the dissemination claim, or reword the premise as a proposal ("Dissemination should be consolidated into a single portal") without asserting the current state. The same passage appears in the LaTeX chapter (line 143 of the `.tex` file), so fix both versions.

### M4. "Universally" overstates Chapter 1's literature claim (line 24)

Chapter 5, line 24:

> "Prior studies universally employed static, full-sample pooled regressions, implicitly assuming parameter stability and failing to test whether corporate combinations altered valuation multiples across the pre- and post-consolidation regimes (Chaudhari, 2025; Chhetri, 2023; Gurung & Dahal, 2025; Timalsina, 2026);"

Chapter 1 does not say "universally". It says "almost exclusively focused on static, sample-average regressions" (Chapter 1, line 13) and "Almost all published Nepalese studies employ pooled OLS or static panel regression designs" (Chapter 1, line 26). "Universally" claims every prior study, which the four citations do not prove and Chapter 1 does not claim. Fix: change "universally" to "almost all", matching Chapter 1. This also appears in the LaTeX chapter (line 23 of the `.tex` file), so fix both versions.

## MINOR issues

### MIN-1. Point-estimate reading stated as investor behaviour (line 76)

Chapter 5, line 76:

> "Equity investors primarily priced current earnings rather than historical book assets."

Both slopes in that bullet are statistically insignificant (pre-EPS p = 0.140, pre-BVPS p = 0.940), and no test of the difference between them is reported. The point estimates (5.577 vs 0.100) do show that pattern, but the sentence as written states it as observed behaviour. Fix: qualify it — "On point estimates, earnings carried the larger pre-consolidation slope, although neither slope was significant at 5%." The same sentence appears in the LaTeX chapter (line 90 of the `.tex` file), so fix both versions if changed.

### MIN-2. "Exactly" overstates VIF precision (line 71)

Chapter 5, line 71:

> "with variance inflation factors of exactly $\\text{VIF} = 1.16$, confirming that multicollinearity between EPS and BVPS is negligible."

The value 1.16 is correct to two decimals (Chapter 4, lines 310–311; 1 / (1 − 0.372²) = 1.16). "Exactly" implies exactness the two-decimal figure does not carry. Fix: delete "exactly". The conclusion ("negligible") is correct and does not change.

### MIN-3. "Established" overstates the conclusion heading (line 92)

Chapter 5, line 92:

> "Based on the empirical findings, econometric diagnostics, and theoretical evaluations conducted in this dissertation, four major conclusions are established:"

Given that the headline conclusion is sensitivity-dependent and every slope is insignificant at 5% in the baseline, "established" is stronger than the chapter's own qualification in line 95. Fix: change to "four major conclusions are drawn" or "the following conclusions follow, subject to the sensitivity qualification in section 5.3.1". The same wording appears in the LaTeX chapter (line 110 of the `.tex` file), so fix both versions if changed.

### MIN-4. "Minimum" contradicts "ceilings" in the trading-halt recommendation (lines 122, 158)

Chapter 5, line 122:

> "restricting trading halts to a minimum of a few sessions around share swap execution."

Chapter 5, line 158:

> "The Securities Board of Nepal and NEPSE should establish regulatory ceilings that restrict secondary market trading halts during corporate combinations to a minimum number of consecutive trading sessions around formal share swap execution."

A ceiling is a maximum, not a minimum. The intended meaning (halts should last at most a few sessions) is clear from context, but line 158 literally says the opposite instrument. Fix: change "minimum" to "maximum" in line 158, and clarify line 122 to "to at most a few sessions". Line 158 also appears in the LaTeX chapter (line 182 of the `.tex` file), so fix both versions.

### MIN-5. "Cross-sectional difference-in-differences" is a terminology slip (line 168)

Chapter 5, line 168:

> "Future studies should expand the cross-sectional sample to encompass all 20 surviving commercial banks on NEPSE, employing cross-sectional difference-in-differences (DiD) frameworks that compare aggressively merged banking series against a larger cohort of organically grown or minimally consolidated peer institutions."

Difference-in-differences is a panel (before/after by group) design, not a cross-sectional one. "Expand the cross-sectional sample" is fine on its own; "cross-sectional DiD" is not. Fix: delete "cross-sectional" before "difference-in-differences", or write "panel DiD". The same sentence appears in the LaTeX chapter (line 193 of the `.tex` file), so fix both versions if changed.

### MIN-6. Trailing space, line 19

Line 19 ends with a trailing space after "clean-surplus accounting relation." Typographic only. Delete it.

### MIN-7 (optional, not counted as an error). R7 timing note is in Chapter 3 but not repeated in the T5 note

Chapter 5 does not discuss R7 timing, and the T5 note still reads only "BVPS adjusted for bonus issues: BVPS_adj = BVPS / (1 + bonus%)". The pro-forma forward nature of that adjustment is disclosed in Chapter 3, so this is not a Chapter 5 error. If the author wants the table to stand alone, one clause could be added to the T5 note. No change is required for Chapter 5 to pass on this point.

## Pass 2 — proofread (what was actually checked)

- No duplicated word found by scan of all 174 lines.
- No broken or unfinished sentence found. All numbered and bulleted lists in sections 5.2–5.5 are complete and parallel in form.
- Terms are consistent throughout the chapter: MPS-RD, pre/post-consolidation periods, R1–R8 labels, and the 5-day freshness rule are used with the same meanings as in Chapters 3 and 4.
- Two genuine proofread faults found, both listed above: MIN-4 (minimum/maximum) and MIN-6 (trailing space). The "cross-sectional DiD" slip (MIN-5) is a terminology fault, not a typo.
- Not flagged as errors: "mid-FY 2079/80" (line 5) — January–February 2023 falls inside FY 2079/80, so "mid-FY" is acceptable; "landmark" (line 5), "monumental" (line 23), "aggressive" (line 65) — evaluative adjectives, but each attaches to a sourced or quantified claim in the same sentence or paragraph, so they are not empty praise.

## Pass 5 — slop hunt

- **No meta comments found.** Chapter 5 contains no "as an AI", no drafting notes, no "in this section I will", and no placeholder text.
- **No verbatim Chapter 4 paragraph copied.** A normalised long-sentence comparison of Chapter 5 against Chapter 4 returned no long sentence copied verbatim. Numbers necessarily repeat between a results chapter and a summary chapter; that repetition is the summary's function, not slop, and it is not flagged.
- **Repetition that is structural, not slop:** section 5.3.1 restates the Model 2 numbers already given in section 5.2.3 (pre-EPS 5.58, pre-BVPS 0.10, post 2.45 and −1.66, Wald 2.954/5.82). That is what a conclusions section is for, and the restatement adds the sensitivity qualification. Not flagged.
- **Generic praise, checked and mostly cleared:** "four major conclusions are established" (line 92) is flagged as MIN-3 for overstrength, not for being generic. "This dissertation demonstrates the importance of rigorous econometric modeling" (line 146) is a summary claim that the chapter's own HC3/fixed-effects discussion supports; it is not empty praise and is not flagged.
- **Deletable filler, minimal:** the transition sentence in line 163, "While this dissertation has established an econometric baseline for evaluating accounting value relevance across the 2023 consolidation wave, several fruitful avenues remain open for future scholarly research:", is a standard section transition. It carries no new claim and could be deleted with no loss, but deleting standard transitions is a style choice, not a quality failure. It is recorded here so the author can decide, and it is not in the fix list.
- **Interpretations correctly labelled as interpretations:** line 98 ("A plausible economic interpretation is that…"), line 95 ("empirical association… rather than as an established causal merger impact"), and the "coinciding with" wording in lines 67 and 114 keep mechanisms (asset quality, provisioning, capital retention) at the level Chapter 4 assigns them — plausible mechanisms, not estimated effects. Chapter 5 does not upgrade any Chapter 4 mechanism into a finding. That restraint is correct and should be preserved in any edit.

## Pass 6 — LaTeX sync (spot-check only)

Every flagged passage was found in the LaTeX chapter at the lines noted in each issue (M1: `.tex` line 97; M3: `.tex` line 143; M4: `.tex` line 23; MIN-1: `.tex` line 90; MIN-3: `.tex` line 110; MIN-4: `.tex` line 182; MIN-5: `.tex` line 193). No flagged passage is Markdown-only. This is a spot-check, NOT a full LaTeX diff: unflagged passages were not compared line by line, and LaTeX-only errors, if any, are in the NOT-checked section below.

## Passages confirmed correct (brief, as assigned)

- Section 5.1 organisation (lines 7–11): four sections, matching sections 5.2–5.5 as written. The Tribhuvan University guidelines citation (2019, p. 15) was not verified against the guideline document itself; see NOT-checked.
- Methodology synthesis (lines 40–56): six years, five series, four merged plus NMB benchmark, NMB Kanchan note, BAFIA operationalisation, 5-day rule, 28/13/15, both model equations, df 16 and 14, HC3-t inference. All correct against Chapters 3 and 4.
- Descriptive, correlation, Model 1, Model 2, R6, and pooled numbers: all correct (Pass 3 above).
- Conclusion 5.3.2: the non-observation of the book-value substitution is correctly tied to an insignificant negative point estimate (p = 0.161) and labelled a plausible interpretation, not a finding.
- Conclusion 5.3.4: R6 significance and the 54/47-day suspensions are correctly stated, and the "must anchor to statutory mandates" prescription follows from the chapter's own design rather than from a new result.

## Fix list, in priority order

1. **M1 — line 81:** replace "verified parameter stability" with a non-rejection wording and a pointer to R6. Both Markdown and LaTeX.
2. **M2 — section 5.3:** add an explicit H1–H4 and joint-test decision paragraph or table (all fail to reject at 5% in the baseline; joint test rejects only under R6). Both versions.
3. **M3 — line 124:** cite a source for "dispersed across corporate websites and print media", or reword the premise as a proposal. Both versions.
4. **M4 — line 24:** change "universally" to "almost all". Both versions.
5. **MIN-1 — line 76:** qualify "primarily priced" as a point-estimate pattern, noting neither pre slope is significant. Both versions.
6. **MIN-2 — line 71:** delete "exactly" before VIF = 1.16.
7. **MIN-3 — line 92:** change "are established" to "are drawn" (or equivalent qualified wording). Both versions.
8. **MIN-4 — lines 122, 158:** change "minimum" to "maximum"/"at most a few sessions" in the trading-halt recommendation. Both versions for line 158.
9. **MIN-5 — line 168:** delete "cross-sectional" before "difference-in-differences". Both versions.
10. **MIN-6 — line 19:** delete the trailing space.

## NOT checked (stated plainly, never to be misread as checked)

- Full LaTeX diff between the Markdown and LaTeX Chapter 5 (spot-check only, Pass 6).
- Re-fitting Models 1 and 2 from the raw panel in this review. Numbers were checked against tables T3/T4/T5, Chapter 4, and an independent descriptive recomputation from the joined panel; the OLS/HC3/Wald refit itself was not redone here.
- Chapters 1–4 in full. Only the passages cited above (Chapter 1 questions/objectives/hypotheses, Chapter 3 population and design passages, Chapter 4 tables and hypothesis decisions) were read for this review.
- Bibliography entries for citations appearing in Chapter 5 (Bhattarai 2014; Pradhan & Dahal 2016; Timalsina 2026; Ohlson 1995; Feltham and Ohlson 1995; Collins et al. 1997; Ball & Brown 1968; Beaver 1968; MacKinnon-White 1985, and others). Citation accuracy was not verified in this review.
- The Tribhuvan University Master's Degree Dissertation Guidelines (2019, p. 15) claim in line 7, against the guideline document itself.
- The NRB 32-to-20 population history beyond Chapter 3's citation (NRB, 2023); Chapter 5's compressed version was checked only for consistency with Chapter 3.
- Rendered PDF output, figure files, and table files other than T3, T4, and T5.
- Whether future-work proposals (20-bank DiD, intraday event study, ESG, cross-sectoral work) are feasible with available NEPSE data. They are assessed here only as proposals, not as claims.
- Any thesis file outside Chapter 5 and the evidence sources listed at the top. Nothing was edited, moved, or deleted.

## LOOP ADDENDUM (2026-10-28, 10-pass loop, see 07_loop_log.md)

- Chapter 5 contains ZERO mentions of "Hypothesis" at all
  (grep-confirmed). Must-fix item 8 stands, stronger.
- New minor/must-fix item 17: section 5.2.2 "during merger
  processes" for the April 2022 suspensions — reword to
  "merger-related suspension" (HBL/NIB merger rejected
  Jan 2022).
- Chapter 5 "largest share of market capitalization"
  citation to Bhattarai (2014) is unsafe: Bhattarai does
  not establish that claim (see 02 addendum). Narrow or
  drop that citation from the sentence.
