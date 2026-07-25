#!/bin/sh
# Build the paper: three pdflatex passes (toc + cross-references + hyperref).
set -e
cd "$(dirname "$0")"
for i in 1 2 3; do
  pdflatex -interaction=nonstopmode -halt-on-error padicmap.tex > build-pass$i.log 2>&1 \
    || { echo "pass $i FAILED"; tail -40 build-pass$i.log; exit 1; }
done
echo "--- undefined references / citations ---"
grep -E "Warning.*(undefined|Undefined)" build-pass3.log || echo "none"
echo "--- overfull/underfull count ---"
grep -c "Overfull" build-pass3.log || true
