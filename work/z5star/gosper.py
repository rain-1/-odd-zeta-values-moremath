"""JOB 2, the last obligation.  With the 16 non-() collapse classes imposed, the
whole bottom boundary reduces to two PURELY RATIONAL single sums

    Sum_{l<n+4} Phi(n,0,l) rho_()(n,0,l)  +  Sum_{k<n+4} Phi(n,k,0) sigma_()(n,k,0) = 0 .

Each telescopes iff the one-variable equation

    gl0(n,l) u(l+1) - u(l) = rho_()(n,0,l),   gl0(n,l) = Phi(n,0,l+1)/Phi(n,0,l)
                                                       = (n+3-l)^2 (n+l+1)^2 / (l+1)^4

has a rational solution u (and the k-mirror).  That is a Gosper problem in ONE
variable and it is decided here by a linear solve in a denominator ansatz.
"""
import sys, os, json
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import mindens, wtools as W, cert4, cert2, cert3
import bare, frw, cert, family, joint, fastlin, ratrec, qrow
from solve import dval

M = 3


def build_joint(n, w, B, dL, sL, d0, s0, p):
    maximal, letters, zero_j = cert2.blocks_of(B)
    act = [j for j in letters
           if any(cert.divide(B[j], B[jj]) is not None and w[jj] for jj in range(len(B)))]
    ansL = cert3.mk(dL, sL, 0, 0); ans0 = cert3.mk(d0, s0, 0, 0)
    nrL = len(ansL.mons_r); nr0 = len(ans0.mons_r)
    avec = [1]
    nptsL = int(1.4 * ansL.nc) + 60
    pdL = frw.PD(p, n, M, nptsL, B, avec, seed=1234)
    MscL = frw.scal_mat(pdL, ansL)
    H = np.array(ratrec.nullspace(MscL, p), dtype=np.int64); nk = H.shape[0]
    rvL = np.zeros((len(B), nptsL), dtype=np.int64); svL = np.zeros((len(B), nptsL), dtype=np.int64)
    for j in maximal:
        rvL[j] = int(w[j]) * pdL.RQ1 % p; svL[j] = int(w[j]) * pdL.SQ1 % p
    RHS = np.zeros((nptsL, len(act)), dtype=np.int64)
    for c, j in enumerate(act):
        RHS[:, c] = family.block_rhs(pdL, w, B, maximal, B[j], rvL, svL)
    XP, rkL, piv, _ = fastlin.solve(MscL, RHS, p)
    ncols = ans0.nc + len(act) * nk
    npts0 = int(1.35 * ncols) + 40
    pd0 = frw.PD(p, n, M, npts0, B, avec, seed=555)
    Msc0 = frw.scal_mat(pd0, ans0)
    R1L, R0L, S1L, S0L = cert.evalmats(pd0, ansL)
    Hr = np.ascontiguousarray(H[:, :nrL].T); Hs = np.ascontiguousarray(H[:, nrL:].T)
    KR = joint.matmul(R1L, Hr, p); KS = joint.matmul(S1L, Hs, p)
    G = np.zeros((npts0, len(act) * nk), dtype=np.int64)
    rv = np.zeros((len(B), npts0), dtype=np.int64); sv = np.zeros((len(B), npts0), dtype=np.int64)
    for j in maximal:
        rv[j] = int(w[j]) * pd0.RQ1 % p; sv[j] = int(w[j]) * pd0.SQ1 % p
    for c, j in enumerate(act):
        sk, sl = cert.shiftpair(pd0, B[j])
        G[:, c * nk:(c + 1) * nk] = ((pd0.gk * sk % p)[:, None] * KR
                                     + (pd0.gl * sl % p)[:, None] * KS) % p
        rv[j] = cert.mv(R1L, XP[:nrL, c], p); sv[j] = cert.mv(S1L, XP[nrL:, c], p)
    rhs0 = cert.Ewphi(pd0, w, (), B)
    for jj in range(len(B)):
        if jj == zero_j:
            continue
        sk, sl = cert.shiftpair(pd0, B[jj])
        rhs0 = (rhs0 - pd0.gk * sk % p * rv[jj] - pd0.gl * sl % p * sv[jj]) % p
    LHS = np.concatenate([Msc0, G], axis=1)
    return dict(LHS=LHS, rhs0=rhs0, ansL=ansL, ans0=ans0, act=act, maximal=maximal,
                zero_j=zero_j, XP=XP, H=H, nk=nk, nrL=nrL, nr0=nr0, B=B, w=w, n=n, p=p)


def class_rows(S, exclude_empty=True, npt=None):
    """(B-bot) rows for every collapse class EXCEPT the empty one"""
    B = S['B']; p = S['p']; n = S['n']
    ansL = S['ansL']; ans0 = S['ans0']; XP = S['XP']; H = S['H']; nk = S['nk']
    nrL = S['nrL']; nr0 = S['nr0']
    idxm = {j: c for c, j in enumerate(S['act'])}
    rng = np.random.default_rng(9090 + n)
    if npt is None:
        npt = max(b for a, b in ans0.mons_r + ansL.mons_r) + 8
    rf, sf = qrow.make_evals(n, p)
    rows = []; rhs = []
    for which in ('k', 'l'):
        cls = cert4.classes(B, which)
        pts = []
        while len(pts) < npt:
            v = int(rng.integers(2, p - 2))
            pts.append((0, v) if which == 'k' else (v, 0))
        for key, js in cls.items():
            if exclude_empty and key == ():
                continue
            js2 = [j for j in js if j in idxm or j == S['zero_j'] or j in S['maximal']]
            if not js2 or all(j in S['maximal'] for j in js2):
                continue
            for (kk, ll) in pts:
                row = np.zeros(S['LHS'].shape[1], dtype=np.int64); const = 0
                for j in js2:
                    if j in S['maximal']:
                        if not S['w'][j]:
                            continue
                        v = (rf(0, kk, ll) if which == 'k' else sf(0, kk, ll))
                        const = (const + int(S['w'][j]) * v) % p
                    elif j == S['zero_j']:
                        mons = ans0.mons_r if which == 'k' else ans0.mons_s
                        off = 0 if which == 'k' else nr0
                        D = ans0.Dr if which == 'k' else ans0.Ds
                        iD = pow(dval(D, n, kk, ll, p), p - 2, p)
                        for u, (a, b) in enumerate(mons):
                            row[off + u] = (row[off + u] + pow(kk % p, a, p)
                                            * pow(ll % p, b, p) % p * iD) % p
                    else:
                        c = idxm[j]
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
                rows.append(row); rhs.append((-const) % p)
    return (np.array(rows, dtype=np.int64) % p, np.array(rhs, dtype=np.int64) % p)


def gosper_side(n, p, vals_at, which, degmax=40):
    """solve  g(x) u(x+1) - u(x) = f(x)  for u = Nu(x)/Du(x), Du a product of
    the plausible linear forms; returns the first (Du, deg) that works."""
    # g(x) = (n+3-x)^2 (n+x+1)^2 / (x+1)^4     for both directions (k=0 / l=0)
    def g(x):
        return Fr((n + 3 - x) ** 2 * (n + x + 1) ** 2, (x + 1) ** 4)
    dens = {
        'D1': [(1, 0, 1), (1, 1, 1), (2, 1, 1), (3, 1, 1)],       # (x+1)(n+x+1)(n+x+2)(n+x+3)
        'D2': [(1, 0, 3), (1, 1, 1), (2, 1, 1), (3, 1, 1)],
        'D3': [(1, 0, 4), (1, 1, 2), (2, 1, 2), (3, 1, 2)],
        'D4': [(1, 0, 1)],
        'D5': [],
    }

    def dv(D, x):
        v = 1
        for (c, cn, m) in D:
            v = v * pow((c + cn * n + x) % p, m, p) % p
        return v
    xs = sorted(vals_at)
    for nm, D in dens.items():
        for deg in range(0, degmax + 1):
            nc = deg + 1
            pts = [x for x in xs if dv(D, x) and dv(D, x + 1)][:int(1.4 * nc) + 10]
            if len(pts) < int(1.3 * nc) + 4:
                continue
            A = np.zeros((len(pts), nc), dtype=np.int64)
            b = np.zeros(len(pts), dtype=np.int64)
            for t, x in enumerate(pts):
                gx = Fr((n + 3 - x) ** 2 * (n + x + 1) ** 2, (x + 1) ** 4)
                gxp = gx.numerator % p * pow(gx.denominator % p, p - 2, p) % p
                iD1 = pow(dv(D, x + 1), p - 2, p)
                iD0 = pow(dv(D, x), p - 2, p)
                for j in range(nc):
                    A[t, j] = (gxp * pow((x + 1) % p, j, p) % p * iD1
                               - pow(x % p, j, p) * iD0) % p
                b[t] = vals_at[x] % p
            X, rk, piv, nbad = fastlin.solve(A, b, p)
            if nbad == 0:
                return (nm, deg, rk)
    return None


if __name__ == '__main__':
    p = W.P1
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    B = W.B
    dc = json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
    w = W.to_p([Fr(c) for c in dc['coeffs']], p)
    S = build_joint(n, w, B, 'M0', 8, 'M0', 12, p)
    A1, b1 = class_rows(S, exclude_empty=True)
    L2 = np.concatenate([S['LHS'], A1], axis=0)
    r2 = np.concatenate([S['rhs0'], b1])
    z, rk, piv, nbad = fastlin.solve(L2, r2, p)
    print('joint + 16 non-() (B-bot) classes: %d extra rows, nbad=%d  %s'
          % (A1.shape[0], nbad, 'CONSISTENT' if nbad == 0 else 'INCONSISTENT'), flush=True)
    if nbad:
        sys.exit(1)
    ans0 = S['ans0']; x0 = z[:ans0.nc]
    # rho_()(n,0,l) and sigma_()(n,k,0) as functions of one variable
    NPT = 400
    rho0 = {}
    sig0 = {}
    for x in range(1, NPT):
        if (x + 1) % p and (n + x + 1) % p and (n + 3 - x) % p:
            rho0[x] = ans0.eval_r(x0, n, 0, x, p)
            sig0[x] = ans0.eval_s(x0, n, x, 0, p)
    for nm, vals in (('rho_()(n,0,l)', rho0), ('sigma_()(n,k,0)', sig0)):
        r = gosper_side(n, p, vals, nm)
        print('   %-18s : %s' % (nm, 'GOSPER-SUMMABLE with denominator %s, numerator degree %d'
                                 % (r[0], r[1]) if r else
                                 'NOT summable in the ansatz scanned'), flush=True)
