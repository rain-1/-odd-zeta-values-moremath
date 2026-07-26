"""Lift the joint (B-bot) certificate u(n,j) to a rational function of n.

u(n,j) = Nu(n,j) / [(j+1)(n+j+1)(n+j+2)(n+j+3)],  deg_j Nu = 12, j^3 | Nu,
and u is UNIQUE (the u-system has full column rank; the homogeneous equation
g(j)v(j+1) = v(j) forces v = c/Phi, not rational, so c = 0).

So each of the 10 surviving coefficients Nu_t(n), t = 3..12, is a well-defined
rational function of n.  Collect them mod p over a range of n and reconstruct.
"""
import pickle
import sys

import numpy as np

import bwz      # noqa: E402  (inserts work/z5star on sys.path)
import fastlin  # noqa: E402
import ratrec   # noqa: E402

D = bwz.DENS['V1']
NC = 13


def coeffs_at(n, p, npts=60, seed=7):
    sol = bwz.solve_x0(n, p, verbose=False)
    if sol is None:
        return None
    rng = np.random.default_rng(seed + n)
    pts, guard = [], 0
    while len(pts) < npts and guard < 200000:
        guard += 1
        x = int(rng.integers(1, p - 5))
        if (x + 1) % p and (n + 3 - x) % p and bwz.dv(D, n, x, p) \
                and bwz.dv(D, n, x + 1, p):
            pts.append(x)
    A, b = [], []
    for x in pts:
        gq = bwz.gratio_Q(n, x)
        gp = gq.numerator % p * pow(gq.denominator % p, p - 2, p) % p
        iD1 = pow(bwz.dv(D, n, x + 1, p), p - 2, p)
        iD0 = pow(bwz.dv(D, n, x, p), p - 2, p)
        A.append([(gp * pow((x + 1) % p, t, p) % p * iD1
                   - pow(x % p, t, p) * iD0) % p for t in range(NC)])
        b.append(bwz.Rfun(sol, x))
    A = np.array(A, dtype=np.int64)
    b = np.array(b, dtype=np.int64)
    X, rk, piv, nbad = fastlin.solve(A, b, p)
    return (None if (nbad or rk != NC) else X)


def main(nmax=48, p=bwz.P1, out='bwz_lift_p%d.pkl'):
    data = {}
    for n in range(1, nmax + 1):
        X = coeffs_at(n, p)
        if X is None:
            print('  n=%2d : no unique u  (skipped)' % n, flush=True)
            continue
        data[n] = [int(v) % p for v in X]
        print('  n=%2d : Nu = %s' % (n, data[n]), flush=True)
    pickle.dump(data, open(out % p, 'wb'))
    print('collected %d values of n' % len(data))
    # zero pattern
    if data:
        zeros = [t for t in range(NC) if all(v[t] == 0 for v in data.values())]
        print('coefficients identically zero for every n: t in %s' % zeros)
    return data


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 48)
