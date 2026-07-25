"""Extract an explicit rational w5 from the (consistent) depth-1 weight-5 fit, and
verify it EXACTLY (Fraction arithmetic) against the ladder.

Method: build the design matrix mod two primes, rref both with the SAME column order
(so the pivot profile agrees), CRT the two particular solutions (free vars = 0),
rational-reconstruct, then evaluate the resulting w5 exactly.
"""
import sys, time, json
import numpy as np
from fractions import Fraction as F
from fit import *
from run_fit import build_basis

MF = (5, 5, 5)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
NEXACT = int(sys.argv[2]) if len(sys.argv) > 2 else 14

kl = ['A%d' % r for r in range(1, 6)] + ['B%d' % r for r in range(1, 6)]
cl = ['C%d' % r for r in range(1, 6)]
nl = ['N%d' % r for r in range(1, 6)] + ['M%d' % r for r in range(1, 6)]
B = build_basis(5, False, *MF, maxr=5, kletters=kl, cletters=cl, nletters=nl)
print('basis', len(B), flush=True)

def design(q):
    Y = lad_ext('P', N + 1, q)
    M = np.zeros((N, len(B)), dtype=np.int64); b = np.zeros(N, dtype=np.int64)
    for i, n in enumerate(range(1, N + 1)):
        M[i] = row(n, q, B, depth2=False, maxr=5); b[i] = Y[n]
    return M, b

sols = {}; pivs = {}
for q in (Q1, Q2):
    t = time.time(); M, b = design(q)
    r, piv, inc, A = rref(M, b, q)
    print('q=%d rank=%d inconsistent=%s (%.0fs)' % (q, r, inc, time.time() - t), flush=True)
    assert not inc
    x = np.zeros(len(B), dtype=np.int64)
    for i, c in enumerate(piv):
        x[c] = A[i, -1] % q
    sols[q] = x; pivs[q] = piv
assert pivs[Q1] == pivs[Q2], 'pivot profiles differ'
print('pivot profiles agree, rank=%d' % len(pivs[Q1]), flush=True)

# CRT + rational reconstruction
Mmod = Q1 * Q2
inv1 = pow(Q1 % Q2, -1, Q2)
def crt(a1, a2):
    return (a1 + Q1 * ((a2 - a1) * inv1 % Q2)) % Mmod

def ratrec(a, m):
    a %= m
    r0, r1 = m, a; s0, s1 = 0, 1
    bound = int((m // 2) ** 0.5)
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound:
        return None
    return F(r1, s1) if s1 > 0 else F(-r1, -s1)

coeffs = {}
bad = 0
for i in range(len(B)):
    v = crt(int(sols[Q1][i]), int(sols[Q2][i]))
    fr = ratrec(v, Mmod)
    if fr is None:
        bad += 1; continue
    if fr != 0:
        coeffs[i] = fr
print('reconstructed %d nonzero coefficients (%d failed)' % (len(coeffs), bad), flush=True)
json.dump({B.label(B.els[i]): [c.numerator, c.denominator] for i, c in coeffs.items()},
          open('w5_solution.json', 'w'), indent=1)

# ---------------- exact verification ----------------
from math import comb
_H = {}
def Hs(m, r):
    key = (m, r); v = _H.get(key)
    if v is None:
        v = F(0) if m <= 0 else Hs(m - 1, r) + F(1, m ** r)
        _H[key] = v
    return v

def letters_exact(n):
    Lk = {}; Lc = {}; Ln = {}
    for r in range(1, 6):
        Lk['A%d' % r] = [Hs(n + k, r) - Hs(k, r) for k in range(n + 1)]
        Lk['B%d' % r] = [Hs(n - k, r) - Hs(k, r) for k in range(n + 1)]
        Lc['C%d' % r] = [Hs(n + m, r) - Hs(m, r) for m in range(2 * n + 1)]
        Ln['N%d' % r] = Hs(n, r); Ln['M%d' % r] = Hs(2 * n, r)
    return Lk, Lc, Ln

def w5_exact(n, k, l, Lk, Lc, Ln):
    tot = F(0)
    for i, cf in coeffs.items():
        a, bidx, ci, ni = B.els[i]
        f = B.km[a][0]; g = B.km[bidx][0]; h = B.cm[ci][0]; s = B.nm[ni][0]
        def ev(mono, tab, idx):
            v = F(1)
            for nm in mono: v *= tab[nm][idx]
            return v
        val = F(1)
        for nm in h: val *= Lc[nm][k + l]
        for nm in s: val *= Ln[nm]
        p1 = ev(f, Lk, k) * ev(g, Lk, l)
        p2 = ev(f, Lk, l) * ev(g, Lk, k)
        tot += cf * val * (p1 if a == bidx else p1 + p2)
    return tot

lad = ladder('P')
print('exact check:', flush=True)
allok = True
for n in range(1, NEXACT + 1):
    Lk, Lc, Ln = letters_exact(n)
    tot = F(0)
    for k in range(n + 1):
        for l in range(n + 1):
            T = comb(n + k, n) * comb(n, k)**2 * comb(n + l, n) * comb(n, l)**2 * comb(n + k + l, n)
            tot += T * w5_exact(n, k, l, Lk, Lc, Ln)
    tgt = F(lad[n][0], lad[n][1])
    ok = (tot == tgt)
    allok &= ok
    print('  n=%2d  %s' % (n, 'OK' if ok else 'MISMATCH  diff=%s' % (tot - tgt)), flush=True)
print('EXACT VERIFICATION:', 'ALL OK' if allok else 'FAILED')
