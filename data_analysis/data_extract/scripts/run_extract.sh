#!/usr/bin/env bash
# Full extraction run, in order. Stops at the first failing stage.
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONPATH=src
python -m data_extract.cli discover
python -m data_extract.cli extract
python -m data_extract.cli validate
