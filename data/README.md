# Download checklist — audited annual reports

Target: **5 bank series × 6 fiscal years (FY 2076/77–2081/82) = 30 reports.**
Save each PDF as: `data/reports/<SERIES>/<FYxxxx-xx>/<SERIES>_FYxxxx-xx_annual_report.pdf`

FY → AD year labels used on bank websites:

| Fiscal year | Website label | Folder |
|---|---|---|
| 2076/77 | 2019/20 | FY2076-77 |
| 2077/78 | 2020/21 | FY2077-78 |
| 2078/79 | 2021/22 | FY2078-79 |
| 2079/80 | 2022/23 | FY2079-80 |
| 2080/81 | 2023/24 | FY2080-81 |
| 2081/82 | 2024/25 | FY2081-82 |

Important: FY **2079/80 is the merger transition year** for the four merged
series — download the **consolidated institution's** audited report for that
year (the same bank's reports for 2080/81 and 2081/82 are also the
consolidated bank's).

---

## 1. Global IME Bank (GBIME) — 6 files
Source: https://www.globalimebank.com/np/annual-report/ (year dropdown; English toggle available)

| FY | Report of | Status |
|---|---|---|
| 2076/77 | Global IME Bank Ltd | ✅ |
| 2077/78 | Global IME Bank Ltd | ✅ |
| 2078/79 | Global IME Bank Ltd | ✅ |
| 2079/80 | Global IME Bank (consolidated; absorbed BoK 9 Jan 2023) | ✅ |
| 2080/81 | Global IME Bank Ltd (consolidated) | ✅ |
| 2081/82 | Global IME Bank Ltd (consolidated) | ✅ |

## 2. Himalayan Bank (HBL) — 6 files
Source: https://www.himalayanbank.com → Financial Reports.
Site was refusing connections on 2026-10-27; fallback: Wayback Machine
(https://web.archive.org) — archived report numbering: 28th AR = FY 2076/77,
29th = 2077/78, 30th = 2078/79, 31st = 2079/80, 32nd = 2080/81, 33rd = 2081/82.
Path pattern: `/images/pdf/uploaded/<N>th Annual Report.pdf`

| FY | Report of | Status |
|---|---|---|
| 2076/77 | Himalayan Bank Ltd (28th AR) | ✅ |
| 2077/78 | Himalayan Bank Ltd (29th AR) | ✅ |
| 2078/79 | Himalayan Bank Ltd (30th AR) | ✅ |
| 2079/80 | Himalayan Bank (consolidated; acquired Civil Bank 24 Feb 2023) | ✅ |
| 2080/81 | Himalayan Bank Ltd (consolidated) | ✅ |
| 2081/82 | Himalayan Bank Ltd (consolidated) | ✅ |

## 3. Kumari Bank (KBL) — 6 files
Source: https://www.kumaribank.com → Reports / Financial Reports
(blocks command-line tools; opens fine in a normal browser)

| FY | Report of | Status |
|---|---|---|
| 2076/77 | Kumari Bank Ltd | ✅ |
| 2077/78 | Kumari Bank Ltd | ✅ |
| 2078/79 | Kumari Bank Ltd | ✅ |
| 2079/80 | Kumari Bank (consolidated; absorbed NCC Bank 1 Jan 2023) | ✅ |
| 2080/81 | Kumari Bank Ltd (consolidated) | ✅ |
| 2081/82 | Kumari Bank Ltd (consolidated) | ✅ |

## 4. Nepal Investment Mega Bank (NIMB) — 6 files
Pre-merger years are **Nepal Investment Bank Ltd** reports — try the legacy
site https://www.nibl.com.np (still online). For FY 2079/80 onward use NIMB's
own site (nimbank.com did not resolve here; if it fails, get the reports via
NEPSE/SEBON or the bank directly).

| FY | Report of | Status |
|---|---|---|
| 2076/77 | Nepal Investment Bank Ltd | ✅ |
| 2077/78 | Nepal Investment Bank Ltd | ✅ |
| 2078/79 | Nepal Investment Bank Ltd | ✅ |
| 2079/80 | Nepal Investment Mega Bank (merger with Mega Bank 11 Jan 2023) | ✅ |
| 2080/81 | Nepal Investment Mega Bank Ltd | ✅ |
| 2081/82 | Nepal Investment Mega Bank Ltd | ✅ |

## 5. NMB Bank (NMB) — 6 files — ✅ DONE
Source: https://www.nmb.com.np/en/report/annual-report

| FY | File | Status |
|---|---|---|
| 2076/77 | data/reports/NMB/FY2076-77/NMB_FY2076-77_annual_report.pdf (English) | ✅ |
| 2077/78 | data/reports/NMB/FY2077-78/NMB_FY2077-78_annual_report.pdf (English) | ✅ |
| 2078/79 | data/reports/NMB/FY2078-79/NMB_FY2078-79_annual_report.pdf (English) | ✅ |
| 2079/80 | data/reports/NMB/FY2079-80/NMB_FY2079-80_annual_report_NP.pdf (Nepali) | ✅ |
| 2080/81 | data/reports/NMB/FY2080-81/NMB_FY2080-81_annual_report.pdf (English) | ✅ |
| 2081/82 | data/reports/NMB/FY2081-82/NMB_FY2081-82_annual_report.pdf (English) | ✅ |

Note: NMB's English 2022/23 link is dead on the bank's own server
(S3 "NoSuchKey"), so FY 2079/80 is the Nepali edition. If the English edition
is wanted, try SEBON/NEPSE or ask the bank; the audited statements are the same.

---

Count: 30 total — 30 done, 0 to download (downloaded 2026-10-27; see notes below).


## Completion note (2026-10-27)
- GBIME: English editions downloaded from globalimebank.com annual-report page.
- HBL: live site refused connections, so all six were fetched from Wayback Machine captures of the bank's own annual-report listing.
- KBL: downloaded from kumaribank.com/reports; the 2076/77 file first returned a blocked-page HTML and was re-fetched successfully.
- NIMB: downloaded from nimb.com.np financial reports (nibl.com.np redirects there); pre-merger years are Nepal Investment Bank reports.
- NMB FY 2079/80: the English file in the repo is the bank's dead S3 link (NoSuchKey XML); the usable audited report is the Nepali edition (NMB_FY2079-80_annual_report_NP.pdf), as already noted above.
