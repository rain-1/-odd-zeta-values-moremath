"""Guard against the `math < file.wl` line-truncation trap.

`math` (and the Wolfram MCP evaluator) read input LINE BY LINE and evaluate each line
as soon as it parses.  A multi-line expression whose first line is already balanced is
silently truncated and the continuation lines are evaluated and discarded.

This flags any line that (a) is bracket-balanced, (b) does not end in `;`, `[`, `,`, or
an operator, and (c) is followed by a line starting with a binary operator.
Run:  python3 wlcheck.py *.wl
"""
import sys, re

OPS = ('+', '-', '*', '/', '^', '.', ',', '&&', '||', '==', '=!=', '<>')

def balanced(s):
    d = 0
    instr = False
    prev = ''
    for ch in s:
        if instr:
            if ch == '"' and prev != '\\':
                instr = False
        elif ch == '"':
            instr = True
        elif ch in '([{':
            d += 1
        elif ch in ')]}':
            d -= 1
        prev = ch
    return d

def assoc_delta(s):
    """<| ... |> nesting change on this line, ignoring string literals.

    A line that leaves this unbalanced is FATAL under `math < file`: the reader
    emits `Syntax::sntxf: "" cannot be followed by "...= <|"` and silently drops
    the whole assignment.  Observed 2026-07-25 on certP.wl; the resulting Symbol
    then propagates into the summand, so two kernels telescoped a wrong object.
    """
    d, i, instr, prev = 0, 0, False, ''
    while i < len(s):
        ch = s[i]
        if instr:
            if ch == '"' and prev != '\\':
                instr = False
        elif ch == '"':
            instr = True
        elif s[i:i+2] == '<|':
            d += 1; i += 1
        elif s[i:i+2] == '|>':
            d -= 1; i += 1
        prev = ch
        i += 1
    return d

def strip_comments(text):
    out, i, d = [], 0, 0
    while i < len(text):
        if text[i:i+2] == '(*':
            d += 1; i += 2
        elif text[i:i+2] == '*)':
            d -= 1; i += 2
        else:
            out.append(' ' if d > 0 and text[i] != '\n' else text[i]); i += 1
    return ''.join(out)


for fn in sys.argv[1:]:
    lines = strip_comments(open(fn).read()).split('\n')
    depth = 0
    adepth = 0
    bad = []
    afail = []
    for i, ln in enumerate(lines):
        code = ln
        depth += balanced(code)
        adepth += assoc_delta(code)
        if adepth != 0:
            # FATAL only when the line ENDS at the "<|" token: `x = <|` is a
            # locally-decidable syntax error for the stdin reader ("<" and "|"
            # are also standalone operators), whereas `x = <|"a" -> 1,` is
            # merely incomplete and continues correctly.
            if code.rstrip().endswith('<|'):
                afail.append((i + 1, code.strip()[:70]))
            adepth = 0
        st = code.strip()
        if depth == 0 and st and not st.endswith((';', '[', '(', ',')) \
           and not st.endswith(OPS) and i + 1 < len(lines):
            nxt = lines[i + 1].strip()
            if nxt.startswith(OPS):
                bad.append((i + 1, st[:70], nxt[:50]))
    status = 'OK'
    if afail:
        status = 'ASSOCIATION SPLIT ACROSS LINES (FATAL under `math < file`)'
    elif bad:
        status = 'TRUNCATION RISK'
    print('%-28s %s' % (fn, status))
    for ln, a in afail:
        print('    line %d: unbalanced <| ... |>  %r' % (ln, a))
    for ln, a, b in bad:
        print('    line %d: %r  followed by  %r' % (ln, a, b))
