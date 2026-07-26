"""DEFINITIVE verification: for a given weight w, build the complete order-3
certificate (all J blocks) and check ALL J residual components at FRESH points.

Blocks:
  * the 90 maximal weight-3 blocks : Theorem R,  r_j = w_j r_Q ,  s_j = w_j s_Q
  * the 18 letter blocks           : ansatz ansL, particular + gauge h_j
  * the () block                   : ansatz ans0
The gauge h_j in ker(Msc_L) and the ()-cofactor are solved TOGETHER.
"""
import sys, os, time, pickle
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
os.chdir('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
import fastlin, ratrec, qrow, ordm
from solve import Ansatz
import bare, frw, cert, family, joint


def build(n, w, B, slackL, slack0, dname='F1', p=frw.P, m=3, ratio=1.35,
          vnpts=400, vseed=987654, verbose=True):
    J = len(B)
    D = frw.dens(m)[dname]
    dk0 = sum(mu * abs(f[2]) for f, mu in D)
    dl0 = sum(mu * abs(f[3]) for f, mu in D)
    ansL = Ansatz(D, D, dk0 + slackL, dl0 + slackL, dk0 + slackL, dl0 + slackL, 0, 0)
    ans0 = Ansatz(D, D, dk0 + slack0, dl0 + slack0, dk0 + slack0, dl0 + slack0, 0, 0)
    maximal = [j for j in range(J) if len(bare.upset(B, B[j])) == 1]
    letters = [j for j in range(J) if len(B[j]) == 1 and j not in maximal]
    idx = {mm: j for j, mm in enumerate(B)}
    zero_j = idx[()]
    avec = [1] + [0] * (m - 3)
    nrL = len(ansL.mons_r)
    # ---- letter blocks
    nptsL = int(1.4 * ansL.nc) + 60
    pdL = frw.PD(p, n, m, nptsL, B, avec, seed=1234)
    MscL = frw.scal_mat(pdL, ansL)
    H = np.array(ratrec.nullspace(MscL, p), dtype=np.int64)
    nk = H.shape[0]
    rvL = np.zeros((J, nptsL), dtype=np.int64); svL = np.zeros((J, nptsL), dtype=np.int64)
    for j in maximal:
        rvL[j] = int(w[j]) * pdL.RQ1 % p
        svL[j] = int(w[j]) * pdL.SQ1 % p
    RHS = np.zeros((nptsL, len(letters)), dtype=np.int64)
    for c, j in enumerate(letters):
        RHS[:, c] = family.block_rhs(pdL, w, B, maximal, B[j], rvL, svL)
    XP, rkL, piv, _ = fastlin.solve(MscL, RHS, p)
    nbadL = sum(int(np.count_nonzero((cert.mv(MscL, XP[:, c], p) - RHS[:, c]) % p))
                for c in range(len(letters)))
    # ---- the () block with the gauge, on its own point set
    ncols = ans0.nc + len(letters) * nk
    npts0 = int(ratio * ncols) + 40
    pd0 = frw.PD(p, n, m, npts0, B, avec, seed=555)
    Msc0 = frw.scal_mat(pd0, ans0)
    R1L, R0L, S1L, S0L = cert.evalmats(pd0, ansL)
    Hr = np.ascontiguousarray(H[:, :nrL].T); Hs = np.ascontiguousarray(H[:, nrL:].T)
    KR = joint.matmul(R1L, Hr, p); KS = joint.matmul(S1L, Hs, p)
    G = np.zeros((npts0, len(letters) * nk), dtype=np.int64)
    for c, j in enumerate(letters):
        sk, sl = cert.shiftpair(pd0, B[j])
        G[:, c * nk:(c + 1) * nk] = ((pd0.gk * sk % p)[:, None] * KR
                                     + (pd0.gl * sl % p)[:, None] * KS) % p
    rv = np.zeros((J, npts0), dtype=np.int64); sv = np.zeros((J, npts0), dtype=np.int64)
    for j in maximal:
        rv[j] = int(w[j]) * pd0.RQ1 % p
        sv[j] = int(w[j]) * pd0.SQ1 % p
    for c, j in enumerate(letters):
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
    for c, j in enumerate(letters):
        h = z[ans0.nc + c * nk: ans0.nc + (c + 1) * nk]
        coefL[j] = (XP[:, c] + (h.astype(object) @ H.astype(object)) % p).astype(np.int64) % p
    if verbose:
        print('  n=%d  letter blocks nbad=%d ; () block: cols=%d rows=%d ratio=%.2f '
              'rank=%d nbad=%d' % (n, nbadL, LHS.shape[1], npts0, npts0 / LHS.shape[1],
                                   rk0, nbad0), flush=True)
    # ---- FRESH-POINT verification of every component
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
    nr0 = len(ans0.mons_r)
    Rv1[zero_j] = cert.mv(V10, x0[:nr0], p); Rv0[zero_j] = cert.mv(V00, x0[:nr0], p)
    Sv1[zero_j] = cert.mv(W10, x0[nr0:], p); Sv0[zero_j] = cert.mv(W00, x0[nr0:], p)
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
        print('  FRESH-POINT check: %d points x %d components = %d identities -- %s'
              % (vnpts, J, vnpts * J, 'ALL ZERO' if not bad else 'FAILURES %s' % bad),
              flush=True)
    return dict(bad=bad, nbad0=nbad0, nbadL=nbadL, coefL=coefL, x0=x0,
                ansL=ansL, ans0=ans0, vnpts=vnpts, J=J)


if __name__ == '__main__':
    fn = sys.argv[1]
    ns = [int(x) for x in sys.argv[2].split(',')]
    slackL = int(sys.argv[3]); slack0 = int(sys.argv[4])
    p = int(sys.argv[5]) if len(sys.argv) > 5 else frw.P
    B, tops = bare.span_w3(maxdeg=2)
    w = np.load(fn)
    if p != frw.P:
        # re-reduce the rational weight at the new prime
        import rationalise
        Q = rationalise.to_Q(w, frw.P)
        w = np.array([int(c.numerator) % p * pow(int(c.denominator) % p, p - 2, p) % p
                      for c in Q], dtype=np.int64)
    for n in ns:
        build(n, w, B, slackL, slack0, p=p)
        sys.stdout.flush()
