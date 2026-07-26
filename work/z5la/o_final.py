"""THE ORDER-7 CERTIFICATE, end to end.

  L_min = A . L_BZ ,   A = sum_{t=0}^{4} a_t(n) S_n^t          (order 7)

  * the 7 supp(w) blocks   : closed form, r_j = w_j sum_t a_t r^(t)   [Theorem R]
  * the 7 standalone blocks: ansatz E1
  * the () block           : ansatz Z3 (its measured denominator)

Verification is INDEPENDENT of the fit: every one of the J block identities is
recomputed from scratch at sample points that no solve ever saw, and the two
(B-bot) boundary obligations are checked as well.
"""
import sys, time
import numpy as np
import zla, solve, fastlin, ratrec, ordm, o_scan, o_zero
from solve import Ansatz, dval


def build(which, n, m, dname, slack, dname0, slack0, p, force=(1, 1),
          avec=None, nchk=350, verbose=True):
    t0 = time.time()
    D = o_scan.dens(m)[dname]
    dk = sum(mu * abs(f[2]) for f, mu in D) + slack
    dl = sum(mu * abs(f[3]) for f, mu in D) + slack
    ans = Ansatz(D, D, dk, dl, dk, dl, force_k=force[0], force_l=force[1])
    D0 = o_scan.dens(m)[dname0]
    ek = sum(mu * abs(f[2]) for f, mu in D0) + slack0
    el = sum(mu * abs(f[3]) for f, mu in D0) + slack0
    ans0 = Ansatz(D0, D0, ek, el, ek, el, force_k=force[0], force_l=force[1])
    na = m - 2
    nfit = int(1.35 * (ans.nc + na)) + 20
    nfit0 = int(1.35 * ans0.nc) + 20
    npts = max(nfit, nfit0) + nchk
    pd = ordm.PDm(which, p, n, m, npts)
    Acol = ordm.acols(pd)
    J = pd.J
    stand = [j for j in pd.free if len(pd.B[j]) > 0]
    zj = [j for j in pd.free if len(pd.B[j]) == 0][0]
    R0, R1, S0, S1, M = o_zero.design(pd, ans)
    if avec is None:
        As = [Acol[i * npts:i * npts + nfit] for i in stand]
        subs, rk = o_scan.asubspaces(M[:nfit].astype(np.int64), As, p)
        inter = o_scan.intersect(subs, na, p)
        if len(inter) != 1:
            if verbose: print('  a-direction dim %d -- abort' % len(inter))
            return None
        avec = np.array(inter[0], dtype=np.int64) % p
    avec = np.asarray(avec, dtype=np.int64) % p
    # --- the seven standalone blocks ---
    rhsS = np.zeros((npts, len(stand)), dtype=np.int64)
    for u, j in enumerate(stand):
        rhsS[:, u] = [int(x) for x in
                      (-(Acol[j * npts:(j + 1) * npts].astype(object)
                         @ avec.astype(object))) % p]
    X, rk1, piv, nb1 = fastlin.solve(M[:nfit].astype(np.int64), rhsS[:nfit], p, nb=64)
    # --- cofactor values for every block at every point ---
    rv0 = {}; rv1 = {}; sv0 = {}; sv1 = {}
    for j in pd.supp:
        wj = pd.supp[j]
        for tgt, src in ((rv0, pd.r0), (rv1, pd.r1), (sv0, pd.s0), (sv1, pd.s1)):
            tgt[j] = np.array([int(x) for x in
                               (wj * (src.astype(object) @ avec.astype(object))) % p],
                              dtype=np.int64)
    for u, j in enumerate(stand):
        rv0[j] = o_zero.matmul_mod(R0, X[:, u:u + 1], p)[:, 0].astype(np.int64)
        rv1[j] = o_zero.matmul_mod(R1, X[:, u:u + 1], p)[:, 0].astype(np.int64)
        sv0[j] = o_zero.matmul_mod(S0, X[:, u:u + 1], p)[:, 0].astype(np.int64)
        sv1[j] = o_zero.matmul_mod(S1, X[:, u:u + 1], p)[:, 0].astype(np.int64)
    # --- the () block ---
    R0z, R1z, S0z, S1z, Mz = o_zero.design(pd, ans0)
    gkf = pd.gk.astype(np.float64); glf = pd.gl.astype(np.float64)
    rhs = np.array([int(x) for x in
                    (-(Acol[zj * npts:(zj + 1) * npts].astype(object)
                       @ avec.astype(object))) % p], dtype=np.float64)
    for j in stand:
        ck = pd.Sk[:, zj, j].astype(np.float64); cl = pd.Sl[:, zj, j].astype(np.float64)
        rhs = (rhs - ((gkf * ck) % p) * rv1[j].astype(np.float64)
               - ((glf * cl) % p) * sv1[j].astype(np.float64)) % p
    Xz, rk2, pz, nb2 = fastlin.solve(Mz[:nfit0].astype(np.int64),
                                     rhs[:nfit0].astype(np.int64), p, nb=64)
    rv0[zj] = o_zero.matmul_mod(R0z, Xz.reshape(-1, 1).astype(np.float64), p)[:, 0].astype(np.int64)
    rv1[zj] = o_zero.matmul_mod(R1z, Xz.reshape(-1, 1).astype(np.float64), p)[:, 0].astype(np.int64)
    sv0[zj] = o_zero.matmul_mod(S0z, Xz.reshape(-1, 1).astype(np.float64), p)[:, 0].astype(np.int64)
    sv1[zj] = o_zero.matmul_mod(S1z, Xz.reshape(-1, 1).astype(np.float64), p)[:, 0].astype(np.int64)
    if verbose:
        print('  n=%d p=%d  a=%s' % (n, p, [int(x) for x in avec]), flush=True)
        print('  fits: 7 standalone (nc=%d, %d rows) nbad=%d | () (nc=%d, %d rows) nbad=%d'
              % (ans.nc, nfit, nb1, ans0.nc, nfit0, nb2), flush=True)
    # --- INDEPENDENT verification on points no solve used ---
    lo = max(nfit, nfit0)
    viol = {}
    for i in range(J):
        bad = 0
        for t in range(lo, npts):
            gk = int(pd.gk[t]); gl = int(pd.gl[t]); tot = 0
            for j in range(J):
                a = int(pd.Sk[t, i, j]); b = int(pd.Sl[t, i, j])
                if a: tot = (tot + gk * a % p * int(rv1[j][t])) % p
                if b: tot = (tot + gl * b % p * int(sv1[j][t])) % p
            tot = (tot - int(rv0[i][t]) - int(sv0[i][t])) % p
            tgt = 0
            for tt in range(na):
                tgt = (tgt + int(avec[tt]) * int(pd.V[t, i, tt])) % p
            if (tot - tgt) % p: bad += 1
        viol[str(pd.B[i])] = bad
    nviol = sum(viol.values())
    if verbose:
        print('  INDEPENDENT check, %d fresh points x %d blocks = %d identities: %s'
              % (npts - lo, J, (npts - lo) * J,
                 'ALL SATISFIED' if nviol == 0 else viol), flush=True)
    # --- (B-bot) boundary obligations:  r_j(n,0,l) = 0 and s_j(n,k,0) = 0 ---
    bb = boundary_check(pd, ans, ans0, X, Xz, avec, stand, zj, p)
    if verbose:
        print('  (B-bot) r_j(n,0,l)=0 and s_j(n,k,0)=0 for all %d blocks: %s  [%.0fs]'
              % (J, 'HOLD' if bb == 0 else '%d FAILURES' % bb, time.time() - t0),
              flush=True)
    return dict(a=avec, nviol=nviol, nb1=nb1, nb2=nb2, bbot=bb, X=X, Xz=Xz,
                ans=ans, ans0=ans0, pd=pd, nfresh=npts - lo, J=J)


def boundary_check(pd, ans, ans0, X, Xz, avec, stand, zj, p, ntest=25):
    """R = Phi_m * sum_j r_j M_j must vanish at k = 0, S at l = 0."""
    n, m = pd.n, pd.m
    import qrow
    bad = 0
    rng = np.random.default_rng(5)
    for _ in range(ntest):
        l = int(rng.integers(50, p - 50)); k = int(rng.integers(50, p - 50))
        for u, j in enumerate(stand):
            if ans.eval_r(X[:, u], n, 0, l, p): bad += 1
            if ans.eval_s(X[:, u], n, k, 0, p): bad += 1
        if ans0.eval_r(Xz, n, 0, l, p): bad += 1
        if ans0.eval_s(Xz, n, k, 0, p): bad += 1
        # Theorem-R blocks: r^(t)(n,0,l) and s^(t)(n,k,0)
        for tt in range(pd.na):
            rf, sf = qrow.make_evals(n + tt, p)
            f0 = ordm.Pm_p(n, 0, l, tt, m, p) * pow(ordm.P03_p(n + tt, 0, l, p), p - 2, p) % p
            g0 = ordm.Pm_p(n, k, 0, tt, m, p) * pow(ordm.P03_p(n + tt, k, 0, p), p - 2, p) % p
            if rf(0, 0, l) * f0 % p: bad += 1
            if sf(0, k, 0) * g0 % p: bad += 1
    return bad


if __name__ == '__main__':
    m = 7
    for (n, p) in ((5, o_scan.P), (9, o_scan.P), (5, o_scan.P2), (11, o_scan.P2)):
        print('=== n=%d p=%d ===' % (n, p), flush=True)
        build('w3', n, m, 'E1', 18, 'Z3', 16, p)
