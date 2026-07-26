"""T1, last part: the TWO-DIGIT iteration.  What exactly is lost?

n = b p^2 + s p + r,  N = b p + s = floor(n/p).

(B) one-digit law with a LARGE high part:  p^3 b_{Np+r} vs b_N a_r,  N < p^2
    -- b_N acquires a p^{-3} pole once N >= p, so the O(p) Lucas defect is
       multiplied by O(p^{-3}).  Measured floor quantifies the loss.
(A) naive two-digit product   p^6 b_n  vs  b_b a_s a_r
(C) does the SCALAR law survive a large high part?   a_{Np+r} vs a_N*Adig(p,r;pN)
(D) the corrected two-digit law with the scalar applied twice.
"""
from fractions import Fraction as F
from core import av, bv, A, Hs, vp, modp, BIG
from dseries import Adig_at

PRIMES = [5, 7, 11, 13]

_U = {}
def U(r):
    if r not in _U:
        _U[r] = sum((A(r, s) * (Hs(r + s, 1) - Hs(r - s, 1))
                     for s in range(r + 1)), F(0))
    return _U[r]

print('=' * 78)
print('(B) ONE-DIGIT law with large high part:  v_p( p^3 b_{Np+r} - b_N a_r )')
print('    N < p (Theorem 2 range)  vs  p <= N < p^2  (out of range)')
print('=' * 78)
print('%-5s %18s %18s' % ('p', 'floor, N<p', 'floor, p<=N<p^2'))
for p in PRIMES:
    m1 = m2 = BIG
    for N in range(1, p * p):
        for r in range(p):
            d = F(p) ** 3 * bv(N * p + r) - bv(N) * av(r)
            v = vp(d, p)
            if N < p:
                m1 = min(m1, v)
            else:
                m2 = min(m2, v)
    print('%-5d %18s %18s' % (p, m1, m2))

print('\n' + '=' * 78)
print('   same for the a-row:  v_p( a_{Np+r} - a_N a_r )   (no harmonic weight)')
print('=' * 78)
print('%-5s %18s %18s' % ('p', 'floor, N<p', 'floor, p<=N<p^2'))
for p in PRIMES:
    m1 = m2 = BIG
    for N in range(1, p * p):
        for r in range(p):
            d = av(N * p + r) - av(N) * av(r)
            v = vp(d, p)
            if N < p:
                m1 = min(m1, v)
            else:
                m2 = min(m2, v)
    print('%-5d %18s %18s' % (p, m1, m2))

print('\n' + '=' * 78)
print('(A) NAIVE TWO-DIGIT:  v_p( p^6 b_{bp^2+sp+r} - b_b a_s a_r ),  b>=1')
print('    and             v_p( a_{bp^2+sp+r} - a_b a_s a_r )')
print('=' * 78)
print('%-5s %14s %14s' % ('p', 'b-row floor', 'a-row floor'))
for p in PRIMES:
    mb = ma = BIG
    for b in range(1, p):
        for s in range(p):
            for r in range(p):
                n = b * p * p + s * p + r
                mb = min(mb, vp(F(p) ** 6 * bv(n) - bv(b) * av(s) * av(r), p))
                ma = min(ma, vp(av(n) - av(b) * av(s) * av(r), p))
    print('%-5d %14s %14s' % (p, mb, ma))

print('\n' + '=' * 78)
print('(C) SCALAR law with large high part:  v_p( a_{Np+r} - a_N Adig(p,r;pN) )')
print('    truncation orders m = 0,1,2;  N < p  vs  p <= N < p^2')
print('=' * 78)
print('%-5s %-10s %6s %6s %6s' % ('p', 'range', 'm=0', 'm=1', 'm=2'))
for p in PRIMES:
    for lab, lo, hi in (('N<p', 1, p), ('N>=p', p, p * p)):
        fl = []
        for m in range(3):
            mn = BIG
            for N in range(lo, hi):
                for r in range(p):
                    u = Adig_at(p, r, F(p * N), 4, order=m)
                    mn = min(mn, vp(av(N * p + r) - av(N) * u, p))
            fl.append(mn)
        print('%-5d %-10s %6s %6s %6s' % (p, lab, *fl))

print('\n' + '=' * 78)
print('(D) the b-row two-digit law, GRADED CORRECTLY:')
print('    p^6 b_n  vs  b_b * a_s * a_r   with the p^3-per-digit grading;')
print('    and the first correction  p^6 b_n - b_b[a_s+2psU_s][a_r+2p(bp+s)U_r]')
print('=' * 78)
print('%-5s %14s %14s' % ('p', 'naive', 'corrected'))
for p in PRIMES:
    m0 = m1 = BIG
    for b in range(1, p):
        for s in range(p):
            for r in range(p):
                n = b * p * p + s * p + r
                N = b * p + s
                lhs = F(p) ** 6 * bv(n)
                m0 = min(m0, vp(lhs - bv(b) * av(s) * av(r), p))
                us = av(s) + 2 * p * b * U(s)
                ur = av(r) + 2 * p * N * U(r)
                m1 = min(m1, vp(lhs - bv(b) * us * ur, p))
    print('%-5d %14s %14s' % (p, m0, m1))
