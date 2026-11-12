import os, subprocess, csv, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = str(HERE.parents[3])
panel = {}
for r in csv.DictReader(open(os.path.join(REPO, "data_analysis/data_extract/output/tidy/accounting_panel.csv"))):
    panel[(r["series"], r["fy"])] = r
reg = list(csv.DictReader(open(os.path.join(REPO, "data_analysis/data_extract/output/audit/source_register.csv"))))
for r in reg:
    key = (r["series"], r["fy"].replace("FY", "FY").replace("-", "/"))
    # panel fy format check: print available keys once via fallback
    prow = panel.get((r["series"], r["fy"])) or panel.get((r["series"], r["fy"].replace("-", "/")))
    if not prow:
        print(r["series"], r["fy"], "NO PANEL ROW"); continue
    eps = prow.get("eps_reported")
    p = os.path.join(REPO, r["annual_report_path"])
    try:
        out = subprocess.run(["pdftotext", "-layout", p, "-"], capture_output=True, text=True, timeout=180).stdout
    except Exception:
        print(r["series"], r["fy"], "TEXT-ERR"); continue
    pages = out.split("\x0c")
    sopl = set()
    for x in r["sopl_pages_pdf"].split(";"):
        if x.strip().isdigit(): sopl.add(int(x.strip()))
    cands = []
    for i, pg in enumerate(pages, start=1):
        if i in sopl: continue
        if "per share" in pg.lower() and eps and eps in pg:
            # snippet: line with eps
            sn = ""
            for line in pg.splitlines():
                if eps in line and "share" in line.lower():
                    sn = line.strip()[:80]; break
            cands.append((i, sn))
    print(f"{r['series']} {r['fy']} eps={eps} sopl_excluded={sorted(sopl)} cands={cands[:4]}")
