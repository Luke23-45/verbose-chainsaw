"""Statistics: coefficient recovery on the synthetic DGP, the joint Wald test,
diagnostics, and the sanity gate against the exploratory numpy audit numbers.
"""
from __future__ import annotations

import numpy as np
import pytest
import statsmodels.formula.api as smf

from analysis.dataset import build_dataset
from analysis.stats.diagnostics import breusch_pagan, cooks_distance, vif_table
from analysis.stats.models import BANK_FE, FY_FE, MODEL1_FORMULA, fit_bank_fe, fit_model1, fit_model2, fit_pooled, linear_combination
from analysis.stats.robustness import build_runs, post_slopes
from analysis.stats.wald import joint_zero_test
from analysis.stats.wild_bootstrap import rademacher_patterns, wild_cluster_bootstrap_wald
from tests.conftest import BVPS_SLOPE, EPS_SLOPE


def test_model1_recovers_planted_slopes(synthetic_study) -> None:
    ds = build_dataset(strict=True)
    fit = fit_model1(ds.panel)
    eps = fit.term("eps")
    bvps = fit.term("bvps")
    assert eps.coef == pytest.approx(EPS_SLOPE, abs=0.35)
    assert bvps.coef == pytest.approx(BVPS_SLOPE, abs=0.06)
    assert eps.ci_low < EPS_SLOPE < eps.ci_high
    assert bvps.ci_low < BVPS_SLOPE < bvps.ci_high


def test_model2_planted_delta_recovered_and_wald_rejects(synthetic_study) -> None:
    ds = build_dataset(strict=True)
    planted = ds.panel.copy()
    planted_delta = 3.0
    post = planted["post"] == 1
    planted.loc[post, "price_rd"] = planted.loc[post, "price_rd"] + planted_delta * planted.loc[post, "eps"]
    fit = fit_model2(planted)
    assert fit.term("eps:post").coef == pytest.approx(planted_delta, abs=0.6)
    wald = joint_zero_test(fit.results, ("eps:post", "bvps:post"))
    assert wald.p_value < 0.05


def test_post_slope_linear_combination_uses_hc3_covariance(synthetic_study) -> None:
    ds = build_dataset(strict=True)
    fit = fit_model2(ds.panel)
    post_eps = linear_combination(fit, "eps + eps:post = 0")
    assert post_eps.coef == pytest.approx(fit.term("eps").coef + fit.term("eps:post").coef)
    assert post_eps.se > 0
    assert 0 <= post_eps.pvalue <= 1
    assert post_eps.ci_low < post_eps.coef < post_eps.ci_high


def test_wald_does_not_reject_when_no_deltas_planted(synthetic_study) -> None:
    ds = build_dataset(strict=True)
    fit = fit_model2(ds.panel)
    wald = joint_zero_test(fit.results, ("eps:post", "bvps:post"))
    assert wald.p_value > 0.05


def test_specification_family(synthetic_study) -> None:
    ds = build_dataset(strict=True)
    pooled = fit_pooled(ds.panel)
    bank = fit_bank_fe(ds.panel)
    two_way = fit_model1(ds.panel)
    assert two_way.rsquared > bank.rsquared > pooled.rsquared
    assert two_way.nobs == bank.nobs == pooled.nobs == 28


def test_diagnostics_shapes(synthetic_study) -> None:
    ds = build_dataset(strict=True)
    fit = fit_model1(ds.panel)
    vifs = vif_table(ds.panel, ("eps", "bvps"))
    assert [row.term for row in vifs] == ["eps", "bvps"]
    assert all(row.vif > 1.0 and 0 < row.tolerance <= 1.0 for row in vifs)
    model2_frame = ds.panel.assign(
        eps_post=ds.panel["eps"] * ds.panel["post"],
        bvps_post=ds.panel["bvps"] * ds.panel["post"],
    )
    model2_vifs = vif_table(
        model2_frame, ("eps", "bvps", "eps_post", "bvps_post")
    )
    assert [row.term for row in model2_vifs] == ["eps", "bvps", "eps_post", "bvps_post"]
    bp = breusch_pagan(fit.results)
    assert 0.0 <= bp.lm_pvalue <= 1.0
    cooks = cooks_distance(fit.results)
    assert cooks.shape == (28,)
    assert np.isfinite(cooks).all()


def test_robustness_runs_cover_methodology_step4(synthetic_study) -> None:
    ds = build_dataset(strict=True)
    runs = build_runs(ds)
    assert [run.id for run in runs] == ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"]
    by_id = {run.id: run for run in runs}
    assert by_id["R3"].earnings_term == "roa"
    assert by_id["R7"].bvps_term == "bvps_adj"
    assert by_id["R5"].result.nobs == 23  # 28 - 5 transition-year rows
    assert by_id["R6"].result.nobs == 23  # 28 - 5 entity-mismatch-year rows
    assert by_id["R8"].result.nobs == 28
    assert by_id["R9"].result.nobs == 27


def test_within_r_squared_is_partial_r_squared_for_two_way_fe(synthetic_study) -> None:
    ds = build_dataset(strict=True)
    fit = fit_model2(ds.panel)
    fe_only = smf.ols(f"price_rd ~ {BANK_FE} + {FY_FE}", data=ds.panel).fit()
    expected = 1.0 - fit.results.ssr / fe_only.ssr
    assert fit.within_rsquared == pytest.approx(expected)
    assert 0.0 <= fit.within_rsquared <= 1.0


def test_sanity_gate_against_exploratory_audit() -> None:
    """Reproduce the exploratory numpy audit (mps_rd_final_audit_2026-10-27,
    section 5) from the real panel before any asset may render: Model 1
    R2 ~ 0.948 with beta(EPS) ~ 2.095 and beta(BVPS) ~ 0.219; Model 2 R2 ~
    0.978 with delta_E ~ -3.124 and delta_B ~ -1.758; no joint rejection."""
    ds = build_dataset(strict=True)
    m1 = fit_model1(ds.panel)
    assert m1.nobs == 28
    assert m1.rsquared == pytest.approx(0.948, abs=0.005)
    assert m1.term("eps").coef == pytest.approx(2.095, abs=0.05)
    assert m1.term("bvps").coef == pytest.approx(0.219, abs=0.05)
    m2 = fit_model2(ds.panel)
    assert m2.rsquared == pytest.approx(0.978, abs=0.005)
    assert m2.term("eps:post").coef == pytest.approx(-3.124, abs=0.05)
    assert m2.term("bvps:post").coef == pytest.approx(-1.758, abs=0.05)
    wald = joint_zero_test(m2.results, ("eps:post", "bvps:post"))
    assert wald.p_value > 0.05  # H0 not rejected under HC3


def test_robustness_post_slopes_match_review_recomputation() -> None:
    """s2: post slopes for the robustness specs, verified against the review's
    own recomputation (R5/R6) and the thesis Table 6 (R2). All post slopes
    keep the baseline signs (EPS positive, BVPS negative) and none is
    significant."""
    ds = build_dataset(strict=True)
    runs = build_runs(ds)
    by_id = {run.id: run for run in runs}
    post_eps_r2, post_bvps_r2 = post_slopes(by_id["R2"])
    assert post_eps_r2.coef == pytest.approx(2.453, abs=0.001)
    assert post_bvps_r2.coef == pytest.approx(-1.658, abs=0.001)
    post_eps_r5, post_bvps_r5 = post_slopes(by_id["R5"])
    assert post_eps_r5.coef == pytest.approx(3.415, abs=0.001)
    assert post_eps_r5.pvalue == pytest.approx(0.401, abs=0.001)
    assert post_bvps_r5.coef == pytest.approx(-2.081, abs=0.001)
    assert post_bvps_r5.pvalue == pytest.approx(0.315, abs=0.001)
    post_eps_r6, post_bvps_r6 = post_slopes(by_id["R6"])
    assert post_eps_r6.coef == pytest.approx(1.900, abs=0.001)
    assert post_eps_r6.pvalue == pytest.approx(0.490, abs=0.001)
    assert post_bvps_r6.coef == pytest.approx(-1.809, abs=0.001)
    assert post_bvps_r6.pvalue == pytest.approx(0.212, abs=0.001)
    for rid in ("R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"):
        post_e, post_b = post_slopes(by_id[rid])
        assert post_e.coef > 0 and post_b.coef < 0
        assert post_e.pvalue > 0.05 and post_b.pvalue > 0.05
    with pytest.raises(ValueError):
        post_slopes(by_id["R1"])  # Model 1 has no interactions


def test_wild_cluster_bootstrap_is_deterministic_and_coarse() -> None:
    """s1: wild-cluster bootstrap of the HC3 joint Wald test, enumerating all
    2**5 = 32 Rademacher patterns at G = 5 banks. The bootstrap p-value is a
    multiple of 1/32; the all-+1 and all−1 patterns both reproduce the observed
    statistic in exact arithmetic, so at least two patterns always count."""
    ds = build_dataset(strict=True)
    runs = build_runs(ds)
    by_id = {run.id: run for run in runs}
    assert len(rademacher_patterns(5)) == 32
    assert rademacher_patterns(5)[0] == (1, 1, 1, 1, 1)
    m2 = by_id["R2"]
    res = wild_cluster_bootstrap_wald(
        m2.result, ds.panel, MODEL1_FORMULA, ("eps:post", "bvps:post")
    )
    assert res.n_boot == 32 and res.n_clusters == 5
    assert res.observed_f == pytest.approx(2.954481, abs=1e-6)
    assert res.bootstrap_p == pytest.approx(2 / 32)
    assert res.n_exceed == 2
    res_again = wild_cluster_bootstrap_wald(
        m2.result, ds.panel, MODEL1_FORMULA, ("eps:post", "bvps:post")
    )
    assert res_again.bootstrap_p == res.bootstrap_p
    r6_frame = ds.panel[ds.panel["fy"] != "FY2078-79"]
    r6 = by_id["R6"]
    res6 = wild_cluster_bootstrap_wald(
        r6.result, r6_frame, MODEL1_FORMULA, ("eps:post", "bvps:post")
    )
    assert res6.observed_f == pytest.approx(5.817708, abs=1e-6)
    assert res6.bootstrap_p == pytest.approx(2 / 32)
    assert res6.n_exceed == 2
