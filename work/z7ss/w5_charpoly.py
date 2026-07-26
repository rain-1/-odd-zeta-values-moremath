"""Exact order-3 degree-9 recurrence for the weight-5 BZ leading coefficients Q_n,
and its characteristic polynomial.  Completes the structural ladder
    weight 3 (Apery, SINGLE sum)  -> order 2, char L^2 - 34 L + 1
    weight 5 (BZ M08, DOUBLE sum) -> order 3, char ?
    weight 7 (BZ M010, ???)       -> order 4, char L^4-6340L^3+67974L^2-6340L+1
"""
from math import comb
from fractions import Fraction
import numpy as np


def Q(n):
    s = 0
    for k1 in range(n + 1):
        w1 = comb(n + k1, n) * comb(n, k1) ** 2
        for k2 in range(n + 1):
            s += w1 * comb(n + k2, n) * comb(n, k2) ** 2 * comb(n + k1 + k2, n)
    return s


ORDER, DEG = 3, 9
seq = [Q(n) for n in range(60)]
ncol = (ORDER + 1) * (DEG + 1)
rows = []
for n in range(ncol + 6):
    row = []
    for j in range(ORDER + 1):
        v = seq[n + j]
        for d in range(DEG + 1):
            row.append(Fraction(v * n ** d))
    rows.append(row)

m = len(rows)
piv = []
r = 0
for c in range(ncol):
    pr = next((i for i in range(r, m) if rows[i][c] != 0), None)
    if pr is None:
        continue
    rows[r], rows[pr] = rows[pr], rows[r]
    pv = rows[r][c]
    rows[r] = [x / pv for x in rows[r]]
    for i in range(m):
        if i != r and rows[i][c] != 0:
            f = rows[i][c]
            rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
    piv.append(c)
    r += 1
free = [c for c in range(ncol) if c not in piv]
print("rank", r, "nullity", len(free))
assert len(free) == 1
sol = [Fraction(0)] * ncol
sol[free[0]] = Fraction(1)
for i, c in enumerate(piv):
    sol[c] = -rows[i][free[0]]
den = 1
for x in sol:
    den = den * x.denominator // __import__("math").gcd(den, x.denominator)
isol = [int(x * den) for x in sol]
g = 0
for x in isol:
    g = __import__("math").gcd(g, x)
isol = [x // g for x in isol]
P = [isol[j * (DEG + 1):(j + 1) * (DEG + 1)] for j in range(ORDER + 1)]
print("polys p_0..p_3 (coeff of n^0..n^9):")
for j, p in enumerate(P):
    print(" p%d =" % j, p)
# verify
bad = sum(1 for n in range(len(seq) - ORDER)
          if sum(sum(c * n ** d for d, c in enumerate(P[j])) * seq[n + j]
                 for j in range(ORDER + 1)) != 0)
print("verification failures:", bad, "of", len(seq) - ORDER)
lead = [P[j][DEG] for j in range(ORDER + 1)]
print("char_lead:", lead)
g = 0
for x in lead:
    g = __import__("math").gcd(g, x)
print("char poly coeffs (L^3..L^0):", [x // g for x in reversed(lead)])
r = np.roots([x // g for x in reversed(lead)])
print("roots:", sorted(r.real, reverse=True))
