"""Exact-Q solve on a PRESCRIBED monomial support, with held-out verification.
Usage: fixsupp.py W KEY NFIT  'mono;mono;...'    (mono = 'r:sym,r:sym')
Symbols: 0 n, 1 k, 2 l, 3 n+k, 4 n+l, 5 n-k, 6 n-l, 7 k+l, 8 n+k+l
"""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import T, Hs, Ph, P, Q
from design2 import monname

W = int(sys.argv[1]); KEY = sys.argv[2]; NFIT = int(sys.argv[3])
MONS = [tuple(sorted(tuple(int(y) for y in x.split(':')) for x in m.split(',')))
        for m in sys.argv[4].split(';') if m]
LAD = {'Ph': Ph, 'P': P, 'Q': Q}[KEY]
IDXF = [lambda n, k, l: n, lambda n, k, l: k, lambda n, k, l: l,
        lambda n, k, l: n + k, lambda n, k, l: n + l, lambda n, k, l: n - k,
        lambda n, k, l: n - l, lambda n, k, l: k + l, lambda n, k, l: n + k + l]
for m in MONS:
    assert sum(r for r, s in m) == W, ('bad weight', m)
print('%d monomials: %s' % (len(MONS), [monname(m) for m in MONS]))


def row(n):
    out = [F(0)] * len(MONS)
    for k in range(n + 1):
        for l in range(n + 1):
            t = T(n, k, l)
            idx = [f(n, k, l) for f in IDXF]
            for j, m in enumerate(MONS):
                v = F(t)
                for (r, s) in m:
                    v *= Hs(idx[s], r)
                out[j] += v
    return out


rows = [row(n) for n in range(NFIT + 1)]
rhs = [LAD(n) for n in range(NFIT + 1)]
M = [rows[i][:] + [rhs[i]] for i in range(len(rows))]
nc = len(MONS)
piv, r = [], 0
for c in range(nc):
    p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
    if p is None:
        continue
    M[r], M[p] = M[p], M[r]
    iv = M[r][c]
    M[r] = [x / iv for x in M[r]]
    for i in range(len(M)):
        if i != r and M[i][c] != 0:
            f = M[i][c]
            M[i] = [M[i][j] - f * M[r][j] for j in range(nc + 1)]
    piv.append(c); r += 1
inc = any(all(M[i][j] == 0 for j in range(nc)) and M[i][nc] != 0 for i in range(r, len(M)))
print('rank %d / %d cols, %d eqs, inconsistent=%s' % (r, nc, len(rows), inc))
if inc:
    sys.exit()
x = [F(0)] * nc
for i, c in enumerate(piv):
    x[c] = M[i][nc]
print('SOLUTION:')
for j in range(nc):
    print('   %-30s %s' % (monname(MONS[j]), x[j]))
bad = []
for n in list(range(NFIT + 1, NFIT + 6)) + [30, 34]:
    rv = row(n)
    if sum(x[j] * rv[j] for j in range(nc)) != LAD(n):
        bad.append(n)
print('held-out n=%d..%d,30,34 : %s' % (NFIT + 1, NFIT + 5, 'ALL PASS' if not bad else 'FAIL %s' % bad))
