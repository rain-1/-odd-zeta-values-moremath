#!/usr/bin/env bash
set -euo pipefail

MAXIMA_BIN="${MAXIMA_BIN:-/home/ubuntu/.local/opt/open-math/usr/bin/maxima}"
ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT_DIR"

"$MAXIMA_BIN" --very-quiet -b work/s7_param/extract_u.mac \
  > /tmp/s7-extract-u.log 2>&1
"$MAXIMA_BIN" --very-quiet -b work/s7_param/extract_v.mac \
  > /tmp/s7-extract-v.log 2>&1
"$MAXIMA_BIN" --very-quiet -b work/s7_param/extract_diag.mac \
  > /tmp/s7-extract-diag.log 2>&1

python work/s7_param/ore_eliminate.py
python work/s7_param/check_formula.py
