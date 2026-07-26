"""Full certificate solve for a GIVEN weight vector w over the bare span:
   * the maximal (weight-3) blocks in closed form by Theorem R,
   * the 18 letter blocks by the scalar ansatz,
   * the () block last (it is the only coupling block),
then an INDEPENDENT verification of ALL J residual components at FRESH points.
"""
import sys, time
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import zla, solve, fastlin, ratrec, ordm, qrow
from solve import Ansatz, dval
import bare, frw


def evalmats(pd, ans):
    """R1,R0,S1,S0 :  npts x nr / npts x ns design matrices so that
       r(k+1,l) = R1 @ x_r ,  r(k,l) = R0 @ x_r ,  s(k,l+1) = S1 @ x_s , ..."""
    p, n, npts = pd.p, pd.n, pd.npts
    nr, ns = len(ans.mons_r), len(ans.mons_s)
    R1 = np.zeros((npts, nr), dtype=np.int64); R0 = np.zeros((npts, nr), dtype=np.int64)
    S1 = np.zeros((npts, ns), dtype=np.int64); S0 = np.zeros((npts, ns), dtype=np.int64)
    dmax = max(max(a, b) for a, b in ans.mons_r + ans.mons_s) + 2
    for t, (k, l) in enumerate(pd.pts):
        iDr = pow(dval(ans.Dr, n, k, l, p), p - 2, p)
        iDrk = pow(dval(ans.Dr, n, k + 1, l, p), p - 2, p)
        iDs = pow(dval(ans.Ds, n, k, l, p), p - 2, p)
        iDsl = pow(dval(ans.Ds, n, k, l + 1, p), p - 2, p)
        kp = [pow(k % p, a, p) for a in range(dmax)]
        lp = [pow(l % p, b, p) for b in range(dmax)]
        k1 = [pow((k + 1) % p, a, p) for a in range(dmax)]
        l1 = [pow((l + 1) % p, b, p) for b in range(dmax)]
        for u, (a, b) in enumerate(ans.mons_r):
            R1[t, u] = k1[a] * lp[b] % p * iDrk % p
            R0[t, u] = kp[a] * lp[b] % p * iDr % p
        for u, (a, b) in enumerate(ans.mons_s):
            S1[t, u] = kp[a] * l1[b] % p * iDsl % p
            S0[t, u] = kp[a] * lp[b] % p * iDs % p
    return R1, R0, S1, S0


def mv(M, x, p):
    """(M @ x) mod p, exactly, via float64 blocking"""
    x = np.asarray(x, dtype=np.int64) % p
    out = np.zeros(M.shape[0], dtype=np.int64)
    blk = 400
    for i in range(0, M.shape[1], blk):
        out = (out + (M[:, i:i + blk].astype(np.float64)
                      @ x[i:i + blk].astype(np.float64)).astype(np.int64)) % p
    return out


def qcof(pd, at_k1=False, at_l1=False):
    """Theorem-R cofactor  sum_t a_t r^(t)  at (k,l) / (k+1,l) / (k,l+1)"""
    p, n, m, npts = pd.p, pd.n, pd.m, pd.npts
    rr = np.zeros(npts, dtype=np.int64); ss = np.zeros(npts, dtype=np.int64)
    for t in range(pd.na):
        a = pd.avec[t]
        if a == 0:
            continue
        rf, sf = qrow.make_evals(n + t, p)
        N = n + t
        for tt, (k, l) in enumerate(pd.pts):
            kr, lr = (k + 1, l) if at_k1 else (k, l)
            ks, ls = (k, l + 1) if at_l1 else (k, l)
            fr = ordm.Pm_p(n, kr, lr, t, m, p) * pow(ordm.P03_p(N, kr, lr, p), p - 2, p) % p
            fs = ordm.Pm_p(n, ks, ls, t, m, p) * pow(ordm.P03_p(N, ks, ls, p), p - 2, p) % p
            rr[tt] = (rr[tt] + a * (rf(0, kr, lr) * fr % p)) % p
            ss[tt] = (ss[tt] + a * (sf(0, ks, ls) * fs % p)) % p
    return rr, ss


def divide(mi, mj):
    rest = list(mj)
    for L in mi:
        if L in rest:
            rest.remove(L)
        else:
            return None
    return tuple(sorted(rest))


def Ewphi(pd, w, mi, B):
    """(E_w/Phi)_{mi} at all points"""
    p = pd.p
    out = np.zeros(pd.npts, dtype=np.int64)
    for j, mj in enumerate(B):
        if w[j] == 0:
            continue
        rest = divide(mi, mj)
        if rest is None:
            continue
        ids = [pd.li[x] for x in rest]
        col = np.zeros(pd.npts, dtype=np.int64)
        for t in range(pd.na):
            at = pd.avec[t]
            if at == 0:
                continue
            for u in range(4):
                a = t + u
                pr = pd.PM[:, a].copy()
                for i in ids:
                    pr = pr * pd.incn[:, i, a] % p
                col = (col + at * (pd.cc[t][u] % p) % p * pr) % p
        out = (out + int(w[j]) * col) % p
    return out


def shiftpair(pd, rest):
    p = pd.p
    ids = [pd.li[x] for x in rest]
    sk = np.ones(pd.npts, dtype=np.int64)
    sl = np.ones(pd.npts, dtype=np.int64)
    for i in ids:
        sk = sk * pd.inck[:, i] % p
        sl = sl * pd.incl[:, i] % p
    return sk, sl


def run_cert(n, m, dname, slack, w, B, p=frw.P, npts=None, seed=777,
             avec=None, verbose=True, vnpts=350, vseed=31337):
    J = len(B)
    D = frw.dens(m)[dname]
    dk = sum(mu * abs(f[2]) for f, mu in D) + slack
    dl = sum(mu * abs(f[3]) for f, mu in D) + slack
    ans = Ansatz(D, D, dk, dl, dk, dl, force_k=0, force_l=0)
    if npts is None:
        npts = int(1.4 * ans.nc) + 40
    if avec is None:
        avec = [1] + [0] * (m - 3)
    nr = len(ans.mons_r)
    maximal = set(j for j in range(J) if len(bare.upset(B, B[j])) == 1)
    idx = {mm: j for j, mm in enumerate(B)}
    zero_j = idx[()]
    letters = [j for j in range(J) if len(B[j]) == 1 and j not in maximal]
    # ---- fit phase
    pd = frw.PD(p, n, m, npts, B, avec, seed=seed)
    Msc = frw.scal_mat(pd, ans)
    R1, R0, S1, S0 = evalmats(pd, ans)
    rv = np.zeros((J, npts), dtype=np.int64)
    sv = np.zeros((J, npts), dtype=np.int64)
    for j in maximal:
        rv[j] = int(w[j]) * pd.RQ1 % p
        sv[j] = int(w[j]) * pd.SQ1 % p
    coefs = {}
    fails = {}
    t0 = time.time()
    # the 18 letter blocks are mutually independent -> ONE elimination, 18 RHS
    RHS = np.zeros((npts, len(letters)), dtype=np.int64)
    for c, j in enumerate(letters):
        mi = B[j]
        rhs = Ewphi(pd, w, mi, B)
        for jj in maximal:
            rest = divide(mi, B[jj])
            if rest is None:
                continue
            if not (rv[jj].any() or sv[jj].any()):
                continue
            sk, sl = shiftpair(pd, rest)
            rhs = (rhs - pd.gk * sk % p * rv[jj] - pd.gl * sl % p * sv[jj]) % p
        RHS[:, c] = rhs
    X, rank, piv, _ = fastlin.solve(Msc, RHS, p)
    Mf = np.asarray(Msc, dtype=np.float64) % p
    for c, j in enumerate(letters):
        resid = (mv(Msc, X[:, c], p) - RHS[:, c]) % p
        fails[j] = int(np.count_nonzero(resid))
        coefs[j] = X[:, c]
        rv[j] = mv(R1, X[:nr, c], p)
        sv[j] = mv(S1, X[nr:, c], p)
    # the () block, which couples to everything
    mi = B[zero_j]
    rhs = Ewphi(pd, w, mi, B)
    for jj in range(J):
        if jj == zero_j:
            continue
        rest = divide(mi, B[jj])
        if rest is None:
            continue
        sk, sl = shiftpair(pd, rest)
        rhs = (rhs - pd.gk * sk % p * rv[jj] - pd.gl * sl % p * sv[jj]) % p
    x, rank0, piv0, nbad0 = fastlin.solve(Msc, rhs, p)
    coefs[zero_j] = x
    fails[zero_j] = nbad0
    rv[zero_j] = mv(R1, x[:nr], p)
    sv[zero_j] = mv(S1, x[nr:], p)
    if verbose:
        print('  ansatz %s slack=%d deg=(%d,%d) nc=%d npts=%d  [%.0fs]'
              % (dname, slack, dk, dl, ans.nc, npts, time.time() - t0))
        bad = {str(B[j]): f for j, f in fails.items() if f}
        print('  block residuals (nbad):', bad if bad else
              'ALL %d BLOCKS SOLVED EXACTLY' % (len(letters) + 1))
    # ---- verification phase, fresh points, ALL J components
    pv = frw.PD(p, n, m, vnpts, B, avec, seed=vseed)
    V1, V0, W1, W0 = evalmats(pv, ans)
    rq0, sq0 = qcof(pv)
    Rv1 = np.zeros((J, vnpts), dtype=np.int64); Rv0 = np.zeros((J, vnpts), dtype=np.int64)
    Sv1 = np.zeros((J, vnpts), dtype=np.int64); Sv0 = np.zeros((J, vnpts), dtype=np.int64)
    for j in range(J):
        if j in maximal:
            Rv1[j] = int(w[j]) * pv.RQ1 % p; Rv0[j] = int(w[j]) * rq0 % p
            Sv1[j] = int(w[j]) * pv.SQ1 % p; Sv0[j] = int(w[j]) * sq0 % p
        elif j in coefs:
            x = coefs[j]
            Rv1[j] = mv(V1, x[:nr], p); Rv0[j] = mv(V0, x[:nr], p)
            Sv1[j] = mv(W1, x[nr:], p); Sv0[j] = mv(W0, x[nr:], p)
    badv = {}
    for i in range(J):
        mi = B[i]
        acc = (-Rv0[i] - Sv0[i]) % p
        for j in range(J):
            rest = divide(mi, B[j])
            if rest is None:
                continue
            sk, sl = shiftpair(pv, rest)
            acc = (acc + pv.gk * sk % p * Rv1[j] + pv.gl * sl % p * Sv1[j]) % p
        acc = (acc - Ewphi(pv, w, mi, B)) % p
        nb = int(np.count_nonzero(acc))
        if nb:
            badv[str(mi)] = nb
    if verbose:
        print('  FRESH-POINT verification: %d points x %d components = %d identities -- %s'
              % (vnpts, J, vnpts * J,
                 'ALL ZERO' if not badv else 'FAILURES %s' % badv))
    return dict(ans=ans, coefs=coefs, fails=fails, badv=badv, npts=npts,
                vnpts=vnpts, J=J, pd=pd)
