"""R2: pin a CANONICAL representative of w5 in the 135-dimensional affine solution space.

Canonicalisation principle (mirrors the structure of w3hat exactly):
order the 448 basis monomials by a fixed PREFERENCE key, then take the rref particular
solution (free variables = 0).  Because rref pivots greedily left-to-right, the solution is
supported on the *most preferred* monomials; the resulting point of the affine family is
canonical once the order is fixed.

Preference key (ascending = preferred):
  1. total number of letter factors            (w3hat uses 1 or 2)
  2. number of B letters                       (w3hat: at most one)
  3. number of C letters                       (w3hat: at most one)
  4. number of constant (N) letters            (w3hat: at most one)
  5. -(weight of the heaviest letter)          (prefer A5 over A1*A4 over ...)
  6. label string                              (deterministic tie-break)

Usage: python3 canon_w5.py [N] [tag]
"""
import sys, time, json
import numpy as np
from fractions import Fraction as F
from fit import *
from run_fit import build_basis

N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
TAG = sys.argv[2] if len(sys.argv) > 2 else 'canon'

kl = ['A%d' % r for r in range(1, 6)] + ['B%d' % r for r in range(1, 6)]
cl = ['C%d' % r for r in range(1, 6)]
nl = ['N%d' % r for r in range(1, 6)]
B = build_basis(5, False, 5, 2, 2, maxr=5, kletters=kl, cletters=cl, nletters=nl)
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
print('columns reordered; first 12:', labels[:12], flush=True)


def design(q):
    Y = lad_ext('P', N + 1, q)
    M = np.zeros((N, len(B)), dtype=np.int64)
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
    r, piv, inc, A = rref(M, b, q)
    rM, _, _, _ = rref(M, np.zeros(N, dtype=np.int64), q)
    print('q=%d rank(M)=%d rank(aug)=%d inconsistent=%s' % (q, rM, r, inc), flush=True)
    assert not inc, 'INCONSISTENT -- N too small or basis wrong'
    x = np.zeros(len(B), dtype=np.int64)
    for i, c in enumerate(piv):
        x[c] = A[i, -1] % q
    sols[q] = x
    pivs[q] = list(piv)
assert pivs[Q1] == pivs[Q2], 'pivot profiles differ'
print('pivot profiles agree, rank=%d, nullity=%d' % (len(pivs[Q1]), len(B) - len(pivs[Q1])), flush=True)

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


coeffs = {}
bad = 0
for i in range(len(B)):
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
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        while d % p == 0:
            d //= p
            dens.add(p)
    if d != 1:
        dens.add(d)
print('primes occurring in denominators:', sorted(dens), flush=True)
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
print('written w5_%s.json' % TAG)
