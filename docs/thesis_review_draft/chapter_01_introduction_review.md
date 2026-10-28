# Supervisor review: Chapter I, Introduction

Draft file: `docs/draft/thesis/chapter_01_introduction.md`
Verdict: Structurally sound and well argued. No data error was found in this
chapter. The fixes are about consistency with later chapters and about not
overstating what the price window proves. None requires new data.

## Strengths

- The problem statement is genuinely structured: four distinct problems
  (regime shift, P/E circularity, look-ahead bias, small-cluster fragility) map
  cleanly onto the objectives, hypotheses, and robustness suite. An examiner
  can follow the logic from problem to test without guessing.
- The merger dates in section 1.2, problem 1, are correct: GBIME 9 January 2023,
  HBL 24 February 2023, KBL 1 January 2023, NIMB 11 January 2023.
- The degrees-of-freedom accounting (28 - 14 = 14 in Model 2) is correct and
  is stated before the results, which is the right place for it.
- The limitation section is unusually honest for a draft: it names the small
  sample, the attrition, the entity mismatch, and the non-causal interpretation
  before the results chapter tries to use them.

## Must fix

1. **Legal requirement versus actual publication (sections 1.2 problem 3,
   1.5 point 2).** The chapter says observing prices after the Chaitra deadline
   "ensures that audited financial information was legally required to be
   public" and, in the rationale, that "the market had legal access to audited
   accounts". The first phrasing is correct. The second, and any sentence that
   slides from "legally required" to "was public", is not proven: per-bank-year
   disclosure-before-deadline proof was never done in this project. Keep the
   legal-requirement wording everywhere. Do not claim actual publication for
   any bank-year that was not individually checked. This is the same point
   that applies, more sharply, to Chapter 3.
2. **Hypothesis framing must match Chapter 4 (section 1.4).** Chapter 1 states,
   correctly, that all hypotheses are tested two-tailed at 5% without
   directional signs, with H1 and H2 as beta != 0. Chapter 4 then states nulls
   as beta <= 0 and hypotheses as beta > 0. Fix Chapter 1 or Chapter 4 so
   they agree; recommended fix is in Chapter 4 (see its review), but Chapter 1
   should also state the nulls explicitly as beta_E = 0 and beta_B = 0, so an
   examiner does not have to infer them from the "two-tailed" sentence.
3. **NMB as benchmark, without the Kanchan qualification (section 1.1).**
   Chapter 1 says NMB "maintained operational continuity without participating
   in the early-2023 consolidation wave". That is true for 2023, but a reader
   will reasonably take it to mean NMB never merged. NMB acquired Kanchan
   Development Bank in August 2020, adding about NPR 0.57 billion to share
   capital in FY 2077/78. Chapters 2 and 3 state this correctly. Add one
   sentence or footnote in Chapter 1, in the same place, so the benchmark
   claim is not misleading on first reading. The correct claim is: NMB did
   not participate in the 2023 wave; it is not a never-merged bank.
4. **"Documented, open-source dataset" (section 1.5 point 5).** The thesis
   claims an open-source dataset. No licence is stated anywhere in the draft
   chapters reviewed, and the dataset's price component is derived from
   third-party aggregators. Either add a licence and a data-availability
   statement that covers the aggregator terms, or delete "open-source" and
   say "documented, reproducible dataset and code". Do not leave an
   open-source claim that cannot be verified from the thesis itself.

## Clarify (not errors, but an examiner will ask)

- **"Apex of 32 commercial banks by FY 2011/12" (section 1.1).** The chapter
  cites Adhikari, Kavanagh, and Hampson 2023 for this census figure. That
  paper, as cited elsewhere in the thesis, is a study of merged banks, not a
  licensing census. Add an NRB licensed-institutions list as the source for
  the 32 figure, or soften to "about 32" with the NRB source. The 20 figure
  for mid-October 2023 is correctly sourced to the NRB list.
- **Limitation 6, "published disclosures confirm" (section 1.6).** The chapter
  says published disclosures confirm banks routinely released highlights months
  before the Chaitra deadline. That is a general practice claim, not a
  per-bank-year finding. Reword to "in the disclosures examined for this
  study, highlights were typically released between Ashwin and Poush", which
  is what the DPS announcement record supports, and keep it as a limitation,
  not as proof of publication for every row.
- **VIF wording (section 1.5 point 3).** The chapter says EPS-ROA collinearity
  has "variance inflation factor about 30". The bivariate VIF from
  r = 0.975 is about 20. The value near 30 comes from the four-variable
  exploratory model, not from the EPS-ROA pair alone. State which model the
  VIF comes from, or give the range "about 20 to 30 depending on
  specification", as Chapter 4 does. This is rounding and context, not a
  substantive error.
- **Objectives versus questions (sections 1.2-1.3).** Question 3 and objective 3
  both now include the transition year, entity mismatch, bonus adjustment,
  and restated EPS. This is consistent, unlike the earlier proposal draft.
  Keep it that way; do not add a robustness item to one list without adding
  it to the other.

## Verified in this chapter

- Research questions, objectives, and hypotheses are mutually consistent in
  content (the inconsistency is only the null framing in Chapter 4).
- Pre/post period definitions (FY 2076/77-2078/79 pre, FY 2079/80-2081/82 post)
  are used identically in Chapters 1, 3, 4, and 5.
- No descriptive statistic in Chapter 1 contradicts Table 4.1.

## Overall for this chapter

Minor revision. Fix items 1-4, then this chapter can stand. The chapter's
argument is stronger than its conclusions chapter, because it does not yet
claim what the results chapter later overclaims.
