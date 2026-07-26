"""JOB 2, final form -- (B-bot) imposed EXACTLY, as GROUPED linear constraints
inside the joint solve.

Why grouped.  (B-bot) is  R_w(n,0,l) = Phi(n,0,l) * sum_j rho_j(n,0,l) M_j(n,0,l) = 0.
At k = 0 the nine-letter alphabet COLLAPSES:

      H^(r)_k      -> 0                     (H^(r)_0 = 0: the monomial dies)
      H^(r)_{n+k}  -> H^(r)_n               = the H^(r)_n letter
      H^(r)_{k+l}  -> H^(r)_l               = the H^(r)_l letter
      H^(r)_{n+k+l}-> H^(r)_{n+l}           = the H^(r)_{n+l} letter
      H^(r)_{n+3-k}-> H^(r)_{n+3}           (mixed base; a constant in l)
      H^(r)_{n+3-l}-> H^(r)_{n+3-l}

so DIFFERENT basis monomials become the SAME function of (n,l).  Over Q(n) with
the harmonic values as independent atoms, (B-bot) is therefore

      for every COLLAPSE CLASS c :   sum_{j in c} rho_j(n,0,l) = 0   identically in l,

which is strictly weaker than the per-block  rho_j(n,0,l) = 0  that force_k = 1
imposes -- and (measured, Z5STAR_CERT 3.2) the difference is exactly whether the
coupling () block closes.  The class of the empty monomial is a singleton, so
rho_{()}(n,0,l) = 0 IS required; that is the one the ansatz must carry.

Implementation: solve the letter blocks with the FULL (unforced) ansatz so the
curl gauge is as large as possible, then solve the () block and the gauge
TOGETHER subject to the grouped (B-bot) rows, appended to the joint system.
"""
import sys, os, time
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
sys.path.insert(1, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
sys.path.insert(2, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import mindens
import bare, solve, fastlin, ratrec, qrow
from solve import Ansatz, dval
import frw, cert, family, joint
import cert2, cert3

P1 = frw.P
P2 = frw.P2

REDK = {'n': 'n', 'pk': 'n', 'l': 'l', 'kl': 'l', 'pl': 'pl', 'pkl': 'pl',
        'mk': 'mk', 'ml': 'ml'}
REDL = {'n': 'n', 'pl': 'n', 'k': 'k', 'kl': 'k', 'pk': 'pk', 'pkl': 'pk',
        'ml': 'ml', 'mk': 'mk'}


def classes(B, which):
    """collapse classes at k = 0 (which='k') or l = 0 (which='l')."""
    red = REDK if which == 'k' else REDL
    dead = 'k' if which == 'k' else 'l'
    out = {}
    for j, m in enumerate(B):
        args = [bare.LETTERS[L][1] for L in m]
        if dead in args:
            continue                        # monomial vanishes: no constraint
        key = tuple(sorted(bare.lname(bare.LETTERS[L][0], red[bare.LETTERS[L][1]])
                           for L in m))
        out.setdefault(key, []).append(j)
    return out


def build(n, w, B, dL, sL, d0, s0, p=P1, m=3, ratio=1.35, vnpts=400,
          vseed=987654, verbose=True, seedL=1234, seed0=555, bbot=True,
          nbpts=None):
    J = len(B)
    maximal, letters, zero_j = cert2.blocks_of(B)
    act = [j for j in letters
           if any(cert.divide(B[j], B[jj]) is not None and w[jj] for jj in range(J))]
    avec = [1] + [0] * (m - 3)
    t0 = time.time()
    ansL = cert3.mk(dL, sL, 0, 0, m)
    ans0 = cert3.mk(d0, s0, 0, 0, m)
    nrL = len(ansL.mons_r); nr0 = len(ans0.mons_r)
    # ---- letter blocks, unforced (maximum curl gauge)
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
    # ---- the () block + gauge
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
        Ab, bb = bbot_rows(n, w, B, act, maximal, zero_j, ansL, ans0, XP, H, p,
                           nbpts)
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
              'nc=%d cols=%d rows=%d(+%d Bbot) ratio=%.2f rank=%d nbad=%d  [%.0fs]'
              % (n, p, bbot, dL, sL, ansL.nc, nk, nbadL, d0, s0, ans0.nc,
                 LHS.shape[1], npts0, nbrow, npts0 / LHS.shape[1], rk0, nbad0,
                 time.time() - t0), flush=True)
    out = dict(nbadL=nbadL, nbad0=nbad0, coefL=coefL, x0=x0, ansL=ansL, ans0=ans0,
               act=act, maximal=maximal, zero_j=zero_j, J=J, nk=nk,
               grp={(0, 0): act}, forces={j: (0, 0) for j in act},
               ansLd={(0, 0): ansL})
    out['ansL'] = {(0, 0): ansL}
    if vnpts:
        out['bad'] = cert3.verify(n, w, B, out, p, m, vnpts, vseed, verbose)
    out['ansL'] = ansL
    return out


def bbot_rows(n, w, B, act, maximal, zero_j, ansL, ans0, XP, H, p, nbpts=None):
    """rows expressing  sum_{j in class} rho_j(n,0,l) = 0  and the l-mirror,
    in the unknowns (x0, h_1..h_{|act|}) of the joint system."""
    nrL = len(ansL.mons_r); nr0 = len(ans0.mons_r)
    nk = H.shape[0]
    ncols = ans0.nc + len(act) * nk
    dlmax = max(b for a, b in ans0.mons_r + ansL.mons_r) + 2
    if nbpts is None:
        nbpts = dlmax + 6
    rng = np.random.default_rng(777 + n)
    rows = []
    rhs = []
    idx = {j: c for c, j in enumerate(act)}
    rf, sf = qrow.make_evals(n, p)
    for which in ('k', 'l'):
        cls = classes(B, which)
        pts = []
        while len(pts) < nbpts:
            v = int(rng.integers(2, p - 2))
            kk, ll = (0, v) if which == 'k' else (v, 0)
            if all(x % p for x in [v, v + 1, v + 2, n + v + 1, n + v + 2, n + v + 3,
                                   v + 1, n + 1 - v, n + 3 - v]):
                pts.append((kk, ll))
        for key, js in cls.items():
            js = [j for j in js if j in idx or j == zero_j or j in maximal]
            if not js:
                continue
            if all(j in maximal for j in js):
                continue                      # r_Q has k^3 / s_Q has l^3: free
            for (kk, ll) in pts:
                row = np.zeros(ncols, dtype=np.int64)
                const = 0
                for j in js:
                    if j in maximal:
                        if not w[j]:
                            continue
                        v = (rf(0, kk, ll) if which == 'k' else sf(0, kk, ll))
                        const = (const + int(w[j]) * v) % p
                    elif j == zero_j:
                        mons = ans0.mons_r if which == 'k' else ans0.mons_s
                        off = 0 if which == 'k' else nr0
                        D = ans0.Dr if which == 'k' else ans0.Ds
                        iD = pow(dval(D, n, kk, ll, p), p - 2, p)
                        for u, (a, b) in enumerate(mons):
                            row[off + u] = (row[off + u]
                                            + pow(kk % p, a, p) * pow(ll % p, b, p)
                                            % p * iD) % p
                    else:
                        c = idx[j]
                        mons = ansL.mons_r if which == 'k' else ansL.mons_s
                        off = 0 if which == 'k' else nrL
                        D = ansL.Dr if which == 'k' else ansL.Ds
                        iD = pow(dval(D, n, kk, ll, p), p - 2, p)
                        vec = np.zeros(ansL.nc, dtype=np.int64)
                        for u, (a, b) in enumerate(mons):
                            vec[off + u] = pow(kk % p, a, p) * pow(ll % p, b, p) % p * iD % p
                        const = (const + int((vec.astype(object)
                                              @ XP[:, c].astype(object)) % p)) % p
                        contrib = (H.astype(object) @ vec.astype(object)) % p
                        base = ans0.nc + c * nk
                        row[base:base + nk] = (row[base:base + nk]
                                               + contrib.astype(np.int64)) % p
                if not row.any():
                    if const % p:
                        rows.append(row); rhs.append((-const) % p)   # infeasible marker
                    continue
                rows.append(row); rhs.append((-const) % p)
    if not rows:
        return np.zeros((0, ncols), dtype=np.int64), np.zeros(0, dtype=np.int64)
    return (np.array(rows, dtype=np.int64) % p,
            np.array(rhs, dtype=np.int64) % p)
