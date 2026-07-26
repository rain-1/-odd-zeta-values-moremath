"""The last residual block, ('()',).  Its equation couples to every other block,
so it is solved AFTER the seven standalone ones -- but the representative chosen
for those is only unique modulo the kernel of the scalar operator (the 'trivial
pairs' of Z5CF_LINALG 4), and that kernel freedom must be offered to the ()
equation or the cascade poisons it.  Here it is offered explicitly."""
import sys, time
import numpy as np
import zla, solve, fastlin, ratrec, ordm, o_scan
from solve import Ansatz, dval

CH = 256


def matmul_mod(A, B, p, ch=CH):
    """(rows x K) @ (K x C) mod p, exactly, via float64 BLAS in K-chunks."""
    A = np.asarray(A, dtype=np.float64) % p
    B = np.asarray(B, dtype=np.float64) % p
    K = A.shape[1]
    out = np.zeros((A.shape[0], B.shape[1]))
    for i in range(0, K, ch):
        out = (out + A[:, i:i + ch] @ B[i:i + ch]) % p
    return out


def design(pd, ans):
    """R0,R1,S0,S1 with  r(k,l) = R0 x,  r(k+1,l) = R1 x,  s(k,l) = S0 x,
    s(k,l+1) = S1 x,  and the scalar operator M = gk R1 - R0 + gl S1 - S0."""
    p, n, npts, nc = pd.p, pd.n, pd.npts, ans.nc
    nr = len(ans.mons_r)
    R0 = np.zeros((npts, nc)); R1 = np.zeros((npts, nc))
    S0 = np.zeros((npts, nc)); S1 = np.zeros((npts, nc))
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
            R0[t, u] = kp[a] * lp[b] % p * iDr % p
            R1[t, u] = k1[a] * lp[b] % p * iDrk % p
        for u, (a, b) in enumerate(ans.mons_s):
            S0[t, nr + u] = kp[a] * lp[b] % p * iDs % p
            S1[t, nr + u] = kp[a] * l1[b] % p * iDsl % p
    gk = pd.gk.astype(np.float64)[:, None]
    gl = pd.gl.astype(np.float64)[:, None]
    M = ((gk * R1) % p - R0 + (gl * S1) % p - S0) % p
    return R0, R1, S0, S1, M


def kernel_basis(M, p, nfit, nb=64):
    """basis of ker(M[:nfit]) as columns of a (nc x nk) array."""
    nc = M.shape[1]
    A = M[:nfit]
    G = np.array(A, dtype=np.float64) % p
    rank, piv = fastlin.elim(G, p, nc, nb)
    freec = [c for c in range(nc) if c not in set(piv)]
    B = (-A[:, freec]) % p
    X, rk, pv, nbad = fastlin.solve(A, B.astype(np.int64), p, nb=nb)
    K = np.zeros((nc, len(freec)))
    K[:, :] = X % p
    for j, c in enumerate(freec):
        K[c, j] = (K[c, j] + 1) % p
    return K, rank


def run(which, n, m, dname, slack, dname0, slack0, p=o_scan.P, avec=None,
        nchk=300, kern=True, verbose=True):
    D = o_scan.dens(m)[dname]
    dk0 = sum(mu * abs(f[2]) for f, mu in D); dl0 = sum(mu * abs(f[3]) for f, mu in D)
    ans = Ansatz(D, D, dk0 + slack, dl0 + slack, dk0 + slack, dl0 + slack,
                 force_k=0, force_l=0)
    D0 = o_scan.dens(m)[dname0]
    ek0 = sum(mu * abs(f[2]) for f, mu in D0); el0 = sum(mu * abs(f[3]) for f, mu in D0)
    ans0 = Ansatz(D0, D0, ek0 + slack0, el0 + slack0, ek0 + slack0, el0 + slack0,
                  force_k=0, force_l=0)
    na = m - 2
    nfit = int(1.35 * (ans.nc + na)) + 20
    nk_guess = ans.nc - int(0.66 * ans.nc)
    ncol0 = ans0.nc + (7 * nk_guess if kern else 0)
    nfit0 = int(1.35 * ncol0) + 20
    npts = max(nfit, nfit0) + nchk
    t0 = time.time()
    pd = ordm.PDm(which, p, n, m, npts)
    Acol = ordm.acols(pd)
    stand = [j for j in pd.free if len(pd.B[j]) > 0]
    zj = [j for j in pd.free if len(pd.B[j]) == 0][0]
    R0, R1, S0, S1, M = design(pd, ans)
    if avec is None:
        As = [Acol[i * npts:i * npts + nfit] for i in stand]
        subs, rank = o_scan.asubspaces(M[:nfit].astype(np.int64), As, p)
        inter = o_scan.intersect(subs, na, p)
        if len(inter) != 1:
            print('  a-direction not unique (%d)' % len(inter)); return None
        avec = np.array(inter[0], dtype=np.int64) % p
    avec = np.asarray(avec, dtype=np.int64) % p
    if verbose:
        print('  a = %s   [%.0fs setup]' % ([int(x) for x in avec], time.time() - t0),
              flush=True)
    # --- particular solutions of the seven standalone blocks ---
    rhsS = np.zeros((npts, len(stand)))
    for u, j in enumerate(stand):
        rhsS[:, u] = (-(Acol[j * npts:(j + 1) * npts].astype(object)
                        @ avec.astype(object))) % p
    X, rank, piv, nbad = fastlin.solve(M[:nfit].astype(np.int64),
                                       rhsS[:nfit].astype(np.int64), p, nb=64)
    if verbose:
        print('  seven standalone blocks: rank=%d nbad=%d' % (rank, nbad), flush=True)
    if nbad: return None
    K, _ = kernel_basis(M, p, nfit) if kern else (np.zeros((ans.nc, 0)), rank)
    nk = K.shape[1]
    # --- the () equation ---
    R0z, R1z, S0z, S1z, Mz = design(pd, ans0)
    gk = pd.gk.astype(np.float64)[:, None]; gl = pd.gl.astype(np.float64)[:, None]
    rhs = (-(Acol[zj * npts:(zj + 1) * npts].astype(object) @ avec.astype(object))) % p
    rhs = np.array([int(x) for x in rhs], dtype=np.float64)
    cols = [Mz]
    r1p = matmul_mod(R1, X, p)          # npts x 7   particular r_j(k+1,l)
    s1p = matmul_mod(S1, X, p)
    r1k = matmul_mod(R1, K, p) if nk else None   # npts x nk
    s1k = matmul_mod(S1, K, p) if nk else None
    for u, j in enumerate(stand):
        ck = pd.Sk[:, zj, j].astype(np.float64)[:, None]
        cl = pd.Sl[:, zj, j].astype(np.float64)[:, None]
        rhs = (rhs - ((gk[:, 0] * ck[:, 0]) % p * r1p[:, u]) % p
               - ((gl[:, 0] * cl[:, 0]) % p * s1p[:, u]) % p) % p
        if nk:
            cols.append((((gk * ck) % p) * r1k + ((gl * cl) % p) * s1k) % p)
    G = np.concatenate(cols, axis=1) % p
    ncol = G.shape[1]
    nfit0 = min(npts - nchk, int(1.35 * ncol) + 20)
    Xz, rankz, pivz, nbadz = fastlin.solve(G[:nfit0].astype(np.int64),
                                           rhs[:nfit0].astype(np.int64), p, nb=64)
    if verbose:
        print('  () block: ansatz %s deg=(%d,%d) nc0=%d + %d kernel cols = %d cols, '
              '%d rows (ratio %.2f) -> rank=%d nbad=%d %s'
              % (dname0, ek0 + slack0, el0 + slack0, ans0.nc, ncol - ans0.nc, ncol,
                 nfit0, nfit0 / ncol, rankz, nbadz,
                 '*** SOLVED ***' if nbadz == 0 else ''), flush=True)
    # --- fresh-point residual of the () equation ---
    chk = npts - nfit0
    res = (matmul_mod(G[nfit0:], Xz.reshape(-1, 1).astype(np.float64), p)[:, 0]
           - rhs[nfit0:]) % p
    if verbose:
        print('  () fresh-point check on %d unused points: %d violations  [%.0fs]'
              % (chk, int(np.count_nonzero(res)), time.time() - t0), flush=True)
    return dict(a=avec, nbad0=nbadz, fresh=int(np.count_nonzero(res)), nchk=chk,
                Xstand=X, Xz=Xz, K=K, pd=pd, ans=ans, ans0=ans0)


if __name__ == '__main__':
    which = sys.argv[1]; n = int(sys.argv[2]); m = int(sys.argv[3])
    run(which, n, m, sys.argv[4], int(sys.argv[5]), sys.argv[6], int(sys.argv[7]),
        p=int(sys.argv[8]) if len(sys.argv) > 8 else o_scan.P)
