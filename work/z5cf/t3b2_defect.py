"""T3b, part 2: the mod-p^2 defect of the graded congruences.

The (A) congruences close at depth exactly 1, so the defect
     Delta(a,r) := ( p^5 P_{ap+r} - P_a Q_r ) / p    mod p
is a well-defined nonzero function on the (p-1) x p grid of digits.  If the
Frobenius matrix has a genuine cross entry, Delta must be BILINEAR in the digits
(rank <= small as a matrix over F_p), the rank being the number of graded cross
terms.  Rank is measured with no model assumed.
"""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import Q, P, Ph, vp

PRIMES = [7, 11, 13, 17, 19, 23]
NMAX = 360


def modp(x, p):
    """image of a p-integral rational in F_p"""
    a, b = x.numerator, x.denominator
    assert b % p != 0, 'not p-integral'
    return a % p * pow(b % p, p - 2, p) % p


def rank_fp(M, p):
    M = [row[:] for row in M]
    rows = len(M); cols = len(M[0]) if rows else 0
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] % p:
                piv = i; break
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


print('=' * 78)
print('DEFECT RANK TEST  (rank of the digit-matrix Delta(a,r) over F_p)')
print('=' * 78)

for tag, num in (
        ('w5:  (p^5 P_n - P_a Q_r)/p',
         lambda p, a, r, n: (F(p) ** 5 * P(n) - P(a) * Q(r)) / p),
        ('w3:  (p^4 Phat_n - p Phat_a Q_r)/p',
         lambda p, a, r, n: (F(p) ** 4 * Ph(n) - p * Ph(a) * Q(r)) / p),
        ('Qrow:(Q_n - Q_a Q_r)/p',
         lambda p, a, r, n: (Q(n) - Q(a) * Q(r)) / p),
):
    print('\n%s' % tag)
    print('   %-4s %8s %8s %8s   %s' % ('p', 'rows', 'cols', 'rank', 'note'))
    for p in PRIMES:
        A = list(range(1, p))
        R = list(range(0, p))
        A = [a for a in A if a * p + p - 1 <= NMAX or a * p <= NMAX]
        M = []
        ok = True
        for a in A:
            row = []
            for r in R:
                n = a * p + r
                if n > NMAX:
                    row = None; break
                v = num(p, a, r, n)
                if v.denominator % p == 0:
                    ok = False; row = None; break
                row.append(modp(v, p))
            if row is None:
                continue
            M.append(row)
        if not M or not ok:
            print('   %-4d %8s %8s %8s   %s' % (p, '-', '-', '-',
                  'not p-integral' if not ok else 'no full rows'))
            continue
        rk = rank_fp(M, p)
        print('   %-4d %8d %8d %8d   %s' % (p, len(M), len(M[0]), rk,
              'RANK 1 -> pure product f(a)g(r)' if rk == 1 else
              ('rank %d' % rk)))
