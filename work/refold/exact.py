"""P1e-refold: EXACT rational construction + verification of a candidate w-tilde.

Builds the design matrix over Q (not mod q) for a chosen list of folded monomials,
solves  Phat_n = sum_{k,l} T(n,k,l) w(n,k,l)  exactly, and validates on HELD-OUT n.
"""
import sys, os
from fractions import Fraction as F
from math import comb

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import T, Hs, Ph, Q, w3hat                       # noqa


def letter_val(lt, n, k, l):
    t, r = lt[0], int(lt[1])
    if lt.endswith('(k)'):
        x = k
    elif lt.endswith('(l)'):
        x = l
    else:
        x = None
    if t == 'A':
        return Hs(n + x, r) - Hs(x, r)
    if t == 'B':
        return Hs(n - x, r) - Hs(x, r)
    if t == 'C':
        return Hs(n + k + l, r) - Hs(k + l, r)
    if t == 'N':
        return Hs(n, r)
    raise ValueError(lt)


def mono_val(mu, n, k, l):
    v = F(1)
    for lt in mu:
        v *= letter_val(lt, n, k, l)
    return v


def sums(monos, ns):
    """{n: [sum_{k,l} T * mu  for mu in monos]}  exactly over Q"""
    out = {}
    for n in ns:
        acc = [F(0)] * len(monos)
        for k in range(n + 1):
            for l in range(n + 1):
                t = T(n, k, l)
                for i, mu in enumerate(monos):
                    acc[i] += t * mono_val(mu, n, k, l)
        out[n] = acc
    return out


def rref_Q(rows):
    """rows: list of lists of Fractions (augmented). Returns (rank, pivots, R)."""
    R = [r[:] for r in rows]
    m, ncol = len(R), len(R[0])
    piv, r = [], 0
    for c in range(ncol - 1):
        p = None
        for i in range(r, m):
            if R[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        R[r], R[p] = R[p], R[r]
        inv = F(1) / R[r][c]
        R[r] = [x * inv for x in R[r]]
        for i in range(m):
            if i != r and R[i][c] != 0:
                f = R[i][c]
                R[i] = [a - f * bb for a, bb in zip(R[i], R[r])]
        piv.append(c)
        r += 1
        if r == m:
            break
    inconsistent = any(all(x == 0 for x in R[i][:-1]) and R[i][-1] != 0 for i in range(m))
    return r, piv, R, inconsistent


def solve_exact(monos, ns_fit, ns_check, target=Ph, verbose=True):
    S = sums(monos, sorted(set(ns_fit) | set(ns_check)))
    rows = [[S[n][i] for i in range(len(monos))] + [target(n)] for n in ns_fit]
    r, piv, R, inc = rref_Q(rows)
    if verbose:
        print('  exact fit: %d rows, %d cols, rank %d, inconsistent=%s'
              % (len(rows), len(monos), r, inc), flush=True)
    if inc:
        return None, None
    x = [F(0)] * len(monos)
    for i, c in enumerate(piv):
        x[c] = R[i][-1]
    free = [c for c in range(len(monos)) if c not in set(piv)]
    bad = []
    for n in ns_check:
        v = sum(x[i] * S[n][i] for i in range(len(monos)))
        if v != target(n):
            bad.append(n)
    if verbose:
        print('  HELD-OUT check on n=%s : %s'
              % (list(ns_check), 'ALL PASS' if not bad else 'FAIL at %s' % bad), flush=True)
    return x, free
