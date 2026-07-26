"""Degree of the residual COFACTOR coefficients as rational functions of n.

Same fast method as o_areduce (one nullspace at a generous bound, then a
polynomial gcd), applied to a sample of the columns of the cofactor vector.
This is the measurement that decides whether the ell-lift of the 8 residual
blocks is of a size Lean can be handed at all.
"""
import sys, pickle
import numpy as np
import ratrec, o_areduce


def load(store, p, key='X'):
    z = np.load(store + '.npz')
    out = {}
    for nm in z.files:
        a, b, kk = nm.split('_')
        if kk != key or int(b) != p: continue
        out[int(a)] = z[nm]
    return out


def degrees(D, p, cols, d=None, verbose=True):
    xs = sorted(D)
    M = len(xs)
    if d is None: d = M // 2 - 3
    out = {}
    for c in cols:
        vals = [int(D[n].reshape(-1)[c]) % p for n in xs]
        if not any(vals):
            out[c] = (None, None, 'identically zero'); continue
        r = o_areduce.recon(vals, xs, p, d)
        if r is None:
            out[c] = (None, None, 'no relation at d<=%d' % d)
        else:
            num, den = r
            ok = all(ratrec.polyval(num, x % p, p)
                     == vals[i] * ratrec.polyval(den, x % p, p) % p
                     for i, x in enumerate(xs))
            out[c] = (len(num) - 1, len(den) - 1, 'fits all %d: %s' % (M, ok))
        if verbose:
            print('   col %-5d : deg num %-5s deg den %-5s  %s'
                  % (c, out[c][0], out[c][1], out[c][2]), flush=True)
    return out


if __name__ == '__main__':
    store = sys.argv[1]; p = int(sys.argv[2])
    key = sys.argv[3] if len(sys.argv) > 3 else 'X'
    ncol = int(sys.argv[4]) if len(sys.argv) > 4 else 8
    d = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    D = load(store, p, key)
    xs = sorted(D)
    print('%d samples, n = %d .. %d,  vector length %d'
          % (len(xs), xs[0], xs[-1], D[xs[0]].size), flush=True)
    C = D[xs[0]].size
    rng = np.random.default_rng(3)
    cols = sorted(set(int(x) for x in rng.integers(0, C, size=ncol)))
    degrees(D, p, cols, d if d else None)
