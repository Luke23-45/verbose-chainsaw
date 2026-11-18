# Thesis issue audit — v1

**Review date:** 18 November 2026  
**Scope:** Seven claims raised in a separate AI review. This register checks the claims against the current thesis workspace and available primary/authoritative sources. The stated reviewer-vote counts were not supplied with source records and are not treated as evidence.

## Summary disposition

| ID | Issue | Finding | Status |
|---|---|---|---|
| I-01 | Prabhu Bank exclusion reason | Real transparency gap. The thesis says four of five early-2023 combinations were sampled, but does not explain which substantive rule excludes Prabhu. Do not invent a post hoc reason. | Author input required |
| I-02 | Chapter III SEBON/MoF source bullets | Real source-provenance concern. The bullets name broad classes of publications, but no direct SEBON or MoF bibliographic entries were found; the examined sources list no specific documents used. | Correct or substantiate |
| I-03 | Kumari SGM source title | The cited 11-page PDF is meeting minutes/resolutions concerning the Kumari–NCC merger, including approval of a 1:1 ratio. The exact cover wording is not recoverable from the text layer, so use a clear descriptive title unless the scan is visually checked. | Content verified; exact cover title pending |
| I-04 | Candidate identifiers and location | Values are present and match the proposal title page exactly. Workspace consistency is verified; correctness against the college/TU record is not. | External record check required |
| I-05 | R9 / KBL FY 2076/77 timing sensitivity | The proposed n=26 addition is a valid supplementary sensitivity, though not the same mismatch as NMB: Deva joint operation began only four days before FY-end, so KBL's annual accounting includes acquisition accounting but almost no post-acquisition operating period; its April 2021 price follows months of joint operations. A provisional same-method estimate materially moves the earnings interaction toward zero. | Add an explicitly post-hoc R10; keep original R9 visible |
| I-06 | Sharma (2011) DPS sign | The thesis's positive-sign description is consistent with the article abstract. A claimed conflict is not established from available evidence; the full article/table was not obtained, so coefficient-level sign and significance remain unchecked. | Do not call a confirmed error |
| I-07 | GBIME 16th AGM minutes | Cited NEPSE PDF URL could not be opened by the research viewer. The requested live-browser attempt was interrupted before the PDF became visible. | Unresolved; needs successful retrieval |

## I-01 — Prabhu Bank exclusion reason

**What the thesis says.** Chapter III §3.3 describes the sample as four of the five Class A combinations completed in the early-2023 consolidation wave plus NMB as an unmerged benchmark; it explicitly names Prabhu's acquisition of Century as the omitted fifth combination (`chapter_03_research_methodology.tex`, sample selection paragraph).

**What can be verified.** NRB's bank supervision report lists Prabhu Bank's joint operation after acquisition as 10 January 2023 and identifies Century as the acquired bank. Prabhu's own annual report likewise says the joint transaction started on 10 January 2023. This supports the fact of the acquisition and its timing; it does not supply a reason for excluding the series.

**Assessment.** The omission is not a hallucination. The method currently provides no differentiating criterion that explains why four combinations qualify and Prabhu does not. The shared criteria (early-2023 operation, listed status, six-year reports) do not on their face distinguish Prabhu. A reason such as data quality, continuity, or comparability must not be inserted unless supported by a contemporaneous record and applied consistently.

**Correction route.** Ask the author for the actual selection rationale and any supporting selection record. If none exists, state plainly that the four merger series were purposively selected and the omitted Prabhu combination was not excluded under a documented objective criterion; describe the sample as selective and limit external claims. Do not call this a “judgement call” in the thesis unless the author endorses that wording.

**Sources:** [NRB Bank Supervision Report 2024](https://www.nrb.org.np/contents/uploads/2025/03/Annual-Bank-Supervision-Report-2024-4.pdf); [Prabhu Bank 22nd Annual Report](https://www.prabhubank.com/uploads/Financial%20Reports/Annual%20reports/22nd%20Annual%20Report%20%28Nepali%29-1.pdf).

## I-02 — Chapter III SEBON and MoF source bullets

**What the thesis says.** Chapter III §3.4.2, under “Contextual and Regulatory Data Sources,” lists SEBON annual reports, Capital Market Trends publications, and disclosure directives, and lists MoF Economic Surveys from FY 2076/77 through FY 2081/82 (`chapter_03_research_methodology.tex`, lines 157–162). These are presented as sources used, not merely possible sources.

**Workspace check.** The thesis bibliography has no direct SEBON or Ministry of Finance entry. SEBON formation/history is cited to a NEPSE source, and the market-capitalization statistic is attributed to Gurung and Dahal (2025), whose article itself cites SEBON (2023); the thesis does not identify or directly cite that SEBON document. I found no MoF Economic Survey citations in the thesis chapters. No source-register entry or local copies for those publication series were found in the inspected project files.

**Assessment.** This is a substantiated provenance/overstatement risk, not proof that the author never consulted those sources. The line should either name specific documents actually consulted and cite them where used, or be removed/qualified so that it does not imply direct use. The single secondary citation is not a substitute for claiming direct SEBON consultation. Reviewer vote count (13/14) is unverified and adds no evidentiary weight.

**Correction route.** Search the author's source log/reference manager for actual documents. For each retained bullet, record title, reporting year, URL, access date, and the claim it supports; add the source to the bibliography and cite the relevant sentence. If no such use can be evidenced, delete the two bullets and any acknowledgements implying reliance on SEBON archives beyond the sources actually consulted. Review the SEBON market-capitalization statistic separately: either retrieve and cite the underlying SEBON report/table or clearly retain Gurung and Dahal as the secondary source.

**Primary lead:** [SEBON publications portal](https://www.sebon.gov.np/publications) (specific cited publication still to be identified). **Secondary article:** [Gurung & Dahal (2025), Pravaha](https://portal.tu.edu.np/downloads/NCCPravaha20251_2025_12_24_10_15_28.pdf).

## I-03 — Kumari SGM document title

**PDF opened:** the official Kumari Bank URL in `references.bib` resolves to an 11-page PDF. The extracted contents show a meeting proceeding with the meeting date 2079/08/25 and numbered agenda/resolution sections. It records resolutions approving the merger report and final agreement between Kumari Bank and Nepal Credit and Commerce Bank, and a 1:1 share swap ratio. Therefore, it is a record/minutes of the special/extraordinary general meeting, not merely an announcement or annual report. The existing bibliography title (“Extraordinary general meeting document, FY 2079/80…”) is an imprecise generic description.

**Exact-title limitation.** The PDF's first page is scanned and the research viewer's screenshot fetch failed. The document body is legible enough to establish its nature and substance, but not to certify the cover's exact verbatim title. A defensible descriptive bibliography title is **“Minutes of the Special General Meeting of Kumari Bank Limited held on 2079/08/25”** (use “Extraordinary” instead of “Special” only if that is what the cover itself prints). This is a catalog description, not a verified transcription of a cover title.

**Assessment.** The interim neutral-title concern is valid. The merger date (1 January 2023) is independently stated by Kumari Bank, and the 1:1 ratio is explicit in the cited minutes; neither fact is challenged by the title issue.

**Correction route.** If the cover can be visually read, replace the bibliography title with its exact printed wording; otherwise adopt the quoted descriptive title and retain the official PDF URL. Cite the minutes for the 1:1 ratio and the bank/NRB source for the effective joint-operation date.

**Sources:** [Kumari Bank meeting PDF](https://backend.kumaribank.com/storage/agm-report/2022/12/1670847430_Extra_Ordinary_General_Meeting_2079-08-25_Kumari_Bank_Ltd..pdf); [Kumari Bank corporate history](https://www.kumaribank.com/personal-banking/welcome-to-kumari-bank); [NRB Bank Supervision Report 2024](https://www.nrb.org.np/contents/uploads/2025/03/Annual-Bank-Supervision-Report-2024-4.pdf).

## I-04 — Roll number, registration number, and “Pokhara, Nepal”

**Workspace check.** `src/thesis/config/metadata.tex` contains Roll No. `67514/24`, Registration No. `7-2-48-1060-2018`, campus “Triveni International College,” and November 2026. The proposal title page contains the same identifiers and “Pokhara, Nepal.” This confirms consistency between the thesis metadata and proposal.

**Assessment.** The AI review accurately describes an external-verification gap; it does not establish an error. The college/TU record is the controlling authority for the identifiers, while the college's official affiliation/address record or the student's submission instructions should govern the location line. Do not change values based on speculation.

**Correction route.** Compare the title-page fields with an official registration/college record before final submission. If the record is not available, retain the proposal-consistent wording only as author-supplied information and keep this item open; do not imply the office has verified it.

## I-05 — R9 and KBL FY 2076/77

**What the thesis says.** R9 excludes NMB FY 2076/77 because its fundamentals precede the Kanchan acquisition while its April 2021 market price follows it (`T5_robustness.md` note; Appendix E). The proposed extra deletion is KBL FY 2076/77 on Deva Bikas timing.

**Evidence checked.** Kumari Bank's FY 2077/78 annual report says Deva's joint operation began on Asadh 28, 2077 (12 July 2020). KBL FY 2076/77 closed on 16 July 2020. KBL's own FY 2076/77 report and local audit trail record Deva within the year-end reporting entity. This differs from NMB's Kanchan acquisition, which followed the FY 2076/77 accounting period. The dates are not parallel in the way the proposed n=26 extension assumes.

**Assessment.** The reviewer is right that this should be examined, but the reason needs precision. KBL FY 2076/77 is not wholly pre-Deva: the annual report records the acquisition and acquired balances before year-end. However, the joint operation started just four days before FY-end, so the annual flow measures contain only a very short post-acquisition operating window while the 13 April 2021 market price follows several months of joint operations. That is a plausible partial-year/entity-timing sensitivity, not the same fully pre-acquisition-fundamentals case as NMB/Kanchan. Because KBL FY 2076/77 is also identified as influential in the thesis diagnostics, the combined exclusion is worth reporting as a supplementary check.

**Provisional estimate check.** An in-memory replication of the existing HC3 two-way fixed-effects computation on the frozen joined panel, dropping both NMB and KBL FY 2076/77, gives n=26, K=14, residual df=12; $δ_E=-0.5575$ (HC3 SE 4.7405), $δ_B=-1.3078$ (SE 0.8446), joint Wald $F(2,12)=1.5699$, $p=0.2479$. The same calculation reproduces the stored R2 and R9 headline coefficients and joint tests within rounding. Existing R9 (NMB-only deletion) is $δ_E=-3.4454$, $δ_B=-1.7414$, $F(2,13)=1.7942$, $p=0.2051$. This provisional result is not thesis-ready: the current R9 script has no R10 path or saved reproducible output. It does show the additional deletion materially changes the earnings-interaction estimate, supporting a formal rerun and transparent reporting.

**Correction route.** Preserve R9 unchanged and add a separately labeled R10 that excludes both NMB and KBL FY 2076/77. Label it a supplementary/post-hoc sensitivity, explain the four-day Deva timing and distinguish it from NMB's fully pre-acquisition FY, and do not present R10 as pre-specified. Implement R10 in the reproducible analysis pipeline, verify the fit against R2/R9, regenerate the full robustness output, and reconsider all text that describes sign stability, inference, or the number of specifications. Since R10 is reported alongside the other joint tests, expand the Holm family from R2–R9 to R2–R10 and update adjusted results consistently. Do not replace R9 or change the primary sample.

**Primary-source trail:** KBL's FY 2076/77 annual report (`data/reports/KBL/FY2076-77/KBL_FY2076-77_annual_report.pdf`) states that Deva joint operation began on 28 Ashadh 2077, records acquisition-related amounts, and reports basic EPS of 12.08. The bank's [FY 2077/78 Annual Report](https://backend.kumaribank.com/storage/financial-report/English_Annual_Report_FY_2077-78.pdf) independently gives the same operation date. FY 2076/77 ended 16 July 2020; joint operation began 12 July 2020.

## I-06 — Sharma (2011) dividend-per-share sign

**What can be verified.** The cited source page identifies Sanjeet Sharma's article, *Determinants of Equity Share Prices in India*, in *Researchers World*, 2(4), 2011, pp. 51–60. Its abstract says DPS and EPS are the strongest determinants and says regular dividends affect market price “in positive direction.” The thesis sentence likewise characterizes Sharma's DPS finding as positive.

**Unresolved part.** The proposed concern says a sign conflict exists in the article's full text/table, but that text was not obtained. The source page's PDF download timed out. Thus there is no evidence here that the thesis's sign is wrong; conversely, the abstract is not enough to verify coefficient-level direction, significance, or whether the article has an internal inconsistency.

**Assessment (journal-title correction superseded).** The claim “DPS-sign conflict” is not established and should not be recorded as a confirmed error. The earlier assertion that “Researchers World - International Refereed Social Sciences Journal” is the journal title confuses the publisher-site heading with the journal wording. The current thesis bibliography's “Journal of Arts, Science and Commerce” is retained, consistent with the article-header/ISSN evidence recorded in the later audit. See `issues/v2/final_reconciliation_record.md` for the current disposition.

**Correction route.** For the journal field, retain “Journal of Arts, Science and Commerce”; do not substitute the publisher-site heading. The full-text sign question remains separate: any year-by-year or coefficient-level claim requires the article text, so keep the thesis summary at the abstract level unless that text is independently available.

**Source:** [Primary journal article page](https://www.researchersworld.com/index.php/rworld/article/view/303).

## I-07 — GBIME 16th AGM minutes

**What the thesis cites.** `references.bib` identifies Global IME Bank's 16th AGM minutes filed with NEPSE, using a NEPSE `fetchFiles` URL.

**Retrieval result.** The research web viewer returned an access error for the exact URL. The user requested one live browser check; the browser opening call was interrupted before a visible PDF or error page could be inspected. This is not a successful check, and no content-level claim about the minutes is made here.

**Correction route.** Retry the exact URL in a normal live browser once, note the result/date, and if available save or locally inspect the PDF's cover and relevant resolution pages. If the URL remains unavailable, locate the same filing via NEPSE's issuer disclosure page or a bank-hosted copy, cross-check identity/date, then update the bibliography URL and cite only facts confirmed in the retrieved document. If no copy can be obtained, replace this citation for the merger fact with a bank annual report or NRB record and remove unsupported details attributed to the minutes.

**URL:** [Cited NEPSE PDF](https://www.nepalstock.com.np/api/nots/security/fetchFiles?fileLocation=gbime_user%2F2023-01-04%2F16th+AGM+Minute_1672813977990.PDF).

## Inputs the author must supply

1. The real selection reason for omitting Prabhu/Century, if one was documented; if none, approval to state the omission as a purposive selection judgement without inventing a factual reason.
2. A college/TU record or confirmation that the title-page identifiers and place line are correct.
3. If available, the GBIME minutes PDF or a request to retry its live browser retrieval.

