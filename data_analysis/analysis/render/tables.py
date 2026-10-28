"""Table rendering: one Table object, two outputs (booktabs .tex + .md twin).

Both twins are written atomically.  LaTeX output uses booktabs rules, escapes
the reserved characters %_&$#, and carries caption, label and a footnotesize
notes block — ready to \\input into the thesis.  The markdown twin mirrors the
same content for quick reading and review.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from analysis.common import config
from analysis.common.io import atomic_write_text

_LATEX_ESCAPE = str.maketrans(
    {
        "%": r"\%",
        "&": r"\&",
        "#": r"\#",
        "$": r"\$",
        "_": r"\_",
    }
)


def _escape_latex(text: str) -> str:
    return text.translate(_LATEX_ESCAPE)


@dataclass(frozen=True)
class Table:
    id: str
    caption: str
    headers: tuple[str, ...]
    rows: tuple[tuple[str, ...], ...]
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.headers:
            raise ValueError(f"{self.id}: table needs at least one column")
        for i, row in enumerate(self.rows):
            if len(row) != len(self.headers):
                raise ValueError(
                    f"{self.id}: row {i} has {len(row)} cells, expected {len(self.headers)}"
                )

    def _label(self) -> str:
        return "tab:" + self.id.lower()

    def to_markdown(self) -> str:
        lines = [f"**{self.caption}**", ""]
        lines.append("| " + " | ".join(self.headers) + " |")
        lines.append("|" + "|".join(["---"] * len(self.headers)) + "|")
        for row in self.rows:
            lines.append("| " + " | ".join(row) + " |")
        if self.notes:
            lines += ["", f"*Notes: {self.notes}*"]
        return "\n".join(lines) + "\n"

    def to_latex(self) -> str:
        colspec = "l" + "r" * (len(self.headers) - 1)
        lines = [
            r"\begin{table}[htbp]",
            r"\centering",
            rf"\caption{{{_escape_latex(self.caption)}}}",
            rf"\label{{{self._label()}}}",
            rf"\begin{{tabular}}{{{colspec}}}",
            r"\toprule",
            " & ".join(_escape_latex(h) for h in self.headers) + r" \\",
            r"\midrule",
        ]
        for row in self.rows:
            lines.append(" & ".join(_escape_latex(cell) for cell in row) + r" \\")
        if self.notes:
            width = len(self.headers)
            lines.append(r"\midrule")
            lines.append(
                rf"\multicolumn{{{width}}}{{l}}{{\footnotesize Notes: {_escape_latex(self.notes)}}} \\"
            )
        lines += [r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]
        return "\n".join(lines)


def save_table(table: Table, relative: str) -> list[Path]:
    base = config.paper_root() / relative
    tex = base.with_suffix(".tex")
    md = base.with_suffix(".md")
    atomic_write_text(tex, table.to_latex())
    atomic_write_text(md, table.to_markdown())
    return [tex, md]
