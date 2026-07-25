#!/usr/bin/env python3
"""Convert the arXiv LaTeX sources in papers/ into LLM-friendly Markdown in llm/.

For each paper directory:
  1. locate the main .tex file and recursively inline \\input / \\include
  2. strip TeX comments
  3. split preamble from body, keeping only macro definitions from the preamble
  4. rebuild a minimal document and run pandoc (latex+latex_macros -> markdown)
  5. fall back to lightly-cleaned LaTeX if pandoc chokes (old plain-TeX sources)

Output: llm/<slug>.md with YAML front matter from the arXiv metadata.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS = os.path.join(ROOT, "papers")
OUT = os.path.join(ROOT, "llm")

MACRO_RE = re.compile(
    r"^\s*\\(?:newcommand|renewcommand|providecommand|def|DeclareMathOperator"
    r"|newtheorem|newenvironment|let|newif|DeclareRobustCommand)\b"
)


def read(path):
    for enc in ("utf-8", "latin-1"):
        try:
            return open(path, encoding=enc).read()
        except UnicodeDecodeError:
            continue
    return open(path, encoding="utf-8", errors="replace").read()


def strip_comments(tex):
    out = []
    for line in tex.split("\n"):
        # a % ends the line unless escaped
        i, n = 0, len(line)
        cut = None
        while i < n:
            if line[i] == "\\":
                i += 2
                continue
            if line[i] == "%":
                cut = i
                break
            i += 1
        out.append(line if cut is None else line[:cut])
    # drop lines that became empty *and* were pure comments
    return "\n".join(out)


def inline(tex, base, depth=0):
    """Recursively expand \\input{f} and \\include{f}."""
    if depth > 6:
        return tex

    def repl(m):
        name = m.group(2).strip()
        for cand in (name, name + ".tex"):
            p = os.path.join(base, cand)
            if os.path.isfile(p):
                return "\n" + inline(strip_comments(read(p)), base, depth + 1) + "\n"
        return ""  # missing file (e.g. .bbl not shipped)

    return re.sub(r"\\(input|include)\s*\{([^}]*)\}", repl, tex)


def pick_main(d):
    texs = [
        os.path.join(dp, f)
        for dp, _, fs in os.walk(d)
        for f in fs
        if f.endswith(".tex")
    ]
    if not texs:
        return None
    scored = []
    for t in texs:
        s = read(t)
        score = (2 if "\\begin{document}" in s else 0) + (
            1 if "\\documentclass" in s or "\\documentstyle" in s else 0
        )
        scored.append((score, len(s), t))
    scored.sort(reverse=True)
    return scored[0][2]


def split_doc(tex):
    """Return (macro_lines, body). Handles plain-TeX files with no \\begin{document}."""
    m = re.search(r"\\begin\s*\{document\}", tex)
    if m:
        preamble, rest = tex[: m.start()], tex[m.end():]
        e = re.search(r"\\end\s*\{document\}", rest)
        body = rest[: e.start()] if e else rest
    else:
        # plain TeX: macro definitions live at the top, content follows
        preamble, body = "", re.split(r"\\bye\b", tex)[0]
    macros = [ln for ln in preamble.split("\n") if MACRO_RE.match(ln)]
    return macros, body


def clean_body(body):
    # strip layout / bookkeeping noise that carries no mathematical content
    for pat in (
        r"\\(?:thanks|footnotetext)\s*\{",  # handled crudely below
    ):
        pass
    body = re.sub(r"\\(?:vspace|hspace|vskip|hskip|smallskip|medskip|bigskip|"
                  r"newpage|clearpage|pagebreak|noindent|allowdisplaybreaks|"
                  r"maketitle|tableofcontents)\b\*?(\{[^}]*\}|\[[^\]]*\])?", "", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def match_group(s, open_idx):
    """Index just past the brace group starting at s[open_idx] == '{'."""
    depth, i, n = 0, open_idx, len(s)
    while i < n:
        c = s[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return -1


def repair(tex):
    """Neutralise constructs that pandoc's LaTeX reader refuses.

    - Zudilin's custom two-argument \\section(running head){title}
    - block environments nested inside \\textit / \\emph (Rivoal's CRAS note)
    """
    tex = re.sub(r"\\(section|subsection)\s*\((?:[^()]|\([^()]*\))*\)", r"\\\1", tex)
    for cmd in ("textit", "emph", "textbf"):
        pat = "\\" + cmd + "{"
        while True:
            i = tex.find(pat)
            found = False
            while i != -1:
                j = match_group(tex, i + len(pat) - 1)
                inner = tex[i + len(pat): j - 1] if j != -1 else ""
                if j != -1 and re.search(r"\\begin\{(itemize|enumerate|equation|align|description)", inner):
                    tex = tex[:i] + inner + tex[j:]
                    found = True
                    break
                i = tex.find(pat, i + 1)
            if not found:
                break
    return tex


def run_pandoc(src):
    try:
        r = subprocess.run(
            ["pandoc", "-f", "latex+latex_macros", "-t", "markdown-raw_tex",
             "--wrap=none", src],
            capture_output=True, text=True, timeout=240,
        )
    except subprocess.TimeoutExpired:
        return None, "pandoc timeout"
    if r.returncode != 0 or len(r.stdout) < 500:
        err = [l for l in (r.stderr or "").split("\n") if l.strip()
               and not l.startswith("[WARNING]")]
        return None, (err[0] if err else "empty output")
    return postprocess(r.stdout), None


def to_markdown(tex, macros, body, workdir):
    """Try, in order: the flattened source, a repaired copy, a minimal rebuild."""
    minimal = ("\\documentclass{article}\n\\usepackage{amsmath,amssymb,amsthm}\n"
               + "\n".join(macros) + "\n\\begin{document}\n" + body
               + "\n\\end{document}\n")
    attempts = [("flat", tex), ("repaired", repair(tex)), ("minimal", repair(minimal))]
    src = os.path.join(workdir, "_flat.tex")
    last = "no attempt"
    for name, text in attempts:
        with open(src, "w", encoding="utf-8") as f:
            f.write(text)
        md, err = run_pandoc(src)
        if md is not None:
            return md, name
        last = f"{name}: {err}"
    return None, last


def postprocess(md):
    md = re.sub(r"^:::+.*$", "", md, flags=re.M)          # pandoc div fences
    # [\[eq:3\]](#eq:3){reference-type="eqref" reference="eq:3"}  ->  (eq:3)
    md = re.sub(r"\[\\\[(.+?)\\\]\]\(#[^)]*\)(\{[^}]*\})?", r"(\1)", md)
    md = re.sub(r"\[([^\]\[]{1,60})\]\(#[^)]*\)(\{[^}]*\})?", r"\1", md)
    md = re.sub(r"\{reference-type=[^}]*\}", "", md)      # stray attribute blobs
    # pandoc sometimes falls back to raw HTML anchors for figure/table refs
    md = re.sub(r'<a href="#[^"]*"[^>]*>(.*?)</a>', r"\1", md, flags=re.S)
    md = re.sub(r'\s*data-reference(-type)?="[^"]*"', "", md)
    md = re.sub(r"\[\\\[[^\]]*\\\]\]\{[^}]*\}", "", md)   # [\[label\]]{#label} anchors
    md = re.sub(r"\{#[^}\s]+\}", "", md)                  # {#anchor}
    md = re.sub(r"\{\.[^}\s]+\}", "", md)                 # {.class}
    md = re.sub(r"\\\[([0-9]+)\\\]", r"[\1]", md)         # \[3\] -> [3]
    md = re.sub(r"[ \t]+$", "", md, flags=re.M)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def fallback(macros, body):
    """LaTeX is itself readable to an LLM; just present it cleanly."""
    head = ""
    if macros:
        head = ("<!-- macro definitions used below -->\n```latex\n"
                + "\n".join(macros) + "\n```\n\n")
    return head + "```latex\n" + body + "\n```"


def yaml_escape(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def main():
    meta = json.load(open(os.path.join(ROOT, "tools", "meta.json"), encoding="utf-8"))
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for slug in sorted(os.listdir(PAPERS)):
        d = os.path.join(PAPERS, slug)
        if not os.path.isdir(d):
            continue
        main_tex = pick_main(d)
        if not main_tex:
            print(f"!! no tex in {slug}")
            continue
        tex = inline(strip_comments(read(main_tex)), os.path.dirname(main_tex))
        macros, body = split_doc(tex)
        body = clean_body(body)
        md, how = to_markdown(tex, macros, body, d)
        mode = "pandoc-" + how
        if md is None:
            md, mode = fallback(macros, body), "latex-verbatim"
            print(f"   {slug}: pandoc fallback ({how})")

        m = meta.get(slug, {})
        fm = [
            "---",
            f"title: {yaml_escape(m.get('title', slug))}",
            "authors:",
        ] + [f"  - {yaml_escape(a)}" for a in m.get("authors", [])] + [
            f"arxiv_id: {yaml_escape(m.get('arxiv_id', ''))}",
            f"arxiv_url: {yaml_escape(m.get('url', ''))}",
            f"published: {yaml_escape(m.get('published', ''))}",
            f"journal_ref: {yaml_escape(m.get('journal_ref') or '')}",
            f"doi: {yaml_escape(m.get('doi') or '')}",
            f"source: {yaml_escape('papers/' + slug + '/' + os.path.basename(main_tex))}",
            f"conversion: {mode}",
            "---",
            "",
            f"# {m.get('title', slug)}",
            "",
            f"**{', '.join(m.get('authors', []))}**"
            + (f" — {m['journal_ref']}" if m.get("journal_ref") else ""),
            "",
            "## Abstract",
            "",
            m.get("abstract", "(not available)"),
            "",
            "---",
            "",
        ]
        text = "\n".join(fm) + md + "\n"
        path = os.path.join(OUT, slug + ".md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        rows.append((slug, mode, len(text)))

    print()
    total = 0
    for slug, mode, n in rows:
        total += n
        print(f"{slug:<60} {mode:<15} {n/1000:7.1f} kB  ~{n//4//1000:5d}k tok")
    print(f"\n{len(rows)} files, {total/1e6:.2f} MB, ~{total//4//1000}k tokens total")


if __name__ == "__main__":
    main()
