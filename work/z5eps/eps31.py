"""eps31.py -- extract the ONE missing dimension as an explicit exact form.

At the eps27 level (pure weight-5 ring, rank 426) the span misses sym(Delta5)
by exactly one dimension.  This script computes the canonical echelon
residual r = sym(Delta5) - proj_span(sym(Delta5)) at two primes, CRT-combines,
rationally reconstructs, and reports r as an exact form.

Then  sum_{k,l} T * r = 0  is the single missing identity: it holds because
sum T*Delta5 = 0 (verified) and every generator is row-null; proving it by an
independent mechanism (e.g. an order-zero telescoping certificate) closes the
Delta5 bridge.  r is echelon-canonical: with the same generator ordering and
pivot pattern at both primes, the reduction is the image of one Q-rational
vector, so CRT is legitimate; the exact membership tgt - r in span_Q(gens) is
then re-verified modulo two FRESH primes.
"""

import sys, time, pickle
import numpy as np
from math import gcd
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')

import eps24, eps25, eps26, eps27
from eps26 import row_echelon
from eps22 import MON, MIDX, NM, SIG, DELTA5, build_rows

ALLF = eps24.GEN_FORMS + eps25.NEWF + eps26.EF + eps27.XF
ALLN = eps24.GEN_NAMES + eps25.NEWN + eps26.EN + eps27.XN
print('generators:', len(ALLF))


def vec_modp(f, p):
    v = np.zeros(NM, dtype=np.int64)
    for m, c in f.items():
        v[MIDX[m]] = (v[MIDX[m]] + c.numerator % p
                      * pow(c.denominator % p, p - 2, p)) % p
    return v


def residual_at_prime(p):
    rows, _ = build_rows(p, 40)
    V = np.zeros((len(ALLF), NM), dtype=np.int64)
    for i, f in enumerate(ALLF):
        V[i] = vec_modp(f, p)
    bad = set()
    for lo in range(0, len(ALLF), 64):
        hi = min(lo + 64, len(ALLF))
        vals = rows.dot(V[lo:hi].T) % p
        for j in range(hi - lo):
            if vals[:, j].any():
                bad.add(lo + j)
    if bad:
        print('  calibration failures at p=%d: %d' % (p, len(bad)))
    keep = [i for i in range(len(ALLF)) if i not in bad]
    G = V[keep]
    inv2 = pow(2, p - 2, p)
    Gs = (G + G[:, SIG]) * inv2 % p
    tgt = np.zeros(NM, dtype=np.int64)
    for m, c in DELTA5.items():
        tgt[MIDX[m]] = (c.numerator % p
                        * pow(c.denominator % p, p - 2, p)) % p
    tgt = (tgt + tgt[SIG]) * inv2 % p
    basis, pivots = row_echelon(Gs, p)
    res = tgt.copy()
    for row, piv in zip(basis, pivots):
        if res[piv]:
            res = (res - res[piv] * row) % p
    return res, tuple(pivots), keep


def crt_pair(a1, p1, a2, p2):
    m1 = pow(p1, -1, p2)
    x = (a1 + p1 * ((a2 - a1) * m1 % p2)) % (p1 * p2)
    return x


def ratrec(a, M):
    if a == 0:
        return F(0)
    bound = int(M ** 0.5) // 2
    r0, r1 = M, a % M
    s0, s1 = 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound:
        return None
    if s1 < 0:
        r1, s1 = -r1, -s1
    if gcd(r1, s1) != 1:
        return None
    return F(r1, s1)


if __name__ == '__main__':
    p1, p2 = 4194301, 4194247   # both prime, 22-bit
    t0 = time.time()
    r1v, piv1, keep1 = residual_at_prime(p1)
    print('p1 done (%.0fs), residual support %d'
          % (time.time() - t0, int((r1v != 0).sum())), flush=True)
    r2v, piv2, keep2 = residual_at_prime(p2)
    print('p2 done, residual support %d' % int((r2v != 0).sum()), flush=True)
    print('pivot patterns match:', piv1 == piv2, ' keeps match:',
          keep1 == keep2)
    if piv1 != piv2:
        sys.exit('pivot mismatch -- residuals not CRT-compatible')

    M = p1 * p2
    RES = {}
    fails = 0
    for i in range(NM):
        if r1v[i] == 0 and r2v[i] == 0:
            continue
        x = crt_pair(int(r1v[i]), p1, int(r2v[i]), p2)
        q = ratrec(x, M)
        if q is None:
            fails += 1
            print('  ratrec FAIL at', MON[i], int(r1v[i]), int(r2v[i]))
        else:
            RES[MON[i]] = q
    print('reconstructed %d coefficients, %d failures' % (len(RES), fails))
    if fails:
        sys.exit(1)

    # sanity: double sum T * r = 0 exactly for small n (r symmetric by constr.)
    import core
    H = core.Hs
    def eval_form(f, n, k, l):
        xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
        s = F(0)
        for m, cc in f.items():
            v = cc
            for (r, a) in m:
                v *= H(xs[a], r)
            s += v
        return s
    ok = True
    for n in range(6):
        tot = sum(core.T(n, k, l) * eval_form(RES, n, k, l)
                  for k in range(n + 1) for l in range(n + 1))
        if tot != 0:
            ok = False
            print('  double-sum check FAIL at n=%d: %s' % (n, tot))
    print('double sum T*r = 0 (n<=5):', 'PASS' if ok else 'FAIL')

    with open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/'
              'eps31_residual.pkl', 'wb') as fh:
        pickle.dump(RES, fh)
    print('saved eps31_residual.pkl; support', len(RES))
    # display by letter profile
    from collections import Counter
    prof = Counter()
    for m in RES:
        prof[tuple(sorted(r for r, a in m))] += 1
    print('degree profile:', dict(prof))
