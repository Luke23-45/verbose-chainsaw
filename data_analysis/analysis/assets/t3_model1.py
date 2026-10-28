"""T3: Model 1 estimates — MPS_RD on EPS and BVPS with two-way fixed effects
and HC3 inference (methodology step 2; hypotheses H1 and H2).

beta(EPS) and beta(BVPS) are the proposal's beta_E and beta_B.
"""
from __future__ import annotations

from analysis.dataset import AnalysisDataset
from analysis.render.tables import Table, save_table
from analysis.stats.models import TermEstimate, fit_model1


def _pfmt(p: float) -> str:
    return "<0.001" if p < 0.001 else f"{p:.3f}"


def _row(est: TermEstimate, name: str) -> tuple[str, ...]:
    return (
        name,
        f"{est.coef:.3f}",
        f"{est.se:.3f}",
        f"{est.tvalue:.2f}",
        _pfmt(est.pvalue),
        f"[{est.ci_low:.3f}, {est.ci_high:.3f}]",
    )


def generate(dataset: AnalysisDataset) -> list:
    fit = fit_model1(dataset.panel, "Model 1")
    rows = [
        _row(fit.term("eps"), "beta(EPS)"),
        _row(fit.term("bvps"), "beta(BVPS)"),
        ("Bank FE", "Yes", "", "", "", ""),
        ("Year FE", "Yes", "", "", "", ""),
        ("n", str(fit.nobs), "", "", "", ""),
        ("R2", f"{fit.rsquared:.3f}", "", "", "", ""),
        ("Adj. R2", f"{fit.rsquared_adj:.3f}", "", "", "", ""),
        ("df (residual)", f"{fit.df_resid:.0f}", "", "", "", ""),
    ]
    table = Table(
        id="T3_model1",
        caption=(
            "Model 1: MPS_RD on EPS and BVPS with bank and fiscal-year fixed effects "
            "(baseline value-relevance model)"
        ),
        headers=("Term", "Coefficient", "HC3 SE", "t", "p", "95% CI"),
        rows=tuple(rows),
        notes=(
            "OLS with bank (mu_i) and fiscal-year (lambda_t) fixed effects; MacKinnon-White "
            "HC3 robust standard errors (G = 5 banks is too few for cluster-robust inference). "
            "Two-tailed tests at the 5% level. Exploratory: associations, not causal effects."
        ),
    )
    return save_table(table, "tables/T3_model1")
