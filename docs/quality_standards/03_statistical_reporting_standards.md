# 03 — Statistical reporting standards

The reference standard is Wilkinson, L., & the Task Force on Statistical
Inference (1999), *American Psychologist, 54*(8), 594–604 — report
effect sizes and confidence intervals, exact p values, and enough
descriptive detail for an independent reader to re-derive every number —
plus the APA Style numbers-and-statistics conventions (exact p to two or
three decimals; CIs in brackets; italic test letters, upright Greek).

This thesis already implements most of it. This file records the
standard, where the thesis meets it, and the watch items.

---

## 1. What every reported model must carry (Wilkinson/TFSI)

For each estimate: the coefficient, its standard error, the test
statistic with degrees of freedom, the exact p value, and (where
interpreted) a confidence interval. Status in this thesis:

- **Met.** Tables 5 and 6 print coefficients with HC3 SEs beneath;
  t, p, and 95% CIs appear in the running text (§4.2.3 point 2: CI
  [−6.587, 10.777] with t(16); §4.2.4: CI [−2.059, 13.213] with t(14)).
- **Implied linear combinations get their own SE/t/p** — the implied
  post-consolidation slopes in Table 6 (2.453, SE 2.269, t 1.08, p
  0.298) are evaluated under the HC3 covariance, stated in the table
  note. This is exactly the TFSI discipline for derived quantities.
- **Residual df are derived, not asserted** — the parameter-count
  arithmetic (28 − 12 = 16; 28 − 14 = 14; R4 13; R5/R6 10) is printed
  in §3.6.1/§3.6.2 and the table notes.

## 2. p-value reporting rules

- Report exact p values to two–three decimals: the thesis prints
  p = 0.616, 0.908, 0.140, 0.940, 0.448, 0.175, 0.085, 0.021 — all
  three-decimal, all consistent between text, tables, and Table 11.
  Status: *met.*
- For values near the threshold, name the threshold and the tail: the
  thesis says "two-tailed tests at α = 0.05" for t-tests and
  "right-tail F-test" for the joint Wald test (Table 6 note, Table 7
  note). Status: *met* — the earlier "Wald tests called two-tailed"
  error is fixed.
- Marginal results are labeled by the level that applies: "does not
  reject ... at the 5% level, though it achieves marginal significance
  at the 10% level" (§4.2.4 point 4). The rule this implements: never
  write "almost significant" or "marginally failed to reject" — name
  the level, state the decision. Keep it.
- Rounding at the threshold: F = 2.95 in Table 7's summary row vs
  F = 2.954 in Table 6 and the text. Two-decimal vs three-decimal
  renderings of the same statistic coexist; harmless but pick three
  decimals everywhere if touching those lines.

## 3. Effect size and economic magnitude (TFSI: never p alone)

- The thesis interprets magnitudes, not just significance: "each
  additional NPR 1.00 of reported earnings per share is associated with
  an incremental NPR 2.10 in post-deadline market share price"
  (§4.2.3 point 1); "equity investors priced commercial bank shares at
  approximately 5.58 times reported earnings" (§4.2.4). This is the
  economic-magnitude discipline TFSI asks for. Status: *met.*
- R² alone never carries an argument: §4.2.7 decomposes the pooled vs
  two-way FE gap (0.136 → 0.948) and attributes it to absorbed
  macro-year variation, and Chapter V repeats the pooled-slope
  attenuation (4.882 → 2.095). Status: *met.*
- VIF as a collinearity statement is reported with its derivation
  (r = 0.975; VIF = 1/(1 − r²) ≈ 20). Status: *met after the 2026-11-02
  unification.*

## 4. Descriptives for replication (TFSI: means, SDs, Ns, exact n)

- Table 3 (descriptives) carries n, mean, SD, min, max for every
  variable × sub-period; the analysis sample's construction (30 target,
  2 excluded by rule, N = 28, 13/15 split) is stated in Chapters I, III,
  IV, and V. Status: *met.*
- The excluded observations are named with their exclusion quantities
  (54 and 47 days) rather than hidden. Status: *met.*

## 5. Robustness presentation

- The robustness suite reports the same coefficient/SE/Wald columns for
  every specification (Table 8), names the sample change for each
  (R5/R6 N = 23, df 10), and prints the one significant cell in bold
  with an explicit asterisk note. Status: *met.*
- The narrative rule: a specification "preserves the structural
  pattern" / "leaves the baseline conclusions intact" — pattern
  language, not confirmation language. Status: *met* (§4.2.6 points
  1–6). Keep "is consistent with" for any new robustness sentence.
- Sensitivity framing in conclusions: "sensitivity-dependent rather
  than conclusive in the baseline" (§5.3.2, §5.3.6 point 5). This is
  the exact phrasing to reuse; do not abbreviate it to "confirmed in
  R6".

## 6. Watch items (small, listed so they are not lost)

1. F = 2.95 (Table 7 row) vs F = 2.954 (Table 6, text, Table 11) —
   three-decimal rendering would be uniform.
2. Figure 2's in-asset fonts (axis labels and the asset's footnote line)
   render small at 0.92\textwidth; a regeneration would raise them, but
   the assets are declared legacy — leave unless the pipeline is run
   again for other reasons.
3. The A2 asset's printed footnote says "its estimates are in T5" —
   internal asset naming; the thesis Note beneath the figure already
   restates the R3 omission in thesis terms. Asset-side only; not a
   thesis-text defect.
4. When any table is regenerated, T2's asset note ("variance inflation
   ~ 30") must be corrected in the asset first, or the regenerated
   table will contradict the chapters' "approximately 20".
