import os, subprocess, csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = str(HERE.parents[3])
panel = {(r["series"], r["fy"]): r for r in csv.DictReader(open(os.path.join(REPO, "data_analysis/data_extract/output/tidy/accounting_panel.csv")))}
reg = list(csv.DictReader(open(os.path.join(REPO, "data_analysis/data_extract/output/audit/source_register.csv"))))
want = {("HBL","FY2076-77"),("KBL","FY2076-77"),("KBL","FY2077-78"),("KBL","FY2078-79"),("KBL","FY2079-80"),("KBL","FY2080-81"),("KBL","FY2081-82"),
("NIMB","FY2076-77"),("NIMB","FY2077-78"),("NIMB","FY2078-79"),("NIMB","FY2079-80"),("NIMB","FY2080-81"),("NIMB","FY2081-82"),
("NMB","FY2076-77"),("NMB","FY2077-78"),("NMB","FY2078-79"),("NMB","FY2080-81")}
def forms(v):
    out = {v}
    try: out.add(f"{float(v):.2f}")
    except Exception: pass
    return out
for r in reg:
    if (r["series"], r["fy"]) not in want: continue
    prow = panel[(r["series"], r["fy"])]
    p = os.path.join(REPO, r["annual_report_path"])
    out = subprocess.run(["pdftotext", "-layout", p, "-"], capture_output=True, text=True, timeout=180).stdout
    pages = out.split("\x0c")
    sopl = set(int(x) for x in r["sopl_pages_pdf"].split(";") if x.strip().isdigit())
    ef, nf = forms(prow["eps_reported"]), forms(prow["nav_reported"])
    ep = [i for i, pg in enumerate(pages, start=1) if i not in sopl and any(e in pg for e in ef)]
    np_ = [i for i, pg in enumerate(pages, start=1) if i not in sopl and any(n in pg for n in nf)]
    print(f"{r['series']} {r['fy']} eps={prow['eps_reported']} EPSpages={ep[:8]} nav={prow['nav_reported']} NAVpages={np_[:8]}")
