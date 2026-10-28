"""CLI: render registered assets from the frozen extraction inputs.

Usage (from data_analysis/):
    python -m analysis.scripts.generate --check
    python -m analysis.scripts.generate
    python -m analysis.scripts.generate --asset T3,F4
    python -m analysis.scripts.generate --section appendix --figures-only
    python -m analysis.scripts.generate --allow-partial

The dataset is built once; each asset is generated in isolation so one failure
does not kill the run (failures are collected and the exit code is 1).  Every
successful output is recorded in generation_manifest.json with its sha256, so
scripts.verify can detect drift afterwards.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys

from analysis.assets import ASSET_REGISTRY, load_generator
from analysis.common import config
from analysis.common.io import atomic_write_text, sha256_file
from analysis.dataset import build_dataset

LOG_FORMAT = "%(levelname)-7s %(name)s | %(message)s"
LOG = logging.getLogger("generate")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m analysis.scripts.generate",
        description="Render thesis figures and tables from the frozen extraction inputs.",
    )
    parser.add_argument("--asset", help="comma-separated asset ids, e.g. T3,F4")
    parser.add_argument("--section", choices=("main", "appendix"), help="restrict to one section")
    parser.add_argument("--figures-only", action="store_true", help="render figure assets only")
    parser.add_argument("--tables-only", action="store_true", help="render table assets only")
    parser.add_argument(
        "--check", action="store_true",
        help="build the dataset and report coverage only; write no outputs",
    )
    parser.add_argument(
        "--allow-partial", action="store_true",
        help="build the dataset leniently (absent cells reported, not raised) and keep "
             "going when an individual asset fails",
    )
    return parser.parse_args(argv)


def select_specs(args: argparse.Namespace) -> list:
    specs = list(ASSET_REGISTRY.values())
    if args.asset:
        wanted = [token.strip().upper() for token in args.asset.split(",") if token.strip()]
        unknown = [token for token in wanted if token not in ASSET_REGISTRY]
        if unknown:
            raise SystemExit(f"unknown asset id(s): {', '.join(unknown)}")
        specs = [ASSET_REGISTRY[token] for token in wanted]
    if args.section:
        specs = [spec for spec in specs if spec.section == args.section]
    if args.figures_only:
        specs = [spec for spec in specs if spec.kind == "figure"]
    if args.tables_only:
        specs = [spec for spec in specs if spec.kind == "table"]
    return specs


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    specs = select_specs(args)

    dataset = build_dataset(strict=not args.allow_partial)
    LOG.info(dataset.coverage.summary())
    coverage = {
        "intended": dataset.coverage.intended,
        "realized": dataset.coverage.realized,
        "realized_pre": dataset.coverage.realized_pre,
        "realized_post": dataset.coverage.realized_post,
        "window_excluded": [f"{c.bank}/{c.fy}" for c in dataset.coverage.window_excluded_cells],
        "entity_mismatch": [f"{c.bank}/{c.fy}" for c in dataset.coverage.entity_mismatch_cells],
    }
    if args.check:
        LOG.info("check: %d assets selected, no outputs written", len(specs))
        return 0

    manifest = {
        "argv": sys.argv[1:],
        "coverage": coverage,
        "assets": {},
    }
    failures: list[str] = []
    for spec in specs:
        try:
            generator = load_generator(spec)
            outputs = generator(dataset)
            manifest["assets"][spec.id] = {
                "title": spec.title,
                "outputs": [
                    {"path": str(path), "sha256": sha256_file(path)} for path in outputs
                ],
            }
            LOG.info("%-4s OK    %s", spec.id, ", ".join(path.name for path in outputs))
        except Exception as exc:  # noqa: BLE001 - one failed asset must not kill the run
            failures.append(spec.id)
            LOG.error("%-4s FAILED  %s: %s", spec.id, type(exc).__name__, exc)

    manifest_path = config.manifest_path()
    atomic_write_text(manifest_path, json.dumps(manifest, indent=2) + "\n")
    LOG.info("manifest: %s (%d assets ok, %d failed)", manifest_path, len(specs) - len(failures), len(failures))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
