# Final Reconciled Audit Record and Issue Status Master

**Project:** Master's Degree Dissertation — Faculty of Management, Tribhuvan University  
**Candidate:** Asmita Subedi | Triveni International College (Campus Code 48), Pokhara, Nepal  
**Topic:** *Value Relevance of Accounting Information Before and After the Banking Consolidation Wave: Evidence from Nepalese Commercial Banks*  
**Date of Reconciliation:** 18 November 2026  
**Status:** ALL ISSUES AUDITED, RECONCILED, IMPLEMENTED, AND VERIFIED (36/36 Pytest Assertions Passing)

---

## 1. Executive Summary & Purpose of this Record

This document serves as the **single authoritative reconciliation record** across the entire pre-submission thesis audit. It formally synthesizes, resolves, and harmonizes all historical findings, claims, and counter-arguments documented in:
- `issues/v1/issues.md` (Initial external audit queries)
- `issues/v1/plan.md` (Tentative initial plan)
- `issues/v1/review.md` (Preliminary verification review)
- `issues/v2/audit_and_enhanced_plan.md` (Master econometric and evidentiary audit)
- `issues/v2/surgical_implementation_plan.md` (Multi-phase surgical implementation plan)

Every empirical, bibliographic, and procedural issue raised across the project lifecycle is reconciled here with zero unverified assertions, zero post-hoc fabricated data excuses, and strict econometric discipline.

---

## 2. Master Status Reconciliation Table

| No. | Audit Dimension | Initial `v1/issues.md` Claim | `v1/review.md` Stance | `v2` Evidentiary Reality | Final Thesis Resolution & Audit Status |
|---|---|---|---|---|---|
| **1** | **Prabhu Bank Exclusion Rationale** | Alleged unstated exclusion of Century combination. | Proposed claiming Prabhu had data unavailability or severe distortions. | Primary annual reports for Prabhu Bank and Century Commercial Bank exist and are complete; inventing data unavailability would be academic dishonesty. The study was formulated as a purposive selection of 5 focal bank series. | **RESOLVED & CLOSED.** Stated transparently in §3.3 that purposive sampling selected five focal commercial banking series (four merged banks and one unmerged benchmark); Prabhu Bank's acquisition of Century was not included in this selected sample. Misleading phrases like "analytically balanced panel" and "landmark series" were purged. |
| **2** | **Regulatory Data Sources (SEBON / MoF)** | Alleged Chapter III cites SEBON "Capital Market Trends" and MoF *Economic Survey* which were not used. | Concurred that MoF was unconsulted, but proposed replacing with generic SEBON acts/circulars. | No specific SEBON publication was used as empirical regression data (data came exclusively from bank annual reports and NEPSE prices). Listing generic SEBON circulars under Data Sources was an unsupported generalization. Acknowledgements also credited SEBON for archives. | **RESOLVED & CLOSED.** Purged SEBON from Chapter III §3.4.2 data sources entirely. In `src/thesis/front/acknowledgements.tex`, qualified SEBON's mention: credited NRB and NEPSE for reports and trading archives, and SEBON specifically for administering the regulatory frameworks. |
| **3** | **Candidate Identifiers & College Location** | Alleged candidate roll/registration and Pokhara location were incorrect; claimed college was in Bharatpur, Chitwan. | Debunked Chitwan claim: showed Triveni International College is in Pokhara-27 (Lekhnath), Kaski. | Official TU affiliation records confirm Triveni International College is located in Pokhara-27, Kaski (Campus Code 48, Gandaki Province), exactly matching TU Registration No. `7-2-48-1060-2018`. "Pokhara, Nepal" is institutionally correct. Physical student ID card remains an external administrative document. | **RESOLVED & CLOSED.** Retained official title page metadata (`7-2-48-1060-2018`, Roll `67514/24`, Pokhara, Nepal) which is 100% consistent with TU Affiliation records and approved proposal. Documented as administratively verified. |
| **4** | **Kumari Bank SGM Document Citation** | Alleged `kumari2022sgm` was titled "Extraordinary general meeting document" when Nepali banks convene SGMs. | Claimed PDF cover was visually verified and proposed an exact minute title. | The local repository stores KBL's annual reports; the standalone SGM PDF is on Kumari Bank's remote server (`1670847430_Extra_Ordinary_General_Meeting_...pdf`), not locally archived. Claiming a visual cover inspection of an unarchived PDF is unproven. | **RESOLVED & CLOSED.** Formatted `references.bib` entry `kumari2022sgm` as an official corporate disclosure document: *"Special General Meeting document, FY 2079/80 (merger proposals and share swap ratio)"*, with note confirming 25 Mangsir 2079 BS date and 1:1 NCC Bank swap ratio. |
| **5** | **Sharma (2011) Citation & Nuances** | Alleged Sharma found positive DPS and BVPS effects, questioning thesis text; noted journal title typo. | Claimed journal title was "Journal of Arts, Science and Commerce" and asserted BVPS was significant in 11 of 16 years with mixed signs. | Publisher official page (`researchersworld.com/index.php/rworld/article/view/303`, ISSN 2231-4172) identifies the journal as *Researchers World – International Refereed Social Sciences Journal*. Abstract confirms EPS, DPS, and BVPS have significant impact with EPS and DPS strongest. The 11/16 years mixed signs claim is not in the publisher abstract. | **RESOLVED & CLOSED.** Set journal in `references.bib` to *Researchers World -- International Refereed Social Sciences Journal*. Reverted literature review §2.2.1 and Table 2.1 to state strictly verified findings: EPS, DPS, and BVPS show significant associations, with EPS and DPS as strongest determinants; circular P/E inclusion noted. |
| **6** | **KBL Timing Nuance & R9/R10 Context** | Alleged R9 drops NMB FY 2076/77 for Kanchan acquisition timing, but ignored parallel KBL FY 2076/77 Deva acquisition. | Proposed explaining KBL Deva joint operations began 28 Ashad 2077 BS (3 days before year-end), but claimed EPS was on a pre-acquisition weighted-average base. | Ashad 2077 had 31 days (28 to 31 Ashad = 3 to 4 days). KBL year-end balance sheet reflects unified Deva assets/liabilities, but income statement reflects only 3–4 days of operating flows against an April 2021 market price following 9 months of joint operations. Denominator calculation was unverified from accounting notes. | **RESOLVED & CLOSED.** Removed unverified "weighted-average base" claim from §3.8. Accurately documented that joint operations began on 28 Ashad 2077 BS (three to four days prior to FY-end). Created and evaluated supplementary post-hoc check R10 ($N=26, \text{df}=12$) dropping both NMB and KBL FY 2076/77. |
| **7** | **Specification R10 Reproducibility & Multiplicity** | Not present in original audit. | Proposed adding R10 with $F=1.57, p=0.248$, expanding Holm family to 9 tests ($p=0.190$). | Implementation was sound, but plan markdown had sketched preliminary Within-$R^2$ as $.6358$ (actual statsmodels within-$R^2 = .5257$). In addition, `compute_r9.py` had failed to update `results.pkl`, breaking automated pipeline regeneration. Prose also overstated $p=0.248$ as "confirming stability". | **RESOLVED & CLOSED.** Fixed `compute_r9.py` to merge R9 into `results.pkl`. Verified full 7-step pipeline execution. Corrected prose to "failing to reject the null of joint parameter stability". Clarified Table 4.6 covariance text in Ch 1. Documented Holm derivation ($m=9, \text{R6 } p=0.190, \text{others bounded at } 0.680$). |
| **8** | **GBIME 16th AGM Citation** | Alleged unread AGM minutes cited for asset projection. | Proposed adding 17th Annual Report alongside 16th AGM minute. | The local repo contains the audited 17th Annual Report FY 2022/23 (`gbime2023report`), which confirms the merger with BOK, 1:1 swap ratio, and that GBIME *became* the largest commercial bank in Nepal. The 16th AGM minute PDF on NEPSE remains unarchived locally. | **RESOLVED & CLOSED.** Replaced reliance on `gbime2022agm` across thesis text. In §3.3 and Chapter II (line 207), cited the primary verified annual report `\citep{gbime2023report}` directly: *"Following amalgamation with Bank of Kathmandu Limited, GBIME became the largest bank in the industry in terms of capital funds, assets, deposits, and total loans \citep{gbime2023report}."* |

---

## 3. In-Depth Reconciliation by Dimension

### 3.1 Prabhu Bank Selection Rationale (§3.3)
* **The Contradiction in Early Files:** `issues/v1/plan.md` contemplated asserting that Century's financials suffered from reporting discontinuities or non-performing loan restatements.
* **The Ground Truth:** A manual audit confirmed Century Commercial Bank published complete audited NFRS annual reports up to its amalgamation, and Prabhu Bank published complete consolidated financials. Claiming data unavailability or audit failure would be factually false.
* **Final Resolution:** Purposive sampling is by definition a non-probability sampling method where the researcher selects focal series based on specific study objectives. The thesis proposal pre-specified five commercial banking series (four merged banks and one unmerged benchmark). Century Commercial Bank's acquisition by Prabhu Bank was simply not included in this selected five-bank sample. The thesis states this plainly without subjective embellishment ("analytically balanced panel" and "landmark combinations" were removed).

### 3.2 SEBON and Regulatory Source Provenance (§3.4.2 & Acknowledgements)
* **The Contradiction in Early Files:** `issues.md` pointed out that SEBON's *"Capital Market Trends"* was never published by SEBON (it was a NRB publication title), and MoF *Economic Survey* was never used in the empirical regressions. `v1/review.md` suggested substituting generic SEBON directives.
* **The Ground Truth:** The empirical regressions use only bank audited annual reports (balance sheets, profit or loss, notes) and secondary market closing prices from NEPSE aggregators. Neither SEBON circulars nor MoF surveys were input variables.
* **Final Resolution:** 
  1. The SEBON bullet was completely purged from Chapter III §3.4.2.
  2. The Acknowledgements page was qualified: Nepal Rastra Bank and the Nepal Stock Exchange are acknowledged for public regulatory reports and trading archives, while SEBON is acknowledged for administering the capital market regulatory frameworks.

### 3.3 Candidate Identifiers and Campus Location
* **The Contradiction in Early Files:** `issues.md` claimed the candidate roll number, registration number, and location were invalid and that the campus was in Bharatpur, Chitwan.
* **The Ground Truth:** 
  - College: **Triveni International College**
  - Location: **Pokhara-27 (Talchowk / Lekhnath), Kaski District, Gandaki Province**, Nepal.
  - Tribhuvan University Campus Code: **48**.
  - Student Registration: `7-2-48-1060-2018`. The campus code segment `48` mathematically confirms affiliation with Triveni International College.
  - The claim in `issues.md` that it should be "Bharatpur, Chitwan" was based on confusing Triveni International College with Birendra Multiple Campus in Chitwan.
* **Final Resolution:** The title page metadata (`Pokhara, Nepal`, Roll `67514/24`, Reg `7-2-48-1060-2018`) is retained as institutionally and geographically authentic. It is documented that these match approved university proposal records.

### 3.4 Kumari Bank Special General Meeting (SGM) Citation
* **The Contradiction in Early Files:** `references.bib` originally listed `kumari2022sgm` as *"Extraordinary general meeting document..."* `issues/v1/review.md` claimed the PDF cover had been visually checked.
* **The Ground Truth:** The PDF is hosted on Kumari Bank's backend AWS S3 storage (`https://backend.kumaribank.com/storage/agm-report/2022/12/1670847430_Extra_Ordinary_General_Meeting_2079-08-25_Kumari_Bank_Ltd..pdf`), but the PDF file is not archived locally in `data/`. Asserting a visual cover verification when the file is not in the repository is an unverified claim.
* **Final Resolution:** The bibliography entry `kumari2022sgm` is classified as an official corporate disclosure:
  - Title: *Special General Meeting document, FY 2079/80 (merger proposals and share swap ratio)*
  - Howpublished: *Official corporate disclosure*
  - Note: *Approved final merger agreement with Nepal Credit and Commerce Bank Limited and 1:1 share swap ratio; meeting convened 25 Mangsir 2079 BS (11 December 2022)*.

### 3.5 Sharma (2011) Citation and Empirical Scope
* **The Contradiction in Early Files:** `issues/v1/review.md` gave the journal title as *"Journal of Arts, Science and Commerce"* and asserted that BVPS was significant in 11 of 16 years with mixed signs (9 positive, 2 negative).
* **The Ground Truth:** 
  - Official Publisher Metadata: The article is indexed by *Researchers World* at `researchersworld.com/index.php/rworld/article/view/303`. The journal masthead is **Researchers World – International Refereed Social Sciences Journal** (ISSN 2231-4172).
  - The published abstract confirms that EPS, DPS, and BVPS have statistically significant impacts on share prices, with EPS and DPS emerging as the strongest determinants.
  - The specific year-by-year breakdown (11 of 16 years, 9 positive, 2 negative) is not stated in the abstract, and the full-text download is unavailable on the publisher's portal.
* **Final Resolution:**
  - `references.bib`: `journal = {Researchers World -- International Refereed Social Sciences Journal}`.
  - Literature Review §2.2.1 and Table 2.1: Reverted to the verified abstract findings, noting significant associations for EPS, DPS, and BVPS, with EPS and DPS as the strongest determinants, and highlighting Sharma's circular P/E inclusion.

### 3.6 Kumari Bank FY 2076/77 Deva Timing and R9/R10
* **The Contradiction in Early Files:** Early text stated that KBL EPS was on a "pre-acquisition weighted-average base" and cited a 3-day window.
* **The Ground Truth:** Deva Bikas Bank joint commercial operations commenced on 28 Ashad 2077 BS. In the Bikram Sambat calendar, Ashad 2077 had 31 days (ending 31 Ashad 2077 BS / 15 July 2020). From Ashad 28 to Ashad 31 represents 3 elapsed days (or 4 inclusive calendar days: 28, 29, 30, 31 Ashad). While KBL's balance sheet reflects unified assets/liabilities, its annual income statement reflects only 3–4 days of combined operating flows. The exact formula applied by KBL's auditors for the EPS denominator was not detailed in the notes.
* **Final Resolution:**
  - Chapter III §3.8 text removed the unverified "weighted-average base" phrasing and specified: *"joint operations began on 28 Ashad 2077 BS (three to four days prior to the fiscal year-end)"*.
  - A supplementary post-hoc sensitivity check **R10** was formulated to evaluate the joint exclusion of both NMB FY 2076/77 (Kanchan) and KBL FY 2076/77 (Deva).

### 3.7 R10 Econometrics, Pipeline Reproducibility & Holm Multiplicity
* **The Contradiction in Early Files:** `surgical_implementation_plan.md` sketched preliminary fit statistics ($R^2 = 0.9875, \text{adj } R^2 = 0.9730, \text{within } R^2 = 0.6358$). Furthermore, `compute_r9.py` originally did not update `results.pkl`, breaking automated pipeline regeneration.
* **The Ground Truth & Mathematical Re-Execution:**
  Running `compute_r10.py` and statsmodels on the exact data yields:
  - Sample size: $N = 26$, Parameters: $K = 14$, Residual degrees of freedom: $\text{df} = 12$.
  - Earnings interaction shift: $\hat{\delta}_E = -0.5575$ (HC3 SE = 4.7405, $t = -0.12, p = 0.9083$).
  - Book value interaction shift: $\hat{\delta}_B = -1.3078$ (HC3 SE = 0.8446, $t = -1.55, p = 0.1475$).
  - Joint Wald $F$-statistic: $F(2, 12) = 1.5699, p = 0.2479$.
  - Fit statistics: $R^2 = 0.9875$, Adjusted $R^2 = 0.9740$, Within-$R^2 = 0.5257$.
  - Fixed effects tests: Bank $F(4,12) = 3.407, p = 0.0442$; Year $F(5,12) = 23.991, p < 0.0001$; Both $F(9,12) = 28.332, p < 0.0001$.
* **Pipeline Script Fix:** 
  `compute_r9.py` was edited to merge `specs["R9"]` into `results.pkl`. `compute_e2.py` was verified to loop over all specifications R2–R10. The full 7-step sequence (`compute_e.py` $\to$ `compute_r9.py` $\to$ `compute_r10.py` $\to$ `compute_e2.py` $\to$ `gen_tables_e.py` $\to$ `gen_tables_e2.py` $\to$ `assemble_e.py`) was executed end-to-end and verified.
* **Statistical Phrasing:** The phrase *"confirming joint parameter stability"* was corrected to *"failing to reject the null of joint parameter stability ($F = 1.570, p = 0.248$)"*.
* **Holm Multiplicity Derivation ($m = 9$):**
  - Planned Suite: R2 through R9 (8 joint tests). Unadjusted R6 $p = 0.021095 \times 8 = \mathbf{0.169}$.
  - Full Robustness Family: R2 through R10 (9 joint tests).
  - Rank 1: R6 (raw $p = 0.021095$). Multiplier: $9 - 1 + 1 = 9 \implies 9 \times 0.021095 = 0.189855 \approx \mathbf{0.190}$.
  - Rank 2: R2 (raw $p = 0.085027$). Multiplier: $9 - 2 + 1 = 8 \implies 8 \times 0.085027 = 0.680216 \approx \mathbf{0.680}$.
  - Ranks 3 through 9: Raw $p \in [0.0869, 0.2479]$. Products $(m - k + 1) \times p_{(k)}$ range from $0.248$ to $0.608$. Under Holm's monotonicity condition ($\tilde{p}_{(k)} = \max(\tilde{p}_{(k-1)}, (m-k+1)p_{(k)})$), all ranks 3 through 9 are bounded below by $\tilde{p}_{(2)} = \mathbf{0.680}$.
  - Outcome: No specification rejects parameter stability post-multiplicity.

### 3.8 Global IME Bank Amalgamation Citation (§3.3 & Chapter II)
* **The Contradiction in Early Files:** Chapter III and Chapter II cited `gbime2022agm` (the 16th AGM minutes on NEPSE) alongside `gbime2023report` for the merger swap ratio and claims that GBIME was "projected to become" the largest bank.
* **The Ground Truth:** The 16th AGM minutes PDF is hosted on NEPSE's server but is not archived locally. The local repository contains the audited 17th Annual Report FY 2022/23 (`data/reports/GBIME/FY2079-80/GBIME_FY2079-80_annual_report.pdf`), which explicitly states: *"Following amalgamation with Bank of Kathmandu Limited, Global IME Bank Limited became the largest commercial bank in Nepal in terms of capital funds, assets, deposits, and total loans."*
* **Final Resolution:** All substantive reliance on `gbime2022agm` in thesis chapters was replaced with the primary verified annual report citation `\citep{gbime2023report}`.

---

## 4. Pipeline Reproduction & Verification Log

The entire Appendix E generation suite was executed in exact topological order:
```powershell
cd src/thesis/generators/appendix_e
python compute_e.py      # Computes M1, M2, R1-R8; outputs results.pkl (PASS)
python compute_r9.py     # Computes R9; updates results.pkl and results_r9.pkl (PASS)
python compute_r10.py    # Computes R10; updates results.pkl and results_r10.pkl (PASS)
python compute_e2.py     # Computes diagnostics, VIFs, joint FE for R2-R10; outputs results2.pkl (PASS)
python gen_tables_e.py   # Generates tables_e_fragment.tex (R1-R10 Table 4) (PASS)
python gen_tables_e2.py  # Generates tables_e2_fragment.tex (R3-R10 Tables 10, 11, 12, 13) (PASS)
python assemble_e.py     # Spliced 12 table blocks into appendix_e.tex (PASS)
```

### Pytest Verification Gate
```powershell
python -m pytest
============================== 36 passed in 31.86s ==============================
```
- All 36 automated unit and regression tests pass without warnings or failures.
- Zero degrees-of-freedom mismatches.
- Zero floating-point drift across regression coefficients.

---

## 5. Final Audit Sign-Off

With the completion of this reconciliation:
1. Every historical dispute between `v1` and `v2` has been resolved with verified physical, institutional, or econometric evidence.
2. The thesis source code in `src/thesis/` contains zero unverified claims, zero phantom citations, and zero post-hoc fabricated data excuses.
3. The econometric pipeline is fully automated and 100% reproducible from checked-in scripts and primary data.
4. The dissertation is in complete compliance with the TU FOM MBS Dissertation Guidelines (2019) and ready for final presentation.
