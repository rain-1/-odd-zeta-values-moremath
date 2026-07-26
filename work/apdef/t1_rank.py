"""T1(i): rank over F_p of the first-order defect matrices on the digit grid.

  b-row  E_p(a,r) = ( p^3 b_{ap+r} - b_a a_r ) / p
  a-row  e_p(a,r) = (     a_{ap+r} - a_a a_r ) / p

Rows a = 1..p-1, columns r = 0..p-1.  (a = 0 is identically 0: b_0 = 0.)
No model assumed.
"""
from fractions import Fraction as F
from core import av, bv, vp, modp, rank_fp, rref_fp, BIG

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31]


def mat_b(p):
    return [[modp((F(p) ** 3 * bv(a * p + r) - bv(a) * av(r)) / p, p)
             for r in range(p)] for a in range(1, p)]


def mat_a(p):
    return [[(av(a * p + r) - av(a) * av(r)) // p % p
             for r in range(p)] for a in range(1, p)]


print('=' * 74)
print('T1(i)  FIRST-ORDER DEFECT RANKS over F_p   (grid a=1..p-1, r=0..p-1)')
print('=' * 74)
print('%-5s %6s %6s %8s %8s' % ('p', 'rows', 'cols', 'rank(E)', 'rank(e)'))
store = {}
for p in PRIMES:
    Mb = mat_b(p)
    Ma = mat_a(p)
    store[p] = (Mb, Ma)
    print('%-5d %6d %6d %8d %8d' % (p, p - 1, p, rank_fp(Mb, p), rank_fp(Ma, p)))

print('\n--- E matrix, p = 5 and 7 (rows a=1.., cols r=0..) ---')
for p in (5, 7):
    print(' p=%d' % p)
    for i, row in enumerate(store[p][0]):
        print('   a=%d  %s' % (i + 1, ' '.join('%3d' % x for x in row)))
print('\n--- e (a-row) matrix, p = 5 and 7 ---')
for p in (5, 7):
    print(' p=%d' % p)
    for i, row in enumerate(store[p][1]):
        print('   a=%d  %s' % (i + 1, ' '.join('%3d' % x for x in row)))

print('\n--- column space / row space structure (rref of E) ---')
for p in PRIMES[:5]:
    R, pc = rref_fp(store[p][0], p)
    print(' p=%-3d rank=%d pivots=%s' % (p, len(R), pc))
    for row in R:
        print('        %s' % ' '.join('%3d' % x for x in row))
