"""DECISIVE NECESSARY-CONDITION TEST at unlimited inflation depth.

Fix a TOP-degree monomial m0 of w (coefficient c).  In the full joint system,
the equations indexed by the blocks  { mu : mu contains m0 }  form a CLOSED
sub-system: the coefficient of mu only ever involves rho_nu, sigma_nu for
nu ⊇ mu ⊇ m0.  Its right-hand sides are  c  at mu = m0  and  0  at every
mu ⊋ m0  (those have degree > deg w).  No boundary condition touches it (the
bottom boundary is a module-level condition over ALL blocks, so dropping it only
relaxes).  Hence:

    sub-system inconsistent  ==>  NO order-zero certificate exists
                                  in the given ansatz class at that depth.

This is far cheaper than the full joint solve, so the inflation depth Delta can
be pushed to 3 with a generous scalar ansatz.  sigma is NOT tied to tau(rho)
here (m0 need not be tau-symmetric), which also makes the negative stronger.
"""
import itertools
import sys

import numpy as np

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import fastlin

import o0core as C
import joint0 as J
from o0core import Ansatz, dstr


def blocks_above(m0, letters, depth, mk_cap=1):
    out = []
    for d in range(depth + 1):
        for S in itertools.combinations_with_replacement(letters, d):
            m = tuple(sorted(m0 + S))
            if C.mkwt(m) > mk_cap or C.mlwt(m) > mk_cap:
                continue
            out.append(m)
    out.sort(key=lambda m: (-len(m), m))
    return out


def run(n, m0, c, letters, depth, D, deg, npts, p=J.P1, seed=11, mk_cap=1,
        label='', verbose=True):
    Bm = blocks_above(m0, letters, depth, mk_cap)
    Jn = len(Bm)
    ans = Ansatz(D, deg, deg, force_k=0)
    nc = ans.nc
    pts = J.sample_points(n, p, npts, seed)
    dmax = max(max(a, b) for a, b in ans.mons) + 2
    rows = Jn * npts
    cols = 2 * Jn * nc
    M = np.zeros((rows, cols))
    rhs = np.zeros(rows)
    i0 = Bm.index(tuple(sorted(m0)))

    def vec(x, y):
        iD = pow(C.dval(D, n, x, y, p), p - 2, p)
        xp = [pow(x % p, a, p) for a in range(dmax)]
        yp = [pow(y % p, a, p) for a in range(dmax)]
        return np.array([xp[a] * yp[b] % p * iD % p for a, b in ans.mons],
                        dtype=np.float64)

    for t, (k, l) in enumerate(pts):
        gk = C.gk_val(n, k, l, p)
        gl = C.gl_val(n, k, l, p)
        Sk = C.shift_cols(Bm, C.KINC, n, k, l, p)
        Sl = C.shift_cols(Bm, C.LINC, n, k, l, p)
        vr1, vr0 = vec(k + 1, l), vec(k, l)
        vs1, vs0 = vec(k, l + 1), vec(k, l)
        for i in range(Jn):
            r = i * npts + t
            for j in np.nonzero(Sk[i])[0]:
                cc = gk * int(Sk[i, j]) % p
                if cc:
                    M[r, j * nc:(j + 1) * nc] = (M[r, j * nc:(j + 1) * nc]
                                                 + cc * vr1) % p
            for j in np.nonzero(Sl[i])[0]:
                cc = gl * int(Sl[i, j]) % p
                if cc:
                    o = Jn * nc + j * nc
                    M[r, o:o + nc] = (M[r, o:o + nc] + cc * vs1) % p
            M[r, i * nc:(i + 1) * nc] = (M[r, i * nc:(i + 1) * nc] - vr0) % p
            o = Jn * nc + i * nc
            M[r, o:o + nc] = (M[r, o:o + nc] - vs0) % p
            rhs[r] = (c % p) if i == i0 else 0
    X, rank, piv, nbad = fastlin.solve(M.astype(np.int64), rhs.astype(np.int64), p)
    if verbose:
        print('  %-26s n=%d depth=%d blocks=%d nc=%d cols=%d rows=%d '
              'ratio=%.2f rank=%d null=%d resid=%d -> %s'
              % (label, n, depth, Jn, nc, cols, rows, rows / cols, rank,
                 cols - rank, nbad, 'REACHABLE' if nbad == 0 else 'NOT reachable'),
              flush=True)
    return nbad == 0


W1 = [C.lname(1, a) for a in ('k', 'l', 'pk', 'pl', 'mk', 'ml', 'kl', 'pkl')]
W12 = W1 + [C.lname(2, a) for a in ('k', 'l', 'pk', 'pl', 'mk', 'ml', 'kl', 'pkl')]

FAM = {
    'G1': [(C.K1, 3), (C.L1, 3), (C.KL[1], 2), (C.KL[2], 1)],
    'G2': [(C.K1, 3), (C.L1, 3), (C.KL[1], 2), (C.KL[2], 1),
           (C.NK[1], 2), (C.NL[1], 2), (C.NKL[1], 1)],
    'G3': [(C.K1, 4), (C.K2, 2), (C.L1, 4), (C.L2, 2), (C.KL[1], 3),
           (C.KL[2], 2), (C.KL[3], 1), (C.NK[1], 2), (C.NK[2], 1),
           (C.NL[1], 2), (C.NL[2], 1), (C.NKL[1], 2), (C.MK[1], 2),
           (C.ML[1], 2)],
}

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    print('DECISIVE TEST -- top block of the CALIBRATION w = L_k+L_l')
    print('  m0 = (h1_pk,), c = -1 ; alphabet = the 8 weight-1 letters')
    for fam in ('G1', 'G2', 'G3'):
        for depth, deg in ((1, 8), (2, 6), (2, 8), (3, 4), (3, 5)):
            nc = (deg + 1) ** 2
            npts = int(2.8 * nc) + 20
            try:
                run(n, ('h1_pk',), -1, W1, depth, FAM[fam], deg, npts,
                    label='%s/depth%d/deg%d' % (fam, depth, deg))
            except MemoryError:
                print('  %s/depth%d/deg%d MEMORY' % (fam, depth, deg), flush=True)
