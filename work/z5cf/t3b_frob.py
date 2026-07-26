"""T3b -- the Frobenius matrix congruence for the Brown-Zudilin triple (Q, Phat, P).

Objects.  Phi_n = [[Q_n,0,0],[Phat_n,Q_n,0],[P_n,X_n,Q_n]]  (lower triangular),
D = diag(1, p^3, p^5)  (the conjectured graded Frobenius diag(1,p^3,p^5)).
Conjugation  Phi^ := D Phi D^{-1}  multiplies entry (i,j) by p^{w_i-w_j}, w=(0,3,5).

Tested statements (exact rational arithmetic, exact ladders n <= 360):

 (A) graded single-digit :  D Phi_n D^{-1}  ==  Phi_a * (Q_r I)      (n = ap+r, a<p)
 (B) naive product       :  Phi^_n == Phi^_a Phi^_r    (same matrix on both digits)
 (C) master/ratio        :  D Phi_n D^{-1} Q_q == Phi_q Q_n          (q = floor(n/p))
 (D) unipotent           :  D U_n D^{-1} == U_q ,  U_n = Phi_n / Q_n
 (E) exponent scan       :  which (s,t) in D = diag(1,p^s,p^t) maximise the floors
"""
import sys, os, json
from fractions import Fraction as F
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import Q, P, Ph, vp, ladders

PRIMES = [7, 11, 13, 17, 19, 23]
NMAX = 360
BIG = 10 ** 9


def vpF(x, p):
    return vp(x, p) if x != 0 else BIG


def fmt(v):
    return '+inf' if v >= BIG else str(v)


print('=' * 78)
print('SANITY: P_0 = %s, Phat_0 = %s, Q_0 = %s  (pure product form B(a)B(r) dies at r=0)'
      % (P(0), Ph(0), Q(0)))
print('=' * 78)

# ---------------------------------------------------------------- (A)
print('\n(A) GRADED SINGLE-DIGIT   D Phi_n D^-1 == Phi_a . (Q_r I),  n = ap+r, 1<=a<p')
print('    entry (1,1): Q_n - Q_a Q_r      [PROVED Lucas]')
print('    entry (2,1): p^3 Phat_n - Phat_a Q_r')
print('    entry (3,1): p^5 P_n   - P_a Q_r')
print('    %-4s %8s %8s %8s %10s %10s %8s' %
      ('p', 'cells', 'min(1,1)', 'min(2,1)', 'min(2,1)|int', 'min(3,1)', 'nonint'))
for p in PRIMES:
    m11 = m21 = m31 = BIG
    m21i = BIG
    cells = 0
    nonint = 0
    for a in range(1, p):
        for r in range(0, p):
            n = a * p + r
            if n > NMAX:
                continue
            cells += 1
            m11 = min(m11, vpF(Q(n) - Q(a) * Q(r), p))
            e21 = vpF(p ** 3 * Ph(n) - Ph(a) * Q(r), p)
            m21 = min(m21, e21)
            if vp(Ph(a), p) >= 0:
                m21i = min(m21i, e21)
            else:
                nonint += 1
            m31 = min(m31, vpF(p ** 5 * P(n) - P(a) * Q(r), p))
    print('    %-4d %8d %8s %8s %10s %10s %8d'
          % (p, cells, fmt(m11), fmt(m21), fmt(m21i), fmt(m31), nonint))

# ---------------------------------------------------------------- (B)
print('\n(B) NAIVE PRODUCT  Phi^_n == Phi^_a Phi^_r  with Phi^ = D Phi D^-1, X = c3*p^2*Phat')
print('    (2,1): p^3 Phat_n - [ p^3 Phat_a Q_r + Q_a p^3 Phat_r ]')
print('    the two candidate right-hand sides are compared:')
print('    %-4s %14s %14s %14s' % ('p', 'v(prod form)', 'v(Phat_a Q_r)', 'v(Q_a Phat_r)'))
for p in PRIMES:
    mp = mA = mB = BIG
    for a in range(1, p):
        for r in range(0, p):
            n = a * p + r
            if n > NMAX:
                continue
            lhs = F(p) ** 3 * Ph(n)
            mp = min(mp, vpF(lhs - (F(p) ** 3 * Ph(a) * Q(r) + Q(a) * F(p) ** 3 * Ph(r)), p))
            mA = min(mA, vpF(lhs - Ph(a) * Q(r), p))
            mB = min(mB, vpF(Q(a) * Ph(r), p))
    print('    %-4d %14s %14s %14s' % (p, fmt(mp), fmt(mA), fmt(mB)))

# ---------------------------------------------------------------- (C)
print('\n(C) MASTER / RATIO FORM  (q = floor(n/p), ALL n <= %d, no digit restriction)' % NMAX)
print('    p^3 Phat_n Q_q - Phat_q Q_n      and      p^5 P_n Q_q - P_q Q_n')
print('    %-4s %8s %12s %12s %12s' % ('p', 'cells', 'floor w=3', 'floor w=5', 'floor Qrow'))
for p in PRIMES:
    m3 = m5 = mq = BIG
    cells = 0
    for n in range(p, NMAX + 1):
        q = n // p
        if q < 1:
            continue
        cells += 1
        m3 = min(m3, vpF(F(p) ** 3 * Ph(n) * Q(q) - Ph(q) * Q(n), p))
        m5 = min(m5, vpF(F(p) ** 5 * P(n) * Q(q) - P(q) * Q(n), p))
        mq = min(mq, vpF(Q(n) - Q(q) * Q(n % p), p))
    print('    %-4d %8d %12s %12s %12s' % (p, cells, fmt(m3), fmt(m5), fmt(mq)))

# ---------------------------------------------------------------- (E)
print('\n(E) EXPONENT SCAN: floor of  v_p( p^s Y_n Q_q - Y_q Q_n ),  q = floor(n/p)')
print('    %-4s %-6s %s' % ('row', 's', '  '.join('p=%d' % p for p in PRIMES)))
for name, Y in (('Phat', Ph), ('P', P)):
    for s in range(0, 8):
        out = []
        for p in PRIMES:
            m = BIG
            for n in range(p, NMAX + 1):
                q = n // p
                m = min(m, vpF(F(p) ** s * Y(n) * Q(q) - Y(q) * Q(n), p))
            out.append(fmt(m))
        print('    %-4s %-6d %s' % (name, s, '  '.join('%6s' % o for o in out)))
