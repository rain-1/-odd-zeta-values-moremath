"""Exact-Q extraction of the compact weight-3 form in the 5-symbol bare alphabet
   {H_n, H_k, H_l, H_{n+k}, H_{n+l}},  degree <= 2.   16 symmetric columns."""
import sys, os, itertools
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import T, Hs, Ph, P, Q
from design2 import monomials, sym_orbits, monname, SIGMA

W = int(sys.argv[1]) if len(sys.argv) > 1 else 3
KEY = sys.argv[2] if len(sys.argv) > 2 else 'Ph'
DMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 2
SYMSET = tuple(int(x) for x in sys.argv[4].split(',')) if len(sys.argv) > 4 else (0, 1, 2, 3, 4)
NFIT = int(sys.argv[5]) if len(sys.argv) > 5 else 24

LAD = {'Ph': Ph, 'P': P, 'Q': Q}[KEY]
IDXF = [lambda n, k, l: n, lambda n, k, l: k, lambda n, k, l: l,
        lambda n, k, l: n + k, lambda n, k, l: n + l, lambda n, k, l: n - k,
        lambda n, k, l: n - l, lambda n, k, l: k + l, lambda n, k, l: n + k + l]

mons = sym_orbits(monomials(W, DMAX, SYMSET))
print('%d symmetric monomials (W=%d, deg<=%d, syms=%s)' % (len(mons), W, DMAX, SYMSET))
for m in mons:
    print('   ', monname(m))


def rowvals(n):
    out = [F(0)] * len(mons)
    for k in range(n + 1):
        for l in range(n + 1):
            t = T(n, k, l)
            idx = [f(n, k, l) for f in IDXF]
            for j, m in enumerate(mons):
                v = F(t)
                for (r, s) in m:
                    v *= Hs(idx[s], r)
                out[j] += v
    return out


rows, rhs = [], []
for n in range(0, NFIT + 1):
    rows.append(rowvals(n)); rhs.append(LAD(n))
    print('  built n=%d' % n, flush=True)


def solve(rows, rhs):
    ncol = len(rows[0])
    M = [rows[i][:] + [rhs[i]] for i in range(len(rows))]
    piv = []
    r = 0
    for c in range(ncol):
        p = None
        for i in range(r, len(M)):
            if M[i][c] != 0:
                p = i; break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        iv = M[r][c]
        M[r] = [x / iv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(ncol + 1)]
        piv.append(c); r += 1
    # consistency
    for i in range(r, len(M)):
        if all(M[i][j] == 0 for j in range(ncol)) and M[i][ncol] != 0:
            return None, piv, r
    x = [F(0)] * ncol
    for i, c in enumerate(piv):
        x[c] = M[i][ncol]
    return x, piv, r


x, piv, rk = solve(rows, rhs)
print('\nrank = %d / %d columns, %d equations' % (rk, len(mons), len(rows)))
if x is None:
    print('INCONSISTENT'); sys.exit()
nz = [(monname(mons[j]), x[j]) for j in range(len(mons)) if x[j] != 0]
print('SOLUTION: %d nonzero coefficients' % len(nz))
for nm, c in nz:
    print('   %-30s %s' % (nm, c))

# independent verification on held-out n
print('\nheld-out verification:')
bad = []
for n in list(range(NFIT + 1, NFIT + 8)) + [34, 36, 40]:
    rv = rowvals(n)
    val = sum(x[j] * rv[j] for j in range(len(mons)))
    ok = (val == LAD(n))
    print('   n=%-3d  %s' % (n, 'OK' if ok else 'FAIL'), flush=True)
    if not ok:
        bad.append(n)
print('held-out: %s' % ('ALL PASS' if not bad else 'FAIL %s' % bad))
