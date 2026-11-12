"""Rebuild A2_robustness_forest.pdf with the R9 row added.

Plots exactly the EPS-channel estimates printed in Appendix E (Table
tab:app_robustfull / tab:app_robust_inf): earnings coefficient and
EPS x Post interaction with 95% HC3 CIs. R3 omitted (ROA scale), R1 has
no interaction term. Old rows must reproduce the v28 figure; only the
R9 row and widened axes are new.
"""
import pickle

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
W = str(HERE) + "/"
r = pickle.load(open(W + "results.pkl", "rb"))
r9 = pickle.load(open(W + "results_r9.pkl", "rb"))
specs = dict(r["specs"])
specs["R9"] = r9["R9"]

# (key, label, eps_name, d_name or None)
ROWS = [
    ("R1", "R1 Model 1 (baseline)", "EPS", None),
    ("R2", "R2 Model 2 (baseline)", "EPS", "d_E"),
    ("R4", "R4 + DPS", "EPS", "d_E"),
    ("R5", "R5 excl. transition FY2079-80", "EPS", "d_E"),
    ("R6", "R6 excl. FY2078-79", "EPS", "d_E"),
    ("R7", "R7 bonus-adjusted BVPS", "EPS", "d_E"),
    ("R8", "R8 restated EPS", "EPS_r", "d_Er"),
    ("R9", "R9 excl. NMB FY2076-77", "EPS", "d_E"),
]

labels, eps, eps_lo, eps_hi, d, d_lo, d_hi = [], [], [], [], [], [], []
for k, lab, en, dn in ROWS:
    res = specs[k]
    i = res["names"].index(en)
    labels.append(lab)
    eps.append(res["beta"][i])
    eps_lo.append(res["ci"][i][0])
    eps_hi.append(res["ci"][i][1])
    print(f"{k} EPS {res['beta'][i]:.4f} CI ({res['ci'][i][0]:.4f}, {res['ci'][i][1]:.4f})")
    if dn is None:
        d.append(np.nan); d_lo.append(np.nan); d_hi.append(np.nan)
    else:
        j = res["names"].index(dn)
        d.append(res["beta"][j])
        d_lo.append(res["ci"][j][0])
        d_hi.append(res["ci"][j][1])
        print(f"{k} d_E {res['beta'][j]:.4f} CI ({res['ci'][j][0]:.4f}, {res['ci'][j][1]:.4f})")

y = np.arange(len(labels))[::-1]
BLUE, GOLD = "#2E75B6", "#E69F00"

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.9), sharey=True)
fig.suptitle("Robustness suite: EPS-channel estimates (n = 28 unless noted in T5)",
             fontsize=11, fontweight="bold", y=0.98)
for ax in (ax1, ax2):
    ax.grid(True, color="#DDDDDD", linewidth=0.6, linestyle="-")
    ax.axvline(0, color="#333333", linewidth=0.9)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
ax1.errorbar(eps, y, xerr=[np.array(eps) - np.array(eps_lo),
                            np.array(eps_hi) - np.array(eps)],
             fmt="o", color=BLUE, ecolor=BLUE, elinewidth=1.5,
             markersize=6, capsize=0)
ax1.set_xlabel("beta(EPS), 95% CI (NPR per NPR)", fontsize=9)
ax1.set_xlim(-12, 24)
ax1.set_xticks([-10, 0, 10, 20])
ax1.set_yticks(y)
ax1.set_yticklabels(labels, fontsize=9)
ax2.errorbar(d, y, xerr=[np.array(d) - np.array(d_lo),
                          np.array(d_hi) - np.array(d)],
             fmt="o", color=GOLD, ecolor=GOLD, elinewidth=1.5,
             markersize=6, capsize=0)
ax2.set_xlabel("delta(EPS x Post), 95% CI (NPR per NPR)", fontsize=9)
ax2.set_xlim(-20, 13)
ax2.set_xticks([-20, -10, 0, 10])
fig.text(0.5, 0.01,
         "R3 (ROA replaces EPS) is omitted: ROA is measured in percentage points "
         "and is not on this scale; its estimates are in T5. R1 has no interaction terms.",
         ha="center", fontsize=8)
plt.tight_layout(rect=[0, 0.06, 1, 0.94])
out = str(REPO / "src/thesis/figures/A2_robustness_forest")
fig.savefig(out + ".pdf")
fig.savefig(out + ".png", dpi=150)
print("saved", out + ".pdf/.png")
