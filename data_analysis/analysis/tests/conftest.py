"""Fixtures: a synthetic 30-row study mirroring the real panel's structure.

The synthetic config redirects both the data root and the output root into
tmp_path via the THESIS_ANALYSIS_CONFIG environment variable (with the config
cache cleared), so the real inputs are never touched by the test suite.  The
synthetic DGP plants known slopes (price = 2.5*EPS + 0.6*BVPS + bank effect +
year effect + noise) and the same two delayed bank-years as the real data.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import yaml

from analysis.common import config

BANKS = ["GBIME", "HBL", "KBL", "NIMB", "NMB"]
FYS = ["FY2076-77", "FY2077-78", "FY2078-79", "FY2079-80", "FY2080-81", "FY2081-82"]
POST_FYS = ["FY2079-80", "FY2080-81", "FY2081-82"]
DELAYED = {("HBL", "FY2077-78"), ("NIMB", "FY2077-78")}
EPS_SLOPE = 2.5
BVPS_SLOPE = 0.6
PRICE_DATES = {
    "FY2076-77": "2021-04-13",
    "FY2077-78": "2022-04-13",
    "FY2078-79": "2023-04-13",
    "FY2079-80": "2024-04-14",
    "FY2080-81": "2025-04-13",
    "FY2081-82": "2026-04-13",
}


def _synthetic_panel() -> pd.DataFrame:
    rng = np.random.default_rng(20260413)
    bank_effect = {bank: 20 * i for i, bank in enumerate(BANKS)}
    year_effect = {fy: 15 * i for i, fy in enumerate(FYS)}
    rows = []
    for bank in BANKS:
        for fy in FYS:
            eps = float(rng.uniform(1, 25))
            bvps = float(rng.uniform(120, 200))
            gap = 54 if (bank, fy) in DELAYED else 0
            price = (
                EPS_SLOPE * eps
                + BVPS_SLOPE * bvps
                + bank_effect[bank]
                + year_effect[fy]
                + float(rng.normal(0, 5))
            )
            if gap > 5:  # price present in the file, excluded by the window rule
                price = float(rng.uniform(100, 500))
            rows.append(
                {
                    "bank": bank,
                    "fy": fy,
                    "post": int(fy in POST_FYS),
                    "price": round(price, 2),
                    "price_date": PRICE_DATES[fy],
                    "gap": gap,
                    "eps": round(eps, 2),
                    "bvps": round(bvps, 2),
                    "dps": float(rng.choice([0.0, 2.0, 5.0])),
                    "roa": round(float(rng.uniform(0.1, 1.8)), 3),
                    "entity_mismatch": fy == "FY2078-79" and bank != "NMB",
                }
            )
    return pd.DataFrame(rows)


@pytest.fixture()
def synthetic_study(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> dict:
    panel = _synthetic_panel()
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    panel.to_csv(data_dir / "panel.csv", index=False)

    bonus = panel.copy()
    bonus["bvps_adj"] = bonus["bvps"]
    bonus["bonus"] = 0.0
    bonus.to_csv(data_dir / "bonusadj.csv", index=False)

    pd.DataFrame(
        [
            {
                "series": row.bank,
                "fy": row.fy,
                "price_date": row.price_date,
                "close_dataset": row.price,
                "gap_days": row.gap,
                "status": "clean"
                if row.gap <= 5
                else "DELAYED - outside 5-day window, treat as missing under short-window rule",
            }
            for row in panel.itertuples()
        ]
    ).to_csv(data_dir / "price_status.csv", index=False)

    pd.DataFrame(
        [
            {
                "symbol": row.bank,
                "price_date": row.price_date,
                "dataset_close": row.price,
                "merolagani_ltp": row.price,
                "outcome": "match",
            }
            for row in panel.itertuples()
        ]
    ).to_csv(data_dir / "merolagani.csv", index=False)

    outputs = tmp_path / "outputs"
    cfg = {
        "data": {
            "root": str(data_dir),
            "panel": "panel.csv",
            "bonusadj": "bonusadj.csv",
            "price_status": "price_status.csv",
            "merolagani": "merolagani.csv",
        },
        "analysis": {
            "price_freshness_days": 5,
            "banks": BANKS,
            "fys": FYS,
            "post_fys": POST_FYS,
            "transition_fy": "FY2079-80",
            "entity_mismatch_fy": "FY2078-79",
            "variables": {
                "dependent": "price",
                "fundamentals": ["eps", "bvps"],
                "robustness_vars": ["dps", "roa"],
            },
            "eps_restated": {"GBIME": {"FY2076-77": float(panel.loc[0, "eps"]) + 1.0}},
        },
        "output": {"paper_root": str(outputs), "manifest_name": "generation_manifest.json"},
        "style": {
            "palette": "okabe_ito",
            "dpi": 150,
            "text_width_in": 5.5,
            "period_colors": {"pre": "blue", "post": "vermillion"},
        },
    }
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(cfg), encoding="utf-8")

    monkeypatch.setenv(config.CONFIG_ENV, str(cfg_path))
    config.get_config.cache_clear()
    try:
        yield {"panel": panel, "outputs": outputs, "data_dir": data_dir, "config": cfg}
    finally:
        config.get_config.cache_clear()
