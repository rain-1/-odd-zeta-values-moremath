"""THE SCALAR LAW.  Conjecture:  the low digit acts by the Gamma-DEFORMED Apery
number evaluated at eps = p*a :

    ( a_{ap+r} , p^3 b_{ap+r} )  =  ( a_a , b_a ) * Adef(r; p a)   mod p^{m+1}

with Adef truncated at order eps^m.  Test the floor for m = 0..6.
"""
import sys
from fractions import Fraction as F
from core import av, bv, vp, BIG
from series import Adef, Adef_at

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31]
MMAX = 6

print('=' * 78)
print('SCALAR LAW:  floor of v_p( X_n - X_a * Adef(r; pa) )  truncated at eps^m')
print('  X = a  (top row)      and      X = p^3 b  (weight-3 row)')
print('=' * 78)
hdr = '  '.join('m=%d' % m for m in range(MMAX + 1))
print('%-5s %-6s %s' % ('p', 'row', hdr))
for p in PRIMES:
    for tag in ('a', 'b'):
        floors = []
        for m in range(MMAX + 1):
            mn = BIG
            for a in range(1, p):
                for r in range(p):
                    n = a * p + r
                    u = Adef_at(r, F(p * a), M=MMAX + 1, order=m)
                    if tag == 'a':
                        d = av(n) - av(a) * u
                    else:
                        d = F(p) ** 3 * bv(n) - bv(a) * u
                    mn = min(mn, vp(d, p))
            floors.append(mn)
        print('%-5d %-6s %s' % (p, tag, '  '.join('%3s' % ('inf' if f >= BIG else f)
                                                  for f in floors)))
