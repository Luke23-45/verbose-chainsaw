"""R10 computation: Model 2 excluding both the Kanchan-mismatched bank-year
(NMB FY 2076/77) and the Kumari Bank FY 2076/77 partial-year acquisition observation.
Estimates n=26, K=14, df=12. Saves results_r10.pkl and updates results.pkl.
"""
import pickle
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

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


# Drop both NMB FY2076-77 and KBL FY2076-77
r10df = clean[~(((clean["bank"] == "NMB") & (clean["fy"] == "FY2076-77")) |
                ((clean["bank"] == "KBL") & (clean["fy"] == "FY2076-77")))].copy()
assert len(r10df) == 26
assert len(clean) - len(r10df) == 2

res10 = m2_on(r10df)
assert res10["n"] == 26 and res10["K"] == 14 and res10["df"] == 12

F10, p10 = waldF(res10, "d_E", "d_B")
nb = [n for n in res10["names"] if n.startswith("Bank ")]
ny = [n for n in res10["names"] if n.startswith("Year ")]
fe = {"bank": waldF(res10, *nb), "year": waldF(res10, *ny),
      "both": waldF(res10, *(nb + ny)), "n_bank": len(nb),
      "n_year": len(ny), "df": res10["df"]}

print(f"R10: n={res10['n']} K={res10['K']} df={res10['df']} R2={res10['r2']:.4f} adj={res10['adj']:.4f} within={res10['within']:.4f}")
print(f"R10 Wald F(2,12)={F10:.4f} p={p10:.4f}")
print(f"R10 FE: bank F={fe['bank'][0]:.4f} p={fe['bank'][1]:.4f}; year F={fe['year'][0]:.4f} p={fe['year'][1]:.4f}; both F={fe['both'][0]:.4f} p={fe['both'][1]:.4f}")

with open(HERE / "results_r10.pkl", "wb") as f:
    pickle.dump(dict(R10=res10, wald=(F10, p10), fe_tests={"R10": fe}), f)
print("saved results_r10.pkl")

# Update results.pkl
with open(HERE / "results.pkl", "rb") as f:
    r = pickle.load(f)
r["specs"]["R10"] = res10
with open(HERE / "results.pkl", "wb") as f:
    pickle.dump(r, f)
print("updated results.pkl with R10")
