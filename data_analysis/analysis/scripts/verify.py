"""CLI: post-generation contract check.

For every registry entry: each declared output must exist and be non-empty;
where generation_manifest.json records a sha256, the file on disk must still
hash to it.  Exits 0 when the contract holds, 1 otherwise, printing every
problem found.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path

from analysis.assets import ASSET_REGISTRY
from analysis.common import config
from analysis.common.io import sha256_file

LOG_FORMAT = "%(levelname)-7s %(name)s | %(message)s"
LOG = logging.getLogger("verify")


def main(argv: list[str] | None = None) -> int:
    del argv  # kept for a uniform CLI surface
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    paper_root = config.paper_root()
    manifest_path = config.manifest_path()

    recorded: dict[str, str] = {}  # output path (both absolute and relative) -> recorded sha256
    if manifest_path.is_file():
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        for entry in data.get("assets", {}).values():
            for output in entry.get("outputs", []):
                p_str = output.get("path")
                sha = output.get("sha256")
                if p_str and sha:
                    p = Path(p_str)
                    if p.is_absolute():
                        recorded[str(p)] = sha
                        try:
                            recorded[str(p.relative_to(paper_root)).replace("\\", "/")] = sha
                        except ValueError:
                            pass
                    else:
                        recorded[str(paper_root / p)] = sha
                        recorded[str(p).replace("\\", "/")] = sha
        LOG.info("manifest: %s (%d outputs recorded)", manifest_path, len(recorded))
    else:
        LOG.warning("manifest not found: %s (run generate first; presence checks only)", manifest_path)

    problems: list[str] = []
    for asset_id, spec in ASSET_REGISTRY.items():
        for relative in spec.outputs:
            path = paper_root / relative
            if not path.is_file():
                problems.append(f"{asset_id}: missing output {relative}")
                continue
            if path.stat().st_size == 0:
                problems.append(f"{asset_id}: empty output {relative}")
                continue
            expected = recorded.get(str(path)) or recorded.get(str(relative).replace("\\", "/"))
            if expected and sha256_file(path) != expected:
                problems.append(f"{asset_id}: sha256 drift for {relative}")

    for problem in problems:
        LOG.error("%s", problem)
    if problems:
        LOG.error("verify: %d problem(s)", len(problems))
        return 1
    LOG.info("verify: %d assets, all declared outputs present and consistent", len(ASSET_REGISTRY))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
