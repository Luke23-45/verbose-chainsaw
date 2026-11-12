#!/usr/bin/env python3
"""Step-2 register re-verification for Appendix D (2026-11-01).
Checks, per register CSV row: file exists, pdfinfo page count, file size,
SHA-256 vs register, SOFP/SOPL/DPS pages within range, text-layer size,
DPS page vs dps.json, and indicator-table candidate pages.
Writes TSV + discrepancy report. No thesis files are modified.
"""
import csv, hashlib, json, os, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = str(HERE.parents[3])
REG = os.path.join(REPO, "data_analysis/data_extract/output/audit/source_register.csv")
DPSJ = os.path.join(REPO, "data_analysis/data_extract/config/dps.json")
OUT = os.path.join(str(HERE), "register_verification.tsv")

def pdfinfo_pages(path):
    try:
        out = subprocess.run(["pdfinfo", path], capture_output=True, text=True, timeout=60).stdout
        for line in out.splitlines():
            if line.startswith("Pages:"):
                return int(line.split(":")[1].strip())
    except Exception as e:
        return f"ERR:{e}"
    return None

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def text_len(path):
    try:
        out = subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True, timeout=180).stdout
        return len(out)
    except Exception:
        return -1

def indicator_pages(path):
    """Return PDF page numbers whose text mentions indicator-table headings."""
    try:
        out = subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True, text=True, timeout=180).stdout
    except Exception:
        return []
    keys = ["financial indicator", "key financial", "financial highlights", "nav per share", "net asset value per share"]
    pages, cur = [], 1
    for line in out.splitlines():
        if line.startswith("\x0c"):
            cur += 1
        low = line.lower()
        if any(k in low for k in keys):
            if cur not in pages:
                pages.append(cur)
    return pages[:6]

dps = json.load(open(DPSJ))
dps_map = {}
for e in dps.get("entries", dps if isinstance(dps, list) else []):
    key = (e.get("bank") or e.get("series"), e.get("fy"))
    dps_map[key] = e

rows = list(csv.DictReader(open(REG)))
print(f"register rows: {len(rows)}")
issues = []
with open(OUT, "w") as f:
    f.write("series\tfy\tfile\tpages\tsize_mb\tsha_match\tsofp\tsopl\tdps_pdf\ttext_chars\tvisual_read\tind_pages\tdps_json_page\n")
    for r in rows:
        p = os.path.join(REPO, r["annual_report_path"])
        exists = os.path.exists(p)
        pages = pdfinfo_pages(p) if exists else None
        size = round(os.path.getsize(p) / 1e6, 2) if exists else None
        sha = sha256(p) if exists else None
        sham = (sha == r["report_sha256"]) if sha else False
        def inrange(v):
            try:
                return all(1 <= int(x) <= pages for x in v.split(";") if x.strip())
            except Exception:
                return False
        ok_sofp = inrange(r["sofp_pages_pdf"]) if pages else False
        ok_sopl = inrange(r["sopl_pages_pdf"]) if pages else False
        ok_dps = (1 <= int(r["dps_pdf_page"]) <= pages) if pages and r["dps_pdf_page"].isdigit() else False
        tl = text_len(p) if exists else -1
        ind = indicator_pages(p) if exists else []
        dj = dps_map.get((r["series"], r["fy"].replace("-", "/").replace("FY", "FY")))
        dj_page = None
        if dj:
            dj_page = dj.get("pdf_page") or dj.get("page")
        f.write(f"{r['series']}\t{r['fy']}\t{os.path.basename(p)}\t{pages}\t{size}\t{sham}\t{r['sofp_pages_pdf']}\t{r['sopl_pages_pdf']}\t{r['dps_pdf_page']}\t{tl}\t{r['visual_read']}\t{','.join(map(str, ind))}\t{dj_page}\n")
        if not exists: issues.append(f"MISSING FILE {r['series']} {r['fy']}")
        if exists and not sham: issues.append(f"SHA MISMATCH {r['series']} {r['fy']}")
        if exists and not (ok_sofp and ok_sopl and ok_dps): issues.append(f"PAGE OUT OF RANGE {r['series']} {r['fy']} sofp={r['sofp_pages_pdf']} sopl={r['sopl_pages_pdf']} dps={r['dps_pdf_page']} pages={pages}")
        if dj_page is not None and str(dj_page) != r["dps_pdf_page"]:
            issues.append(f"DPS PAGE CSVvsJSON {r['series']} {r['fy']} csv={r['dps_pdf_page']} json={dj_page}")

print("ISSUES:")
for i in issues:
    print(" -", i)
print(f"total issues: {len(issues)}")
print(f"wrote {OUT}")
