"""T3b, part 4: THE SCALAR FROBENIUS FORM.

Prediction from the rank-1 defect + Theorem C + Lemma Phi:  in the W-normalisation
    Wh_n = Phat_n - H3(n) Q_n ,   W_n = P_n - H5(n) Q_n ,
the whole graded triple is multiplied by ONE scalar by the low digit:

    ( Q_n , p^3 Wh_n , p^5 W_n )  ==  ( Q_a , Wh_a , W_a ) * u(a,r)   (mod p^2)
    u(a,r) := Q_r + p a Psi_r ,    Psi_r := sum_{s,t<=r} T(r,s,t) Phi(s,t),
    Phi(s,t) = H_{r+s} + H_{r+t} + H_{r+s+t} + H_r - 2H_{r-s} - 2H_{r-t}.

Equivalently the ratio (Frobenius) form, with NO low digit at all:
    p^3 Wh_n Q_q == Wh_q Q_n ,   p^5 W_n Q_q == W_q Q_n   (mod p^k),  q = floor(n/p).
We measure the exact floor k for every row, both normalisations (P vs W).
"""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import Q, P, Ph, Hs, T, vp

PRIMES = [7, 11, 13, 17, 19, 23]
NMAX = 360
BIG = 10 ** 9


def vpF(x, p):
    return vp(x, p) if x != 0 else BIG


def fmt(v):
    return 'inf' if v >= BIG else str(v)


def Wh(n):
    return Ph(n) - Hs(n, 3) * Q(n)


def W(n):
    return P(n) - Hs(n, 5) * Q(n)


_psi = {}
def Psi(r):
    if r in _psi:
        return _psi[r]
    tot = F(0)
    for s in range(r + 1):
        for t in range(r + 1):
            phi = (Hs(r + s, 1) + Hs(r + t, 1) + Hs(r + s + t, 1) + Hs(r, 1)
                   - 2 * Hs(r - s, 1) - 2 * Hs(r - t, 1))
            tot += T(r, s, t) * phi
    _psi[r] = tot
    return tot


print('=' * 78)
print('(F1) SCALAR FORM   (Q_n, p^3 Wh_n, p^5 W_n) == (Q_a, Wh_a, W_a) * u(a,r)')
print('     u(a,r) = Q_r + p a Psi_r         [single-digit cells n = ap+r, 1<=a<p]')
print('     %-4s %7s %10s %10s %10s' % ('p', 'cells', 'floor Q', 'floor Wh', 'floor W'))
for p in PRIMES:
    mQ = mH = mW = BIG
    cells = 0
    for a in range(1, p):
        for r in range(0, p):
            n = a * p + r
            if n > NMAX:
                continue
            cells += 1
            u = Q(r) + F(p) * a * Psi(r)
            mQ = min(mQ, vpF(Q(n) - Q(a) * u, p))
            mH = min(mH, vpF(F(p) ** 3 * Wh(n) - Wh(a) * u, p))
            mW = min(mW, vpF(F(p) ** 5 * W(n) - W(a) * u, p))
    print('     %-4d %7d %10s %10s %10s' % (p, cells, fmt(mQ), fmt(mH), fmt(mW)))

print('\n(F2) RATIO / FROBENIUS FORM   q = floor(n/p),  ALL n <= %d' % NMAX)
print('     v_p( p^w Y_n Q_q - Y_q Q_n )    for Y in {Phat, Wh, P, W}')
print('     %-6s %-3s %s' % ('row', 'w', ' '.join('%7s' % ('p=%d' % p) for p in PRIMES)))
for name, Y, w in (('Phat', Ph, 3), ('Wh', Wh, 3), ('P', P, 5), ('W', W, 5)):
    out = []
    for p in PRIMES:
        m = BIG
        for n in range(p, NMAX + 1):
            q = n // p
            m = min(m, vpF(F(p) ** w * Y(n) * Q(q) - Y(q) * Q(n), p))
        out.append(fmt(m))
    print('     %-6s %-3d %s' % (name, w, ' '.join('%7s' % o for o in out)))

print('\n(F3) RATIO FORM restricted to SINGLE-DIGIT q  (1 <= q < p)')
print('     %-6s %-3s %s' % ('row', 'w', ' '.join('%7s' % ('p=%d' % p) for p in PRIMES)))
for name, Y, w in (('Phat', Ph, 3), ('Wh', Wh, 3), ('P', P, 5), ('W', W, 5)):
    out = []
    for p in PRIMES:
        m = BIG
        for n in range(p, min(NMAX, p * p - 1) + 1):
            q = n // p
            if not (1 <= q < p):
                continue
            m = min(m, vpF(F(p) ** w * Y(n) * Q(q) - Y(q) * Q(n), p))
        out.append(fmt(m))
    print('     %-6s %-3d %s' % (name, w, ' '.join('%7s' % o for o in out)))
