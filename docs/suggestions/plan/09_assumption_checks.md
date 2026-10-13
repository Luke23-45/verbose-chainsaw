# Plan 09 — Qualify-for-test / assumption checks (professor sketch bottom note)

Source: `../detail/16_handdrawn_framework_guide.md` ("qualify for test ?? -> checking (Assumption fulfill भएको छ कि छैन)") + `../detail/15_methodology_stats_tools_p10.md` (tick + Diagnostic loop + cautiously underline)
Target: `src/proposal/sections/07_methodology/07_methodology.tex` — `\msub{1.1.5 Methods of analysis}` enumerated plan (items 1–4) + closing SPSS/Excel sentence. Eq.(1) untouched.

## Paste-ready LaTeX (replaces the 4-item estimation procedure + closing software sentence)

```latex
\needspace{6\baselineskip}
\msub{1.1.5 Methods of analysis}
To examine the empirical relationships and evaluate the hypotheses formulated in
this study, both descriptive and inferential statistical techniques are applied.

\textbf{Model Specification:}
To examine the joint and conditional associations of all four accounting
fundamentals with post-disclosure market price per share, the following multiple
linear regression model is estimated:
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
The empirical analysis follows a structured analytical plan, applied only after the data qualify for each test:
\begin{enumerate}
  \item \textbf{Descriptive Statistics:} The mean, standard deviation, minimum,
    and maximum of all variables are computed to examine distributional
    properties across the panel.
  \item \textbf{Correlation Analysis:} Pearson correlations measure bivariate
    associations between each fundamental and $\mathit{MPS}^{post}$ and screen
    for collinearity among regressors.
  \item \textbf{Multiple Regression Analysis:} The multiple linear regression
    model (Eq.~\ref{eq:main}) is estimated using Ordinary Least Squares (OLS).
    The overall explanatory power is evaluated via the coefficient of
    determination ($R^2$) and adjusted $R^2$. Although the research hypotheses
    specify positive directional associations, two-tailed $t$-tests at the 5\%
    significance level are used for conservative statistical inference, while
    the $F$-test at 5\% ($\alpha = 0.05$) evaluates overall model significance.
  \item \textbf{Diagnostic Tests:} Model assumptions are examined before interpreting results.
    Multicollinearity is evaluated with variance inflation factors and tolerance statistics alongside the correlation matrix.
    Residual diagnostics include examinations for heteroskedasticity (White / Breusch-Pagan) and
    screening for influential observations using Cook's distance. Normality of residuals is inspected via Q-Q plots.
    With $N=5$ banks and $T=6$ years, pooled OLS serves as the baseline exploratory
    specification, inference is interpreted cautiously given repeated
    within-bank observations, and small-sample limitations are explicitly
    acknowledged. If diagnostics show assumptions are not fulfilled, robust or clustered-by-bank standard errors are reported and the limitation is stated rather than hidden.
\end{enumerate}

All data organization, coding, and econometric estimations are conducted using
the Statistical Package for the Social Sciences (SPSS) and Microsoft Excel.
```

## What changed vs current text (so nothing hides)

- Added the qualify-for-test gate ("applied only after the data qualify for each test").
- Named White / Breusch-Pagan for heteroskedasticity + Q-Q plots for normality (current text said only "examinations for heteroskedasticity" — now testable).
- Added the fulfilled-or-not rule ("If diagnostics show assumptions are not fulfilled, robust or clustered-by-bank standard errors are reported and the limitation is stated").
- Everything else (R², two-tailed t at 5%, F at 5%, VIF/tolerance, Cook's distance, N=5/T=6 pooled-OLS caution, SPSS+Excel) kept verbatim — these were ticked/accepted.

## Verify after apply

- 1.1.5 contains "qualify", "White / Breusch-Pagan", "Q-Q", "clustered-by-bank", "N=5", "T=6", "SPSS", "Excel".
- Eq.(1) + where-paragraph byte-identical. Build 0 errors.
