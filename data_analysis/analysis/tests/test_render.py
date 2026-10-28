"""Renderer contracts: table twins (booktabs LaTeX + markdown) and figure
twins (PDF + PNG), exercised on the synthetic study.
"""
from __future__ import annotations

from analysis.assets import ASSET_REGISTRY, load_generator
from analysis.dataset import build_dataset
from analysis.render.tables import Table, save_table


def _table() -> Table:
    return Table(
        id="T_test",
        caption="A test table with 50% and under_scores",
        headers=("Term", "Coef", "p"),
        rows=(("beta(EPS)", "2.095", "<0.001"), ("beta(BVPS)", "0.219", "0.904")),
        notes="HC3 standard errors; exploratory.",
    )


def test_table_latex_uses_booktabs_and_escapes(tmp_path, monkeypatch) -> None:
    latex = _table().to_latex()
    assert r"\toprule" in latex and r"\midrule" in latex and r"\bottomrule" in latex
    assert r"\caption{A test table with 50\% and under\_scores}" in latex
    assert r"\label{tab:t_test}" in latex
    assert "Notes:" in latex


def test_table_markdown_twin() -> None:
    markdown = _table().to_markdown()
    assert markdown.startswith("**A test table with 50% and under_scores**")
    assert "| Term | Coef | p |" in markdown
    assert "| beta(BVPS) | 0.219 | 0.904 |" in markdown


def test_save_table_writes_both_twins(synthetic_study) -> None:
    paths = save_table(_table(), "tables/T_test")
    assert len(paths) == 2
    for path in paths:
        assert path.is_file() and path.stat().st_size > 0
    assert {path.suffix for path in paths} == {".tex", ".md"}


def test_figure_save_writes_pdf_and_png(synthetic_study) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    from analysis.render.figures import save

    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    paths = save(fig, "figures/main/F_test")
    assert {path.suffix for path in paths} == {".pdf", ".png"}
    for path in paths:
        assert path.is_file() and path.stat().st_size > 0


def test_registry_assets_render_on_synthetic_study(synthetic_study) -> None:
    """Every asset must generate end-to-end on a well-formed synthetic study."""
    ds = build_dataset(strict=True)
    for spec in ASSET_REGISTRY.values():
        outputs = load_generator(spec)(ds)
        assert outputs, spec.id
        for path in outputs:
            assert path.is_file() and path.stat().st_size > 0, (spec.id, path)
