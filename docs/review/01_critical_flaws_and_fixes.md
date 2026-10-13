# Critical Academic Flaws and Professional Solutions

This document provides the finalized, comprehensive supervisor-grade critique of the proposal draft. It analyzes every technical, methodological, and factual defect that poses a risk of rejection or critical challenge during proposal defense before the Research Management Cell (RMC), Tribhuvan University (TU).

---

## 1. The Econometric "Panel Data" Paradox (Section 1.1.1 & 1.1.5)

### The Defect
On page 7 of the reviewed draft (`detail/12`), the supervisor underlined **`"Panel data"`** twice and added **`"??"`**.  
The current proposal states that the study uses secondary panel data ($N=5, T=6 \implies 30$ observations), but then specifies:
> *"The multiple linear regression model (Eq. 1) is estimated using Ordinary Least Squares (OLS)... pooled OLS serves as the baseline exploratory specification... All data organization, coding, and econometric estimations are conducted using the Statistical Package for the Social Sciences (SPSS) and Microsoft Excel."*

### Why University Committees Challenge This
1. **The Homogeneity Fallacy of Pooled OLS:**  
   Pooled OLS pools all 30 bank-year observations into a single regression, assuming that all commercial banks share an identical intercept ($\beta_0$) and that unobserved bank-specific heterogeneity is zero. In banking, institutions differ drastically in management culture, risk appetite, brand reputation, digital capabilities, and branch footprints (unobserved bank-specific effects $\alpha_i$). If these bank-specific characteristics correlate with the explanatory fundamentals, **Pooled OLS yields biased and inconsistent estimates**.
2. **Missing Panel Specification Tests:**  
   In empirical finance theses under TU FOM, a panel study must formally specify:
   - **Breusch-Pagan Lagrange Multiplier (LM) Test:** Tests whether individual random heterogeneity exists (Pooled OLS vs. Random Effects).
   - **Hausman Specification Test:** Tests whether individual effects correlate with the explanatory variables, formally deciding whether the **Fixed Effects Model (FEM)** or **Random Effects Model (REM)** is the consistent estimator.
3. **The Software Exposure (The "SPSS" Trap):**  
   Standard SPSS has **no native panel econometric estimation module**. It cannot perform the Breusch-Pagan LM test or the Hausman specification test. At Tribhuvan University, empirical panel regressions are estimated in **EViews** or **Stata** (or R), while SPSS/Excel are used for descriptive statistics and Pearson correlations. Claiming that panel econometrics is performed purely in SPSS exposes the candidate to immediate technical skepticism.

### The Finalized Fix
Formally declare the three-stage panel estimation workflow in Section 1.1.5 (Pooled OLS $\to$ Fixed Effects $\to$ Random Effects $\to$ Breusch-Pagan LM test $\to$ Hausman test), and explicitly state:
> *"Data organization, coding, and descriptive statistics are conducted using Microsoft Excel and SPSS. Panel econometric estimations, diagnostic specification tests (Breusch-Pagan LM and Hausman tests), and panel regression models are estimated using EViews and Stata."*

---

## 2. The Literature Review Table (Table 1: Meta Table of Related Studies)

### The Defect
In Section vi (`06_literature_review.tex`), a 12-row `longtable` spanning ~1.5 pages summarizes empirical studies using telegraphic notes (*"BV, EPS, P/E positive. Dividend yield inverse"*).

### Why University Committees Reject This
1. **Shortcut vs. Scholarly Synthesis:** An empirical review must be a **thematic, critical narrative**. Dumping a raw summary table shows only that the student collected notes; it fails to demonstrate critical understanding of methodological differences, sample periods, or contradictory findings.
2. **Supervisor's Direct Directive:** Across pages 5 and 6 of the reviewed draft (`detail/07`, `detail/09`, `detail/11`), the supervisor:
   - Wrote: *"56 page Review of literature Should be the Strongest part of your research. You need to write again the literature review => both theoretical & empirical review"*.
   - Circled "Earnings per share" with an arrow pointing to **`"-> NO headings"`**.
   - Drew **large diagonal red pen strokes crossing out Table 1** across page 5 and continuing across page 6. The diagonal slash across the table means **eliminate the table and write a proper narrative review**.

### The Finalized Fix
Delete Table 1 completely and synthesize all 12 verified studies into **three dense, thematic narrative paragraphs**:
- **Paragraph 1 (The Foundational Consensus):** Synthesizing international studies (Malhotra & Tandon, 2013; Almumani, 2014) and early Nepalese evidence (Bhattarai, 2014; Pradhan & Dahal, 2016; Bajracharya & Sawagvudcharee, 2019) showing positive price responses to EPS/DPS and inverse yield/inflation effects.
- **Paragraph 2 (The Acute Contradictions):** Contrasting positive BVPS findings (Joshi et al., 2023; Chhetri, 2023) against negative/insignificant findings (Niroula, 2021; Pant et al., 2024), and contrasting positive ROA (Pradhan & Dahal, 2016; Chhetri, 2023) against insignificant ROA (Gyawali, 2022) and negative ROA (Chaudhari, 2025).
- **Paragraph 3 (Institutional Context & Consolidation):** Capital adequacy regulations (Bhattarai, 2024), corporate governance (Dongol & Shrestha, 2024), macro rates (Timalsina, 2026), and the post-merger 46% price drop (Adhikari et al., 2023a, 2023b).

---

## 3. Casual Phrasing in Research Questions and Objectives

### The Defect
In Sections ii and iii, the previous simplification reduced the text to informal phrasing:
- *"How is each fundamental linked to $\mathit{MPS}^{post}$?"*
- *"To measure the link between each fundamental and $\mathit{MPS}^{post}$."*
- *"How well do the four fundamentals jointly explain $\mathit{MPS}^{post}$?"*

### Why University Committees Challenge This
Simplifying sentences does not mean using colloquial vocabulary. Words like *"linked"* and *"measure the link"* make the proposal sound like an undergraduate assignment.

### The Finalized Fix
- **Q2:** *"How is each accounting fundamental associated with post-disclosure market price per share ($\mathit{MPS}^{post}$)?"*
- **Q3:** *"To what extent do the four accounting fundamentals jointly explain variations in $\mathit{MPS}^{post}$?"*
- **Obj 2:** *"To evaluate the bivariate relationship between each accounting fundamental and $\mathit{MPS}^{post}$."*
- **Obj 3:** *"To estimate the joint explanatory power and conditional effects of the four accounting fundamentals on $\mathit{MPS}^{post}$."*

---

## 4. Citation Attribution Anachronism in Background (Section i)

### The Defect
In `01_background.tex`, the text states:
> *"...Nepal Investment Bank merged with Mega Bank to form Nepal Investment Mega Bank, and Himalayan Bank acquired Civil Bank \citep{adhikari2023}."*

### Why University Committees Challenge This
Adhikari, Kavanagh, & Hampson (2023a in *Asia Pacific Management Review*, 2023b in *Central Bank Review*) examined empirical data from the **2013–2020** merger wave with datasets ending prior to 2021. They did not document the live January/February 2023 mergers in their historical dataset.

### The Finalized Fix
Cite **Nepal Rastra Bank (2023)** for the live early 2023 merger completions, preserving Adhikari et al. (2023a, 2023b) strictly for the empirical finding that post-merger share prices fell by 46% while operational fundamentals remained statistically unchanged.

---

## 5. Broken Citation Syntax in Research Gap (`\citeyearpar`)

### The Defect
In line 57 of `06_literature_review.tex`:
```latex
Second, results on ROA and BVPS directly contradict: \citeyearpar{chhetri2023} reports ROA significantly positive, \citeyearpar{chaudhari2025} significantly negative...
```
In `apacite`/`natbib`, `\citeyearpar` prints only `(2023)`, stripping the author's name and leaving sentences without grammatical subjects: `"(2023) reports ROA..."`.

### The Finalized Fix
Replace with `\citet{...}` so that `apacite` outputs `Author (Year)`:
```latex
Second, results on ROA and BVPS directly contradict: \citet{chhetri2023} reports ROA significantly positive, \citet{chaudhari2025} significantly negative, and \citet{gyawali2022} positive but insignificant; on BVPS, \citet{joshi2023} find it significant while \citet{pant2024} find it negative and insignificant.
```

---

## 6. Padded Front Matter (`List of Tables` & `List of Figures`)

### The Defect
In `src/proposal/main.tex`, standalone pages are created for `\listoftables` (page iii) and `\listoffigures` (page iv) with `\clearpage`.

### Why University Committees Challenge This
With Table 1 removed and Table 2 converted to a paragraph, there are zero tables in the proposal (`\listoftables` prints an empty page). Having an entire page for a one-line `List of Figures` is obvious padding. TU FOM Guidelines (pp. 7–9) prescribe preliminary materials for the final 100-page dissertation, not the 10-page proposal. The supervisor's printout (`detail/02`) contained only the `Table of Content`.

### The Finalized Fix
Remove `\listoftables` and `\listoffigures` from `main.tex`. Retain only the Title Page and the `Table of Contents`.

---

## 7. Sentence Duplication and TikZ Geometry in Section 1.1.4

### The Defects
1. **Sentence Duplication:** In Section 1.1.4, the exact operational definition of $\mathit{MPS}^{post}$ is printed verbatim both above and below Figure 1.
2. **TikZ Asymmetry:** Figure 1 aligns `mps` with node #3 (`bvps`) instead of the midpoint between node #2 and node #3, pulling the box downward and distorting the arrows.
3. **Missing Measurement Units:** Operational definitions omit units (Nepalese Rupees vs. Percentage).

### The Finalized Fix
- Remove the premature definition sentence from above Figure 1.
- In Figure 1, define `\path (dps) -- (bvps) coordinate[midway] (mid); \node[dep, right=2.2cm of mid] (mps) {...};`.
- Explicitly declare units: Nepalese Rupees (NPR per share) for $\mathit{MPS}^{post}$, EPS, DPS, BVPS; Percentage (%) for ROA.
