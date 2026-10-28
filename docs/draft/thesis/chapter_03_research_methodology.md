# CHAPTER III: RESEARCH METHODOLOGY

## 3.1 Introduction

Scientific research in empirical finance and financial accounting is distinguished by the formalization, transparency, and reproducibility of its methodological design. The research methodology establishes the systematic protocol through which research questions are investigated, theoretical constructs are operationalized into observable metrics, empirical data are collected and audited, and statistical models are specified and estimated. A rigorous methodology allows subsequent researchers to replicate the findings, verify empirical claims, and evaluate the econometric robustness of reported inferences.

This chapter sets out the comprehensive research methodology employed to investigate the value relevance of accounting information across Nepal's 2023 commercial banking consolidation wave. Structured in strict compliance with the *Master's Degree Dissertation Guidelines (2019)* of the Faculty of Management, Tribhuvan University (pp. 13–14), this chapter is organized into five interrelated sections:
* **Section 3.2: Research Design** outlines the epistemological and econometric architecture of the study, specifying its quantitative, correlational, comparative, and longitudinal panel dimensions.
* **Section 3.3: Population, Sample, and Sampling Procedure** defines the commercial banking population, justifies the purposive sampling design, presents the institutional profiles of the five selected bank series, discloses the 5-day freshness rule for trading records, and presents the realized price observation matrix.
* **Section 3.4: Nature and Sources of Data, and Data Collection Procedure** details the primary financial statement inputs, market price series aggregators, regulatory publications, and the audit reconciliation protocols utilized to verify data integrity.
* **Section 3.5: Research Framework and Definition of Variables** delineates the conceptual valuation framework, establishes the operational definitions and measurement rules for dependent, independent, moderating, and robustness variables, and justifies the mathematical exclusion of price-derived ratios (P/E).
* **Section 3.6: Methods of Analysis and Econometric Specification** details the baseline (Model 1) and regime-shift (Model 2) two-way fixed-effects panel regression models, formulates the MacKinnon-White HC3 robust inference procedure, accounts for finite-sample degrees of freedom, outlines econometric diagnostic tests, and specifies the eight-part robustness suite.

---

## 3.2 Research Design

This study adopts a quantitative, correlational, and comparative longitudinal panel research design utilizing secondary financial accounting and capital market data (Pant, 2016). The design is explicitly aligned with the research questions and objectives formulated in Chapter I:
1. **Quantitative and Correlational:** The study operationalizes fundamental accounting metrics—earnings per share (EPS), book value per share (BVPS), return on assets (ROA), and dividend per share (DPS)—and evaluates their statistical associations with secondary market equity closing prices ($\mathit{MPS}^{RD}$) using parametric correlation matrices and linear regression estimation.
2. **Comparative and Longitudinal Panel:** The research design tracks five commercial banking institutions across six consecutive fiscal years, spanning FY 2076/77 (2019/20) through FY 2081/82 (2024/25). This longitudinal dimension allows the study to compare valuation relationships across two distinct calendar and institutional regimes: the pre-consolidation period (FY 2076/77–2078/79, $n = 13$ clean observations) and the post-consolidation period (FY 2079/80–2081/82, $n = 15$ clean observations).
3. **Observational and Non-Experimental:** Because the researcher does not manipulate corporate financial decisions, assign institutions to merger treatments, or intervene in market price formation, the investigation is non-experimental and observational. In accordance with rigorous econometric principles, parameter estimates are interpreted as conditional statistical associations rather than as causal merger impacts.
4. **Two-Way Fixed-Effects Framework:** To mitigate potential omitted-variable bias, the core empirical architecture implements a two-way fixed-effects panel model incorporating unobserved time-invariant bank fixed effects ($\mu_i$) and common fiscal-year fixed effects ($\lambda_t$). Bank fixed effects control for persistent differences in institutional reputation, corporate governance, risk appetite, and historical branch networks. Fiscal-year fixed effects absorb market-wide macroeconomic shocks, shifts in monetary policy, inflation cycles, and broad NEPSE equity index movements. Consequently, slope coefficients are identified exclusively from within-year cross-sectional variation among the sampled commercial banks.
5. **Exploratory Finite-Sample Inference:** Recognizing the small cross-sectional dimension ($N = 5$ banking series, $G = 5$ clusters), the research design explicitly disclaims asymptotic certainty. Inference is structured around MacKinnon-White HC3 heteroskedasticity-robust standard errors with transparent reporting of finite-sample degrees of freedom, providing an exploratory, honest assessment of parameter uncertainty.

---

## 3.3 Population, Sample, and Sampling Procedure

### 3.3.1 Population of the Study
The target population for this study comprises all commercial banks licensed by Nepal Rastra Bank as Class 'A' financial institutions operating in the Federal Democratic Republic of Nepal. Over the past decade, successive consolidation mandates executed by NRB dramatically compressed the commercial banking sector from an apex of 32 institutions in FY 2011/12 to 20 commercial banks by mid-October 2023 (Asoj 2080 BS) (NRB, 2023). These 20 licensed institutions constitute the universal population of the modern Nepalese commercial banking industry.

### 3.3.2 Sampling Method and Selection Criteria
From the total population of 20 licensed commercial banks, a purposive (judgmental) sample of five commercial bank series is selected. Purposive sampling is mathematically and conceptually appropriate because the core research objective focuses specifically on evaluating accounting value relevance across the prominent commercial banking consolidations that reshaped the financial sector in early 2023, while requiring longitudinal data continuity across both pre- and post-merger regimes.

The specific sampling criteria applied to select the institutions are:
1. **Participation in the 2023 Consolidation Wave:** Prominent commercial bank series that executed horizontal statutory amalgamations or major corporate acquisitions that commenced joint commercial operations during the early-2023 consolidation wave (January–February 2023 / mid-FY 2079/80).
2. **Benchmark Series Continuity:** Inclusion of an established Class 'A' commercial bank that did not participate in the early-2023 consolidation wave, providing a contemporaneous, unmerged benchmark series to differentiate sector-wide market trends from merger-specific structural shifts.
3. **Longitudinal Data Availability and Regulatory Compliance:** Availability of complete, audited annual financial statements across all six fiscal years (FY 2076/77 to FY 2081/82) prepared in accordance with Nepal Financial Reporting Standards (NFRS) and submitted to Nepal Rastra Bank.
4. **Secondary Market Trading Continuity:** Continuous active listing on the Nepal Stock Exchange (NEPSE) with secondary trading records that satisfy the study's post-deadline freshness window.

### 3.3.3 Profile of the Sampled Commercial Banks
The five purposively selected commercial bank series, identified by their current corporate names, are:

1. **Global IME Bank Limited (GBIME):**
   * *Consolidation Status:* Amalgamated with Bank of Kathmandu Limited (BOK).
   * *Effective Joint Operation Date:* 9 January 2023 (25 Poush 2079 BS).
   * *Consolidation Mechanism:* Statutory merger with an equity share swap ratio of 1:1. Following amalgamation, GBIME emerged as the largest commercial bank in Nepal by total asset scale and paid-up equity capital (Global IME Bank, 2022; NRB, 2023).
   * *Pre-Merger Entity:* Global IME Bank Limited standalone operations.

2. **Himalayan Bank Limited (HBL):**
   * *Consolidation Status:* Acquired Civil Bank Limited.
   * *Effective Joint Operation Date:* 24 February 2023 (12 Falgun 2079 BS).
   * *Consolidation Mechanism:* Statutory acquisition with an equity share swap ratio of 100:80.28 (100 shares of Civil Bank exchanged for 80.28 shares of HBL). The acquisition substantially expanded HBL's domestic retail deposit base and branch network (Himalayan Bank, 2023; NRB, 2023).
   * *Pre-Merger Entity:* Himalayan Bank Limited standalone operations.

3. **Kumari Bank Limited (KBL):**
   * *Consolidation Status:* Amalgamated with Nepal Credit and Commerce Bank Limited (NCC Bank).
   * *Effective Joint Operation Date:* 1 January 2023 (17 Poush 2079 BS).
   * *Consolidation Mechanism:* Statutory horizontal amalgamation with an equity share swap ratio of 1:1, combining complementary branch networks across semi-urban and commercial centers (Kumari Bank, 2022; NRB, 2023).
   * *Pre-Merger Entity:* Kumari Bank Limited standalone operations.

4. **Nepal Investment Mega Bank Limited (NIMB):**
   * *Consolidation Status:* Amalgamation of Nepal Investment Bank Limited (NIB) and Mega Bank Nepal Limited.
   * *Effective Joint Operation Date:* 11 January 2023 (27 Poush 2079 BS).
   * *Consolidation Mechanism:* Statutory horizontal amalgamation with an equity share swap ratio of 100:90 (100 shares of Mega Bank exchanged for 90 shares of NIB), creating one of the largest corporate banking portfolios in the country (Nepal Investment Mega Bank, 2023; NRB, 2023).
   * *Pre-Merger Entity:* Nepal Investment Bank Limited (NIB) standalone operations.

5. **NMB Bank Limited (NMB):**
   * *Consolidation Status:* Did not participate in the early-2023 consolidation wave, serving as the benchmark series for the 2023 restructuring.
   * *Corporate History Note:* NMB acquired Kanchan Development Bank Limited in August 2020 (Bhadra 2077 BS), adding approximately NPR 0.57 billion to share capital in FY 2077/78. However, its core corporate identity, executive management, and operational boundaries remained continuous and unmerged throughout the early-2023 consolidation wave (NRB, 2023).

### 3.3.4 Sample Size, Missingness Protocol, and Realized Observations
The research protocol targets 30 potential bank-year observations, comprising five commercial bank series tracked over six fiscal years (FY 2076/77 to FY 2081/82). Primary audited annual financial reports are complete for all 30 bank-years ($100\%$ accounting coverage).

However, in secondary equity pricing, corporate restructuring frequently induces prolonged trading halts. To ensure empirical integrity, the study enforces a strict **five-day calendar freshness rule**:
> *If a security was suspended from trading or recorded zero valid transactions within a five-day calendar window following the statutory reporting deadline (end of Chaitra / mid-April), the observation is coded as missing and excluded from the regression sample. It is never imputed from stale pre-suspension prices.*

Two bank-year observations fail this freshness rule due to prolonged merger-related trading suspensions:
1. **Himalayan Bank Limited (HBL) FY 2077/78:** Trading in HBL shares was suspended on NEPSE during complex tripartite merger negotiations with Nepal Investment Bank. Trading remained suspended until 6 June 2022 (Jestha 2079 BS), representing a resumption delay of 54 days beyond the target deadline of 13 April 2022.
2. **Nepal Investment Mega Bank Limited (NIMB, formerly NIB) FY 2077/78:** Trading in NIB shares was concurrently suspended during the same negotiation process, resuming on 30 May 2022 (Jestha 2079 BS), representing a resumption delay of 47 days beyond the 13 April 2022 deadline.

Consequently, these two observations are coded as missing, leaving a realized clean estimation sample of **$N = 28$ observations** (13 pre-consolidation bank-years and 15 post-consolidation bank-years).

Table 3.1 reports the complete panel matrix of observation dates, closing market share prices, trading status, and entity timing notes across all 30 bank-years.

**Table 3.1: Realized $MPS^{RD}$ Observation Dates, Market Closing Prices, and Trading Status**

| Fiscal Year | Observation Date | GBIME | HBL | KBL | NIMB | NMB |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **FY 2076/77** | 13 April 2021 | 450.00 | 520.00 | 328.00 | 466.00 | 437.00 |
| **FY 2077/78** | 13 April 2022 | 299.70 | *Missing*$^a$ | 222.00 | *Missing*$^b$ | 293.00 |
| **FY 2078/79** | 13 April 2023 | 189.00$^c$ | 231.00$^c$ | 176.00$^c$ | 191.00$^c$ | 235.00 |
| **FY 2079/80** | 14 April 2024$^d$ | 179.00 | 183.00 | 136.90 | 156.00 | 176.00 |
| **FY 2080/81** | 13 April 2025 | 218.69 | 231.07 | 206.03 | 211.51 | 251.13 |
| **FY 2081/82** | 13 April 2026 | 238.00 | 208.50 | 229.00 | 210.70 | 248.40 |

*Notes:*
* Prices are expressed in Nepalese Rupees (NPR) per ordinary share, retrieved from capital market data aggregators (ShareSansar and Merolagani; cross-checked against FinancialNotices for FY 2081/82) and verified against NEPSE trading records.
* $^a$HBL merger-related trading suspension until 6 June 2022 (54 days late; gap > 5 days; coded as missing under freshness rule).
* $^b$NIMB (formerly NIB) trading suspension until 30 May 2022 (47 days late; gap > 5 days; coded as missing under freshness rule).
* $^c$Entity timing transition mismatch: accounting fundamentals reflect pre-merger standalone operations, whereas April 2023 prices reflect post-merger consolidated trading (mergers commenced January–February 2023). Retained in baseline; evaluated in Sensitivity Check R6.
* $^d$Chaitra-end fell on Friday, 12 April 2024; Sunday, 14 April 2024 was the first subsequent NEPSE trading session (gap = 2 calendar days, clean).
* Total realized sample size: $N = 28$ observations (13 pre-consolidation, 15 post-consolidation).

---

## 3.4 Nature and Sources of Data, and Data Collection Procedure

### 3.4.1 Nature of Data
This dissertation relies exclusively on quantitative secondary data extracted from audited financial disclosures and official secondary capital market trading archives. The empirical dataset comprises two primary streams of financial information:
1. **Audited Financial Accounting Data:** Comprehensive annual financial metrics—specifically basic earnings per share, total equity attributable to equity holders, ordinary shares outstanding, profit after tax, average total assets, and recommended cash dividends per share.
2. **Secondary Market Trading Data:** Daily equity transaction records—specifically closing market share prices, trade dates, trading volume, and official corporate trading suspension and resumption notices on NEPSE.

### 3.4.2 Sources of Data Collection
To ensure institutional credibility and empirical accuracy, data sources are bifurcated into primary empirical inputs and contextual regulatory publications:

**Primary Empirical Data Sources:**
* *Audited Annual Financial Reports:* Statements of Financial Position (Balance Sheets), Statements of Profit or Loss (Income Statements), Statements of Changes in Equity, and accompanying Notes to Accounts extracted directly from the published annual reports of Global IME Bank, Himalayan Bank, Kumari Bank, Nepal Investment Mega Bank, and NMB Bank.
* *Capital Market Data Aggregators:* Secondary closing market share prices retrieved from established capital market aggregators (ShareSansar, Merolagani, and FinancialNotices), cross-checked against historical price archives and company filing records.

**Contextual and Regulatory Data Sources:**
* *Nepal Rastra Bank (NRB):* Annual Banking and Financial Statistics, licensed financial institution directories, Bank and Financial Institutions Merger and Acquisition Bylaws, and circulars issued by the Bank Supervision Department.
* *Securities Board of Nepal (SEBON):* Annual reports, Capital Market Trends publications, and corporate disclosure directives.
* *Ministry of Finance (MoF), Government of Nepal:* *Economic Survey* publications (FY 2076/77 through FY 2081/82).

### 3.4.3 Data Audit, Extraction, and Reconciliation Protocol
All secondary data were processed through a multi-stage audit and verification protocol to ensure zero data transcription error:
1. **Primary Audit Verification:** All fundamental accounting variables (EPS, equity, ordinary shares, net profit, total assets, DPS) were manually extracted from original audited annual reports and verified across balance sheet and income statement schedules.
2. **Reconciliation Against Aggregators:** Figures compiled from financial aggregators were cross-referenced against original audited PDF reports. In all instances of discrepancy, figures were resolved strictly in favor of the originating audited financial accounts.
3. **Cross-Aggregator Price Reconciliation:** For every bank-year observation, closing market share prices on the target date were compared across ShareSansar and Merolagani (and FinancialNotices for FY 2081/82). Out of 30 target cells, 29 demonstrated perfect zero-variance matching; the single minor discrepancy (NMB FY 2076/77, Merolagani 437.00 vs. ShareSansar 436.00) was arbitrated and verified at NPR 437.00 based on NEPSE floor trading archives.
4. **Trading Status and Freshness Verification:** Daily trading status was screened across the calendar window following the reporting deadline to identify trading halts, record dates, and resumption sessions.

---

## 3.5 Research Framework and Definition of Variables

### 3.5.1 Conceptual Framework
The conceptual framework guiding this research synthesizes the residual income valuation theory of Ohlson (1995) and the post-merger valuation model of Kwon and Wang (2020). The framework is diagrammatically conceptualized below:

```
+------------------------------------+
|  Fundamental Accounting Regressors |
|  - Earnings Per Share (EPS)        |
|  - Book Value Per Share (BVPS)     |
+------------------------------------+
                   |
                   | Baseline Slopes (beta_E, beta_B)
                   v
+------------------------------------+           +------------------------------------+
|        Dependent Variable          | < - - - - |   Consolidation Period Moderator   |
|   Market Price per Share at        |           |   (Post_t: Pre = 0 vs. Post = 1)   |
|   Reporting Deadline (MPS^RD)      |           |   Shift Slopes (delta_E, delta_B)  |
+------------------------------------+           +------------------------------------+
                   ^
                   | Fixed Effects Controls
+------------------------------------+
|  Econometric Controls              |
|  - Bank Fixed Effects (mu_i)       |
|  - Fiscal-Year Fixed Effects (l_t) |
+------------------------------------+
```

In this framework, secondary market closing price at the reporting deadline ($\mathit{MPS}^{RD}$) serves as the outcome variable. Earnings per share (EPS) and book value per share (BVPS) are the primary independent fundamental regressors. The consolidation period indicator ($\mathit{Post}_t$) acts as a temporal moderating indicator, interacting with EPS and BVPS to test for structural parameter shifts ($\delta_E, \delta_B$) across the consolidation wave. Bank fixed effects ($\mu_i$) and fiscal-year fixed effects ($\lambda_t$) control for time-invariant institutional heterogeneity and market-wide macroeconomic trends.

### 3.5.2 Operational Definition and Measurement of Variables

#### 1. Dependent Variable
* **Market Price per Share at Reporting Deadline ($\mathit{MPS}^{RD}$):**
  * *Definition:* The closing secondary market trading price for ordinary shares, measured in Nepalese Rupees (NPR), recorded on the first trading session on the Nepal Stock Exchange (NEPSE) following the statutory nine-month audited annual reporting publication deadline established under Section 59(2) of the Banks and Financial Institutions Act, 2017 (Government of Nepal, 2017).
  * *Operational Measurement:* Operationalized at the end of Chaitra (mid-April) of the subsequent fiscal year. If the deadline falls on a weekend, public holiday, or trading halt, price is recorded on the first active trading session within a 5-day calendar window. Observations exceeding the 5-day window are coded as missing.
  * *Theoretical Rationale:* Unlike Ashadh-end prices (which introduce look-ahead bias) or reconstructed disclosure timestamps (which introduce measurement noise), $\mathit{MPS}^{RD}$ provides a standardized, objective observation window where audited financial accounts were legally required to be public.

#### 2. Primary Independent Variables
* **Earnings per Share (EPS):**
  * *Definition:* Basic earnings per ordinary share, expressed in NPR, extracted from each bank's own audited Statement of Profit or Loss (the own-current reported basic EPS rule).
  * *Operational Measurement:* Calculated as net profit after tax attributable to ordinary equity holders divided by the weighted-average number of ordinary shares outstanding during the fiscal year:
    $$\mathit{EPS}_{it} = \frac{\text{Net Profit Attributable to Equity Holders}_{it}}{\text{Weighted Average Number of Ordinary Shares}_{it}}$$
  * *Restatement Rule:* Retrospective audited restatements reported in subsequent annual reports (for bonus issues or share splits) are retained for sensitivity analysis rather than overwriting original audited figures, preserving the exact information set available to market participants at the reporting date.

* **Book Value per Share (BVPS):**
  * *Definition:* Net asset value per ordinary share, expressed in NPR, reflecting the net worth backing of each ordinary equity share at fiscal year-end.
  * *Operational Measurement:* Recomputed directly from audited Statement of Financial Position components as total ordinary shareholders' equity attributable to equity holders divided by the total number of ordinary shares outstanding at fiscal year-end:
    $$\mathit{BVPS}_{it} = \frac{\text{Total Equity Attributable to Ordinary Equity Holders}_{it}}{\text{Total Number of Ordinary Shares Outstanding at Year-End}_{it}}$$
  * *Reconciliation Rule:* Printed Net Asset Value (NAV) per share reported in bank financial highlights is utilized as an audit reconciliation check against recomputed balance-sheet net worth.

#### 3. Moderating / Interaction Variable
* **Consolidation Period Indicator ($\mathit{Post}_t$):**
  * *Definition:* A binary temporal indicator variable reflecting the structural regime shift of the early-2023 banking consolidation wave.
  * *Operational Measurement:* Formulated as:
    $$\mathit{Post}_t = \begin{cases} 0 & \text{for pre-consolidation fiscal years (FY 2076/77, 2077/78, 2078/79)} \\ 1 & \text{for post-consolidation fiscal years (FY 2079/80, 2080/81, 2081/82)} \end{cases}$$
  * *Interaction Terms:* Interacts with EPS ($\mathit{EPS}_{it} \times \mathit{Post}_t$) and BVPS ($\mathit{BVPS}_{it} \times \mathit{Post}_t$) to estimate parameter differences ($\delta_E, \delta_B$) across regimes.

#### 4. Supplementary and Robustness Variables
* **Return on Assets (ROA):**
  * *Definition:* Operating profitability expressed as net profit after tax divided by average total assets, expressed as a percentage:
    $$\mathit{ROA}_{it} = \left(\frac{\text{Profit After Tax}_{it}}{\text{Average Total Assets}_{it}}\right) \times 100$$
  * *Econometric Treatment:* Evaluated in Specification R3 as an asset-scaled substitute for EPS. Because EPS and ROA correlate at $r = 0.975$ (variance inflation factor $\approx 30$), they are never co-included in the same regression to prevent severe multicollinearity.
* **Dividend per Share (DPS):**
  * *Definition:* Cash dividend recommended per ordinary share, expressed in NPR, for the corresponding fiscal year.
  * *Operational Measurement:* Evaluated in Specification R4, including only eligible cash dividends that were officially declared on or prior to the $\mathit{MPS}^{RD}$ observation date. Documented zero-dividend decisions are recorded as zero; unannounced dividends are treated as missing.

#### 5. Strict Exclusion of Price-Derived Multiples
The Price-to-Earnings (P/E) ratio is strictly excluded from all regression models. As mathematically proved in Section 2.2.6, because $\text{P/E} = \text{MPS} / \text{EPS}$, regressing MPS on P/E introduces circular algebraic endogeneity that biases coefficients and spuriously inflates explanatory power.

---

## 3.6 Methods of Analysis and Econometric Specification

The empirical protocol is executed through descriptive statistics, bivariate correlation diagnostics, fixed-effects panel regressions, finite-sample inference adjustments, and an eight-part robustness suite.

### 3.6.1 Model 1: Baseline Value Relevance Model
To evaluate the baseline value relevance of accounting fundamentals (Hypotheses $H_1$ and $H_2$), Model 1 specifies a two-way fixed-effects panel regression:
$$\mathit{MPS}^{RD}_{it} = \alpha + \mu_i + \lambda_t + \beta_E \mathit{EPS}_{it} + \beta_B \mathit{BVPS}_{it} + \varepsilon_{it}$$
where:
* $i = 1, \dots, 5$ indexes the five commercial bank series;
* $t = 1, \dots, 6$ indexes the six fiscal years;
* $\mathit{MPS}^{RD}_{it}$ is the secondary market closing price observed at the post-reporting-deadline window;
* $\mathit{EPS}_{it}$ is basic earnings per share from own audited SOPL;
* $\mathit{BVPS}_{it}$ is recomputed book value per share at fiscal year-end;
* $\mu_i$ represents unobserved time-invariant bank fixed effects (estimated via 4 bank dummy variables, with GBIME as reference);
* $\lambda_t$ represents common fiscal-year fixed effects (estimated via 5 year dummy variables, with FY 2076/77 as reference);
* $\beta_E$ and $\beta_B$ are the baseline valuation slopes for EPS and BVPS;
* $\varepsilon_{it}$ is the idiosyncratic disturbance term.

### 3.6.2 Model 2: Consolidation-Period Regime Shift Model
To test whether accounting value relevance differed before and after the banking consolidation wave (Hypotheses $H_3$ and $H_4$), Model 2 introduces interaction terms between accounting fundamentals and the consolidation indicator:
$$\mathit{MPS}^{RD}_{it} = \alpha + \mu_i + \lambda_t + \beta_E \mathit{EPS}_{it} + \beta_B \mathit{BVPS}_{it} + \delta_E (\mathit{EPS}_{it} \times \mathit{Post}_t) + \delta_B (\mathit{BVPS}_{it} \times \mathit{Post}_t) + \varepsilon_{it}$$

#### Econometric Note on Standalone Post Absorption:
Because Model 2 includes a full set of fiscal-year fixed effects ($\lambda_t$), the standalone consolidation indicator ($\mathit{Post}_t$) is a deterministic linear combination of the post-consolidation year dummy indicators:
$$\mathit{Post}_t = \lambda_{2079/80} + \lambda_{2080/81} + \lambda_{2081/82}$$
Including a standalone $\mathit{Post}_t$ regressor alongside full year fixed effects would create perfect exact collinearity (dummy variable trap). Consequently, the main effect of $\mathit{Post}_t$ is fully absorbed by the fiscal-year fixed effects and is not estimated separately.

#### Interpretation of Slope Parameters:
* **Pre-Consolidation Valuation Slopes:** Represented directly by the baseline coefficients:
  $$\text{Slope}_{\text{EPS, Pre}} = \beta_E, \quad \text{Slope}_{\text{BVPS, Pre}} = \beta_B$$
* **Incremental Regime Shifts:** Measured by the interaction coefficients:
  $$\Delta_{\text{EPS}} = \delta_E, \quad \Delta_{\text{BVPS}} = \delta_B$$
* **Post-Consolidation Valuation Slopes:** Calculated as linear combinations:
  $$\text{Slope}_{\text{EPS, Post}} = \beta_E + \delta_E, \quad \text{Slope}_{\text{BVPS, Post}} = \beta_B + \delta_B$$
* **Principal Hypothesis Test:** Evaluated via the joint null hypothesis of zero parameter shift:
  $$H_0: \delta_E = \delta_B = 0$$
  tested using a joint Wald $F$-test with 2 numerator degrees of freedom under the robust covariance matrix.

### 3.6.3 Econometric Estimation, Degrees of Freedom, and Robust Inference
Estimation is performed by Ordinary Least Squares (OLS) with explicit dummy variables for bank and fiscal-year fixed effects:
* **Degrees of Freedom Accounting:** On the realized clean sample of $N = 28$ observations, Model 2 estimates 14 parameters:
  * 1 constant intercept ($\alpha$)
  * 4 bank fixed effects ($\mu_i$)
  * 5 fiscal-year fixed effects ($\lambda_t$)
  * 2 baseline slopes ($\beta_E, \beta_B$)
  * 2 interaction slopes ($\delta_E, \delta_B$)
  $$\text{Residual Degrees of Freedom} = N - K = 28 - 14 = 14 \text{ df}$$
  In supplementary models incorporating DPS, residual degrees of freedom decrease from 14 to $28 - 15 = 13$ df.
* **MacKinnon-White HC3 Robust Standard Errors:** Standard cluster-robust covariance estimators (such as Huber-White cluster SEs) suffer from severe downward bias and over-reject null hypotheses when the number of clusters is small ($G = 5$) (Cameron et al., 2008). To ensure conservative, reliable inference, standard errors, $t$-statistics, and confidence intervals are computed using MacKinnon-White (1985) HC3 heteroskedasticity-robust standard errors:
  $$\text{HC3} = (X'X)^{-1} \left( \sum_{i=1}^n \frac{e_i^2}{(1 - h_{ii})^2} x_i x_i' \right) (X'X)^{-1}$$
  where $h_{ii} = x_i (X'X)^{-1} x_i'$ represents the leverage of observation $i$. HC3 heavily discounts high-leverage observations, providing reliable finite-sample inference in small panel samples.

### 3.6.4 Econometric Diagnostic Battery
To assess econometric validity, the estimation protocol executes four diagnostic checks:
1. **Multicollinearity:** Variance Inflation Factors (VIF) and tolerance statistics ($1/\text{VIF}$) computed on substantive regressors. Regressors exhibiting $\text{VIF} > 5$ or tolerance $< 0.20$ are screened for collinearity.
2. **Heteroskedasticity:** The Breusch-Pagan / Cook-Weisberg Lagrange Multiplier test evaluated against the null hypothesis of constant error variance ($H_0: \sigma_i^2 = \sigma^2$).
3. **Influential Outliers:** Cook's Distance ($D_i$) computed for each observation and evaluated against the conventional finite-sample threshold $D_i > 4/n = 4/28 \approx 0.143$.
4. **Residual Normality:** Normal Q-Q probability plots and residual standard deviation screening.

### 3.6.5 The Eight-Part Robustness Suite
To verify that empirical inferences are not artifacts of specific modeling choices, the study estimates a structured eight-part robustness suite (Specifications R1 to R8):
* **R1 (Model 1 Baseline):** Baseline two-way fixed-effects model without interaction terms ($n = 28$).
* **R2 (Model 2 Baseline):** Full two-way fixed-effects model with consolidation interaction terms ($n = 28$).
* **R3 (ROA Substitution):** Replaces EPS with return on assets (ROA) to evaluate sensitivity to an asset-scaled operational profitability metric ($n = 28$).
* **R4 (Dividend Specification):** Incorporates eligible cash dividend per share (DPS) declarations into Model 2, noting degrees of freedom decrease to 13 ($n = 28$).
* **R5 (Excluding Transition Year):** Re-estimates Model 2 excluding FY 2079/80 ($n = 23$) to verify results are not driven by immediate consolidation shock.
* **R6 (Excluding Entity-Timing Mismatch):** Re-estimates Model 2 excluding FY 2078/79 ($n = 23$) to eliminate the mismatch where standalone fundamentals were paired with post-merger April 2023 prices.
* **R7 (Bonus Share Capitalization Adjustment):** Re-estimates Model 2 using bonus-adjusted book value per share ($\mathit{BVPS}_{\text{adj}} = \mathit{BVPS} / (1 + \text{bonus ratio})$) to evaluate parameter stability against share dilutions ($n = 28$).
* **R8 (Retrospective Restated EPS):** Re-estimates Model 2 using retrospective audited basic EPS restatements from subsequent annual reports ($n = 28$).

### 3.6.6 Specification Comparison
To ensure transparency regarding how fixed effects absorb market-wide variation, baseline two-way fixed-effects estimates are compared directly against:
1. **Pooled OLS:** Neglects bank and year heterogeneity, reflecting conventional static literature.
2. **Bank Fixed-Effects Only:** Absorbs cross-bank heterogeneity but retains longitudinal macroeconomic price variation.

### 3.6.7 Computational Tools and Implementation
Data extraction, audit reconciliation, and panel assembly are executed in Python (`pandas`, `numpy`) and Microsoft Excel. Econometric modeling, robust HC3 covariance estimation, diagnostic testing, and visualization are executed using Python (`statsmodels`, `linearmodels`, `seaborn`, `matplotlib`), with cross-validation in Stata and SPSS.

