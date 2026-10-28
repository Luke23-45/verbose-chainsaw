# Supervisor review: Chapter II, Literature Review

Draft file: `docs/draft/thesis/chapter_02_literature_review.md`
Verdict: The empirical summaries that could be checked are accurate, including
two that looked suspicious at first glance and turned out to be correct. The
must-fix items are one theoretical derivation, one legal wording regression,
and three overstatements. No empirical summary needs to be withdrawn.

## Strengths

- The theory section is not decorative: Ohlson, Kwon and Wang, signalling,
  agency, opacity, and the P/E circularity argument each do work that the
  methodology later uses. That is rarer than it should be in drafts.
- The Nepalese empirical review is specific (sample, period, method, finding)
  rather than a list of names, and Table 2.1 matches the text for the studies
  checked.
- The Kanchan qualification for NMB is stated correctly here (section 2.3.3),
  unlike its absence in Chapter 1.

## Verified and correct (do not "fix" these)

- **Gurung and Dahal 2025.** The draft describes a paper with 10 banks,
  FY 2013/14-2023/24, fixed-effects Hausman test, DPR, P/E, EPS, BVPS, and ROA
  significant. This was independently verified against the publisher record:
  Gurung and Dahal, "Decoding Market Valuation", Pravaha, vol. 31(1),
  pp. 1-12, DOI 10.3126/pravaha.v31i1.89145, abstract confirming 10 of 19 banks
  and the same period and variables. The description is correct.
  Warning for the author: there is a second, different paper by Dahal, Gurung,
  and Ghimire 2025 (Interdisciplinary Journal of Management and Social
  Sciences, 209 observations, all listed banks). Add a footnote in this
  chapter distinguishing the two Gurung papers, or an examiner who knows the
  second will mark the first description wrong.
- **Giri 2024.** Verified: Journal of Advanced Academic Research, vol. 11(1),
  pp. 12-23, DOI 10.3126/jaar.v11i1.65518. Abstract confirms 4 banks, 40
  observations, FY 2070/71-2079/80, significant positive correlation of price
  with DPS, P/E, and net worth, negligible EPS correlation. The draft's
  description is correct.
- **Kwon and Wang 2020.** Verified: Accounting and Finance, vol. 60(3),
  pp. 2717-2757, DOI 10.1111/acfi.12411. The draft's summary (post-merger
  earnings relevance falls, book value relevance rises as an anchor) is
  consistent with the paper's abstract. Note, however, that the draft's own
  finding is the opposite for book value (post slope negative). That
  divergence is a legitimate finding, not an error, but Chapter 4 must present
  it as a divergence from Kwon and Wang, not as confirmation of them
  (see Chapter 4 review).
- **Merger list (section 2.3.3).** Dates and swap ratios for all four 2023
  mergers, and the NMB-Kanchan note, are correct against the project record.

## Must fix

1. **Ohlson coefficient derivation (section 2.2.1, point 4).** The chapter
   derives P = BVPS + alpha_1 x abnormal earnings + alpha_2 x v, then states
   the empirical equation P = beta_0 + beta_1 x EPS + beta_2 x BVPS with
   beta_1 = omega / (1 + r - omega) and beta_2 = r(1 - omega) / (1 + r - omega).
   That step is not a valid exact derivation as written, and this was
   re-checked against the Ohlson literature in the second review pass.
   The correct Ohlson price equation is P_t = BV_t + alpha_1 x abnormal
   earnings_t + alpha_2 x v_t, with alpha_1 = omega / (R_f - omega),
   R_f = 1 + r, and abnormal earnings defined on lagged book value
   (EPS_t - r x BVPS_{t-1}). Substituting the clean-surplus identity
   (BV_t = BV_{t-1} + EPS_t - DPS_t) gives the weighted-average form
   P_t = (1 - k) x BV_t + k x (phi x EPS_t - DPS_t) + alpha_2 x v_t,
   where k = r x alpha_1 = r x omega / (R_f - omega) and
   phi = R_f / r. Hence the correct coefficient on contemporaneous BVPS
   is (1 - k) = 1 - r x omega / (R_f - omega), and the correct coefficient
   on contemporaneous EPS is k x phi = omega x (1 + r) / (R_f - omega).
   The draft's beta_1 = omega / (1 + r - omega) is alpha_1 itself, not
   the EPS coefficient, and its beta_2 = r(1 - omega) / (1 + r - omega)
   matches neither coefficient. Fix by either (a) showing the full
   derivation above, with lagged BVPS and v, and then stating that the
   thesis estimates a linear approximation that omits v and uses
   contemporaneous BVPS, or (b) deleting the closed-form beta formulas
   and presenting the empirical equation as the standard Ohlson-inspired
   linear specification used in the value-relevance literature
   (P = alpha_0 + alpha_1 x BV + alpha_2 x EPS + error, with EPS as a
   proxy for abnormal earnings). Do not present the approximation as an
   exact Ohlson result. An examiner in accounting will check this
   derivation first.
2. **BAFIA wording regressed (section 2.3.2).** The chapter says the statutory
   nine-month timeline "terminates exactly at the end of Chaitra". The statute
   (BAFIA Section 59(2)) requires publication within nine months of fiscal
   year-end; it does not name Chaitra. End-of-Chaitra is the thesis's
   operationalization of those nine months, counting Shrawan to Chaitra. The
   proposal was corrected on exactly this point in an earlier review; the
   draft thesis has reintroduced the unqualified wording. Restore the
   operationalization wording everywhere in this chapter: "operationalized
   at end-of-Chaitra", never "terminates exactly at end-of-Chaitra" as if
   the statute said so. Correction added in the second review pass, after
   checking the statute text (BAFIA 2073, Section 59, via the Law
   Commission / kaanun.app text): the draft's block quotation of
   Section 59(2) is itself inaccurate and must be replaced, not merely
   reworded. The actual Section 59(2) has two distinct duties: (a) submit
   the balance sheet and profit and loss account to NRB within three
   months of fiscal year-end, with details published for the public within
   that period as prescribed by NRB; and (b) publish the audited balance
   sheet and profit and loss account "within nine months of the next
   fiscal year", in the prescribed format. The draft's quotation
   ("within nine months of the completion of each financial year ...
   after obtaining the approval of the Rastra Bank") matches neither
   clause. Replace the quotation with the actual text, drop the
   quotation marks if the thesis prefers a paraphrase, and distinguish
   the 3-month unaudited duty from the 9-month audited duty. The
   end-of-Chaitra operationalization still follows from clause (b):
   nine months into the next fiscal year (Shrawan to Chaitra) ends at
   Chaitra-end, but that is the thesis's counting, not the statute's
   wording, and must be presented as such.
3. **"Uniquely among recent studies" (section 2.4.4, Gurung and Dahal).**
   The chapter says Gurung and Dahal are unique in applying the Hausman test
   and bank fixed effects. That superlative was not verified against every
   recent study in the review, and it is not needed for the argument.
   Delete "uniquely" and say "among the studies reviewed, Gurung and Dahal
   are the closest methodological precedent, because they use bank fixed
   effects". The gap claim survives without the superlative; with it, one
   counterexample defeats it.
4. **Universal negative gap claims (section 2.5).** "No published study in
   Nepal has formulated an explicit regime-interaction model" and "existing
   literature completely overlooks entity timing" are universal claims.
   They are plausible, but a universal negative cannot be proven by a
   literature sample. Reword to "none identified in this review" and "none
   of the studies reviewed addresses entity timing". The contribution does
   not shrink; the claim becomes defensible.
5. **Adhikari 46.01% figure (section 2.4.4).** The chapter attributes a
   46.01% post-merger decline in mean share price, with stable EPS, to
   Adhikari, Kavanagh, and Hampson 2023 (7 merged banks, 2013-2020). The
   thesis bibliography contains two Adhikari papers from 2023 (the journal
   article and the Central Bank Review article). This review did not confirm
   the 46.01% figure from the full text of either. Before submission, confirm
   which of the two papers contains it, the exact sample, and whether the
   decline is in mean price or mean price change, and cite that paper
   specifically. Do not leave a two-decimal figure attached to an ambiguous
   citation.

## Clarify

- **Table 2.1 versus text, Bhattarai 2014.** The text (section 2.4.2) says
  Bhattarai evaluated EPS, dividend yield, P/E, and BVPS; Table 2.1 lists
  MPS, EPS, DPS, P/E, BVPS. "Dividend yield" and "DPS" are not the same
  variable. Reconcile the two, and confirm from the paper which one Bhattarai
  used. Chapter 4 then says Bhattarai examined 14 banks, while Chapter 2
  says 35 bank-years; both can be true (14 banks need not give 35 bank-years
  in an unbalanced panel), but the thesis should state the bank count and
  the bank-year count together in one place so the two numbers do not look
  contradictory.
- **"Guarantees" language (section 2.2.5).** The chapter says observing prices
  after the deadline "guarantees that audited accounts were legally required
  to be public". That sentence is logically fine (it guarantees the legal
  requirement, not the fact), but it is easily misread as guaranteeing actual
  publication. Reword to "ensures the observation date falls after the date
  by which audited accounts were legally required to be public". Same
  substance, no misreading.
- **Capital market history (section 2.3.1).** The Securities Exchange Centre
  (1976), Securities Exchange Act (1983), NEPSE restructuring (1993), floor
  trading (13 January 1994), and SEBON's role are stated confidently. This
  review did not re-verify each date against a primary source. Add the NEPSE
  (2017) citation, which the draft already uses for floor trading, to the
  other history sentences, or confirm them from SEBON/NEPSE histories before
  submission. This is a citation-completeness point, not a suspected error.

## Overall for this chapter

Moderate revision. Fix the Ohlson derivation and the BAFIA wording first;
those two are the items an examiner is most likely to test. The empirical
review itself is stronger than most drafts, and the two most checkable
summaries (Gurung and Dahal, Giri) are right.
