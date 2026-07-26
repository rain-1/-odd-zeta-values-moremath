"""THIRD-order defect: where the CROSS TERM appears.

  u3(a,r) = Adig(p,r; pa) truncated at eps^2      (the proved depth-3 scalar)
  D3a = (   a_{ap+r} - a_a u3 ) / p^3   mod p
  D3b = ( p^3 b_{ap+r} - b_a u3 ) / p^3 mod p

PREDICTION (derived):  H^(3)_m = p^{-3} H^(3)_{floor(m/p)} + G_m  with
G_m = sum_{j<=m, p!|j} j^{-3};  G_{ap+r} = H^(3)_r  and  G_{cp+s} = H^(3)_s (mod p)
because a full block sum_{t=1}^{p-1} t^{-3} = 0 (mod p) for p >= 5.  Hence
  p^3 b_n = [scalar part] + p^3 * sum_k A(n,k)(2 G_n - G_k),  and the second piece
  = a_a * b_r   (mod p).   So D3b - a_a b_r should be the same SCALAR channel as D3a.

=> matrix law   (a_n, p^3 b_n) = (a_a, b_a) * [[u, p^3 b_r],[0, u]]
"""
from fractions import Fraction as F
from core import av, bv, A, Hs, vp, modp, rank_fp, rref_fp, BIG
from dseries import Adig_at

PRIMES = [5, 7, 11, 13, 17, 19, 23]


def u3(p, a, r):
    return Adig_at(p, r, F(p * a), 4, order=2)


def mats(p):
    Ma, Mb, Mc = [], [], []
    for a in range(1, p):
        ra, rb, rc = [], [], []
        for r in range(p):
            n = a * p + r
            u = u3(p, a, r)
            da = (av(n) - av(a) * u) / p ** 3
            db = (F(p) ** 3 * bv(n) - bv(a) * u) / p ** 3
            ra.append(modp(da, p)); rb.append(modp(db, p))
            rc.append((modp(db, p) - av(a) % p * modp(bv(r), p)) % p)
        Ma.append(ra); Mb.append(rb); Mc.append(rc)
    return Ma, Mb, Mc


print('=' * 78)
print('THIRD-ORDER DEFECT: ranks, and the cross term  a_a * b_r')
print('=' * 78)
print('%-5s %8s %8s %10s %14s' % ('p', 'rk D3a', 'rk D3b', 'rk D3b-xt', 'same r-space?'))
for p in PRIMES:
    Ma, Mb, Mc = mats(p)
    ra = rank_fp(Ma, p); rb = rank_fp(Mb, p); rc = rank_fp(Mc, p)
    st = rank_fp(Ma + Mc, p)
    print('%-5d %8d %8d %10d %14s' % (p, ra, rb, rc, 'YES' if st == max(ra, rc)
                                      else 'no (%d)' % st))

print('\n' + '=' * 78)
print('THE MATRIX LAW:  floor of  v_p( p^3 b_n - b_a u3 - p^3 a_a b_r )')
print('  compared with   v_p( p^3 b_n - b_a u3 )   and   v_p( a_n - a_a u3 )')
print('=' * 78)
print('%-5s %12s %12s %12s' % ('p', 'a-row', 'b-row raw', 'b-row + xt'))
for p in PRIMES:
    m1 = m2 = m3 = BIG
    for a in range(1, p):
        for r in range(p):
            n = a * p + r
            u = u3(p, a, r)
            m1 = min(m1, vp(av(n) - av(a) * u, p))
            d = F(p) ** 3 * bv(n) - bv(a) * u
            m2 = min(m2, vp(d, p))
            m3 = min(m3, vp(d - F(p) ** 3 * av(a) * bv(r), p))
    print('%-5d %12s %12s %12s' % (p, m1, m2, m3))
