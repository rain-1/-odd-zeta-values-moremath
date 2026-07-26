"""JOB 2 -- the full order-3 certificate WITH (B-bot) imposed in the ansatz.

Same architecture as work/z5rep/verify_full.py, with three additions:

  * force_k / force_l:  k | N_rho  and  l | N_sigma, i.e. (B-bot)
        rho_j(n,0,l) = 0 ,  sigma_j(n,k,0) = 0        for every ansatz block.
    The MAXIMAL blocks are  rho_j = w_j * r_Q  and already satisfy (B-bot):
    r_Q's numerator has a factor k^3 and s_Q's an l^3
    [VERIFIED symbolically from work/z5cf/Qrow_phicert.m, "Bbot_r_k0"/"Bbot_s_l0"].
  * a configurable denominator zoo (dens2) so the ansatz can be SHRUNK and the
    minimal one measured rather than guessed.
  * the solved cofactor coefficient vectors are returned, so that the n-sweep of
    JOB 3 can reconstruct them over Q(n).

Everything is mod p at fixed numeric n, exactly as the predecessor.
"""
import sys, os, time, pickle
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
sys.path.insert(1, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import bare
import ordm, solve, fastlin, ratrec
from solve import Ansatz
import frw, cert, family, joint

P1 = frw.P
P2 = frw.P2


# ------------------------------------------------------------- denominators -

def dens2(m=3):
    """denominator zoo.  F1 is the predecessor's; the G-family is leaner and is
    what the minimal-ansatz measurement scans."""
    K1, L1 = ordm.K1, ordm.L1
    NK, NL, NKL = ordm.NK, ordm.NL, ordm.NKL
    KL = [(j, 0, 1, 1) for j in range(0, 12)]
    for _j in range(12):
        solve.NAMES[KL[_j]] = 'k+l+%d' % _j
    out = dict(frw.dens(m))
    out['G0'] = [(K1, 3), (L1, 3), (KL[1], 1), (KL[2], 1)] \
        + [(NK[j], 1) for j in range(1, m + 1)] + [(NL[j], 1) for j in range(1, m + 1)] \
        + [(NKL[1], 1)]
    out['G1'] = [(K1, 3), (L1, 3), (KL[1], 1), (KL[2], 1), (KL[3], 1)] \
        + [(NK[j], 2) for j in range(1, m + 1)] + [(NL[j], 2) for j in range(1, m + 1)] \
        + [(NKL[j], 1) for j in range(1, m + 1)]
    out['G2'] = [(K1, 4), (L1, 4), (KL[1], 2), (KL[2], 2), (KL[3], 1)] \
        + [(NK[j], 2) for j in range(1, m + 1)] + [(NL[j], 2) for j in range(1, m + 1)] \
        + [(NKL[j], 1) for j in range(1, m + 1)]
    out['G3'] = [(K1, 3), (L1, 3), (KL[1], 1), (KL[2], 1), (KL[3], 1)] \
        + [(NK[j], 1) for j in range(1, m + 1)] + [(NL[j], 1) for j in range(1, m + 1)] \
        + [(NKL[j], 1) for j in range(1, m + 1)]
    return out


def mk_ansatz(dname, slack, force, m=3):
    D = dens2(m)[dname]
    dk0 = sum(mu * abs(f[2]) for f, mu in D)
    dl0 = sum(mu * abs(f[3]) for f, mu in D)
    return Ansatz(D, D, dk0 + slack, dl0 + slack, dk0 + slack, dl0 + slack,
                  force_k=force, force_l=force), dk0 + slack, dl0 + slack


def blocks_of(B):
    J = len(B)
    maximal = [j for j in range(J) if len(bare.upset(B, B[j])) == 1]
    letters = [j for j in range(J) if len(B[j]) == 1 and j not in maximal]
    return maximal, letters, B.index(())


# --------------------------------------------- letter blocks only (cheap) ---

def letters_only(n, w, B, dname, slack, force, p=P1, m=3, ratio=1.40, seed=99,
                 verbose=True):
    """Does the LETTER-block system solve in this ansatz?  Returns per-block
    residual counts.  This is the cheap probe used for the minimal-ansatz scan."""
    J = len(B)
    ans, dk, dl = mk_ansatz(dname, slack, force, m)
    npts = int(ratio * ans.nc) + 40
    avec = [1] + [0] * (m - 3)
    maximal, letters, zero_j = blocks_of(B)
    t0 = time.time()
    pd = frw.PD(p, n, m, npts, B, avec, seed=seed)
    Msc = frw.scal_mat(pd, ans)
    rv = np.zeros((J, npts), dtype=np.int64); sv = np.zeros((J, npts), dtype=np.int64)
    for j in maximal:
        rv[j] = int(w[j]) * pd.RQ1 % p
        sv[j] = int(w[j]) * pd.SQ1 % p
    act = [j for j in letters if any(cert.divide(B[j], B[jj]) is not None
                                     and w[jj] for jj in range(J))]
    RHS = np.zeros((npts, len(act)), dtype=np.int64)
    for c, j in enumerate(act):
        RHS[:, c] = family.block_rhs(pd, w, B, maximal, B[j], rv, sv)
    X, rank, piv, _ = fastlin.solve(Msc, RHS, p)
    nb = []
    for c, j in enumerate(act):
        r = (cert.mv(Msc, X[:, c], p) - RHS[:, c]) % p
        nb.append((B[j][0], int(np.count_nonzero(r))))
    nfail = sum(1 for _, x in nb if x)
    if verbose:
        print('   %-3s slack=%-3d force=%d deg=(%d,%d) nc=%-5d npts=%-5d rank=%-5d '
              'ker=%-5d : %d/%d letter blocks FAIL  [%.0fs]'
              % (dname, slack, force, dk, dl, ans.nc, npts, rank, ans.nc - rank,
                 nfail, len(act), time.time() - t0), flush=True)
        if nfail and nfail <= 6:
            print('        failing:', [x for x in nb if x[1]], flush=True)
    return dict(ans=ans, nfail=nfail, nb=nb, X=X, rank=rank, act=act, npts=npts)


# --------------------------------------------- full joint build + verify ----

def build(n, w, B, dnameL, slackL, dname0, slack0, force, p=P1, m=3, ratio=1.35,
          vnpts=400, vseed=987654, verbose=True, seedL=1234, seed0=555):
    """letter blocks (particular + full curl gauge) and the () block solved
    TOGETHER, then every one of the J residual components verified at FRESH
    points.  Returns the cofactor coefficient vectors."""
    J = len(B)
    ansL, dkL, dlL = mk_ansatz(dnameL, slackL, force, m)
    ans0, dk0, dl0 = mk_ansatz(dname0, slack0, force, m)
    maximal, letters, zero_j = blocks_of(B)
    avec = [1] + [0] * (m - 3)
    nrL = len(ansL.mons_r)
    nr0 = len(ans0.mons_r)
    act = [j for j in letters if any(cert.divide(B[j], B[jj]) is not None and w[jj]
                                     for jj in range(J))]
    t0 = time.time()
    # ---- letter blocks
    nptsL = int(1.4 * ansL.nc) + 60
    pdL = frw.PD(p, n, m, nptsL, B, avec, seed=seedL)
    MscL = frw.scal_mat(pdL, ansL)
    H = np.array(ratrec.nullspace(MscL, p), dtype=np.int64)
    if H.size == 0:
        H = np.zeros((0, ansL.nc), dtype=np.int64)
    nk = H.shape[0]
    rvL = np.zeros((J, nptsL), dtype=np.int64); svL = np.zeros((J, nptsL), dtype=np.int64)
    for j in maximal:
        rvL[j] = int(w[j]) * pdL.RQ1 % p
        svL[j] = int(w[j]) * pdL.SQ1 % p
    RHS = np.zeros((nptsL, len(act)), dtype=np.int64)
    for c, j in enumerate(act):
        RHS[:, c] = family.block_rhs(pdL, w, B, maximal, B[j], rvL, svL)
    XP, rkL, piv, _ = fastlin.solve(MscL, RHS, p)
    nbadL = sum(int(np.count_nonzero((cert.mv(MscL, XP[:, c], p) - RHS[:, c]) % p))
                for c in range(len(act)))
    # ---- () block with the letter blocks' curl gauge
    ncols = ans0.nc + len(act) * nk
    npts0 = int(ratio * ncols) + 40
    pd0 = frw.PD(p, n, m, npts0, B, avec, seed=seed0)
    Msc0 = frw.scal_mat(pd0, ans0)
    R1L, R0L, S1L, S0L = cert.evalmats(pd0, ansL)
    G = np.zeros((npts0, len(act) * nk), dtype=np.int64)
    if nk:
        Hr = np.ascontiguousarray(H[:, :nrL].T); Hs = np.ascontiguousarray(H[:, nrL:].T)
        KR = joint.matmul(R1L, Hr, p); KS = joint.matmul(S1L, Hs, p)
        for c, j in enumerate(act):
            sk, sl = cert.shiftpair(pd0, B[j])
            G[:, c * nk:(c + 1) * nk] = ((pd0.gk * sk % p)[:, None] * KR
                                         + (pd0.gl * sl % p)[:, None] * KS) % p
    rv = np.zeros((J, npts0), dtype=np.int64); sv = np.zeros((J, npts0), dtype=np.int64)
    for j in maximal:
        rv[j] = int(w[j]) * pd0.RQ1 % p
        sv[j] = int(w[j]) * pd0.SQ1 % p
    for c, j in enumerate(act):
        rv[j] = cert.mv(R1L, XP[:nrL, c], p)
        sv[j] = cert.mv(S1L, XP[nrL:, c], p)
    rhs0 = cert.Ewphi(pd0, w, (), B)
    for jj in range(J):
        if jj == zero_j:
            continue
        sk, sl = cert.shiftpair(pd0, B[jj])
        rhs0 = (rhs0 - pd0.gk * sk % p * rv[jj] - pd0.gl * sl % p * sv[jj]) % p
    LHS = np.concatenate([Msc0, G], axis=1)
    z, rk0, piv0, nbad0 = fastlin.solve(LHS, rhs0, p)
    x0 = z[:ans0.nc]
    coefL = {}
    for c, j in enumerate(act):
        h = z[ans0.nc + c * nk: ans0.nc + (c + 1) * nk]
        coefL[j] = ((XP[:, c] + (h.astype(object) @ H.astype(object)) % p)
                    .astype(np.int64) % p) if nk else XP[:, c] % p
    if verbose:
        print('  n=%d p=%d force=%d  letters(%s,s%d) nc=%d nbad=%d ker=%d ; '
              '()(%s,s%d) nc=%d cols=%d rows=%d ratio=%.2f rank=%d nbad=%d  [%.0fs]'
              % (n, p, force, dnameL, slackL, ansL.nc, nbadL, nk, dname0, slack0,
                 ans0.nc, LHS.shape[1], npts0, npts0 / LHS.shape[1], rk0, nbad0,
                 time.time() - t0), flush=True)
    # ---- fresh-point verification of every component
    bad = {}
    if vnpts:
        pv = frw.PD(p, n, m, vnpts, B, avec, seed=vseed)
        V1L, V0L, W1L, W0L = cert.evalmats(pv, ansL)
        V10, V00, W10, W00 = cert.evalmats(pv, ans0)
        rq0, sq0 = cert.qcof(pv)
        Rv1 = np.zeros((J, vnpts), dtype=np.int64); Rv0 = np.zeros((J, vnpts), dtype=np.int64)
        Sv1 = np.zeros((J, vnpts), dtype=np.int64); Sv0 = np.zeros((J, vnpts), dtype=np.int64)
        for j in maximal:
            Rv1[j] = int(w[j]) * pv.RQ1 % p; Rv0[j] = int(w[j]) * rq0 % p
            Sv1[j] = int(w[j]) * pv.SQ1 % p; Sv0[j] = int(w[j]) * sq0 % p
        for j, x in coefL.items():
            Rv1[j] = cert.mv(V1L, x[:nrL], p); Rv0[j] = cert.mv(V0L, x[:nrL], p)
            Sv1[j] = cert.mv(W1L, x[nrL:], p); Sv0[j] = cert.mv(W0L, x[nrL:], p)
        Rv1[zero_j] = cert.mv(V10, x0[:nr0], p); Rv0[zero_j] = cert.mv(V00, x0[:nr0], p)
        Sv1[zero_j] = cert.mv(W10, x0[nr0:], p); Sv0[zero_j] = cert.mv(W00, x0[nr0:], p)
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
                  % (vnpts, J, vnpts * J, 'ALL ZERO' if not bad
                     else 'FAILURES %s' % bad), flush=True)
    return dict(bad=bad, nbad0=nbad0, nbadL=nbadL, coefL=coefL, x0=x0, ansL=ansL,
                ans0=ans0, act=act, maximal=maximal, zero_j=zero_j, nk=nk, J=J)
