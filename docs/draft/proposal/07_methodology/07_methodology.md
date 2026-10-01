# Research Methodology

> Guideline position: **vii.** (p. 7), with the five mandated sub-parts:
> 1.1.1 Research design
> 1.1.2 Population and sampling procedure
> 1.1.3 Nature and sources of data collection
> 1.1.4 Research framework and definition of variables
> 1.1.5 Methods of analysis
>
> Keep the numbering explicit. Write in future or present tense, not past.

## 1.1.1 Research design

The study adopts a descriptive and causal-comparative research design.

The descriptive design is used to establish the characteristics of the sampled
banks and of the variables under examination, providing the descriptive
statistics reported for earnings per share, dividend per share, price-earnings
ratio, return on assets, book value per share and market price per share.

The causal-comparative design is used to examine the relationship between the
firm-specific independent variables and the dependent variable, market price
per share, in order to determine the influence each factor exerts on share
price.

<!--
TODO(You):
  - If the design moves to a fixed-effects panel (strongly recommended given
    multiple banks across multiple years, see below), this section must change.
    "Causal-comparative" is a weak fit for a model that controls for
    bank-specific and time-specific effects. Consider whether
    "explanatory" or "analytical" describes the design more accurately.
-->

## 1.1.2 Population and sampling procedure

The population of the study comprises all commercial banks operating in Nepal
that are listed on Nepal Stock Exchange Limited and for which continuous annual
data on the variables of interest are available.

A sample of five commercial banks is drawn using the purposive sampling
technique:

1. Global IME Bank Limited
2. Himalayan Bank Limited
3. Kumari Bank Limited
4. Nepal Investment Bank Limited
5. NMB Bank Limited

The procedure is purposive rather than random because the study requires
continuous annual data from bank annual reports over the full observation
period, and because the five banks are among the most actively traded on NEPSE,
which makes their share prices observable and comparable.

The observation period is fiscal year 2076/77 to fiscal year 2081/82, giving
five banks over six years and 30 bank-year observations.

<!--
CRITICAL TODO(You) - this must be resolved before anything else.

  The five banks above are the ones sampled in the earlier study. Since that
  study was completed, mergers and acquisitions have changed the legal identity
  of several of them. Verify the current status of each and record it here:

    - Global IME Bank Ltd      - merged with Bank of Kathmandu; now Global IME
                                 Bank Limited
    - Himalayan Bank Ltd      - merged with Civil Bank; now Himalayan Bank
                                 Limited
    - Kumari Bank Ltd         - merged with NCC Bank
    - Nepal Investment Bank   - status to confirm
    - NMB Bank Ltd            - status to confirm

  Three workable responses:
    (a) Use the merged successor entity, presenting pre-merger figures for the
        predecessor and post-merger figures for the successor as a continuous
        series. Defensible, but requires a note on the discontinuity.
    (b) Keep only banks with unbroken legal existence across the full window
        and substitute others to restore the sample size.
    (c) Restate the sample as the five largest listed banks by market
        capitalisation in the current period, and justify on those grounds.

  Whichever is chosen, state it explicitly and be ready to justify it. A sample
  naming entities that no longer exist is the kind of error that damages
  credibility with the research committee.

  Also confirm the observation period is genuinely available. Verify that FY
  2081/82 annual reports are published, and if the most recent year is not yet
  available, shift the window back rather than leaving a gap.
-->

## 1.1.3 Nature and sources of data collection

The study is based entirely on secondary data. The variables examined are
earnings per share, dividend per share, price-earnings ratio, book value per
share, return on assets and market price per share, for the sampled banks over
the stated observation period.

Sources are:

- Annual reports of the sampled commercial banks
- *Banking and Financial Statistics*, Nepal Rastra Bank
- *Economic Survey*, Ministry of Finance
- Nepal Stock Exchange trading and price reports

No primary data are collected and no questionnaire or interview instrument is
administered.

<!--
TODO(You):
  - NEPSE publishes fiscal-year-end closing prices. Specify exactly which price
    measure is used for MPS (year-end closing price is the conventional choice)
    and where it is sourced. The earlier study's table caption implies market
    price per share but the measurement row in its variable table gives
    "total share capital divided by number of common shares outstanding", which
    is a definition of something other than market price. This is an error in
    the earlier thesis and must not be reproduced.
  - Confirm whether NRB's Banking and Financial Statistics carries bank-level
    EPS, DPS, ROA and BVPS for the required years, or whether all of these must
    be computed from the annual reports.
-->

## 1.1.4 Research framework and definition of variables

The conceptual framework of the study posits market price per share as the
dependent variable, determined by five firm-specific independent variables:
earnings per share, dividend per share, price-earnings ratio, book value per
share and return on assets.

```
Independent variables                     Dependent variable

Earnings per share (EPS)   ─┐
Dividend per share (DPS)    │
Price-earnings ratio (P/E)  ├────────►  Market price per share (MPS)
Book value per share (BVPS) │
Return on assets (ROA)     ─┘
                              (Source: adapted from Pradhan and Dahal, 2014)
```

### Variable definitions and measurement

| Code | Variable | Measurement |
|---|---|---|
| MPS | Market price per share | Fiscal year-end closing price of the share on NEPSE, in rupees |
| EPS | Earnings per share | (Net income − preference dividend) / number of outstanding shares |
| DPS | Dividend per share | Total dividends paid / number of outstanding shares |
| P/E | Price-earnings ratio | Market price per share / earnings per share |
| ROA | Return on assets | Net income / total assets |
| BVPS | Book value per share | (Total equity − preference equity) / number of common shares outstanding |
| e | Error term | Residual in the estimated relationship |

<!--
TODO(You):
  - Replace the ASCII diagram with a proper TikZ or similar figure before
    submission. The guideline requires the conceptual framework to be presented
    as a figure with citation of source.
  - Decide the treatment of the price-earnings ratio and record the reasoning
    here, consistent with the note in section 04_hypotheses. The measurement row
    "MPS / EPS" makes the mechanical dependency explicit; the methodology must
    then state how the regression handles it.
-->

## 1.1.5 Methods of analysis

The collected data are analysed using descriptive, correlation and regression
methods, with statistical processing carried out in SPSS.

**Descriptive statistics.** Mean, standard deviation, minimum and maximum values
are computed for each variable to characterise the sampled banks and to provide
the basis for assessing the distribution of the data.

**Correlation analysis.** Pearson correlation coefficients are computed between
the dependent variable and each independent variable, and among the independent
variables, to establish the direction and magnitude of association and to
identify multicollinearity among the regressors.

**Regression analysis.** Ordinary least squares is used to estimate the
relationship between the dependent and independent variables. The model is:

```
MPS(i,t) = α + β1 EPS(i,t) + β2 DPS(i,t) + β3 P/E(i,t)
              + β4 BVPS(i,t) + β5 ROA(i,t) + e(i,t)
```

Individual effects are tested using the `t`-statistic and the overall model is
tested using the `F`-statistic, both at the 5 percent level of significance.
Coefficients, standard errors, standardised coefficients, `t` values, `p`
values, `R`, `R²`, adjusted `R²` and the standard error of the estimate are
reported.

Analysis proceeds in the following order:

1. Descriptive statistics for all variables
2. Pearson correlation matrix
3. Simple regression of MPS on each independent variable separately
4. Multiple regression estimating the full model
5. Testing of the stated hypotheses and interpretation of results

<!--
TODO(You) - four methodological problems inherited from the earlier study that
  should be addressed here rather than repeated.

  1. Sample size and panel structure. Thirty bank-year observations with five
     regressors is a small sample relative to the parameter count. A fixed-
     effects or random-effects panel model, which is what bank-year data across
     multiple banks actually is, both increases effective sample size and
     controls for unobserved bank-level and year-level heterogeneity. Present
     pooled OLS, fixed effects and random effects, and report a Hausman test.
     This is the single most significant methodological improvement available.

  2. ROA recorded to the wrong precision. The earlier thesis tabulates ROA as
     values of exactly 1.00, 2.00 or 0.30 percent, i.e. rounded to whole
     percentage points. Banking-sector ROA varies in the second decimal place;
     a variable with that level of rounding cannot support regression. Extract
     full-precision ROA from the annual reports.

  3. Serial and cross-sectional dependence ignored. With annual bank data,
     residuals are unlikely to be independent across years within a bank. Report
     standard errors robust to heteroskedasticity and serial correlation, or use
     clustered standard errors by bank.

  4. P/E as a regressor. As noted in section 04_hypotheses, including both EPS
     and P/E in the same specification places market price on both sides of the
     equation. State the resolution here.

  Also: report a VIF or condition index to evidence the multicollinearity claim,
  and use the White or Breusch-Pagan test for heteroskedasticity rather than
  assuming homoskedasticity.
-->

## Analysis plan

The results of the above analyses are presented in Chapter IV of the thesis in
the following order: descriptive statistics, correlation analysis, regression
output for the overall model, and hypothesis testing. Chapter V presents the
summary, conclusion, limitations and recommendations.

<!--
TODO(You):
  - Once the design decision (OLS versus panel) is made, update this section
    and the corresponding paragraphs in 03_objectives and 04_hypotheses so the
    three agree. Supervisors check this consistency first.
  - Add a data-availability note: how missing values will be handled, and what
    happens if a sampled bank reports a zero or negative EPS in any year. A zero
    EPS makes the P/E ratio undefined, and this occurred in the earlier sample
    (NMB Bank, FY 2068/69). Decide the rule now and state it.
-->