"""(GAP-5) route A, step 3: the depth-conditioned family has nullity 124; hunt for points of
it whose coefficient denominators avoid a given prime.

The DEPTH conditions are p-independent and structural.  What is representative-dependent is
only the set of primes dividing the coefficient DENOMINATORS: a coefficient with p in its
denominator inflates d5 at that one prime.  So we need, for each p >= 5, SOME point of the
depth-conditioned family that is p-integral.  Different column orders (= different rref pivot
sets) give different points; this script sweeps orders and reports the denominator primes.

Usage: python3 solve_depth2.py [N]
"""
import sys, time, json, random
import numpy as np
from fractions import Fraction as F
from collections import defaultdict

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from fit import Q1, Q2, row, rref, lad_ext
from depthcond import basis, patterns, elem_expansion

N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
B = basis()
NC = len(B.els)
print('basis', NC, flush=True)


def prefkey(e):
    i, j, ci, ni = e
    mons = list(B.km[i][0]) + list(B.km[j][0]) + list(B.cm[ci][0]) + list(B.nm[ni][0])
    nfac = len(mons)
    nB = sum(1 for m in mons if m[0] == 'B')
    nC = sum(1 for m in mons if m[0] == 'C')
    nN = sum(1 for m in mons if m[0] == 'N')
    top = max([int(m[1]) for m in mons], default=0)
    return (nfac, nB, nC, nN, -top, B.label(e))


ORDERS = {}
els0 = list(B.els)
ORDERS['pref'] = sorted(els0, key=prefkey)
ORDERS['prefrev'] = sorted(els0, key=prefkey)[::-1]
ORDERS['nB_desc'] = sorted(els0, key=lambda e: (prefkey(e)[0], -prefkey(e)[1]) + prefkey(e)[2:])
ORDERS['top_asc'] = sorted(els0, key=lambda e: (prefkey(e)[0], prefkey(e)[4], prefkey(e)[1],
                                                prefkey(e)[2], prefkey(e)[3], prefkey(e)[5]))
ORDERS['nfac_desc'] = sorted(els0, key=lambda e: (-prefkey(e)[0],) + prefkey(e)[1:])
for s in range(8):
    rnd = random.Random(1000 + s)
    o = list(els0)
    rnd.shuffle(o)
    ORDERS['rand%d' % s] = o

# ------------------------------------------------------- conditions (basis-order indexed)
B.els = els0
caps = patterns()
rows = defaultdict(lambda: [F(0)] * NC)
for ci, e in enumerate(B.els):
    for pat, cap in caps.items():
        if pat == (0, 0, 0, 1):
            continue
        for (u, sym), v in elem_expansion(B, e, pat).items():
            if u > cap:
                rows[(pat, u, sym)][ci] += v
C = []
for k, vec in rows.items():
    if not any(vec):
        continue
    den = 1
    for v in vec:
        den = den * v.denominator // np.gcd(den, v.denominator)
    C.append([int(v * den) for v in vec])
C = np.array(C, dtype=object)
print('condition rows %d x %d' % C.shape, flush=True)

# ------------------------------------------------------- design matrices (basis order)
DES = {}
for q in (Q1, Q2):
    Y = lad_ext('P', N + 1, q)
    M = np.zeros((N, NC), dtype=np.int64)
    b = np.zeros(N, dtype=np.int64)
    t0 = time.time()
    for i, n in enumerate(range(1, N + 1)):
        M[i] = row(n, q, B, depth2=False, maxr=5)
        b[i] = Y[n]
    Cq = np.array([[int(v) % q for v in r] for r in C], dtype=np.int64)
    A = np.concatenate([M, Cq], axis=0)
    rhs = np.concatenate([b, np.zeros(len(Cq), dtype=np.int64)])
    DES[q] = (A, rhs)
    print('design q=%d built %.0fs' % (q, time.time() - t0), flush=True)

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


idx = {e: i for i, e in enumerate(els0)}
results = {}
for name, order in ORDERS.items():
    perm = np.array([idx[e] for e in order])
    sols, pivs, ok = {}, {}, True
    for q in (Q1, Q2):
        A, rhs = DES[q]
        r, piv, inc, R = rref(A[:, perm], rhs, q)
        if inc:
            print('%-10s INCONSISTENT (q=%d)' % (name, q), flush=True)
            ok = False
            break
        x = np.zeros(NC, dtype=np.int64)
        for i, c in enumerate(piv):
            x[c] = R[i, -1] % q
        sols[q] = x
        pivs[q] = list(piv)
    if not ok or pivs[Q1] != pivs[Q2]:
        print('%-10s pivot mismatch' % name, flush=True)
        continue
    coeffs, bad = {}, 0
    for i in range(NC):
        fr = ratrec(crt(int(sols[Q1][i]), int(sols[Q2][i])), Mmod)
        if fr is None:
            bad += 1
            continue
        if fr != 0:
            coeffs[B.label(order[i])] = fr
    dens = set()
    for c in coeffs.values():
        d = c.denominator
        for p in range(2, 200):
            while d % p == 0:
                d //= p
                dens.add(p)
        if d != 1:
            dens.add(d)
    print('%-10s  terms=%3d  ratrec-fail=%d  denominator primes=%s'
          % (name, len(coeffs), bad, sorted(dens)), flush=True)
    if bad == 0:
        results[name] = (coeffs, sorted(dens))
        json.dump({k: [v.numerator, v.denominator] for k, v in sorted(coeffs.items())},
                  open('w5_dm_%s.json' % name, 'w'), indent=1)

print('\nSUMMARY (denominator primes >= 5 are the ONLY bad primes for that representative):',
      flush=True)
for name, (co, dens) in results.items():
    print('  %-10s %3d terms  bad primes %s' % (name, len(co), [p for p in dens if p >= 5]),
          flush=True)
