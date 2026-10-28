"""Statistics: coefficient recovery on the synthetic DGP, the joint Wald test,
diagnostics, and the sanity gate against the exploratory numpy audit numbers.
"""
from __future__ import annotations

import numpy as np
import pytest

from analysis.dataset import build_dataset
from analysis.stats.diagnostics import breusch_pagan, cooks_distance, vif_table
from analysis.stats.models import fit_bank_fe, fit_model1, fit_model2, fit_pooled
from analysis.stats.robustness import build_runs
from analysis.stats.wald import joint_zero_test
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
    planted.loc[post, "price"] = planted.loc[post, "price"] + planted_delta * planted.loc[post, "eps"]
    fit = fit_model2(planted)
    assert fit.term("eps:post").coef == pytest.approx(planted_delta, abs=0.6)
    wald = joint_zero_test(fit.results, ("eps:post", "bvps:post"))
    assert wald.p_value < 0.05


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
    bp = breusch_pagan(fit.results)
    assert 0.0 <= bp.lm_pvalue <= 1.0
    cooks = cooks_distance(fit.results)
    assert cooks.shape == (28,)
    assert np.isfinite(cooks).all()


def test_robustness_runs_cover_methodology_step4(synthetic_study) -> None:
    ds = build_dataset(strict=True)
    runs = build_runs(ds)
    assert [run.id for run in runs] == ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]
    by_id = {run.id: run for run in runs}
    assert by_id["R3"].earnings_term == "roa"
    assert by_id["R7"].bvps_term == "bvps_adj"
    assert by_id["R5"].result.nobs == 23  # 28 - 5 transition-year rows
    assert by_id["R6"].result.nobs == 23  # 28 - 5 entity-mismatch-year rows
    assert by_id["R8"].result.nobs == 28


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
