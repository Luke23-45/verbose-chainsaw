"""T5: robustness suite (methodology step 4) — every specification re-fitted
from the same analysis frame, reported side by side with the two baselines.

R1/R2 baselines; R3 ROA-for-EPS; R4 +DPS; R5 excludes the transition year
FY2079-80; R6 excludes FY2078-79 (entity mismatch); R7 bonus-adjusted BVPS;
R8 restated EPS (as printed, rows flagged).
"""
from __future__ import annotations

import numpy as np

from analysis.dataset import AnalysisDataset
from analysis.render.tables import Table, save_table
from analysis.stats.robustness import RobustnessRun, build_runs, interaction_terms
from analysis.stats.wald import joint_zero_test
from analysis.assets.t3_model1 import _pfmt


def _combo(fit, constraint: str) -> tuple[float, float]:
    """(estimate, HC3 SE) of a linear combination of coefficients."""
    test = fit.results.t_test(constraint)
    effect = float(np.asarray(test.effect, dtype=float).ravel()[0])
    se = float(np.asarray(test.sd, dtype=float).ravel()[0])
    return effect, se


def _run_row(run: RobustnessRun) -> tuple[str, ...]:
    earnings = run.earnings()
    bvps = run.bvps()
    if run.has_deltas():
        delta_e_name, delta_b_name = interaction_terms(run)
        delta_e = run.result.term(delta_e_name)
        delta_b = run.result.term(delta_b_name)
        wald = joint_zero_test(run.result.results, (delta_e_name, delta_b_name))
        wald_cell = f"{wald.f_stat:.2f} ({_pfmt(wald.p_value)})"
        delta_e_cell = f"{delta_e.coef:.3f} ({delta_e.se:.3f})"
        delta_b_cell = f"{delta_b.coef:.3f} ({delta_b.se:.3f})"
    else:
        wald_cell = "n/a"
        delta_e_cell = "n/a"
        delta_b_cell = "n/a"
    return (
        f"{run.id} {run.label}",
        f"{earnings.coef:.3f} ({earnings.se:.3f})",
        f"{bvps.coef:.3f} ({bvps.se:.3f})",
        delta_e_cell,
        delta_b_cell,
        wald_cell,
        str(run.result.nobs),
    )


def generate(dataset: AnalysisDataset) -> list:
    runs = build_runs(dataset)
    rows = tuple(_run_row(run) for run in runs)
    notes = "; ".join(f"{run.id}: {run.note}" for run in runs if run.note != "baseline reference")
    table = Table(
        id="T5_robustness",
        caption=(
            "Robustness of the value-relevance estimates across specifications "
            "(earnings and BVPS coefficients, consolidation interactions, joint Wald F)"
        ),
        headers=(
            "Specification",
            "Earnings coef (SE)",
            "BVPS coef (SE)",
            "delta(E) (SE)",
            "delta(B) (SE)",
            "Joint Wald F (p)",
            "n",
        ),
        rows=rows,
        notes=(
            "All coefficients estimated by OLS with bank and fiscal-year fixed effects and "
            "HC3 standard errors (SE in parentheses); the Wald F tests H0: delta_E = "
            "delta_B = 0 under the HC3 covariance. " + notes
        ),
    )
    return save_table(table, "tables/T5_robustness")
