"""Enlarge the anti-diagonal Laurent search by all natural affine endpoints.

Every generated column is still an exact zero identity: it is a finite linear
combination of Laurent coefficients of either R_n(x,m-x) == 0 or R_n(x,j) == 0.
The modular solve is used only to discover a short combination; any hit must
be reconstructed over Q and checked coefficientwise afterwards.
"""

from fractions import Fraction as F
import numpy as np

import search_antidiag_laurent as S
import search_t3zeros as OLD
import fastlin


AFFINE = {
    'n-t-m': lambda n, t, m: n - t - m,
    'n+t-m': lambda n, t, m: n + t - m,
    'n-t+m': lambda n, t, m: n - t + m,
    'm-t': lambda n, t, m: m - t,
    't-m': lambda n, t, m: t - m,
}


def admissible(region, arg, positive):
    for n in range(1, 10):
        for t, m in S.REGIONS[region](n):
            value = arg(n, t, m)
            if value < (1 if positive else 0):
                return False
    return True


def columns():
    out = OLD.columns()
    out += [(f'Laurent0/{rg}/{nm}', S.column(rg, wt))
            for rg in S.REGIONS for nm, wt in S.WEIGHTS]
    out += [(f'Laurent1/{rg}', S.column(rg, lambda n, t, m: F(1), 1))
            for rg in S.REGIONS]
    out += [(f'Vertical0/{rg}/{nm}', S.column_vertical(rg, wt))
            for rg in S.REGIONS for nm, wt in S.WEIGHTS]
    out += [(f'Vertical1/{rg}',
             S.column_vertical(rg, lambda n, t, m: F(1), 1))
            for rg in S.REGIONS]

    for rg in S.REGIONS:
        for nm, arg in AFFINE.items():
            if admissible(rg, arg, False):
                wt = lambda n, t, m, arg=arg: S.h(arg(n, t, m))
                out.append((f'Laurent0/{rg}/H_{nm}', S.column(rg, wt)))
                out.append((f'Vertical0/{rg}/H_{nm}',
                            S.column_vertical(rg, wt)))
            if admissible(rg, arg, True):
                wt = lambda n, t, m, arg=arg: F(1, arg(n, t, m))
                out.append((f'Laurent0/{rg}/inv_{nm}', S.column(rg, wt)))
                out.append((f'Vertical0/{rg}/inv_{nm}',
                            S.column_vertical(rg, wt)))
    return out


if __name__ == '__main__':
    cols = columns()
    cells = [(n, k, l) for n in range(1, 9)
             for k in range(n + 1) for l in range(n + 1)]
    rows, rhs = [], []
    for n, k, l in cells:
        target = S.target(n, k, l)
        values = [fn(n, k, l) for _, fn in cols]
        for component in range(3):
            rows.append([S.mq(value[component]) for value in values])
            rhs.append(S.mq(target[component]))
    matrix = np.array(rows, dtype=np.int64)
    vector = np.array(rhs, dtype=np.int64)
    solution, rank, _, bad = fastlin.solve(matrix, vector, S.P)
    print('rows=%d cols=%d rank=%d bad=%d' %
          (len(rows), len(cols), rank, bad))
    if bad == 0:
        support = [(cols[i][0], int(solution[i]))
                   for i in range(len(cols)) if solution[i] % S.P]
        print('support', len(support))
        for item in support:
            print(item)
