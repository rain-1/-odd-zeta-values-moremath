"""Is order 7 minimal for a telescoper of ANY shape (not just a left multiple
of L_BZ)?

{('xk',), ('u2','xk')} is a CLOSED two-block subsystem: (S^d)_{ij} != 0 iff
M_i | M_j, and the only monomials divisible by ('xk',) are itself and
('u2','xk'), whose own equation involves nothing else.  So for a fully free
operator  L = sum_{a=0}^{M} d_a S_n^a  the pair gives a necessary condition on d
at a cost of 2*nc columns instead of J*nc.
"""
import sys, time
import numpy as np
import zla, solve, fastlin, ratrec, ordm, o_scan, o_zero
from solve import Ansatz


def dcols(pd, M):
    """Wd[i*npts+t, a] = ( Pm(n,k,l,a,M) * w(n+a,k,l) )_i   for a = 0..M"""
    p, n, F, J, npts = pd.p, pd.n, pd.F, pd.J, pd.npts
    W = np.zeros((J * npts, M + 1), dtype=np.int64)
    for t, (k, l) in enumerate(pd.pts):
        for a in range(M + 1):
            el = zla.w_shift_mixed(F, pd.w, a, n, k, l, pd.base)
            v = zla.el_to_vec(F, pd.B, zla.el_scale(F, el, ordm.Pm_p(n, k, l, a, M, p)))
            for i in range(J):
                W[i * npts + t, a] = v[i]
    return W


def run(which, n, M, dname, slack, p=o_scan.P, verbose=True):
    D = o_scan.dens(M)[dname]
    dk = sum(mu * abs(f[2]) for f, mu in D) + slack
    dl = sum(mu * abs(f[3]) for f, mu in D) + slack
    ans = Ansatz(D, D, dk, dl, dk, dl, force_k=0, force_l=0)
    nd = M + 1
    npts = int(1.35 * (2 * ans.nc + nd) / 2) + 20
    t0 = time.time()
    pd = ordm.PDm(which, p, n, M, npts)
    B = pd.B
    i = B.index(('xk',)); j = B.index(('u2', 'xk'))
    W = dcols(pd, M)
    R0, R1, S0, S1, Msc = o_zero.design(pd, ans)
    nc = ans.nc
    G = np.zeros((2 * npts, 2 * nc + nd))
    gk = pd.gk.astype(np.float64); gl = pd.gl.astype(np.float64)
    # block j rows  (its own equation)
    G[:npts, nc:2 * nc] = Msc
    G[:npts, 2 * nc:] = (-W[j * npts:(j + 1) * npts]) % p
    # block i rows
    G[npts:, :nc] = Msc
    ck = pd.Sk[:, i, j].astype(np.float64)[:, None]
    cl = pd.Sl[:, i, j].astype(np.float64)[:, None]
    G[npts:, nc:2 * nc] = (((gk[:, None] * ck) % p) * R1
                           + ((gl[:, None] * cl) % p) * S1) % p
    G[npts:, 2 * nc:] = (-W[i * npts:(i + 1) * npts]) % p
    G %= p
    rank, piv = fastlin.elim(G, p, 2 * nc, 64)
    Z = (G[rank:, 2 * nc:].astype(np.int64)) % p
    ns = ratrec.nullspace(Z, p) if Z.shape[0] else []
    if verbose:
        print('%s n=%d order<=%2d %s deg=(%d,%d) nc=%d cols=%d rows=%d ratio=%.2f '
              'rank=%d -> %d telescoper direction(s)%s  [%.0fs]'
              % (which, n, M, dname, dk, dl, nc, 2 * nc + nd, 2 * npts,
                 2 * npts / (2 * nc + nd), rank, len(ns),
                 '  ***' if ns else '', time.time() - t0), flush=True)
    return ns


if __name__ == '__main__':
    which = sys.argv[1]; n = int(sys.argv[2]); dname = sys.argv[3]
    slack = int(sys.argv[4])
    for M in [int(x) for x in sys.argv[5:]]:
        run(which, n, M, dname, slack)
