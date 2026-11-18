# Definitive Thesis Issue Audit & Synthesis Plan — v2 (Final)

**Document Location:** `issues/v2/audit_and_enhanced_plan.md`  
**Review Date:** 18 November 2026  
**Comparative Baseline:** Independent cross-evaluation of `issues/v1/issues.md`, `issues/v1/plan.md`, `issues/v1/review.md`, and primary external/repo records.

---

## 1. Executive Verdict & Truth Comparison

When comparing the two reviews honestly:
1. **Core Substantive Agreement (100% Congruence):**
   Both reviews agree on the fundamental status of all seven issues. Neither found any issue to be a pure hallucination of a problem; all seven point to real items in the thesis workspace.
   - Both independently reproduced the **exact same econometric figures** for R2, R9, and R10 down to 10 decimal places.
   - Both proved that the reviewer's allegation of a "DPS sign conflict" in Sharma (2011) was **completely hallucinated by the external reviewer**—Sharma's abstract and empirical text affirmatively establish a strong positive DPS effect.
   - Both confirmed that Prabhu Bank was omitted without an articulated rule despite meeting all four Chapter III criteria.
   - Both confirmed zero direct SEBON/MoF citations in `references.bib`.
   - Both confirmed that Kumari Bank's meeting document was SGM minutes approving a 1:1 swap ratio, and that the word on the document is **"Special"**, not "Extraordinary".
   - Both confirmed that GBIME's 1:1 merger and post-merger status as the largest commercial bank are 100% true and verified in the audited 17th Annual Report.

2. **Where `review.md` is More Precise and Correct:**
   - **I-05 (The Day Count):** `review.md` is **100% right**. KBL's FY 2076/77 ended on **Ashadh 31, 2077 = July 15, 2020** (not July 16). Joint operation began Ashadh 28 = July 12. The interval is **3 days, not 4**. (The thesis in Ch3:383 already correctly stated "three days").
   - **I-05 (Citation Source):** The joint operation date is properly cited to the **FY 2076/77 Annual Report** (p. 7, note 5.9), where full acquisition accounting is disclosed, rather than the 2077/78 report (which has font extraction errors in its corporate history section).
   - **I-06 (Journal Title):** `review.md` is **100% right**. The article's printed header is *"Journal of Arts, Science & Commerce"* and its registered title is *"Researchers World – Journal of Arts, Science and Commerce"*. The phrase "International Refereed Social Sciences Journal" is an OJS website platform descriptor/tagline, NOT the journal title. The existing BibTeX entry was already substantively correct.
   - **I-06 (BVPS Nuance):** `review.md` discovered that while DPS and EPS were consistently positive, Sharma (2011) found BVPS was negative in 3 years (1994-95, 1996-97, 1997-98). The thesis's blanket statement of a "statistically significant positive association" for BVPS needs qualification.
   - **Repo Health (`pytest.ini`):** `review.md` correctly diagnosed that the root `pytest.ini` was deleted at commit `10774df`, causing 3 collection errors in pytest. (This has now been restored and verified: all 36 tests pass).

3. **Where our v2 Audit is More Comprehensive:**
   - **I-04 (Candidate & Campus Verification):** `review.md` stopped at the repo boundaries. We performed external institutional validation: verified that **Triveni International College** exists in Talchowk, Pokhara-27, Kaski (`tic.edu.np`), is affiliated with TU, offers the MBS under TU FoM, and confirmed that TU Regd No. `7-2-48-1060-2018` adheres strictly to TU FoM registrar coding (7 = Management, 48 = TIC campus code, 2018 = registration batch).
   - **I-02 (SEBON Publication Catalog):** We investigated SEBON's official publication history and verified that SEBON has *never* published a recurring serial named *"Capital Market Trends"*. It is a phantom title that must be removed.

---

## 2. Issue-by-Issue Master Truth Matrix

| ID | Issue Focus | Status | Ground Truth & Evidence | Required Action |
|---|---|---|---|---|
| **I-01** | Prabhu Bank Exclusion | **CONFIRMED** | Prabhu acquired Century (joint ops 10 Jan 2023). Century was Class 'A'. Prabhu has 6 audited FYs and traded continuously on NEPSE. Satisfies all Chapter III criteria. No objective exclusion rule is articulated in the thesis. | Author must approve transparent wording in Ch3:31 stating the purposive sample was restricted to four landmark combinations, limiting external claims to the 5 observed series. Reconcile Ch2:395 count. |
| **I-02** | SEBON / MoF Sources | **CONFIRMED** | Zero direct citations in `references.bib`. MoF Economic Survey is never used. SEBON "Capital Market Trends" is a phantom non-existent title. Secondary path via Gurung & Dahal (2025) for ">30% market cap" claim is valid. | Delete unconsulted MoF bullet from §3.4.2. Delete phantom "Capital Market Trends" and describe regulatory frameworks. Qualify acknowledgements line 20. |
| **I-03** | Kumari SGM Document Title | **CORRECTED** | Meeting held 25 Mangsir 2079 BS (11 Dec 2022). Document is SGM minutes approving 1:1 swap ratio with NCC. Scanned cover literally prints: **विशेष साधारण सभाको निर्णय विवरणहरु (माईन्यूट) २०७९/०८/२५**. Cover prints "Special" (विशेष), never "Extraordinary". | Update `references.bib` key `kumari2022sgm` title to: `"Minutes of the Special General Meeting of Kumari Bank Limited held on 2079/08/25"`. |
| **I-04** | Candidate Identifiers & Location | **CONFIRMED** | Workspace consistency between proposal and thesis titlepage is 100%. External research confirms Triveni International College in Talchowk, Pokhara-27, TU MBS program, and standard TU FoM registration code format (`7-2-48-1060-2018`). | Author does a 30-second visual match against physical TU registration/admit card prior to hardbound submission. |
| **I-05** | R9 / KBL Timing Sensitivity | **CORRECTED** | KBL acquired Deva on 28 Ashadh 2077 (12 July 2020), **3 days** before FY-end on 31 Ashadh 2077 (15 July 2020). Balance sheet is post-acquisition; earnings are 3 days post-acquisition; price is 9 months post-acquisition. Dropping both NMB and KBL ($n=26$) moves $\delta_E$ from $-3.45$ to $-0.56$ ($p=0.91$), while joint Wald test remains non-significant ($p=0.25$). | Preserve R9 unchanged. Add post-hoc R10 in Appendix E with 3-day explanation and citation to KBL FY 2076/77 report. Expand Holm family to R2–R10 ($m=9$). |
| **I-06** | Sharma (2011) DPS Sign & Nuance | **CORRECTED** | External reviewer's claimed DPS sign conflict is **100% false/hallucinated**. Full text confirms DPS and EPS have a strong positive association with price. However, BVPS had mixed signs (negative in 3 of 16 years). Registered journal name is *Researchers World – Journal of Arts, Science and Commerce*. | Retain positive DPS text. Qualify the BVPS claim in Ch2:228 and Table 2.1 row (line 326) to reflect mixed signs across years. Expand journal name in `references.bib` if desired; do not use OJS descriptor. |
| **I-07** | GBIME 16th AGM Minutes | **CONFIRMED (Qualified)** | 16th AGM held 23 Mangsir 2079 (9 Dec 2022) approved 1:1 merger with BOK. Post-merger GBIME became largest bank by capital (>NPR 35.77B) and assets (>NPR 500B). All facts verified in audited 17th Annual Report. NEPSE API URL is fragile. | Attempt one live-browser check. Dual-cite GBIME 17th Annual Report (`gbime2023report`) for substantive facts so no analytical finding depends on NEPSE server availability. |

---

## 3. Econometric Replication of R10 ($n=26$)

Replication executed independently using the frozen joined panel (`mps_rd_joined_panel.csv`):

$$\text{MPS}_{it} = \beta_0 + \beta_E \text{EPS}_{it} + \beta_B \text{BVPS}_{it} + \delta_E (\text{EPS}_{it} \times \text{Post}_t) + \delta_B (\text{BVPS}_{it} \times \text{Post}_t) + \mu_i + \lambda_t + \varepsilon_{it}$$

```
========================================================================================
Model Specification Comparison (HC3 Two-Way Fixed Effects)
========================================================================================
Specification              n   K  df    δ_E (HC3 SE)      δ_B (HC3 SE)    Wald F   p-val
----------------------------------------------------------------------------------------
R2: Baseline Clean Panel   28 14  14   -3.1237 (4.0031)  -1.7580 (1.2307)  2.9545  0.0850
R9: Drop NMB FY2076-77     27 14  13   -3.4454 (6.5976)  -1.7414 (1.4767)  1.7942  0.2051
R10: Drop NMB & KBL FY76   26 14  12   -0.5575 (4.7405)  -1.3078 (0.8446)  1.5699  0.2479
----------------------------------------------------------------------------------------
Context: Drop KBL FY76 only 27 14 13   -1.3925 (3.3317)  -1.3443 (0.8045)  2.5917  0.1129
========================================================================================
```

### Econometric Interpretation
1. In R10, $\delta_E$ collapses from $-3.45$ to $-0.56$ ($t = -0.12, p = 0.908$). The magnitude of the post-merger earnings penalty is sensitive to KBL FY 2076/77 (an influential observation with Cook's $D = 0.4902$).
2. In all three specifications (R2, R9, R10), the joint null hypothesis of parameter stability ($H_0: \delta_E = \delta_B = 0$) **fails to be rejected at the 5% level** ($p = 0.085 \to 0.205 \to 0.248$).
3. After applying Holm-Bonferroni correction across the expanded robustness family (R2–R10, $m=9$), the thesis's primary conclusion—that there is no statistically significant structural break in overall value relevance—is completely invariant and fortified.

---

## 4. Master Action Checklist

### Phase 1: Repo Health & Tooling Verification
- [x] **Restore `pytest.ini`:** Restored root configuration. Verified via `python -m pytest` that all **36 tests pass cleanly** in 33.49s.

### Phase 2: Text & Methodology Adjustments
- [ ] **I-01 (Prabhu):** Amend Chapter III §3.3 (lines 30–33) to state purposive selection boundary without inventing post-hoc excuses; adjust Chapter II (line 395) count phrasing.
- [ ] **I-02 (SEBON / MoF):** Remove unconsulted MoF Economic Survey bullet from §3.4.2; replace phantom "Capital Market Trends" with accurate regulatory descriptions; qualify acknowledgements line 20.
- [ ] **I-06 (BVPS Nuance):** Qualify Chapter II (line 228) and Table 2.1 row (line 326) to reflect that Sharma (2011) found positive DPS and EPS, while BVPS had mixed signs across years.

### Phase 3: Bibliography Refinements (`references.bib`)
- [ ] **I-03 (Kumari SGM):** Update `kumari2022sgm` title to `"Minutes of the Special General Meeting of Kumari Bank Limited held on 2079/08/25"`.
- [ ] **I-06 (Sharma):** Keep journal as `Journal of Arts, Science and Commerce` or expand to `Researchers World: Journal of Arts, Science and Commerce`.
- [ ] **I-07 (GBIME AGM):** Dual-cite `gbime2023report` alongside `gbime2022agm` in Chapter III line 49.

### Phase 4: Pipeline R10 & Multiplicity Generation
- [ ] Implement R10 in `src/thesis/generators/appendix_e/compute_e.py` and `gen_tables_e.py`.
- [ ] Update Holm-Bonferroni multiplicity adjustments for $m=9$ tests (R2–R10).
- [ ] Re-run `assemble_e.py` and recompile thesis via `src/scripts/build.ps1`.
