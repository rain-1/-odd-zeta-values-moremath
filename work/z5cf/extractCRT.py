"""Exact-Q extraction by CRT + rational reconstruction, then EXACT verification.

Solves  sum_j x_j * (sum_{k,l} T * mon_j)  =  Y_n  over several 25-bit primes with a
FIXED pivot choice, CRTs the coefficient vectors and rationally reconstructs.
Final answer is re-verified with exact Fraction arithmetic from core.T / core.Hs.
"""
import sys, os, time, json, numpy as np
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from design2 import build, monomials, sym_orbits, monname, rref
from bare import lad_mod, SYMNAME
from core import T, Hs, Ph, P, Q

W = int(sys.argv[1]); KEY = sys.argv[2]; DMAX = int(sys.argv[3])
SY = tuple(int(x) for x in sys.argv[4].split(','))
N = int(sys.argv[5])
OUT = sys.argv[6] if len(sys.argv) > 6 else None

PRIMES = [33554393, 33554467, 33554371, 33554383, 33554429,
          33554467 - 100, 16777213, 16777199]
PRIMES = [p for p in PRIMES if all(p % d for d in range(2, 6000)) or p > 33554000]
PRIMES = [33554393, 33554467, 33554371, 33554383, 33554429, 16777259, 16777213, 16777199]

mons = sym_orbits(monomials(W, DMAX, SY))
NCOL = len(mons)
print('%d symmetric monomials' % NCOL, flush=True)

sols = []
usedp = []
pivref = None
for q in PRIMES:
    _, M = build(W, N, q, mons=mons)
    b = np.array([lad_mod(KEY, n, q) for n in range(N + 1)], dtype=np.int64)
    R, rk, piv = rref(np.hstack([M % q, b[:, None]]), q)
    if NCOL in piv:
        print('  q=%d INCONSISTENT' % q); continue
    if pivref is None:
        pivref = piv
    elif piv != pivref:
        print('  q=%d pivot mismatch -> skip' % q); continue
    x = [0] * NCOL
    for i, c in enumerate(piv):
        x[c] = int(R[i, NCOL])
    sols.append(x); usedp.append(q)
    print('  q=%d ok (rank %d, %d free cols)' % (q, rk, NCOL - len(piv)), flush=True)
    if len(sols) >= 6:
        break


def crt(rs, ms):
    x, m = rs[0] % ms[0], ms[0]
    for r, mi in zip(rs[1:], ms[1:]):
        g, p_, q_ = 0, 0, 0
        # solve x + m*t = r mod mi
        inv = pow(m % mi, mi - 2, mi)
        t = (r - x) % mi * inv % mi
        x = x + m * t
        m *= mi
    return x % m, m


def ratrec(a, m):
    """rational reconstruction of a mod m"""
    u = (m, 0); v = (a, 1)
    lim = int(m ** 0.5) // 2
    while v[0] > lim:
        qq = u[0] // v[0]
        u, v = v, (u[0] - qq * v[0], u[1] - qq * v[1])
    n_, d_ = v
    if d_ == 0:
        return None
    if d_ < 0:
        n_, d_ = -n_, -d_
    from math import gcd
    if gcd(abs(n_), d_) != 1:
        return None
    return F(n_, d_)


coeffs = []
ok = True
for j in range(NCOL):
    a, m = crt([s[j] for s in sols], usedp)
    r = ratrec(a, m)
    if r is None:
        ok = False; r = None
    coeffs.append(r)
print('rational reconstruction: %s' % ('OK' if ok else 'FAILED for some columns'))
nz = [(mons[j], coeffs[j]) for j in range(NCOL) if coeffs[j] not in (None, 0)]
print('\n%d nonzero coefficients:' % len(nz))
for m, c in nz:
    print('   %-34s %s' % (monname(m), c))

# ---------------- exact verification ----------------
IDXF = [lambda n, k, l: n, lambda n, k, l: k, lambda n, k, l: l,
        lambda n, k, l: n + k, lambda n, k, l: n + l, lambda n, k, l: n - k,
        lambda n, k, l: n - l, lambda n, k, l: k + l, lambda n, k, l: n + k + l]
LAD = {'Ph': Ph, 'P': P, 'Q': Q}[KEY]
print('\nEXACT verification (Fraction arithmetic):')
bad = []
for n in list(range(0, 21)) + [24, 28, 30, 34]:
    tot = F(0)
    for k in range(n + 1):
        for l in range(n + 1):
            t = T(n, k, l)
            idx = [f(n, k, l) for f in IDXF]
            s = F(0)
            for m, c in nz:
                v = c
                for (r, si) in m:
                    v *= Hs(idx[si], r)
                s += v
            tot += t * s
    good = (tot == LAD(n))
    print('   n=%-3d %s' % (n, 'OK' if good else 'FAIL'), flush=True)
    if not good:
        bad.append(n)
print('EXACT: %s' % ('ALL PASS' if not bad else 'FAIL at %s' % bad))
if OUT:
    json.dump({'W': W, 'key': KEY, 'dmax': DMAX, 'syms': list(SY),
               'terms': [[monname(m), str(c)] for m, c in nz],
               'mons': [[list(x) for x in m] for m, c in nz],
               'exact_verified': [n for n in list(range(0, 21)) + [24, 28, 30, 34] if n not in bad]},
              open(OUT, 'w'), indent=1)
    print('wrote %s' % OUT)
