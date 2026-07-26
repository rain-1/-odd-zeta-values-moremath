"""MEASURE (never guess) the denominators of the standalone-block right-hand
sides at weight 5.

For every structural type of standalone block (h1h1, h1h2, h1h3, h2h2, h4) and
every column of its A-matrix -- i.e. every elementary weight direction e_j with
M_block | M_j -- reconstruct the exact rational function of k (l fixed) and of
l (k fixed) and factor the denominator against the candidate linear forms.
"""
import sys, time
from collections import Counter, defaultdict
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import ratrec
import w5span as W
import pd5


def kroots(n, l, m=pd5.M):
    R = [('k+%d' % j, -j) for j in range(1, m + 5)]
    R += [('k+l+%d' % j, -l - j) for j in range(1, m + 7)]
    R += [('n+k+%d' % j, -n - j) for j in range(0, m + 5)]
    R += [('n+%d-k' % j, n + j) for j in range(0, m + 5)]
    R += [('n+k+l+%d' % j, -n - l - j) for j in range(0, m + 5)]
    return R


def lroots(n, k, m=pd5.M):
    R = [('l+%d' % j, -j) for j in range(1, m + 5)]
    R += [('k+l+%d' % j, -k - j) for j in range(1, m + 7)]
    R += [('n+l+%d' % j, -n - j) for j in range(0, m + 5)]
    R += [('n+%d-l' % j, n + j) for j in range(0, m + 5)]
    R += [('n+k+l+%d' % j, -n - k - j) for j in range(0, m + 5)]
    return R


def measure(n=9, p=pd5.P1, nsamp=260, maxdeg=60, k0=100003, l0=200003,
            which=None, verbose=True, spandeg=3):
    B, T = W.span_w5(None, 5, spandeg)
    maxi, stand, coup, us = W.blocks(B)
    # one representative standalone block per structural type
    types = {}
    for j in stand:
        key = tuple(W.LETTERS[L][0] for L in B[j])
        types.setdefault(key, []).append(j)
    reps = {key: v[0] for key, v in sorted(types.items())}
    if which is not None:
        reps = {k: v for k, v in reps.items() if k == which}
    kden = Counter(); lden = Counter()
    for key, j in reps.items():
        mi = B[j]
        # --- k direction
        pts = [(k0 + t, l0) for t in range(nsamp)]
        pd = pd5.PD5(p, n, 0, B, pts=pts)
        cols = pd5.Acols_standalone(pd, B, [j], us)[0][2]
        upnames = [B[jj] for jj, _ in us[j]]
        xs = [k0 + t for t in range(nsamp)]
        for c in range(cols.shape[1]):
            vals = [int(x) for x in cols[:, c]]
            res = ratrec.null_min_deg(vals, xs, p, maxdeg)
            if res is None:
                print('  %-28s col %-28s  k: NO FIT (deg > %d)'
                      % (str(mi), str(upnames[c]), maxdeg))
                continue
            num, den = res
            mult, rest = ratrec.factor_mult(den, kroots(n, l0), p)
            for f, e in mult.items():
                kden[f] = max(kden[f], e)
            if verbose:
                print('  %-24s <- %-30s k: degN=%-3d degD=%-3d  %s%s'
                      % (str(mi), str(upnames[c]), len(num) - 1, len(den) - 1,
                         dict(sorted(mult.items())),
                         '' if len(rest) <= 1 else '  UNFACTORED deg %d' % (len(rest) - 1)))
        # --- l direction
        pts = [(k0, l0 + t) for t in range(nsamp)]
        pd = pd5.PD5(p, n, 0, B, pts=pts)
        cols = pd5.Acols_standalone(pd, B, [j], us)[0][2]
        xs = [l0 + t for t in range(nsamp)]
        for c in range(cols.shape[1]):
            vals = [int(x) for x in cols[:, c]]
            res = ratrec.null_min_deg(vals, xs, p, maxdeg)
            if res is None:
                print('  %-28s col %-28s  l: NO FIT' % (str(mi), str(upnames[c])))
                continue
            num, den = res
            mult, rest = ratrec.factor_mult(den, lroots(n, k0), p)
            for f, e in mult.items():
                lden[f] = max(lden[f], e)
            if verbose:
                print('  %-24s <- %-30s l: degN=%-3d degD=%-3d  %s%s'
                      % (str(mi), str(upnames[c]), len(num) - 1, len(den) - 1,
                         dict(sorted(mult.items())),
                         '' if len(rest) <= 1 else '  UNFACTORED deg %d' % (len(rest) - 1)))
    print('\n=== union of k-denominators (max multiplicity) ===')
    print(dict(sorted(kden.items())))
    print('=== union of l-denominators (max multiplicity) ===')
    print(dict(sorted(lden.items())))
    return kden, lden


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    sd = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    only = sys.argv[3] if len(sys.argv) > 3 else None
    wk = tuple(int(x) for x in only.split(',')) if only else None
    measure(n=n, spandeg=sd, which=wk)
