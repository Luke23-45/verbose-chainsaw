# CHAPTER V: SUMMARY, CONCLUSION, AND IMPLICATIONS

## 5.1 Introduction

This concluding chapter synthesizes the theoretical arguments, empirical methodologies, econometric results, and interpretive discussions developed throughout this dissertation. The primary objective of this investigation has been to examine the value relevance of accounting information—specifically earnings per share (EPS) and book value per share (BVPS)—among prominent Nepalese commercial banks, and to evaluate whether the fundamental valuation relationships underwent a structural regime shift following the landmark commercial banking consolidation wave executed in early 2023 (mid-FY 2079/80).

In accordance with the Faculty of Management, Tribhuvan University *Master's Degree Dissertation Guidelines* (2019, p. 15), this chapter is organized into four core functional sections:
1. **Summary of the Study** (Section 5.2), providing an integrated overview of the research problem, operational objectives, theoretical foundation, research design, and major empirical results;
2. **Conclusions** (Section 5.3), articulating the insights and academic knowledge derived from the empirical findings regarding accounting value relevance, structural discontinuities, and capital market pricing behavior in Nepal;
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
2. Did the valuation associations of EPS and BVPS differ between the pre-consolidation period (FY 2076/77–2078/79) and the post-consolidation period (FY 2079/80–2081/82)?
3. How sensitive are the estimated valuation coefficients to transition-year effects, entity-timing mismatches, operating profitability substitutions, dividend exclusions, bonus share adjustments, and restated earnings?

Correspondingly, the study set out to: (i) evaluate the baseline value relevance of EPS and BVPS under a standardized post-reporting-deadline pricing framework; (ii) quantify structural shifts in valuation slopes across the 2023 consolidation wave using an interactive panel specification; and (iii) execute a comprehensive eight-part robustness suite to establish the empirical boundary conditions of accounting multiples in Nepal.

---

### 5.2.2 Methodology and Research Design Synthesis

To execute this investigation with rigorous econometric discipline, the study employed a longitudinal panel design spanning six fiscal years (FY 2076/77 through FY 2081/82, corresponding to 2019/20 through 2024/25). The target population encompassed all Class 'A' commercial banks listed on NEPSE. A purposive sample of five prominent commercial banking series was selected:
- Four amalgamated banking series representing the major corporate combinations of the early-2023 wave: Global IME Bank Limited (GBIME, absorbed Bank of Kathmandu), Himalayan Bank Limited (HBL, acquired Civil Bank), Kumari Bank Limited (KBL, absorbed NCC Bank), and Nepal Investment Mega Bank Limited (NIMB, amalgamation of Nepal Investment Bank and Mega Bank Nepal); and
- One benchmark banking series: NMB Bank Limited (NMB), which maintained continuous corporate operations throughout the 2023 wave without participating in horizontal combinations (note: NMB acquired Kanchan Development Bank Limited in August 2020, adding approximately NPR 0.57 billion to share capital in FY 2077/78, while its corporate identity remained continuous through the 2023 consolidation).

To eliminate look-ahead bias, market prices were observed at a standardized window immediately following the statutory annual financial reporting deadline. Section 59(2) of the Banks and Financial Institutions Act, 2017 (BAFIA) legally mandates that commercial banks publish their audited annual balance sheets and profit and loss accounts within nine months of fiscal year-end—operationalized at the end of Chaitra (mid-April) of the subsequent fiscal year. The dependent variable, $MPS^{RD}$, was defined as the closing market price on the first trading session following this statutory threshold, subject to a strict 5-day freshness rule.

Under this 5-day rule, 28 clean bank-year observations were realized out of an intended balanced panel of 30 bank-years (13 pre-consolidation and 15 post-consolidation observations). Two observations were excluded and dropped rather than imputed: HBL FY 2077/78 (trading resumed 54 days late on 6 June 2022) and NIMB FY 2077/78 (trading resumed 47 days late on 30 May 2022), both resulting from prolonged secondary market trading suspensions during merger processes around the April 2022 deadline.

Econometric estimation was structured around two core models:
1. **Model 1 (Baseline Value Relevance):** Specified as a two-way fixed effects panel regression:
   $$MPS^{RD}_{it} = \alpha + \mu_i + \lambda_t + \beta_E \text{EPS}_{it} + \beta_B \text{BVPS}_{it} + \varepsilon_{it}$$
   where $\mu_i$ captures unobserved bank fixed effects (with GBIME as reference) and $\lambda_t$ absorbs common fiscal-year macroeconomic shocks and NEPSE-wide price cycles (with FY 2076/77 as reference). Residual degrees of freedom were exact: $28 - 12 = 16$.
2. **Model 2 (Regime Shift Interaction):** Specified to estimate structural changes across the early-2023 consolidation wave:
   $$MPS^{RD}_{it} = \alpha + \mu_i + \lambda_t + \beta_E \text{EPS}_{it} + \beta_B \text{BVPS}_{it} + \delta_E (\text{EPS}_{it} \times Post_t) + \delta_B (\text{BVPS}_{it} \times Post_t) + \varepsilon_{it}$$
   where $Post_t = 1$ for post-consolidation years (FY 2079/80–2081/82) and 0 for pre-consolidation years (FY 2076/77–2078/79). The main effect of $Post_t$ was fully absorbed by the fiscal-year fixed effects ($\lambda_t$). Residual degrees of freedom were exact: $28 - 14 = 14$.

To safeguard against small-cluster downward bias ($G = 5$), all inferential statistical tests ($t$-tests, confidence intervals, and the principal joint Wald $F$-test of $H_0: \delta_E = \delta_B = 0$) were conducted using the MacKinnon-White (1985) HC3 heteroskedasticity-consistent covariance estimator evaluated on Student's $t$ residual degrees of freedom.

---

### 5.2.3 Summary of Major Empirical Findings

The empirical analysis yielded several substantive findings regarding the statistical properties, baseline relevance, regime stability, and sensitivity of accounting fundamentals:

1. **Descriptive Shifts Across Regimes:**
   - **Market Price Collapse:** Full sample mean $MPS^{RD}$ stood at NPR 254.34. Across regimes, mean share price dropped by 33.80% from NPR 310.59 pre-consolidation to NPR 205.60 post-consolidation, while cross-sectional standard deviation contracted by 72.00% (from 119.46 to 33.45), documenting an aggressive market-wide price compression.
   - **Earnings Deterioration & Dispersion:** Mean EPS contracted by 40.11% from NPR 17.90 pre-consolidation to NPR 10.72 post-consolidation. Concurrently, earnings dispersion widened by 63.66% (SD increased from 3.99 to 6.53), reflecting asset quality friction and credit-loss provisioning volatility among consolidated entities.
   - **Dividend Reduction:** Cash dividends per share (DPS) experienced a severe collapse of 76.90% (from NPR 6.06 to NPR 1.40), with 12 out of 15 post-consolidation bank-years recording exactly zero cash dividends, coinciding with post-merger capital retention and provisioning pressures.
   - **Book Value Stability:** Mean BVPS remained anchored across regimes, rising modestly by 2.44% from NPR 158.11 to NPR 161.97, reflecting statutory reserve retention mandated by NRB.
2. **Correlation and Multicollinearity Boundaries:**
   - Operating profitability (ROA) correlated almost perfectly with EPS ($r = 0.975, p < 0.01$), confirming that simultaneous inclusion would generate catastrophic multicollinearity ($\text{VIF} \approx 20\text{--}30$). Hence, ROA was preserved strictly as an isolated substitute.
   - In contrast, EPS and BVPS exhibited moderate correlation ($r = 0.372, p = 0.051$), with variance inflation factors of exactly $\text{VIF} = 1.16$, confirming that multicollinearity between EPS and BVPS is negligible.
3. **Baseline Value Relevance (Model 1):**
   - In the baseline two-way fixed effects model, the estimated earnings coefficient was $\hat{\beta}_E = 2.095$ (HC3 SE = 4.096, $t = 0.51, p = 0.616$ on $t(16)$) and the book value coefficient was $\hat{\beta}_B = 0.219$ (HC3 SE = 1.858, $t = 0.12, p = 0.908$ on $t(16)$).
   - Both coefficients were positive, consistent with valuation theory, but neither was statistically significant at the 5% level once macro-year price movements were absorbed by $\lambda_t$. The model yielded $R^2 = 0.948$ (Adjusted $R^2 = 0.912$); the sharp increase from $R^2 = 0.136$ in pooled OLS illustrates how much price variation common fiscal-year effects absorb.
4. **Regime Shift and Valuation Multiple Compression (Model 2):**
   - **Pre-Consolidation Valuation:** Prior to consolidation, the earnings slope was substantial: $\hat{\beta}_E = 5.577$ (HC3 SE = 3.560, $t = 1.57, p = 0.140$ on $t(14)$), whereas the book value slope was negligible: $\hat{\beta}_B = 0.100$ (HC3 SE = 1.306, $t = 0.08, p = 0.940$ on $t(14)$). Equity investors primarily priced current earnings rather than historical book assets.
   - **Regime Interaction Shifts:** The post-consolidation interaction terms were negative: $\hat{\delta}_E = -3.124$ (HC3 SE = 4.003, $t = -0.78, p = 0.448$) and $\hat{\delta}_B = -1.758$ (HC3 SE = 1.231, $t = -1.43, p = 0.175$).
   - **Implied Post-Consolidation Slopes:** Post-consolidation earnings slope compressed to $\hat{\beta}_E + \hat{\delta}_E = 2.453$ ($t = 1.08, p = 0.298$), while the implied book value slope turned negative to $\hat{\beta}_B + \hat{\delta}_B = -1.658$ ($t = -1.48, p = 0.161$).
   - **Principal Joint Wald Test:** The joint test of parameter stability ($H_0: \delta_E = \delta_B = 0$) yielded $F(2, 14) = 2.954$ ($p = 0.085$). Under the designated 5% threshold, the baseline model does not reject parameter stability, though it achieves marginal significance at the 10% level.
5. **Robustness Suite Insights and the Entity-Timing Sensitivity:**
   - The robustness suite (R1–R8) verified parameter stability across ROA substitution (R3), cash dividend inclusion (R4, residual $\text{df} = 13$), transition-year removal (R5), bonus share dilution (R7), and restated basic earnings (R8).
   - **Entity-Timing Sensitivity (Specification R6):** When FY 2078/79 was excluded to eliminate the entity-timing asymmetry (standalone pre-merger fundamentals vs. post-merger April 2023 trading prices across the four merged banks), the joint Wald test became **statistically significant at the 5% level**:
     $$F(2, 10) = 5.82, \quad p = 0.021 \quad (N = 23)$$
     with $\hat{\delta}_B = -2.611$ (HC3 SE = 1.517, $t = -1.72, p = 0.116$ on $t(10)$). While the individual interaction coefficient is not significant at 10% under Student's $t(10)$, the joint test indicates that excluding the transition mismatch reveals a statistically significant joint structural difference across the calendar regimes.
6. **Specification Comparisons and Omitted Variable Bias:**
   - Comparing pooled OLS to two-way fixed effects revealed that pooled OLS yielded an inflated earnings slope ($\hat{\beta}_E = 4.882, R^2 = 0.136$). Introducing fiscal-year fixed effects attenuated the slope to $2.095$ while increasing explanatory power to $94.8\%$, illustrating how unadjusted pooled models can absorb macro-temporal cycles. Notably, even in the pooled specification, HC3 robust inference yielded an insignificant slope ($t = 1.58, p = 0.126$).

---

## 5.3 Conclusions

Based on the empirical findings, econometric diagnostics, and theoretical evaluations conducted in this dissertation, four major conclusions are established:

### 5.3.1 Regime Differences in Accounting Valuation Multiples
The empirical evidence indicates that the valuation associations of accounting fundamentals among Nepalese commercial banks exhibited noticeable differences between the pre- and post-consolidation periods. In the pre-consolidation regime (FY 2076/77–2078/79), equity market pricing was primarily oriented toward operational earnings capacity ($\hat{\beta}_E = 5.58$), while balance-sheet net worth exerted virtually no incremental influence ($\hat{\beta}_B = 0.10$). In the post-consolidation period (FY 2079/80–2081/82), valuation multiples on earnings compressed (implied slope $2.45$) and book value multiples became negative (implied slope $-1.66$). In the baseline model, the joint test does not reject structural stability at the 5% level ($F = 2.954, p = 0.085$). However, after excluding the entity-mismatch fiscal year (Specification R6), the joint test rejects parameter stability at the 5% level ($F = 5.82, p = 0.021$). The evidence for a regime shift is therefore sensitivity-dependent rather than conclusive in the baseline; it is documented as an empirical association across calendar periods, rather than as an established causal merger impact.

### 5.3.2 Behavior of Book Value and Earnings Multiples Across Regimes
Under classical valuation theory (e.g., Ohlson, 1995; Collins et al., 1997), when reported earnings become transitory or disrupted by corporate restructuring, equity investors are expected to shift their valuation focus toward balance-sheet book value as an abandonment or liquidation floor. This theoretical substitution was **not observed** in this sample of Nepalese commercial banks. Rather than acting as a valuation anchor, the post-consolidation point estimate for book value per share turned negative ($\hat{\beta}_B + \hat{\delta}_B = -1.658$, though statistically insignificant at $p = 0.161$). A plausible economic interpretation is that in the post-merger banking environment, expanded book equity can reflect capital issued to absorb distressed assets, unamortized restructuring costs, or regulatory reserve transfers, rather than unencumbered liquidation value. Because commercial banks are highly leveraged institutions subject to regulatory resolution rather than orderly liquidation, market participants did not treat expanded book equity as an uncompromised asset anchor.

### 5.3.3 Econometric Discipline: Specification Sensitivity and Macro-Year Variation
This dissertation highlights the crucial role of econometric specification in evaluating accounting value relevance in frontier markets. In this sample, pooled estimation yields a larger earnings slope estimate ($\hat{\beta}_E = 4.882$) than two-way fixed effects ($\hat{\beta}_E = 2.095$), while explaining far less variance ($R^2 = 0.136$ versus $0.948$), illustrating how omitted macro-year variation can inflate accounting slope estimates. When fiscal-year fixed effects absorb common market-wide price levels, slope coefficients are identified strictly from within-year cross-sectional differentiation. Furthermore, studies that included the Price-to-Earnings (P/E) ratio as an explanatory regressor face severe mechanical endogeneity, as P/E directly embeds the dependent variable ($MPS$) in its numerator. When P/E is strictly excluded, prices are measured post-disclosure, and two-way fixed effects are estimated with HC3 robust standard errors, accounting fundamentals explain cross-sectional bank differentiation with substantial uncertainty, while macro-temporal trends account for the large majority of price variation.

### 5.3.4 Archival Timing and Data Integrity in Frontier Market Research
The sensitivity analysis demonstrates that the econometric evaluation of corporate restructuring in frontier markets is acutely sensitive to archival timing and entity-boundary definitions. In the immediate aftermath of amalgamations, reporting lags create temporal asymmetries where historical standalone financial accounts are paired with newly enlarged capitalized market entities. Purging this entity mismatch in specification R6 yielded a statistically significant joint test ($F = 5.82, p = 0.021$). Furthermore, enforcing the 5-day freshness rule demonstrated that prolonged secondary trading suspensions—such as those observed for HBL (54 days) and NIMB (47 days)—preclude reliable price observation. Methodologically defensible research must anchor market observations to statutory disclosure mandates (BAFIA Section 59(2)) and explicitly exclude stale or suspended price series.

---

## 5.4 Implications of the Study

The findings and methodological insights of this dissertation offer targeted implications across multiple institutional domains:

### 5.4.1 Implications for Regulatory Authorities (Nepal Rastra Bank)
1. **Scrutiny of Post-Merger Asset Quality and Provisioning Transparency:**
   The observed downward compression in earnings multiples and the lack of a positive book value pricing anchor post-consolidation coincide with market caution regarding the asset quality of merged commercial banks. NRB's supervisory departments should prioritize rigorous on-site asset quality reviews (AQRs) across consolidated entities. Standardized, transparent impairment testing of loan books assimilated during amalgamations is essential to restore market confidence in reported financial accounts.
2. **Evaluation of Mandatory Consolidation Policies:**
   While consolidation mandates reduced the universal population of commercial banks from 32 to 20, the empirical evidence indicates that horizontal amalgamations were accompanied by substantial earnings transitoriness and valuation compression. Policy frameworks should consider that structural combinations do not automatically translate into improved financial stability or higher equity valuations in the short to medium term.
3. **Transparency in Capital Distribution Directives:**
   The sharp reduction in cash dividend distributions post-consolidation removed a historical valuation anchor for bank equities. NRB should provide clear, forward-looking guidelines regarding dividend distribution criteria and counter-cyclical capital buffer expectations, helping market participants formulate realistic cash flow projections.

### 5.4.2 Implications for Securities Market Regulators and Exchanges (SEBON and NEPSE)
1. **Reforming Secondary Market Trading Suspension Practices:**
   A critical institutional friction identified in this study was the extended suspension of secondary market trading during merger processes, which froze trading for up to 54 days past statutory reporting deadlines. SEBON and NEPSE should enforce trading continuity during corporate combinations, restricting trading halts to a minimum of a few sessions around share swap execution. Continuous price discovery is vital to maintain liquidity and avoid information distortion.
2. **Standardizing Corporate Disclosure Timelines and Digital Access:**
   Under Section 59(2) of BAFIA, commercial banks are legally mandated to publish audited financial statements within nine months of fiscal year-end. However, public dissemination remains dispersed across corporate websites and print media. SEBON and NEPSE should operationalize a centralized electronic disclosure portal where audited annual reports, quarterly NFRS financials, and merger swap audit reports are uploaded instantaneously with certified timestamps.
3. **Discouraging Endogenous Ratios in Equity Research:**
   Given the historical use of endogenous price-earnings multiples in local equity research and academic literature, regulatory education frameworks should promote sound financial modeling practices that avoid regressing share price on price-derived ratios.

### 5.4.3 Implications for Commercial Bank Executives and Boards of Directors
1. **Prioritizing Post-Merger Operational and Credit Integration:**
   The observed earnings dispersion post-consolidation highlights the necessity for executive leadership to focus on internal operational harmonization. Boards of directors of consolidated banks should expedite the integration of management information systems, unify core banking software, and align credit underwriting standards to address legacy loan portfolios.
2. **Transparent Disclosure of Restructuring Adjustments:**
   Because market participants discounted book equity post-consolidation, commercial bank management should enhance voluntary footnote disclosures regarding purchase price allocations, recognized goodwill, restructuring provisions, and reserve transfers. Granular disclosures regarding asset quality can help alleviate investor skepticism.
3. **Communication of Sustainable Capital Policies:**
   Bank executives should pursue sustainable capital management strategies that balance regulatory capital adequacy maintenance with transparent, predictable dividend distribution policies.

### 5.4.4 Implications for Equity Investors, Financial Analysts, and Market Participants
1. **Scrutinizing Book Value Composition:**
   Equity investors and analysts in Nepal should exercise caution when using unadjusted book value per share as a safety metric for consolidated banks. In the post-merger banking era, reported book equity may encompass capital issued against stressed assets or restructuring costs. Fundamental analysis should examine the underlying quality of net assets, adjusting for unamortized goodwill and loan provisioning levels.
2. **Recognizing Earnings Transitoriness in Merged Institutions:**
   Market participants should account for the fact that reported accounting earnings in the immediate years following major amalgamations can exhibit heightened transitoriness due to credit-loss charges and integration expenses. Valuation models should utilize normalized operational metrics rather than headline basic EPS.
3. **Incorporating Macro-Temporal Factors:**
   Financial analysts must recognize that macroeconomic cycles—including systemic liquidity, policy rates, and broad market sentiment—exert a dominant influence on bank share prices. Valuation frameworks should incorporate macro-temporal factors rather than relying solely on static accounting multiples.

### 5.4.5 Implications for Academic Researchers and Accounting Standard Setters
1. **Adopting Rigorous Panel Econometric Frameworks:**
   This dissertation demonstrates the importance of rigorous econometric modeling in Nepalese empirical accounting research. Graduate researchers and academic institutions should eliminate mathematically circular regressors (such as P/E predicting MPS), incorporate two-way fixed effects to control for unobserved bank and temporal heterogeneity, and employ robust inference methods such as HC3.
2. **Standardizing NFRS Restatement Disclosures:**
   The Accounting Standards Board (ASB) of Nepal and ICAN should enforce uniform reporting of bonus-adjusted basic EPS and diluted EPS across consecutive annual reports, ensuring transparent historical comparability following capital expansions.

---

## 5.5 Recommendations and Directions for Future Research

### 5.5.1 Policy and Managerial Recommendations
Based on the synthesized conclusions and institutional implications, the following specific recommendations are offered:

1. **Mandatory Post-Merger Asset Quality Disclosures:** Nepal Rastra Bank should mandate that commercial banks completing horizontal amalgamations publish a semi-annual "Asset Quality and Integration Disclosure Report" for three years post-merger, detailing the recovery performance, provisioning coverage, and write-offs associated with acquired legacy loan portfolios.
2. **Limiting Trading Suspensions During Corporate Restructuring:** The Securities Board of Nepal and NEPSE should establish regulatory ceilings that restrict secondary market trading halts during corporate combinations to a minimum number of consecutive trading sessions around formal share swap execution.
3. **Operationalizing a Centralized Digital Filings Repository:** SEBON should establish an open-access, machine-readable digital filings portal requiring all listed financial institutions to upload audited financial statements, board resolutions, and statutory disclosures concurrently with their public release.
4. **Publishing Core Operational Earnings Metrics:** Commercial bank management and equity research institutions should report normalized operating earnings per share alongside statutory NFRS basic EPS, distinguishing ongoing operational performance from non-recurring merger adjustments and regulatory reserve transfers.

### 5.5.2 Avenues for Future Academic Inquiry
While this dissertation has established an econometric baseline for evaluating accounting value relevance across the 2023 consolidation wave, several fruitful avenues remain open for future scholarly research:

1. **Extension to Long-Horizon Post-Consolidation Panels:**
   This study examined the post-consolidation regime across three initial fiscal years (FY 2079/80 through FY 2081/82). As additional financial years elapse, future research should re-estimate the interactive valuation models over longer post-merger horizons (5 to 10 years) to evaluate whether valuation multiples recover once integration is fully completed.
2. **Expansion to the Full Commercial Banking Population:**
   Future studies should expand the cross-sectional sample to encompass all 20 surviving commercial banks on NEPSE, employing cross-sectional difference-in-differences (DiD) frameworks that compare aggressively merged banking series against a larger cohort of organically grown or minimally consolidated peer institutions.
3. **Investigation of Non-Financial Disclosure and ESG Metrics:**
   Subsequent research should examine the value relevance of non-financial indicators, corporate governance metrics, digital banking investments, and Environmental, Social, and Governance (ESG) disclosures among Nepalese financial institutions, assessing whether non-accounting disclosures provide incremental pricing power.
4. **Intraday Event-Study Methodologies:**
   Building upon the panel findings of this study, future inquiries could employ high-frequency, intraday event-study methodologies to capture the immediate market reaction surrounding statutory board dividend announcements, AGM approvals, and quarterly earnings releases, quantifying the speed and informational efficiency of NEPSE's price discovery mechanism.
5. **Cross-Sectoral Valuation Comparative Inquiries:**
   Finally, comparative studies should investigate accounting value relevance across divergent sectors of the Nepalese economy, contrasting the commercial banking industry with insurance companies, hydropower developers, microfinance institutions, and manufacturing corporations to evaluate how divergent regulatory environments shape the pricing of earnings and book value.
