"""(GAP-5) route A, step 2: solve for a DEPTH-MINIMAL w5.

Adjoin to the 448-column fitting system  P_n = sum_{k,l} T(n,k,l) w5(n,k,l)
the p-independent linear conditions of depthcond.py:

    for each reachable pole pattern (alpha,gamma,kappa,theta) with depth cap J,
    and each j > J,  the u^j-component of w5 (u = p^-1) vanishes identically
    in the Z_p symbols.

Then pin the point of the remaining affine family by the same preference-ordered
rref used for the sparsest canonical representative (canon_w5.py).

Usage: python3 solve_depth.py [N] [tag]
"""
import sys, time, json
import numpy as np
from fractions import Fraction as F
from collections import defaultdict

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from fit import Q1, Q2, row, rref, lad_ext
from depthcond import basis, patterns, elem_expansion

N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
TAG = sys.argv[2] if len(sys.argv) > 2 else 'canon2'

B = basis()
print('basis', len(B), flush=True)


def key(e):
    i, j, ci, ni = e
    mons = list(B.km[i][0]) + list(B.km[j][0]) + list(B.cm[ci][0]) + list(B.nm[ni][0])
    nfac = len(mons)
    nB = sum(1 for m in mons if m[0] == 'B')
    nC = sum(1 for m in mons if m[0] == 'C')
    nN = sum(1 for m in mons if m[0] == 'N')
    top = max([int(m[1]) for m in mons], default=0)
    return (nfac, nB, nC, nN, -top, B.label(e))


B.els = sorted(B.els, key=key)
labels = [B.label(e) for e in B.els]
NC = len(B.els)

# ------------------------------------------------------------------ conditions
caps = patterns()
print('patterns:', {k: v for k, v in sorted(caps.items())}, flush=True)
rows = defaultdict(lambda: [F(0)] * NC)      # (pat,j,symkey) -> vector
t0 = time.time()
for ci, e in enumerate(B.els):
    for pat, cap in caps.items():
        if pat == (0, 0, 0, 1):
            continue                          # no poles at all
        exp = elem_expansion(B, e, pat)
        for (u, sym), v in exp.items():
            if u > cap:
                rows[(pat, u, sym)][ci] += v
print('condition rows built in %.0fs: %d raw' % (time.time() - t0, len(rows)), flush=True)

C = []
for k, vec in rows.items():
    if not any(vec):
        continue
    den = 1
    for v in vec:
        den = den * v.denominator // np.gcd(den, v.denominator)
    iv = [int(v * den) for v in vec]
    g = 0
    for v in iv:
        g = np.gcd(g, abs(v))
    if g:
        iv = [v // int(g) for v in iv]
    C.append(iv)
C = np.array(C, dtype=object)
print('nonzero condition rows: %d x %d' % C.shape, flush=True)


def design(q):
    Y = lad_ext('P', N + 1, q)
    M = np.zeros((N, NC), dtype=np.int64)
    b = np.zeros(N, dtype=np.int64)
    t0 = time.time()
    for i, n in enumerate(range(1, N + 1)):
        M[i] = row(n, q, B, depth2=False, maxr=5)
        b[i] = Y[n]
        if n % 150 == 0:
            print('   n=%d  %.0fs' % (n, time.time() - t0), flush=True)
    return M, b


sols, pivs = {}, {}
for q in (Q1, Q2):
    M, b = design(q)
    Cq = np.array([[int(v) % q for v in r] for r in C], dtype=np.int64)
    # rank of the FIT system alone (sanity: 313)
    rM, _, _, _ = rref(M, np.zeros(N, dtype=np.int64), q)
    rC, _, _, _ = rref(Cq, np.zeros(len(Cq), dtype=np.int64), q)
    A = np.concatenate([M, Cq], axis=0)
    rhs = np.concatenate([b, np.zeros(len(Cq), dtype=np.int64)])
    r, piv, inc, R = rref(A, rhs, q)
    rA, _, _, _ = rref(A, np.zeros(len(rhs), dtype=np.int64), q)
    print('q=%d  rank(fit)=%d  rank(cond)=%d  rank(joint)=%d  rank(aug)=%d  INCONSISTENT=%s'
          % (q, rM, rC, rA, r, inc), flush=True)
    if inc:
        print('  >>> DEPTH CONDITIONS ARE INFEASIBLE inside the solution family <<<', flush=True)
        sys.exit(2)
    x = np.zeros(NC, dtype=np.int64)
    for i, c in enumerate(piv):
        x[c] = R[i, -1] % q
    sols[q] = x
    pivs[q] = list(piv)
    print('   nullity after conditions = %d' % (NC - rA), flush=True)

assert pivs[Q1] == pivs[Q2], 'pivot profiles differ'
Mmod = Q1 * Q2
inv1 = pow(Q1 % Q2, -1, Q2)


def crt(a1, a2):
    return (a1 + Q1 * ((a2 - a1) * inv1 % Q2)) % Mmod


def ratrec(a, m):
    a %= m
    r0, r1 = m, a
    s0, s1 = 0, 1
    bound = int((m // 2) ** 0.5)
    while r1 > bound:
        qq = r0 // r1
        r0, r1 = r1, r0 - qq * r1
        s0, s1 = s1, s0 - qq * s1
    if s1 == 0 or abs(s1) > bound:
        return None
    return F(r1, s1) if s1 > 0 else F(-r1, -s1)


coeffs, bad = {}, 0
for i in range(NC):
    v = crt(int(sols[Q1][i]), int(sols[Q2][i]))
    fr = ratrec(v, Mmod)
    if fr is None:
        bad += 1
        continue
    if fr != 0:
        coeffs[labels[i]] = fr
print('reconstructed %d nonzero coefficients (%d failed)' % (len(coeffs), bad), flush=True)

dens = set()
for c in coeffs.values():
    d = c.denominator
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        while d % p == 0:
            d //= p
            dens.add(p)
    if d != 1:
        dens.add(d)
print('primes in denominators:', sorted(dens), flush=True)
from collections import Counter
hist = Counter()
for lab in coeffs:
    fg, rest = lab.split(']x')
    f, g = fg[1:].split('|')
    h, s = rest.split('x')
    sp = lambda x: [] if x == '1' else x.split('*')
    hist[len(sp(f)) + len(sp(g)) + len(sp(h)) + len(sp(s))] += 1
print('factor-count histogram:', dict(sorted(hist.items())), flush=True)

json.dump({k: [v.numerator, v.denominator] for k, v in sorted(coeffs.items())},
          open('w5_%s.json' % TAG, 'w'), indent=1)
print('written w5_%s.json' % TAG, flush=True)
