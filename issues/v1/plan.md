# Thesis issue resolution plan — v1

This plan sequences corrections to the seven-item audit in `issues.md`. No thesis source files or estimates are changed by this register. Close items only when the evidence or author decision described below is recorded.

## Phase 1 — Author-supplied facts and research design decisions

1. **Prabhu/Century selection rationale (I-01).** Ask the author for the contemporaneous factual rationale and any source/selection note. If there is no defensible rule, use transparent author-approved language that says the selection was purposive, identifies the omitted fifth combination, and acknowledges that the thesis does not claim an objective basis for preferring the four selected combinations. Do not make up a data-availability or comparability explanation.
2. **Identity fields (I-04).** Verify roll number, registration number, institution name, and “Pokhara, Nepal” against an official college/TU record. Change metadata only if the record conflicts; otherwise log that the author checked it.
3. **R9 / KBL timing (I-05).** Preserve R9 and add an explicitly supplementary, post-hoc R10 excluding both NMB and KBL FY 2076/77. The basis is the short four-day window between Deva joint operation and FY-end, contrasted with an April 2021 market price after several months of joint operation. State that KBL's annual report records acquisition accounting at year-end, so this is a partial-year exposure check, not another fully pre-acquisition row. The provisional estimate changes the earnings interaction materially, so a reproducible final estimate is needed.

## Phase 2 — Evidence and reference corrections

4. **SEBON/MoF source claims (I-02).** Inventory source notes and bibliography. For each claimed source, record the exact publication, year, URL, and claim supported. Add direct citations where claims rely on it. Remove or accurately qualify unsupported source bullets and revise any acknowledgements that overstate use. Verify the >30% market-capitalization statement against SEBON's primary table or leave it explicitly attributed to Gurung & Dahal as a secondary source.
5. **Kumari meeting source (I-03).** Read the PDF cover visually if available. Replace the generic bib title with the printed title; if the cover cannot be read, use the descriptive meeting-minutes title stated in `issues.md`. Keep the already supported 1 January 2023 operation date and 1:1 ratio but cite each to the source that directly establishes it.
6. **Sharma article (I-06).** Obtain the full article, inspect its actual regression table and conclusion, and correct the bibliography's journal title. Keep or revise the DPS-sign sentence only after this check. Until then, do not label the sign conflict confirmed.
7. **GBIME minutes (I-07).** Make one successful live-browser retrieval attempt. Record URL, date, and outcome. If successful, inspect the cover and the specific relevant resolution. If not, locate a NEPSE issuer mirror or bank-hosted copy; if still unavailable, switch to a source that supports the thesis claim and remove details unique to the unobserved minutes.

## Phase 3 — Implement and reconcile

8. Make accepted edits in the bibliography, Chapter III, and any dependent Chapter I/IV/V text. Preserve the audit trail and avoid silently changing the main sample.
9. Implement and run R10 from the versioned analysis script and frozen dataset; record the excluded rows, n=26, K=14, residual df=12, all coefficients, HC3 inference, and joint Wald test. Keep R9 as the existing NMB-only sensitivity. Regenerate all dependent tables/figures and revise every cross-reference and interpretation. Expand the Holm family to R2–R10 and update every adjusted p-value and related conclusion.
10. Perform a final cross-document consistency pass for sample description, exclusions, source citations, title-page metadata, bibliography, and any claims in abstract/conclusion. Close an issue only after the changed source and rendered thesis agree.

## Priority order

| Priority | Items | Reason |
|---|---|---|
| P0 | I-01, I-02, I-04, I-05 | Sampling transparency, source provenance, identity fields, and the material R10 sensitivity affect defensibility before submission. |
| P1 | I-03, I-06, I-07 | Resolve citation metadata and do not attribute content to files that remain unread. |

## Exit criteria

- Every issue is marked **resolved**, **author-approved limitation**, or **unresolved with explicit reason**.
- No empirical reason for Prabhu's exclusion is stated unless the author supplies support.
- R9 and post-hoc R10 remain separately labeled, and R10 is reproducible from recorded data and code with consistent multiplicity reporting.
- Every description of the R1–R9 suite, eight joint tests, and robustness-table coverage is reconciled with the added R10.
- Direct-source and secondary-source claims are distinguishable in the text and bibliography.
- Candidate identifiers have either been checked against an authoritative record or remain honestly labeled unverified.
- No unchecked claim is silently carried forward as a verified fact.

