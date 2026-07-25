#!/bin/sh
# Build script for papers_out/lucas2nd.
# Plain pdflatex, three passes (TOC + cross-references + hyperref bookmarks).
# No bibtex: the bibliography is a manual thebibliography environment in refs.tex.
set -e
cd "$(dirname "$0")"
: > build.log
for pass in 1 2 3; do
  echo "===== pdflatex pass $pass =====" >> build.log
  pdflatex -interaction=nonstopmode -file-line-error main.tex >> build.log 2>&1
done
echo "===== summary =====" >> build.log
grep -a "Output written" main.log >> build.log || true
printf 'overfull/underfull boxes: ' >> build.log
grep -a -c "Overfull\|Underfull" main.log >> build.log || true
printf 'undefined references/citations: ' >> build.log
grep -a -c -i "undefined" main.log >> build.log || true
tail -6 build.log
