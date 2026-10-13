# Plan 06 — Research design "Why?" + "Panel data ??" (answer both)

Source: `../detail/12_methodology_population_p7.md` (handwritten "x Why?", "Panel data ??", underlines, i>/ii>/iii>)
Target: `src/proposal/sections/07_methodology/07_methodology.tex` — `\msub{1.1.1 Research design}` paragraph + `\msub{1.1.2 ...}` sampling paragraph (bank list itself unchanged — ticked i>/ii>/iii>).

## Answers (paste-ready)

### 1.1.1 replacement paragraph (answers "Why?" in the first sentence)

```latex
\msub{1.1.1 Research design}
This study employs a descriptive and explanatory quantitative research design using secondary panel data, in accordance with established social science methodology \citep{pant2016}. The design follows directly from the research questions: description answers what the levels and trends are (Q1), while explanation tests how each fundamental links to price and how well they jointly explain it (Q2--Q3). The descriptive component reports distributional characteristics, central tendencies, and historical variations of EPS, DPS, BVPS, ROA, and $\mathit{MPS}^{post}$. The explanatory component estimates bivariate correlations and the multiple regression in Eq.~\ref{eq:main} for conditional associations. The data are a panel: the same $N=5$ banks observed over the same $T=6$ fiscal years (FY 2076/77 to FY 2081/82), yielding $5 \times 6 = 30$ bank-year observations. Pooled OLS is the baseline exploratory specification; inference is interpreted cautiously given repeated within-bank observations and the small sample, with diagnostic checks in 1.1.5.
```

Why this passes: the "Why?" is answered explicitly (design ← questions), "panel data" is defined (same units × same years, N/T stated), and the pooled-OLS + caution + diagnostics forward-reference disarms the "??" without hiding the N=5/T=6 limit.

### 1.1.2 sampling paragraph (keep banks/dates/ratios EXACT — ticked; only strengthen the criteria wording)

Keep the population sentence (20 banks mid-2023 per \citet{dongol2024}; peak 32 per \citet{adhikari2023}) and the purposive technique. Keep criteria (i)(ii)(iii) verbatim in meaning. Keep the 5-bank list EXACTLY (verified Jan 2023 merger week: Kumari+NCC joint operation 1 Jan 2023 swap 1:1; Global IME+Bank of Kathmandu 9 Jan 2023 swap 1:1; Nepal Investment Mega 11 Jan 2023 swap 100:90; Himalayan+Civil 24 Feb 2023 swap 100:80.28; NMB unmerged — cross-checked against NRB licensed-bank list Jan 2024 + Republica/Annapurna merger reports + NRB merger breakdown PDF):

```latex
The sampled commercial banks, identified by their current legal corporate names, are:
\begin{enumerate}
  \item Global IME Bank Limited (absorbed Bank of Kathmandu, joint operation commenced 9 January 2023, swap ratio 1:1)
  \item Himalayan Bank Limited (acquired Civil Bank, joint operation commenced 24 February 2023, swap ratio 100:80.28)
  \item Kumari Bank Limited (absorbed Nepal Credit and Commerce Bank, joint operation commenced 1 January 2023, swap ratio 1:1)
  \item Nepal Investment Mega Bank Limited (merger of Nepal Investment Bank and Mega Bank, joint operation commenced 11 January 2023, swap ratio 100:90)
  \item NMB Bank Limited (maintained independent operations without merger during the period)
\end{enumerate}
```

Keep the merged-bank rule paragraph (pre = acquirer, post = consolidated; no causal-merger reading) and the FY 2076/77–2081/82 = 30 bank-year sentence unchanged (per `../detail/13_*` circled confirmation).

## Verify after apply

- 1.1.1 first sentence contains both "directly from the research questions" and "secondary panel data ... $N=5$ ... $T=6$".
- 1.1.2 bank names/dates/ratios character-identical to above. Criteria (i)(ii)(iii) present.
