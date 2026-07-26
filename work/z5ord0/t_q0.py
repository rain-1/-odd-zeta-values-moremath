"""TEST A -- the single most important feasibility question.

Does the CONSTANT weight w = 1 admit an order-zero certificate

    1 = gk rho(k+1,l) - rho(k,l) + gl sigma(k,l+1) - sigma(k,l)

with rho, sigma RATIONAL?  Every target weight w has top-degree monomials with
nonzero rational coefficients, and if rho is confined to the divisor-closure of
supp(w) those blocks are exactly this equation.  A NO here means the ansatz must
be inflated above deg(w) (kernel/gauge blocks), a YES makes the cascade direct.

No boundary conditions are imposed (they are a module-level condition on the
whole certificate, not blockwise).
"""
import sys
import numpy as np

import o0core as C
from o0core import Ansatz, dstr

P = 4194301


def points(n, p, npts, seed=1):
    rng = np.random.default_rng(seed)
    pts = []
    guard = 0
    while len(pts) < npts:
        guard += 1
        if guard > 200000:
            raise RuntimeError('no points')
        k = int(rng.integers(3, p - 3)); l = int(rng.integers(3, p - 3))
        bad = False
        for c in [k + 1, k + 2, k + 3, l + 1, l + 2, l + 3]:
            if c % p == 0:
                bad = True
        for j in range(0, 6):
            for c in [k + l + j, n + k + j, n + l + j, n + k + l + j,
                      n + j - k, n + j - l]:
                if c % p == 0:
                    bad = True
        # also at the shifted arguments
        for (kk, ll) in ((k + 1, l), (k, l + 1)):
            for j in range(0, 6):
                for c in [kk + ll + j, n + kk + j, n + ll + j, n + kk + ll + j,
                          n + j - kk, n + j - ll, kk + j, ll + j]:
                    if c % p == 0:
                        bad = True
        if not bad:
            pts.append((k, l))
    return pts


def opmat(pts, n, p, Ar, As):
    """columns: rho coefficients then sigma coefficients."""
    npts = len(pts)
    M = np.zeros((npts, Ar.nc + As.nc), dtype=np.int64)
    dmax = max([a for a, b in Ar.mons + As.mons] +
               [b for a, b in Ar.mons + As.mons]) + 2
    for t, (k, l) in enumerate(pts):
        gk = C.gk_val(n, k, l, p)
        gl = C.gl_val(n, k, l, p)
        iDr = pow(C.dval(Ar.D, n, k, l, p), p - 2, p)
        iDrk = pow(C.dval(Ar.D, n, k + 1, l, p), p - 2, p)
        iDs = pow(C.dval(As.D, n, k, l, p), p - 2, p)
        iDsl = pow(C.dval(As.D, n, k, l + 1, p), p - 2, p)
        kp = [pow(k % p, a, p) for a in range(dmax)]
        lp = [pow(l % p, a, p) for a in range(dmax)]
        k1 = [pow((k + 1) % p, a, p) for a in range(dmax)]
        l1 = [pow((l + 1) % p, a, p) for a in range(dmax)]
        for u, (a, b) in enumerate(Ar.mons):
            M[t, u] = (gk * k1[a] % p * lp[b] % p * iDrk
                       - kp[a] * lp[b] % p * iDr) % p
        for u, (a, b) in enumerate(As.mons):
            M[t, Ar.nc + u] = (gl * kp[a] % p * l1[b] % p * iDsl
                               - kp[a] * lp[b] % p * iDs) % p
    return M


def run(n, D, deg, npts, p=P, seed=1, label=''):
    sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
    import fastlin
    Ar = Ansatz(D, deg, deg, force_k=0)
    Ds = [((cn, cl, ck, c0), m) for (cn, ck, cl, c0), m in D]
    As = Ansatz(Ds, deg, deg, force_k=0)
    pts = points(n, p, npts, seed)
    M = opmat(pts, n, p, Ar, As)
    b = np.ones(npts, dtype=np.int64)
    X, rank, piv, nbad = fastlin.solve(M, b, p)
    r0, _ = fastlin.rank_only(M, p)
    print('  %-22s D=%-46s deg=%d nc=%d rows=%d rank=%d nullity=%d  '
          'residual=%d  -> %s'
          % (label, dstr(D), deg, M.shape[1], npts, r0, M.shape[1] - r0,
             nbad, 'SOLVABLE' if nbad == 0 else 'no'), flush=True)
    return nbad == 0, X, Ar, As, pts


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    print('TEST A: order-zero certificate for the CONSTANT weight, n=%d' % n)
    fams = [
        ('empty', []),
        ('kl1', [(C.KL[1], 1)]),
        ('k1l1', [(C.K1, 1), (C.L1, 1)]),
        ('E1', [(C.K1, 1), (C.L1, 1), (C.KL[1], 1), (C.KL[2], 1),
                (C.NK[1], 1), (C.NL[1], 1)]),
        ('E2', [(C.K1, 2), (C.L1, 2), (C.KL[1], 2), (C.KL[2], 2),
                (C.NK[1], 2), (C.NL[1], 2)]),
        ('E4', [(C.K1, 1), (C.L1, 1), (C.KL[1], 1), (C.KL[2], 1),
                (C.NK[1], 1), (C.NL[1], 1), (C.MK[0], 1), (C.ML[0], 1)]),
        ('E5', [(C.K1, 3), (C.L1, 3), (C.KL[1], 2), (C.KL[2], 1),
                (C.NK[1], 2), (C.NL[1], 2), (C.NKL[1], 1),
                (C.MK[0], 2), (C.ML[0], 2)]),
    ]
    for lab, D in fams:
        for deg in (6, 10):
            npts = 2 * ((deg + 1) ** 2) * 2 + 60
            run(n, D, deg, npts, label=lab)
