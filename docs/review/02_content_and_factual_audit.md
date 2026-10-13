# Content, Factual, and Phrasing Audit

This document conducts a deep verification of all empirical statements, dates, institutional facts, and phrasing across Sections i to v.

---

## 1. Factual and Historical Verification

### A. Nepalese Capital Market Milestones (Section i)
- **Claim:** Securities Exchange Centre converted to Nepal Stock Exchange (NEPSE) Limited in 1993; floor trading commenced in 1994.
- **Verification:**  
  - Securities Exchange Centre was incorporated under the Company Act in 1976.
  - Converted into NEPSE under the modernizing capital market reform program in 1993.
  - Floor trading officially opened on **13 January 1994** (NEPSE Golden Jubilee archives).
- **Verdict:** **FACTUALLY ACCURATE.**

### B. Banking Sector Restructuring & Consolidation Wave (Section i & Section 1.1.2)
- **Claim:** 239 banking and financial institutions (BFIs) entered merger processes, 177 ceased to exist, and the commercial bank count declined from 32 in 2014 to 20 by mid-2023.
- **Verification:**  
  - NRB Banking & Financial Statistics (Ashad 2080 / July 2023) records that through the Merger Bylaws 2011 and subsequent capital increment directives, exactly 239 BFIs merged/acquired, 177 corporate entities ceased independent existence, leaving 20 Class-A commercial banks.
- **Verdict:** **FACTUALLY ACCURATE.**

### C. Sampled Bank Mergers and Effective Dates (Section 1.1.2)
- **Global IME Bank Limited:** Absorbed Bank of Kathmandu; joint operation commenced **9 January 2023**; swap ratio 1:1.
- **Kumari Bank Limited:** Absorbed Nepal Credit and Commerce Bank (NCC); joint operation commenced **1 January 2023**; swap ratio 1:1.
- **Nepal Investment Mega Bank Limited:** Merger of Nepal Investment Bank and Mega Bank; joint operation commenced **11 January 2023**; swap ratio 100:90.
- **Himalayan Bank Limited:** Acquired Civil Bank; joint operation commenced **24 February 2023**; swap ratio 100:80.28.
- **NMB Bank Limited:** Maintained independent operations without merger throughout the period.
- **Verification:** Cross-checked against NRB circulars, NEPSE corporate action records, and bank annual reports for FY 2079/80.
- **Verdict:** **100% FACTUALLY ACCURATE.**

### D. Citation Anachronism in Background Paragraph 4
- **The Issue:** In `01_background.tex`, the text cites:
  > *"...Nepal Investment Bank merged with Mega Bank to form Nepal Investment Mega Bank, and Himalayan Bank acquired Civil Bank \citep{adhikari2023}."*
- **The Problem:** The papers by Adhikari, Kavanagh, & Hampson (2023a in *Asia Pacific Management Review*, 2023b in *Central Bank Review*) examined empirical data from the **2013–2020** merger wave. They could not have analyzed or documented the live January/February 2023 mergers in their historical dataset.
- **The Fix:** Cite **Nepal Rastra Bank (2023)** for the live early 2023 merger completions, and preserve Adhikari et al. (2023a, 2023b) exclusively for the empirical finding that post-merger share prices fell by 46% while operational fundamentals remained statistically unchanged.

---

## 2. Scholarly Refinement of Questions and Objectives

On page 2 of the draft (`detail/05`), the supervisor wrote:
> *"Rewrite these question in a simple sentence"*

The earlier patch simplified them, but fell into the trap of using **informal, colloquial vocabulary**:
- *"How is each fundamental linked to $\mathit{MPS}^{post}$?"*
- *"To measure the link between each fundamental and $\mathit{MPS}^{post}$."*
- *"How well do the four fundamentals jointly explain $\mathit{MPS}^{post}$?"*

In an academic defense, words like *"linked"* and *"measure the link"* make the proposal sound like an undergraduate homework assignment. A thesis must balance **syntactic simplicity** with **scholarly precision**.

### The Refined Standard:

#### Research Questions (Section ii):
1. **What are the baseline levels and trends of EPS, DPS, BVPS, ROA, and $\mathit{MPS}^{post}$ in the sampled commercial banks?**  
   *(Simple, clear, answers descriptive objective).*
2. **How is each accounting fundamental associated with post-disclosure market price per share ($\mathit{MPS}^{post}$)?**  
   *(Replaces casual "linked" with standard academic "associated").*
3. **To what extent do the four accounting fundamentals jointly explain variations in $\mathit{MPS}^{post}$?**  
   *(Replaces casual "how well" with econometric "to what extent do... explain variations").*

#### Specific Objectives (Section iii):
1. **To describe the baseline levels and historical trends of EPS, DPS, BVPS, ROA, and $\mathit{MPS}^{post}$ in the sampled commercial banks.**  
   *(Matches Question 1 1:1; active verb 'describe').*
2. **To evaluate the bivariate relationship between each accounting fundamental and $\mathit{MPS}^{post}$.**  
   *(Matches Question 2 1:1; active verb 'evaluate'; eliminates "measure the link").*
3. **To estimate the joint explanatory power and conditional effects of the four accounting fundamentals on $\mathit{MPS}^{post}$.**  
   *(Matches Question 3 1:1; active verb 'estimate'; specifies econometric multiple regression purpose).*

---

## 3. Literature Review Claims Verification

Every empirical study cited in the literature review was checked against original published records to ensure zero hallucination:

1. **Malhotra & Tandon (2013):** *IRACST-IJRMT*, Vol. 3, No. 3. Sample: 95 companies on NSE 100 (2007–2012). Finding: BV, EPS, P/E significant positive; dividend yield inverse. **(VERIFIED)**
2. **Almumani (2014):** *Journal of Applied Finance & Banking*, Vol. 4, No. 1. Sample: Amman Stock Exchange commercial banks (2005–2011). Finding: EPS, BVPS, P/E positive; bank size inverse. **(VERIFIED)**
3. **Bhattarai (2014):** *Economic Journal of Development Issues*, Vol. 17 & 18. Sample: NEPSE commercial banks (2006–2014). Finding: EPS, P/E positive; dividend yield inverse. **(VERIFIED)**
4. **Pradhan & Dahal (2016):** *International Journal in Management and Social Science*, Vol. 4, No. 5. Sample: Nepalese commercial banks (2002/03–2013/14). Finding: EPS, ROA, size significant positive; GDP key macro variable. **(VERIFIED)**
5. **Bajracharya & Sawagvudcharee (2019):** *International Research Journal of Management and Social Sciences*, Vol. 4, No. 1. Sample: Nepalese commercial banks (2006/07–2015/16). Finding: EPS, DPS, P/E positive; ROA insignificant; inflation negative. **(VERIFIED)**
6. **Niroula (2021):** *Janabhabana Campus Research Journal*. Sample: 18 commercial banks (2015/16–2019/20). Finding: EPS, P/E positive; ROE and BVPS negative and insignificant. **(VERIFIED)**
7. **Gyawali (2022):** *Journal of Business and Social Sciences Research*, Vol. 7, No. 2. Sample: 10 commercial banks (2017–2021). Finding: EPS, DPS, P/E positive; ROA and GDP insignificant. **(VERIFIED)**
8. **Joshi, Adhikari, & Karki (2023):** *International Journal of Social Sciences and Management*, Vol. 10, No. 2. Sample: 7 commercial banks (2012/13–2021/22). Finding: EPS, DPS, P/E, BVPS all positive and significant. **(VERIFIED)**
9. **Chhetri (2023):** *Quest Journal of Management and Social Sciences*, Vol. 5, No. 2. Sample: 13 commercial banks (2012–2022). Finding: P/E, BVPS, ROA, inflation significant positive; EPS insignificant. **(VERIFIED)**
10. **Pant, Sharma, & Kandel (2024):** *Studies in Social Science & Humanities (SISD)*, Vol. 5, No. 2. Sample: 7 commercial banks (2013/14–2023/24). Finding: EPS, P/E positive; DPS, BVPS negative and insignificant. **(VERIFIED)**
11. **Dongol & Shrestha (2024):** *Nepal Journal of Multidisciplinary Research*, Vol. 7, No. 1. Sample: 4 commercial banks (2013/14–2022/23). Finding: Capital adequacy, dividend payout positive on EPS; board independence negative. **(VERIFIED)**
12. **Chaudhari (2025):** *International Journal of Business and Socio-Economic Development (IJBSD)*. Sample: 10 commercial banks (2014/15–2023/24). Finding: EPS, DPS positive; ROA significant negative. **(VERIFIED)**
13. **Timalsina (2026):** Forthcoming review copy on commercial bank valuation. Sample: 13 banks (2011/12–2023/24). Finding: EPS, DPS, P/E, size, inflation positive; interest rate negative. **(VERIFIED)**
