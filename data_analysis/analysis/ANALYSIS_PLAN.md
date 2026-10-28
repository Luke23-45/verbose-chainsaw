# Analysis plan — figures and tables (v1.1, 2026-10-28)

Versioned design document for every asset in `assets/__init__.py::ASSET_REGISTRY`.
The registry implements this plan; any registry change must be reflected here
(and vice versa), following the PhaseForge precedent of recording design
adjustments instead of silently diverging.

## Data inventory (verified 2026-10-28)

- Primary panel: `../data_extract/output/manual_review/mps_rd_joined_panel.csv`
  — 30 bank-years (5 banks x 6 FYs), columns `bank, fy, post, price, price_date,
  gap, eps, bvps, dps, roa, entity_mismatch`.
- Analysis sample: 28 realized (13 pre, 15 post).  Window-excluded under the
  5-day rule (never imputed): HBL FY2077-78 (gap 54), NIMB FY2077-78 (gap 47).
  Entity mismatch FY2078-79 (pre-merger fundamentals vs post-merger April 2023
  price, kept in baseline): GBIME, HBL, KBL, NIMB.
- Companion inputs: bonus-adjusted panel (`bvps_adj = BVPS / (1 + bonus%)`),
  price-status table (clean / DELAYED), Merolagani LTP cross-check
  (29/30 match; NMB FY2076-77 resolved by third source at 437.00).
- Restated EPS (final audit 2026-10-27, note a): GBIME FY2076-77 17.99 -> 15.33,
  NMB FY2077-78 16.66 -> 14.76; HBL FY2077-78 28.07 -> 27.60 sits in a dropped
  row.  Values are used as printed and the substituted rows flagged — no
  mechanical restatement rule may be invented.

## Sanity gate (passed)

The statsmodels pipeline reproduces the exploratory numpy audit of
2026-10-27 (section 5) on the real panel; this is pinned as
`tests/test_stats.py::test_sanity_gate_against_exploratory_audit`:

- Model 1: R2 = 0.948, beta(EPS) = 2.095 (HC3 SE 4.096), beta(BVPS) = 0.219.
- Model 2: R2 = 0.978, delta_E = -3.124, delta_B = -1.758.
- Joint Wald F(2, 14) = 2.954, p = 0.085 — H0: delta_E = delta_B = 0 is NOT
  rejected under HC3 at the 5% level.

## Design principles

1. Every number in the thesis comes from this pipeline — no manual edits.
2. HC3 inference everywhere the proposal designates it; classical statistics
   only as secondary disclosure.
3. Okabe-Ito palette, fixed semantic colors: pre = blue, post = vermillion,
   delta = orange.  Twin outputs: figures PDF + PNG (300 dpi, fonts embedded),
   tables booktabs `.tex` + markdown `.md`, written atomically.
4. Exploratory, non-causal wording in every caption and notes block.
5. Fail-closed: assets refuse to render on structural surprises; one failed
   asset does not abort the run (`generate` collects failures, exit 1).

## Registry (18 assets)

| ID | Kind | Section | Priority | Content |
|----|------|---------|----------|---------|
| T1 | table | main | P0 | Descriptives: mean/SD/min/max per variable x {full, pre, post} |
| T2 | table | main | P0 | Pearson correlations, lower triangle, significance stars, EPS-ROA caveat |
| T3 | table | main | P0 | Model 1 estimates: beta_E, beta_B, HC3 SE/t/p, 95% CI, R2, df |
| T4 | table | main | P0 | Model 2: deltas, implied post slopes (t-contrasts), joint Wald F |
| T5 | table | main | P0 | Robustness suite R1-R8: one row per specification |
| T6 | table | main | P1 | Model 1 diagnostics: VIF/tolerance, Breusch-Pagan, Cook's D vs 4/n |
| F1 | figure | main | P1 | Seaborn scatter matrix of MPS_RD/EPS/BVPS, hue = period |
| F2 | figure | main | P1 | Correlation heatmap, diverging Okabe-Ito scale |
| F3 | figure | main | P0 | MPS_RD vs EPS and vs BVPS, per-period OLS fit lines |
| F4 | figure | main | P0 | Coefficient forest: pre slopes, deltas, implied post slopes (H1-H4 visual) |
| F5 | figure | main | P1 | Model 1 diagnostics panel: Q-Q, resid-vs-fitted, scale-location, Cook's D |
| F6 | figure | main | P1 | Variable trends by bank series, post-consolidation years shaded; window-excluded prices shown as open markers |
| A1 | figure | appendix | P1 | Coverage map 5x6: realized / mismatch / window-excluded (gap days) / absent |
| A2 | figure | appendix | P1 | Robustness forest, EPS channel: beta(EPS) and delta(EPS x Post) per specification |
| A3 | figure | appendix | P2 | Model 2 diagnostics panel (shared renderer with F5) |
| A4 | table | appendix | P2 | Price verification: dataset close vs Merolagani LTP, outcome per bank-year |
| A5 | table | appendix | P2 | Specification comparison: pooled OLS vs bank FE vs two-way FE |
| A6 | table | appendix | P2 | Analysis dataset: all 30 bank-years with exclusion/mismatch/restatement notes |

## Recorded design adjustments

v1.0:
- The original plan folded the pooled-OLS / bank-FE / two-way-FE comparison
  into T6; it moved to its own appendix asset (A5) so T6 stays a
  single-purpose diagnostics table.
- Bonus-adjusted estimates live inside T5 as row R7 rather than as a separate
  asset; the fuller bonus-adjusted breakdown of the 2026-10-27 audit (note a)
  can be added as A6 if the supervisor asks for it.
- Merolagani verification is rendered from the verification CSV joined on
  (bank, price_date) with the pre-merger `NIB` symbol mapped to `NIMB`; the
  join must cover every bank-year or the asset raises.

v1.1 (visual audit pass, 2026-10-28):
- A2 redesigned: the first draft plotted the earnings coefficient across all
  eight robustness runs in one panel, but R3's ROA coefficient (measured per
  percentage point, CI roughly -230 to +260 NPR) flattened every other row
  into illegibility.  A2 now shows the EPS channel only (beta(EPS) and
  delta(EPS x Post) across R1, R2, R4-R8) with R3's omission footnoted on the
  figure and its numbers carried by T5.
- F6 added (variable trends by bank series, post years shaded, window-excluded
  prices as open markers) and A6 added (full 30-row analysis dataset with
  exclusion / mismatch / restatement notes) — standard descriptive elements a
  thesis of this type is expected to carry.
- Diagnostics panels (F5/A3): the scale-location y-label mathtext was broken
  and the Cook's-distance annotation collided with the 4/n line; the label is
  fixed and the threshold value moved into the panel title.
- F3: the right panel's y-axis label was seaborn's raw column name
  (`price_rd`); both panels now label MPS_RD (NPR) and the legend moved clear
  of the data.
