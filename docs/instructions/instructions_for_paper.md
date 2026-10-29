# Advanced Research Writing & Econometric Audit Guidelines
## An Independent, Strict Quality Standard for Empirical Accounting & Financial Economics

**Field:** Capital Markets Research in Accounting, Corporate Finance, Panel Econometrics  
**Target:** Master's Dissertations, Ph.D. Chapters, and Peer-Reviewed Empirical Working Papers  
**Foundational References:** John H. Cochrane (Stanford GSB), Deirdre N. McCloskey, Holthausen & Watts (2001), Barth, Beaver, & Landsman (2001), Brown, Lo, & Lys (1999), Cameron, Gelbach, & Miller (2008), Gow, Ormazabal, & Taylor (2010), Gopen & Swan (1990), Kobak et al. (2024), and TU FOM (2019).

---

## Purpose of this Standard

This document is **not** a summary of any existing manuscript, nor is it a retrospective justification of past writing choices. It is an **independent, uncompromising, state-of-the-art normative standard** designed to audit, critique, stress-test, and elevate empirical research in accounting and financial economics. 

Use this standard to audit drafts ruthlessly. If a draft violates these principles—whether through mechanical circularity, spurious correlation, scale distortions, over-claimed causality, superficial literature summaries, or synthetic AI-generated fluff—it must be corrected.

---

## 1. Epistemology & Theoretical Discipline in Value-Relevance Research

### 1.1 The Association Criterion vs. Welfare/Standard-Setting Claims
- **Understand what value relevance does and does not measure:** Following the seminal critique of Holthausen & Watts (2001) and the defense of Barth, Beaver, & Landsman (2001), an empirical association between an accounting metric and stock price establishes **only** that the metric reflects or summarizes information that is impounded in secondary market valuations.
- **Never claim welfare or standard-setting optimality:** Finding that an accounting number is statistically associated with share prices does **not** prove that the accounting standard is socially optimal, that managers are acting in shareholder interests, or that market efficiency is verified. Avoid leapfrogging from statistical association ($\beta \ne 0$) to normative policy endorsements.
- **Acknowledge the contracting and stewardship roles:** Financial accounting numbers serve debt contracting, regulatory capital adequacy, and executive compensation—not merely equity pricing (Holthausen & Watts, 2001). When bank equity prices diverge from book values or earnings, recognize that regulatory capital compliance (e.g., NRB prudential capital mandates) and loan loss provisioning may supersede secondary equity market considerations.

### 1.2 Theoretical Anchoring in the Clean-Surplus Framework
- **Ground linear valuation models in formal theory:** The regression of equity prices on earnings and book value is not an ad-hoc heuristic; it derives mathematically from the clean-surplus relation ($BV_t = BV_{t-1} + NI_t - Div_t$) and linear information dynamics under the Residual Income Valuation (RIV) framework (Ohlson, 1995; Feltham & Ohlson, 1995).
- **Interpret stock vs. flow variables correctly:**
  - **Book Value per Share ($\text{BVPS}$):** Represents the historical, cumulative net asset stock contributed by equity holders and retained from past operations. In banking, it serves as the ultimate liquidation and regulatory solvency anchor.
  - **Earnings per Share ($\text{EPS}$):** Represents current operational flow and serves as a proxy for the mean-reverting path of future abnormal earnings.
- **Account for transitoriness across structural disruptions:** As established by Collins, Maydew, & Weiss (1997) and Kwon & Wang (2020), when corporate events (mergers, reorganizations, sudden regulatory capital mandates) inject transitory items, restructuring costs, and portfolio provisioning into reported earnings, earnings persistence drops. In such regimes, rational investors place greater relative valuation weight on balance-sheet net worth ($\text{BVPS}$) than on volatile contemporaneous earnings ($\text{EPS}$).

---

## 2. Econometric Integrity & The Eight Deadly Empirical Traps

Any empirical paper in accounting or finance must actively defend against the eight classic methodological traps. A paper that succumbs to any of these is flawed at its foundation.

### Trap 1: Mechanical Circularity and Endogenous Multiples
- **The Violation:** Including price-derived valuation multiples—such as the Price-to-Earnings ($\text{P/E}$) ratio, Price-to-Book ($\text{P/B}$) ratio, or Market-to-Book ratio—as explanatory regressors in models where Market Price per Share ($\text{MPS}$) is the dependent variable.
- **The Consequence:** Because $\text{P/E} = \text{MPS} / \text{EPS}$, regressing $\text{MPS}$ on $\text{P/E}$ places the dependent variable directly inside the numerator of its own regressor. This creates deterministic mathematical endogeneity, spuriously inflates $R^2$, biases all other regression slopes, and completely invalidates hypothesis testing.
- **The Standard:** Strict and absolute exclusion of all price-deflated or market-derived multiples from the right-hand side of valuation regressions. Explanatory variables must consist exclusively of fundamental accounting figures and exogenous indicators determined independently of secondary market share prices.

### Trap 2: The Scale Effect and the $R^2$ Illusion
- **The Violation:** Interpreting high or shifting $R^2$ values in unscaled levels regressions as evidence of high or changing "value relevance," or comparing raw $R^2$ across different sub-samples without addressing scale differences.
- **The Consequence:** As demonstrated by Brown, Lo, & Lys (1999) and Easton (1998), regressing unscaled share price on per-share accounting metrics across firms with wide differences in scale induces severe heteroskedasticity and artificially inflates $R^2$ simply due to cross-sectional scale dispersion. Apparent temporal shifts in $R^2$ across regimes are frequently statistical artifacts of changing cross-sectional sample variance rather than true shifts in information relevance.
- **The Standard:** 
  1. Do not rely primarily on $R^2$ to claim structural change; rely on formal coefficient interaction parameters ($\delta$) and joint Wald tests.
  2. Implement panel fixed effects to absorb cross-sectional scale heterogeneity.
  3. When pooled cross-sectional models are reported, disclose that scale differences inflate explanatory power relative to within-firm panel estimators.

### Trap 3: Look-Ahead Bias and Information Availability Timing
- **The Violation:** Aligning fiscal-year-end closing prices (e.g., Ashadh-end / mid-July in Nepal) with audited annual accounting statements that were not completed, audited, or disclosed until months later.
- **The Consequence:** Conditioning market prices at time $t$ on accounting disclosures that only entered the public domain at time $t + k$ introduces severe look-ahead bias and reverse causality. It violates the core premise of capital markets research: prices can only reflect information that was publicly known at the observation timestamp (Ball & Brown, 1968; Beaver, 1968; Bernard & Thomas, 1989).
- **The Standard:** 
  1. Share prices must be sampled **after** the financial accounts have been made legally and publicly available.
  2. If specific corporate press-release timestamps cannot be verified with archival audit trails across historical samples, establish an objective, statutory cutoff rule (such as the BAFIA Section 59(2) 9-month statutory reporting deadline at Chaitra-end).
  3. State the operational window explicitly and implement a strict freshness rule (e.g., 5 trading days) to ensure prices reflect active floor trading rather than stale historical quotes.

### Trap 4: Small-Cluster Over-Confidence and Downward-Biased Standard Errors
- **The Violation:** Relying on naive OLS standard errors, or uncritically applying standard cluster-robust sandwich covariance estimators (e.g., Huber-White cluster) when the number of clusters is small (e.g., $G < 30$).
- **The Consequence:** As proven by Cameron, Gelbach, & Miller (2008), Petersen (2009), and Gow, Ormazabal, & Taylor (2010), standard cluster-robust standard errors rely on asymptotic theory where $G \to \infty$. When clusters are few (such as $G = 5$ or $G = 10$), the asymptotic sandwich estimator is severely biased downward, producing artificially inflated $t$-statistics, falsely tiny $p$-values, and catastrophic over-rejection of the null hypothesis (false discoveries).
- **The Standard:** 
  1. Never report unadjusted OLS standard errors in panel datasets with cross-sectional and temporal dependence.
  2. With small cluster dimensions, deploy finite-sample leverage corrections, specifically the MacKinnon-White (1985) HC3 covariance estimator, which applies a $(1 - h_{ii})^2$ leverage penalty to protect against over-rejection.
  3. Treat all inferential tests in small-$G$ panels as exploratory indicators rather than asymptotic certainties, and report exact $p$-values rather than binary cutoff asterisks.

### Trap 5: Parameter Proliferation and Degrees-of-Freedom Depletion
- **The Violation:** Adding multi-way fixed effects, multiple interaction terms, and supplementary control variables to small samples without transparent parameter accounting.
- **The Consequence:** In a panel of $N = 28$ observations, estimating 5 bank fixed effects (4 dummies), 6 year fixed effects (5 dummies), an intercept, two baseline slopes, and two interaction slopes consumes $1 + 4 + 5 + 2 + 2 = 14$ parameters. The residual degrees of freedom collapse to $28 - 14 = 14$. Under 14 degrees of freedom, the statistical power of the regression is constrained, and tests are sensitive to individual influential points.
- **The Standard:** 
  1. Always explicitly compute and state residual degrees of freedom ($df = N - K$) in every regression table and text discussion.
  2. Screen for collinearity absorption (e.g., recognizing that time dummies $\sum_{t \in \text{Post}} \lambda_t$ perfectly absorb the standalone $Post_t$ indicator).
  3. Run sensitivity tests (such as Cook's distance and studentized residuals) to confirm that findings are not driven by single high-leverage observations.

### Trap 6: Asterisk Econometrics and the Neglect of Economic Significance
- **The Violation:** Focusing exclusively on whether a $p$-value falls below $0.05$ or $0.01$ (hunting for asterisks) while completely ignoring the economic magnitude, sign, and practical plausibility of the estimated coefficients (McCloskey & Ziliak, 1996; Cochrane, 2005).
- **The Consequence:** A statistically significant coefficient may be economically trivial, or an economically massive coefficient may carry a wide confidence interval in small samples. Treating statistical significance as synonymous with economic importance is bad economics.
- **The Standard:** 
  1. Interpret the economic magnitude of coefficients directly: What does a $\beta_E = 6.43$ mean in rupees of market price for every rupee of EPS? Is that multiple plausible relative to the sector's price-to-earnings distribution?
  2. Report and interpret confidence intervals alongside point estimates.
  3. Discuss economic significance alongside statistical significance.

### Trap 7: Pseudo-Causal Creep in Observational Studies
- **The Violation:** Using causal verbs ("mergers improved," "consolidation caused," "the reform impacted") in non-experimental, observational designs where treatment assignment is non-random and regimes are demarcated by calendar time (Angrist & Pischke, 2009, 2010; Atanasov & Black, 2016).
- **The Consequence:** In calendar-time event studies, the post-event indicator ($Post_t$) captures not only the event of interest (banking consolidation), but also every contemporaneous macroeconomic shift, interest rate change, inflation trend, regulatory policy adjustment, and broad-market index movement that occurred over the same time horizon. Attributing observed parameter shifts solely to corporate mergers is an identification fallacy.
- **The Standard:** 
  1. Use strictly associational, non-causal language: *"is consistent with"*, *"coincided with"*, *"was associated with"*, *"attenuated across the consolidation divide"*.
  2. Formally declare that the model estimates conditional statistical associations rather than isolated causal treatment effects.
  3. Explicitly list concurrent macroeconomic and capital market confounding factors that occurred during the sample period.

### Trap 8: Survivorship and Truncation Distortions
- **The Violation:** Deleting missing, delisted, or trading-suspended observations without documentation, or imputing stale prices from months prior to avoid missing data.
- **The Consequence:** Corporate reorganizations frequently induce prolonged regulatory trading suspensions. Imputing a price from 60 days before the reporting window contaminates the regression with stale, pre-merger sentiment; conversely, silently dropping observations hides survivorship bias and distorts sample attrition.
- **The Standard:** 
  1. Establish an explicit, reproducible protocol for missing data and trading halts (e.g., a formal 5-day freshness rule).
  2. Document every excluded observation with its exact corporate action, suspension dates, and days elapsed.
  3. Conduct sensitivity analyses evaluating entity-timing mismatches (e.g., when historical financial statements reflect standalone operations while trading prices reflect the unified corporate entity).

---

## 3. Information Architecture & Rhetorical Structure (The Cochrane Standard)

A research paper or dissertation in finance is an exercise in persuasion through evidence, not a chronological diary of what the researcher did (Cochrane, 2005).

```
┌────────────────────────────────────────────────────────────────────────┐
│                   THE INFORMATION PYRAMID (Cochrane, 2005)              │
│                                                                        │
│   1. THE CORE FINDING       What do we learn about valuation and       │
│      (First 2 pages)        consolidation that was previously unknown? │
│                                                                        │
│   2. THE ECONOMIC PUZZLE    Why does this setting, conflict, or regime │
│      (Introduction)         shift matter for market pricing?           │
│                                                                        │
│   3. THE IDENTIFICATION     Why does this model isolate the parameter, │
│      (Methodology)          and what are its exact structural limits?  │
│                                                                        │
│   4. THE MEASURED FACTS     What do the coefficients, Wald tests, and  │
│      (Results)              robustness models actually show?           │
│                                                                        │
│   5. THE SYNTHESIS          How does this alter our view of prior      │
│      (Discussion)           literature and regulatory reality?         │
└────────────────────────────────────────────────────────────────────────┘
```

### 3.1 The 15-Minute Skim Test
A professional reader (supervisor, external examiner, journal referee) reads an empirical finance paper hierarchically:
1. **Title and Abstract:** What is the specific question, the empirical setting, the core estimate, and the overarching conclusion?
2. **Introduction:** By page 2 or 3, the reader must know:
   - What is the question?
   - Why is it important?
   - What did the author do (data, sample, period, estimator)?
   - What is the central empirical finding (exact magnitudes and significance)?
   - What does it teach us that prior literature missed?
3. **Tables and Figures:** The reader flips straight to the primary tables (Descriptive Statistics, Baseline Model, Interaction Model, Robustness Suite). Every table must be completely self-contained.
4. **Conclusion:** Does it summarize the answers cleanly without introducing new, unexamined claims or apologizing for bounded results?

If a reader cannot pass the 15-minute skim test with complete comprehension of your findings, the paper is structurally disorganized.

### 3.2 Eradicating the Laundry-List Introduction
- **Do not begin with historical trivia or elementary textbooks:** Never open with "Since ancient times, trade has been important..." or "Commercial banks play an important role in the economy by taking deposits and making loans." 
- **Hook the economic problem immediately:** Open with the tension: Equity valuation models predict that market prices reflect fundamental earnings capacity and balance-sheet asset backing. In emerging banking systems undergoing concentrated consolidation, however, financial reporting faces a dual crisis of earnings transitoriness and capital restructuring. Does the secondary market continue to price earnings, or does valuation shift to balance-sheet net worth?
- **Do not write a "roadmap" that simply recites chapter numbers:** The final paragraph of an introduction should briefly state the structural organization, but each sentence should preview the *intellectual purpose* of the chapter, not merely its title.

---

## 4. Literature Review: Thematic Dialectics vs. Annotated Bibliographies

### 4.1 The Difference Between an Annotated Bibliography and a Critical Review
- **The Annotated Bibliography (Amateur Standard):**
  > *"Bhattarai (2014) examined nine banks and found EPS was positive. Pradhan (2016) examined 14 banks and found size was positive. Joshi (2023) studied seven banks and found BVPS was positive. Pant (2024) studied seven banks and found BVPS was negative."*  
  *Critique:* This is a lifeless catalogue of past papers. It teaches the reader nothing about *why* the findings contradict each other, what methodological flaws caused the divergence, or what intellectual debate remains unresolved.
- **The Thematic Dialectic (Scholar Standard):**
  > Group the literature around structural themes, methodological debates, and empirical contradictions:
  1. *The Earning Power vs. Net Asset Value Debate:* Contrast studies where earnings dominate (e.g., Bhandari, 2026; Niroula, 2021) against studies where book value dominates (e.g., Chhetri, 2023; Silwal, 2019), and explain the institutional or macroeconomic context (e.g., capital escalation shocks, non-performing asset surges) that drove the divergence.
  2. *The Methodological Flaw of Circular Multiples:* Systematically document how prior studies contaminated their specifications by including $\text{P/E}$ ratios in share price regressions, generating spurious correlation.
  3. *The Temporal Misalignment Problem:* Document how previous literature relied on Ashadh-end prices that preceded public disclosure, creating severe look-ahead bias.
  4. *The Static Pooling Assumption:* Critique prior Nepalese literature for universally estimating static full-sample averages, failing to test whether valuation parameters shifted across the structural consolidation wave.

### 4.2 The Literature Synthesis Matrix
Every empirical dissertation must feature a comprehensive, standardized Literature Synthesis Matrix (e.g., Table 2.1) structured with the following mandatory columns:
- **Study & Author(s)** (Formal APA citation);
- **Sample & Period** (Number of cross-sections, exact years, total observations);
- **Econometric Methodology** (Pooled OLS, Random Effects, Two-Way Fixed Effects, etc.);
- **Key Variables Investigated** (Dependent and explanatory variables);
- **Core Findings & Methodological Critique** (Direction, significance, and specific limitations such as circular multiples, unadjusted standard errors, or Ashadh-end pricing).

### 4.3 Formulating the Research Gap
A genuine research gap is **never** merely geographical ("No one has studied this in Pokhara") or chronological ("No one has studied 2024 yet"). A scholarly research gap is an **unresolved theoretical tension or an uncorrected methodological flaw**:
1. *The Structural Shift Gap:* Failure of extant literature to test parameter stability across corporate consolidation divides using interactive panel specifications.
2. *The Endogeneity/Circularity Gap:* Pervasive reliance on circular price-derived multiples in share price models.
3. *The Temporal Look-Ahead Gap:* Failure to synchronize price observation with legal, audited disclosure availability.
4. *The Small-Cluster Inferential Gap:* Reliance on naive or invalid standard errors in small-sample banking panels.

---

## 5. Methodological Rigor & Data Integrity

### 5.1 Sample Selection and Purposive Criteria
- **State selection criteria with operational precision:** If the sample is purposive (judgmental), state the exact exclusion and inclusion hurdles:
  1. Sectoral classification (licensed Class 'A' commercial banks);
  2. Direct participation in the focal consolidation wave versus continuous unmerged benchmark status;
  3. Continuous availability of audited primary financial reports across the entire longitudinal horizon;
  4. Availability of verifiable secondary market trading prices satisfying the post-deadline freshness window.
- **Disclose sample boundaries and coverage:** Document the proportion of aggregate sector assets, equity, or market capitalization represented by the sampled institutions to substantiate sectoral relevance.

### 5.2 Primary vs. Secondary Source Reconciliation
- **Never rely uncritically on third-party aggregators:** Financial web aggregators (ShareSansar, Merolagani, FinancialNotices) frequently contain transcription errors, unadjusted bonus share distortions, and rounded values.
- **Enforce the Primary Audit Rule:** All accounting fundamentals (ordinary share capital, reserves, total equity attributable to equity holders, net profit after tax, basic EPS, audited NAV per share) must be extracted directly from primary, audited annual financial statements. Secondary compilations serve only as secondary flags; any discrepancies must be resolved in favor of the audited accounts.
- **Document capital actions explicitly:** Changes in share bases due to bonus share capitalizations, rights offerings, or merger share swap ratios must be audited across annual report notes (Share Capital and Reserves schedules).

---

## 6. Reporting Results: Economic Meaning, Diagnostics, and Robustness

### 6.1 Principles of Tabular Presentation
- **Self-Contained Requirement:** A reader must be able to comprehend a table and its findings without reading the narrative text.
- **Table Headers:** Titles must be informative, bold, and placed **above** the table.
- **Comprehensive Footnotes:** Must be placed **below** the table in single spacing, containing:
  - Exact definition of every variable and acronym;
  - Unit of measurement (e.g., NPR per share, percentage);
  - Sample size ($N$) and panel structure (cross-sections $n$, time periods $T$);
  - Estimator type (e.g., Two-Way Fixed Effects with Bank and Year Fixed Effects);
  - Standard error specification (e.g., MacKinnon-White HC3 heteroskedasticity-robust standard errors);
  - Residual degrees of freedom ($df$);
  - Definition of all significance levels and asterisks ($^{***}p < 0.01, ^{**}p < 0.05, ^{*}p < 0.10$).

### 6.2 Narrative Discussion of Regression Estimates
- **Do not recite tables:** Never write: "As seen in Table 4.4, the coefficient of EPS is 6.430 with a t-stat of 2.47 and p-value of 0.025, and BVPS is 0.781 with a t-stat of 0.92..."
- **Narrate the economic and theoretical story:** 
  > *"In the baseline model, earnings per share exhibits a positive and statistically significant association with market price ($\hat{\beta}_E = 6.43, p = 0.025$). Economically, this indicates that each additional rupee of audited earnings per share is associated with an incremental market price of NPR 6.43, after conditioning on balance-sheet net worth, time-invariant bank characteristics, and common macroeconomic shocks. Conversely, book value per share yields a positive but statistically insignificant conditional association ($\hat{\beta}_B = 0.78, p = 0.370$), indicating that within-bank market price variation was predominantly anchored in operating profitability rather than historical net asset book values during the baseline horizon."*

### 6.3 The Regime Interaction Model and Joint Wald Testing
- **Explain interaction mechanics clearly:**
  - $\beta_E$ and $\beta_B$ represent baseline slopes (pre-consolidation regime).
  - $\delta_E$ and $\delta_B$ represent the incremental slope shifts in the post-consolidation regime.
  - The total post-consolidation valuation slopes are $(\beta_E + \delta_E)$ and $(\beta_B + \delta_B)$.
- **Do not rely solely on individual $t$-tests for interaction terms:** When individual interaction terms carry collinearity or small-sample noise, evaluate the **joint Wald test**:
  $$H_0: \delta_E = 0 \text{ and } \delta_B = 0$$
  Reporting the joint $F$-test statistic and exact $p$-value tests whether the *combined accounting valuation structure* shifted across regimes, protecting against false negatives arising from collinear slope reallocation.

### 6.4 The Robustness Suite as a Scientific Stress Test
A robustness section is not decorative; it is an active effort to falsify your own findings. Design robustness checks to address specific structural vulnerabilities:
1. **Model Specification Sensitivity:** Pooled OLS vs. Bank Fixed Effects vs. Two-Way Fixed Effects.
2. **Alternative Proxy Substitution:** Replacing per-share earnings ($\text{EPS}$) with asset-scaled profitability ($\text{ROA}$) to eliminate per-share price scale effects.
3. **Omitted Variable Inclusion:** Introducing cash dividend announcements ($\text{DPS}$) to test whether earnings relevance was merely proxying for payout signaling.
4. **Transition Shock Exclusion:** Removing the consolidation transition year (FY 2079/80) to confirm that findings reflect sustained structural shifts rather than transient merger implementation turbulence.
5. **Entity-Timing Mismatch Sensitivity:** Removing the boundary year (FY 2078/79) to eliminate the friction of pairing pre-merger standalone balance sheets with post-merger consolidated trading prices.
6. **Accounting Capital Adjustments:** Re-estimating models using bonus-share-adjusted metrics and retrospective audited restatements.

---

## 7. Tone, Academic Prose, and Eradication of AI Slop (The Kobak Standard)

Academic writing in economics and finance must be objective, sober, precise, and transparent. Every sentence must communicate verified facts or reasoned economic arguments.

### 7.1 Absolute Eradication of Generative AI Vocabulary
Recent large-scale bibliometric analyses (Kobak et al., 2024; Gray, 2024) have proven that LLMs heavily over-index on a specific cluster of decorative, pseudo-intellectual words. Their presence in a manuscript immediately signals unedited AI generation to examiners and journal editors.

**The Prohibited Vocabulary & Replacement Guide:**

| Prohibited AI Cliché | Why It Fails | Scholarly Replacement |
| :--- | :--- | :--- |
| **delve / delving** | Gratuitous pseudo-scholarly flourish | *examine, investigate, analyze, evaluate* |
| **underscores** | Overused emphatic crutch | *indicates, reveals, demonstrates, highlights* |
| **showcasing / showcase** | Promotional PR language | *illustrating, displaying, presenting, documenting* |
| **pivotal / testament** | Dramatic editorializing | *critical, central, evidence of, consistent with* |
| **beacon / tapestry** | Empty poetic metaphor | *benchmark, framework, institutional environment* |
| **paramount / crucial role**| Unearned rhetorical emphasis | *substantial, significant, necessary, foundational* |
| **game changer** | Colloquial corporate jargon | *structural shift, major reorganization* |
| **multifaceted / myriad** | Vague filler for complex phenomena | *diverse, multiple, specific, distinct* |
| **serves as a testament to** | Empty celebratory fluff | *provides evidence of, reflects* |
| **it is important to note that**| Throat-clearing padding | *Cut entirely; state the fact directly* |

### 7.2 Active Scholarly Voice vs. Passive Bureaucratic Evasion
- **Avoid agentless passives:** Instead of *"It was observed that the coefficient decreased,"* write *"The estimated coefficient decreased"* or *"We find that the coefficient attenuated."*
- **Avoid anthropomorphism:** Data do not "speak," tables do not "believe," and numbers do not "know." A regression does not "find"; the researcher finds using the regression.
- **Write with simple Saxon clarity:** Prefer short, direct verbs over Latinate circumlocutions:
  - *use* instead of *utilize*;
  - *help* instead of *facilitate*;
  - *change* instead of *undergo transformation*;
  - *show* instead of *demonstrate empirical veracity*.

### 7.3 Information Architecture at the Sentence Level (Gopen & Swan, 1990)
- **The Topic Position (Beginning):** The first 5 to 7 words of a sentence should connect directly to what the reader already knows (the subject, the anchor, the context).
- **The Stress Position (Ending):** The end of a sentence carries the natural rhetorical weight. Place your punchline, your coefficient, your statistical decision, or your core finding at the very end of the sentence.
- **Never strand the finding in the middle:** 
  - *Weak:* *"The coefficient for EPS, which was 6.43 and statistically significant at the 5% level, indicated value relevance in the baseline model."*
  - *Strong:* *"In the baseline model, earnings per share is statistically significant and economically positive ($\hat{\beta}_E = 6.43, p = 0.025$)."*

---

## 8. Summary, Conclusions, and Decision Integrity (Chapter V)

### 8.1 Direct Answers to Research Questions
Chapter V must not be an unfocused recap. It must systematically deliver clear, definitive answers to the specific research questions posed in Chapter I:
- Did the accounting fundamentals exhibit baseline value relevance? **Answer directly with empirical support.**
- Did the valuation slopes shift across the consolidation divide? **Answer directly with Wald test evidence.**
- Were the empirical relationships robust across alternative specifications and sample restrictions? **Answer directly based on the robustness suite.**

### 8.2 The Formal Hypothesis Testing Decision Table
Every scientific dissertation must present a clear, tabular summary of all formal hypotheses, the tested parameter, empirical estimate, test statistic, exact $p$-value, and explicit decision:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        FORMAL HYPOTHESIS DECISION FRAMEWORK                             │
│                                                                                        │
│  Hypothesis   Parameter   Estimate   Test Stat & p-value   Decision (α = 0.05)         │
│  ────────────────────────────────────────────────────────────────────────────          │
│  H1 (EPS)     β_E ≠ 0     +6.430     t = 2.47, p = 0.025   Supported (Reject H0)       │
│  H2 (BVPS)    β_B ≠ 0     +0.781     t = 0.92, p = 0.370   Not Supported (Fail to rej) │
│  H3 (Δ EPS)   δ_E ≠ 0    -14.619     t = -1.82, p = 0.089  Not Supported at 5% (p<0.10)│
│  H4 (Δ BVPS)  δ_B ≠ 0     +0.087     t = 0.05, p = 0.963   Not Supported (Fail to rej) │
│  Joint Shift  δ_E=δ_B=0   Vector     F = 2.76, p = 0.098   Supported at 10% Level      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 8.3 Tripartite Policy and Managerial Implications
Under TU FOM standards, practical implications must be categorized into three distinct, non-overlapping stakeholder domains:
1. **Capital Market Participants & Equity Investors:** How investors should interpret reported post-merger accounting numbers; recognizing earnings transitoriness; relying on balance-sheet capital strength during restructuring; avoiding naive trailing P/E multiples.
2. **Commercial Bank Executives & Boards of Directors:** Capital management strategies; managing earnings volatility during integration; communicating balance-sheet transparency; dividend payout sustainability following share capital expansion.
3. **Statutory Regulators & Policy Makers (NRB, SEBON, NEPSE):** Developing centralized, timestamped corporate disclosure databases; reducing protracted merger trading suspensions that destroy liquidity; refining reporting guidelines under NFRS/IFRS 9.

---

## 9. Formatting, Typography, and Compliance (TU FOM 2019)

### 9.1 Dimensions and Typography
- **Margins:** Top: 2.54 cm (1.0 in), Bottom: 2.54 cm (1.0 in), Right: 2.54 cm (1.0 in), Left: **3.18 cm (1.25 in)** (mandatory allowance for binding).
- **Typeface:** **Times New Roman** uniformly across all pages, titles, headings, and tables.
- **Font Sizes:**
  - Chapter Headings: 14–16 pt bold centered.
  - Section Headings: 12 pt bold.
  - Body Text: 12 pt regular.
  - Table and Figure Interiors: 10–11 pt.
  - Table Notes and Footnotes: 9–10 pt.
- **Line Spacing:**
  - Body narrative: **True 1.5 line spacing** (pitch $\approx 20.66$ pt).
  - Single line spacing: Table of Contents, Lists of Tables/Figures, table interiors, block quotations, footnotes, and References.
- **Paragraph Layout:** Flush left, 0 pt first-line indent, followed by a 10 pt paragraph gap (`\parskip`).

### 9.2 Pagination Standards
- **Preliminary Pages (Front Matter):** Numbered consecutively in lowercase Roman numerals (**i, ii, iii, iv...**), placed at the **bottom center** of the page. The Title Page is counted as page `i` but does not carry a printed page number.
- **Main Body (Chapters I–V, References, Appendices):** Numbered consecutively in Arabic numerals (**1, 2, 3...**), placed at the **top right corner** of the page. Page 1 begins on the first page of Chapter I.

### 9.3 Front Matter Structural Order
1. Title Page (counted, unnumbered);
2. Certification of Authorship (strictly single page);
3. Report of Viva-Voce Committee (strictly single page);
4. Declaration of Authenticity (strictly single page);
5. Acknowledgements (strictly single page);
6. Table of Contents (single-spaced, dot leaders, right-aligned pages);
7. List of Tables (single-spaced);
8. List of Figures (single-spaced);
9. Abbreviations / Acronyms (alphabetized, single-spaced);
10. Abstract (strictly single page, narrative summary, $\le 5$ keywords).

---

## 10. The 25-Point Comprehensive Quality Audit Rubric

Before any draft or chapter is finalized, evaluate it against this 25-point master rubric. Every question must be answered with a verified **"YES"**.

### Econometric Rigor & Identification
- [ ] 1. Are price-derived multiples (P/E, P/B) strictly excluded from the right-hand side of all price models?
- [ ] 2. Are share prices sampled strictly *after* audited financial reports were legally in the public domain (no look-ahead bias)?
- [ ] 3. Is the operational pricing window defended using institutional/statutory requirements (e.g., BAFIA Section 59(2))?
- [ ] 4. Are trading halts and missing observations governed by an objective freshness rule, with zero unverified imputations?
- [ ] 5. Are both cross-sectional (bank) and temporal (year) unobservables controlled for via two-way fixed effects?
- [ ] 6. Is the absorption of the standalone $Post_t$ indicator by year fixed effects clearly explained mathematically?
- [ ] 7. Are standard errors adjusted for finite-sample leverage and small-cluster bias using MacKinnon-White HC3?
- [ ] 8. Are exact residual degrees of freedom ($df = N - K$) disclosed and evaluated in every regression specification?
- [ ] 9. Are empirical findings framed strictly associationally, with zero unwarranted causal claims?
- [ ] 10. Is the regression model subjected to a multi-pronged robustness suite (proxy substitution, omissions, transition exclusions, capital restatements)?

### Data & Archival Precision
- [ ] 11. Do all numbers, sample counts, and test statistics match 100% across text, tables, figures, and code?
- [ ] 12. Are corporate actions (acquisitions, bonus shares, rights issues, swap ratios) fully audited against primary financial report notes?
- [ ] 13. Is the exact realized clean sample size ($N = 28$, pre $= 13$, post $= 15$) consistently maintained across all baseline tables?
- [ ] 14. Are collinearity diagnostics (Pearson $r$, VIF, tolerance) formally reported, specifically addressing EPS–ROA collinearity?

### Writing Craft & Information Architecture
- [ ] 15. Does the introduction hook the economic puzzle within the first two pages?
- [ ] 16. Is the literature review organized around thematic tensions and methodological debates rather than an annotated laundry list?
- [ ] 17. Does the literature review include a structured, comprehensive synthesis matrix with methodological critiques?
- [ ] 18. Are the 5 identified literature gaps grounded in structural and econometric limitations of prior research?
- [ ] 19. Do regression discussions focus on economic magnitudes, multiples, and patterns rather than mechanical cell recitation?
- [ ] 20. Are all tables and figures completely self-contained with comprehensive notes defining all terms, units, estimators, and asterisks?
- [ ] 21. Does Chapter V directly answer all Research Questions and provide a formal Hypothesis Testing Decision Table?
- [ ] 22. Are implications rigorously partitioned across investors, bank executives, and statutory regulators?
- [ ] 23. Is the entire manuscript 100% free of AI filler words (*delve, underscores, showcasing, pivotal, testament, beacon, tapestry*)?
- [ ] 24. Are citations formatted in strict APA 6th Edition using proper `\citet{}` and `\citep{}` commands?
- [ ] 25. Does the document strictly comply with TU FOM 2019 formatting (margins, 12pt TNR, 1.5 line spacing, Roman/Arabic pagination, single-page preliminary sections) and compile with **0 errors**?
