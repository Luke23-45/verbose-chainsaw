# Front-matter loop — Round 4 review (the loop catches its own error)

Method: LaTeX-accurate analytic page fit, after discovering that the
first visual mock was wrong. The mock used 18 pt body leading; the
real LaTeX 12 pt class with \setstretch{1.5} gives 14.5 × 1.5 = 21.75 pt
per body line, and it also duplicated each heading. The mock is
discarded. The analytic check (workspace/frontmatter_build/
analytic_fit.py) wraps each paragraph with Liberation Serif widths
(metric-compatible with Times New Roman) at the true text width
(433.13 pt) and sums: heading 18 pt + stated gap + lines × 21.75 pt +
10 pt paragraph gaps + signature/table blocks at single spacing.
It does not hyphenate, so it is conservative: LaTeX hyphenation can
save at most about one line per page.

## Finding: Round 1 broke two pages it tried to tidy

Round 1 standardised heading gaps to 1.5 cm and paragraph gaps to
10 pt on Acknowledgements and Abstract, calling the smaller original
values inconsistent. That was wrong. The original small values were
fit-driven, and the standardised values spill both pages:

- Acknowledgements, Round 1 spacing: 731.0 pt against a 697.9 pt text
  height — spills by 33.1 pt (1.5 body lines). With the original
  0.2 cm gap and 3 pt paragraph gaps it totals ≈ 666 pt and fits by
  ≈ 32 pt.
- Abstract, Round 1 spacing: 721.2 pt after correcting a double count
  of the keywords paragraph in the first analytic run — spills by
  23.3 pt (1.1 body lines). With the original 0.1 cm gap and 3 pt
  paragraph gaps it totals ≈ 667 pt and fits by ≈ 31 pt. The abstract
  is the one front page FOM explicitly limits to one page, so a
  1-line spill there is a hard failure, not a preference.
- Abbreviations, Round 1 spacing (0.8 cm gap, 48 rows): 645.2 pt,
  fits by 52.7 pt, with only one row (HC3) wrapping to two lines.
  The earlier mock spill for this list was a mock artefact (14.5 pt
  per table row instead of the true 12 pt first line + 14.5 pt per
  further line). No change.
- Authorship (419 pt), Research Committee (≈ 513 pt, counting its
  table and dates once), Approval Sheet (≈ 440 pt): fit comfortably
  at 1.5 cm / 10 pt. No change.

## Round 4 fix

Revert Acknowledgements and Abstract to their original fit-driven
spacing, and document the exception in the files so the next reviewer
does not "standardise" them again:
- acknowledgements.tex: heading gap back to 0.2 cm, local 3 pt
  paragraph gap restored.
- abstract.tex: heading gap back to 0.1 cm, local 3 pt paragraph gap
  restored.
- abbreviations.tex: 0.8 cm gap already documented; no change.

Principle recorded for the rest of the loop: a documented fit
exception beats visual uniformity. A page spill is a defect; a
different heading gap on a long page is not, once it is documented.

## Round 4 fix list

Revert the two spacing changes above, then re-run the analytic fit.
The real LaTeX compile (TeX install still running) remains the final
gate: if it shows either page spilling despite the analytic fit, the
next fix is prose trimming of that page, not another spacing change.
