"""R9 computation: Model 2 excluding the Kanchan-mismatched bank-year
(NMB FY2076/77). Functions copied verbatim from compute_e2.py (design/fit/
waldF/m2_on) and the within-R^2 definition from compute_e.py, so R9 is
estimated by exactly the same code path as R1-R8. Sanity check: m2_on(clean)
must reproduce R2 before R9 is trusted.
"""
import pickle

import numpy as np
import pandas as pd
from scipy import stats
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]

PANEL = str(REPO / "data_analysis/data_extract/output/manual_review/mps_rd_joined_panel.csv")
p = pd.read_csv(PANEL)
clean = p[p["gap"] <= 5].copy().reset_index(drop=True)
BANKS = ["GBIME", "HBL", "KBL", "NIMB", "NMB"]
YEARS = sorted(clean["fy"].unique())


def design(df, slopes, ref_bank="GBIME", ref_year="FY2076-77"):
    names = ["Intercept"] + [s[0] for s in slopes]
    cols = [np.ones(len(df))] + [np.asarray(s[1], dtype=float) for s in slopes]
    for b in BANKS:
        if b != ref_bank and (df["bank"] == b).any():
            names.append(f"Bank {b}")
            cols.append((df["bank"] == b).astype(float).values)
    for y in YEARS:
        if y != ref_year and (df["fy"] == y).any():
            names.append(f"Year {y}")
            cols.append((df["fy"] == y).astype(float).values)
    return names, np.column_stack(cols)


def fit(df, slopes, **kw):
    df = df.reset_index(drop=True)
    names, X = design(df, slopes, **kw)
    y = df["price"].values.astype(float)
    n, K = X.shape
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    e = y - X @ beta
    XtX_inv = np.linalg.inv(X.T @ X)
    h = np.einsum("ij,jk,ik->i", X, XtX_inv, X)
    w = (e / (1 - h)) ** 2
    V = XtX_inv @ ((X * w[:, None]).T @ X) @ XtX_inv
    se = np.sqrt(np.diag(V))
    dfree = n - K
    t = beta / se
    pv = 2 * stats.t.sf(np.abs(t), dfree)
    crit = stats.t.ppf(0.975, dfree)
    ci = np.column_stack([beta - crit * se, beta + crit * se])
    ssr = float(e @ e)
    sst = float(((y - y.mean()) ** 2).sum())
    r2 = 1 - ssr / sst
    adj = 1 - (1 - r2) * (n - 1) / dfree
    _, X0 = design(df, [])
    b0, *_ = np.linalg.lstsq(X0, y, rcond=None)
    e0 = y - X0 @ b0
    within_r2 = 1 - ssr / float(e0 @ e0)
    return dict(names=names, beta=beta, se=se, t=t, p=pv, ci=ci, V=V,
                n=n, K=K, df=dfree, r2=r2, adj=adj, within=within_r2,
                ssr=ssr)


def waldF(res, *nms):
    idx = [res["names"].index(n) for n in nms]
    b = res["beta"][idx]
    Vsub = res["V"][np.ix_(idx, idx)]
    q = len(idx)
    F = float(b @ np.linalg.inv(Vsub) @ b) / q
    return F, float(stats.f.sf(F, q, res["df"]))


def m2_on(df):
    ref_year = "FY2076-77" if (df["fy"] == "FY2076-77").any() else sorted(df["fy"].unique())[0]
    ref_bank = "GBIME" if (df["bank"] == "GBIME").any() else sorted(df["bank"].unique())[0]
    return fit(df, [("EPS", df["eps"]), ("BVPS", df["bvps"]),
                    ("d_E", df["eps"] * df["post"]),
                    ("d_B", df["bvps"] * df["post"])],
               ref_bank=ref_bank, ref_year=ref_year)


# ---- sanity: full clean panel must reproduce R2 ----
r2 = m2_on(clean)
iE, iB = r2["names"].index("EPS"), r2["names"].index("BVPS")
idE, idB = r2["names"].index("d_E"), r2["names"].index("d_B")
F2, p2 = waldF(r2, "d_E", "d_B")
assert abs(r2["beta"][iE] - 5.577) < 0.001, r2["beta"][iE]
assert abs(r2["beta"][idE] - (-3.124)) < 0.001, r2["beta"][idE]
assert abs(F2 - 2.954) < 0.005, F2
print(f"sanity R2 reproduced: EPS={r2['beta'][iE]:.4f} d_E={r2['beta'][idE]:.4f} F={F2:.4f} p={p2:.4f}")

# ---- R9: drop NMB FY2076/77 ----
r9df = clean[~((clean["bank"] == "NMB") & (clean["fy"] == "FY2076-77"))].copy()
assert len(r9df) == 27
assert len(clean) - len(r9df) == 1
res = m2_on(r9df)
assert res["n"] == 27 and res["K"] == 14 and res["df"] == 13
F9, p9 = waldF(res, "d_E", "d_B")
nb = [n for n in res["names"] if n.startswith("Bank ")]
ny = [n for n in res["names"] if n.startswith("Year ")]
fe = {"bank": waldF(res, *nb), "year": waldF(res, *ny),
      "both": waldF(res, *(nb + ny)), "n_bank": len(nb),
      "n_year": len(ny), "df": res["df"]}
print(f"R9: n={res['n']} K={res['K']} df={res['df']} R2={res['r2']:.4f} adj={res['adj']:.4f} within={res['within']:.4f}")
print(f"R9 Wald F(2,13)={F9:.4f} p={p9:.4f}")
print(f"R9 FE: bank F={fe['bank'][0]:.4f} p={fe['bank'][1]:.4f}; year F={fe['year'][0]:.4f} p={fe['year'][1]:.4f}; both F={fe['both'][0]:.4f} p={fe['both'][1]:.4f}")
for nm, b, s, t, pv, (lo, hi) in zip(res["names"], res["beta"], res["se"],
                                    res["t"], res["p"], res["ci"]):
    print(f"  {nm:14s} beta={b:10.4f} se={s:8.4f} t={t:8.4f} p={pv:.4f} CI=({lo:.4f}, {hi:.4f})")

with open(HERE / "results_r9.pkl", "wb") as f:
    pickle.dump(dict(R9=res, wald=(F9, p9), fe_tests={"R9": fe}), f)
print("saved results_r9.pkl")
