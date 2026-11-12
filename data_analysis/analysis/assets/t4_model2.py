"""T4: Model 2 estimates — consolidation interactions and the joint Wald test
(methodology step 3; hypotheses H3, H4 and the principal joint null
H0: delta_E = delta_B = 0).

Implied post slopes are the linear combinations beta + delta, tested with
HC3-robust t-contrasts.
"""
from __future__ import annotations

from analysis.dataset import AnalysisDataset
from analysis.render.tables import Table, save_table
from analysis.stats.models import TermEstimate, fit_model2, linear_combination
from analysis.stats.wald import joint_zero_test
from analysis.assets.t3_model1 import _pfmt  # shared p formatting


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
    fit = fit_model2(dataset.panel, "Model 2")
    eps = fit.term("eps")
    bvps = fit.term("bvps")
    delta_e = fit.term("eps:post")
    delta_b = fit.term("bvps:post")
    post_e = linear_combination(fit, "eps + eps:post = 0")
    post_b = linear_combination(fit, "bvps + bvps:post = 0")
    wald = joint_zero_test(fit.results, ("eps:post", "bvps:post"))
    rows = [
        _row(eps, "beta(EPS), pre slope"),
        _row(bvps, "beta(BVPS), pre slope"),
        _row(delta_e, "delta(EPS x Post)"),
        _row(delta_b, "delta(BVPS x Post)"),
        _row(post_e, "Post slope EPS (beta+delta)"),
        _row(post_b, "Post slope BVPS (beta+delta)"),
        ("Joint Wald F (H0: delta_E = delta_B = 0)", f"F = {wald.f_stat:.3f}", "", "",
         _pfmt(wald.p_value), f"df ({wald.df_num:.0f}, {wald.df_den:.0f})"),
        ("n", str(fit.nobs), "", "", "", ""),
        ("R2", f"{fit.rsquared:.3f}", "", "", "", ""),
        ("Adj. R2", f"{fit.rsquared_adj:.3f}", "", "", "", ""),
        ("Within-R2", f"{fit.within_rsquared:.3f}", "", "", "", ""),
        ("df (residual)", f"{fit.df_resid:.0f}", "", "", "", ""),
    ]
    table = Table(
        id="T4_model2",
        caption=(
            "Model 2: MPS_RD on EPS, BVPS and their post-consolidation interactions, "
            "with bank and fiscal-year fixed effects"
        ),
        headers=("Term", "Coefficient", "HC3 SE", "t", "p", "95% CI"),
        rows=tuple(rows),
        notes=(
            "Post = 1 from FY2079/80 onward; the Post main effect is absorbed by the year "
            "fixed effects (proposal eq. 2). Post slopes are linear combinations beta + "
            "delta tested under the HC3 covariance. The principal test is the joint Wald F "
            "of H0: delta_E = delta_B = 0; the joint Wald F is an upper-tail test at 5%; "
            "exploratory, non-causal framing."
        ),
    )
    return save_table(table, "tables/T4_model2")
