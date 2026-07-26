"""Cascade solver.  For a fixed prime p and a fixed NUMERIC n, solve the J
scalar WZ problems
      f_i  =  gk * r_i(k+1,l) - r_i(k,l) + gl * s_i(k,l+1) - s_i(k,l)
in decreasing monomial degree, where
      f_i = b_i - sum_j [ gk*(Sk-I)_{ij} r_j(k+1,l) + gl*(Sl-I)_{ij} s_j(k,l+1) ]
and (Sk-I)_{ij} = 0 unless deg(M_j) > deg(M_i)  (unipotence of the shifts).

Ansatz per level:  r_i = Nr_i(k,l)/Dr(n,k,l),  s_i = Ns_i(k,l)/Ds(n,k,l) with
Dr, Ds FIXED products of linear forms and Nr, Ns of bounded bidegree.  The
matrix depends only on the ansatz, so it is factored once per level.
"""
import numpy as np
import zla

# ------------------------------------------------------------ linear forms --
# a linear form is (const, cn, ck, cl)

def lf(f, n, k, l):
    c, cn, ck, cl = f
    return c + cn * n + ck * k + cl * l

def dval(D, n, k, l, p):
    v = 1
    for f, m in D:
        v = v * pow(lf(f, n, k, l) % p, m, p) % p
    return v

# named factors
KL1 = (1, 0, 1, 1); KL2 = (2, 0, 1, 1); KL3 = (3, 0, 1, 1)
NK = [(j, 1, 1, 0) for j in range(0, 6)]      # NK[j] = n+k+j
NL = [(j, 1, 0, 1) for j in range(0, 6)]      # NL[j] = n+l+j
MK = [(j, 1, -1, 0) for j in range(0, 6)]     # MK[j] = n+j-k
ML = [(j, 1, 0, -1) for j in range(0, 6)]     # ML[j] = n+j-l
K1 = (1, 0, 1, 0); L1 = (1, 0, 0, 1)

NAMES = {KL1: 'k+l+1', KL2: 'k+l+2', KL3: 'k+l+3', K1: 'k+1', L1: 'l+1'}
for j in range(6):
    NAMES[NK[j]] = 'n+k+%d' % j; NAMES[NL[j]] = 'n+l+%d' % j
    NAMES[MK[j]] = 'n+%d-k' % j; NAMES[ML[j]] = 'n+%d-l' % j

def dstr(D):
    return '*'.join(NAMES.get(f, str(f)) + ('^%d' % m if m > 1 else '')
                    for f, m in D)

# ---------------------------------------------------------------- ansatz ----

class Ansatz:
    def __init__(self, Dr, Ds, dkr, dlr, dks, dls, force_k=1, force_l=1):
        self.Dr, self.Ds = Dr, Ds
        self.mons_r = [(a, b) for a in range(force_k, dkr + 1)
                       for b in range(0, dlr + 1)]
        self.mons_s = [(a, b) for a in range(0, dks + 1)
                       for b in range(force_l, dls + 1)]
        self.nc = len(self.mons_r) + len(self.mons_s)
        self.par = (dkr, dlr, dks, dls, force_k, force_l)

    def key(self):
        return (tuple(self.Dr), tuple(self.Ds), self.par)

    def __repr__(self):
        return ('Ansatz(Dr=%s, Ds=%s, deg=%s, nc=%d)'
                % (dstr(self.Dr), dstr(self.Ds), self.par, self.nc))

    def eval_r(self, coef, n, k, l, p):
        num = 0
        kk = k % p; ll = l % p
        for t, (a, b) in enumerate(self.mons_r):
            c = coef[t]
            if c: num = (num + c * pow(kk, a, p) % p * pow(ll, b, p)) % p
        return num * pow(dval(self.Dr, n, k, l, p), p - 2, p) % p

    def eval_s(self, coef, n, k, l, p):
        off = len(self.mons_r)
        num = 0
        kk = k % p; ll = l % p
        for t, (a, b) in enumerate(self.mons_s):
            c = coef[off + t]
            if c: num = (num + c * pow(kk, a, p) % p * pow(ll, b, p)) % p
        return num * pow(dval(self.Ds, n, k, l, p), p - 2, p) % p

# --------------------------------------------------------- mod-p lin alg ----

def rref(A, p):
    A = A % p
    rows, cols = A.shape
    perm = np.arange(rows)
    piv, prow, r = [], [], 0
    for c in range(cols):
        if r >= rows: break
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0: continue
        i = r + int(nz[0])
        if i != r:
            A[[r, i]] = A[[i, r]]; perm[[r, i]] = perm[[i, r]]
        A[r] = A[r] * pow(int(A[r, c]), p - 2, p) % p
        col = A[:, c].copy(); col[r] = 0
        nzr = np.nonzero(col)[0]
        if nzr.size:
            A[nzr] = (A[nzr] - col[nzr, None] * A[r][None, :]) % p
        piv.append(c); prow.append(int(perm[r])); r += 1
    return A, piv, prow

def matinv(A, p):
    n = A.shape[0]
    M = np.concatenate([A % p, np.eye(n, dtype=np.int64)], axis=1)
    for c in range(n):
        nz = np.nonzero(M[c:, c])[0]
        if nz.size == 0: return None
        i = c + int(nz[0])
        if i != c: M[[c, i]] = M[[i, c]]
        M[c] = M[c] * pow(int(M[c, c]), p - 2, p) % p
        col = M[:, c].copy(); col[c] = 0
        nzr = np.nonzero(col)[0]
        if nzr.size:
            M[nzr] = (M[nzr] - col[nzr, None] * M[c][None, :]) % p
    return M[:, n:]

def matvec(M, x, p):
    return ((M * x[None, :]) % p).sum(axis=1) % p

# --------------------------------------------------------------- pointdata --

class PointData:
    """the (n,p)-dependent numeric data at all sample points"""
    def __init__(self, which, p, n, npts, seed=12345, extra_forms=(), base=None):
        self.p, self.n, self.which = p, n, which
        self.base = {} if base is None else base
        F = zla.Fp(p); self.F = F
        self.w = zla.weight_element(F, which)
        self.B = zla.closure_basis(self.w)
        self.J = len(self.B)
        self.deg = [len(m) for m in self.B]
        rng = np.random.default_rng(seed + p % 1000003 + 7919 * n)
        pts = []; bad = 0
        while len(pts) < npts:
            k = int(rng.integers(2, p - 2)); l = int(rng.integers(2, p - 2))
            if self._ok(k, l, extra_forms): pts.append((k, l))
            else:
                bad += 1
                if bad > 20000: raise RuntimeError('no sample points')
        self.pts = pts; self.npts = npts
        self._build()

    def _ok(self, k, l, extra):
        p, n = self.p, self.n
        chk = [k + 1, l + 1, k + 2, l + 2, k + 3, l + 3,
               k + l + 1, k + l + 2, k + l + 3, k + l + 4]
        for j in range(0, 7):
            chk += [n + k + j, n + l + j, n + k + l + j, n + j - k, n + j - l]
        for c in chk:
            if c % p == 0: return False
        for f in extra:
            for (kk, ll) in ((k, l), (k + 1, l), (k, l + 1)):
                if lf(f, n, kk, ll) % p == 0: return False
        return True

    def _build(self):
        p, n, F = self.p, self.n, self.F
        J, npts = self.J, self.npts
        self.bvec = np.zeros((npts, J), dtype=np.int64)
        self.Nk = np.zeros((npts, J, J), dtype=np.int64)
        self.Nl = np.zeros((npts, J, J), dtype=np.int64)
        self.gk = np.zeros(npts, dtype=np.int64)
        self.gl = np.zeros(npts, dtype=np.int64)
        for t, (k, l) in enumerate(self.pts):
            self.gk[t] = zla.gk_val(F, n, k, l)
            self.gl[t] = zla.gl_val(F, n, k, l)
            e = zla.rhs_element_mixed(F, self.w, n, k, l, self.base)
            self.bvec[t] = zla.el_to_vec(F, self.B, e)
            for arr, d in ((self.Nk, 'k'), (self.Nl, 'l')):
                cols = zla.shift_matrix_mixed(F, self.B, d, n, k, l, self.base)
                for j in range(J):
                    for i in range(J):
                        arr[t, i, j] = cols[j][i]
                    arr[t, j, j] = (arr[t, j, j] - 1) % p

# ------------------------------------------------------------ level solver --

class LevelSolver:
    def __init__(self, pd, A):
        self.pd, self.A = pd, A
        p, n = pd.p, pd.n
        npts, nc = pd.npts, A.nc
        M = np.zeros((npts, nc), dtype=np.int64)
        nr = len(A.mons_r)
        dmax = max(max(a, b) for a, b in A.mons_r + A.mons_s) + 2
        for t, (k, l) in enumerate(pd.pts):
            gk, gl = int(pd.gk[t]), int(pd.gl[t])
            iDr = pow(dval(A.Dr, n, k, l, p), p - 2, p)
            iDrk = pow(dval(A.Dr, n, k + 1, l, p), p - 2, p)
            iDs = pow(dval(A.Ds, n, k, l, p), p - 2, p)
            iDsl = pow(dval(A.Ds, n, k, l + 1, p), p - 2, p)
            kp = [pow(k % p, a, p) for a in range(dmax)]
            lp = [pow(l % p, b, p) for b in range(dmax)]
            k1p = [pow((k + 1) % p, a, p) for a in range(dmax)]
            l1p = [pow((l + 1) % p, b, p) for b in range(dmax)]
            for j, (a, b) in enumerate(A.mons_r):
                M[t, j] = (gk * k1p[a] % p * lp[b] % p * iDrk
                           - kp[a] * lp[b] % p * iDr) % p
            for j, (a, b) in enumerate(A.mons_s):
                M[t, nr + j] = (gl * kp[a] % p * l1p[b] % p * iDsl
                                - kp[a] * lp[b] % p * iDs) % p
        self.M = M
        _, piv, prow = rref(M.copy(), p)
        self.piv, self.prow = piv, prow
        self.rank = len(piv)
        self.Minv = matinv(M[np.array(prow)][:, np.array(piv)], p)

    def solve(self, rhs):
        p = self.pd.p
        x = np.zeros(self.A.nc, dtype=np.int64)
        x[np.array(self.piv)] = matvec(self.Minv, rhs[np.array(self.prow)], p)
        res = (matvec(self.M, x, p) - rhs) % p
        return x, int(np.count_nonzero(res))

# ---------------------------------------------------------------- cascade ---

def cascade(pd, ansatz_by_deg, topblock=None, order_hint=None):
    """ansatz_by_deg : dict degree -> Ansatz.  topblock : (index, rfun, sfun)
    with rfun(n,k,l) -> int mod p, to hard-wire a known block."""
    p, J, npts = pd.p, pd.J, pd.npts
    solvers = {}
    for d, A in ansatz_by_deg.items():
        key = A.key()
        if key not in solvers: solvers[key] = LevelSolver(pd, A)
    coefs = [None] * J
    fail = {}
    rvals = np.zeros((J, npts), dtype=np.int64)
    svals = np.zeros((J, npts), dtype=np.int64)
    done = np.zeros(J, dtype=bool)
    order = sorted(range(J), key=lambda i: (-pd.deg[i], i))
    for i in order:
        rhs = pd.bvec[:, i].copy()
        for j in range(J):
            if not done[j]: continue
            nk = pd.Nk[:, i, j]
            if nk.any(): rhs = (rhs - pd.gk * nk % p * rvals[j]) % p
            nl = pd.Nl[:, i, j]
            if nl.any(): rhs = (rhs - pd.gl * nl % p * svals[j]) % p
        if topblock is not None and i == topblock[0]:
            rf, sf = topblock[1], topblock[2]
            rv = np.array([rf(pd.n, k + 1, l) % p for (k, l) in pd.pts], dtype=np.int64)
            r0 = np.array([rf(pd.n, k, l) % p for (k, l) in pd.pts], dtype=np.int64)
            sv = np.array([sf(pd.n, k, l + 1) % p for (k, l) in pd.pts], dtype=np.int64)
            s0 = np.array([sf(pd.n, k, l) % p for (k, l) in pd.pts], dtype=np.int64)
            chk = (pd.gk * rv % p - r0 + pd.gl * sv % p - s0 - rhs) % p
            fail[i] = int(np.count_nonzero(chk))
            coefs[i] = 'TOP'; rvals[i], svals[i] = rv, sv; done[i] = True
            continue
        A = ansatz_by_deg[pd.deg[i]]
        LS = solvers[A.key()]
        x, nbad = LS.solve(rhs)
        coefs[i] = x; fail[i] = nbad
        rvals[i] = np.array([A.eval_r(x, pd.n, k + 1, l, p) for (k, l) in pd.pts],
                            dtype=np.int64)
        svals[i] = np.array([A.eval_s(x, pd.n, k, l + 1, p) for (k, l) in pd.pts],
                            dtype=np.int64)
        done[i] = True
    return coefs, fail, solvers
