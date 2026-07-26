"""Verification of the JOINT one-variable WZ certificate for the last (B-bot)
obligation.

Certificate:  u(n,j) = Nu(j) / [(j+1)(n+j+1)(n+j+2)(n+j+3)]   (family V1)
              G(n,j) = Phi(n,0,j) u(n,j)

Claims, each checked here and never assumed:
 (C1) g(j) u(j+1) - u(j) = R(n,j)  at FRESH j never used in the fit
 (C2) u(n,0) = 0                          -> G(n,0) = 0
 (C3) Du(n, n+4) != 0                     -> u regular at the top endpoint
 (C4) Phi(n,0,n+4) = 0                    -> G(n,n+4) = 0
 (C5) Du(n,j) != 0 for 0 <= j <= n+4      -> no interior pole
 (C6) cellwise  Delta_j G = Phi(n,0,j) R(n,j)  for every j in 0..n+3
 (C7) the telescoped total  Sum_{j=0}^{n+3} Phi(n,0,j) R(n,j) = 0
"""
import sys
from math import comb

import numpy as np

import bwz


def minimal_degree(sol, D, dmax=40):
    lo = None
    for deg in range(0, dmax + 1):
        ok, X, shp = bwz.gosper_joint(sol, D, deg)
        if ok:
            lo = (deg, X, shp)
            break
    return lo


def verify(n, p, Dname='V1', dmax=40, nfresh=60, verbose=True):
    D = bwz.DENS[Dname]
    sol = bwz.solve_x0(n, p, verbose=False)
    if sol is None:
        print('  n=%d p=%d : 16-class system INCONSISTENT' % (n, p))
        return None
    bs = bwz.boundary_sum(sol)
    got = minimal_degree(sol, D, dmax)
    if got is None:
        print('  n=%2d p=%d : NO certificate in %s up to deg %d'
              % (n, p, Dname, dmax))
        return None
    deg, X, shp = got
    # ---- (C1) fresh points, disjoint from the fit's random sample
    rng = np.random.default_rng(999331 + 17 * n + p % 101)
    fresh, guard = [], 0
    while len(fresh) < nfresh and guard < 200000:
        guard += 1
        x = int(rng.integers(p // 3, p - 5))
        if (x + 1) % p == 0 or (n + 3 - x) % p == 0:
            continue
        if not bwz.dv(D, n, x, p) or not bwz.dv(D, n, x + 1, p):
            continue
        fresh.append(x)
    bad1 = 0
    for x in fresh:
        gq = bwz.gratio_Q(n, x)
        gp = gq.numerator % p * pow(gq.denominator % p, p - 2, p) % p
        lhs = (gp * bwz.eval_u(X, D, n, x + 1, p) - bwz.eval_u(X, D, n, x, p)) % p
        if (lhs - bwz.Rfun(sol, x)) % p:
            bad1 += 1
    # ---- (C2)..(C5)
    u0 = bwz.eval_u(X, D, n, 0, p)
    Dtop = bwz.dv(D, n, n + 4, p)
    phitop = bwz.Phi_p(n, 0, n + 4, p)
    Dint = [j for j in range(0, n + 5) if bwz.dv(D, n, j, p) == 0]
    # ---- (C6) cellwise telescoping on the ACTUAL range
    bad6 = 0
    for j in range(0, n + 4):
        G1 = bwz.Phi_p(n, 0, j + 1, p) * bwz.eval_u(X, D, n, j + 1, p) % p
        G0 = bwz.Phi_p(n, 0, j, p) * bwz.eval_u(X, D, n, j, p) % p
        if ((G1 - G0) - bwz.Phi_p(n, 0, j, p) * bwz.Rfun(sol, j)) % p:
            bad6 += 1
    # ---- (C7)
    tot = 0
    for j in range(0, n + 4):
        tot = (tot + bwz.Phi_p(n, 0, j, p) * bwz.Rfun(sol, j)) % p
    Gtop = bwz.Phi_p(n, 0, n + 4, p) * bwz.eval_u(X, D, n, n + 4, p) % p
    Gbot = bwz.Phi_p(n, 0, 0, p) * u0 % p
    ok = (bad1 == 0 and u0 == 0 and Dtop != 0 and phitop == 0 and not Dint
          and bad6 == 0 and tot == 0 and Gtop == 0 and Gbot == 0)
    if verbose:
        print('  n=%2d p=%d  deg(Nu)=%2d  rows=%d/%d ratio=%.1f | '
              'C1 fresh %d/%d bad | C2 u(0)=%d | C3 Du(n+4)=%s | C4 Phi_top=%d | '
              'C5 interior poles %d | C6 %d bad | C7 sum=%d G_top=%d G_bot=%d -> %s'
              % (n, p, deg, shp[0], shp[1], shp[0] / shp[1], bad1, nfresh, u0,
                 'nonzero' if Dtop else 'ZERO', phitop, len(Dint), bad6, tot,
                 Gtop, Gbot, 'PASS' if ok else 'FAIL'), flush=True)
    return dict(n=n, p=p, deg=deg, X=X, ok=ok, bs=bs, shape=shp)


if __name__ == '__main__':
    ns = [int(x) for x in (sys.argv[1].split(',') if len(sys.argv) > 1
                           else ['9'])]
    Dname = sys.argv[2] if len(sys.argv) > 2 else 'V1'
    print('JOINT (B-bot) WZ certificate, family %s = %s'
          % (Dname, bwz.DNAME[Dname]))
    res = []
    for n in ns:
        for p in (bwz.P1, bwz.P2):
            res.append(verify(n, p, Dname))
    good = [r for r in res if r and r['ok']]
    print('%d/%d (n,p) pairs fully verified' % (len(good), len(res)))
    if good:
        print('minimal numerator degrees:',
              sorted({(r['n'], r['deg']) for r in good}))
