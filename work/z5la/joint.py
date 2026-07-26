"""Full joint system:  for every basis component i and every sample point,
   sum_j [ gk*Sk[i][j]*r_j(k+1,l) + gl*Sl[i][j]*s_j(k,l+1) ] - r_i - s_i
   =  sum_{a} d_a * (P_a(n,k,l) * w(n+a,k,l))_i
with the d_a either FIXED to c_a(n) (test: does L_BZ admit a certificate?) or
left as unknowns (test: what is the telescoper?).
"""
import numpy as np
import zla, solve
from solve import dval


def build(pd, A, mord=3, free_d=False):
    """returns (M, rhs, ncols, info)"""
    p, n, J, npts = pd.p, pd.n, pd.J, pd.npts
    F = pd.F
    nc = A.nc
    nblk = J
    nd = (mord + 1) if free_d else 0
    ncols = nblk * nc + nd
    rows = J * npts
    M = np.zeros((rows, ncols), dtype=np.int64)
    rhs = np.zeros(rows, dtype=np.int64)
    nr = len(A.mons_r)
    # per-point: the w(n+a) expansions
    for t, (k, l) in enumerate(pd.pts):
        gk, gl = int(pd.gk[t]), int(pd.gl[t])
        iDr = pow(dval(A.Dr, n, k, l, p), p - 2, p)
        iDrk = pow(dval(A.Dr, n, k + 1, l, p), p - 2, p)
        iDs = pow(dval(A.Ds, n, k, l, p), p - 2, p)
        iDsl = pow(dval(A.Ds, n, k, l + 1, p), p - 2, p)
        dmax = max(max(a, b) for a, b in A.mons_r + A.mons_s) + 2
        kp = [pow(k % p, a, p) for a in range(dmax)]
        lp = [pow(l % p, b, p) for b in range(dmax)]
        k1p = [pow((k + 1) % p, a, p) for a in range(dmax)]
        l1p = [pow((l + 1) % p, b, p) for b in range(dmax)]
        Sk = (pd.Nk[t] + np.eye(J, dtype=np.int64)) % p
        Sl = (pd.Nl[t] + np.eye(J, dtype=np.int64)) % p
        # r-monomial values shifted / unshifted
        vr1 = np.array([k1p[a] * lp[b] % p * iDrk % p for (a, b) in A.mons_r],
                       dtype=np.int64)
        vr0 = np.array([kp[a] * lp[b] % p * iDr % p for (a, b) in A.mons_r],
                       dtype=np.int64)
        vs1 = np.array([kp[a] * l1p[b] % p * iDsl % p for (a, b) in A.mons_s],
                       dtype=np.int64)
        vs0 = np.array([kp[a] * lp[b] % p * iDs % p for (a, b) in A.mons_s],
                       dtype=np.int64)
        for i in range(J):
            row = i * npts + t
            for j in range(J):
                skij = int(Sk[i, j]); slij = int(Sl[i, j])
                base = j * nc
                if skij:
                    M[row, base:base + nr] = gk * skij % p * vr1 % p
                if slij:
                    M[row, base + nr:base + nc] = gl * slij % p * vs1 % p
            # diagonal -r_i - s_i
            bi = i * nc
            M[row, bi:bi + nr] = (M[row, bi:bi + nr] - vr0) % p
            M[row, bi + nr:bi + nc] = (M[row, bi + nr:bi + nc] - vs0) % p
        if free_d:
            for a in range(mord + 1):
                el = zla.w_shift_n(F, pd.w, a, n, k, l)
                Pa = F.cst(zla.Pi(n, k, l, a))
                v = zla.el_to_vec(F, pd.B, zla.el_scale(F, el, Pa))
                for i in range(J):
                    M[i * npts + t, nblk * nc + a] = (-v[i]) % p
        else:
            for i in range(J):
                rhs[i * npts + t] = pd.bvec[t, i]
    return M, rhs, ncols
