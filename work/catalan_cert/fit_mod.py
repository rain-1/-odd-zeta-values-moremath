"""
Fit p_i(n)/p4(n) (i=0..3) as rational functions of n mod P = 2^127-1 from the
'praw <n0> [v0..v4]' lines of scan3 order-4 outputs, one parity at a time; then
rationally reconstruct the coefficients and emit exact sympy expressions.

Usage: python3 fit_mod.py file1 [file2 ...]
(mix of files; parity is inferred from n0 mod 2 and fitted separately)
"""
import sys, re, ast
import sympy as sp
from fractions import Fraction as F

P = 2**127 - 1
n = sp.Symbol('n')

def inv(a): return pow(a % P, P - 2, P)

def rat_reconstruct(a):
    a %= P
    r0, r1 = P, a
    s0, s1 = 0, 1
    bound = int(P**0.5) // 2
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q*r1
        s0, s1 = s1, s0 - q*s1
    if s1 == 0:
        return None
    return F(r1 if s1 > 0 else -r1, abs(s1))

pts = {0: {}, 1: {}}
for fn in sys.argv[1:]:
    for m in re.finditer(r'praw (\d+) \[([0-9, ]+)\]', open(fn).read()):
        n0 = int(m.group(1))
        vals = [int(x) for x in m.group(2).split(',')]
        pts[n0 % 2][n0] = vals

def fit(component_vals, dmax=30):
    """component_vals: {n0: ratio mod P}.  Find N,D poly deg <= d with
    N(n0) = ratio*D(n0) mod P for all points, minimal d, cross-validated."""
    items = sorted(component_vals.items())
    for d in range(1, dmax + 1):
        nun = d + 1 + d  # N coeffs + D coeffs (D monic deg d)
        if len(items) < 2*d + 4:
            break
        fitpts = items[:2*d + 2]
        testpts = items[2*d + 2:]
        # unknowns: a_0..a_d (N), b_0..b_{d-1} (D monic)
        rows = []
        for n0, v in fitpts:
            row = [pow(n0, i, P) for i in range(d + 1)]
            row += [(-v * pow(n0, i, P)) % P for i in range(d)]
            rhs = v * pow(n0, d, P) % P
            rows.append((row, rhs))
        # solve least-structured: gauss
        W = len(rows[0][0])
        M = [list(r) + [b] for r, b in rows]
        piv = {}
        pr = 0
        for c in range(W):
            q = next((i for i in range(pr, len(M)) if M[i][c]), None)
            if q is None:
                continue
            M[pr], M[q] = M[q], M[pr]
            iv = inv(M[pr][c])
            M[pr] = [x * iv % P for x in M[pr]]
            for i in range(len(M)):
                if i != pr and M[i][c]:
                    f = M[i][c]
                    M[i] = [(a - f*b) % P for a, b in zip(M[i], M[pr])]
            piv[c] = pr
            pr += 1
        if any(all(x == 0 for x in row[:-1]) and row[-1] for row in M):
            continue
        solv = [0]*W
        for c, i in piv.items():
            solv[c] = M[i][W]
        Nc = solv[:d + 1]; Dc = solv[d + 1:] + [1]
        okall = True
        for n0, v in testpts:
            Nv = sum(c * pow(n0, i, P) for i, c in enumerate(Nc)) % P
            Dv = sum(c * pow(n0, i, P) for i, c in enumerate(Dc)) % P
            if (Nv - v * Dv) % P != 0:
                okall = False
                break
        if okall and len(testpts) >= 2:
            Ne = sum((rat_reconstruct(c) or 0) * n**i for i, c in enumerate(Nc))
            De = sum((rat_reconstruct(c) or 0) * n**i for i, c in enumerate(Dc))
            return sp.cancel(sp.nsimplify(Ne) / sp.nsimplify(De)), d
    return None, None

for par in (0, 1):
    data = pts[par]
    print('parity %s: %d points (n=%s..%s)' % ('even' if par == 0 else 'odd',
          len(data), min(data) if data else '-', max(data) if data else '-'))
    if len(data) < 8:
        continue
    for comp in range(4):
        vals = {n0: v[comp] for n0, v in data.items()}
        ratio, d = fit(vals)
        if ratio is None:
            print('  p%d/p4: FIT FAILED (need more points?)' % comp)
        else:
            print('  p%d/p4 (deg %d) = %s' % (comp, d, sp.factor(ratio)))
