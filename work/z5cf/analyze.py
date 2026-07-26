"""Structural analysis of the compact forms:
 (a) shift-closure size = rank of the d-module that creative telescoping must close
     (every bare letter H^(r)_{linear} has RATIONAL n-, k- and l-differences, so the
     closure is exactly the set of sub-monomials);
 (b) distinct (argument, order) symbol count;
 (c) (H3) digit compatibility of every argument on the surviving set;
 (d) (H4) tameness verdict.
"""
import sys, os, json, itertools
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from design2 import monname
from bare import SYMNAME

HERE = os.path.dirname(os.path.abspath(__file__))

FORMS = {
    'w3 (7-term, minimal)': [((3, 3),), ((1, 1), (2, 3)), ((1, 2), (2, 3)),
                             ((1, 3), (2, 3)), ((1, 4), (2, 3)),
                             ((1, 5), (2, 3)), ((1, 6), (2, 3))],
    'w5 (27-term)': [tuple(tuple(x) for x in m)
                     for m in json.load(open(os.path.join(HERE, 'w5_bare.json')))['mons']],
}


def submonos(m):
    """all non-empty sub-multisets of the monomial m"""
    out = set()
    for r in range(1, len(m) + 1):
        for c in itertools.combinations(range(len(m)), r):
            out.add(tuple(sorted(m[i] for i in c)))
    return out


print('(a)(b) SIZE METRICS')
print('  %-24s %8s %8s %10s %10s' % ('form', 'terms', 'maxdeg', 'symbols', 'closure'))
for name, mons in FORMS.items():
    clo = set()
    syms = set()
    for m in mons:
        clo |= submonos(m)
        syms |= set(m)
    print('  %-24s %8d %8d %10d %10d'
          % (name, len(mons), max(len(m) for m in mons), len(syms), len(clo) + 1))
    print('      degree histogram: %s' % dict(sorted(Counter(len(m) for m in mons).items())))
    print('      symbols: %s' % sorted('H%d[%s]' % (r, SYMNAME[s]) for (r, s) in syms))

print('\n(c) (H3) DIGIT COMPATIBILITY  floor(x(n,k,l)/p) == x(a,b,c)  on the surviving set')
print('    surviving set (Theorem A, Lemma 4): r+s+t < p, with n=ap+r, k=bp+s, l=cp+t')
ARG = {'n': lambda n, k, l: n, 'k': lambda n, k, l: k, 'l': lambda n, k, l: l,
       'n+k': lambda n, k, l: n + k, 'n+l': lambda n, k, l: n + l,
       'n-k': lambda n, k, l: n - k, 'n-l': lambda n, k, l: n - l,
       'k+l': lambda n, k, l: k + l, 'n+k+l': lambda n, k, l: n + k + l}
for p in (7, 11, 13):
    bad = {}
    tot = 0
    for a in range(1, p):
        for r in range(p):
            n = a * p + r
            for b in range(a + 1):
                for s in range(p):
                    k = b * p + s
                    if k > n:
                        continue
                    for c in range(a + 1):
                        for t in range(p):
                            l = c * p + t
                            if l > n or r + s + t >= p:
                                continue
                            tot += 1
                            for nm, f in ARG.items():
                                if f(n, k, l) // p != f(a, b, c):
                                    bad[nm] = bad.get(nm, 0) + 1
    print('    p=%-3d cells=%-8d violations: %s' % (p, tot, bad if bad else 'NONE for any argument'))

print('\n(d) (H4) TAMENESS  (0 <= x(n,k,l) <= n required)')
for nm, f in ARG.items():
    worst = max(f(20, k, l) for k in range(21) for l in range(21))
    print('    %-8s max over the cell range at n=20 : %-4d  %s'
          % (nm, worst, 'TAME' if worst <= 20 else 'NOT TAME (reaches %gn)' % (worst / 20)))
