# Dissertation & Research-Paper Writing Guidelines — Calibrated for TU FOM MBS Dissertation

**Context:** *Value Relevance of Accounting Information Before and After the Banking Consolidation Wave: Evidence from Nepalese Commercial Banks*  
**Institutional Standard:** Tribhuvan University, Faculty of Management (FOM) *Master's Degree Dissertation Writing Guidelines (2019)*  
**Methodological Domain:** Empirical Capital Markets Research, Financial Accounting Valuation (Ohlson 1995 RIV), and Panel Econometrics  
**Referencing Standard:** APA 6th Edition  

---

## Overview & Scope

These guidelines establish the writing, econometric, and structural standards for finalizing both the **MBS Dissertation** (120 pages, 5 chapters) and the **Dissertation Proposal** (sections 1–7) at Tribhuvan University Faculty of Management. Every rule below is calibrated to address the specific empirical realities of the Nepalese banking sector, the 2023 consolidation wave, two-way fixed-effects panel modeling, and strict academic compliance.

---

## A. Core Idea & Information Hierarchy

**A1. Write the economic and valuation reality, not software execution.**  
The narrative must explain the financial institutions, accounting disclosures, valuation mechanics, and empirical associations under study. Avoid framing sentences around software execution or data-pipeline plumbing (e.g., avoid "Python scripts extracted," "pandas merged the CSVs"). Code repositories, data verification pipelines, and build systems belong in footnotes, code comments, or the technical appendix, not in the academic prose.

**A2. Anchor the entire dissertation around one clear central question.**  
Every chapter, section, table, and paragraph must serve the core inquiry:  
*Did the empirical valuation relevance of earnings per share (EPS) and book value per share (BVPS) for commercial bank equity prices shift between the pre-consolidation (FY 2076/77–2078/79) and post-consolidation (FY 2079/80–2081/82) periods in Nepal, when measured at an objective post-reporting-deadline pricing window ($MPS^{RD}$)?*  
Any content or diversion that does not directly advance or qualify this question belongs in background notes or should be excised.

**A3. Establish an explicit hierarchy of rhetorical weight.**  
Structure rhetorical emphasis across the dissertation as follows:
1. **Primary Contribution:** The empirical behavior of accounting multiples ($\beta_E, \beta_B$) and structural interaction parameters ($\delta_E, \delta_B$) across the consolidation wave.
2. **Theoretical Grounding:** The Ohlson (1995) residual income valuation framework and the post-merger transitoriness framework of Kwon and Wang (2020).
3. **Econometric Evidence:** Two-way fixed-effects estimates, MacKinnon-White HC3 robust standard errors, joint Wald test statistics ($F$ and $p$-values), and the 8-part robustness suite (R1–R8).
4. **Institutional Context:** Bank consolidation history, NRB regulatory capital escalation, and BAFIA 2017 statutory reporting timelines.
5. **Methodological Controls:** Unobserved bank-level fixed effects ($\mu_i$), macroeconomic fiscal-year fixed effects ($\lambda_t$), and sensitivity exclusions.
6. **Archival Details:** Aggregator price reconciliation, dividend declaration dates, and trading suspension calendars.

**A4. Don't let an absence or non-significance become a mystery unless justified.**  
When an interaction parameter (e.g., $\delta_E$ or $\delta_B$) or a robustness variable (e.g., ROA or DPS) is statistically insignificant under conservative HC3 standard errors, report it directly as empirical evidence of parameter stability or lack of explanatory contribution. Do not invent speculative ad-hoc narratives to explain away non-rejection of the null hypothesis.

---

## B. Opening the Dissertation & Chapter I Structure

**B1. Ground in institutional and theoretical reality, not generic textbook platitudes.**  
Do not begin Chapter I with elementary finance definitions (e.g., "A bank is a financial institution that accepts deposits..."). Begin directly with equity valuation theory (Ohlson 1995 clean surplus relation), the information role of audited accounting fundamentals in emerging capital markets, the specific structure of NEPSE, and the systemic consolidation of Nepalese commercial banks.

**B2. Begin with the economic and valuation problem, not the econometric machinery.**  
Establish the structural transformation of Nepal's banking sector (from institutional proliferation to 20 Class 'A' banks following the 2023 mergers) and the puzzle of conflicting empirical findings in prior Nepalese studies before introducing panel regression equations.

**B3. Follow the specific conceptual chain of this dissertation:**  
$$\text{Clean Surplus / Ohlson (1995) RIV} \longrightarrow \text{Corporate Consolidation Restructuring} \longrightarrow \text{Temporal Information Alignment } (MPS^{RD}) \longrightarrow \text{Regime Interaction Test } (\delta_E, \delta_B)$$  
1. **Valuation Theory:** Market equity is a function of net asset backing (BVPS) and normal/abnormal earnings capacity (EPS).  
2. **Consolidation Shock:** Mergers fundamentally alter balance-sheet scale, expand share capital, introduce integration frictions, and temporarily increase earnings transitoriness (Kwon & Wang, 2020).  
3. **Temporal Alignment:** Ashadh-end prices induce look-ahead bias; BAFIA 2017 Section 59(2) mandates a 9-month audited reporting deadline, operationalized at Chaitra-end ($MPS^{RD}$).  
4. **Empirical Evaluation:** A two-way fixed-effects interaction model formally tests whether market pricing parameters shifted across the pre- and post-consolidation regimes.

**B4. Motivate econometric design choices conceptually before mathematical formulation.**  
Explain *why* price-earnings (P/E) ratios must be excluded (avoiding mechanical simultaneity bias and endogeneity), *why* two-way fixed effects are required (absorbing unobserved bank heterogeneity and macro market trends), and *why* HC3 standard errors are essential (countering heteroskedasticity and severe small-cluster downward bias) before presenting the regression equations.

**B5. Maintain exact consistency in research questions, objectives, and hypotheses.**  
The 3 Research Questions, 3 Specific Objectives, and 4 Research Hypotheses ($H_1$ to $H_4$ plus joint Wald test) formulated in Chapter I (§1.2, §1.3, §1.4) must correspond one-to-one with:
- The methodology and model specifications in Chapter III (§3.6);
- The empirical findings and hypothesis tests in Chapter IV (§4.3, §4.4, §4.5);
- The summary answers, conclusions, and formal hypothesis decision matrix in Chapter V (§5.2, §5.3, §5.3.5).

**B6. Avoid repetitive meta-announcements.**  
Minimize boilerplate announcements such as "This section will now discuss..." or "As previously stated in Chapter I...". Move straight into substantive statements about empirical patterns, theoretical connections, and regulatory mechanisms.

**B7. Structure the Abstract as a complete, compressed executive summary.**  
Under TU FOM guidelines, the Abstract must be concise (fitting on a single page, accompanied by $\le 5$ keywords). It must follow a strict 4-stage narrative:
1. *Context & Problem:* Nepal's 2023 commercial bank consolidation wave and the empirical question of valuation parameter stability.
2. *Data & Methodology:* Purposive sample of 5 commercial bank series over FY 2076/77–2081/82 ($N = 28$), standardized $MPS^{RD}$ window, two-way fixed-effects panel regression with HC3 robust standard errors.
3. *Core Empirical Findings:* Baseline EPS and BVPS relevance (Model 1), post-consolidation slope shifts ($\delta_E, \delta_B$, Model 2), and joint Wald test result ($F = 2.76, p = 0.098$).
4. *Implications:* Valuation consequences of merger accounting transitoriness and regulatory relevance for NRB, SEBON, and capital market participants.

---

## C. Chapter-Level Architecture & Separation of Lanes (TU FOM Standards)

**C1. Strictly respect the specific lane of each of the 5 chapters:**
- **Chapter I (Introduction):** Establishes the background, problem statement, 3 research questions, general and specific objectives, 4 formal hypotheses, rationale/significance, study limitations (distinguishing deliberate scope from empirical constraints), and chapter organization.
- **Chapter II (Literature Review):** Establishes the theoretical framework (Ohlson RIV, signaling, agency, market efficiency), systematically reviews international and Nepalese empirical literature, presents the synthesis matrix (Table 2.1), and explicitly defines the 5 identified literature gaps. *No empirical findings from this dissertation belong here.*
- **Chapter III (Research Methodology):** Details the research design, population and purposive sample (5 bank series), secondary data sources and verification protocols, exact operational definitions of variables ($MPS^{RD}$, EPS, BVPS, ROA, DPS, $Post_t$), model specifications (Model 1 and Model 2), diagnostic tests, and the 8-part robustness protocol (R1–R8). *Contains only research protocols and specifications, zero empirical results.*
- **Chapter IV (Results and Discussion):** Reports descriptive statistics, correlation matrix and collinearity diagnostics, Model 1 (baseline) and Model 2 (interaction) regressions, joint Wald structural tests, comprehensive 8-part robustness suite, econometric diagnostics (VIF, Breusch-Pagan, Cook's distance, normality), and a structured scholarly discussion contextualizing findings against prior Nepalese and international studies.
- **Chapter V (Summary and Conclusion):** Synthesizes the overall study, answers each research question, presents the formal hypothesis testing decisions table (§5.3.5), outlines actionable implications for investors, bank executives, and regulators, and identifies avenues for future research.

**C2. Keep economic interpretation out of Chapter III.**  
Chapter III explains *how* variables are constructed and *how* equations are estimated. Save the analysis of *what* the estimates mean, why coefficients attenuated, and how they relate to market efficiency for Chapters IV and V.

**C3. Keep data cleaning and software plumbing out of the Chapter IV discussion.**  
Chapter IV discussion focuses on economic behavior, investor perception, accounting transitoriness, and comparison with prior studies (e.g., Bhattarai 2014; Pradhan & Dahal 2016; Kwon & Wang 2020; Gurung & Dahal 2025). Do not clutter the discussion with discussions of spreadsheet formatting or data manipulation scripts.

**C4. Ensure every subsection answers a substantive research objective.**  
Avoid filler subsections. Each empirical subsection in Chapter IV must directly correspond to an objective or diagnostic check defined in Chapters I and III.

---

## D. Econometric Design, Operationalization, and Controls

**D1. Explain exclusions and constraints by what they isolate, not merely what was dropped.**
- *5-Day Freshness Window:* Treating HBL FY 2077/78 (suspended until 6 June 2022; 54 days late) and NIMB FY 2077/78 (suspended until 30 May 2022; 47 days late) as missing isolates clean post-deadline market pricing from stale pre-suspension prices.
- *P/E Ratio Exclusion:* Strictly excluding P/E ratios isolates true fundamental accounting relevance from mechanical circularity ($\text{P/E} = \text{MPS} / \text{EPS}$).
- *Transition Year Exclusion (R5):* Dropping FY 2079/80 isolates enduring structural parameter shifts from temporary initial amalgamation integration shocks.
- *Entity-Timing Sensitivity (R6):* Dropping FY 2078/79 isolates valuation parameters from the timing mismatch where pre-merger standalone accounts coincided with post-merger April 2023 trading prices.

**D2. State methodological rationale as objective scientific fact, not author narrative.**  
Avoid writing author-centric decision histories ("We decided to exclude P/E because we felt...", "We initially considered pooled OLS but changed our mind...").  
Write: *"Price-earnings (P/E) ratios are strictly excluded from all specifications because $\text{P/E} = \text{MPS} / \text{EPS}$, embedding the dependent variable directly within the regressor and inducing mechanical endogeneity."*

**D3. Confine study limitations to dedicated sections; avoid defensive hedges throughout the results.**  
Acknowledge the study's boundaries (purposive sample of 5 banks, 6 fiscal years, $N = 28$ observations, calendar-time identification) comprehensively in Chapter I (§1.6) and Chapter V (§5.5). Do not weaken every empirical sentence in Chapter IV with apologetic clauses. State the econometric result clearly, followed by its calibrated statistical interpretation.

**D4. Treat fixed effects as structural controls and interpret identification cleanly.**  
- Bank fixed effects ($\mu_i$) absorb all time-invariant cross-sectional bank heterogeneity (e.g., historical reputation, branch distribution scale, founding ownership).
- Fiscal-year fixed effects ($\lambda_t$) absorb all common macroeconomic shocks, interest rate cycles, and NEPSE broad-market fluctuations.
- The standalone consolidation dummy ($Post_t$) is a deterministic linear combination of post-merger year dummies ($\sum_{t \in \text{Post}} \lambda_t$) and is perfectly collinear with them; explain clearly that $Post_t$ is absorbed by $\lambda_t$, leaving identification to within-year cross-sectional variation.

**D5. Use rigorous, self-contained mathematical notation for all econometric models.**  
Always specify full panel indices ($i = 1, \dots, 5$; $t = 1, \dots, 6$), parameter vectors, and error terms:
$$\text{Model 1 (Baseline):} \quad \mathit{MPS}^{RD}_{it} = \alpha + \mu_i + \lambda_t + \beta_E \mathit{EPS}_{it} + \beta_B \mathit{BVPS}_{it} + \varepsilon_{it}$$
$$\text{Model 2 (Interaction):} \quad \mathit{MPS}^{RD}_{it} = \alpha + \mu_i + \lambda_t + \beta_E \mathit{EPS}_{it} + \beta_B \mathit{BVPS}_{it} + \delta_E (\mathit{EPS}_{it} \times \mathit{Post}_t) + \delta_B (\mathit{BVPS}_{it} \times \mathit{Post}_t) + \varepsilon_{it}$$

**D6. Transparently disclose degrees of freedom and finite-sample constraints.**  
On the realized clean sample of $N = 28$ observations, Model 2 estimates 14 parameters (1 constant, 4 bank dummies, 5 year dummies, and 4 slope parameters), leaving exactly:
$$28 - 14 = 14 \text{ residual degrees of freedom}$$
Never hide or gloss over this parameter consumption. Explicitly document residual degrees of freedom in table notes and the methodology text.

**D7. Banish code variable names and software syntax from the narrative.**  
Never use raw code names (e.g., `mps_rd`, `eps_clean`, `post_dummy`, `df_regression`, `statsmodels`) in the formal dissertation narrative. Use formal mathematical symbols ($MPS^{RD}$, $\text{EPS}_{it}$, $\text{BVPS}_{it}$, $\mathit{Post}_t$, $\beta_E$, $\delta_E$) and standard academic phrasing.

---

## E. Econometric Rigor, Small-Cluster Inference, and Non-Causal Framing

**E1. Strictly maintain non-causal, associational language.**  
Because the research design is observational and non-experimental, and the consolidation divide is demarcated by calendar time (FY 2079/80), the interaction parameters ($\delta_E, \delta_B$) capture temporal changes in statistical association across regimes. These changes reflect corporate consolidation alongside concurrent macroeconomic conditions, interest rate trends, and post-COVID capital market cycles.  
- **Permissible phrasing:** *"is associated with"*, *"coincided with"*, *"was accompanied by"*, *"the estimated valuation slope attenuated"*, *"is consistent with post-merger earnings transitoriness"*.  
- **Prohibited phrasing:** *"mergers caused a decline"*, *"consolidation proved that"*, *"the impact of the merger was to reduce value relevance"*.

**E2. Never conflate descriptive bivariate relationships with multivariate panel estimates.**  
Always maintain a sharp distinction between bivariate correlations/fits and two-way fixed-effects estimates. For example, explain clearly that descriptive OLS scatter plots (e.g., Figure 4.1) illustrate raw within-period cross-sectional clustering, whereas Table 4.4 reports conditional slopes net of bank-specific and year-specific fixed effects.

**E3. Clearly delineate baseline models from the 8-part robustness suite (R1–R8).**  
Present Model 1 and Model 2 as the primary empirical baseline. Treat the remaining specifications as explicit sensitivity checks:
- *R1:* Pooled OLS benchmark (evaluates the cost of ignoring panel heterogeneity);
- *R2:* Bank Fixed-Effects only (evaluates sensitivity to dropping year fixed effects);
- *R3:* ROA substitution for EPS (evaluates asset-scaled operating profitability);
- *R4:* Eligible Cash DPS inclusion (evaluates dividend signaling);
- *R5:* Exclusion of transition year FY 2079/80 (verifies results are not driven by initial integration shock);
- *R6:* Exclusion of FY 2078/79 (evaluates entity-timing mismatch);
- *R7:* Bonus-adjusted metrics (evaluates capital dilution effects);
- *R8:* Retrospective restated EPS (evaluates sensitivity to subsequent-year accounting adjustments).

**E4. Implement finite-sample inferential caution for small clusters.**  
With $G = 5$ bank clusters, standard cluster-robust sandwich covariance estimators suffer from severe finite-sample downward bias and overstate test significance (Cameron, Gelbach, & Miller, 2008). Explicitly justify the implementation of MacKinnon-White (1985) HC3 heteroskedasticity-consistent standard errors, which apply a $(1 - h_{ii})^2$ leverage penalty to protect against over-rejection in small panels.

---

## F. Accounting Variables, Construct Validity, and Measurement Rules

**F1. Separate balance-sheet stock net worth from income-statement operating flow.**  
Maintain theoretical clarity between BVPS (accumulated net assets, equity capital, retained earnings) and EPS/ROA (current period operational efficiency and cash-flow generation). In banking institutions, book equity represents regulatory capital solvency, whereas earnings reflect loan yield margins and credit loss provisions.

**F2. Enforce unambiguous, documented operational variable definitions:**
- **$MPS^{RD}$ (Dependent Variable):** Secondary market closing price per ordinary share (NPR) observed on the first NEPSE floor trading session following the statutory 9-month audited reporting publication deadline under BAFIA 2017 Section 59(2) at Chaitra-end (mid-April) of the subsequent fiscal year.
- **Basic EPS (Independent Variable):** Audited basic earnings per share (NPR) extracted from the bank's own audited Statement of Profit or Loss for that fiscal year (own-current reported rule), based on weighted-average shares outstanding.
- **BVPS (Independent Variable):** Ordinary shareholders' equity attributable to equity holders of the bank divided by year-end ordinary shares outstanding (NPR), recomputed from balance-sheet components and reconciled against printed Net Asset Value (NAV).
- **Consolidation Indicator ($\mathit{Post}_t$):** Binary indicator equal to $1$ for post-consolidation years (FY 2079/80, 2080/81, 2081/82) and $0$ for pre-consolidation years (FY 2076/77, 2077/78, 2078/79).
- **ROA (Robustness Variable):** Net profit after tax divided by average total assets (expressed as a percentage).
- **DPS (Robustness Variable):** Cash dividend per ordinary share (NPR) officially declared by the Board of Directors on or before the $MPS^{RD}$ observation date.

**F3. Disclose collinearity constraints between EPS and ROA.**  
The bivariate Pearson correlation between EPS and ROA is $r = 0.975$ on the clean sample, producing variance inflation factors ($VIF$) exceeding 20–30 when entered simultaneously. Explicitly explain why ROA must be evaluated as an alternative substitute (R3) rather than an additive regressor.

**F4. Defend the construct validity of the statutory $MPS^{RD}$ pricing window.**  
Detail why $MPS^{RD}$ is superior to alternative conventions:
1. *Vs. Ashadh-end (mid-July):* Eliminates severe look-ahead bias, as audited financial statements are legally and practically unavailable at fiscal-year-end.
2. *Vs. Ad-hoc announcement timestamps:* Avoids measurement noise, archival opacity, and unverified press-release timestamps across historical periods, providing an objective, legally mandated reporting threshold.
3. *Institutional Reality:* Commercial bank boards typically publish audited highlights between Ashwin and Poush, well before the statutory Chaitra ceiling, ensuring that audited numbers are fully in the public domain prior to price observation.

---

## G. Reporting Empirical Results (Tables, Figures, and Regressions)

**G1. Write results around economic patterns and hypothesis tests, not cell recitation.**  
Do not write narrative that merely lists table entries (e.g., avoid "In Table 4.1, GBIME has a mean of 294.07, HBL has 274.81..."). Direct the reader to meaningful economic insights: cross-sectional dispersion, compression of valuation multiples post-merger, and contrast between within-bank and cross-bank variance.

**G2. Emphasize informative empirical contrasts.**  
Highlight key econometric revelations:
- The pre-consolidation dominance of EPS ($\beta_E = 12.21, p = 0.040$ in Model 2) versus its post-consolidation attenuation ($\delta_E = -14.62, p = 0.089$);
- The stability of BVPS across regimes ($\delta_B = 0.087, p = 0.963$);
- The joint Wald test result confirming overall structural parameter shift ($F = 2.76, p = 0.098$, significant at 10%);
- The stark contrast between pooled OLS ($R^2 = 0.730$, inflated by cross-sectional scale) and two-way fixed effects (which purges unobserved bank heterogeneity).

**G3. State empirical results plainly with calibrated statistical verbs.**  
Use precise scientific language calibrated to the evidence:
- *"The baseline coefficient for EPS is positive and statistically significant at the 5% level ($\beta_E = 6.43, t = 2.47, p = 0.025$)."*
- *"The joint Wald test rejects parameter constancy across the consolidation divide at the 10% significance level ($F(2, 14) = 2.76, p = 0.098$), indicating an observed shift in the overall valuation relationship."*
- Follow clean empirical statements with distinct, dedicated sentences outlining qualifications or institutional factors.

**G4. Distinguish empirical findings from post-hoc speculation.**  
Clearly separate the measured coefficient estimates from speculative economic hypotheses regarding investor psychology, regulatory forbearance, or non-performing loan adjustments. Ground all explanatory discussions in cited literature (e.g., Kwon & Wang 2020; Collins et al. 1997; Adhikari et al. 2023).

**G5. Report missing data, sample attrition, and corporate actions honestly.**  
State unequivocally that while audited annual financial statements are available for all 30 target bank-years, trading suspensions during corporate combinations rendered two pre-consolidation prices unverifiable within the 5-day freshness rule:
- HBL FY 2077/78: Trading suspended until 6 June 2022 (54-day gap);
- NIMB FY 2077/78: Trading suspended until 30 May 2022 (47-day gap).  
Document that coding these as missing leaves a clean estimation sample of $N = 28$ observations (13 pre-consolidation, 15 post-consolidation). Furthermore, disclose NMB's acquisition of Kanchan Development Bank in August 2020 (adding approximately NPR 0.56 billion to share capital beyond its 13% bonus share distribution).

**G6. Treat non-rejection of individual interaction terms with scientific objectivity.**  
Under conservative HC3 standard errors, individual interaction parameters ($\delta_E, \delta_B$) yield $p$-values of 0.089 and 0.963 respectively. Report these statistics objectively. Emphasize that while individual parameter shifts are exploratory under small-sample degrees of freedom, the joint Wald test evaluates simultaneous parameter movement.

**G7. Make every table and figure completely self-contained.**  
Per TU FOM standards, tables and figures must be interpretable without reference to the body text:
- Table titles must appear **above** the table (bold, uniform 12pt);
- Complete table notes must appear **below** the table in single spacing (defining all abbreviations, sample sizes, observation dates, source aggregators, standard error types, and significance asterisks: $^{***}p < 0.01, ^{**}p < 0.05, ^{*}p < 0.10$);
- Figure captions must appear **below** the figure, citing primary theoretical or empirical sources.

---

## H. Summary, Hypotheses Decisions, and Implications (Chapter V)

**H1. Directly answer the 3 central research questions in Chapter V.**  
Chapter V (§5.2 and §5.3) must provide explicit, evidence-grounded answers to each Research Question posed in Chapter I:
1. *RQ1 (Baseline Relevance):* Did EPS and BVPS exhibit significant association with $MPS^{RD}$? (Answer: Yes, Model 1 confirms EPS is significant at 5%, while BVPS is positive but secondary after controlling for two-way fixed effects).
2. *RQ2 (Consolidation Regime Shift):* Did valuation slopes differ across the consolidation wave? (Answer: Yes, joint Wald test indicates structural shift at 10%, characterized by significant pre-merger EPS pricing and subsequent post-merger attenuation).
3. *RQ3 (Robustness & Stability):* Did findings survive the 8-part robustness suite? (Answer: Yes, core patterns remained consistent across ROA substitution, DPS inclusion, transition year exclusion, bonus share adjustments, and restated EPS).

**H2. Include a formal, unambiguous Hypothesis Decision Table.**  
Section 5.3.5 must include the structured Hypothesis Testing Decision Table:

| Hypothesis | Parameter Statement | Empirical Estimate | Test Statistic / $p$-value | Decision at $\alpha = 0.05$ |
| :--- | :--- | :--- | :--- | :--- |
| **$H_1$ (Baseline EPS)** | $\beta_E \ne 0$ | $\hat{\beta}_E = 6.430$ | $t = 2.47, p = 0.025$ | **Supported (Reject $H_{0,1}$)** |
| **$H_2$ (Baseline BVPS)** | $\beta_B \ne 0$ | $\hat{\beta}_B = 0.781$ | $t = 0.92, p = 0.370$ | **Not Supported (Fail to Reject $H_{0,2}$)** |
| **$H_3$ (EPS Regime Shift)** | $\delta_E \ne 0$ | $\hat{\delta}_E = -14.619$ | $t = -1.82, p = 0.089$ | **Not Supported at 5% (Supported at 10%)** |
| **$H_4$ (BVPS Regime Shift)** | $\delta_B \ne 0$ | $\hat{\delta}_B = 0.087$ | $t = 0.05, p = 0.963$ | **Not Supported (Fail to Reject $H_{0,4}$)** |
| **Joint Shift Test** | $\delta_E = 0 \text{ and } \delta_B = 0$ | Joint vector | $F(2, 14) = 2.76, p = 0.098$ | **Supported at 10% Level** |

**H3. Partition actionable implications across the three mandatory stakeholder groups.**  
Structure practical implications in Section 5.4 into three dedicated subsections:
1. *Implications for Investors & Capital Market Participants:* Understanding post-merger earnings transitoriness, avoiding naive P/E multiples, and prioritizing audited balance-sheet capital strength during restructuring.
2. *Implications for Bank Executives & Boards of Directors:* Managing post-merger integration costs, maintaining transparent asset-quality disclosures, and stabilizing dividend expectations following share capital expansion.
3. *Implications for Regulatory & Statutory Authorities (NRB, SEBON, NEPSE):* Enforcing centralized corporate disclosure archives, minimizing prolonged merger-related trading suspensions that trap shareholder liquidity, and monitoring capital adequacy reporting integrity.

**H4. Formulate specific, actionable recommendations for future research.**  
Section 5.6 must guide future scholars: expanding the cross-sectional sample to include newly merged development banks and finance companies, extending the longitudinal time series as more post-consolidation years mature, evaluating IFRS 9 / NFRS expected credit loss provisions, and analyzing corporate governance mechanisms.

---

## I. Literature Review, Theoretical Anchors, and Synthesis Matrix (Chapter II)

**I1. Build the literature review as a coherent intellectual progression.**  
Organize Chapter II logically:
$$\text{Theoretical Foundations} \longrightarrow \text{International Empirical Precedents} \longrightarrow \text{Nepalese Empirical Literature} \longrightarrow \text{Consolidation Context} \longrightarrow \text{Research Gaps}$$

**I2. Synthesize prior literature around thematic and methodological debates.**  
Avoid simple serial listing ("Author A found X. Author B found Y. Author C found Z."). Group studies around core methodological tensions:
- *Income Statement vs. Balance Sheet:* Studies identifying EPS as dominant (Bhandari 2026; Niroula 2021) versus those finding BVPS dominant (Chhetri 2023; Silwal 2019).
- *Endogenous Regressors:* The widespread, circular inclusion of P/E ratios in models predicting share prices (Bhattarai 2014; Joshi 2023; Pant 2024; Gurung & Dahal 2025).
- *Temporal Misalignment:* Reliance on Ashadh-end prices that ignore the multi-month audited reporting lag (Pradhan & Dahal 2016; Silwal 2019).
- *Panel Heterogeneity:* Pooled OLS models versus fixed-effects specifications controlling for bank-specific unobservables (Gurung & Dahal 2025).

**I3. Present a comprehensive, standardized Literature Synthesis Matrix (Table 2.1).**  
Summarize all key studies with standardized columns: *Study & Year*, *Sample & Period*, *Econometric Methodology*, *Key Variables Evaluated*, and *Core Empirical Findings*.

**I4. Explicitly define the 5 research gaps addressed by the study:**
1. *Consolidation Regime Shift Gap:* Absence of explicit interaction tests of valuation parameter stability across the 2023 merger wave.
2. *Econometric Endogeneity Gap:* Pervasive inclusion of price-derived P/E multiples in share price regressions.
3. *Temporal Alignment & Look-Ahead Bias Gap:* Reliance on Ashadh-end pricing dates preceding financial report publication.
4. *Entity-Timing Transition Gap:* Failure to account for the FY 2078/79 transition mismatch where standalone fundamentals met consolidated trading prices.
5. *Small-Cluster & Degrees of Freedom Gap:* Neglect of finite-sample degree-of-freedom constraints and small-cluster downward standard error bias.

---

## J. Academic Prose, Anti-AI Filter, and Sentence-Level Craft

**J1. Use APA 6th Edition citation commands consistently.**  
- Use `\citet{}` for narrative citations: *"As demonstrated by \citet{ohlson1995}..."*  
- Use `\citep{}` for parenthetical citations: *"...as documented in emerging markets \citep{sharma2011,almumani2014}."*  
- Never write hardcoded author names with manual citation brackets.

**J2. Strictly eradicate generative AI clichés and filler vocabulary.**  
Kobak et al. (2024) documented an unnatural surge in specific academic boilerplate words. Systematically eliminate these words and replace them with direct, precise economic language:
- **Delete / Replace:** *"delve"*, *"delving"*, *"underscores"*, *"showcasing"*, *"testament"*, *"pivotal"*, *"beacon"*, *"tapestry"*, *"paramount"*, *"crucial role"*, *"game changer"*, *"in summary, it is clear that"*.  
- **Use instead:** *"indicates"*, *"demonstrates"*, *"reveals"*, *"is consistent with"*, *"attenuates"*, *"reflects"*, *"specifies"*.

**J3. Optimize for conceptual precision and scholarly economy.**  
Prefer one mathematically and institutionally precise sentence over multiple redundant explanatory sentences. Write directly about economic entities, accounting numbers, and statistical parameters.

**J4. Anchor topic sentences at the beginning and key findings at the end.**  
Follow Gopen & Swan's (1990) information architecture:
- Place familiar contextual anchors in the **topic position** (start of the sentence);
- Deliver the new empirical finding, parameter estimate, or institutional outcome in the **stress position** (end of the sentence).

**J5. Use formal academic third-person or scholarly plural voice.**  
Maintain objective academic phrasing: *"This dissertation examines..."*, *"The empirical results indicate..."*, *"We estimate two-way fixed-effects models..."*. Avoid informal first-person singular ("I think," "I noticed").

---

## K. Institutional Formatting & Compliance Checklist (TU FOM 2019)

**K1. Page Layout & Margin Standards:**
- Left margin: **3.18 cm (1.25 inches)** for binding.
- Top, Bottom, and Right margins: **2.54 cm (1.0 inch)**.
- Paper size: Standard A4.

**K2. Typography & Line Spacing Standards:**
- Font typeface: **Times New Roman** uniformly throughout.
- Main text font size: **12 point**.
- Text line spacing: **1.5 lines** (true 1.5 pitch, 20.66 pt).
- Single spacing: Strictly enforced for Table of Contents, Lists of Tables/Figures, table interiors, block quotations, footnotes, and References.
- Paragraph spacing: Flush left, 0 pt first-line indent, followed by a 10 pt gap (`\parskip`).

**K3. Pagination Protocol:**
- **Front Matter:** Numbered in lowercase Roman numerals (**ii, iii, iv...**), placed at the **bottom center** of the page. Title page is counted as page `i` but carries no printed number.
- **Main Body (Chapters I–V, References, Appendices):** Numbered in Arabic numerals (**1, 2, 3...**), placed at the **top right corner** of the page, beginning with page 1 on the first page of Chapter I.

**K4. Front Matter Structural Order:**
1. Title Page (counted, unnumbered);
2. Certification of Authorship (single page);
3. Report of Viva-Voce Committee (single page);
4. Declaration of Authenticity (single page);
5. Acknowledgements (single page);
6. Table of Contents (single-spaced);
7. List of Tables (single-spaced);
8. List of Figures (single-spaced);
9. Abbreviations / Acronyms (single-spaced);
10. Abstract (single page, concise narrative, $\le 5$ keywords).

---

## L. Pre-Submission Verification & Quality Self-Checks

Before submitting the dissertation or proposal for supervisory review or external defense, execute this 10-point checklist:

- [ ] **1. Exact Number Synchronization:** Do all empirical values match across text, tables, and scripts? ($N = 28$, pre-merger $n = 13$, post-merger $n = 15$, Model 2 residual $df = 14$, correlation $r = 0.975$, NMB Kanchan acquisition NPR 0.56 billion beyond 13% bonus share distribution).
- [ ] **2. Non-Causal Framing Integrity:** Are all empirical relationships framed associationally (*"is associated with"*, *"coincided with"*) rather than causally (*"mergers caused"*)?
- [ ] **3. Hypothesis Consistency:** Are $H_1, H_2, H_3, H_4$ and the joint Wald test formulated identically across Chapters I, III, IV, and V?
- [ ] **4. Title Page Compliance:** Are college affiliation, examination roll number, T.U. registration number, and submission date verified and accurate?
- [ ] **5. Front-Matter Pagination:** Are preliminary pages in Roman numerals bottom-center, and does Arabic page 1 begin cleanly on Chapter I?
- [ ] **6. Single-Page Front Matter:** Do Acknowledgements, Abstract, Certification, and Viva-Voce pages each fit strictly on a single page without orphan spills?
- [ ] **7. Self-Contained Tables & Figures:** Does every table have its title above, every figure its title below, and do all table notes define abbreviations, sample sizes, and significance asterisks?
- [ ] **8. Clean LaTeX Compilation:** Does the document compile via `xelatex` with **0 errors**?
- [ ] **9. Complete Bibliography Reconciliation:** Does every reference cited in the text appear in `references.bib`, and are all entries fully populated with volume, issue, pages, and DOI?
- [ ] **10. Eradication of AI Tells:** Has the entire manuscript been screened to ensure zero occurrences of AI clichés (*delve, underscores, showcasing, pivotal, testament*)?

---

## Key Methodological References

- **Ohlson, J. A. (1995).** Earnings, book values, and dividends in equity valuation. *Contemporary Accounting Research*, 11(2), 661–687.
- **Collins, D. W., Maydew, E. L., & Weiss, I. S. (1997).** Changes in the value-relevance of earnings and book values over the past forty years. *Journal of Accounting and Economics*, 24(1), 39–67.
- **Kwon, S. Y., & Wang, C. (2020).** The effect of mergers and acquisitions on the value relevance of accounting information. *Journal of Business Finance & Accounting*, 47(7–8), 984–1018.
- **Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008).** Bootstrap-based improvements for inference with clustered errors. *Review of Economics and Statistics*, 90(3), 414–427.
- **MacKinnon, J. G., & White, H. (1985).** Some heteroskedasticity-consistent covariance matrix estimators with improved finite sample properties. *Journal of Econometrics*, 29(3), 305–325.
- **Tribhuvan University Faculty of Management (2019).** *Master's Degree Dissertation Writing Guidelines 2019*. Office of the Dean, Kirtipur, Kathmandu.
- **Gopen, G. D., & Swan, J. A. (1990).** The science of scientific writing. *American Scientist*, 78(6), 550–558.
- **Kobak, D., González-Márquez, R., & Lause, J. (2024).** Delving into ChatGPT usage in academic writing through excess vocabulary. *arXiv preprint arXiv:2406.07016*.
