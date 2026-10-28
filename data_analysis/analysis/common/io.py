"""Fail-closed I/O helpers shared by loaders and renderers.

Every read validates presence and columns, naming the offending file; every
write is atomic (tempfile + os.replace + fsync) so a failed run never leaves a
half-written figure or table behind.
"""
from __future__ import annotations

import contextlib
import hashlib
import os
import tempfile
from pathlib import Path

import pandas as pd


def read_csv_strict(path: Path, required: tuple[str, ...]) -> pd.DataFrame:
    if not path.is_file():
        raise FileNotFoundError(f"Required analysis input is missing: {path}")
    frame = pd.read_csv(path)
    missing = [name for name in required if name not in frame.columns]
    if missing:
        raise ValueError(f"{path}: missing required column(s): {', '.join(missing)}")
    return frame


def to_numeric_strict(
    frame: pd.DataFrame, columns: tuple[str, ...], source: Path
) -> pd.DataFrame:
    out = frame.copy()
    for name in columns:
        raw = out[name]
        converted = pd.to_numeric(raw, errors="coerce")
        bad = converted.isna() & raw.notna() & (raw.astype(str).str.strip() != "")
        if bad.any():
            first = bad.idxmax()
            line = int(first) + 2  # data row 0 sits on CSV line 2 (after the header)
            raise ValueError(
                f"{source}: column {name!r} line {line}: "
                f"cannot parse {raw.loc[first]!r} as a number"
            )
        out[name] = converted
    return out


def to_bool_strict(
    frame: pd.DataFrame, column: str, source: Path
) -> pd.DataFrame:
    out = frame.copy()
    raw = out[column]
    if raw.dtype == bool:
        return out
    mapped = raw.astype(str).str.strip().str.lower().map({"true": True, "false": False})
    if mapped.isna().any():
        first = mapped.isna().idxmax()
        line = int(first) + 2
        raise ValueError(
            f"{source}: column {column!r} line {line}: "
            f"expected true/false, got {raw.loc[first]!r}"
        )
    out[column] = mapped
    return out


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(dir=str(path.parent), suffix=path.suffix + ".tmp")
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    except BaseException:
        with contextlib.suppress(FileNotFoundError):
            tmp.unlink()
        raise


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()
