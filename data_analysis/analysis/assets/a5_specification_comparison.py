"""A5: specification comparison — pooled OLS vs bank fixed effects vs two-way
fixed effects for the baseline value-relevance model.  Shows what the fixed
effects contribute before the interactions of Model 2 (methodology step 5:
"compare against pooled OLS and bank-only FE").
"""
from __future__ import annotations

from analysis.dataset import AnalysisDataset
from analysis.render.tables import Table, save_table
from analysis.stats.models import fit_bank_fe, fit_model1, fit_pooled


def generate(dataset: AnalysisDataset) -> list:
    panel = dataset.panel
    fits = [
        fit_pooled(panel, "Pooled OLS (no FE)"),
        fit_bank_fe(panel, "Bank FE only"),
        fit_model1(panel, "Two-way FE (Model 1)"),
    ]
    rows = tuple(
        (
            fit.label,
            f"{fit.term('eps').coef:.3f} ({fit.term('eps').se:.3f})",
            f"{fit.term('bvps').coef:.3f} ({fit.term('bvps').se:.3f})",
            f"{fit.rsquared:.3f}",
            str(fit.nobs),
        )
        for fit in fits
    )
    table = Table(
        id="A5_specification_comparison",
        caption="Specification comparison: pooled OLS, bank FE and two-way FE",
        headers=("Specification", "beta(EPS)", "beta(BVPS)", "R2", "n"),
        rows=rows,
        notes=(
            "HC3 robust standard errors in parentheses. Two-way FE adds fiscal-year dummies "
            "to the bank fixed effects; this is Model 1, the baseline carried into Model 2."
        ),
    )
    return save_table(table, "tables/A5_specification_comparison")
