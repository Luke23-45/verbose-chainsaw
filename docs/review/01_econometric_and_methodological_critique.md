# Econometric and Methodological Critique

This document addresses the most dangerous technical vulnerability in the proposal: the methodology section, specifically deconstructing the supervisor's red-pen query: **`"Panel data ??"`** (page 7 of the reviewed draft, `detail/12`).

---

## 1. Deconstructing the `"Panel data ??"` Query

On page 7 of the reviewed draft, the supervisor underlined `"Panel data"` twice and wrote `"??"`. 

### Why the Supervisor Questioned This
In academic finance and econometrics, a researcher cannot simply invoke the phrase *"secondary panel data"* without providing the formal econometric framework that defines and tests panel structures. 

Currently, the proposal states:
> *"The data are a panel: the same $N=5$ banks observed over the same $T=6$ fiscal years (FY 2076/77 to FY 2081/82), yielding $5 \times 6 = 30$ bank-year observations. Pooled OLS is the baseline exploratory specification... All data organization, coding, and econometric estimations are conducted using the Statistical Package for the Social Sciences (SPSS) and Microsoft Excel."*

Any thesis examiner who teaches Econometrics or Quantitative Research Methods at Tribhuvan University will immediately raise three fatal objections:

1. **The Homogeneity Fallacy of Pooled OLS:**  
   Pooled OLS pools all 30 bank-year observations into a single cross-section, assuming that all banks share an identical intercept ($\beta_0$) and that unobserved bank-specific heterogeneity is zero. In banking reality, banks differ dramatically in management quality, digital adoption, risk appetite, brand loyalty, and branch networks (unobserved bank-specific effects $\alpha_i$). If these bank-specific characteristics correlate with the explanatory fundamentals, **Pooled OLS yields biased and inconsistent estimates**.
2. **Missing Panel Specification Tests:**  
   If a study uses panel data, the examiner expects to see:
   - **The Chow / Redundant Fixed Effects Test ($F$-test):** Testing Pooled OLS against the Fixed Effects Model.
   - **The Breusch-Pagan Lagrange Multiplier (LM) Test:** Testing Pooled OLS against the Random Effects Model.
   - **The Hausman Specification Test:** The definitive test to decide whether the Fixed Effects Model (FE) or Random Effects Model (RE) is the consistent estimator.
3. **The Software Exposure (The "SPSS" Trap):**  
   Standard SPSS has **no native panel econometric estimation module**. It cannot perform the Breusch-Pagan LM test or the Hausman specification test without advanced custom Python/R integration scripts. Every professor at TU knows that empirical panel finance theses in Nepal are estimated in **EViews** or **Stata** (or R), while SPSS is used primarily for basic cross-sectional surveys, descriptive statistics, and bivariate correlations. Claiming to run an entire panel data econometric analysis in SPSS signals to the committee that the candidate does not understand panel data tools.

---

## 2. Sample Size, Degrees of Freedom, and Statistical Power

The proposal specifies a balanced panel:
- Cross-sectional units: $N = 5$ commercial banks
- Time periods: $T = 6$ fiscal years (FY 2076/77 to FY 2081/82)
- Total observations: $N \times T = 30$ bank-year observations

### Econometric Parameter Constraints
The multiple regression equation is:
$$\mathit{MPS}^{post}_{it} = \beta_0 + \beta_1 \mathit{EPS}_{it} + \beta_2 \mathit{DPS}_{it} + \beta_3 \mathit{BVPS}_{it} + \beta_4 \mathit{ROA}_{it} + \varepsilon_{it}$$

- Number of estimated parameters: $k + 1 = 5$ ($\beta_0, \beta_1, \beta_2, \beta_3, \beta_4$).
- **Residual Degrees of Freedom in Pooled OLS:** $30 - 5 = 25$ degrees of freedom.
- **Residual Degrees of Freedom in Fixed Effects (Within-Transformation):**  
  In a one-way Fixed Effects model with bank dummy variables, $N - 1 = 4$ bank intercepts are estimated. The remaining degrees of freedom become $N \times T - N - k = 30 - 5 - 4 = 21$ degrees of freedom.

### The Defense Argument
A hostile committee member may argue: *"Thirty observations is too small for multiple regression."*  
The candidate must be armed with a clear, published defense:
1. **Green (1991) Rule of Thumb:** $N \ge 50 + 8k$ for testing $R^2$, and $N \ge 104 + k$ for testing individual regressors. However, in emerging market banking where total population is capped at 20 banks, **asymptotic sample sizes are impossible**.
2. **Purposive Population Coverage:** The 5 sampled banks account for **over 35% of total commercial banking assets and deposits in Nepal** following the 2023 consolidations. The sample represents economic concentration, not statistical randomness.
3. **Exploratory Pooled OLS with Diagnostics:** Acknowledge openly that $N=30$ is an exploratory panel sample. By declaring that Pooled OLS is evaluated alongside Fixed/Random Effects and backed by **Huber-White robust standard errors** or **clustered standard errors by bank**, the candidate disarms the critique before the examiner can speak.

---

## 3. The Professional Panel Workflow to Add to Section 1.1.5

To make the methodology bulletproof, Section 1.1.5 must formally outline the three-stage panel estimation protocol:

```
[STAGE 1: MODEL SPECIFICATIONS]
1. Pooled OLS Model: Assumes uniform intercept across banks.
2. Fixed Effects Model (FEM): Controls for unobserved, time-invariant bank heterogeneity (\alpha_i).
3. Random Effects Model (REM): Assumes individual bank effects are random disturbances uncorrelated with regressors.

[STAGE 2: MODEL SELECTION TESTS]
1. F-Test / Likelihood Ratio Test: Tests Pooled OLS (H_0) vs. Fixed Effects (H_1).
2. Breusch-Pagan LM Test: Tests Pooled OLS (H_0) vs. Random Effects (H_1).
3. Hausman Specification Test: 
   - Null Hypothesis (H_0): Random Effects are consistent and efficient (Cov(\alpha_i, X_it) = 0).
   - Alternative Hypothesis (H_1): Random Effects are inconsistent; Fixed Effects model is required.
   - Decision Rule: If p < 0.05, reject H_0 and report Fixed Effects; if p >= 0.05, retain Random Effects.

[STAGE 3: RESIDUAL & ASSUMPTION DIAGNOSTICS]
1. Multicollinearity: Variance Inflation Factors (VIF < 10) and tolerance (> 0.1).
2. Heteroskedasticity: Modified Wald test for groupwise heteroskedasticity in panel data / White's test.
3. Panel Autocorrelation: Wooldridge test for serial correlation in panel models.
4. Normality: Jarque-Bera test and Q-Q plots of standardized residuals.
5. Robust Standard Errors: Reporting Huber-White cluster-robust standard errors if heteroskedasticity or serial correlation is detected.
```

---

## 4. Software Rectification

In the closing sentence of Section 1.1.5, replace the SPSS-only claim with the industry-standard multi-tool statement:

> *"Data compilation, variable transformation, and descriptive statistics are performed using Microsoft Excel and SPSS. Panel econometric estimations, diagnostic tests (Breusch-Pagan LM, Hausman test), and panel regression models are estimated using EViews / Stata."*

This simple adjustment transforms the methodology from an amateur draft into a professional, graduate-level econometrics submission.
