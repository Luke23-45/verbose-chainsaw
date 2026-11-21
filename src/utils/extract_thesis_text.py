#!/usr/bin/env python3
"""Concatenate the thesis chapter .tex files into one UTF-8 .txt file."""

from __future__ import annotations

import argparse
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
CHAPTERS_DIR = REPOSITORY_ROOT / "src" / "thesis" / "chapters"
DEFAULT_OUTPUT = CHAPTERS_DIR / "all_chapters.txt"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Merge chapter_*.tex files into one text file, in filename order."
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output .txt path (default: {DEFAULT_OUTPUT})",
    )
    args = parser.parse_args()

    chapter_files = sorted(CHAPTERS_DIR.glob("chapter_*.tex"))
    if not chapter_files:
        parser.error(f"No chapter_*.tex files found in {CHAPTERS_DIR}")

    sections: list[str] = []
    for chapter_file in chapter_files:
        content = chapter_file.read_text(encoding="utf-8").rstrip()
        sections.append(f"===== {chapter_file.name} =====\n\n{content}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n\n".join(sections) + "\n", encoding="utf-8")

    print("Merged chapter files:")
    for chapter_file in chapter_files:
        print(f"  {chapter_file.name}")
    print(f"Text saved to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
