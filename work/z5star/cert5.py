"""The certificate in the (B-bot)-SATISFYING GAUGE, with the 16 collapse-class
rows assembled EXACTLY and for free.

The vectorisation the coordinator asked for turned out to be a simplification
instead.  At k = 0 the ansatz numerator collapses:

    rho_j(n,0,l) = ( sum_{a,b} c_{ab} 0^a l^b ) / D(n,0,l)
                 = ( sum_b c_{0b} l^b ) / D(n,0,l) ,

so only the  a = 0  row of the (k,l)-monomial grid survives -- 13 of 169
coefficients for a letter block, 17 of 289 for the () block.  Every ansatz block
shares the SAME denominator D, so a collapse class c imposes

    sum_{j in c}  c^{(j)}_{0b}  =  0        for every power b,

which is an EXACT linear condition on the unknowns with no sample points at all.
The maximal blocks drop out identically: their cofactor is w_j*r_Q and r_Q has a
factor k^3 (and s_Q an l^3), so they contribute 0 at the boundary.

Cost: 17 x 17 = 289 dense rows assembled by numpy indexing, microseconds --
against the ~40 s per (n,p) of the point-sampled version in gosper.py.
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
import cert2, cert3, cert4

P1 = frw.P
M = 3


def rho_k0_index(ans):
    """indices in the coefficient vector of the monomials (a=0, b) of N_rho,
    in increasing b -- these are the only ones that survive at k = 0."""
    return {b: u for u, (a, b) in enumerate(ans.mons_r) if a == 0}


def sig_l0_index(ans):
    """indices of the monomials (a, b=0) of N_sigma, in increasing a."""
    nr = len(ans.mons_r)
    return {a: nr + u for u, (a, b) in enumerate(ans.mons_s) if b == 0}


def bbot_rows_exact(B, act, maximal, zero_j, ansL, ans0, XP, H, ncols, p,
                    exclude_empty=True):
    """the 16 collapse-class conditions, EXACT.  Unknown vector is
    (x0 | h_1 ... h_{|act|}) exactly as in cert4.build."""
    nk = H.shape[0]
    idxm = {j: c for c, j in enumerate(act)}
    IL = {'k': rho_k0_index(ansL), 'l': sig_l0_index(ansL)}
    I0 = {'k': rho_k0_index(ans0), 'l': sig_l0_index(ans0)}
    rows = []
    rhs = []
    for which in ('k', 'l'):
        cls = cert4.classes(B, which)
        # H restricted to the surviving coefficient positions, per power
        for key, js in cls.items():
            if exclude_empty and key == ():
                continue
            js2 = [j for j in js if j in idxm or j == zero_j]
            if not js2:
                continue                    # only maximal members: identically 0
            powers = set(IL[which]) | set(I0[which])
            for b in sorted(powers):
                row = np.zeros(ncols, dtype=np.int64)
                const = 0
                touched = False
                for j in js2:
                    if j == zero_j:
                        u = I0[which].get(b)
                        if u is None:
                            continue
                        row[u] = (row[u] + 1) % p
                        touched = True
                    else:
                        u = IL[which].get(b)
                        if u is None:
                            continue
                        c = idxm[j]
                        const = (const + int(XP[u, c])) % p
                        base = ans0.nc + c * nk
                        row[base:base + nk] = (row[base:base + nk] + H[:, u]) % p
                        touched = True
                if not touched:
                    continue
                rows.append(row)
                rhs.append((-const) % p)
    if not rows:
        return (np.zeros((0, ncols), dtype=np.int64), np.zeros(0, dtype=np.int64))
    return (np.array(rows, dtype=np.int64) % p, np.array(rhs, dtype=np.int64) % p)


def build(n, w, B, dL, sL, d0, s0, p=P1, m=3, ratio=1.35, vnpts=400,
          vseed=987654, verbose=True, seedL=1234, seed0=555, bbot=True):
    J = len(B)
    maximal, letters, zero_j = cert2.blocks_of(B)
    act = [j for j in letters
           if any(cert.divide(B[j], B[jj]) is not None and w[jj] for jj in range(J))]
    avec = [1] + [0] * (m - 3)
    t0 = time.time()
    ansL = cert3.mk(dL, sL, 0, 0, m)
    ans0 = cert3.mk(d0, s0, 0, 0, m)
    nrL = len(ansL.mons_r); nr0 = len(ans0.mons_r)
    nptsL = int(1.4 * ansL.nc) + 60
    pdL = frw.PD(p, n, m, nptsL, B, avec, seed=seedL)
    MscL = frw.scal_mat(pdL, ansL)
    H = np.array(ratrec.nullspace(MscL, p), dtype=np.int64)
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
    ncols = ans0.nc + len(act) * nk
    npts0 = int(ratio * ncols) + 40
    pd0 = frw.PD(p, n, m, npts0, B, avec, seed=seed0)
    Msc0 = frw.scal_mat(pd0, ans0)
    R1L, R0L, S1L, S0L = cert.evalmats(pd0, ansL)
    Hr = np.ascontiguousarray(H[:, :nrL].T); Hs = np.ascontiguousarray(H[:, nrL:].T)
    KR = joint.matmul(R1L, Hr, p); KS = joint.matmul(S1L, Hs, p)
    G = np.zeros((npts0, len(act) * nk), dtype=np.int64)
    rv = np.zeros((J, npts0), dtype=np.int64); sv = np.zeros((J, npts0), dtype=np.int64)
    for j in maximal:
        rv[j] = int(w[j]) * pd0.RQ1 % p
        sv[j] = int(w[j]) * pd0.SQ1 % p
    for c, j in enumerate(act):
        sk, sl = cert.shiftpair(pd0, B[j])
        G[:, c * nk:(c + 1) * nk] = ((pd0.gk * sk % p)[:, None] * KR
                                     + (pd0.gl * sl % p)[:, None] * KS) % p
        rv[j] = cert.mv(R1L, XP[:nrL, c], p)
        sv[j] = cert.mv(S1L, XP[nrL:, c], p)
    rhs0 = cert.Ewphi(pd0, w, (), B)
    for jj in range(J):
        if jj == zero_j:
            continue
        sk, sl = cert.shiftpair(pd0, B[jj])
        rhs0 = (rhs0 - pd0.gk * sk % p * rv[jj] - pd0.gl * sl % p * sv[jj]) % p
    LHS = np.concatenate([Msc0, G], axis=1)
    rhsF = rhs0
    nbrow = 0
    if bbot:
        Ab, bb = bbot_rows_exact(B, act, maximal, zero_j, ansL, ans0, XP, H,
                                 LHS.shape[1], p)
        nbrow = Ab.shape[0]
        LHS = np.concatenate([LHS, Ab], axis=0)
        rhsF = np.concatenate([rhs0, bb])
    z, rk0, piv0, nbad0 = fastlin.solve(LHS, rhsF, p)
    x0 = z[:ans0.nc]
    coefL = {}
    for c, j in enumerate(act):
        h = z[ans0.nc + c * nk: ans0.nc + (c + 1) * nk]
        coefL[j] = ((XP[:, c] + (h.astype(object) @ H.astype(object)) % p)
                    .astype(np.int64) % p)
    if verbose:
        print('  n=%-3d p=%d bbot=%s  letters %s/s%d nc=%d ker=%d nbad=%d ; () %s/s%d '
              'nc=%d cols=%d rows=%d(+%d Bbot) rank=%d nbad=%d  [%.1fs]'
              % (n, p, bbot, dL, sL, ansL.nc, nk, nbadL, d0, s0, ans0.nc,
                 LHS.shape[1], npts0, nbrow, rk0, nbad0, time.time() - t0), flush=True)
    out = dict(nbadL=nbadL, nbad0=nbad0, coefL=coefL, x0=x0, ansL={(0, 0): ansL},
               ans0=ans0, act=act, maximal=maximal, zero_j=zero_j, J=J, nk=nk,
               grp={(0, 0): act}, forces={j: (0, 0) for j in act})
    if vnpts:
        out['bad'] = cert3.verify(n, w, B, out, p, m, vnpts, vseed, verbose)
    out['ansL'] = ansL
    return out


def bbot_verify(n, w, B, out, p, npt=40, verbose=True):
    """DIRECT check that the solved cofactors satisfy (B-bot): every collapse
    class sums to zero at k = 0 (resp. l = 0), at random points."""
    import qrow
    from solve import dval
    ansL = out['ansL']; ans0 = out['ans0']
    rng = np.random.default_rng(31337 + n)
    rf, sf = qrow.make_evals(n, p)
    bad = []
    for which in ('k', 'l'):
        cls = cert4.classes(B, which)
        for key, js in cls.items():
            if key == ():
                continue
            js2 = [j for j in js if j in out['act'] or j == out['zero_j']
                   or j in out['maximal']]
            if not js2 or all(j in out['maximal'] for j in js2):
                continue
            for _ in range(npt):
                v = int(rng.integers(2, p - 2))
                kk, ll = (0, v) if which == 'k' else (v, 0)
                tot = 0
                for j in js2:
                    if j in out['maximal']:
                        if not w[j]:
                            continue
                        val = (rf(0, kk, ll) if which == 'k' else sf(0, kk, ll))
                        tot = (tot + int(w[j]) * val) % p
                    elif j == out['zero_j']:
                        tot = (tot + (ans0.eval_r(out['x0'], n, kk, ll, p)
                                      if which == 'k'
                                      else ans0.eval_s(out['x0'], n, kk, ll, p))) % p
                    else:
                        x = out['coefL'][j]
                        tot = (tot + (ansL.eval_r(x, n, kk, ll, p) if which == 'k'
                                      else ansL.eval_s(x, n, kk, ll, p))) % p
                if tot % p:
                    bad.append((which, key, v))
    if verbose:
        print('  (B-bot) DIRECT: %d violations over the 16 classes x %d points  %s'
              % (len(bad), npt, 'PASS' if not bad else 'FAIL %s' % bad[:3]), flush=True)
    return bad
