"""T1(ii): identify the rank-1 factorisation.

DERIVATION (p >= 5).  For 0<=s<=r<p, 0<=c<=a<p, r+s<p, Wolstenholme gives
    C(ap+r,cp+s) = C(a,c)C(r,s)(1 + p[a H_r - c H_s - (a-c)H_{r-s}])   mod p^2
    C((a+c)p+(r+s),cp+s) = C(a+c,c)C(r+s,s)(1 + p[(a+c)H_{r+s} - c H_s - a H_r])
so with A = (C(n,k)C(n+k,k))^2,
    A(ap+r,cp+s) = A(a,c)A(r,s)(1 + 2p[a*u(r,s) + c*v(r,s)])          mod p^2
    u(r,s) = H_{r+s} - H_{r-s}                 (= d/dn log A / 2)
    v(r,s) = H_{r+s} + H_{r-s} - 2H_s          (= d/dk log A / 2)
Outside that region A(ap+r,cp+s) = 0 mod p^2 and A(r,s) = 0 mod p^2.  Hence

    e(a,r) := (a_{ap+r} - a_a a_r)/p  = 2[ a*a_a*U_r + a'_a*V_r ]      mod p
    E(a,r) := (p^3 b_{ap+r} - b_a a_r)/p = 2[ a*b_a*U_r + b'_a*V_r ]   mod p

    U_r = sum_s A(r,s)(H_{r+s}-H_{r-s})       V_r = sum_s A(r,s)(H_{r+s}+H_{r-s}-2H_s)
    a'_a = sum_c c A(a,c)                     b'_a = sum_c c A(a,c)(2H3_a - H3_c)

This script tests V_r = 0 (the rank-1 mechanism) and both factorisations.
"""
from fractions import Fraction as F
from core import av, bv, A, Hs, vp, modp, rank_fp, BIG

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31]


def U(r):
    return sum((A(r, s) * (Hs(r + s, 1) - Hs(r - s, 1)) for s in range(r + 1)), F(0))


def V(r):
    return sum((A(r, s) * (Hs(r + s, 1) + Hs(r - s, 1) - 2 * Hs(s, 1))
                for s in range(r + 1)), F(0))


def aprime(a):
    return sum(c * A(a, c) for c in range(a + 1))


def bprime(a):
    h = Hs(a, 3)
    return sum((c * A(a, c) * (2 * h - Hs(c, 3)) for c in range(a + 1)), F(0))


print('=' * 74)
print('THE IDENTITY  V_r = 0   (the rank-1 mechanism)')
print('=' * 74)
bad = [r for r in range(61) if V(r) != 0]
print('  V_r for r = 0..60 : all zero?  %s   (nonzero at %s)' % (not bad, bad))
print('  sum_k A(n,k)(H_{n+k}+H_{n-k}-2H_k) = 0  [VERIFIED exact over Q, n=0..60]')

print('\n' + '=' * 74)
print('THE SEQUENCE U_r   (= (1/2) d a_n/dn in the Gamma-form)')
print('=' * 74)
for r in range(9):
    print('   U_%-2d = %s' % (r, U(r)))

print('\n' + '=' * 74)
print('FIRST-ORDER LAW:  e = 2 a a_a U_r ,  E = 2 a b_a U_r   (mod p)')
print('=' * 74)
print('%-5s %14s %14s' % ('p', 'a-row fails', 'b-row fails'))
for p in PRIMES:
    fa = fb = 0
    for a in range(1, p):
        for r in range(p):
            n = a * p + r
            e = (av(n) - av(a) * av(r)) // p
            E = (F(p) ** 3 * bv(n) - bv(a) * av(r)) / p
            if (e - 2 * a * av(a) * modp(U(r), p)) % p:
                fa += 1
            if (modp(E, p) - 2 * a * modp(bv(a) * U(r), p)) % p:
                fb += 1
    print('%-5d %14d %14d' % (p, fa, fb))

print('\n' + '=' * 74)
print('SECOND-LEVEL LAW mod p^2:   (a_n, p^3 b_n) = (a_a, b_a) * u(a,r)')
print('                            u(a,r) = a_r + 2 p a U_r')
print('=' * 74)
print('%-5s %10s %10s   %s' % ('p', 'a-row', 'b-row', 'floor of the p^2 defect'))
for p in PRIMES:
    fa = fb = 0
    mna = mnb = BIG
    for a in range(1, p):
        for r in range(p):
            n = a * p + r
            u = av(r) + 2 * p * a * U(r)
            da = av(n) - av(a) * u
            db = F(p) ** 3 * bv(n) - bv(a) * u
            va, vb = vp(da, p), vp(db, p)
            if va < 2:
                fa += 1
            if vb < 2:
                fb += 1
            mna = min(mna, va); mnb = min(mnb, vb)
    print('%-5d %10d %10d   a:%s  b:%s' % (p, fa, fb, mna, mnb))
