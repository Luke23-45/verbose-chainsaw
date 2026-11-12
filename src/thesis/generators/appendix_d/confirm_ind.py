import os, subprocess, csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = str(HERE.parents[3])
panel = {(r["series"], r["fy"]): r for r in csv.DictReader(open(os.path.join(REPO, "data_analysis/data_extract/output/tidy/accounting_panel.csv")))}
reg = {(r["series"], r["fy"]): r for r in csv.DictReader(open(os.path.join(REPO, "data_analysis/data_extract/output/audit/source_register.csv")))}
cands = {
 ("GBIME","FY2076-77"): [8], ("GBIME","FY2077-78"): [65], ("GBIME","FY2078-79"): [67],
 ("GBIME","FY2079-80"): [72], ("GBIME","FY2081-82"): [29],
 ("HBL","FY2076-77"): [28], ("HBL","FY2077-78"): [33], ("HBL","FY2078-79"): [36],
 ("HBL","FY2079-80"): [34], ("HBL","FY2080-81"): [40], ("HBL","FY2081-82"): [38],
 ("KBL","FY2079-80"): [160], ("KBL","FY2080-81"): [165], ("KBL","FY2081-82"): [172],
 ("NIMB","FY2076-77"): [156], ("NIMB","FY2077-78"): [159], ("NIMB","FY2078-79"): [167],
 ("NIMB","FY2079-80"): [168], ("NIMB","FY2080-81"): [172], ("NIMB","FY2081-82"): [164],
 ("NMB","FY2076-77"): [34, 35], ("NMB","FY2077-78"): [27], ("NMB","FY2078-79"): [31],
}
for (s, fy), pages in cands.items():
    prow, rrow = panel[(s, fy)], reg[(s, fy)]
    p = os.path.join(REPO, rrow["annual_report_path"])
    eps, nav = prow["eps_reported"], prow["nav_reported"]
    for pg in pages:
        try:
            txt = subprocess.run(["pdftotext", "-f", str(pg), "-l", str(pg), "-layout", p, "-"], capture_output=True, text=True, timeout=60).stdout
        except Exception:
            txt = ""
        has_eps = eps in txt
        has_nav = nav in txt
        first = " | ".join(l.strip()[:60] for l in txt.splitlines() if l.strip())[:140]
        print(f"{s} {fy} p{pg}: eps({eps})={has_eps} nav({nav})={has_nav} :: {first}")
# NMB Nepali: number-string search for panel EPS/NAV across all pages
rrow = reg[("NMB","FY2079-80")]; prow = panel[("NMB","FY2079-80")]
p = os.path.join(REPO, rrow["annual_report_path"])
out = subprocess.run(["pdftotext", "-layout", p, "-"], capture_output=True, text=True, timeout=180).stdout
pages = out.split("\x0c")
eps, nav = prow["eps_reported"], prow["nav_reported"]
hits = [i for i, pg in enumerate(pages, start=1) if eps in pg and nav in pg]
print(f"NMB FY2079-80 Nepali eps={eps} nav={nav} pages_with_both={hits[:10]}")
