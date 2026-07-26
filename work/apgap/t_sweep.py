"""TEST 5: 0-failure sweeps of every lemma, p up to 31, ALL cells.

  S1  the three cell formulas for A(ap+r,cp+s) mod p^3,  all (a,c,r,s)
  S2  the assembled second-order defect, a-row AND b-row, all (a,r)
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/apdef')
from fractions import Fraction as F
from core import A, Hs, av, bv, vp, modp
from gap_core import sigmas, Xi, moments, Ur
from t_cellwise import region1, region2a, region2b

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31]


def sweep_cells(p):
    bad = 0; tot = 0
    for a in range(p):
        for r in range(p):
            n = a * p + r
            for c in range(a + 1):
                for s in range(p):
                    k = c * p + s
                    if k > n:
                        continue
                    if s <= r and r + s < p:
                        pred = region1(p, a, c, r, s)
                    elif s <= r:
                        pred = region2a(p, a, c, r, s)
                    elif 2 * r + (s - r) < p:
                        pred = region2b(p, a, c, r, s - r)
                    else:
                        pred = 0
                    tot += 1
                    if vp(F(A(n, k)) - pred, p) < 3:
                        bad += 1
    return bad, tot


def bmoments(p, a):
    """b-row moments: sum_c c^j A(a,c) (2H3_a - H3_c)"""
    w = [2 * Hs(a, 3) - Hs(c, 3) for c in range(a + 1)]
    return (sum(A(a, c) * w[c] for c in range(a + 1)),
            sum(c * A(a, c) * w[c] for c in range(a + 1)),
            sum(c * c * A(a, c) * w[c] for c in range(a + 1)))


def sweep_D2(p):
    bad = 0; tot = 0
    for a in range(p):
        Sa, Sb = moments(a), bmoments(p, a)
        for r in range(p):
            Sa2, Sac, Scc = sigmas(r)
            X = Xi(p, r)
            u1 = av(r) + 2 * p * a * Ur(r)
            meas_a = modp(F(av(a * p + r) - av(a) * u1, p ** 2), p)
            meas_b = modp(F(p) ** 3 * bv(a * p + r) / p ** 2 - F(bv(a) * u1, p ** 2), p)
            for M, meas in ((Sa, meas_a), (Sb, meas_b)):
                m0, m1, m2 = M
                pred = modp(a * a * m0 * Sa2 + a * m1 * Sac + m2 * Scc
                            + (a * a * m0 - 2 * a * m1 + m2) * X, p)
                tot += 1
                if pred != meas:
                    bad += 1
    return bad, tot


if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'both'
    if what in ('cells', 'both'):
        print('S1  cell formulas mod p^3')
        for p in PRIMES:
            b, t = sweep_cells(p)
            print('    p=%-3d cells %-8d failures %d' % (p, t, b)); sys.stdout.flush()
    if what in ('d2', 'both'):
        print('S2  assembled second-order defect (a-row and b-row)')
        for p in PRIMES:
            b, t = sweep_D2(p)
            print('    p=%-3d cells %-8d failures %d' % (p, t, b)); sys.stdout.flush()
