"""P1g E3a: extract an exact-Q representative of the R-extended joint system.

Usage: python3 e3_solve.py MODE KSPEC CSPEC NSPEC N q1,q2[,q3...] OUT.json [ORDER]
ORDER: pivot preference; 'pref' (default) = fewest factors, fewest B, fewest C,
       fewest N, fewest R, heaviest letter first, label.  'plain' = label order.
Solves [fit ; depth-conditions] mod each q with free variables 0, checks the pivot
sets agree, CRTs, rational-reconstructs, and writes the exact representative.
"""
import sys, time, json
from math import isqrt, gcd
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from rfit import (AB, KL, CL, DL, NL, YL, VL, ZL, build_basis, row, rref, lad_ext)
import rdepth

SH = {'AB': AB, 'ABR': KL, 'ABY': AB + YL, 'ABRY': KL + YL,
      'C': CL, 'CD': CL + DL, 'CV': CL + VL, 'CDV': CL + DL + VL,
      'N': NL, 'NZ': NL + ZL}

MODE = sys.argv[1]
kl = SH.get(sys.argv[2], sys.argv[2].split(','))
cl = SH.get(sys.argv[3], sys.argv[3].split(','))
nl = SH.get(sys.argv[4], sys.argv[4].split(','))
N = int(sys.argv[5])
QS = [int(x) for x in sys.argv[6].split(',')]
OUT = sys.argv[7]
ORDER = sys.argv[8] if len(sys.argv) > 8 else 'pref'
useD = any(x[0] == 'D' for x in cl)
nested = any(x[0] in 'YVZ' for x in kl + cl + nl)

B = build_basis(kletters=kl, cletters=cl, nletters=nl, useD=useD, nested=nested)


def key(e):
    i, j, ci, ni = e
    mons = list(B.km[i][0]) + list(B.km[j][0]) + list(B.cm[ci][0]) + list(B.nm[ni][0])
    return (len(mons),
            sum(1 for m in mons if m[0] == 'B'), sum(1 for m in mons if m[0] == 'C'),
            sum(1 for m in mons if m[0] == 'N'), sum(1 for m in mons if m[0] == 'R'),
            sum(1 for m in mons if m[0] in 'DYVZ'),
            -max([int(m[1]) for m in mons], default=0), B.label(e))


if ORDER == 'pref':
    B.els = sorted(B.els, key=key)
NC = len(B.els)
print('basis %d cols, N=%d, primes %s, order=%s' % (NC, N, QS, ORDER), flush=True)

caps = rdepth.caps_for(MODE, refine_eps=useD)
C = rdepth.condition_rows(B, caps)
print('condition rows %d' % len(C), flush=True)

sols, pivs = [], None
for q in QS:
    t0 = time.time()
    Y = lad_ext('P', N + 1, q)
    M = np.zeros((N, NC), dtype=np.int64)
    b = np.zeros(N, dtype=np.int64)
    for i, n in enumerate(range(1, N + 1)):
        M[i] = row(n, q, B, useD=useD, nested=nested)
        b[i] = Y[n]
    Cq = np.array([[int(v) % q for v in r] for r in C], dtype=np.int64)
    A = np.concatenate([M, Cq], axis=0)
    rhs = np.concatenate([b, np.zeros(len(Cq), np.int64)])
    r, piv, inc, R = rref(A, rhs, q)
    print('  q=%d rank=%d inconsistent=%s (%.1f s)' % (q, r, inc, time.time() - t0), flush=True)
    if inc:
        sys.exit('INCONSISTENT at q=%d -- nothing to extract' % q)
    x = np.zeros(NC, dtype=np.int64)
    for i, c in enumerate(piv):
        x[c] = R[i, -1] % q
    if pivs is None:
        pivs = piv
    elif pivs != piv:
        sys.exit('pivot sets differ between primes -- unlucky prime')
    sols.append(x)

# ---- CRT + rational reconstruction
Mtot = 1
for q in QS:
    Mtot *= q
bound = isqrt(Mtot // 2)


def crt(vals):
    x, m = 0, 1
    for v, q in zip(vals, QS):
        # solve y = x mod m, y = v mod q
        t = (v - x) % q * pow(m % q, q - 2, q) % q
        x += m * t
        m *= q
    return x % m


def ratrec(x, m):
    a0, a1 = m, x % m
    b0, b1 = 0, 1
    while a1 > bound:
        qq = a0 // a1
        a0, a1 = a1, a0 - qq * a1
        b0, b1 = b1, b0 - qq * b1
    if b1 == 0:
        return None
    if b1 < 0:
        a1, b1 = -a1, -b1
    if b1 > bound or gcd(abs(a1), b1) != 1:
        return None
    return F(a1, b1)


out, nbad, nz = {}, 0, 0
for c in range(NC):
    v = crt([int(s[c]) for s in sols])
    fr = ratrec(v, Mtot)
    if fr is None:
        nbad += 1
        continue
    if fr != 0:
        nz += 1
        out[B.label(B.els[c])] = [fr.numerator, fr.denominator]
print('reconstruction failures: %d ; nonzero terms: %d' % (nbad, nz), flush=True)
if nbad:
    sys.exit('rational reconstruction failed -- add primes')
json.dump(out, open(OUT, 'w'))
dens = set()
for _, d in out.values():
    dd = d
    for p in (2, 3, 5, 7, 11, 13):
        while dd % p == 0:
            dd //= p
    dens.add(dd)
print('wrote %s : %d terms' % (OUT, len(out)), flush=True)
print('denominator residual factors (after removing 2,3,5,7,11,13): %s'
      % sorted(dens)[:10], flush=True)
