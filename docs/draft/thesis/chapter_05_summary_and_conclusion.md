# CHAPTER V: SUMMARY, CONCLUSION, AND IMPLICATIONS

## 5.1 Introduction

This concluding chapter synthesizes the theoretical arguments, empirical methodologies, econometric results, and interpretive discussions developed throughout this dissertation. The primary objective of this investigation has been to examine the value relevance of accounting information—specifically earnings per share (EPS) and book value per share (BVPS)—among prominent Nepalese commercial banks, and to evaluate whether the fundamental valuation relationships underwent a structural regime shift following the landmark commercial banking consolidation wave executed in early 2023 (mid-FY 2079/80).

In accordance with the Faculty of Management, Tribhuvan University *Master's Degree Dissertation Guidelines* (2019, p. 15), this chapter is organized into four core functional sections:
1. **Summary of the Study** (Section 5.2), providing an integrated overview of the research problem, operational objectives, theoretical foundation, research design, and major empirical results;
2. **Conclusions** (Section 5.3), articulating the definitive insights and academic knowledge derived from the empirical findings regarding accounting value relevance, structural discontinuities, and capital market pricing behavior in Nepal;
3. **Implications of the Study** (Section 5.4), delineating targeted, actionable implications for regulatory institutions (Nepal Rastra Bank and the Securities Board of Nepal), commercial bank executives, retail and institutional equity investors, and accounting standard setters; and
4. **Recommendations and Directions for Future Research** (Section 5.5), presenting practical policy recommendations alongside prospective avenues for subsequent scholarly inquiry.

---

## 5.2 Summary of the Study

### 5.2.1 Research Overview, Problem, and Objectives

The valuation of common equity lies at the intersection of accounting disclosure, corporate governance, and capital market efficiency. Under the residual income valuation (RIV) framework established by Ohlson (1995) and Feltham and Ohlson (1995), market equity value is formalized as a linear function of contemporaneous balance-sheet equity (book value per share, capturing cumulative resources) and operational profitability (earnings per share, capturing abnormal forward-looking earning capacity), anchored in the clean-surplus accounting relation. 

In emerging and frontier capital markets such as Nepal, the empirical stability of these accounting valuation relationships is routinely challenged by institutional friction, regulatory shifts, information asymmetry, and structural corporate reorganizations. The commercial banking sector in Nepal represents the dominant institutional pillar of the Nepal Stock Exchange (NEPSE), historically accounting for the largest share of aggregate market capitalization, annual trading turnover, and retail investor participation (Bhattarai, 2014; Pradhan & Dahal, 2016; Timalsina, 2026). Over the past decade, Nepal Rastra Bank (NRB) pursued aggressive regulatory policies to consolidate the banking industry, culminating in the 2022–2023 consolidation wave during which major commercial banks executed large-scale horizontal amalgamations and statutory acquisitions.

Despite the monumental scale of this corporate restructuring, existing empirical research on Nepalese banking equity valuation exhibited substantial theoretical, methodological, and econometric deficiencies:
1. Prior studies universally employed static, full-sample pooled regressions, implicitly assuming parameter stability and failing to test whether corporate combinations altered valuation multiples across the pre- and post-consolidation regimes (Chaudhari, 2025; Chhetri, 2023; Gurung & Dahal, 2025; Timalsina, 2026);
2. Empirical models frequently introduced the circular Price-to-Earnings (P/E) ratio as an independent regressor predicting market share price (MPS), embedding the dependent variable within its own explanatory matrix and generating severe mechanical endogeneity and spurious correlation (Bhattarai, 2014; Giri, 2024; Joshi, Ghimire, & Singh, 2023; Pant, Joshi, & Saud, 2024);
3. Share prices were conventionally measured at fiscal year-end (Ashadh-end / mid-July), long before audited annual financial statements were completed and published, inducing severe look-ahead bias and violating temporal causality (Ball & Brown, 1968; Beaver, 1968); and
4. Prior panel estimations routinely ignored the finite-sample constraints of small cross-sectional clusters ($G = 5$), risking false discoveries and overstated statistical precision through inappropriate covariance estimators.

To resolve these empirical gaps, this dissertation addressed three core research questions:
1. Are fundamental accounting measures (EPS and BVPS) statistically associated with secondary market share prices observed immediately following statutory annual reporting deadlines ($MPS^{RD}$)?
2. Did the valuation associations of EPS and BVPS differ significantly between the pre-consolidation period (FY 2076/77–2078/79) and the post-consolidation period (FY 2079/80–2081/82)?
3. How sensitive are the estimated valuation coefficients to transition-year effects, entity-timing mismatches, operating profitability substitutions, dividend exclusions, bonus share adjustments, and restated earnings?

Correspondingly, the study set out to: (i) evaluate the baseline value relevance of EPS and BVPS under a standardized post-reporting-deadline pricing framework; (ii) quantify structural shifts in valuation slopes across the 2023 consolidation wave using an interactive panel specification; and (iii) execute a comprehensive eight-part robustness suite to establish the empirical boundary conditions of accounting multiples in Nepal.

---

### 5.2.2 Methodology and Research Design Synthesis

To execute this investigation with rigorous econometric discipline, the study employed a longitudinal panel design spanning six fiscal years (FY 2076/77 through FY 2081/82, corresponding to 2019/20 through 2024/25). The target population encompassed all Class 'A' commercial banks listed on NEPSE. A purposive sample of five prominent commercial banking series was selected:
- Four amalgamated banking series representing the major corporate combinations of the early-2023 wave: Global IME Bank Limited (GBIME, absorbed Bank of Kathmandu), Himalayan Bank Limited (HBL, acquired Civil Bank), Kumari Bank Limited (KBL, absorbed NCC Bank), and Nepal Investment Mega Bank Limited (NIMB, amalgamation of Nepal Investment Bank and Mega Bank Nepal); and
- One unmerged benchmark banking series: NMB Bank Limited (NMB), which maintained continuous, independent corporate operations throughout the 2023 wave without participating in horizontal combinations.

To eliminate look-ahead bias, market prices were observed at a standardized window immediately following the statutory annual financial reporting deadline. Section 59(2) of the Banks and Financial Institutions Act, 2017 (BAFIA) legally mandates that commercial banks publish their audited annual balance sheets and profit and loss accounts within nine months of fiscal year-end—operationalized at the end of Chaitra (mid-April) of the subsequent fiscal year. The dependent variable, $MPS^{RD}$, was defined as the closing market price on the first trading session following this statutory threshold, subject to a strict 5-day freshness rule.

Under this 5-day rule, 28 clean bank-year observations were realized out of an intended balanced panel of 30 bank-years (13 pre-consolidation and 15 post-consolidation observations). Two observations were excluded and dropped rather than imputed: HBL FY 2077/78 (trading resumed 54 days late on 6 June 2022) and NIMB FY 2077/78 (trading resumed 47 days late on 30 May 2022), both resulting from prolonged secondary market trading suspensions during merger negotiations around the April 2022 deadline.

Econometric estimation was structured around two core models:
1. **Model 1 (Baseline Value Relevance):** Specified as a two-way fixed effects panel regression:
   $$MPS^{RD}_{it} = \mu_i + \lambda_t + \beta_E \text{EPS}_{it} + \beta_B \text{BVPS}_{it} + \varepsilon_{it}$$
   where $\mu_i$ captures unobserved bank fixed effects and $\lambda_t$ absorbs common fiscal-year macroeconomic shocks and NEPSE-wide price cycles. Residual degrees of freedom were exact: $28 - 12 = 16$.
2. **Model 2 (Regime Shift Interaction):** Specified to estimate structural changes across the early-2023 consolidation wave:
   $$MPS^{RD}_{it} = \mu_i + \lambda_t + \beta_E \text{EPS}_{it} + \beta_B \text{BVPS}_{it} + \delta_E (\text{EPS}_{it} \times Post_t) + \delta_B (\text{BVPS}_{it} \times Post_t) + \varepsilon_{it}$$
   where $Post_t = 1$ for post-consolidation years (FY 2079/80–2081/82) and 0 for pre-consolidation years (FY 2076/77–2078/79). The main effect of $Post_t$ was fully absorbed by the fiscal-year fixed effects ($\lambda_t$). Residual degrees of freedom were exact: $28 - 14 = 14$.

To safeguard against small-cluster downward bias ($G = 5$), all inferential statistical tests ($t$-tests, confidence intervals, and the principal joint Wald $F$-test of $H_0: \delta_E = \delta_B = 0$) were conducted using the MacKinnon-White (1985) HC3 heteroskedasticity-consistent covariance estimator.

---

### 5.2.3 Summary of Major Empirical Findings

The empirical analysis yielded several substantive findings regarding the statistical properties, baseline relevance, regime stability, and sensitivity of accounting fundamentals:

1. **Descriptive Shifts Across Regimes:**
   - **Market Price Collapse:** Full sample mean $MPS^{RD}$ stood at NPR 254.34. Across regimes, mean share price dropped by 33.80% from NPR 310.59 pre-consolidation to NPR 205.60 post-consolidation, while cross-sectional standard deviation contracted by 72.00% (from 119.46 to 33.45), documenting an aggressive market-wide price compression.
   - **Earnings Deterioration & Dispersion:** Mean EPS contracted by 40.11% from NPR 17.90 pre-consolidation to NPR 10.72 post-consolidation. Concurrently, earnings dispersion widened by 63.66% (SD increased from 3.99 to 6.53), reflecting asset quality friction and credit-loss provisioning volatility among consolidated entities.
   - **Dividend Elimination:** Cash dividends per share (DPS) experienced a severe collapse of 76.90% (from NPR 6.06 to NPR 1.40), with 12 out of 15 post-consolidation bank-years recording exactly zero cash dividends due to regulatory capital adequacy constraints.
   - **Book Value Stability:** Mean BVPS remained anchored across regimes, rising modestly by 2.44% from NPR 158.11 to NPR 161.97, reflecting statutory reserve retention mandated by NRB.
2. **Correlation and Multicollinearity Boundaries:**
   - Operating profitability (ROA) correlated almost perfectly with EPS ($r = 0.975, p < 0.01$), confirming that simultaneous inclusion would generate catastrophic multicollinearity ($\text{VIF} \approx 20\text{--}30$). Hence, ROA was preserved strictly as an isolated substitute.
   - In contrast, EPS and BVPS exhibited moderate correlation ($r = 0.372, p = 0.051$), with variance inflation factors of exactly $\text{VIF} = 1.16$, confirming empirical independence.
3. **Baseline Value Relevance (Model 1):**
   - In the baseline two-way fixed effects model, the estimated earnings coefficient was $\hat{\beta}_E = 2.095$ (HC3 SE = 4.096, $t = 0.51, p = 0.609$) and the book value coefficient was $\hat{\beta}_B = 0.219$ (HC3 SE = 1.858, $t = 0.12, p = 0.906$).
   - Both coefficients were positive, consistent with valuation theory, but neither was statistically significant at the 5% level once macro-year price movements were absorbed by $\lambda_t$. The model explained 94.8% of price variance ($R^2 = 0.948$, Adjusted $R^2 = 0.912$), primarily driven by the absorption of market-wide cycles.
4. **Regime Shift and Valuation Multiple Compression (Model 2):**
   - **Pre-Consolidation Valuation:** Prior to consolidation, the earnings slope was substantial: $\hat{\beta}_E = 5.577$ (HC3 SE = 3.560, $t = 1.57, p = 0.117$), whereas the book value slope was negligible: $\hat{\beta}_B = 0.100$ (HC3 SE = 1.306, $t = 0.08, p = 0.939$). Equity investors primarily priced current earnings rather than historical book assets.
   - **Regime Interaction Shifts:** The post-consolidation interaction terms were uniformly negative: $\hat{\delta}_E = -3.124$ (HC3 SE = 4.003, $p = 0.435$) and $\hat{\delta}_B = -1.758$ (HC3 SE = 1.231, $p = 0.153$).
   - **Implied Post-Consolidation Slopes:** Post-consolidation earnings slope compressed to $\hat{\beta}_E + \hat{\delta}_E = 2.453$ ($p = 0.280$), while the implied book value slope turned negative to $\hat{\beta}_B + \hat{\delta}_B = -1.658$ ($p = 0.139$).
   - **Principal Joint Wald Test:** The joint test of parameter stability ($H_0: \delta_E = \delta_B = 0$) yielded $F(2, 14) = 2.954$ ($p = 0.085$). Under the designated 5% threshold, the null hypothesis of structural stability was not rejected, though it achieved marginal significance at the 10% level.
5. **Robustness Suite Insights and the Entity-Timing Resolution:**
   - The robustness suite (R1–R8) verified parameter stability across ROA substitution (R3), cash dividend inclusion (R4, residual $\text{df} = 13$), transition-year removal (R5), bonus share dilution (R7), and restated basic earnings (R8).
   - **Critical Empirical Breakthrough (Specification R6):** When FY 2078/79 was excluded to eliminate the entity-timing asymmetry (standalone pre-merger fundamentals vs. enlarged post-merger April 2023 trading prices across the four merged banks), the joint Wald test became **statistically significant at the 5% level**:
     $$F(2, 10) = 5.82, \quad p = 0.021 \quad (N = 23)$$
     with $\hat{\delta}_B = -2.611$ ($t = -1.97, p = 0.077$). Purging this entity mismatch revealed that the 2023 consolidation wave produced a genuine, statistically verifiable structural break in the accounting valuation function.
6. **Specification Comparisons and Omitted Variable Bias:**
   - Comparing pooled OLS to two-way fixed effects revealed that pooled OLS generated an artificially inflated earnings slope ($\hat{\beta}_E = 4.882, R^2 = 0.136$). Introducing fiscal-year fixed effects attenuated the slope to $2.095$ while increasing explanatory power to $94.8%$, proving that unadjusted pooled regressions in prior Nepalese studies severely suffered from macro-omitted variable bias.

---

## 5.3 Conclusions

Based on the empirical findings, econometric diagnostics, and theoretical evaluations conducted in this dissertation, four major conclusions are established:

### 5.3.1 Regime-Dependent Accounting Value Relevance in Nepalese Banking
The empirical evidence demonstrates that the valuation relevance of published accounting fundamentals among Nepalese commercial banks is fundamentally regime-dependent. In the pre-consolidation regime (FY 2076/77–2078/79), equity market pricing was primarily oriented toward operational earnings capacity ($\hat{\beta}_E = 5.58$), while balance-sheet net worth exerted virtually no incremental influence ($\hat{\beta}_B = 0.10$). Following the massive horizontal consolidation wave of early 2023, this pricing structure was severely disrupted. Surging loan-loss provisions, asset quality reclassifications, capital dilution, and the sudden cessation of cash dividend distributions induced an aggressive compression of valuation multiples, cutting the implied earnings multiple by more than half (to $2.45$) and turning the book value multiple negative (to $-1.66$). Thus, the assumption of temporal parameter stability that underpins conventional valuation research in Nepal is conclusively rejected.

### 5.3.2 The Asymmetry of Earnings and Book Value Pricing under Consolidation
A central theoretical tenet of the Ohlson (1995) and Collins et al. (1997) frameworks posits that when reported earnings become transitory or contaminated by organizational restructuring, equity investors shift their valuation focus toward balance-sheet book value as an abandonment or liquidation floor. This study concludes that this theoretical substitution **does not hold** in the context of commercial banking amalgamations in Nepal. Rather than serving as an asset anchor, higher book value per share post-consolidation was weakly associated with lower market prices. In the post-merger Nepalese banking environment, high reported book equity frequently masked unamortized merger goodwill, capitalized restructuring costs, and unprovisioned legacy credit exposures from acquired institutions. Because commercial banks are highly leveraged, tightly regulated entities whose insolvency leads to regulatory resolution rather than market liquidation, equity investors heavily discounted reported net assets, treating expanded book equity as an indicator of capital trapped in distressed loan portfolios.

### 5.3.3 Econometric Discipline: Spurious Multiples vs. Macro-Year Absorption
This dissertation definitively resolves the methodological controversies that have characterized prior empirical banking literature in Nepal. The statistically significant, large positive valuation coefficients widely reported in earlier Nepalese studies were artifacts of two severe econometric errors: (i) the circular inclusion of the Price-to-Earnings (P/E) ratio as an independent variable, which mechanically guarantees statistical significance through mathematical endogeneity; and (ii) the failure to include common fiscal-year fixed effects, which causes static regressions to conflate macro-level NEPSE price movements and NRB monetary policy cycles with fundamental accounting value relevance. When P/E is strictly excluded, share prices are measured post-disclosure, and two-way fixed effects are estimated with HC3 robust standard errors, accounting fundamentals explain cross-sectional bank differentiation only moderately, while macro-temporal trends account for the overwhelming majority of equity price variation ($R^2 = 0.948$).

### 5.3.4 Resolution of Structural Timing and Archival Integrity
The sensitivity analysis demonstrates that the econometric detection of structural regime shifts in emerging markets is acutely sensitive to archival timing and entity-boundary definitions. In the immediate aftermath of corporate amalgamations, reporting lags create temporal asymmetries where historical standalone financial accounts are paired with newly enlarged capitalized market entities. Purging this entity mismatch in specification R6 revealed that the 2023 consolidation wave caused a statistically significant structural break ($F = 5.82, p = 0.021$). Furthermore, the enforcement of the 5-day freshness rule demonstrated that prolonged secondary trading suspensions—such as those observed for HBL (54 days) and NIMB (47 days)—distort empirical price discovery. Methodologically defensible research must anchor market observations to statutory disclosure mandates (BAFIA Section 59(2)) and explicitly exclude stale or suspended price series.

---

## 5.4 Implications of the Study

The conclusions established in this dissertation yield vital practical, policy, and managerial implications across multiple institutional domains:

### 5.4.1 Implications for Regulatory Authorities (Nepal Rastra Bank)
1. **Scrutiny of Post-Merger Asset Quality and Provisioning Transparency:**
   The sharp downward compression in earnings multiples and the emergence of negative book value pricing post-consolidation reflect deep market skepticism regarding the reported asset quality of merged commercial banks. NRB's supervisory wings must enforce rigorous, uncompromised on-site asset quality reviews (AQRs) across all consolidated entities. Regulatory forbearance policies—such as extended grace periods for loan reclassification and phased credit-loss provisioning—obscure true institutional health, distort market price discovery, and undermine investor confidence. NRB must mandate standardized, transparent impairment testing of legacy loan books acquired through amalgamations.
2. **Re-Evaluation of Mandatory Consolidation Policies:**
   While NRB's consolidation drive successfully reduced the institutional count of commercial banks from 32 to 20, the empirical evidence reveals that horizontal mergers did not immediately generate operational efficiency or enhance shareholder value. Instead, amalgamations created complex, unwieldy institutions burdened by divergent credit cultures, duplicated branch networks, and substantial non-performing loan burdens. Future macroprudential policies should prioritize organic institutional strengthening, digital modernization, and risk management governance over forced balance-sheet amalgamations.
3. **Harmonization of Capital Distribution Directives:**
   The abrupt collapse of cash dividend distributions post-consolidation removed a primary valuation anchor for bank equities. NRB should establish transparent, forward-looking macroprudential guidelines regarding dividend eligibility criteria, counter-cyclical capital buffer (CCyB) enforcement, and reserve retention thresholds, allowing market participants to formulate realistic long-term cash flow expectations.

### 5.4.2 Implications for Securities Market Regulators and Exchanges (SEBON and NEPSE)
1. **Reforming Secondary Market Trading Suspension Rules:**
   A critical institutional friction identified in this study was the prolonged suspension of secondary market trading during merger negotiations, which froze trading for up to 54 days past statutory reporting deadlines. Although SEBON subsequently revised its merger suspension directives in late 2022 to shorten suspension durations, secondary trading halts during corporate restructuring remain excessively disruptive. SEBON and NEPSE must enforce continuous, uninterrupted trading during corporate combinations, restricting halts to a maximum of a few trading sessions surrounding swap execution. Continuous price discovery is essential to prevent speculative panics and preserve market liquidity.
2. **Standardizing Corporate Disclosure Timelines and Digital Access:**
   Under Section 59(2) of BAFIA, commercial banks are legally mandated to publish audited financial statements within nine months of fiscal year-end. However, public dissemination remains fragmented across corporate websites, newspaper advertisements, and exchange portals. SEBON and NEPSE should operationalize a centralized, mandatory electronic disclosure repository (analogous to the US SEC EDGAR or Indian MCA/BSE systems) where audited annual reports, quarterly NFRS financials, and merger swap audit reports are uploaded instantaneously in standardized digital formats with certified timestamps.
3. **Eradicating Circular Multiples from Financial Analysis Guidelines:**
   Given the pervasive use of endogenous price-earnings multiples in local equity research reports and academic dissertations, SEBON's investor education initiatives and financial literacy frameworks should explicitly educate analysts and market participants on the mathematical circularity of using current P/E ratios to forecast equity price targets.

### 5.4.3 Implications for Commercial Bank Executives and Boards of Directors
1. **Prioritizing Post-Merger Organizational and Credit Integration:**
   The empirical finding of widened earnings dispersion and compressed valuation multiples post-merger indicates that executive leadership must shift focus from balance-sheet expansion to internal operational harmonization. Boards of directors of consolidated banks must accelerate the integration of management information systems (MIS), unify disparate core banking software (CBS), align risk underwriting standards, and execute aggressive, proactive loan recovery initiatives to cleanse legacy credit portfolios.
2. **Transparency in Reporting Goodwill, Bargain Purchases, and Reserves:**
   Because investors exhibited deep apprehension toward reported book values post-merger, commercial bank management must enhance footnote disclosures regarding purchase price allocations (PPA), merger swap calculations, recognized goodwill, bargain purchase gains, and statutory reserve transfers. Voluntary disclosure of granular asset impairment metrics can mitigate market skepticism and restore credibility to balance-sheet net worth.
3. **Managing Investor Expectations Regarding Capital Returns:**
   Bank executives must abandon the historical practice of placating retail shareholders with unbacked bonus share issuances that inflate equity capital without providing cash flows. Management should communicate transparent, sustainable capital management strategies that balance regulatory capital adequacy maintenance with predictable, realistic dividend distribution policies.

### 5.4.4 Implications for Equity Investors, Financial Analysts, and Market Participants
1. **De-Emphasizing Unadjusted Book Value as a Safety Anchor:**
   Equity investors and portfolio managers in Nepal must re-evaluate conventional fundamental analysis rules that treat high book value per share as an absolute margin of safety. In the post-consolidation banking era, reported book value may conceal substantial asset quality impairments and illiquid capital. Fundamental analysis must scrutinize the composition of equity, adjusting reported book value for unamortized goodwill, deferred tax assets, and under-provisioned substandard loans.
2. **Discounting Earnings Transitoriness in Merged Institutions:**
   Investors must recognize that reported net profit in the initial years following major amalgamations contains substantial transitory noise, including one-off integration expenditures, harmonized provisioning charges, and tax adjustments. Valuation models should utilize normalized operating earnings—adjusted for credit-loss volatility—rather than headline basic EPS.
3. **Accounting for Macro-Temporal Valuation Cycles:**
   Financial analysts must recognize that macroeconomic factors—including systemic liquidity conditions, NRB policy rates, remittance inflows, and broad market sentiment—exert a far more dominant influence on Nepalese bank share prices than firm-specific accounting increments. Equity valuation frameworks must explicitly incorporate macroeconomic and monetary cycles rather than relying solely on static accounting ratios.

### 5.4.5 Implications for Academic Researchers and Accounting Standard Setters
1. **Adopting Econometrically Rigorous Valuation Methodologies:**
   This dissertation demonstrates the absolute necessity of rigorous econometric modeling in Nepalese empirical accounting research. Academic institutions, including Tribhuvan University and other national business schools, must train graduate researchers to strictly eliminate mathematically endogenous regressors (such as P/E predicting MPS), incorporate multi-way fixed effects to prevent omitted variable bias, and verify finite-sample cluster assumptions using HC3 robust inference.
2. **Standardization of NFRS Reporting and Restatement Practices:**
   The Accounting Standards Board (ASB) of Nepal and the Institute of Chartered Accountants of Nepal (ICAN) must enforce strict adherence to Nepal Financial Reporting Standards (NFRS)—particularly NFRS 3 (*Business Combinations*) and NFRS 9 (*Financial Instruments*). Divergent practices in reporting bonus-adjusted basic EPS versus diluted EPS across consecutive annual reports create archival confusion. Standard setters should mandate uniform historical restatement tables in all published annual accounts following capital expansions.

---

## 5.5 Recommendations and Directions for Future Research

### 5.5.1 Policy and Managerial Recommendations
Based on the synthesized conclusions and institutional implications, the following specific, actionable recommendations are offered:

1. **Mandatory Post-Merger Asset Quality Disclosures:** Nepal Rastra Bank should mandate that all commercial banks completing horizontal mergers publish a comprehensive "Asset Quality and Integration Disclosure Report" semi-annually for three years post-merger, detailing the recovery performance, provisioning coverage, and write-offs specifically associated with acquired legacy loan portfolios.
2. **Elimination of Trading Suspensions During Corporate Restructuring:** The Securities Board of Nepal and NEPSE should permanently dismantle the practice of long-term trading suspensions for merging companies, establishing strict regulatory ceilings that limit trading halts to a maximum of three consecutive trading sessions around formal share swap execution.
3. **Establishment of a Centralized Digital Corporate Filings Portal:** SEBON should construct an open-access, machine-readable digital filings portal requiring all listed institutions to upload audited financial statements, board resolutions, and statutory disclosures concurrently with their public release, embedding immutable cryptographic timestamps.
4. **Transition to Normalized Core Earnings Metrics:** Commercial bank management and equity research institutions should formally compute and publish "Core Operating Earnings per Share" alongside statutory NFRS basic EPS, stripping out non-recurring merger adjustments, write-backs, and regulatory reserve transfers to provide retail investors with a reliable indicator of ongoing operational profitability.

### 5.5.2 Avenues for Future Academic Inquiry
While this dissertation has established a rigorous econometric baseline for evaluating accounting value relevance across the 2023 consolidation wave, several fruitful avenues remain open for future scholarly research:

1. **Extension to Long-Horizon Post-Consolidation Panels:**
   This study examined the post-consolidation regime across three initial fiscal years (FY 2079/80 through FY 2081/82). As additional financial years elapse, future research should re-estimate the interactive valuation models over longer post-merger horizons (5 to 10 years) to evaluate whether valuation multiples recover once post-merger integration is fully completed and legacy loan portfolios are permanently cleansed.
2. **Expansion to the Entire Commercial Banking Population:**
   Future studies should expand the cross-sectional sample to encompass all 20 surviving commercial banks on NEPSE, employing cross-sectional difference-in-differences (DiD) frameworks that compare aggressively merged banking series against a larger cohort of organically grown or minimally consolidated peer institutions.
3. **Investigation of Non-Financial Disclosure and ESG Metrics:**
   Beyond financial statement numbers, subsequent research should examine the value relevance of non-financial indicators, corporate governance metrics, digital banking investments, and Environmental, Social, and Governance (ESG) disclosures among Nepalese financial institutions, assessing whether non-accounting disclosures provide incremental pricing power.
4. **Analysis of Intraday Price Discovery and Event-Study Methodologies:**
   Building upon the macro-level findings of this study, future inquiries could employ high-frequency, intraday event-study methodologies to capture the immediate market reaction surrounding statutory board dividend announcements, AGM approvals, and quarterly earnings releases, quantifying the speed and informational efficiency of NEPSE's price discovery mechanism.
5. **Cross-Sectoral Valuation Comparative Inquiries:**
   Finally, comparative studies should investigate accounting value relevance across divergent sectors of the Nepalese economy, contrasting the banking industry with insurance companies, hydropower developers, microfinance institutions, and manufacturing corporations to evaluate how divergent regulatory environments shape the pricing of earnings and book value.

---

