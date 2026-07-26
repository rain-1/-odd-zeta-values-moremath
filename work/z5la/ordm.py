"""Order-m telescoper search for  T*w :   L = A . L_BZ ,  A = sum_{t=0}^{m-3} a_t S_n^t.

Base is  Phi_m(n,k,l) = T(n+m,k,l) / prod_{j=1..m} (n+j)(n+k+j)(n+l+j)(n+k+l+j),
pole free for n,k,l >= 0, with

    T(n+i,k,l) = Phi_m(n,k,l) * Pm(n,k,l,i,m),      0 <= i <= m,
    Pm = prod_{j=1..i}(n+j)(n+k+j)(n+l+j)(n+k+l+j)
         * [prod_{j=i+1..m}(n+j-k)]^2 [prod_{j=i+1..m}(n+j-l)]^2

    Phi_m(n,k+1,l) (k+1)^3 (k+l+1) = Phi_m(n,k,l) (n+m-k)^2 (n+k+1)(n+k+l+1)
 => gk_m = (n+m-k)^2 (n+k+1)(n+k+l+1) / [ (k+1)^3 (k+l+1) ]        (l mirror)

Q-row cofactor of  S_n^t L_BZ  over the base Phi_m, in CLOSED FORM
(Z5CF_LINALG 6.1a):

    r^(t)(n,k,l) = r_Q(n+t,k,l) * Pm(n,k,l,t,m) / P0_3(n+t,k,l)
    P0_3(N,k,l)  = [ (N+1-k)(N+2-k)(N+3-k) ]^2 [ (N+1-l)(N+2-l)(N+3-l) ]^2

Theorem R then gives the supp(w) blocks as  r_j = w_j * sum_t a_t r^(t),
LINEAR in the unknowns a_t, so the free-coefficient search keeps all of
Theorem R's savings and only the J - |supp(w)| residual blocks are unknown.

MIXED BASE:  the letters H^(r)_{n-k}, H^(r)_{n-l} are normalised at n+m, so
Pm's double zeros prod_{j=a+1..m}(n+j-k)^2 cancel the poles 1/(n+j-k)^r that the
normalisation introduces  (Z5CF_LINALG 5, "also recorded").
"""
import numpy as np
import zla, solve, qrow
from solve import dval

# ------------------------------------------------------------- polynomials --

def Pm_p(n, k, l, i, m, p):
    v = 1
    for j in range(1, i + 1):
        v = v * ((n + j) % p) % p
        v = v * ((n + k + j) % p) % p
        v = v * ((n + l + j) % p) % p
        v = v * ((n + k + l + j) % p) % p
    a = 1; b = 1
    for j in range(i + 1, m + 1):
        a = a * ((n + j - k) % p) % p
        b = b * ((n + j - l) % p) % p
    return v * a % p * a % p * b % p * b % p


def P03_p(N, k, l, p):
    a = 1; b = 1
    for j in (1, 2, 3):
        a = a * ((N + j - k) % p) % p
        b = b * ((N + j - l) % p) % p
    return a * a % p * b % p * b % p


def gkm(F, n, k, l, m):
    return F.frac((n + m - k) ** 2 * (n + k + 1) * (n + k + l + 1),
                  (k + 1) ** 3 * (k + l + 1))


def glm(F, n, k, l, m):
    return F.frac((n + m - l) ** 2 * (n + l + 1) * (n + k + l + 1),
                  (l + 1) ** 3 * (k + l + 1))


# ---------------------------------------------------------- linear forms ----
# (const, cn, ck, cl)
KL1 = (1, 0, 1, 1); KL2 = (2, 0, 1, 1); KL3 = (3, 0, 1, 1); KL4 = (4, 0, 1, 1)
K1 = (1, 0, 1, 0); L1 = (1, 0, 0, 1)
K2 = (2, 0, 1, 0); L2 = (2, 0, 0, 1)
solve.NAMES[KL4] = 'k+l+4'; solve.NAMES[K2] = 'k+2'; solve.NAMES[L2] = 'l+2'
NK = [(j, 1, 1, 0) for j in range(0, 20)]
NL = [(j, 1, 0, 1) for j in range(0, 20)]
MK = [(j, 1, -1, 0) for j in range(0, 20)]
ML = [(j, 1, 0, -1) for j in range(0, 20)]
NKL = [(j, 1, 1, 1) for j in range(0, 20)]
for _j in range(20):
    solve.NAMES[NK[_j]] = 'n+k+%d' % _j
    solve.NAMES[NL[_j]] = 'n+l+%d' % _j
    solve.NAMES[MK[_j]] = 'n+%d-k' % _j
    solve.NAMES[ML[_j]] = 'n+%d-l' % _j
    solve.NAMES[NKL[_j]] = 'n+k+l+%d' % _j


# --------------------------------------------------------------- pointdata --

class PDm:
    """all (n, p, m)-dependent numeric data at the sample points"""

    def __init__(self, which, p, n, m, npts, seed=12345, mixed=True, pts=None):
        assert m >= 3
        if pts is not None: npts = len(pts)
        self.p, self.n, self.m, self.npts, self.which = p, n, m, npts, which
        F = zla.Fp(p); self.F = F
        self.base = {'yk': m, 'yl': m} if mixed else {}
        self.w = zla.weight_element(F, which)
        self.wQ = zla.weight_element(zla.FQ(), which)     # exact constants
        self.B = zla.closure_basis(self.w)
        self.J = J = len(self.B)
        self.deg = [len(x) for x in self.B]
        self.supp = {self.B.index(mm): self.w[mm] for mm in self.w}   # j -> w_j mod p
        self.free = [j for j in range(J) if j not in self.supp]
        self.na = m - 2                                    # a_0 .. a_{m-3}
        rng = np.random.default_rng(seed + p % 1000003 + 7919 * n + 31 * m)
        if pts is not None:
            self.pts = list(pts); self._build(); return
        pts = []; bad = 0
        while len(pts) < npts:
            k = int(rng.integers(2, p - 2)); l = int(rng.integers(2, p - 2))
            if self._ok(k, l):
                pts.append((k, l))
            else:
                bad += 1
                if bad > 100000: raise RuntimeError('no sample points')
        self.pts = pts
        self._build()

    def _ok(self, k, l):
        p, n, m = self.p, self.n, self.m
        chk = [k + 1, l + 1, k + 2, l + 2, k + l + 1, k + l + 2, k + l + 3]
        for j in range(0, m + 6):
            chk += [n + k + j, n + l + j, n + k + l + j, n + j - k, n + j - l]
        for c in chk:
            if c % p == 0: return False
        return True

    def _build(self):
        p, n, m, F = self.p, self.n, self.m, self.F
        J, npts, na = self.J, self.npts, self.na
        self.gk = np.zeros(npts, dtype=np.int64)
        self.gl = np.zeros(npts, dtype=np.int64)
        self.Sk = np.zeros((npts, J, J), dtype=np.int64)
        self.Sl = np.zeros((npts, J, J), dtype=np.int64)
        self.V = np.zeros((npts, J, na), dtype=np.int64)
        for t, (k, l) in enumerate(self.pts):
            self.gk[t] = gkm(F, n, k, l, m)
            self.gl[t] = glm(F, n, k, l, m)
            for arr, d in ((self.Sk, 'k'), (self.Sl, 'l')):
                cols = zla.shift_matrix_mixed(F, self.B, d, n, k, l, self.base)
                for j in range(J):
                    for i in range(J):
                        arr[t, i, j] = cols[j][i]
            for tt in range(na):
                C = zla.cc(n + tt)
                el = {}
                for u in range(4):
                    co = F.mul(F.cst(C[u]), Pm_p(n, k, l, tt + u, m, p))
                    el = zla.el_add(F, el,
                                    zla.w_shift_mixed(F, self.w, tt + u, n, k, l, self.base),
                                    co)
                v = zla.el_to_vec(F, self.B, el)
                for i in range(J):
                    self.V[t, i, tt] = v[i]
        # closed-form Q-row cofactors of S^t L_BZ over Phi_m
        self.r0 = np.zeros((npts, na), dtype=np.int64)
        self.r1 = np.zeros((npts, na), dtype=np.int64)
        self.s0 = np.zeros((npts, na), dtype=np.int64)
        self.s1 = np.zeros((npts, na), dtype=np.int64)
        for tt in range(na):
            rf, sf = qrow.make_evals(n + tt, p)
            N = n + tt
            for t, (k, l) in enumerate(self.pts):
                f00 = Pm_p(n, k, l, tt, m, p) * pow(P03_p(N, k, l, p), p - 2, p) % p
                fk1 = Pm_p(n, k + 1, l, tt, m, p) * pow(P03_p(N, k + 1, l, p), p - 2, p) % p
                fl1 = Pm_p(n, k, l + 1, tt, m, p) * pow(P03_p(N, k, l + 1, p), p - 2, p) % p
                self.r0[t, tt] = rf(0, k, l) * f00 % p
                self.r1[t, tt] = rf(0, k + 1, l) * fk1 % p
                self.s0[t, tt] = sf(0, k, l) * f00 % p
                self.s1[t, tt] = sf(0, k, l + 1) * fl1 % p


# ------------------------------------------------------------ the a-columns --

def acols(pd):
    """Acol[i*npts+t, tt] = the coefficient of a_tt in
         (Theorem-R fixed blocks' contribution) - V_tt,i
    i.e. everything in the row that is linear in a."""
    p, J, npts, na = pd.p, pd.J, pd.npts, pd.na
    A = np.zeros((J * npts, na), dtype=np.int64)
    eyeJ = np.eye(J, dtype=np.int64)
    for t in range(npts):
        gk = int(pd.gk[t]); gl = int(pd.gl[t])
        Sk = pd.Sk[t]; Sl = pd.Sl[t]
        for i in range(J):
            row = i * npts + t
            acc = np.zeros(na, dtype=np.int64)
            for j, wj in pd.supp.items():
                a = int(Sk[i, j]); b = int(Sl[i, j])
                if a: acc = (acc + gk * a % p * (wj * pd.r1[t] % p)) % p
                if b: acc = (acc + gl * b % p * (wj * pd.s1[t] % p)) % p
            if i in pd.supp:
                wi = pd.supp[i]
                acc = (acc - wi * (pd.r0[t] + pd.s0[t]) % p) % p
            A[row] = (acc - pd.V[t, i]) % p
    return A


def freecols(pd, ans):
    """the cofactor columns for the FREE blocks (Theorem R fixes the rest)."""
    p, n, J, npts = pd.p, pd.n, pd.J, pd.npts
    nc = ans.nc; nr = len(ans.mons_r)
    free = pd.free
    pos = {j: t for t, j in enumerate(free)}
    M = np.zeros((J * npts, len(free) * nc), dtype=np.int64)
    dmax = max(max(a, b) for a, b in ans.mons_r + ans.mons_s) + 2
    for t, (k, l) in enumerate(pd.pts):
        gk = int(pd.gk[t]); gl = int(pd.gl[t])
        iDr = pow(dval(ans.Dr, n, k, l, p), p - 2, p)
        iDrk = pow(dval(ans.Dr, n, k + 1, l, p), p - 2, p)
        iDs = pow(dval(ans.Ds, n, k, l, p), p - 2, p)
        iDsl = pow(dval(ans.Ds, n, k, l + 1, p), p - 2, p)
        kp = [pow(k % p, a, p) for a in range(dmax)]
        lp = [pow(l % p, b, p) for b in range(dmax)]
        k1 = [pow((k + 1) % p, a, p) for a in range(dmax)]
        l1 = [pow((l + 1) % p, b, p) for b in range(dmax)]
        vr1 = np.array([k1[a] * lp[b] % p * iDrk % p for a, b in ans.mons_r], dtype=np.int64)
        vr0 = np.array([kp[a] * lp[b] % p * iDr % p for a, b in ans.mons_r], dtype=np.int64)
        vs1 = np.array([kp[a] * l1[b] % p * iDsl % p for a, b in ans.mons_s], dtype=np.int64)
        vs0 = np.array([kp[a] * lp[b] % p * iDs % p for a, b in ans.mons_s], dtype=np.int64)
        Sk = pd.Sk[t]; Sl = pd.Sl[t]
        for i in range(J):
            row = i * npts + t
            for j in free:
                a = int(Sk[i, j]); b = int(Sl[i, j])
                base = pos[j] * nc
                if a: M[row, base:base + nr] = gk * a % p * vr1 % p
                if b: M[row, base + nr:base + nc] = gl * b % p * vs1 % p
            if i in pos:
                b0 = pos[i] * nc
                M[row, b0:b0 + nr] = (M[row, b0:b0 + nr] - vr0) % p
                M[row, b0 + nr:b0 + nc] = (M[row, b0 + nr:b0 + nc] - vs0) % p
    return M


# ------------------------------------------------------------- diagnostics --

def qrow_selftest(p, n, m, npts=40):
    """for w = 1 the identity  sum_u c_u(n+t) Pm(n,k,l,t+u,m)
         =  gk_m r^(t)(k+1,l) - r^(t)(k,l) + gl_m s^(t)(k,l+1) - s^(t)(k,l)
    must hold EXACTLY for every t = 0..m-3.  This validates Pm, gk_m, r^(t)."""
    pd = PDm('q0', p, n, m, npts)
    bad = 0
    for t in range(npts):
        gk = int(pd.gk[t]); gl = int(pd.gl[t])
        for tt in range(pd.na):
            lhs = int(pd.V[t, 0, tt])
            rhs = (gk * int(pd.r1[t, tt]) - int(pd.r0[t, tt])
                   + gl * int(pd.s1[t, tt]) - int(pd.s0[t, tt])) % p
            if (lhs - rhs) % p: bad += 1
    return bad, npts * pd.na


def theoremR_selftest(which, p, n, m, npts=40, seed=7):
    """with the free blocks 0 and the supp(w) blocks r_j = w_j sum_t a_t r^(t),
    the supp(w) components of the residual must vanish for EVERY a."""
    pd = PDm(which, p, n, m, npts)
    A = acols(pd)
    rng = np.random.default_rng(seed)
    a = rng.integers(1, p, size=pd.na)
    res = (A.astype(object) @ a.astype(object)) % p
    out = {}
    for i in range(pd.J):
        out[pd.B[i]] = int(np.count_nonzero(res[i * npts:(i + 1) * npts]))
    return pd, out
