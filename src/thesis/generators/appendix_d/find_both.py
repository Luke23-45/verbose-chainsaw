import os, subprocess, csv, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = str(HERE.parents[3])
panel = {(r["series"], r["fy"]): r for r in csv.DictReader(open(os.path.join(REPO, "data_analysis/data_extract/output/tidy/accounting_panel.csv")))}
reg = list(csv.DictReader(open(os.path.join(REPO, "data_analysis/data_extract/output/audit/source_register.csv"))))
def forms(v):
    out = {v}
    try:
        f = float(v); out.add(f"{f:.2f}")
    except Exception: pass
    return out
for r in reg:
    prow = panel[(r["series"], r["fy"])]
    p = os.path.join(REPO, r["annual_report_path"])
    try:
        out = subprocess.run(["pdftotext", "-layout", p, "-"], capture_output=True, text=True, timeout=180).stdout
    except Exception:
        print(r["series"], r["fy"], "TEXT-ERR"); continue
    pages = out.split("\x0c")
    sopl = set(int(x) for x in r["sopl_pages_pdf"].split(";") if x.strip().isdigit())
    ef, nf = forms(prow["eps_reported"]), forms(prow["nav_reported"])
    hits = []
    for i, pg in enumerate(pages, start=1):
        if i in sopl: continue
        if any(e in pg for e in ef) and any(n in pg for n in nf):
            # context: does page mention share/indicator?
            ctx = "share" if "share" in pg.lower() else ("indic" if "indic" in pg.lower() else "")
            hits.append((i, ctx))
    print(f"{r['series']} {r['fy']} eps={prow['eps_reported']} nav={prow['nav_reported']} both_pages={hits[:8]}")
