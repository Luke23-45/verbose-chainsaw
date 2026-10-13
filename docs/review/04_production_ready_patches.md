# Production-Ready Implementation Patches

This document provides the exact, production-ready LaTeX replacements for all five files requiring refinement. Applying these blocks directly resolves every vulnerability identified in the supervisor audit.

---

## 1. Patch for `src/proposal/main.tex`

### Target
`src/proposal/main.tex` (lines 68–85)

### Replacement Code
```latex
% --- Front matter (FOM 2019 p.9: Table of contents; p.20: single spacing)
% Title page = i (counted, unnumbered). Front matter = ii bottom centre.
\pagenumbering{roman}
\setcounter{page}{2}
\begingroup
\singlespacing
\tableofcontents
\clearpage
\endgroup

% --- Main body i-vii ---
% Body restarts at arabic 1 per FOM p.21, numbers at top right.
\pagenumbering{arabic}
\setcounter{page}{1}
\fancyhf{}
\fancyhead[R]{\thepage}
\renewcommand{\headrulewidth}{0pt}
```

---

## 2. Patch for `src/proposal/sections/01_background/01_background.tex`

### Target
`src/proposal/sections/01_background/01_background.tex` (Paragraph 4)

### Replacement Code
```latex
The Nepalese banking sector has undergone substantial structural transformation
through the merger and acquisition wave of 2013--2020 and the major consolidation
of early 2023: Global IME Bank absorbed Bank of Kathmandu, Kumari Bank absorbed
Nepal Credit and Commerce Bank, Nepal Investment Bank merged with Mega Bank to form
Nepal Investment Mega Bank, and Himalayan Bank acquired Civil Bank
\citep{nrb2023}. Across the broader financial sector, 239 banking and
financial institutions entered merger processes and 177 ceased to exist in their
own names, with the commercial-bank count falling from 32 in 2014 to 20 by
mid-2023. Sector-wide market price per share fell by roughly 46\% in the
periods following the mergers while earnings per share and dividend per share were
statistically unchanged \citep{adhikari2023,adhikari2023cbr}. Most existing
empirical studies on share prices rely on pre-merger datasets that do not reflect
the restructured banking environment. Furthermore, conflicting findings on ROA
and BVPS across recent studies underscore the need to re-examine the associations
between accounting fundamentals and share prices across a study window spanning
the periods before, during, and after the major 2023 consolidation.
```

---

## 3. Patch for `src/proposal/sections/02_problem_statement/02_problem_statement.tex`

### Target
`src/proposal/sections/02_problem_statement/02_problem_statement.tex` (Enumerate block, lines 29–35)

### Replacement Code
```latex
To address these empirical contradictions and examine the associations between
accounting fundamentals and equity prices, this study formulates the following
specific research questions:
\begin{enumerate}
  \item What are the baseline levels and trends of EPS, DPS, BVPS, ROA, and $\mathit{MPS}^{post}$ in the sampled commercial banks?
  \item How is each accounting fundamental associated with post-disclosure market price per share ($\mathit{MPS}^{post}$)?
  \item To what extent do the four accounting fundamentals jointly explain variations in $\mathit{MPS}^{post}$?
\end{enumerate}
```

---

## 4. Patch for `src/proposal/sections/03_objectives/03_objectives.tex`

### Target
`src/proposal/sections/03_objectives/03_objectives.tex` (Enumerate block, lines 9–15)

### Replacement Code
```latex
To achieve this primary aim, the study sets forth the following specific
objectives:
\begin{enumerate}
  \item To describe the baseline levels and historical trends of EPS, DPS, BVPS, ROA, and $\mathit{MPS}^{post}$ in the sampled commercial banks.
  \item To evaluate the bivariate relationship between each accounting fundamental and $\mathit{MPS}^{post}$.
  \item To estimate the joint explanatory power and conditional effects of the four accounting fundamentals on $\mathit{MPS}^{post}$.
\end{enumerate}
```

---

## 5. Patch for `src/proposal/sections/06_literature_review/06_literature_review.tex`

### Target
`src/proposal/sections/06_literature_review/06_literature_review.tex` (From `\subsection*{Empirical review}` through the end of the file)

### Replacement Code
```latex
\subsection*{Empirical review}

Empirical investigations into equity valuation across commercial banks have established fundamental accounting variables as significant correlates of market prices, yet critical discrepancies persist across sample periods and variable specifications. Internationally, \citet{malhotra2013} demonstrated that book value, earnings per share, and price-earnings multiples serve as positive determinants of equity prices on the National Stock Exchange of India, while dividend yield exhibited an inverse association. Similarly, \citet{almumani2014} confirmed earnings, book value, and price-earnings ratios as dominant positive determinants of commercial bank share prices in the Amman Stock Exchange. In Nepal, early studies by \citet{bhattarai2014} across 2006--2014 and \citet{pradhan2016} across 2002/03--2013/14 established that earnings per share and payout measures correlate positively with bank stock prices, with market size and macroeconomic GDP expansion serving as significant conditioning factors. Subsequent evidence by \citet{bajracharya2019} corroborated the positive explanatory power of earnings and dividends over the period 2006/07--2015/16, while noting that inflation exerts a significant negative drag on secondary equity valuations.

Despite broad consensus regarding the primary role of earnings, empirical findings diverge sharply concerning return on assets (ROA) and book value per share (BVPS). While \citet{joshi2023} documented earnings, dividends, and BVPS as consistently positive and statistically significant determinants across seven commercial banks during 2012/13--2021/22, and \citet{chhetri2023} identified BVPS alongside ROA as dominant positive valuation drivers across a 13-bank panel (2012--2022), other studies report contrary results. Specifically, \citet{niroula2021} found BVPS and return on equity to be negative and statistically insignificant across 18 commercial banks (2015/16--2019/20), while \citet{pant2024} observed that both dividends and BVPS were insignificantly negative across the 2013/14--2023/24 period. Evidence on operational asset efficiency is equally contradictory: \citet{pradhan2016} and \citet{chhetri2023} found ROA to be statistically significant and positive, whereas \citet{gyawali2022} and \citet{bajracharya2019} observed no statistically significant association. Most recently, \citet{chaudhari2025} reported a statistically significant negative coefficient for ROA across a ten-bank panel (2014/15--2023/24), highlighting the empirical necessity for resolution across a consistent post-restructuring observation window.

The institutional and regulatory environment of Nepalese banking introduces additional dimensions that shape equity prices. Regulatory requirements enforced by Nepal Rastra Bank, particularly capital adequacy thresholds and loan-loss provisioning, directly influence reported earnings and valuation multiples \citep{bhattarai2024}. Governance characteristics also condition earnings quality, with empirical evidence demonstrating that capital adequacy and dividend payout enhance earnings, whereas board independence exhibits a weak negative association \citep{dongol2024}. Furthermore, macroeconomic forces including money supply and interest rate fluctuations significantly alter banking valuation dynamics \citep{timalsina2026}. Crucially, the extensive structural consolidation of the banking sector between 2013 and 2020, culminating in the major consolidation wave of early 2023, profoundly altered secondary market valuations: sector-wide market capitalization and share prices fell by approximately 46\% following merger completions due to expanded equity capital bases, whereas core fundamental performance metrics (EPS and DPS) remained statistically unchanged \citep{adhikari2023,adhikari2023cbr}.

\subsection*{Research gap}

The existing literature exhibits three critical limitations that motivate this study. First, the majority of existing empirical studies utilize datasets that terminate prior to the major 2023 consolidation wave, leaving valuation dynamics across the newly restructured banking environment largely unexamined \citep{adhikari2023,chaudhari2025}. Second, empirical findings regarding the valuation impact of ROA and BVPS remain fundamentally contradictory: \citet{chhetri2023} reports ROA as significantly positive, \citet{chaudhari2025} reports it as significantly negative, and \citet{gyawali2022} finds it statistically insignificant; on BVPS, \citet{joshi2023} document a significant positive determinant, whereas \citet{pant2024} report an insignificant negative relationship. Third, numerous prior specifications incorporated the price-earnings (P/E) ratio alongside market price per share \citep{bhattarai2014,chhetri2023}. Because $\text{P/E}$ is mathematically defined as $\text{MPS} / \text{EPS}$, including it creates direct definitional dependence with the dependent variable. This study excludes market multiples to maintain econometric validity.

This study examines a purposively selected sample across FY 2076/77 to FY 2081/82, spanning before, during, and after the major 2023 consolidation, estimating a unified model of EPS, DPS, BVPS, and ROA against post-disclosure equity prices while excluding valuation multiples constructed directly from market prices.
```

---

## 6. Patch for `src/proposal/sections/07_methodology/07_methodology.tex`

### Target
`src/proposal/sections/07_methodology/07_methodology.tex` (From Section 1.1.4 through end of 1.1.5)

### Replacement Code
```latex
\msub{1.1.4 Research framework and definition of variables}
The research framework illustrating the functional relationship between the
explanatory accounting fundamentals and the dependent variable is depicted in
Figure~\ref{fig:framework}. Post-disclosure market price per share
($\mathit{MPS}^{post}$) serves as the dependent variable, while earnings per share
(EPS), dividend per share (DPS), book value per share (BVPS), and return on assets
(ROA) serve as explanatory independent variables.

\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=0.45cm,
  ind/.style={rectangle, draw, minimum width=3.4cm, minimum height=0.7cm, text centered, font=\small},
  dep/.style={rectangle, draw, minimum width=3.6cm, minimum height=1.7cm, text centered, font=\small, fill=gray!10},
  arrow/.style={thick,->,>=stealth}]
  \node[ind] (eps)  {EPS};
  \node[ind, below=of eps] (dps)  {DPS};
  \node[ind, below=of dps] (bvps) {BVPS};
  \node[ind, below=of bvps] (roa) {ROA};
  \path (dps) -- (bvps) coordinate[midway] (mid);
  \node[dep, right=2.2cm of mid] (mps) {$\mathit{MPS}^{\mathit{post}}$};
  \draw[arrow] (eps.east)  -- ([yshift=18pt]mps.west);
  \draw[arrow] (dps.east)  -- ([yshift=6pt]mps.west);
  \draw[arrow] (bvps.east) -- ([yshift=-6pt]mps.west);
  \draw[arrow] (roa.east)  -- ([yshift=-18pt]mps.west);
  \node[above=0.2cm of eps, font=\small\itshape] {Independent variables};
  \node[below=0.25cm of mps, font=\small\itshape] {Dependent variable};
\end{tikzpicture}
\caption{Research framework (Source: adapted from Pradhan and Dahal, 2016)}
\label{fig:framework}
\end{figure}

Post-disclosure market price per share ($\mathit{MPS}^{\mathit{post}}$), measured in Nepalese Rupees (NPR), is the closing market price on the first NEPSE trading day following public disclosure of the corresponding audited annual financial statements through NEPSE, applied consistently across all sampled banks and fiscal years. Earnings per share (EPS), expressed in NPR, is profit attributable to ordinary equity holders divided by the weighted average number of ordinary shares outstanding during the period from the audited annual report. Dividend per share (DPS), expressed in NPR, is total dividend per share distributed for the fiscal year as reported in the audited annual report. Book value per share (BVPS), expressed in NPR, represents total shareholders' equity divided by outstanding common shares from the audited annual report. Return on assets (ROA), expressed as a percentage (\%), represents net profit after tax divided by total assets multiplied by 100 as reported in the audited annual statements.

\needspace{6\baselineskip}
\msub{1.1.5 Methods of analysis}
To examine the empirical relationships and evaluate the hypotheses formulated in
this study, both descriptive and inferential econometric techniques are applied.

\textbf{Model Specification:}
To examine the joint and conditional associations of all four accounting
fundamentals with post-disclosure market price per share, the following multiple
linear regression model is specified:
\begin{equation}
\mathit{MPS}^{post}_{it} = \beta_0 + \beta_1 \mathit{EPS}_{it} + \beta_2 \mathit{DPS}_{it} + \beta_3 \mathit{BVPS}_{it} + \beta_4 \mathit{ROA}_{it} + \varepsilon_{it}
\label{eq:main}
\end{equation}
where $\mathit{MPS}^{post}_{it}$ represents the closing market price observed
at the pre-specified post-disclosure trading date for bank $i$ in fiscal year
$t$. $\mathit{EPS}_{it}$, $\mathit{DPS}_{it}$, $\mathit{BVPS}_{it}$, and
$\mathit{ROA}_{it}$ denote earnings per share, dividend per share, book value
per share, and return on assets, respectively. The parameter $\beta_0$ represents
the intercept, $\beta_1$ through $\beta_4$ represent regression slope coefficients
capturing the estimated conditional association between each regressor and
$\mathit{MPS}^{post}$ holding the other included variables constant, and
$\varepsilon_{it}$ is the stochastic disturbance term.

\textbf{Statistical Tools and Estimation Procedure:}
The empirical analysis follows a structured analytical protocol, applied only after the data qualify for each test:
\begin{enumerate}
  \item \textbf{Descriptive Statistics:} The mean, standard deviation, minimum,
    and maximum of all variables are computed to examine distributional
    properties across the panel.
  \item \textbf{Correlation Analysis:} Pearson correlations measure bivariate
    associations between each fundamental and $\mathit{MPS}^{post}$ and screen
    for collinearity among regressors.
  \item \textbf{Panel Regression Analysis:} The empirical specification (Eq.~\ref{eq:main}) is evaluated through alternative panel modeling techniques:
    \begin{itemize}
      \item \textit{Pooled OLS:} Estimated as the baseline exploratory benchmark assuming cross-sectional homogeneity.
      \item \textit{Fixed Effects Model (FEM):} Accounts for unobserved, time-invariant bank-specific characteristics ($\alpha_i$).
      \item \textit{Random Effects Model (REM):} Assumes bank-specific variations are random disturbances uncorrelated with regressors.
    \end{itemize}
    The Breusch-Pagan Lagrange Multiplier (LM) test evaluates the presence of random individual heterogeneity (Pooled OLS vs. REM). The Hausman specification test evaluates whether individual bank effects correlate with the explanatory variables, determining whether Fixed Effects or Random Effects yields consistent and efficient estimates. The overall explanatory power is evaluated via $R^2$ and adjusted $R^2$, while two-tailed $t$-tests at the 5\% level ($\alpha = 0.05$) evaluate individual coefficient significance, and the $F$-test evaluates overall model significance.
  \item \textbf{Diagnostic Tests:} Model assumptions are examined before interpreting results.
    Multicollinearity is evaluated with variance inflation factors (VIF) and tolerance statistics alongside the correlation matrix.
    Residual diagnostics include examinations for heteroskedasticity (White / Breusch-Pagan) and
    screening for influential observations using Cook's distance. Normality of residuals is inspected via Q-Q plots.
    With $N=5$ banks and $T=6$ years, inference is interpreted cautiously given repeated
    within-bank observations, and small-sample limitations are explicitly
    acknowledged. If diagnostics show that classical spherical disturbance assumptions are violated, Huber-White robust standard errors or clustered standard errors by bank are reported and the limitation is explicitly stated.
\end{enumerate}

Data organization, coding, and descriptive statistics are conducted using Microsoft Excel and the Statistical Package for the Social Sciences (SPSS). Panel econometric estimations, diagnostic specification tests (Breusch-Pagan LM and Hausman tests), and panel regression models are estimated using EViews and Stata.
```
