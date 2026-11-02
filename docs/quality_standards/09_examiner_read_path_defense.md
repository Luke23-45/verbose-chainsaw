# 09 — The examiner's read path, and the defense file

Primary sources: Pat Thomson, "How an examiner reads a thesis"
(https://patthomson.net/2017/04/03/how-an-examiner-reads-a-thesis/) —
examiners begin with conclusions/abstract looking for the contribution;
Golding et al. (2014), "What examiners do: what thesis students should
know", *Assessment & Evaluation in Higher Education*
(https://www.tandfonline.com/doi/full/10.1080/02602938.2013.859230) —
examiners judge whether the thesis is the student's own work of adequate
standard, with precision and honesty weighing more than ambition; Man
(2020) on master's examiner feedback patterns; McGill University's
published evaluation criteria
(https://www.mcgill.ca/gps/thesis/thesis-guidelines/examination/evaluation-written-thesis)
— examiners rate abstract/summary quality, evidence of scholarship,
methodological competence, presentation, and contribution.

---

## 1. The read path, and what it implies for editing order

Thomson's observation: examiners commonly (a) read the abstract and the
final chapter first, (b) skim the table of contents and the tables and
figures, (c) sample the literature review's gap claim, and (d) only then
read continuously — checking earlier promises against later delivery.

Implications already implemented in this thesis:
- Chapter V closes the hypothesis lifecycle by name (Table 11) — the
  contribution hunt lands on decisions, not promises.
- The abstract carries the headline numbers, so the first-read sampling
  already agrees with the tables.
- The TOC's entry titles are content-bearing ("Research Framework and
  Definition of Variables", "The Eight-Specification Estimation and
  Robustness Suite") — a skimming examiner can navigate by them.
- The gap claim is hedged to the reviewed literature (survives the
  examiner's counter-example test; see file 05).

## 2. The likely examiner questions for THIS thesis, with prepared answers

Every answer below exists somewhere in the thesis; this table is the
defense map (section pointers in brackets). If any answer requires new
analysis at viva time, that is a gap to close BEFORE submission.

**Q1. Why only five banks? Why not all twenty?**
[A: §3.3.2 + §1.6 item 1.] Purposive selection is the design: the four
major consolidations of the wave plus one unmerged benchmark, chosen for
pre/post data continuity. The 25.0% count proportion is stated; asset
shares are explicitly not claimed. Generalizability is limited to the
selected series — stated, not hidden.

**Q2. Your price is from aggregators, not NEPSE. Isn't that a problem?**
[A: §3.4.1, §3.4.3, §1.6.] The thesis's own disclosure: ShareSansar-
derived closes, 29/30 Merolagani agreement, the one divergence (NMB
437.00 vs 436.00) retained on the dataset's own full record and labeled
non-independent; NEPSE floor closes unverified. The window's validity
comes from the BAFIA §59(2) deadline, not from the price source; the
study's claims are associations, robust to price-source noise. If
pressed: the two excluded suspensions show the rule is applied against
the study's own interest in sample size.

**Q3. Why is nothing significant — is this a failed thesis?**
[A: §4.2.5, §4.3, §5.3.] The design anticipated this: two-tailed tests
with 14 residual df and HC3 conservatism; the contribution is the
regime-shift *evaluation* and the sensitivity result (R6 rejects at 5%),
not a rejection of theory. The magnitude story stands independently of
p-values (multiple halving; DPS collapse). Cite ASA principle 3 (file
08): conclusions are not threshold-driven.

**Q4. Isn't R6 just cherry-picking?**
[A: §4.2.6 item 4, §5.3.6.] R6 is pre-motivated: FY2078/79 pairs
pre-merger fundamentals with post-merger prices for four banks — a
stated entity-timing mismatch, disclosed in Table 2's note c and
evaluated by dedicated exclusion. It is a sensitivity specification
declared before results are discussed, not a post-hoc search; the five
other robustness variants are reported alongside it.

**Q5. Why HC3 and not clustered standard errors with G = 5?**
[A: §3.6.3.] Cluster-robust SEs are severely downward-biased and
over-reject with few clusters (citing Cameron et al.); HC3 with
Student's t on residual df is the conservative finite-sample choice.
The df accounting is printed.

**Q6. Two-tailed tests — but theory predicts directions. Why?**
[A: §1.4.] The hypotheses are framed non-directionally to let the data
support or fail to support theory; the theory's directional expectations
are discussed as theory (§1.4, §4.3.3), and the results are reported on
point estimates. This avoids the garden-of-forking-paths objection.

**Q7. The FY2078/79 mismatch is retained in the baseline. Why?**
[A: §3.3.4 note c, §1.6 item 5, R6.] Retained in baseline to preserve
sample continuity and because it is a real institutional feature of
merger accounting; its influence is measured by dedicated exclusion
(R6), not ignored.

**Q8. What is new here — Gurung & Dahal already did bank FE on NEPSE?**
[A: §2.4.4, §2.5.] Their design is static full-sample; no regime
interaction, no reporting-deadline price rule, no P/E exclusion applied
to the regime question. The five named gaps each map to a design
element.

**Q9. DPS collapsed to zero for 12 of 15 post years — did you model
selection?**
[A: §3.5.2, R4.] DPS is included only as a robustness regressor with
eligible-declaration timing; zero dividends are documented nils, not
missing. The thesis does not model dividend policy — that is stated as
future work (§5.5).

**Q10. Why is the accounting period 2076/77–2081/82 the right window?**
[A: §3.2 item 2.] Three pre + three post years around the January–
February 2023 joint-operation dates; April observation dates; the
window is the data availability constraint stated openly.

## 3. The McGill-criteria self-rating (do before submission)

McGill's examiner form dimensions, with this thesis's standing:

1. **Abstract/summary communicates the whole** — MET (A-checks in file
   04).
2. **Evidence of scholarship (literature command)** — MET via §2.4–2.5
   structure and the Table 2.1 matrix; the six pending observation
   counts are the only scholarship gaps.
3. **Methodological competence and justification** — MET (file 01 §Ch
   III; alternatives named at every choice).
4. **Quality of presentation** — MET (visual passes; zero overfull);
   re-verify after every rebuild.
5. **Contribution to knowledge** — MET (the regime-interaction result +
   the reproducible MPS_RD protocol; both stated in §1.1, §2.5, §5.3).
6. **Honesty/transparency** — the thesis's strongest dimension: the
   aggregator disclosure, the exclusion rule, the R6 sensitivity, the
   flagged NMB NAV variance, and the no-imputation protocol. Golding et
   al.'s finding that examiners reward precision and honesty over
   ambition is the reason these disclosures must never be softened to
   look "stronger".

## 4. Pre-viva verification sweep (one hour, before submission)

1. Rebuild; confirm zero overfull boxes and correct page numbering.
2. Re-run the full-text meta-comment sweep on the fresh PDF.
3. Trace one number per chapter (I → IV → V) by grep.
4. Re-read Table 11 and the abstract side by side — they must agree to
   the third decimal.
5. Rehearse Q1–Q10 aloud; every answer must end in a section pointer,
   never in improvisation.
