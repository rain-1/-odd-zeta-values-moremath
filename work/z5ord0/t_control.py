"""POSITIVE CONTROL for the joint solver plumbing.

Pick a random rho* inside the ansatz, set sigma* = tau(rho*), compute the
right-hand side b = Op(rho*, sigma*) numerically at the sample points, and feed
it to the solver.  Residual must be 0.  This tests the shift matrices, the
tau-pairing, gk/gl and the block layout -- everything except the mathematics.

Also measures the KERNEL (trivial-pair gauge) dimension of the scalar operator
for a given denominator, which is what makes degree inflation do anything at
all:  kernel elements are  rho0 = gl v(k,l+1)-v(k,l),  sigma0 = -(gk v(k+1,l)
-v(k,l)),  whose denominators carry (l+1)^3 resp. (k+1)^3 -- so a denominator
without those cubes has NO gauge and inflation is a no-op.
"""
import sys

import numpy as np

import joint0 as J
import o0core as C
import weights as W

P = J.P1


def scalar_kernel(n, D, deg, npts, p=P, seed=3):
    """nullity of  gk r(k+1,l)-r(k,l)+gl s(k,l+1)-s(k,l)  with s = tau(r)."""
    sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
    import fastlin
    ans = C.Ansatz(D, deg, deg, force_k=0)
    pts = J.sample_points(n, p, npts, seed)
    M = np.zeros((npts, ans.nc))
    dmax = max(max(a, b) for a, b in ans.mons) + 2

    def vec(x, y):
        iD = pow(C.dval(D, n, x, y, p), p - 2, p)
        xp = [pow(x % p, a, p) for a in range(dmax)]
        yp = [pow(y % p, a, p) for a in range(dmax)]
        return np.array([xp[a] * yp[b] % p * iD % p for a, b in ans.mons])
    for t, (k, l) in enumerate(pts):
        gk = C.gk_val(n, k, l, p)
        gl = C.gl_val(n, k, l, p)
        M[t] = (gk * vec(k + 1, l) - vec(k, l)
                + gl * vec(l + 1, k) - vec(l, k)) % p
    rank, _ = fastlin.rank_only(M.astype(np.int64), p)
    return ans.nc, rank, ans.nc - rank


def control(n, w, D, deg, maxdeg, npts, p=P, seed=5, bnd=False):
    B = J.build_basis(w, maxdeg)
    ans = C.Ansatz(D, deg, deg, force_k=0)
    S = J.System(w, n, p, B, ans, npts, seed, bnd=bnd, nbnd=0)
    rng = np.random.default_rng(99)
    Xstar = rng.integers(0, p, size=len(B) * ans.nc).astype(np.int64)
    S.dmax = max(max(a, b) for a, b in ans.mons) + 2
    tgt = {}
    for t, (k, l) in enumerate(S.pts):
        tgt[t] = S.op_values(Xstar, k, l)
    S.build(rhs_fn=lambda i, t: tgt[t][i])
    X, rank, nbad = S.solve()
    print('  CONTROL n=%d J=%d nc=%d cols=%d rows=%d rank=%d resid=%d -> %s'
          % (n, len(B), ans.nc, S.M.shape[1], S.M.shape[0], rank, nbad,
             'PLUMBING OK' if nbad == 0 else 'PLUMBING BROKEN'), flush=True)
    return nbad == 0


if __name__ == '__main__':
    n = 7
    w = W.w_cal()
    print('kernel (trivial-pair gauge) dimension of the scalar operator:')
    for lab, D in [
            ('(k+1)(l+1)(k+l+1)', [(C.K1, 1), (C.L1, 1), (C.KL[1], 1)]),
            ('(k+1)^2(l+1)^2(k+l+1)', [(C.K1, 2), (C.L1, 2), (C.KL[1], 1)]),
            ('(k+1)^3(l+1)^3(k+l+1)', [(C.K1, 3), (C.L1, 3), (C.KL[1], 1)]),
            ('(k+1)^3(l+1)^3(k+l+1)^2', [(C.K1, 3), (C.L1, 3), (C.KL[1], 2)]),
            ('(k+1)^3(l+1)^3(k+l+1)(k+l+2)',
             [(C.K1, 3), (C.L1, 3), (C.KL[1], 1), (C.KL[2], 1)]),
    ]:
        for deg in (4, 6, 8):
            nc, rank, null = scalar_kernel(n, D, deg, int(1.5 * deg * (deg + 2)) + 40)
            print('   %-32s deg=%d nc=%d rank=%d nullity=%d'
                  % (lab, deg, nc, rank, null), flush=True)
    print('plumbing control:')
    control(n, w, [(C.K1, 3), (C.L1, 3), (C.KL[1], 1)], 5, 2, 200)
