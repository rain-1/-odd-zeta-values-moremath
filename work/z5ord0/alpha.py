"""ALPHABET DETERMINATION for the universal kernel coefficients.

The brief's alphabet warning: the contour-native local coefficients use finite
shifted-product and Euler sums and need NOT lie in the bare product span.  This
module measures, exactly, which letters actually occur in

    [zeta(2)] I^(2,2),   [1] I^(1,1), [1] I^(1,2), [1] I^(2,1), [1] I^(2,2).

Candidate letters (functions of k,l only -- the universal kernels do not see n):
  products of H^(r)_x, x in {k, l, k+l};
  univariate Euler sums   S_{r,m}(x) = sum_{t=1}^{x} H^(m)_t / t^r;
  bivariate coupled sums  U_{r,m}(a,b) = sum_{t=1}^{a} H^(m)_{t+b} / t^r.
"""
from fractions import Fraction as Fr
from functools import lru_cache
import itertools


@lru_cache(None)
def H(m, r):
    if m <= 0:
        return Fr(0)
    return H(m - 1, r) + Fr(1, m ** r)


@lru_cache(None)
def S(x, r, m):
    """sum_{t=1}^{x} H^(m)_t / t^r"""
    return sum((H(t, m) / Fr(t ** r) for t in range(1, x + 1)), Fr(0))


@lru_cache(None)
def U(a, b, r, m):
    """sum_{t=1}^{a} H^(m)_{t+b} / t^r"""
    return sum((H(t + b, m) / Fr(t ** r) for t in range(1, a + 1)), Fr(0))


ARGS = ('k', 'l', 'kl')


def argval(a, k, l):
    return {'k': k, 'l': l, 'kl': k + l}[a]


def prod_letters(weight):
    """all monomials in H^(r)_x of total weight `weight`, as (name, fn)."""
    out = []
    parts = []

    def gen(rem, start, cur):
        if rem == 0:
            parts.append(tuple(cur))
            return
        for r in range(1, rem + 1):
            for a in ARGS:
                gen(rem - r, 0, cur + [(r, a)])
    gen(weight, 0, [])
    seen = set()
    for pr in parts:
        key = tuple(sorted(pr))
        if key in seen:
            continue
        seen.add(key)
        name = '*'.join('H%d_%s' % (r, a) for r, a in key)
        fn = (lambda key: (lambda k, l: _pv(key, k, l)))(key)
        out.append((name, fn))
    return out


def _pv(key, k, l):
    v = Fr(1)
    for r, a in key:
        v *= H(argval(a, k, l), r)
    return v


def euler_letters(weight):
    out = []
    for r in range(1, weight):
        m = weight - r
        for a in ARGS:
            out.append(('S%d%d_%s' % (r, m, a),
                        (lambda r, m, a: (lambda k, l: S(argval(a, k, l), r, m)))(r, m, a)))
    return out


def biv_letters(weight):
    out = []
    for r in range(1, weight):
        m = weight - r
        out.append(('U%d%d_kl' % (r, m),
                    (lambda r, m: (lambda k, l: U(k, l, r, m)))(r, m)))
        out.append(('U%d%d_lk' % (r, m),
                    (lambda r, m: (lambda k, l: U(l, k, r, m)))(r, m)))
    return out


def basis(weight, use_euler=True, use_biv=False):
    B = prod_letters(weight)
    if use_euler:
        B += euler_letters(weight)
    if use_biv:
        B += biv_letters(weight)
    return B


# ------------------------------------------------------------------- fitting
def fit(target, B, cells, verbose=True, tag=''):
    """exact Q least-structure fit; returns (ok, coeffs) with free params 0."""
    rows = [[f(k, l) for _, f in B] for (k, l) in cells]
    rhs = [target(k, l) for (k, l) in cells]
    ncol = len(B)
    A = [r[:] + [rhs[i]] for i, r in enumerate(rows)]
    piv = []
    r = 0
    for c in range(ncol):
        pr = None
        for i in range(r, len(A)):
            if A[i][c] != 0:
                pr = i
                break
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        inv = Fr(1) / A[r][c]
        A[r] = [v * inv for v in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c)
        r += 1
        if r == len(A):
            break
    bad = [i for i in range(r, len(A)) if A[i][ncol] != 0]
    coef = [Fr(0)] * ncol
    for t, c in enumerate(piv):
        coef[c] = A[t][ncol]
    if verbose:
        print('  %-16s cells=%d basis=%d rank=%d -> %s'
              % (tag, len(cells), ncol, r,
                 'CONSISTENT' if not bad else 'INCONSISTENT (%d bad rows)' % len(bad)))
        if not bad:
            print('     ' + '  '.join('%s*%s' % (coef[j], B[j][0])
                                      for j in range(ncol) if coef[j] != 0))
    return (not bad), coef
