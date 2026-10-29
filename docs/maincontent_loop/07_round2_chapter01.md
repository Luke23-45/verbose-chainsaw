# Main-content loop — Round 2, Chapter I review (fresh re-review)

Reviewer: independent re-review of the CURRENT files (after Round 1
fixes). No files edited. Compile evidence: whole-document log has
0 LaTeX errors, 0 undefined references; Chapter I log segment
(lines 1231–1307) contains no undefined reference.

## MUST-FIX: none

Verified clean: zero \ref/\eqref (so zero dangling); all 34
citation keys resolve; all 8 labels unique across chapters +
appendices + front; braces 193/193; dollars 110, even;
environments balanced (enumerate 5/5, itemize 9/9, equation 9/9);
zero hardcoded formatting commands; no tables/figures/footnotes.

## MINOR (same as Round 1, disposition unchanged)

- M1: 9 hypothesis equations numbered but unlabelled/uncited —
  KEPT (same Round 1 disposition: numbering without citation is
  legitimate, not a defect).
- M2: `Model~2` tie once vs plain `Model 1/2` — NOTATION PASS.
- M3: fiscal-year ranges in two forms — NOTATION PASS.
- M4: 12 body overfulls, max 16.94 pt (lines 197–198), none a
  pagination break — RECORDED, document-wide tolerance decision
  only, no rewording.
- M5: notation typeface split (line 33 upright text symbols vs
  $MPS^{RD}$; $\mathit{Post}_t$ once at line 196) — NOTATION PASS.
- M6: lead-in paragraphs before lists (lines 42, 54) — CHECKED
  CLEAN in Round 2: no overfull at lines 42–43 or 54–55 and no
  page-break complaint, so no keep-with-next guard. This CLOSES
  the Round 1 M4 open item (compile-time glance): no stranding
  evidence, no action.

## PASSES (Round 2, accepted)

Heading hierarchy (chapter → 7 sections → 2 subsections, no
skip); lists (identical bold-label spec, each restarts at 1);
chapter-number display confirmed Roman in body AND TOC
(preamble \thechapter = \Roman{chapter}, line 83; TOC
\thecontentslabel reproduces it); print hygiene clean
(no double spaces, ??, TODO, unescaped % or &); chapter
references consistently Roman in text.
