# Structural, Formatting, and LaTeX Flaws

This document details the presentation, typographical, and structural defects across `main.tex`, `06_literature_review.tex`, and `07_methodology.tex`, providing the rationale for their elimination.

---

## 1. Dismantling the Literature Review Table (Table 1)

### Context and Evidence
In `src/proposal/sections/06_literature_review/06_literature_review.tex`, the proposal inserts a 12-row `longtable` titled *"Meta table of related studies"*. 

On pages 5 and 6 of the supervisor's reviewed printout (`detail/07`, `detail/09`, `detail/11`), the supervisor:
1. Wrote: *"56 page Review of literature Should be the Strongest part of your research. You need to write again the literature review => both theoretical & empirical review"* with *"Strongest"* and *"both theoretical & empirical review"* underlined.
2. Circled "Earnings per share" with an arrow pointing to **`"-> NO headings"`**.
3. Drew **massive diagonal red ink strokes across Table 1 from top edge to bottom left**, continuing across the remaining three rows on page 6.

### Academic Rationale
In academic thesis proposals, a table summarizing literature is an informal reading aid; it is **not** an acceptable literature review. Literature reviews must be written in **cohesive, critical prose** that contrasts methodologies, samples, and empirical outcomes. Dumping a table with bullet points (*"BV, EPS, P/E positive"*) is considered lazy student drafting. 

When the table is deleted, the empirical review becomes a three-part narrative:
1. **The Consensus on Core Earnings & Distributions** (Malhotra & Tandon 2013, Almumani 2014, Bhattarai 2014, Pradhan & Dahal 2016, Bajracharya & Sawagvudcharee 2019).
2. **The Conflict on Asset Efficiency & Book Value** (Joshi et al. 2023, Chhetri 2023 vs. Niroula 2021, Pant et al. 2024 vs. Gyawali 2022, Chaudhari 2025).
3. **The Regulatory & Consolidation Landscape** (Bhattarai 2024, Dongol & Shrestha 2024, Timalsina 2026, Adhikari et al. 2023a, 2023b).

---

## 2. Stripping Empty Front Matter (`List of Tables` & `List of Figures`)

### Context
In `src/proposal/main.tex`, lines 70–82:
```latex
\tableofcontents
\clearpage
\listoftables
\clearpage
\listoffigures
\clearpage
```

### Academic Rationale
1. **Zero Tables:** With Table 2 converted to a paragraph and Table 1 converted to narrative text, the proposal contains **zero tables**. Running `\listoftables` outputs a blank page with only the title, which is an immediate technical blunder.
2. **One Figure:** Generating a full A4 page for a single line (`Figure 1: Research framework ... 8`) is obvious padding.
3. **TU Guideline Standard:** The TU FOM Master's Degree Dissertation Guidelines (2019, pp. 7–9) explicitly specify preliminary materials (Abstract, Acknowledgement, Table of Contents, List of Tables, List of Figures) for the **final 100-page dissertation**, but explicitly define the proposal structure as:
   - Title Page
   - Proposal body (Sections i through vii)
   - References  
   In fact, the supervisor's reviewed printout (`detail/02`) contained only the `Table of Content`.

### Fix
Strip `\listoftables` and `\listoffigures`. Retain only `\tableofcontents` in the preliminary group.

---

## 3. Fixing Broken Citation Grammar (`\citeyearpar`)

### The Defect
In line 57 of `06_literature_review.tex`:
```latex
Second, results on ROA and BVPS directly contradict: \citeyearpar{chhetri2023} reports ROA significantly positive, \citeyearpar{chaudhari2025} significantly negative, and \citeyearpar{gyawali2022} positive but insignificant; on BVPS, \citeyearpar{joshi2023} find it significant while \citeyearpar{pant2024} find it negative and insignificant.
```

### Output in PDF
> *"Second, results on ROA and BVPS directly contradict: (2023) reports ROA significantly positive, (2025) significantly negative, and (2022) positive but insignificant; on BVPS, (2023) find it significant while (2024) find it negative and insignificant."*

### Fix
Change `\citeyearpar{...}` to `\citet{...}`:
```latex
Second, results on ROA and BVPS directly contradict: \citet{chhetri2023} reports ROA significantly positive, \citet{chaudhari2025} significantly negative, and \citet{gyawali2022} positive but insignificant; on BVPS, \citet{joshi2023} find it significant while \citet{pant2024} find it negative and insignificant.
```

---

## 4. De-duplicating Definition of $\mathit{MPS}^{post}$

### The Defect
In Section 1.1.4, the introductory paragraph above Figure 1 ends with:
> *"For each fiscal-year observation, $\mathit{MPS}^{post}_{it}$ is defined as the closing market price on the first NEPSE trading day following the public disclosure of the corresponding audited annual financial statements through NEPSE. The same rule is applied consistently across all sampled banks and fiscal years."*

And the paragraph immediately below Figure 1 opens with:
> *"Post-disclosure market price per share ($\mathit{MPS}^{\mathit{post}}$) is the closing market price on the first NEPSE trading day following public disclosure of the corresponding audited annual financial statements through NEPSE."*

### Fix
Remove the sentence from above Figure 1. Keep the opening paragraph purely conceptual, and consolidate the definition once in the paragraph below Figure 1 alongside EPS, DPS, BVPS, and ROA.

---

## 5. Centering Figure 1 TikZ Geometry

### The Defect
```latex
\node[ind] (eps)  {EPS};
\node[ind, below=of eps] (dps)  {DPS};
\node[ind, below=of dps] (bvps) {BVPS};
\node[ind, below=of bvps] (roa) {ROA};
\node[dep, right=2.2cm of bvps] (mps) {$\mathit{MPS}^{\mathit{post}}$};
```
Aligning `mps` horizontally with `bvps` (the 3rd box) forces the entire dependent box downward. The top arrow from `eps` drops steeply down, while the bottom arrow from `roa` slants upward.

### Fix
Define the midpoint between node 2 (`dps`) and node 3 (`bvps`):
```latex
\node[ind] (eps)  {EPS};
\node[ind, below=of eps] (dps)  {DPS};
\node[ind, below=of dps] (bvps) {BVPS};
\node[ind, below=of bvps] (roa) {ROA};
\path (dps) -- (bvps) coordinate[midway] (mid);
\node[dep, right=2.2cm of mid] (mps) {$\mathit{MPS}^{\mathit{post}}$};
```
This produces a perfectly balanced, symmetrical diagram matching the supervisor's hand-drawn template in `detail/16`.

---

## 6. Declaring Units of Measurement in Variable Definitions

### The Defect
In econometric multiple regressions, failure to declare measurement units leaves coefficient interpretation open to challenge.

### Fix
Explicitly incorporate the units in the definition paragraph:
- $\mathit{MPS}^{post}$: Nepalese Rupees (NPR per share)
- $\mathit{EPS}$: Nepalese Rupees (NPR per share)
- $\mathit{DPS}$: Nepalese Rupees (NPR per share)
- $\mathit{BVPS}$: Nepalese Rupees (NPR per share)
- $\mathit{ROA}$: Percentage (%)
