"""Round-2 computations for the Appendix E gap closure (v25).

Loads results.pkl from round 1 (verified M1/M2/R1-R8 fits) and computes only
the new items: Model 2 diagnostics, Model 2 VIFs, joint fixed-effect tests
for R3-R8, leave-one-year fits, and post-consolidation confidence intervals.
Verification: leave-one-year for FY2078/79 and FY2079/80 must reproduce R6
and R5 exactly, and the joint-FE function must reproduce Table 21's Model 2
row from specs['R2'].
"""
import pickle

import numpy as np
import pandas as pd
from scipy import stats
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]

r = pickle.load(open(HERE / "results.pkl", "rb"))
M2, specs = r["M2"], r["specs"]
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
    return dict(names=names, beta=beta, se=se, t=t, p=pv, ci=ci, V=V,
                n=n, K=K, df=dfree)


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


# ---- 1. Model 2 Breusch-Pagan ----
Xb = np.column_stack([np.ones(28), M2["X"][:, 1:]])
bb, *_ = np.linalg.lstsq(Xb, M2["e"] ** 2, rcond=None)
eb = M2["e"] ** 2 - Xb @ bb
v = M2["e"] ** 2
r2b = 1 - (eb @ eb) / ((v - v.mean()) @ (v - v.mean()))
bp_lm = 28 * r2b
bp_p = float(stats.chi2.sf(bp_lm, 13))
print(f"M2 BP: LM={bp_lm:.4f} df=13 p={bp_p:.4f}")

# ---- 2. Model 2 flagged observations ----
s2 = M2["ssr"] / M2["df"]
cook2 = (M2["e"] ** 2 / (M2["K"] * s2)) * (M2["h"] / (1 - M2["h"]) ** 2)
flag2 = clean[cook2 > 4 / 28].copy()
flag2["cook"] = cook2[cook2 > 4 / 28]
flag2["lev"] = M2["h"][cook2 > 4 / 28]
print("M2 flagged:")
for _, row in flag2.iterrows():
    print(f"  {row['bank']} {row['fy']}: Cook={row['cook']:.4f} lev={row['lev']:.4f}")
assert len(flag2) == 5
assert clean.loc[cook2.argmax(), "bank"] == "KBL" and abs(cook2.max() - 0.4902) < 0.0005

# ---- 3. Model 2 VIFs (slopes-only auxiliary regressions, thesis method) ----
def vif_aux(yv, Xv):
    Xv = np.column_stack([np.ones(len(yv)), Xv])
    b, *_ = np.linalg.lstsq(Xv, yv, rcond=None)
    e = yv - Xv @ b
    r2a = 1 - (e @ e) / ((yv - yv.mean()) @ (yv - yv.mean()))
    return 1 / (1 - r2a)
eps, bvps, post = clean["eps"].values, clean["bvps"].values, clean["post"].values
dE, dB = eps * post, bvps * post
vifs = {
    "EPS": vif_aux(eps, np.column_stack([bvps, dE, dB])),
    "BVPS": vif_aux(bvps, np.column_stack([eps, dE, dB])),
    "d_E": vif_aux(dE, np.column_stack([eps, bvps, dB])),
    "d_B": vif_aux(dB, np.column_stack([eps, bvps, dE])),
}
print("M2 VIFs:", {k: round(v, 2) for k, v in vifs.items()})
assert abs(vifs["EPS"] - 10.33) < 0.01 and abs(vifs["d_B"] - 24.13) < 0.01

# ---- 4. Joint FE tests for R3-R8 (+ R2 sanity check vs Table 21) ----
fe_tests = {}
for k in ["R2", "R3", "R4", "R5", "R6", "R7", "R8"]:
    res = specs[k]
    nb = [n for n in res["names"] if n.startswith("Bank ")]
    ny = [n for n in res["names"] if n.startswith("Year ")]
    fe_tests[k] = {
        "bank": waldF(res, *nb), "year": waldF(res, *ny),
        "both": waldF(res, *(nb + ny)),
        "n_bank": len(nb), "n_year": len(ny), "df": res["df"],
    }
    print(k, {t: (round(fe_tests[k][t][0], 3), round(fe_tests[k][t][1], 4))
               for t in ["bank", "year", "both"]})
assert abs(fe_tests["R2"]["bank"][0] - 2.618) < 0.001
assert abs(fe_tests["R2"]["year"][0] - 27.102) < 0.001
assert abs(fe_tests["R2"]["both"][0] - 30.835) < 0.001

# ---- 5. Leave-one-year fits (all six years) ----
loy = {}
for y in YEARS:
    sub = clean[clean["fy"] != y]
    res = m2_on(sub)
    F, pv = waldF(res, "d_E", "d_B")
    iE, iB = res["names"].index("d_E"), res["names"].index("d_B")
    loy[y] = dict(n=len(sub), dE=res["beta"][iE], dE_se=res["se"][iE],
                  dB=res["beta"][iB], dB_se=res["se"][iB], F=F, p=pv,
                  df=res["df"])
    print(f"drop {y}: n={len(sub)} d_E={res['beta'][iE]:.4f} d_B={res['beta'][iB]:.4f} F={F:.3f} p={pv:.4f}")
# verification: FY2078-79 must equal R6, FY2079-80 must equal R5
assert abs(loy["FY2078-79"]["dE"] - (-2.4363)) < 0.0005
assert abs(loy["FY2078-79"]["F"] - 5.818) < 0.005
assert abs(loy["FY2079-80"]["dE"] - (-2.5783)) < 0.0005
assert abs(loy["FY2079-80"]["F"] - 2.414) < 0.005
print("leave-one-year verification vs R5/R6: PASS")

# ---- 6. Post-consolidation full inference ----
crit = stats.t.ppf(0.975, M2["df"])
post_inf = {}
for lab in ["post EPS", "post BVPS"]:
    est, se, t, pv = M2[lab]
    post_inf[lab] = dict(est=est, se=se, t=t, p=pv,
                         lo=est - crit * se, hi=est + crit * se)
    print(lab, {k: round(v, 4) for k, v in post_inf[lab].items()})
assert abs(post_inf["post EPS"]["lo"] - (-2.4124)) < 0.0005
assert abs(post_inf["post BVPS"]["hi"] - 0.7441) < 0.0005

with open(HERE / "results2.pkl", "wb") as f:
    pickle.dump(dict(bp=(bp_lm, bp_p), flag2=flag2, vifs=vifs,
                     fe_tests=fe_tests, loy=loy, post_inf=post_inf), f)
print("saved results2.pkl")
