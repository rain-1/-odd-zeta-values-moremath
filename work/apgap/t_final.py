"""TEST 4: the finished statement, re-verified.

THEOREM (to be checked): for p>=5, n = ap+r with a,r < p,

    ( a_n , p^3 b_n )  ==  ( a_a , b_a ) * u(a,r)   (mod p^3),
    u(a,r) = a_r + 2p a U_r + p^2 a^2 X_p(r),
    X_p(r) = Sa2(r) + Xi_p(r) = [eps^2] sum_{s=0}^{p-1} A_Gamma(r+eps,s).

Checks:
  C1  X_p(r) == [eps^2] Adig(p,r)  (mod p)                 -- agrees with sec 4.3
  C2  v_p( a_{ap+r} - a_a u ) >= 3 and floor exactly 3
  C3  v_p( p^3 b_{ap+r} - b_a u ) >= 3 and floor exactly 3
  C4  second-order defect D2 = (X_n - X_a(a_r+2paU_r))/p^2 has rank exactly 1,
      both rows, same r-space, and a-side factor exactly a^2.
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/apdef')
from fractions import Fraction as F
from core import av, bv, vp, modp, rank_fp, rref_fp
from dseries import Adig
from gap_core import sigmas, Xi, Ur

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def Xp(p, r):
    return sigmas(r)[0] + Xi(p, r)


def uscal(p, a, r):
    return av(r) + 2 * p * a * Ur(r) + p * p * a * a * Xp(p, r)


def run(p, check_adig=True):
    out = {}
    if check_adig:
        out['adig'] = all(modp(Xp(p, r) - Adig(p, r, 2)[2], p) == 0 for r in range(p))
    fa = fb = 10 ** 9
    for a in range(1, p):
        for r in range(p):
            u = uscal(p, a, r)
            fa = min(fa, vp(av(a * p + r) - av(a) * u, p))
            fb = min(fb, vp(F(p) ** 3 * bv(a * p + r) - bv(a) * u, p))
    out['floor_a'] = fa
    out['floor_b'] = fb
    # second-order defect matrices, rows a=1..p-1, cols r=0..p-1
    Ma, Mb = [], []
    for a in range(1, p):
        ra, rb = [], []
        for r in range(p):
            u1 = av(r) + 2 * p * a * Ur(r)
            ra.append(modp(F(av(a * p + r) - av(a) * u1, p ** 2), p))
            rb.append(modp(F(p) ** 3 * bv(a * p + r) / p ** 2 - F(bv(a) * u1, p ** 2), p))
        Ma.append(ra); Mb.append(rb)
    out['rank_a'] = rank_fp(Ma, p)
    out['rank_b'] = rank_fp(Mb, p)
    out['same_rowspace'] = rref_fp(Ma, p)[0] == rref_fp(Mb, p)[0]
    # predicted:  row_a[a][r] = a^2 a_a X_p(r),  row_b = a^2 b_a X_p(r)
    pa = [[modp(a * a * av(a) * Xp(p, r), p) for r in range(p)] for a in range(1, p)]
    pb = [[modp(a * a * bv(a) * Xp(p, r), p) for r in range(p)] for a in range(1, p)]
    out['pred_a'] = (Ma == pa)
    out['pred_b'] = (Mb == pb)
    return out


if __name__ == '__main__':
    print('%-4s %-6s %-8s %-8s %-7s %-7s %-6s %-7s %-7s'
          % ('p', 'Adig', 'floor_a', 'floor_b', 'rank_a', 'rank_b', 'same', 'pred_a', 'pred_b'))
    allok = True
    for p in PRIMES:
        o = run(p)
        allok &= o['adig'] and o['floor_a'] == 3 and o['floor_b'] == 3 \
            and o['rank_a'] == 1 and o['rank_b'] == 1 and o['same_rowspace'] \
            and o['pred_a'] and o['pred_b']
        print('%-4d %-6s %-8d %-8d %-7d %-7d %-6s %-7s %-7s'
              % (p, o['adig'], o['floor_a'], o['floor_b'], o['rank_a'], o['rank_b'],
                 o['same_rowspace'], o['pred_a'], o['pred_b']))
        sys.stdout.flush()
    print('\nALL CHECKS PASS :', allok)
