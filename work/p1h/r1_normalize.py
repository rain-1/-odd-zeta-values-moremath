"""P1h R1: normalize (REC-*).

n0 = (p-5)/2  <=>  2n0+5 = p  =>  n0 == -5/2 (mod p).
So c_i(n0) mod p = c_i(-5/2) mod p : UNIVERSAL rational numbers, independent of p.
Compute them exactly and clear denominators.
"""
from fractions import Fraction as F
import sys
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import a0, B8, B9

def c0(n): return (n+1)**5 * (n+2) * a0(n+1)
def c1(n): return -2*(n+2)*B8(n)
def c2(n): return -2*B9(n)
def c3(n): return 2*(n+3)**5*(2*n+5)*a0(n)

x = F(-5,2)
r0, r1, r2 = c0(x), c1(x), c2(x)
print('c0(-5/2) =', r0)
print('c1(-5/2) =', r1)
print('c2(-5/2) =', r2)
print('c3(-5/2) =', c3(x), '  (must be 0)')
from math import gcd
den = 1
for r in (r0,r1,r2):
    den = den*r.denominator//gcd(den,r.denominator)
R = [int(r*den) for r in (r0,r1,r2)]
g = 0
for v in R: g = gcd(g, v)
R = [v//g for v in R]
print('common denominator', den, ' content', g)
print('normalized (R0,R1,R2) =', R)
print('July A1-MID row       = (11907, -334374, -19292)')
# also give primitive integer form and factorizations
import sympy
for nm,v in zip(('R0','R1','R2'), R):
    print('  %s = %d = %s' % (nm, v, sympy.factorint(v)))
