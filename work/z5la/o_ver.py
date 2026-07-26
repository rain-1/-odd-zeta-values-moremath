"""Find the a-direction at order m, solve EVERY residual block for it, and then
verify the complete certificate on FRESH sample points that were not used in any
fit.  The verification recomputes all J block residuals from scratch."""
import sys, time
import numpy as np
import zla, solve, fastlin, ratrec, ordm, o_scan
from solve import Ansatz, dval


def solve_all(which, n, m, dname, slack, p, nfit=None, nchk=400, avec=None,
              verbose=True):
    D = o_scan.dens(m)[dname]
    dk0 = sum(mu * abs(f[2]) for f, mu in D)
    dl0 = sum(mu * abs(f[3]) for f, mu in D)
    dk, dl = dk0 + slack, dl0 + slack
    ans = Ansatz(D, D, dk, dl, dk, dl, force_k=0, force_l=0)
    na = m - 2
    if nfit is None: nfit = int(1.35 * (ans.nc + na)) + 20
    npts = nfit + nchk
    pd = ordm.PDm(which, p, n, m, npts)
    Acol = ordm.acols(pd)
    J, F = pd.J, pd.F
    stand = [j for j in pd.free if len(pd.B[j]) > 0]
    zero = [j for j in pd.free if len(pd.B[j]) == 0]
    Mfull = o_scan.scal_mat(pd, ans)                 # npts x nc
    Mfit = Mfull[:nfit]

    # ---- 1. the a-direction, from the standalone blocks only ----
    if avec is None:
        As = [Acol[i * npts:i * npts + nfit] for i in stand]
        subs, rank = o_scan.asubspaces(Mfit, As, p)
        inter = o_scan.intersect(subs, na, p)
        if verbose:
            print('  a-subspace dims %s -> common %d'
                  % ([len(x) for x in subs], len(inter)), flush=True)
        if len(inter) != 1: return None
        avec = np.array(inter[0], dtype=np.int64) % p
    avec = np.asarray(avec, dtype=np.int64) % p

    # ---- 2. solve every free block ----
    rv0 = {}; rv1 = {}; sv0 = {}; sv1 = {}     # per block j, arrays over ALL points
    coef = {}
    for j in pd.supp:                          # Theorem R, closed form
        wj = pd.supp[j]
        rv0[j] = (wj * (pd.r0 @ avec.astype(object) % p)) % p
        rv1[j] = (wj * (pd.r1 @ avec.astype(object) % p)) % p
        sv0[j] = (wj * (pd.s0 @ avec.astype(object) % p)) % p
        sv1[j] = (wj * (pd.s1 @ avec.astype(object) % p)) % p
    nbads = {}
    for j in stand:
        rhs = (-(Acol[j * npts:(j + 1) * npts].astype(object) @ avec.astype(object))) % p
        X, rank, piv, nbad = fastlin.solve(Mfit, rhs[:nfit].astype(np.int64), p, nb=64)
        coef[j] = X; nbads[str(pd.B[j])] = nbad
        rv0[j], rv1[j], sv0[j], sv1[j] = _evalblock(ans, X, pd, p)
    for j in zero:                             # the () block: RHS now fully known
        acc = (-(Acol[j * npts:(j + 1) * npts].astype(object) @ avec.astype(object))) % p
        acc = np.array(acc, dtype=object)
        for jj in stand:
            for t in range(npts):
                a = int(pd.Sk[t, j, jj]); b = int(pd.Sl[t, j, jj])
                if a: acc[t] = (acc[t] - int(pd.gk[t]) * a % p * int(rv1[jj][t])) % p
                if b: acc[t] = (acc[t] - int(pd.gl[t]) * b % p * int(sv1[jj][t])) % p
        rhs = np.array([int(x) % p for x in acc], dtype=np.int64)
        X, rank, piv, nbad = fastlin.solve(Mfit, rhs[:nfit], p, nb=64)
        coef[j] = X; nbads[str(pd.B[j])] = nbad
        rv0[j], rv1[j], sv0[j], sv1[j] = _evalblock(ans, X, pd, p)
    if verbose:
        print('  per-block fit residuals (nbad over %d fit rows): %s'
              % (nfit, nbads), flush=True)

    # ---- 3. INDEPENDENT verification on the fresh check points ----
    res = {}
    for i in range(J):
        bad = 0
        for t in range(nfit, npts):
            gk = int(pd.gk[t]); gl = int(pd.gl[t])
            tot = 0
            for j in range(J):
                a = int(pd.Sk[t, i, j]); b = int(pd.Sl[t, i, j])
                if a: tot = (tot + gk * a % p * int(rv1[j][t])) % p
                if b: tot = (tot + gl * b % p * int(sv1[j][t])) % p
            tot = (tot - int(rv0[i][t]) - int(sv0[i][t])) % p
            tgt = 0
            for tt in range(na):
                tgt = (tgt + int(avec[tt]) * int(pd.V[t, i, tt])) % p
            if (tot - tgt) % p: bad += 1
        res[str(pd.B[i])] = bad
    return dict(a=avec, coef=coef, ans=ans, pd=pd, nbads=nbads, check=res,
                nchk=npts - nfit)


def _evalblock(ans, X, pd, p):
    n = pd.n
    r0 = np.array([ans.eval_r(X, n, k, l, p) for (k, l) in pd.pts], dtype=np.int64)
    r1 = np.array([ans.eval_r(X, n, k + 1, l, p) for (k, l) in pd.pts], dtype=np.int64)
    s0 = np.array([ans.eval_s(X, n, k, l, p) for (k, l) in pd.pts], dtype=np.int64)
    s1 = np.array([ans.eval_s(X, n, k, l + 1, p) for (k, l) in pd.pts], dtype=np.int64)
    return r0, r1, s0, s1


if __name__ == '__main__':
    which = sys.argv[1]; n = int(sys.argv[2]); m = int(sys.argv[3])
    dname = sys.argv[4]; slack = int(sys.argv[5])
    p = int(sys.argv[6]) if len(sys.argv) > 6 else o_scan.P
    t0 = time.time()
    out = solve_all(which, n, m, dname, slack, p)
    if out is None:
        print('no unique a-direction'); sys.exit()
    print('  a (normalised) =', [int(x) for x in out['a']])
    tot = sum(out['check'].values())
    print('  FRESH-POINT verification over %d points x %d blocks : %d violations  %s'
          % (out['nchk'], len(out['check']), tot, 'ALL ZERO' if tot == 0 else out['check']))
    print('  [%.0fs]' % (time.time() - t0))
