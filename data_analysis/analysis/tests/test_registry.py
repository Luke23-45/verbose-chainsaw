"""Registry integrity and renderer contracts (no real data needed)."""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

from analysis.assets import ASSET_REGISTRY, load_generator


def test_registry_ids_unique_and_complete() -> None:
    assert len(ASSET_REGISTRY) == 18
    ids = set(ASSET_REGISTRY)
    assert {f"T{i}" for i in range(1, 7)} <= ids
    assert {f"F{i}" for i in range(1, 7)} <= ids
    assert {f"A{i}" for i in range(1, 7)} <= ids


def test_every_spec_module_loads_with_generator() -> None:
    for spec in ASSET_REGISTRY.values():
        generator = load_generator(spec)
        assert callable(generator), spec.id


def test_output_paths_match_kind_and_section() -> None:
    for spec in ASSET_REGISTRY.values():
        for relative in spec.outputs:
            expected_prefix = "figures/main" if (spec.kind, spec.section) == ("figure", "main") \
                else "figures/appendix" if spec.kind == "figure" \
                else "tables"
            assert relative.startswith(expected_prefix + "/"), (spec.id, relative)
            suffix = relative.rsplit(".", 1)[-1]
            expected_suffixes = {"pdf", "png"} if spec.kind == "figure" else {"tex", "md"}
            assert suffix in expected_suffixes, (spec.id, relative)
