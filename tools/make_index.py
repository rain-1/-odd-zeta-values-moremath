#!/usr/bin/env python3
"""Build llm/INDEX.md — a machine-readable manifest of the converted corpus."""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LLM = os.path.join(ROOT, "llm")


def front_matter(path):
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", txt, re.S)
    fm = {}
    if m:
        for line in m.group(1).split("\n"):
            k, _, v = line.partition(":")
            if _ and not k.startswith(" "):
                fm[k.strip()] = v.strip().strip('"')
    return fm, len(txt)


def main():
    files = sorted(f for f in os.listdir(LLM) if f.endswith(".md") and f != "INDEX.md")
    rows = []
    for f in files:
        fm, n = front_matter(os.path.join(LLM, f))
        rows.append((f, fm, n))

    total = sum(n for _, _, n in rows)
    out = [
        "# Corpus manifest",
        "",
        f"{len(rows)} documents · {total/1e6:.2f} MB · ~{total//4//1000}k tokens "
        "(rough 4 chars/token estimate).",
        "",
        "Each file carries YAML front matter with `title`, `authors`, `arxiv_id`, "
        "`arxiv_url`, `published`, `source` and `conversion`.",
        "",
        "| file | ~tokens | year | conversion | title |",
        "|---|---|---|---|---|",
    ]
    for f, fm, n in rows:
        title = fm.get("title", f).replace("|", "\\|")
        year = (fm.get("published") or "")[:4]
        out.append(
            f"| `{f}` | {n//4//1000}k | {year} | {fm.get('conversion','')} | {title} |"
        )

    out += [
        "",
        "## Conversion modes",
        "",
        "- `pandoc-flat` — arXiv LaTeX flattened (`\\input` inlined, comments stripped) "
        "and converted by pandoc. Math is preserved as LaTeX inside `$`/`$$`.",
        "- `pandoc-repaired` — same, after neutralising constructs pandoc's reader "
        "rejects (custom `\\section(...)` arguments, block environments nested in "
        "`\\textit`).",
        "- `latex-verbatim` — pandoc could not parse the source; the cleaned LaTeX is "
        "included verbatim in a fenced block. Still readable, just noisier.",
        "- `pdftotext -layout` — no TeX source exists. Formulas are flattened to "
        "approximate plain text and are **lossy**; consult the PDF for anything "
        "load-bearing.",
        "",
        "## Not converted",
        "",
        "Four PDFs use PostScript-era Type-3 / bitmap fonts with no `ToUnicode` map, "
        "so no usable text can be extracted. They remain in `books-and-surveys/` as "
        "PDFs only:",
        "",
        "- `zudilin-2001-one-of-zeta5-7-9-11-is-irrational.pdf` (Russian) — the result "
        "itself is fully developed in `04-zudilin-2002-arithmetic-of-linear-forms.md`",
        "- `zudilin-2001-one-of-eight-zeta5-to-zeta19.pdf`",
        "- `zudilin-2001-irrationality-odd-integer-points-brief.pdf` (Russian)",
        "- `zudilin-2003-algebraic-relations-for-mzv-survey.pdf` — superseded for "
        "reading purposes by `zudilin-MZV-tasting-notes.md`",
        "",
        "Regenerate everything with: `python3 tools/tex2llm.py && "
        "python3 tools/pdf2llm.py && python3 tools/make_index.py`",
        "",
    ]
    with open(os.path.join(LLM, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"wrote llm/INDEX.md — {len(rows)} documents, ~{total//4//1000}k tokens")


if __name__ == "__main__":
    main()
