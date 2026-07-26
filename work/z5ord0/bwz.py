"""THE LAST (B-bot) OBLIGATION -- a JOINT one-variable WZ certificate.

Z5STAR_CERT 3.3: with the 16 non-() collapse classes imposed, the whole bottom
boundary reduces to

    Sum_{l=0}^{n+3} Phi(n,0,l) rho_()(n,0,l)
  + Sum_{k=0}^{n+3} Phi(n,k,0) sigma_()(n,k,0)  =  0     [VERIFIED n = 1..13]

KEY OBSERVATION (checked in check_phi_symmetry below): Phi is k<->l SYMMETRIC,
Phi(n,j,0) = Phi(n,0,j).  So the two sums share one hypergeometric factor and
combine into a SINGLE sum

    Sum_{j=0}^{n+3} Phi(n,0,j) R(n,j) = 0 ,
    R(n,j) := rho_()(n,0,j) + sigma_()(n,j,0)          (a rational function of j)

with

    g(j) := Phi(n,0,j+1)/Phi(n,0,j) = (n+3-j)^2 (n+j+1)^2 / (j+1)^4 .

So the obligation is Gosper-summability of ONE term.  Find rational u with

    g(j) u(j+1) - u(j) = R(n,j)                                     (GOS)

and then G(n,j) := Phi(n,0,j) u(n,j) satisfies Delta_j G = Phi(n,0,j) R(n,j).

BOUNDARY.  G(n,0) = Phi(n,0,0) u(n,0) and Phi(n,0,0) = 1/prod_{j=1..3}(n+j)^4
is NONZERO, so u(n,0) = 0 must be imposed.  G(n,n+4) = Phi(n,0,n+4) u(n,n+4)
and Phi(n,0,n+4) = 0 because C(n+3,n+4) = 0 -- free PROVIDED u has no pole at
j = n+4.  Both are checked explicitly, never assumed.

WHY THIS AND NOT gosper.py.  work/z5star/gosper.py runs gosper_side on rho0 and
sigma0 SEPARATELY and both come back negative -- that is Z5STAR_CERT 3.3's
route 1, [EXCLUDED with bounds].  It is their SUM that vanishes, so the
certificate must mix the two halves.  Nobody has run the sum.
"""
import json
import sys
from fractions import Fraction as Fr
from math import comb

import numpy as np

Z5STAR = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'
sys.path.insert(0, Z5STAR)
import wtools as W          # noqa: E402
import gosper as GZ         # noqa: E402
import fastlin              # noqa: E402
from solve import dval      # noqa: E402

P1 = 4194301
P2 = 4194287
WJSON = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'


# ----------------------------------------------------------------- the base --
def Phi_p(n, k, l, p):
    N = n + 3
    T = (comb(N + k, N) * comb(N, k) ** 2 * comb(N + l, N) * comb(N, l) ** 2
         * comb(N + k + l, N))
    d = 1
    for j in (1, 2, 3):
        d *= (n + j) * (n + k + j) * (n + l + j) * (n + k + l + j)
    return T % p * pow(d % p, p - 2, p) % p


def Phi_Q(n, k, l):
    N = n + 3
    T = (comb(N + k, N) * comb(N, k) ** 2 * comb(N + l, N) * comb(N, l) ** 2
         * comb(N + k + l, N))
    d = 1
    for j in (1, 2, 3):
        d *= (n + j) * (n + k + j) * (n + l + j) * (n + k + l + j)
    return Fr(T, d)


def check_phi_symmetry(nmax=12):
    bad = [(n, k, l) for n in range(nmax + 1) for k in range(n + 5)
           for l in range(n + 5) if Phi_Q(n, k, l) != Phi_Q(n, l, k)]
    return not bad


def gratio_Q(n, j):
    return Fr((n + 3 - j) ** 2 * (n + j + 1) ** 2, (j + 1) ** 4)


# --------------------------------------------------- the certificate solve ---
def solve_x0(n, p, dL='M0', sL=8, d0='M0', s0=12, verbose=True):
    """reproduce Z5STAR_CERT 3.3: joint system + the 16 non-() (B-bot) classes."""
    dc = json.load(open(WJSON))
    w = W.to_p([Fr(c) for c in dc['coeffs']], p)
    S = GZ.build_joint(n, w, W.B, dL, sL, d0, s0, p)
    A1, b1 = GZ.class_rows(S, exclude_empty=True)
    L2 = np.concatenate([S['LHS'], A1], axis=0)
    r2 = np.concatenate([S['rhs0'], b1])
    z, rk, piv, nbad = fastlin.solve(L2, r2, p)
    if verbose:
        print('  n=%d p=%d : joint+%d class rows, cols=%d rows=%d rank=%d nbad=%d %s'
              % (n, p, A1.shape[0], L2.shape[1], L2.shape[0], rk, nbad,
                 'CONSISTENT' if nbad == 0 else 'INCONSISTENT'), flush=True)
    if nbad:
        return None
    ans0 = S['ans0']
    return dict(S=S, z=z, x0=z[:ans0.nc], ans0=ans0, LHS=L2, rhs=r2,
                rank=rk, piv=piv, n=n, p=p)


def Rfun(sol, j):
    """R(n,j) = rho_()(n,0,j) + sigma_()(n,j,0)   (mod p)"""
    n, p, ans0, x0 = sol['n'], sol['p'], sol['ans0'], sol['x0']
    return (ans0.eval_r(x0, n, 0, j, p) + ans0.eval_s(x0, n, j, 0, p)) % p


def boundary_sum(sol):
    n, p = sol['n'], sol['p']
    tot = 0
    for j in range(0, n + 4):
        tot = (tot + Phi_p(n, 0, j, p) * Rfun(sol, j)) % p
    return tot


# ------------------------------------------------------ the joint Gosper -----
# u = Nu(j)/Du(n,j),  Du a product of linear forms (c + cn*n + j)^m
DENS = {
    'U0': [],
    'U1': [(1, 0, 1)],                                        # (j+1)
    'U2': [(1, 0, 2)],
    'U3': [(1, 0, 3)],
    'U4': [(1, 0, 4)],
    'V1': [(1, 0, 1), (1, 1, 1), (2, 1, 1), (3, 1, 1)],       # (j+1)(n+j+1)(n+j+2)(n+j+3)
    'V2': [(1, 0, 2), (1, 1, 1), (2, 1, 1), (3, 1, 1)],
    'V3': [(1, 0, 3), (1, 1, 1), (2, 1, 1), (3, 1, 1)],
    'V4': [(1, 0, 4), (1, 1, 2), (2, 1, 2), (3, 1, 2)],
    'W1': [(1, 0, 1), (1, 1, 1), (2, 1, 1), (3, 1, 1), (4, 1, 1)],
    'W2': [(1, 0, 2), (1, 1, 2), (2, 1, 2), (3, 1, 2), (4, 1, 1)],
    'X1': [(1, 0, 1), (1, 1, 1), (2, 1, 1), (3, 1, 1), (0, 1, 1)],
    'X2': [(1, 0, 3), (1, 1, 2), (2, 1, 2), (3, 1, 2), (0, 1, 2), (4, 1, 1)],
}
DNAME = {
    'U0': '1', 'U1': '(j+1)', 'U2': '(j+1)^2', 'U3': '(j+1)^3', 'U4': '(j+1)^4',
    'V1': '(j+1)(n+j+1)(n+j+2)(n+j+3)',
    'V2': '(j+1)^2(n+j+1)(n+j+2)(n+j+3)',
    'V3': '(j+1)^3(n+j+1)(n+j+2)(n+j+3)',
    'V4': '(j+1)^4(n+j+1)^2(n+j+2)^2(n+j+3)^2',
    'W1': '(j+1)(n+j+1)(n+j+2)(n+j+3)(n+j+4)',
    'W2': '(j+1)^2(n+j+1)^2(n+j+2)^2(n+j+3)^2(n+j+4)',
    'X1': '(j+1)(n+j)(n+j+1)(n+j+2)(n+j+3)',
    'X2': '(j+1)^3(n+j)^2(n+j+1)^2(n+j+2)^2(n+j+3)^2(n+j+4)',
}


def dv(D, n, x, p):
    v = 1
    for (c, cn, m) in D:
        v = v * pow((c + cn * n + x) % p, m, p) % p
    return v


def gosper_joint(sol, D, deg, npts=None, force_u0=True, seed=7, verbose=False):
    """solve  g(j) u(j+1) - u(j) = R(n,j)  for u = Nu(j)/Du, deg Nu <= deg.

    force_u0 adds the row u(n,0) = 0 (the bottom boundary term of G)."""
    n, p = sol['n'], sol['p']
    nc = deg + 1
    if npts is None:
        npts = int(1.4 * nc) + 30
    rng = np.random.default_rng(seed + n)
    pts = []
    guard = 0
    while len(pts) < npts:
        guard += 1
        if guard > 200000:
            break
        x = int(rng.integers(1, p - 5))
        if (x + 1) % p == 0 or (n + 3 - x) % p == 0:
            continue
        if not dv(D, n, x, p) or not dv(D, n, x + 1, p):
            continue
        pts.append(x)
    rows, rhs = [], []
    for x in pts:
        gq = gratio_Q(n, x)
        gp = gq.numerator % p * pow(gq.denominator % p, p - 2, p) % p
        iD1 = pow(dv(D, n, x + 1, p), p - 2, p)
        iD0 = pow(dv(D, n, x, p), p - 2, p)
        row = [(gp * pow((x + 1) % p, t, p) % p * iD1
                - pow(x % p, t, p) * iD0) % p for t in range(nc)]
        rows.append(row)
        rhs.append(Rfun(sol, x))
    if force_u0:
        iD0 = pow(dv(D, n, 0, p), p - 2, p)
        rows.append([(pow(0, t, p) * iD0) % p for t in range(nc)])
        rhs.append(0)
    A = np.array(rows, dtype=np.int64) % p
    b = np.array(rhs, dtype=np.int64) % p
    X, rk, piv, nbad = fastlin.solve(A, b, p)
    if verbose:
        print('     D=%-10s deg=%-3d cols=%d rows=%d ratio=%.2f rank=%d nbad=%d'
              % (D and DNAME.get(D, '?') or '1', deg, nc, A.shape[0],
                 A.shape[0] / nc, rk, nbad), flush=True)
    return (nbad == 0), X, A.shape


def eval_u(X, D, n, x, p):
    num = 0
    for t, c in enumerate(X):
        c = int(c) % p
        if c:
            num = (num + c * pow(x % p, t, p)) % p
    return num * pow(dv(D, n, x, p), p - 2, p) % p
