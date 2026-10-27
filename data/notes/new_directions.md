After checking the published literature, the reporting rules, your existing research report, and the statistical constraints, this is the model I recommend taking forward for your thesis. I would not finalize the earlier DPS-incremental model as the primary contribution.

The key change is to study whether the relationship between accounting fundamentals and market valuation changed across Nepal's 2023 banking-consolidation period, using a consistent price-measurement rule rather than trying to reconstruct 30 individual disclosure-event dates.

## 1. Why this is a stronger research direction

Three findings shape this decision.

First, the ordinary stock-price-determinants model is already well covered in Nepal. Gurung and Dahal's 2025 study examines ten commercial banks across approximately a decade, including EPS, BVPS, ROA, dividend payout, and other variables. Giri (2024) studies a similar relationship using DPS, EPS, P/E, and net worth per share. A conventional regression using those same variables would have limited differentiation.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

Pravaha+1



Second, a stronger theoretical question exists: does the market's relative valuation of accounting earnings and book value change after mergers? Kwon and Wang (2020) explicitly investigate changes in accounting value relevance after mergers and acquisitions. This establishes a theoretical precedent for studying changes in valuation relationships, without claiming that the same model or findings automatically apply to Nepal.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://onlinelibrary.wiley.com\&sz=32)

Wiley Online Library



Third, the standard accounting valuation framework developed by Ohlson (1995) provides a theoretical foundation for examining share prices in relation to earnings and book value.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://onlinelibrary.wiley.com\&sz=32)

Wiley Online Library



The potential contribution, therefore, is not merely using newer data or adding another financial ratio. It is examining whether the association between accounting fundamentals and equity prices differs across the consolidation period, with a price-measurement rule designed for the Nepalese reporting environment.

## 2. The final recommended research design

PROPOSED THESIS TITLE

# VALUE RELEVANCE OF ACCOUNTING INFORMATION BEFORE AND AFTER THE BANKING CONSOLIDATION WAVE: EVIDENCE FROM NEPALESE COMMERCIAL BANKS

Research design at a glance

## 5

Banks

## 6

Fiscal years

## 30

Intended bank-year observations

Sample: GBIME, HBL, KBL, NIMB, and NMB; FY 2076/77–2081/82. The existing data report identifies these five banks and six fiscal years.&#x20;

MPS_post Research.html



### 3. The dependent variable: a fixed reporting-window price

I would replace the exact-event variable `MPS_post` with a precisely defined measurement variable, provisionally called \\(MPS^{RD}\\), meaning market price per share at the reporting-deadline window.

Nepal's Banks and Financial Institutions Act, Section 59(2), specifies a statutory publication deadline for audited annual financial statements within the first nine months of the following fiscal year. This gives us a locally grounded date for constructing a fixed observation window.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://repository.lawcommission.gov.np\&sz=32)

नेपाल कानून आयोग+1



The proposed operational rule is:

- Identify the end of Chaitra in the fiscal year following the accounting year, corresponding to the statutory nine-month reporting deadline.
- Obtain the actual NEPSE closing price on the first trading session after that deadline on which the bank's security records a valid trade.
- If trading is suspended or no valid price can be established within a predefined short window, treat the observation as missing rather than carrying forward a stale closing price.
- Check for known late disclosures. A legal deadline does not prove that every bank complied with it.

This avoids the need to locate the exact day each annual report was first uploaded. But there is an important distinction: this is a fixed post-reporting-deadline price, not a verified first-trading-day-after-disclosure price. The thesis should not claim to measure an immediate disclosure reaction.

The new dependent variable is defensible only if the required historical closing prices can be retrieved and validated. The fixed-date price series must pass a feasibility check before we lock the design.

## 4. The final mathematical model

The main model should focus on two theoretically important variables: earnings per share and book value per share.

### Model 1 — Baseline value relevance

\\[ \begin{aligned} MPS^{RD}\_{it}={}&\alpha+\mu_i+\lambda_t\\\ &+\beta_E EPS\_{it} +\beta_B BVPS\_{it} +\varepsilon\_{it} \end{aligned} \\]

This estimates the association of EPS and BVPS with the fixed-window market price, controlling for persistent bank differences and common fiscal-year effects.

### Model 2 — Change in value relevance across the consolidation period

\\[ \begin{aligned} MPS^{RD}\_{it}={}&\alpha+\mu_i+\lambda_t\\\ &+\beta_E EPS\_{it}+\beta_B BVPS\_{it}\\\ &+\delta_E(EPS\_{it}\times Post_t)\\\ &+\delta_B(BVPS\_{it}\times Post_t)\\\ &+\varepsilon\_{it} \end{aligned} \\]

Here:

- \\(i\\) indexes the five banks.
- \\(t\\) indexes the six fiscal years.
- \\(MPS^{RD}\_{it}\\) is the verified closing price at the predetermined reporting-deadline window.
- \\(EPS\_{it}\\) is earnings per share in fiscal year \\(t\\).
- \\(BVPS\_{it}\\) is book value per share in fiscal year \\(t\\).
- \\(\mu_i\\) represents bank fixed effects.
- \\(\lambda_t\\) represents fiscal-year fixed effects.
- \\(Post_t=1\\) for FY 2079/80–2081/82 and \\(0\\) for FY 2076/77–2078/79.
- \\(\delta_E\\) and \\(\delta_B\\) measure changes in the estimated EPS and BVPS slopes across the two periods.

Because the model includes fiscal-year fixed effects, the standalone \\(Post_t\\) indicator is absorbed by those effects and is not estimated separately.

The main test is whether the accounting-value relationships change across the periods. The pre-period EPS slope is \\(\beta_E\\), while the post-period slope is \\(\beta_E+\delta_E\\). The corresponding BVPS slopes are \\(\beta_B\\) and \\(\beta_B+\delta_B\\).

The joint null hypothesis is:

\\[ H_0:\delta_E=\delta_B=0 \\]

Rejecting this null would provide evidence that the estimated relationships between the two accounting variables and market prices differ across the defined periods. It would not prove that the mergers themselves caused the change.

## 5. Hypotheses and supporting analyses

I would formulate the hypotheses as follows.

| Hypothesis | Expected or tested relationship                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------- |
| H1         | EPS is positively associated with the market price in the baseline value-relevance model.               |
| H2         | BVPS is positively associated with the market price in the baseline model.                              |
| H3         | The EPS–price association differs between the pre- and post-consolidation periods: \\(\delta_E\ne0\\).  |
| H4         | The BVPS–price association differs between the pre- and post-consolidation periods: \\(\delta_B\ne0\\). |

H3 and H4 should be tested two-sided. Although international merger research provides a rationale for examining a possible shift from earnings relevance toward book-value relevance, that direction should not be assumed to hold in Nepal before examining the evidence.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://onlinelibrary.wiley.com\&sz=32)

Wiley Online Library



For robustness, I recommend three checks:

1. ROA specification: Replace EPS with ROA rather than automatically including both. Recalculate correlation and VIF on the final sample before deciding whether both can be included together.
2. Dividend specification: Examine DPS separately, using only observations where the relevant dividend information was available by the price-measurement date. The DPS extension should be secondary, not the main novelty.
3. Transition-year sensitivity: Re-estimate the model excluding FY 2079/80, the first fiscal year ending after the major consolidation. This checks whether the transition year dominates the results.

I would exclude P/E ratio from the primary model because it is calculated from MPS and EPS, creating a mechanical relationship with the dependent variable.

## 6. Estimation and data-quality requirements

With 30 observations, bank fixed effects, fiscal-year fixed effects, and the four slopes in Model 2, the regression is mathematically estimable, but the residual degrees of freedom are only about 16. That is a small sample for interaction analysis.

The final methodology should therefore:

- Report coefficient estimates, confidence intervals, and uncertainty, not just p-values and \\(R^2\\).
- Use a parsimonious fixed-effects specification and clearly state that the evidence is exploratory.
- Avoid causal claims about mergers.
- Harmonize EPS, BVPS, and market prices for bonus shares, rights issues, merger share exchanges, and changes in share units.
- Never silently replace missing or suspended-day prices with an older close.

Conventional cluster-robust inference is especially unreliable with only five bank clusters; econometric research documents serious small-cluster problems. If the five-bank sample cannot be expanded, uncertainty estimates must be interpreted cautiously.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.nber.org\&sz=32)

NBER+1



## 7. Ready-to-use version for the thesis proposal

The following is the proposed final wording for your research design, subject to validating the fixed-window price series.

# VALUE RELEVANCE OF ACCOUNTING INFORMATION BEFORE AND AFTER THE BANKING CONSOLIDATION WAVE: EVIDENCE FROM NEPALESE COMMERCIAL BANKS

## Research Problem

Existing studies of Nepalese commercial banks have examined associations between market prices and accounting indicators such as earnings per share, book value per share, dividend measures, and profitability. However, conventional pooled models primarily estimate average relationships across the observation period. The 2023 banking consolidation provides a setting in which to examine whether the association between accounting fundamentals and market valuation differed across the pre- and post-consolidation periods.

This study adopts an accounting value-relevance framework and investigates whether earnings per share and book value per share are associated with subsequent market prices, and whether their estimated relationships differ across the consolidation period. The study does not attempt to estimate the immediate causal market reaction to individual financial-report announcements.

## General Objective

To examine the value relevance of accounting fundamentals and assess whether their associations with market prices differ across Nepal's 2023 banking-consolidation period.

## Specific Objectives

1. To estimate the association of earnings per share and book value per share with market prices measured at a standardized post-reporting-deadline window.
2. To test whether the estimated EPS–price and BVPS–price relationships differ between the pre- and post-consolidation periods.
3. To evaluate the robustness of the results using alternative profitability specifications and eligible dividend information.

## Research Questions

1. Are EPS and BVPS associated with the observed market prices of the selected Nepalese commercial banks?
2. Did the estimated associations between EPS, BVPS, and market prices differ across the pre- and post-consolidation periods?
3. Are the principal findings robust to alternative accounting-variable specifications and treatment of the transition year?

## Model Specification

The baseline model is:

[\
MPS^{RD}*{it}=\alpha+\mu_i+\lambda_t+*\
*\beta_E EPS*{it}+\beta_B BVPS\_{it}+\varepsilon\_{it}.\
]

The consolidation-period interaction model is:

[\
\begin{aligned}\
MPS^{RD}*{it}={}&\alpha+\mu_i+\lambda_t+*\
*\beta_E EPS*{it}+\beta_B BVPS\_{it}\\\
&+\delta_E(EPS\_{it}\times Post_t)\
+\delta_B(BVPS\_{it}\times Post_t)\
+\varepsilon\_{it}.\
\end{aligned}\
]

Here, (MPS^{RD}*{it}) denotes the market price per share measured at the predetermined reporting-deadline observation window. (EPS*{it}) and (BVPS\_{it}) denote earnings per share and book value per share for bank (i) in fiscal year (t). The bank and fiscal-year effects are represented by (\mu_i) and (\lambda_t), respectively. The variable (Post_t) equals one for FY 2079/80–2081/82 and zero for FY 2076/77–2081/82's preceding three fiscal years (FY 2076/77–2078/79).

The principal test evaluates the joint null hypothesis (H_0:\delta_E=\delta_B=0), which tests whether the estimated accounting-price associations differ across the two periods. These coefficients are interpreted as differences in association, not as causal effects of mergers.

## Measurement and Estimation

The sample comprises five selected commercial banks over FY 2076/77–2081/82, with a maximum of 30 bank-year observations. Market prices are obtained from verified historical trading records using a fixed observation rule defined relative to the statutory audited-reporting deadline. Observations with unavailable, suspended, or unverifiable prices are documented rather than imputed from unrelated dates.

The baseline analysis uses a parsimonious fixed-effects regression. Descriptive statistics, correlation analysis, and multicollinearity diagnostics are conducted before estimation. A supplementary model replaces EPS with ROA to assess robustness, while DPS is examined only when its public availability is consistent with the selected price date. The transition year is excluded in a sensitivity analysis.

Given the small number of banks and observations, the analysis emphasizes coefficient estimates, uncertainty, and sensitivity rather than strong causal claims or broad population generalization.

## 8. The decision to lock

My recommendation is to adopt the title, research objectives, and two-model framework above. It creates a clearer research question than a routine EPS–BVPS–DPS regression and has a theoretical foundation in accounting value relevance and changes in valuation following mergers.

There is one non-negotiable step before treating the model as final: validate that the fixed reporting-deadline price series can actually be recovered consistently for the sampled bank-years. If it cannot, do not relabel Ashadh-end prices as post-disclosure prices. We must instead use a lagged-fundamentals design with a correspondingly revised title and research question.

That is the defensible route to a thesis you can explain and defend in front of an examiner.