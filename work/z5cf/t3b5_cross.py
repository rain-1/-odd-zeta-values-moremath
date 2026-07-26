"""T3b, part 5: (i) is there a cross term at the NEXT order?  (ii) multi-digit.

(i)  The scalar form closes to depth 2 for Q and W.  If the graded Frobenius had a
     unipotent cross entry it would show up as rank > 1 in the p^2-order defect
         Delta2(a,r) = ( p^5 W_n - W_a u(a,r) ) / p^2   mod p .
(ii) Multi-digit: p^{5s} P_n  vs  P_a * prod Q_{digits}, and the PADIC_SEAM T3 form.
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


def Wh(n): return Ph(n) - Hs(n, 3) * Q(n)
def W(n):  return P(n) - Hs(n, 5) * Q(n)


_psi = {}
def Psi(r):
    if r in _psi:
        return _psi[r]
    tot = F(0)
    for s in range(r + 1):
        for t in range(r + 1):
            tot += T(r, s, t) * (Hs(r + s, 1) + Hs(r + t, 1) + Hs(r + s + t, 1)
                                 + Hs(r, 1) - 2 * Hs(r - s, 1) - 2 * Hs(r - t, 1))
    _psi[r] = tot
    return tot


def modp(x, p):
    a, b = x.numerator, x.denominator
    if b % p == 0:
        return None
    return a % p * pow(b % p, p - 2, p) % p


def rank_fp(M, p):
    M = [row[:] for row in M]
    rows = len(M); cols = len(M[0]) if rows else 0
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c] % p), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][c], p - 2, p)
        M[r] = [x * iv % p for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


print('(i) RANK of the next-order defect  (cross-term detector)')
print('    %-28s %s' % ('object', ' '.join('%5s' % ('p=%d' % p) for p in PRIMES)))
for tag, fn, dv in (
        ('(Q_n - Q_a u)/p^2', lambda p, a, r, n, u: (Q(n) - Q(a) * u), 2),
        ('(p^5 W_n - W_a u)/p^2', lambda p, a, r, n, u: (F(p) ** 5 * W(n) - W(a) * u), 2),
        ('(p^3 Wh_n - Wh_a u)/p', lambda p, a, r, n, u: (F(p) ** 3 * Wh(n) - Wh(a) * u), 1),
):
    out = []
    for p in PRIMES:
        A = [a for a in range(1, p) if a * p + p - 1 <= NMAX]
        M, ok = [], True
        for a in A:
            row = []
            for r in range(p):
                v = fn(p, a, r, a * p + r, Q(r) + F(p) * a * Psi(r)) / F(p) ** dv
                m = modp(v, p)
                if m is None:
                    ok = False; break
                row.append(m)
            if not ok:
                break
            M.append(row)
        out.append('%5s' % (rank_fp(M, p) if (ok and M) else '-'))
    print('    %-28s %s' % (tag, ' '.join(out)))

print('\n(ii) MULTI-DIGIT.  n = a p^s + ... ,  compare p^{w s} Y_n  with  Y_a * prod Q_{r_i}')
print('     %-6s %-3s %-3s %s' % ('row', 'w', 's', ' '.join('%7s' % ('p=%d' % p) for p in PRIMES)))
for name, Y, w in (('Phat', Ph, 3), ('P', P, 5)):
    for s in (1, 2):
        out = []
        for p in PRIMES:
            m = BIG
            seen = 0
            for n in range(p ** s, min(NMAX, p ** (s + 1) - 1) + 1):
                d = []
                x = n
                while x:
                    d.append(x % p); x //= p
                if len(d) != s + 1:
                    continue
                a = d[-1]
                prod = F(1)
                for t in d[:-1]:
                    prod *= Q(t)
                seen += 1
                m = min(m, vpF(F(p) ** (w * s) * Y(n) - Y(a) * prod, p))
            out.append(fmt(m) if seen else '-')
        print('     %-6s %-3d %-3d %s' % (name, w, s, ' '.join('%7s' % o for o in out)))

print('\n(iii) PADIC_SEAM T3 form:  p^{5s} P_{a p^s} Q_{a p^{s-1}} - p^{5(s-1)} P_{a p^{s-1}} Q_{a p^s}')
print('     %-4s %-3s %s' % ('s', '', ' '.join('%7s' % ('p=%d' % p) for p in PRIMES)))
for s in (1, 2):
    out = []
    for p in PRIMES:
        m = BIG
        seen = 0
        for a in range(1, p):
            n1, n0 = a * p ** s, a * p ** (s - 1)
            if n1 > NMAX:
                continue
            seen += 1
            m = min(m, vpF(F(p) ** (5 * s) * P(n1) * Q(n0)
                           - F(p) ** (5 * (s - 1)) * P(n0) * Q(n1), p))
        out.append(fmt(m) if seen else '-')
    print('     %-4d %-3s %s' % (s, '', ' '.join('%7s' % o for o in out)))
