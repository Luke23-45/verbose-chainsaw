# Appendix D generators

Generates the Appendix D table rows from the verified source register.
All paths are resolved from this directory, so the scripts run from any
checkout of this repository.

## Files

- `gen_tables.py` -> `table14_rows.tex`, `table15_rows.tex` — Tables 14
  and 15 row fragments, from the source register CSV, the verification
  TSV and the frozen indicators in `table_map_frozen.md`. Asserts 30
  rows each, unique SHA-12 prefixes, all pages in range. Assembly into
  `appendix_d.tex` replaces placeholders there.
- `verify_register.py` — re-verifies the register (file exists, pdfinfo
  page count, file size, SHA-256, SOFP/SOPL/DPS pages, DPS page vs
  `dps.json`, indicator-table candidate pages). Writes
  `register_verification.tsv`. Modifies no thesis file.
- `table_map_frozen.md` — frozen table map for Tables 14/15.
- `find_both.py`, `find_eps_pages.py`, `find_indicators.py`,
  `find_sep.py`, `confirm_ind.py` — one-off indicator-page searches
  from the 2026-11-01 build. Kept as the provenance record for the
  table contents; not part of the regeneration path.

## Rule

Never hand-edit `table14_rows.tex` or `table15_rows.tex`. Edit
`gen_tables.py` (or the register inputs) and re-run it, then check
`git diff`. A re-run must reproduce the tracked fragments exactly.
