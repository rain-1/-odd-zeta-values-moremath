"""JOB 2 -- (B-bot) imposed EXACTLY, per block, at the measured minimal ansatz.

(B-bot) is  R_w(n,0,l) = Phi(n,0,l) * sum_j rho_j(n,0,l) M_j(n,0,l) = 0.
A monomial M_j VANISHES at k = 0 whenever it contains a letter H^(r)_k, because
H^(r)_0 = 0.  So the sharp form of (B-bot) is

    k | N_{rho_j}   only for the blocks j whose M_j does NOT contain an H^(r)_k
    l | N_{sigma_j} only for the blocks j whose M_j does NOT contain an H^(r)_l

which is strictly weaker than the blanket force_k = force_l = 1 of the ansatz,
and (measured, see Z5STAR_CERT 3.2) it is the difference between the coupling
() block closing and not closing.  The MAXIMAL blocks carry rho_j = w_j r_Q and
satisfy both automatically (r_Q has a factor k^3, s_Q a factor l^3).
"""
import sys, os, time
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
sys.path.insert(1, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
sys.path.insert(2, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import mindens
import bare, solve, fastlin, ratrec
from solve import Ansatz
import frw, cert, family, joint
import cert2

P1 = frw.P
P2 = frw.P2


def kfree(m):
    """does M vanish at k = 0 ?  (i.e. does it contain an H^(r)_k letter)"""
    return any(bare.LETTERS[L][1] == 'k' for L in m)


def lfree(m):
    return any(bare.LETTERS[L][1] == 'l' for L in m)


def force_of(m):
    """the (B-bot) forcing REQUIRED for block M"""
    return (0 if kfree(m) else 1, 0 if lfree(m) else 1)


def mk(dname, slack, fk, fl, m=3):
    D = cert2.dens2(m)[dname]
    dk0 = sum(mu * abs(f[2]) for f, mu in D)
    dl0 = sum(mu * abs(f[3]) for f, mu in D)
    return Ansatz(D, D, dk0 + slack, dl0 + slack, dk0 + slack, dl0 + slack,
                  force_k=fk, force_l=fl)


def build(n, w, B, dL, sL, d0, s0, p=P1, m=3, ratio=1.35, vnpts=400,
          vseed=987654, verbose=True, seedL=1234, seed0=555, bbot=True):
    J = len(B)
    maximal, letters, zero_j = cert2.blocks_of(B)
    act = [j for j in letters
           if any(cert.divide(B[j], B[jj]) is not None and w[jj] for jj in range(J))]
    avec = [1] + [0] * (m - 3)
    t0 = time.time()
    # --- group the active letter blocks by their required forcing
    grp = {}
    for j in act:
        g = force_of(B[j]) if bbot else (0, 0)
        grp.setdefault(g, []).append(j)
    ansL = {g: mk(dL, sL, g[0], g[1], m) for g in grp}
    g0 = force_of(()) if bbot else (0, 0)          # the () block: (1,1)
    ans0 = mk(d0, s0, g0[0], g0[1], m)
    nptsL = int(1.4 * max(a.nc for a in ansL.values())) + 60
    pdL = frw.PD(p, n, m, nptsL, B, avec, seed=seedL)
    MscL = {g: frw.scal_mat(pdL, ansL[g]) for g in grp}
    H = {}
    for g in grp:
        ns = ratrec.nullspace(MscL[g], p)
        H[g] = np.array(ns, dtype=np.int64) if ns else np.zeros((0, ansL[g].nc), np.int64)
    rvL = np.zeros((J, nptsL), dtype=np.int64); svL = np.zeros((J, nptsL), dtype=np.int64)
    for j in maximal:
        rvL[j] = int(w[j]) * pdL.RQ1 % p
        svL[j] = int(w[j]) * pdL.SQ1 % p
    XP = {}
    nbadL = 0
    for g, js in grp.items():
        RHS = np.zeros((nptsL, len(js)), dtype=np.int64)
        for c, j in enumerate(js):
            RHS[:, c] = family.block_rhs(pdL, w, B, maximal, B[j], rvL, svL)
        X, rk, piv, _ = fastlin.solve(MscL[g], RHS, p)
        for c, j in enumerate(js):
            XP[j] = X[:, c]
            nbadL += int(np.count_nonzero((cert.mv(MscL[g], X[:, c], p) - RHS[:, c]) % p))
    # --- the () block with every letter block's curl gauge
    ncols = ans0.nc + sum(H[force_of(B[j]) if bbot else (0, 0)].shape[0] for j in act)
    npts0 = int(ratio * ncols) + 40
    pd0 = frw.PD(p, n, m, npts0, B, avec, seed=seed0)
    Msc0 = frw.scal_mat(pd0, ans0)
    EV = {g: cert.evalmats(pd0, ansL[g]) for g in grp}
    rv = np.zeros((J, npts0), dtype=np.int64); sv = np.zeros((J, npts0), dtype=np.int64)
    for j in maximal:
        rv[j] = int(w[j]) * pd0.RQ1 % p
        sv[j] = int(w[j]) * pd0.SQ1 % p
    Gcols = []
    slots = {}
    off = ans0.nc
    for j in act:
        g = force_of(B[j]) if bbot else (0, 0)
        R1L, R0L, S1L, S0L = EV[g]
        nrL = len(ansL[g].mons_r)
        rv[j] = cert.mv(R1L, XP[j][:nrL], p)
        sv[j] = cert.mv(S1L, XP[j][nrL:], p)
        nk = H[g].shape[0]
        if nk:
            Hr = np.ascontiguousarray(H[g][:, :nrL].T)
            Hs = np.ascontiguousarray(H[g][:, nrL:].T)
            KR = joint.matmul(R1L, Hr, p); KS = joint.matmul(S1L, Hs, p)
            sk, sl = cert.shiftpair(pd0, B[j])
            Gcols.append(((pd0.gk * sk % p)[:, None] * KR
                          + (pd0.gl * sl % p)[:, None] * KS) % p)
        slots[j] = (off, nk, g)
        off += nk
    rhs0 = cert.Ewphi(pd0, w, (), B)
    for jj in range(J):
        if jj == zero_j:
            continue
        sk, sl = cert.shiftpair(pd0, B[jj])
        rhs0 = (rhs0 - pd0.gk * sk % p * rv[jj] - pd0.gl * sl % p * sv[jj]) % p
    LHS = np.concatenate([Msc0] + Gcols, axis=1) if Gcols else Msc0
    z, rk0, piv0, nbad0 = fastlin.solve(LHS, rhs0, p)
    x0 = z[:ans0.nc]
    coefL = {}
    for j in act:
        o, nk, g = slots[j]
        h = z[o:o + nk]
        coefL[j] = ((XP[j] + (h.astype(object) @ H[g].astype(object)) % p)
                    .astype(np.int64) % p) if nk else XP[j] % p
    if verbose:
        print('  n=%-3d p=%d bbot=%s  letters %s/s%d nc=%s ker=%s nbad=%d ; '
              '() %s/s%d nc=%d cols=%d rows=%d ratio=%.2f rank=%d nbad=%d  [%.0fs]'
              % (n, p, bbot, dL, sL, {g: ansL[g].nc for g in grp},
                 {g: H[g].shape[0] for g in grp}, nbadL, d0, s0, ans0.nc,
                 LHS.shape[1], npts0, npts0 / LHS.shape[1], rk0, nbad0,
                 time.time() - t0), flush=True)
    out = dict(nbadL=nbadL, nbad0=nbad0, coefL=coefL, x0=x0, ansL=ansL, ans0=ans0,
               act=act, maximal=maximal, zero_j=zero_j, grp=grp, J=J,
               forces={j: (force_of(B[j]) if bbot else (0, 0)) for j in act})
    if vnpts:
        out['bad'] = verify(n, w, B, out, p, m, vnpts, vseed, verbose)
    return out


def verify(n, w, B, out, p, m, vnpts, vseed, verbose=True):
    """recompute EVERY one of the J residual components at FRESH points"""
    J = len(B)
    avec = [1] + [0] * (m - 3)
    pv = frw.PD(p, n, m, vnpts, B, avec, seed=vseed)
    EV = {g: cert.evalmats(pv, out['ansL'][g]) for g in out['grp']}
    V10, V00, W10, W00 = cert.evalmats(pv, out['ans0'])
    rq0, sq0 = cert.qcof(pv)
    Rv1 = np.zeros((J, vnpts), dtype=np.int64); Rv0 = np.zeros((J, vnpts), dtype=np.int64)
    Sv1 = np.zeros((J, vnpts), dtype=np.int64); Sv0 = np.zeros((J, vnpts), dtype=np.int64)
    for j in out['maximal']:
        Rv1[j] = int(w[j]) * pv.RQ1 % p; Rv0[j] = int(w[j]) * rq0 % p
        Sv1[j] = int(w[j]) * pv.SQ1 % p; Sv0[j] = int(w[j]) * sq0 % p
    for j in out['act']:
        g = out['forces'][j]
        V1L, V0L, W1L, W0L = EV[g]
        nrL = len(out['ansL'][g].mons_r)
        x = out['coefL'][j]
        Rv1[j] = cert.mv(V1L, x[:nrL], p); Rv0[j] = cert.mv(V0L, x[:nrL], p)
        Sv1[j] = cert.mv(W1L, x[nrL:], p); Sv0[j] = cert.mv(W0L, x[nrL:], p)
    nr0 = len(out['ans0'].mons_r)
    zj = out['zero_j']
    Rv1[zj] = cert.mv(V10, out['x0'][:nr0], p); Rv0[zj] = cert.mv(V00, out['x0'][:nr0], p)
    Sv1[zj] = cert.mv(W10, out['x0'][nr0:], p); Sv0[zj] = cert.mv(W00, out['x0'][nr0:], p)
    bad = {}
    for i in range(J):
        mi = B[i]
        acc = (-Rv0[i] - Sv0[i]) % p
        for j in range(J):
            rest = cert.divide(mi, B[j])
            if rest is None:
                continue
            sk, sl = cert.shiftpair(pv, rest)
            acc = (acc + pv.gk * sk % p * Rv1[j] + pv.gl * sl % p * Sv1[j]) % p
        acc = (acc - cert.Ewphi(pv, w, mi, B)) % p
        nb = int(np.count_nonzero(acc))
        if nb:
            bad[str(mi)] = nb
    if verbose:
        print('  FRESH-POINT check: %d pts x %d components = %d identities -- %s'
              % (vnpts, J, vnpts * J, 'ALL ZERO' if not bad else 'FAILURES %s' % bad),
              flush=True)
    return bad


def bbot_check(n, w, B, out, p, m=3, npt=80, verbose=True):
    """DIRECT numerical (B-bot).  For every block j whose monomial M_j does NOT
    vanish at k = 0 we must have rho_j(n,0,l) = 0 identically in l; likewise
    sigma_j(n,k,0) = 0 for every j with M_j not vanishing at l = 0.  Blocks whose
    M_j DOES vanish there are unconstrained.  Checked at random l (resp. k).
    The maximal blocks carry w_j*r_Q, w_j*s_Q and are checked the same way."""
    import qrow
    J = len(B)
    rng = np.random.default_rng(20260726 + n)
    rf, sf = qrow.make_evals(n, p)
    badR = []
    badS = []
    for _ in range(npt):
        l = int(rng.integers(2, p - 2)); k = int(rng.integers(2, p - 2))
        for j in range(J):
            mj = B[j]
            if j in out['maximal']:
                if not w[j]:
                    continue
                cofR = int(w[j]) * rf(0, 0, l) % p
                cofS = int(w[j]) * sf(0, k, 0) % p
            elif j in out['act']:
                g = out['forces'][j]; a = out['ansL'][g]
                cofR = a.eval_r(out['coefL'][j], n, 0, l, p)
                cofS = a.eval_s(out['coefL'][j], n, k, 0, p)
            elif j == out['zero_j']:
                a = out['ans0']
                cofR = a.eval_r(out['x0'], n, 0, l, p)
                cofS = a.eval_s(out['x0'], n, k, 0, p)
            else:
                continue
            if not kfree(mj) and cofR % p:
                badR.append((str(mj), l))
            if not lfree(mj) and cofS % p:
                badS.append((str(mj), k))
    if verbose:
        print('  (B-bot) DIRECT, %d random points x %d blocks : '
              'rho_j(n,0,l) != 0 in %d cases, sigma_j(n,k,0) != 0 in %d cases  %s'
              % (npt, J, len(badR), len(badS),
                 'PASS' if not badR and not badS else
                 'FAIL %s %s' % (badR[:3], badS[:3])), flush=True)
    return badR, badS
