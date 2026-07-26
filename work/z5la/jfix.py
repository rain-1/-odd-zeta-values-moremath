"""Joint system with some blocks FIXED to known values.

Structural fact:  writing  E_w = sum_a c_a T(n+a) w(n+a)  and using the CERTIFIED
Q-row pair (rho_Q, sigma_Q) with  L_BZ.T = D_k(rho_Q T) + D_l(sigma_Q T),
    E_w = D_k(rho_Q T w) + D_l(sigma_Q T w) + G,
    G := sum_a c_a T(n+a)[w(n+a)-w]
         - rho_Q(k+1)T(k+1)[w(k+1)-w] - sigma_Q(l+1)T(l+1)[w(l+1)-w]
and every bracket has STRICTLY smaller module degree (unipotence).  Hence the
top-degree cofactors are forced: r_j = w_j * r_Q, s_j = w_j * s_Q for every
monomial M_j in the support of w, and only the lower-degree blocks are unknown.
"""
import numpy as np
import zla, solve
from solve import dval

def build(pd, A, free, fixed_r, fixed_s):
    """free: list of block indices to solve for.
    fixed_r[j], fixed_s[j]: dict j -> (r0, r1, s0, s1) arrays over sample points
        r0=r_j(k,l), r1=r_j(k+1,l), s0=s_j(k,l), s1=s_j(k,l+1)"""
    p, n, J, N = pd.p, pd.n, pd.J, pd.npts
    nc = A.nc; nr = len(A.mons_r)
    pos = {j: t for t, j in enumerate(free)}
    ncols = len(free) * nc
    M = np.zeros((J * N, ncols), dtype=np.int64)
    rhs = np.zeros(J * N, dtype=np.int64)
    dmax = max(max(a, b) for a, b in A.mons_r + A.mons_s) + 2
    for t, (k, l) in enumerate(pd.pts):
        gk, gl = int(pd.gk[t]), int(pd.gl[t])
        iDr = pow(dval(A.Dr, n, k, l, p), p - 2, p)
        iDrk = pow(dval(A.Dr, n, k + 1, l, p), p - 2, p)
        iDs = pow(dval(A.Ds, n, k, l, p), p - 2, p)
        iDsl = pow(dval(A.Ds, n, k, l + 1, p), p - 2, p)
        kp = [pow(k % p, a, p) for a in range(dmax)]; lp = [pow(l % p, b, p) for b in range(dmax)]
        k1 = [pow((k+1) % p, a, p) for a in range(dmax)]; l1 = [pow((l+1) % p, b, p) for b in range(dmax)]
        vr1 = np.array([k1[a]*lp[b] % p*iDrk % p for a, b in A.mons_r], dtype=np.int64)
        vr0 = np.array([kp[a]*lp[b] % p*iDr % p for a, b in A.mons_r], dtype=np.int64)
        vs1 = np.array([kp[a]*l1[b] % p*iDsl % p for a, b in A.mons_s], dtype=np.int64)
        vs0 = np.array([kp[a]*lp[b] % p*iDs % p for a, b in A.mons_s], dtype=np.int64)
        Sk = (pd.Nk[t] + np.eye(J, dtype=np.int64)) % p
        Sl = (pd.Nl[t] + np.eye(J, dtype=np.int64)) % p
        for i in range(J):
            row = i*N + t
            acc = int(pd.bvec[t, i])
            for j in range(J):
                skij = int(Sk[i, j]); slij = int(Sl[i, j])
                if j in pos:
                    base = pos[j]*nc
                    if skij: M[row, base:base+nr] = gk*skij % p*vr1 % p
                    if slij: M[row, base+nr:base+nc] = gl*slij % p*vs1 % p
                else:
                    if skij: acc = (acc - gk*skij % p*int(fixed_r[j][1][t])) % p
                    if slij: acc = (acc - gl*slij % p*int(fixed_s[j][1][t])) % p
            if i in pos:
                b0 = pos[i]*nc
                M[row, b0:b0+nr] = (M[row, b0:b0+nr] - vr0) % p
                M[row, b0+nr:b0+nc] = (M[row, b0+nr:b0+nc] - vs0) % p
            else:
                acc = (acc + int(fixed_r[i][0][t]) + int(fixed_s[i][0][t])) % p
            rhs[row] = acc % p
    return M, rhs
