"""Dataset rules: coverage, the short-window rule, and fail-closed validation."""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from analysis.common import config
from analysis.dataset import Cell, build_dataset


def test_coverage_and_window_rule(synthetic_study) -> None:
    ds = build_dataset(strict=True)
    coverage = ds.coverage
    assert coverage.intended == 30
    assert coverage.realized == 28
    assert (coverage.realized_pre, coverage.realized_post) == (13, 15)
    assert set(coverage.window_excluded_cells) == {
        Cell("HBL", "FY2077-78"),
        Cell("NIMB", "FY2077-78"),
    }
    assert len(ds.panel_all) == 30
    assert len(ds.panel) == 28


def test_window_excluded_prices_are_never_imputed(synthetic_study) -> None:
    ds = build_dataset(strict=True)
    for bank, fy in (("HBL", "FY2077-78"), ("NIMB", "FY2077-78")):
        row = ds.cell(bank, fy)
        assert not row.in_sample
        assert np.isnan(row.price_rd)
        assert not np.isnan(row.price)  # raw price kept for traceability


def test_period_labels_match_post_flag(synthetic_study) -> None:
    ds = build_dataset(strict=True)
    frame = ds.panel
    assert (frame.loc[frame["post"] == 1, "period"] == "post").all()
    assert (frame.loc[frame["post"] == 0, "period"] == "pre").all()
    assert frame["entity_mismatch"].sum() == 4  # merged banks, FY2078-79


def test_restated_eps_substitution_is_flagged(synthetic_study) -> None:
    ds = build_dataset(strict=True)
    flagged = ds.restated.loc[ds.restated["eps_is_restated"]]
    assert list(zip(flagged["bank"], flagged["fy"])) == [("GBIME", "FY2076-77")]
    expected = float(synthetic_study["panel"].loc[0, "eps"]) + 1.0
    assert flagged.iloc[0]["eps"] == pytest.approx(expected)
    assert ds.restated["eps_is_restated"].sum() == 1


def test_duplicate_cell_raises(synthetic_study) -> None:
    panel = synthetic_study["panel"]
    data_dir = synthetic_study["data_dir"]
    pd.concat([panel, panel.iloc[[0]]]).to_csv(data_dir / "panel.csv", index=False)
    with pytest.raises(ValueError, match="duplicate bank-year cells"):
        build_dataset(strict=True)


def test_unknown_bank_raises(synthetic_study) -> None:
    panel = synthetic_study["panel"].copy()
    panel.loc[0, "bank"] = "SCBL"
    panel.to_csv(synthetic_study["data_dir"] / "panel.csv", index=False)
    with pytest.raises(ValueError, match="unknown bank/fy"):
        build_dataset(strict=True)


def test_post_flag_disagreement_raises(synthetic_study) -> None:
    panel = synthetic_study["panel"].copy()
    panel.loc[0, "post"] = 1  # GBIME FY2076-77 marked post
    panel.to_csv(synthetic_study["data_dir"] / "panel.csv", index=False)
    with pytest.raises(ValueError, match="post flag disagrees"):
        build_dataset(strict=True)


def test_absent_cell_strict_and_lenient(synthetic_study) -> None:
    panel = synthetic_study["panel"]
    data_dir = synthetic_study["data_dir"]
    panel.drop(index=[0]).to_csv(data_dir / "panel.csv", index=False)
    with pytest.raises(ValueError, match="absent bank-year cells"):
        build_dataset(strict=True)
    ds = build_dataset(strict=False)
    assert ds.coverage.realized == 27
    assert ds.coverage.absent_cells[0] == Cell("GBIME", "FY2076-77")


def test_price_status_disagreement_raises(synthetic_study) -> None:
    status = pd.read_csv(synthetic_study["data_dir"] / "price_status.csv")
    status.loc[status["status"] != "clean", "status"] = "clean"  # panel keeps 2 delayed
    status.to_csv(synthetic_study["data_dir"] / "price_status.csv", index=False)
    with pytest.raises(ValueError, match="DELAYED cells disagree"):
        build_dataset(strict=True)


def test_bonusadj_value_drift_raises(synthetic_study) -> None:
    bonus = pd.read_csv(synthetic_study["data_dir"] / "bonusadj.csv")
    bonus.loc[0, "eps"] = float(bonus.loc[0, "eps"]) + 5.0
    bonus.to_csv(synthetic_study["data_dir"] / "bonusadj.csv", index=False)
    with pytest.raises(ValueError, match="disagrees with the primary panel"):
        build_dataset(strict=True)


def test_config_redirect_is_active(synthetic_study) -> None:
    assert config.get_config()["data"]["root"] == str(synthetic_study["data_dir"])
