# Final Reconciled Audit Record and Issue Status Master

**Project:** Master's Degree Dissertation — Faculty of Management, Tribhuvan University  
**Proposal-listed candidate/institution:** Asmita Subedi | Triveni International College (Campus Code 48), Pokhara, Nepal
**Topic:** *Value Relevance of Accounting Information Before and After the Banking Consolidation Wave: Evidence from Nepalese Commercial Banks*  
**Date of Reconciliation:** 18 November 2026  
**Status:** Reconciliation record; status statements below distinguish implemented edits from claims still awaiting independent evidence.

---

## 1. Executive Summary & Purpose of this Record

This document records the current disposition of the pre-submission thesis audit and supersedes conflicting earlier recommendations where stated. Earlier files are retained as audit history; their unresolved or superseded claims should not be read as current status. This record does not treat tests or proposal consistency as verification of personal or institutional records. It synthesizes findings documented in:
- `issues/v1/issues.md` (Initial external audit queries)
- `issues/v1/plan.md` (Tentative initial plan)
- `issues/v1/review.md` (Preliminary verification review)
- `issues/v2/audit_and_enhanced_plan.md` (Master econometric and evidentiary audit)
- `issues/v2/surgical_implementation_plan.md` (Multi-phase surgical implementation plan)

The record distinguishes verified source claims, implemented prose changes, author-confirmed facts, and items still awaiting primary evidence.

---

## 2. Master Status Reconciliation Table

| No. | Audit Dimension | Initial `v1/issues.md` Claim | `v1/review.md` Stance | `v2` Evidentiary Reality | Final Thesis Resolution & Audit Status |
|---|---|---|---|---|---|
| **1** | **Prabhu Bank Exclusion Rationale** | Prabhu/Century is the fifth early-2023 consolidation combination but is not sampled. | Earlier plans proposed unsupported data-based explanations. | The author confirms no separate factual or data-based exclusion criterion is known or claimed. Online check confirms Prabhu's listed Class A status, 10 January 2023 joint-operation date, 1:1 ratio, and an official archive listing annual reports 19–24; not every report was checked for six-year comparability. The stated timing/listing criteria do not distinguish Prabhu. | **TRANSPARENTLY DISCLOSED; SELECTION RATIONALE REMAINS OPEN FOR SUPERVISOR DISPOSITION.** Chapters III and V name the omission and state that no separate data-based criterion is claimed. Do not invent a reason. The transparency fix does not itself establish why four of five merger combinations were selected. |
| **2** | **Regulatory Data Sources (SEBON / MoF)** | Alleged Chapter III cites SEBON "Capital Market Trends" and MoF *Economic Survey* which were not used. | Concurred that MoF was unconsulted, but proposed replacing with generic SEBON acts/circulars. | No specific SEBON publication was used as empirical regression data (data came exclusively from bank annual reports and NEPSE prices). Listing generic SEBON circulars under Data Sources was an unsupported generalization. Acknowledgements also credited SEBON for archives. | **RESOLVED & CLOSED.** Purged SEBON from Chapter III §3.4.2 data sources entirely. In `src/thesis/front/acknowledgements.tex`, qualified SEBON's mention: credited NRB and NEPSE for reports and trading archives, and SEBON specifically for administering the regulatory frameworks. |
| **3** | **Candidate Identifiers & College Location** | Alleged candidate roll/registration and Pokhara location were incorrect; claimed college was in Bharatpur, Chitwan. | Earlier review found the values consistent with the proposal; it did not verify the candidate's record. | The author confirms the title-page values match the proposal. No official college/TU record verifying the candidate-specific roll and registration numbers has been supplied. | **PROPOSAL CONSISTENCY CONFIRMED; OFFICIAL-RECORD VERIFICATION OPEN.** Leave the title-page values unchanged. Do not describe the roll or registration number as independently verified. |
| **4** | **Kumari Bank SGM Document Citation** | The exact wording on the PDF cover was disputed. | Earlier review records conflict on whether the cover was visually verified. | The meeting content, date, merger resolution, and 1:1 ratio are supported by the document review, but the exact cover wording is not verified in the current evidence set. | **CONTENT SUPPORTED; EXACT COVER WORDING UNVERIFIED.** The bibliography uses a descriptive title and explicitly notes that it is not a transcription of the cover. |
| **5** | **Sharma (2011) Citation & Nuances** | Earlier review questioned the reported DPS/BVPS findings and journal title. | Earlier records confused the journal's printed title with the publisher-site masthead and included an unsupported year-by-year sign claim. | The thesis bibliography uses *Journal of Arts, Science and Commerce* and author `Sharma, Sanjeet`. The local audit identifies the article's printed header as *Journal of Arts, Science & Commerce* (ISSN 2231-4172); another audit note gives the fuller indexed form as *Researchers World – Journal of Arts, Science and Commerce*. The publisher-site phrase *Researchers World – International Refereed Social Sciences Journal* is a site heading, not the article's journal title. The thesis summary is limited to the reported EPS/DPS/BVPS findings; the 11-of-16-year sign claim is omitted. | **JOURNAL FIELD RECONCILED; THESIS SUMMARY LIMITED.** Keep the concise printed title, *Journal of Arts, Science and Commerce*, in `references.bib`; the fuller indexed form is also consistent, but there is no reason to substitute the publisher-site masthead. The journal-name conflict is closed on the article-header/ISSN evidence recorded in the audit. Year-by-year findings remain unverified from a primary full text in the local files and are not claimed in the thesis. |
| **6** | **KBL Timing Nuance & R9/R10 Context** | Alleged R9 drops NMB FY 2076/77 for Kanchan acquisition timing, but ignored parallel KBL FY 2076/77 Deva acquisition. | Proposed explaining KBL Deva joint operations began 28 Ashad 2077 BS (3 days before year-end), but claimed EPS was on a pre-acquisition weighted-average base. | Ashad 2077 had 31 days (28 to 31 Ashad = 3 to 4 days). KBL year-end balance sheet reflects unified Deva assets/liabilities, but income statement reflects only 3–4 days of operating flows against an April 2021 market price following 9 months of joint operations. Denominator calculation was unverified from accounting notes. | **RESOLVED & CLOSED.** Removed unverified "weighted-average base" claim from §3.8. Accurately documented that joint operations began on 28 Ashad 2077 BS (three to four days prior to FY-end). Created and evaluated supplementary post-hoc check R10 ($N=26, \text{df}=12$) dropping both NMB and KBL FY 2076/77. |
| **7** | **Specification R10 Reproducibility & Multiplicity** | Not present in original audit. | Proposed adding R10 with $F=1.57, p=0.248$, expanding Holm family to 9 tests ($p=0.190$). | Implementation was sound, but plan markdown had sketched preliminary Within-$R^2$ as $.6358$ (actual statsmodels within-$R^2 = .5257$). In addition, `compute_r9.py` had failed to update `results.pkl`, breaking automated pipeline regeneration. Prose also overstated $p=0.248$ as "confirming stability". | **RESOLVED & CLOSED.** Fixed `compute_r9.py` to merge R9 into `results.pkl`. Verified full 7-step pipeline execution. Corrected prose to "failing to reject the null of joint parameter stability". Clarified Table 4.6 covariance text in Ch 1. Documented Holm derivation ($m=9, \text{R6 } p=0.190, \text{others bounded at } 0.680$). |
| **8** | **GBIME 16th AGM Citation** | Alleged unread AGM minutes cited for asset projection. | Proposed adding 17th Annual Report alongside 16th AGM minute. | Thesis chapters cite the audited 17th Annual Report (`gbime2023report`) for the merger ratio and the post-merger largest-bank statement. The 16th AGM minute PDF remains unarchived locally and was not verified. | **RESOLVED & CLOSED FOR THE THESIS.** Confirmed `gbime2022agm` is not cited in either thesis chapter; removed its unused entry from `src/thesis/references.bib`. The substantive thesis claims rely on `gbime2023report`, so retrieving the minutes is unnecessary for those claims. The separate proposal bibliography still contains its own `gbime2022agm` entry. |

---

## 3. In-Depth Reconciliation by Dimension

### 3.1 Prabhu Bank Selection Rationale (§3.3)
* **The Contradiction in Early Files:** `issues/v1/plan.md` contemplated asserting that Century's financials suffered from reporting discontinuities or non-performing loan restatements.
* **Author input:** The author confirms that no separate factual or data-based reason for omitting Prabhu/Century is known or claimed.
* **Online factual check (19 November 2026):** Prabhu's official 22nd Annual Report identifies it as a listed Class A commercial bank, states joint operations with Century began on 10 January 2023, and records a 1:1 swap ratio. The bank's investor-relations archive lists its 19th through 24th annual reports; the 19th is identified as FY 2076/77. This supports checking, but does not by itself prove, six-year comparability under the thesis's NFRS/data-availability criterion because every report was not inspected. [Prabhu Bank 22nd Annual Report](https://www.prabhubank.com/uploads/Financial%20Reports/Annual%20reports/22nd%20Annual%20Report%20%28Nepali%29-1.pdf); [Prabhu Bank investor-relations archive](https://www.prabhubank.com/investor-relation).
* **Methodological assessment:** The thesis's stated early-2023 timing and listing criteria do not distinguish Prabhu from the sampled merger combinations. Reporting guidance for observational studies calls for eligibility criteria and, for case-control designs, a rationale for case selection; purposive-sampling guidance likewise stresses reporting selection criteria and limiting claims from subjective samples to the sample. These are reporting principles, not a binding banking-thesis rule. [STROBE checklist](https://www.strobe-statement.org/fileadmin/Strobe/uploads/checklists/STROBE_checklist_v4_combined.pdf); [Stratton, “Purposeful Sampling: Advantages and Pitfalls”](https://www.cambridge.org/core/journals/prehospital-and-disaster-medicine/article/purposeful-sampling-advantages-and-pitfalls/7915F1727F04A3051245959ACBA61C06).
* **Current disposition:** Chapters III and V identify Prabhu/Century as omitted and explicitly state that no separate data-based exclusion criterion is claimed. This resolves the disclosure gap and avoids fabrication; it does not supply the missing selection rationale. Keep this as an open methodological item for supervisor disposition. Do not add a reason or re-estimate the sample unless a supervisor-approved design decision requires it.

### 3.2 SEBON and Regulatory Source Provenance (§3.4.2 & Acknowledgements)
* **The Contradiction in Early Files:** `issues.md` pointed out that SEBON's *"Capital Market Trends"* was never published by SEBON (it was a NRB publication title), and MoF *Economic Survey* was never used in the empirical regressions. `v1/review.md` suggested substituting generic SEBON directives.
* **The Ground Truth:** The empirical regressions use only bank audited annual reports (balance sheets, profit or loss, notes) and secondary market closing prices from NEPSE aggregators. Neither SEBON circulars nor MoF surveys were input variables.
* **Final Resolution:** 
  1. The SEBON bullet was completely purged from Chapter III §3.4.2.
  2. The Acknowledgements page was qualified: Nepal Rastra Bank and the Nepal Stock Exchange are acknowledged for public regulatory reports and trading archives, while SEBON is acknowledged for administering the capital market regulatory frameworks.

### 3.3 Candidate Identifiers and Campus Location
* **Proposal consistency:** The author confirms that the roll number, registration number, and "Pokhara, Nepal" match the proposal title page.
* **Verification limit:** No official college/TU record verifying the candidate-specific roll or registration number has been supplied. Proposal consistency is not independent institutional verification. Leave the thesis values unchanged and describe them only as matching the proposal unless an official record is checked.

### 3.4 Kumari Bank Meeting Document Citation
* **The Contradiction in Early Files:** `references.bib` originally listed `kumari2022sgm` as *"Extraordinary general meeting document..."* `issues/v1/review.md` claimed the PDF cover had been visually checked.
* **The Ground Truth:** The PDF is hosted on Kumari Bank's backend AWS S3 storage (`https://backend.kumaribank.com/storage/agm-report/2022/12/1670847430_Extra_Ordinary_General_Meeting_2079-08-25_Kumari_Bank_Ltd..pdf`), but the PDF file is not archived locally in `data/`. Asserting a visual cover verification when the file is not in the repository is an unverified claim.
* **Current citation treatment:** The bibliography entry `kumari2022sgm` is classified as an official corporate disclosure and uses a descriptive title, not a claimed exact cover title:
  - Title: *Meeting minutes and resolutions concerning the merger of Kumari Bank Limited and Nepal Credit and Commerce Bank Limited (2079/08/25)*
  - Howpublished: *Official corporate disclosure*
  - Note: *Approved final merger agreement with Nepal Credit and Commerce Bank Limited and 1:1 share swap ratio; meeting convened 25 Mangsir 2079 BS (11 December 2022). Descriptive bibliographic title; exact PDF cover wording not verified.*

### 3.5 Sharma (2011) Citation and Empirical Scope
* **Citation decision:** Keep `Sharma, Sanjeet` and *Journal of Arts, Science and Commerce* in `references.bib`. The local audit records the article header as *Journal of Arts, Science & Commerce* with ISSN 2231-4172 and also records the fuller indexed form *Researchers World – Journal of Arts, Science and Commerce*. *Researchers World – International Refereed Social Sciences Journal* is treated as the publisher-site heading, not the article's journal title.
* **Evidence limit:** The full article is not present in the local thesis files, so this record does not claim a fresh inspection. The journal-name conflict is closed based on the article-header/ISSN evidence recorded in the audit; year-by-year findings are not asserted.
* **Thesis findings summary:** The literature review and Table 2.1 retain only the abstract-level summary: EPS, DPS, and BVPS have significant associations, with EPS and DPS identified as the strongest determinants. The specific 11-of-16-year sign breakdown remains excluded.
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

This reconciliation records the current evidence and limits:
1. The Prabhu/Century omission is disclosed without an invented reason; the selection rationale remains open for supervisor disposition.
2. Candidate details are confirmed against the proposal, not an official candidate-specific college/TU record.
3. The pipeline run and test results are reported in the execution log; this record does not treat them as verification of external factual claims.
4. Earlier v1/v2 files remain as audit history and may contain superseded findings; consult this status record and the primary sources before treating any claim as closed.
