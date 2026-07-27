"""Extract the one-dimensional-looking residual left by eps25.

This is discovery code in Sol's writable tree.  It imports only the committed
generator descriptions from work/z5eps and writes nothing there.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F

import numpy as np

sys.path.insert(0, "../z5eps")
import eps25 as E25
from eps22 import DELTA5, MIDX, MON, NM, SIG

P = int(sys.argv[1]) if len(sys.argv) > 1 else 2147483647


def fm(fr):
    fr = F(fr)
    return fr.numerator % P * pow(fr.denominator % P, P - 2, P) % P


forms = E25.GEN_FORMS + E25.NEWF
names = E25.GEN_NAMES + E25.NEWN
print("forms", len(forms), "monomials", NM, flush=True)

g = np.zeros((len(forms), NM), dtype=np.int64)
for i, form in enumerate(forms):
    g[i] = E25.form_to_vec_modp(form, P)
i2 = pow(2, P - 2, P)
g = (g + g[:, SIG]) * i2 % P

d = np.zeros(NM, dtype=np.int64)
for mon, c in DELTA5.items():
    d[MIDX[mon]] = fm(c)
d = (d + d[SIG]) * i2 % P


def rref_rows(a):
    a = a.copy()
    rows, cols = a.shape
    rank = 0
    pivots = []
    for col in range(cols):
        nz = np.nonzero(a[rank:, col] % P)[0]
        if not len(nz):
            continue
        pr = rank + int(nz[0])
        if pr != rank:
            a[[rank, pr]] = a[[pr, rank]]
        a[rank] = a[rank] * pow(int(a[rank, col]), P - 2, P) % P
        factors = a[:, col].copy()
        factors[rank] = 0
        rr = np.nonzero(factors)[0]
        if len(rr):
            a[rr] = (a[rr] - factors[rr, None] * a[rank][None, :]) % P
        pivots.append(col)
        rank += 1
        if rank == rows:
            break
        if rank % 50 == 0:
            print("rank", rank, "pivot", col, flush=True)
    return a[:rank], pivots


basis, pivots = rref_rows(g)
print("rank", len(pivots), flush=True)
r = d.copy()
for row, col in zip(basis, pivots):
    if r[col]:
        r = (r - r[col] * row) % P

support = np.nonzero(r)[0]
print("residual support", len(support))
for i in support:
    c = int(r[i])
    centered = c if c <= P // 2 else c - P
    print(i, centered, MON[i])
