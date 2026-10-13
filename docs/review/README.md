# Master Supervisor Review & Defense Readiness Audit

**Document Under Review:** MBS Dissertation Proposal  
**Title:** Fundamental Determinants of Share Prices: Evidence from Nepalese Commercial Banks  
**Candidate:** Asmita Subedi | Exam Roll No: 67514/24 | T.U. Regd. No: 7-2-48-1060-2018  
**Institution:** Triveni International College, Faculty of Management, Tribhuvan University  
**Auditor:** Senior Academic Reviewer / External Examiner Perspective  
**Evaluation Standard:** TU FOM Master's Degree Dissertation Guidelines (2019) & Empirical Econometric Standards  

---

## 1. Executive Verdict: The Unvarnished Truth

This proposal has a strong conceptual foundation, an interesting study period (bridging the major 2023 consolidation wave), and correct typographic margins (Times New Roman 12 pt, 1.5 line spacing, 1.25"/1.0" margins). 

However, **if submitted in its current form to the TU Faculty of Management Research Management Cell (RMC), it faces severe challenges or conditional rejection** from experienced examiners. The defects are not merely formatting glitches—they go straight to the **scholarly maturity, econometric validity, and empirical integrity** of the work:

1. **The Econometric "Panel Data" Paradox (Section 1.1.1 & 1.1.5):**  
   The supervisor explicitly underlined `"Panel data ??"` in red ink on page 7. Why? Because the proposal claims to use a panel of $N=5$ banks across $T=6$ years ($N \times T = 30$), but then claims to estimate only **Pooled OLS in SPSS**!  
   *The examiner's trap:* Pooled OLS assumes zero unobserved bank-specific heterogeneity ($\alpha_i = \alpha$). In banking, banks differ drastically in management culture, risk appetite, and brand capital. If individual bank effects exist, Pooled OLS is biased and inconsistent. Standard panel econometrics demands the **Fixed Effects Model (FEM)**, **Random Effects Model (REM)**, the **Breusch-Pagan LM test**, and the **Hausman Specification Test**. Furthermore, **standard SPSS cannot perform panel Hausman tests or Fixed/Random Effects without specialized syntax or plugins**—every econometrics professor knows that panel data regression requires **EViews, Stata, or R**. Claiming to do panel econometrics purely in SPSS and Excel exposes the candidate to immediate technical embarrassment.

2. **The "Homework Spreadsheet" in the Literature Review (Section vi):**  
   Dumping a 12-row, 1.5-page raw summary table (`Table 1: Meta table of related studies`) with telegraphic phrases (*"BV, EPS, P/E positive. Dividend yield inverse"*) in an 8–12 page proposal looks like unassimilated student notes. The supervisor drew massive diagonal strokes across Table 1 precisely to say: **"Do not give me a table; synthesize the empirical literature into critical narrative prose."**

3. **Colloquial Wording in Research Questions and Objectives (Sections ii & iii):**  
   Shortening the questions was ordered, but simplifying them to *"How is each fundamental linked to MPS?"* and *"To measure the link..."* introduces casual, unscientific vocabulary. In academic finance, researchers do not "measure links"—they *evaluate empirical associations* or *analyze bivariate relationships*.

4. **Factual Attribution Anachronism (Section i):**  
   In `01_background.tex`, the early 2023 mega-mergers (NIMB, Himalayan-Civil) are cited as `\citep{adhikari2023}`. Adhikari et al. (2023a, 2023b) published their papers analyzing the *2013–2020* merger wave with datasets ending prior to 2021. The early 2023 consolidations were live market events documented by Nepal Rastra Bank (NRB) and NEPSE reports, not by Adhikari's 2013–2020 sample. A careful banking examiner will catch this sloppy citation attribution.

5. **Amateur Drafting Artifacts:**  
   - Broken citation syntax (`\citeyearpar{chhetri2023}`) printing sentences with missing subjects: `"(2023) reports ROA..."`.
   - Dedicated front-matter pages for an empty `List of Tables` and a one-line `List of Figures`, violating TU proposal norms.
   - Word-for-word repetition of the $\mathit{MPS}^{post}$ operational definition sentence immediately above and below Figure 1.
   - A lopsided TikZ diagram where the dependent variable box is pulled downward because it is aligned with box #3 instead of the center.
   - Missing operational units (Nepalese Rupees vs. Percentage), leaving regression slope interpretation ambiguous.

---

## 2. Comprehensive Defense Risk Assessment

| Academic Area | Current Proposal Status | External Examiner Reaction | Post-Audit Fix |
|---|---|---|---|
| **Panel Econometrics** | Pooled OLS only; claims SPSS software | **HARSH REJECTION RISK:** "Why no Hausman test? Why no FE/RE? SPSS cannot run panel models!" | Incorporates Pooled OLS, FE, RE, Hausman test, and specifies EViews/Stata alongside SPSS |
| **Literature Review** | 12-row raw table across 1.5 pages | **HIGH CRITIQUE:** "Amateur literature dump; lack of critical synthesis" | Replaced with 3 dense, scholarly thematic paragraphs synthesizing all 12 studies |
| **Questions / Objectives** | Informal phrasing ("linked", "measure link") | **MODERATE FLAG:** "Unscientific colloquial vocabulary" | Refined to simple yet rigorous academic finance language |
| **Citation Attribution** | Cites Adhikari (2023) for 2023 live mergers | **FACTUAL FLAG:** "Adhikari's sample ended in 2021; cite NRB/NEPSE" | Corrected to cite NRB (2023) and NEPSE official records |
| **Citation Grammar** | `\citeyearpar` outputs `(2023) reports...` | **EMBARRASSING ERROR:** Grammatical subjects missing from sentences | Replaced with `\citet{...}` (Author, Year) |
| **Front Matter** | Standalone LOT (blank) & LOF (1-line) pages | **AMATEUR TELL:** Artificial padding to inflate page count | Stripped to clean, elegant Table of Contents only |
| **Framework Diagram** | Box aligned with box 3 (downward slant) | **VISUAL FLAW:** Lopsided, asymmetrical arrows | Centered using mathematical midpoint coordinate |
| **Variable Definitions** | Verbatim duplicate sentences; missing units | **EDITING FLAW:** Repeated text; regression units undefined | Consolidated into single clean definition with NPR and % |

---

## 3. Directory Guide

The audit in this directory is divided into five exhaustive documents:

1. [01_critical_flaws_and_fixes.md](file:///C:/Users/Hellx/Documents/Docs/Res/As/thesis/docs/review/01_critical_flaws_and_fixes.md)  
   Master summary of the 7 major academic defects, why university defense committees challenge them, and their finalized solutions.

2. [01_econometric_and_methodological_critique.md](file:///C:/Users/Hellx/Documents/Docs/Res/As/thesis/docs/review/01_econometric_and_methodological_critique.md)  
   Resolves the `"Panel data ??"` query: full defense of $N=5, T=6$, degrees of freedom, Pooled OLS vs. Fixed Effects vs. Random Effects, Hausman test workflow, and why EViews/Stata must be named alongside SPSS.

3. [02_content_and_factual_audit.md](file:///C:/Users/Hellx/Documents/Docs/Res/As/thesis/docs/review/02_content_and_factual_audit.md)  
   Verifies every historical date, merger swap ratio, NRB figure, and citation attribution; refines research questions and objectives to scholarly finance standards.

4. [03_structural_and_latex_defects.md](file:///C:/Users/Hellx/Documents/Docs/Res/As/thesis/docs/review/03_structural_and_latex_defects.md)  
   Detailed dismantling of Table 1, removal of padded LOT/LOF front matter, correction of Figure 1 geometry, and operational unit declarations.

5. [04_production_ready_patches.md](file:///C:/Users/Hellx/Documents/Docs/Res/As/thesis/docs/review/04_production_ready_patches.md)  
   Exact, verified, drop-in LaTeX code blocks for all affected files, ready to apply immediately.

