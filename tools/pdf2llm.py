#!/usr/bin/env python3
"""Extract text from the PDF-only items in books-and-surveys/ into llm/.

Several of these are PostScript-era files with Type-3 / bitmap fonts and no
ToUnicode map, so pdftotext yields garbage. We detect that and skip rather than
write unusable text, recording the reason in the output index.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "books-and-surveys")
OUT = os.path.join(ROOT, "llm")

# Words that should show up in any real English/French maths paper.
PROBE = re.compile(
    r"\b(the|and|for|that|with|proof|theorem|lemma|zeta|irrational|"          # en
    r"nous|nombres|est|des|une|soit|pour|dans|que|par|les|sur|avec|"          # fr
    r"donc|cette|nombre)\b",
    re.I,
)
MIN_WORDS_PER_KB = 3.0


def legible(text):
    """Heuristic: real prose has many common words and few control chars."""
    if len(text) < 400:
        return False, "too little text extracted"
    hits = len(PROBE.findall(text))
    per_kb = hits / (len(text) / 1000)
    ctrl = sum(1 for c in text if ord(c) < 9 or 11 <= ord(c) < 32)
    if ctrl / len(text) > 0.02:
        return False, f"{ctrl} control characters (bitmap/Type-3 font)"
    if per_kb < MIN_WORDS_PER_KB:
        return False, f"only {per_kb:.1f} common words per kB (no ToUnicode map)"
    return True, f"{per_kb:.0f} common words/kB"


def main():
    os.makedirs(OUT, exist_ok=True)
    for f in sorted(os.listdir(SRC)):
        if not f.endswith(".pdf"):
            continue
        path = os.path.join(SRC, f)
        r = subprocess.run(["pdftotext", "-layout", path, "-"],
                           capture_output=True, text=True, errors="replace")
        text = r.stdout
        ok, why = legible(text)
        slug = f[:-4]
        if not ok:
            print(f"SKIP  {slug:<58} {why}")
            continue
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"[ \t]+$", "", text, flags=re.M)
        header = (
            "---\n"
            f'title: "{slug}"\n'
            f'source: "books-and-surveys/{f}"\n'
            "conversion: pdftotext -layout\n"
            "note: \"extracted text; formulas are flattened and may be lossy — "
            "check the PDF for anything load-bearing\"\n"
            "---\n\n"
        )
        with open(os.path.join(OUT, slug + ".md"), "w", encoding="utf-8") as fh:
            fh.write(header + text.strip() + "\n")
        print(f"OK    {slug:<58} {len(text)/1000:6.1f} kB  ({why})")


if __name__ == "__main__":
    main()
