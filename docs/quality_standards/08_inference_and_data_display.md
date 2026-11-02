# 08 — Statistical inference language and data display

Primary sources (ASA statement and APA guide fetched in full):
Wasserstein & Lazar (2016), "The ASA Statement on p-Values: Context,
Process, and Purpose", *The American Statistician* 70(2), with the six
principles (https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf);
Wilkinson & the Task Force on Statistical Inference (1999),
*American Psychologist* 54(8), 594–604; APA Style *Numbers and
Statistics Guide*, 7th ed. (https://apastyle.apa.org/instructional-aids/numbers-statistics-guide.pdf);
E. R. Tufte, *The Visual Display of Quantitative Information* — data-ink
maximization, chartjunk, the lie factor.

---

## 1. The ASA's six principles, verbatim, and what each binds in this thesis

The ASA Statement (2016) adopts six principles; quoted in substance:

1. *"P-values can indicate how incompatible the data are with a
   specified statistical model."* — The thesis's p values come from HC3
   t statistics on stated residual df; the "specified model" (two-way
   FE) is named everywhere a p appears. Binding: never report a p
   without the model context nearby.
2. *"P-values do not measure the probability that the studied
   hypothesis is true."* — Binding: the thesis must never write "there
   is a 95% probability that..." or "the hypothesis is 95% likely".
   Current text is clean; keep it.
3. *"Scientific conclusions and business or policy decisions should not
   be based only on whether a p-value passes a specific threshold."*
   — Binding: this is exactly the thesis's sensitivity-dependent
   framing. The joint Wald p = 0.085 never appears alone; it is always
   accompanied by the R6 reversal and the magnitude story. The policy
   recommendations in §5.4 are grounded in magnitudes (DPS −76.9%,
   54-day halts), not in p-value crossings. Keep this separation.
4. *"Proper inference requires full reporting and transparency."* —
   Binding: all eight specifications reported (Table 8), including the
   ones that weaken the story (R6's rejection is printed next to the
   five non-rejections); exclusion rules and their two casualties named.
   Never add a specification that is estimated but unreported, and
   never drop one that embarrasses — the suite's honesty is the
   thesis's strongest defense.
5. *"A p-value, or statistical significance, does not measure the size
   of an effect or the importance of a result."* — Binding: the thesis
   separates significance talk from magnitude talk ("economically
   substantial but not statistically significant"). The magnitude
   narrative (multiple halving; DPS collapse) must continue to appear
   regardless of the p values.
6. *"By itself, a p-value does not provide a good measure of evidence
   regarding a model or hypothesis."* — Binding: no sentence may hang
   an entire conclusion on one p; every conclusion in §5.3 carries
   estimate + level + sensitivity status.

## 2. NHST language rules for a two-tailed framework

- Decisions are "fail to reject H0" / "reject H0" — never "accept",
  "prove", "confirm the hypothesis". (The historical "confirm for a
  two-tailed test" violation is fixed; keep it fixed. "Structural
  instability confirmed at the 5% level" in the §1.1 preview is the
  one borderline instance — a rejection *is* a confirmed incompatibility
  with H0, but "rejected at the 5% level" is the safer verb. Watch
  item.)
- "Marginal" only with its level attached ("marginal significance at
  the 10% level"), never "almost significant".
- Two-tailed framing: H1–H4 are non-directional; the text may not
  re-introduce direction through verbs ("earnings *drive* prices" is
  directional; "earnings carry the larger point-estimate slope" is not).
  §5.2.3's "on point estimates" hedge is the model.
- R6's rejection language: "the joint Wald test rejected parameter
  stability at the 5% level" — the one place "reject" appears; keep the
  sensitivity attribution beside it every time.

## 3. APA number conventions, and the one deliberate deviation

APA (7th guide; 6th edition, §4.31–4.35 rules on statistics):
- Statistics to two decimals (df and exact p to two–three);
- *Italic* Latin statistical letters (t, F, p, r, n), upright Greek
  (β, δ, λ, α, μ) — the thesis typesets β_E, δ_B, λ_t as upright Greek
  with italic subscripts, consistent throughout;
- CIs in square brackets with the confidence level stated: "95% CI
  [−6.587, 10.777]" — the thesis's format matches (§4.2.3 point 2);
- **Strict-APA deviation, documented:** APA omits the leading zero for
  statistics bounded by 1 (p = .616, r = .975); the thesis consistently
  uses p = 0.616, r = 0.975. The deviation is uniform (every p and r in
  the thesis), matches common thesis practice, and the TU reference
  thesis retains leading zeros. Decision: keep the leading zeros for
  consistency; do NOT mix conventions. If the supervisor asks for
  strict APA, the change is global (p, r only — never df or
  coefficients) and must be done in one pass.
- Percentages: the thesis writes "33.80%" (recomputed from rounded
  means, documented in the phase review as a shared rounding artefact).
  The note-level rule — recomputed percentages may differ from
  unrounded computation by ≤ 0.3pp — should be volunteered if an
  examiner asks about any percentage's third decimal.

## 4. Tufte's display principles, applied to Tables 1–13 and Figures 1–11

**Data-ink maximization.** The thesis tables use booktabs rules only
(toprule/midrule/bottomrule) with no vertical rules and no cell shading
— the Tufte-approved table form. Figures plot data with minimal
furniture (light grids, Okabe–Ito colorblind-safe palette). Keep this;
adding borders, heavy grids, or 3-D effects would be chartjunk.

**The lie factor (|graphed change ÷ actual change| ≈ 1).** The one
recurring examiner question for this thesis's figures: several y-axes
do not start at zero (e.g., F6's MPS_RD panel spans ~200–500; BVPS
~140–200). For line charts of *levels* this is standard and honest —
the variation is real and the axis frame is labeled — but the defense
must be ready: the axes measure levels over time (difference matters),
not magnitudes from zero, and every axis is tick-labeled. If asked,
answer with the Tufte principle that matters here: the chart must not
exaggerate — the visible break at FY2078/79 corresponds to a real 33.8%
mean price drop. The scatter plots (F1, F3) plot the raw data range
with no truncation.

**Integrity of encodings.** F3's fit lines are descriptive bivariate
OLS fits — and the thesis Note says so and explains the post-BVPS sign
difference as year-effect absorption. This is the anti-"lie factor"
discipline at the caption level: the display never lets a reader
mistake a descriptive line for the model estimate. The same disclosure
pattern (asset code in the note; exclusions marked as open markers in
F6) should extend to any new figure.

**Data-ink in tables: the number is the ink.** Two consequences:
1. Alignment — numerals are right-aligned/decimal-aligned in all thesis
   tables (p- and c-columns verified in the visual pass). Preserve when
   editing columns.
2. Units live in headers ("(NPR)", "(%)"), never inside cells — so
   cells stay comparable. Keep.

## 5. The binding checklist for any new number, table, or figure

1. Exact p to three decimals, with df and tail named.
2. SE under every estimate, under the named covariance (HC3) and df.
3. CI for anything interpreted as a magnitude range.
4. Magnitude sentence (economic units) separate from significance
   sentence (level).
5. Mechanism sentence only in the labeled "Plausible Mechanism" frame.
6. Exclusions and sample changes stated where the sample changes.
7. Display: booktabs rules only; axis ticks labeled; palette unchanged;
   caption states what the display is NOT (fit lines ≠ model estimates).
8. Source note names the aggregator status (ShareSansar-derived; NEPSE
   closes unverified) wherever prices appear.
