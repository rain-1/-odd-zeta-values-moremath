"""T1(iii): the SECOND-order defect, mod p^2, and its rank.

  u(a,r) = a_r + 2 p a U_r     (the proved first correction)
  D2a(a,r) = (   a_{ap+r} - a_a u(a,r) ) / p^2   mod p
  D2b(a,r) = ( p^3 b_{ap+r} - b_a u(a,r) ) / p^2 mod p

Then: identify.  Level-a library (level-r factors are read off by rank
factorisation), and the carry functional
  kappa_p(r) = sum_{s<=r, r+s>=p} A(r,s) / p^2
which is the only p-DEPENDENT letter the expansion can produce at this order.
"""
from fractions import Fraction as F
from core import av, bv, A, Hs, vp, modp, rank_fp, rref_fp, BIG

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31]

_U = {}
def U(r):
    if r not in _U:
        _U[r] = sum((A(r, s) * (Hs(r + s, 1) - Hs(r - s, 1))
                     for s in range(r + 1)), F(0))
    return _U[r]


def kappa(p, r):
    t = sum(A(r, s) for s in range(r + 1) if r + s >= p)
    assert t % p ** 2 == 0
    return t // p ** 2


def mats(p):
    Ma, Mb = [], []
    for a in range(1, p):
        ra, rb = [], []
        for r in range(p):
            n = a * p + r
            u = av(r) + 2 * p * a * U(r)
            da = (av(n) - av(a) * u) / p ** 2
            db = (F(p) ** 3 * bv(n) - bv(a) * u) / p ** 2
            ra.append(modp(da, p)); rb.append(modp(db, p))
        Ma.append(ra); Mb.append(rb)
    return Ma, Mb


print('=' * 74)
print('T1(iii)  SECOND-ORDER DEFECT RANKS over F_p')
print('=' * 74)
print('%-5s %8s %8s' % ('p', 'rk D2a', 'rk D2b'))
store = {}
for p in PRIMES:
    Ma, Mb = mats(p)
    store[p] = (Ma, Mb)
    print('%-5d %8d %8d' % (p, rank_fp(Ma, p), rank_fp(Mb, p)))

print('\n--- row space (rref) of D2b, small primes ---')
for p in (5, 7, 11):
    R, pc = rref_fp(store[p][1], p)
    print(' p=%-3d pivots=%s' % (p, pc))
    for row in R:
        print('       %s' % ' '.join('%3d' % x for x in row))
print('--- row space (rref) of D2a ---')
for p in (5, 7, 11):
    R, pc = rref_fp(store[p][0], p)
    print(' p=%-3d pivots=%s' % (p, pc))
    for row in R:
        print('       %s' % ' '.join('%3d' % x for x in row))

print('\n--- is the r-side row space the SAME for the two rows? ---')
for p in PRIMES:
    Ma, Mb = store[p]
    ra, _ = rref_fp(Ma, p)
    rb, _ = rref_fp(Mb, p)
    both, _ = rref_fp(Ma + Mb, p)
    print(' p=%-3d rk(a)=%d rk(b)=%d rk(stacked)=%d  %s'
          % (p, len(ra), len(rb), len(both),
             'SAME row space' if len(both) == max(len(ra), len(rb)) else 'DIFFERENT'))
