# Thesis chapter content review vs TU FOM Dissertation Guidelines 2019 — gap file

> **FIX APPLICATION RECORD (2026-11-02).** The must-fix and minor items
> below were applied to the LaTeX thesis and verified in a clean build
> (zero overfull boxes). Item by item:
> - **A1** — VIF unified to "approximately 20" in Chapters 1, 3, 4, and 5.
>   Exact panel r(EPS, ROA) = 0.9747 gives VIF = 19.98; the printed
>   r = 0.975 gives 20.25; "approximately 20" is correct under both.
> - **A2** — Appendix C intro, body text, and caption now say seven
>   specifications (R1, R2, R4--R8) with the R3 omission stated, matching
>   the figure and its generation code.
> - **A3** — Appendix A "independently archived by Merolagani" removed;
>   now "archived by the Merolagani aggregator", consistent with the
>   thesis's non-independence disclosures.
> - **A4** — Chapter 2 "universally" → "almost all".
> - **A5** — Chapter 5 section 5.1 now states the guideline's three-section
>   structure (p. 15) and discloses the four-section adaptation as a
>   separation of the guideline's Implications material.
> - **B** — Table 2.1: a Methodological Critique column was added, carrying
>   only the tags already present in the Core Empirical Findings cells
>   (nothing invented); the unsourced Kwon "(1998–2014)" and Bhandari
>   "(2015–2024)" periods were removed from the Sample & Period cells;
>   Gurung & Dahal prose "ten-year" corrected to "eleven-year" (110 obs =
>   10 banks x 11 FYs, consistent with the table); an exclusion sentence
>   for bhattarai2024, dongol2024, adhikari2023cbr, and niraula2026 was
>   added to the selection paragraph; the note now defines EY = earnings
>   yield and MTB = market-to-book ratio (verified against the Dahal et
>   al. 2025 paper, NepJOL 75407) and states that observation counts are
>   shown where the underlying study reports them.
> - **C** — Chapter 2's announcement-registry claim is now hedged to the
>   disclosures examined for this study; Chapter 3's "standard Nepalese
>   banking valuation convention" sentence was reworded to the regulatory
>   return framework; Chapter 1 "unverifiable" → "ineligible"; Chapter 5
>   "universal population" → "licensed commercial bank population".
> - **D** — the four hardcoded section cross-references were converted to
>   \ref (labels added at 3.3.4, 4.2.6, 4.2.7); Table 9 note "correct
>   parameter count" → "model's parameter count"; "Addressed via HC3" →
>   "Mitigated via HC3".
>
> **Deliberately not done:** the generated analysis assets (e.g. the
> "~ 30" note in t2_correlations.py) and the Markdown Table 2.1 remain
> untouched — the LaTeX tables are the submission artifact and the
> Python/Markdown versions are legacy per the author's instruction; the
> figure assets were not regenerated (the "T5" tag printed inside the A2
> asset remains an asset-side artifact; the thesis Note below the figure
> restates the R3 omission). Observation counts for six Table 2.1 rows
> and the Lamsal years/count still require the papers themselves and
> remain pending, as does the Markdown-LaTeX sync.

Thesis: VALUE RELEVANCE OF ACCOUNTING INFORMATION BEFORE AND AFTER THE
BANKING CONSOLIDATION WAVE: EVIDENCE FROM NEPALESE COMMERCIAL BANKS.
Repo state at review time: working tree of HEAD 7b6bd07 (thesis chapters
unmodified; only src/proposal files carry uncommitted edits).
Review scope, per the author's instruction: chapter CONTENT conformance
against the Master's Degree Dissertation Guidelines 2019 (structure,
required sections, content obligations) plus everything about the
chapters themselves — internal consistency, number fidelity, and the
open items carried from the Phase 2 review (`00_overall_verdict.md`)
and its two fix-verification rounds (`docs/finalized/07`, `08`).
Files changed to write this review: NONE, except this file.
A compiled-PDF pass was NOT possible: `src/build/thesis/` was deleted
mid-review (by the author); page-span checks against the guideline
length guides must be re-run on the next build.

## How this review was run

Guideline pages 10-15 (chapter content obligations) and page 9/20/21
(prefatory order, spacing, typography) were extracted and checked
section by section against the five chapter .tex files, read in full.
Every headline number in Chapters 1, 4, and 5 was recomputed or
checked against the audited values from the Phase 1/Phase 2 loops
(T1-T6, panel CSV, verified regression set). Figure notes were checked
against the generation code. Bibliography keys were checked against
`references.bib`. Table 2.1 rows were re-verified against the round-2
verification findings.

## One-line verdict

The chapter content is in strong, submittable shape: all 17 Phase 2
must-fix items are verified applied in the current LaTeX, no recomputed
number disagrees with its source, and every guideline-required chapter
section exists. What remains is one leftover number inconsistency in
Chapter 1, two appendix descriptions that contradict the thesis's own
disclosures or its figure code, one self-contradicting "universally"
in Chapter 2, one misstated conformance claim in Chapter 5, the
carried-over Table 2.1 completion job, and small wording nits.

## Guideline conformance matrix (guideline pp. 11-15)

| Chapter | Guideline requires | Thesis has | Status |
|---|---|---|---|
| I Introduction | Background; Problem statement (ends in research questions); Objectives (general + specific, action verbs); Hypotheses (if any); Rationale; Limitations (scope vs limitations distinguished) | 1.1 Background; 1.2 Problem statement ending in RQ1-RQ3; 1.3 Objectives (general + specific, action verbs); 1.4 Hypotheses H1-H4 with H0/Ha, two-tailed alpha = 0.05; 1.5 Rationale and Significance; 1.6 Limitations with explicit scope/limitation distinction; plus 1.7 Organization of the Study (extra, standard) | CONFORMS |
| II Literature Review | Introduction linking Ch. I + organization overview; theoretical review; empirical review; government policy/regulation; gap established with evidence; APA | 2.1 Introduction with link + four-section overview; 2.2 Theoretical (RIV, M&A dynamics, dividend models, signaling/agency, EMH/PEAD, P/E circularity); 2.3 Legal/regulatory/policy Nepal; 2.4 Empirical (international, foundational, recent, consolidation-wave, synthesis Table 2.1); 2.5 Research Gap (five evidenced gaps) | CONFORMS |
| III Methodology | Introduction; (i) design; (ii) population/sample/sampling; (iii) nature/sources of data + instrument; (iv) methods of analysis; (v) framework + variables | 3.1 Introduction; 3.2 Design; 3.3 Population/sample/sampling; 3.4 Nature/sources/collection; 3.5 Framework + variables; 3.6 Methods of analysis. Note: thesis orders (v) before (iv); guideline clause "sections may be altered... upon the advice of the supervisor" covers this, but it is currently unremarked | CONFORMS (order note below) |
| IV Results and Discussion | Results (organized subsections; test statistic + df; all RQs/hypotheses) then Discussion (interpretation vs theory and prior studies, biases/limitations, leads to conclusion) | 4.2 Results in 7 subsections (all tables carry statistic + df); 4.3 Discussion in 5 subsections incl. reconciliation with Ohlson/Kwon/signaling/opacity, comparison with prior Nepalese and emerging-market studies, methodological context; cites (2019, pp. 14-15) correctly | CONFORMS |
| V Summary and Conclusion | THREE sections: Summary; Conclusion; Implications (implications include recommendations and future research) | FIVE-ish: 5.1 Introduction; 5.2 Summary; 5.3 Conclusions (incl. RQ answers 5.3.1 and hypothesis-decision Table 5.1 in 5.3.6); 5.4 Implications (three domains); 5.5 Recommendations and Future Research as a separate section — while 5.1 claims "In accordance with... (2019, p. 15)... four core functional sections" | DEVIATION + misstated claim (finding A5) |
| Prefatory (context) | Order per p. 9 Appendix B | main.tex order: Title, Authorship, Research Committee, Approval, Acknowledgements, TOC, LOT, LOF, Abbreviations, Abstract | CONFORMS |
| Abstract | One page; <= 5 keywords; purpose/methods/findings/conclusions | One page (fit-tuned); exactly 5 keywords; all four question types answered | CONFORMS |

## A. Must-fix content findings (current LaTeX)

1. **Chapter 1, line 150 — leftover unsupported VIF range.** Rationale
   point 3 still says EPS-ROA collinearity yields "variance inflation
   factors between approximately 20 and 30 depending on model
   specification". The computable bivariate value is 1/(1 - 0.975^2) =
   20.25. Chapter 3 line 245 says "approximately 20.3"; Chapter 4 line
   130 and Chapter 5 line 80 say "approximately 20.2". The "20 and 30"
   range is the residue of the old uncomputed "~30" claim and
   contradicts the exact value used everywhere else. Fix: make Chapter 1
   match the computed value (and unify 20.2 vs 20.3 across chapters —
   see D1).

2. **Appendix C — forest plot described as eight specifications; the
   figure shows seven.** The intro says "across the full eightfold
   sensitivity suite (R1 through R8)" and the caption says "Across
   Robustness Specifications R1–R8". The asset
   (`figures/A2_robustness_forest.pdf`) is generated by
   `data_analysis/analysis/assets/a2_robustness_forest.py` with
   `EPS_RUN_IDS = ("R1", "R2", "R4", "R5", "R6", "R7", "R8")` — R3 is
   omitted, and the figure's own printed caption says so. Chapter 4's
   use of the same asset (line 446: "seven specifications (R1, R2, R4–
   R8; R3 omitted...)") is correct. This is the same figure-note-vs-code
   error class the Phase 2 loop found in F1/F2/F5; it survived in
   Appendix C. Fix the Appendix C intro and caption to seven
   specifications with the R3 omission stated.

3. **Appendix A, intro paragraph — "independently archived by
   Merolagani".** This overstates the verification position the thesis
   otherwise maintains with precision: Chapter 3 section 3.4.3 states
   the Merolagani comparison "does not represent independent
   verification", and Appendix A's own note (a) says exactly the same
   for the one divergent cell. The intro sentence contradicts both.
   Fix: delete "independently" (e.g., "as archived by Merolagani, a
   capital market data aggregator").

4. **Chapter 2, line 295 — self-contradicting "universally".** "With few
   exceptions, extant Nepalese banking studies employ pooled OLS...;
   While recent work by Gurung and Dahal introduces bank fixed
   effects..., existing literature universally estimates static,
   full-period average coefficients." The sentence names its own
   exception and then says "universally" in the same breath. It also
   breaks the cross-chapter rule enforced everywhere else (Chapter 5's
   "universally" was already downgraded to "almost all"). Fix: "almost
   all" (or "virtually all").

5. **Chapter 5, section 5.1 — misstated guideline conformance.** The
   chapter cites "(2019, p. 15)" and then claims FOUR "core functional
   sections". Guideline p. 15 specifies THREE sections (Summary,
   Conclusion, Implications), with recommendations and future research
   inside Implications. The four-way split (5.4 Implications / 5.5
   Recommendations and Future Research) is defensible under the
   guideline's supervisor-advice clause, but the current sentence
   misstates what p. 15 says, and an examiner who opens p. 15 will see
   the mismatch. Fix either: merge 5.5 under 5.4 as the guideline
   structures it, or reword to "extending the three-section structure
   of the Guidelines (2019, p. 15) by separating recommendations and
   future research into their own section".

## B. Table 2.1 completion job (carried from fix-verification round 2; re-confirmed in current LaTeX)

All of the following were re-confirmed against
`chapter_02_literature_review.tex` lines 300-362:

- Still no dedicated Methodological Critique column; critique survives
  only as parenthetical tags inside Core Empirical Findings.
- Total observations still missing for six rows: Pradhan (2003),
  Collins (1997), Kwon & Wang (2020), Sharma (2011), Adhikari (2023),
  Bhandari (2026) ("Census" with years, no count).
- Unverified period figures still printed: Kwon & Wang "(1998–2014)"
  and Bhandari "(2015–2024)" — neither period appears in the chapter
  prose. Source or remove.
- Gurung & Dahal row says "110 obs" next to prose (line 271) calling it
  a "ten-year period FY 2013/14 to 2023/24"; that span is 11 fiscal
  years. Align the label and the count.
- Lamsal (2024) row (and prose, line 256) still gives no years and no
  observation count ("multi-year panel").
- Niraula (2026) is discussed in prose (line 275) but absent from the
  table; the prose does not state its dependent variable, so either add
  it or state why it fails the stated selection criterion. (bhattarai2024,
  dongol2024, and adhikari2023cbr legitimately fail the DV = MPS criterion;
  one clause saying so would close the question.)
- The table note (line 361) says "EY and MTB are reproduced as labelled
  in the Dahal et al. (2025) row; their expansions are not defined in
  the thesis text." This reads like an audit-trail confession in a
  submitted document. Define them (standard expansions: earnings yield,
  market-to-book ratio, to be confirmed against the paper) or drop the
  two labels from the row.

## C. Open minors (carried; re-confirmed)

- Chapter 1: the three purposive-selection criteria are not previewed
  in Chapter I itself (they live in Ch. 3, section 3.3.2); limitation 1
  gestures at them without listing them.
- Chapter 2, line 149: uncited institutional claims — "delayed
  dissemination of corporate filings, and the absence of a unified
  electronic corporate announcement timestamp registry". Cite or hedge
  as observation.
- Chapter 3, line 133: "consistent with standard Nepalese banking
  valuation convention" remains uncited.
- Generated T2 note still reads "variance inflation ~ 30"
  (`data_analysis/analysis/assets/t2_correlations.py:56`), which will
  contradict the chapters' exact ~20.2/20.3 the next time tables are
  regenerated. Fix in the asset, not the chapters.

## D. Uniformity and wording nits

1. VIF of EPS-ROA appears three ways: "between approximately 20 and 30"
   (Ch. 1), "approximately 20.3" (Ch. 3), "approximately 20.2" (Ch. 4,
   Ch. 5). Computed from the printed r = 0.975: 20.25. Pick one value
   and use it everywhere (A1 above is the same fix).
2. Chapter 1, line 173: the two suspended observations are described as
   "unverifiable within the 5-day freshness window". They were not
   unverifiable; they were ineligible (prices resumed 54/47 days past
   the deadline). "Ineligible under the 5-day freshness rule" matches
   Chapters 3-5.
3. Chapter 5, line 187: "reduced the universal population of commercial
   banks" — odd collocation; "the population of commercial banks" (or
   "the universe of licensed banks").
4. Hardcoded cross-references instead of \ref: Ch. 3 line 36
   ("Section~3.3.4"), Ch. 3 line 252 ("Section~2.2.6"), Ch. 4 line 209
   ("Section~4.2.7"), Ch. 4 line 598 ("Section~4.2.6"). All currently
   point at the right sections, but any renumbering breaks them
   silently.
5. Chapter 4, Table 4.6 note: "Cook's distance evaluated using the
   correct parameter count (K = 12)" — drop "correct" (self-referential);
   state the count.
6. Chapter 4, Table 4.6 row: Cook's distance "Assessment: Addressed via
   HC3" still slightly overclaims (HC3 does not remove influence; it
   hardens inference against it). The prose below the table states the
   mechanism correctly; consider "Robustness via HC3".
7. "(Codebase Asset F3)"-style tags in Chapter 4 figure notes are fine
   given Chapter 1's reproducibility commitment (section 1.5, point 5),
   but confirm with the supervisor that the analytical codebase is
   submitted or available, since the tags presuppose it.

## E. Verified clean (so these are not re-litigated)

- Numbers: Model 1 (2.095 / 4.096 / t 0.51 / p 0.616 / df 16; 0.219 /
  1.858 / 0.908; R2 0.948, adj 0.912, within 0.152), Model 2 (5.577 /
  3.560 / 0.140; 0.100 / 1.306 / 0.940; delta_E -3.124 / 4.003 / 0.448;
  delta_B -1.758 / 1.231 / 0.175; implied post slopes 2.453 (2.269,
  t 1.08, p 0.298) and -1.658 (1.120, t -1.48, p 0.161); Wald F(2,14) =
  2.954, p = 0.085; R2 0.978, within 0.642), R3-R8 rows, pooled 4.882
  (3.099) R2 0.136 df 25, bank-FE 5.217 df 21, R6 F(2,10) = 5.82, p =
  0.021 with delta_B -2.611 (1.517) — all match the audited
  Phase 1/Phase 2 verified set and the in-text t/p recomputations.
- Descriptives and derived percentages (price -33.80%, SD -72.00%, EPS
  -40.11%, EPS SD +63.66%, BVPS +2.44%, DPS -76.90%, ROA -46.56%) all
  recompute from Table 4.1.
- Sample attribution spot-checks from the joined panel: sample-max EPS
  27.60 is HBL FY 2076/77 (28.07 belongs to the excluded HBL FY 2077/78
  row), sample-min EPS 0.02 is KBL FY 2080/81 — Chapter 4's attributions
  are correct.
- All 17 Phase 2 must-fix items verified applied in current LaTeX
  (preview p-values, merger-date citations, Kanchan 0.56bn beyond-bonus
  arithmetic, BAFIA publication duty, Chaitra operationalization
  wording in Ch. 2 line 191 and Ch. 3 line 208-210, HC3 direction in
  Ch. 3 line 338 and Ch. 4 line 485, Group-equity scoping Ch. 3 line
  133, linearmodels/Excel removed, Student's t disclosure, "verified
  stability" gone, H1-H4 decision table (Ch. 5 Table 5.1, values
  correct), causal language hedged, universality claims scoped, KBL
  9.59m restatement added, R7 pro-forma note, R8 28.07 correct).
- Figure notes in Chapter 4 match generation code (F1: 3 variables, no
  fit lines; F2: no asterisks; F3: bivariate-lines disclaimer present;
  F5: Q-Q top-left, residuals top-right; F6: open-marker/line behavior
  disclosed; A2: seven specs, EPS channel, R3 omission explained).
- Appendix B note carries every Phase 1 disclosure (NIMB NAV integer
  rounding with NMB FY 2081/82 kept flagged; EPS-denominator timing
  with the GBIME 22.06/18.71, NIMB 13.92/10.90, HBL 9.18/7.22 examples;
  R8 substitutions; exclusion notes), and its 30 rows match the panel.
- Bibliography: every cited key exists in `references.bib` (31 keys
  spot-checked across all chapters); `nmb2021report` is cited nowhere
  in the thesis and correctly absent from its .bib.
- Banned/over-broad word sweep (utiliz*, pivotal, crucial role,
  underscores, universally): one hit only — the Chapter 2 "universally"
  (finding A4).
- Abstract: 5 keywords, one page, purpose/methods/findings/implications
  all present, sensitivity-dependent framing consistent with Ch. 4/5.

## F. Markdown-LaTeX sync (drift confirmed still present)

`docs/draft/thesis/chapter_02_literature_review.md` still carries the
pre-fix versions that round 2 fixed only in LaTeX: Table 2.1 has 20
rows (LaTeX has 22 — Lamsal and Gurung & Subedi missing), the Bhattarai
row still reads "72 obs" (MD line 229), and the Dahal row still reads
"dividend rate significantly positive" (MD line 240). If the Markdown
drafts feed any future regeneration, sync them first; if not, they
remain an audit-trail inconsistency only.

## Pending external checks (unchanged, not thesis-text defects)

- NEPSE official-close verification (28 rows) — never done; framing
  disclosure is correct throughout.
- Supervisor approval of the aggregator-price MPS_RD definition — the
  standing gate for final (non-draft) framing.
- Page-span check of the guideline length guides (Background "2-3
  pages should suffice"; problem statement 2-4; Chapter II 10-20) on
  the next build — `src/build/thesis/` was removed mid-review, so this
  review could not measure compiled spans.
- Full-text checks still outstanding from Phase 2: Timalsina (2026)
  169 observations; Bhandari et al. (2026) "all 19"; KBL–NCC 1 Jan 2023
  / 1:1 against a KBL primary source; Dahal, Gurung & Ghimire (2025)
  pages 252-261; the changed Lamsal (2024) summary against the paper.
