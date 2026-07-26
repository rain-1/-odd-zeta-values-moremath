"""Point data and the certificate-system matrices for  L = L_BZ  (order 3,
m = 3, a = (1))  acting on  T * w  with  w  a FREE vector in the bare weight-5
span.

Base (Z5CF_TELESCOPER 1, m = 3):
    Phi(n,k,l) = T(n+3,k,l) / prod_{j=1..3}(n+j)(n+k+j)(n+l+j)(n+k+l+j)
    T(n+i,k,l) = Phi * Pm(n,k,l,i,3)
    gk = (n+3-k)^2 (n+k+1)(n+k+l+1) / [ (k+1)^3 (k+l+1) ]        (l mirror)
    r^(0) = r_Q(n,k,l)  exactly  (Pm(.,0,3) = P03(n,.) so the quotient is 1)

MIXED BASE: H^(r)_{n-k}, H^(r)_{n-l} normalised at n+3.

The block-M equation is
    gk rho_M(k+1,l) - rho_M + gl sigma_M(k,l+1) - sigma_M  =  A_M(k,l) . w
with A_M KNOWN and LINEAR in w -- for the STANDALONE blocks, i.e. those whose
every strict multiple is maximal (Theorem R).  At weight 5, degree <= 3 those
are the 261 degree-2 blocks; each has an up-set of exactly 10 monomials.
"""
import sys, time
import numpy as np

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import zla, solve, fastlin, ratrec, ordm, qrow
from solve import Ansatz, dval
import w5span as W

P1 = 4194301
P2 = 4194287
M = 3                      # the operator is L_BZ itself: order 3, base Phi_3


# ------------------------------------------------------------------ ansatz ---

def dens(m=M):
    """denominator families.  ordm.NK[j] = n+k+j etc.
    G* are built from the MEASURED standalone-block RHS denominators
    (poles5.py, n = 9, p = 4194301, exact univariate reconstruction):
       k-side  (k+1)^3 (k+l+1)^4 (k+l+2) prod_{j=1..3}(n+k+j)^2 (n+k+l+j)^2 (n+j-k)
       l-side  mirror
    """
    K1, L1 = ordm.K1, ordm.L1
    NK, NL, NKL, MK, ML = ordm.NK, ordm.NL, ordm.NKL, ordm.MK, ordm.ML
    KL = [(j, 0, 1, 1) for j in range(0, 14)]
    for _j in range(14):
        solve.NAMES[KL[_j]] = 'k+l+%d' % _j
    out = {}
    # F1 -- the weight-3 family of Z5CF_REP 3 (kept for cross-calibration)
    out['F1'] = [(K1, 2), (L1, 2)] \
        + [(KL[j], 1) for j in range(1, m + 3)] \
        + [(NK[j], 2) for j in range(1, m + 1)] + [(NL[j], 2) for j in range(1, m + 1)] \
        + [(NKL[j], 1) for j in range(1, m + 1)]
    # H0 -- deliberately SMALL: the low rung of the adequacy ladder
    out['H0'] = [(K1, 2), (L1, 2), (KL[1], 2), (KL[2], 1)] \
        + [(NK[j], 1) for j in range(1, m + 1)] + [(NL[j], 1) for j in range(1, m + 1)] \
        + [(NKL[j], 1) for j in range(1, m + 1)]
    # H1 -- the measured denominators, padded by one on every family
    out['H1'] = [(K1, 3), (L1, 3), (KL[1], 4), (KL[2], 2), (KL[3], 1), (KL[4], 1)] \
        + [(NK[j], 2) for j in range(1, m + 1)] + [(NL[j], 2) for j in range(1, m + 1)] \
        + [(NKL[j], 2) for j in range(1, m + 1)] \
        + [(MK[j], 1) for j in range(1, m + 1)] + [(ML[j], 1) for j in range(1, m + 1)]
    # H2 -- generous
    out['H2'] = [(K1, 4), (L1, 4), (KL[1], 5), (KL[2], 3), (KL[3], 2), (KL[4], 1),
                 (KL[5], 1)] \
        + [(NK[j], 3) for j in range(1, m + 2)] + [(NL[j], 3) for j in range(1, m + 2)] \
        + [(NKL[j], 3) for j in range(1, m + 1)] \
        + [(MK[j], 1) for j in range(0, m + 2)] + [(ML[j], 1) for j in range(0, m + 2)]
    return out


def ansatz(dname, slack, m=M):
    D = dens(m)[dname]
    dk0 = sum(mu * abs(f[2]) for f, mu in D)
    dl0 = sum(mu * abs(f[3]) for f, mu in D)
    return Ansatz(D, D, dk0 + slack, dl0 + slack, dk0 + slack, dl0 + slack,
                  force_k=0, force_l=0), dk0 + slack, dl0 + slack


# -------------------------------------------------------------- point data ---

class PD5:
    def __init__(self, p, n, npts, B, seed=4242, pts=None, m=M):
        self.p, self.n, self.m, self.B = p, n, m, B
        self.J = len(B)
        if pts is not None:
            self.pts = list(pts); self.npts = len(pts)
        else:
            rng = np.random.default_rng(seed + p % 1000003 + 7919 * n)
            got = []; bad = 0
            while len(got) < npts:
                k = int(rng.integers(2, p - 2)); l = int(rng.integers(2, p - 2))
                if self._ok(k, l):
                    got.append((k, l))
                else:
                    bad += 1
                    if bad > 400000:
                        raise RuntimeError('no sample points')
            self.pts = got; self.npts = npts
        self._build()

    def _ok(self, k, l):
        p, n, m = self.p, self.n, self.m
        chk = [k, l, k + 1, l + 1, k + 2, l + 2, k + 3, l + 3]
        for j in range(0, m + 9):
            chk += [k + l + j, n + k + j, n + l + j, n + k + l + j,
                    n + j - k, n + j - l, n + j]
        for c in chk:
            if c % p == 0:
                return False
        return True

    def _build(self):
        p, n, m, B = self.p, self.n, self.m, self.B
        npts, J = self.npts, self.J
        F = zla.Fp(p)
        letters = sorted({L for mm in B for L in mm})
        self.letters = letters
        li = {L: i for i, L in enumerate(letters)}
        self.li = li
        nl = len(letters)
        self.gk = np.zeros(npts, dtype=np.int64)
        self.gl = np.zeros(npts, dtype=np.int64)
        self.incn = np.zeros((npts, nl, m + 1), dtype=np.int64)
        self.inck = np.zeros((npts, nl), dtype=np.int64)
        self.incl = np.zeros((npts, nl), dtype=np.int64)
        self.PM = np.zeros((npts, m + 1), dtype=np.int64)
        self.RQ1 = np.zeros(npts, dtype=np.int64)      # r_Q(n,k+1,l)
        self.SQ1 = np.zeros(npts, dtype=np.int64)      # s_Q(n,k,l+1)
        self.RQ0 = np.zeros(npts, dtype=np.int64)      # r_Q(n,k,l)
        self.SQ0 = np.zeros(npts, dtype=np.int64)
        self.QR = np.zeros(npts, dtype=np.int64)       # sum_u c_u(n) Pm(u)
        cc = zla.cc(n)
        self.cc = cc
        rf, sf = qrow.make_evals(n, p)

        def inv(x):
            return pow(int(x) % p, p - 2, p)

        def hstep(r, x):
            return inv(pow((x + 1) % p, r, p))

        for t, (k, l) in enumerate(self.pts):
            self.gk[t] = int(ordm.gkm(F, n, k, l, m))
            self.gl[t] = int(ordm.glm(F, n, k, l, m))
            for i in range(m + 1):
                self.PM[t, i] = ordm.Pm_p(n, k, l, i, m, p)
            for L in letters:
                r, a = W.LETTERS[L]
                cn, ck, cl = W.ARGS[a]
                d = W.delta(L, m)
                i = li[L]
                for aa in range(m + 1):
                    tot = 0
                    if cn:
                        if aa > d:
                            for ii in range(d, aa):
                                tot = (tot + hstep(r, cn * (n + ii) + ck * k + cl * l)) % p
                        elif aa < d:
                            for ii in range(aa, d):
                                tot = (tot - hstep(r, cn * (n + ii) + ck * k + cl * l)) % p
                    self.incn[t, i, aa] = tot
                xb = cn * (n + d) + ck * k + cl * l
                self.inck[t, i] = (hstep(r, xb) if ck == 1 else
                                   (-inv(pow(xb % p, r, p)) % p if ck == -1 else 0))
                self.incl[t, i] = (hstep(r, xb) if cl == 1 else
                                   (-inv(pow(xb % p, r, p)) % p if cl == -1 else 0))
            self.RQ1[t] = rf(0, k + 1, l)
            self.SQ1[t] = sf(0, k, l + 1)
            self.RQ0[t] = rf(0, k, l)
            self.SQ0[t] = sf(0, k, l)
            q = 0
            for u in range(4):
                q = (q + (cc[u] % p) * int(self.PM[t, u])) % p
            self.QR[t] = q


# -------------------------------------------------------- system matrices ----

def scal_mat(pd, ans):
    """gk r(k+1,l) - r + gl s(k,l+1) - s  in the ansatz basis (npts x nc)."""
    p, n, npts = pd.p, pd.n, pd.npts
    nc, nr = ans.nc, len(ans.mons_r)
    Mx = np.zeros((npts, nc), dtype=np.int64)
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
        for u, (a, b) in enumerate(ans.mons_r):
            Mx[t, u] = (gk * k1[a] % p * lp[b] % p * iDrk - kp[a] * lp[b] % p * iDr) % p
        for u, (a, b) in enumerate(ans.mons_s):
            Mx[t, nr + u] = (gl * kp[a] % p * l1[b] % p * iDsl - kp[a] * lp[b] % p * iDs) % p
    return Mx


def evalmats(pd, ans):
    p, n, npts = pd.p, pd.n, pd.npts
    nr, ns = len(ans.mons_r), len(ans.mons_s)
    R1 = np.zeros((npts, nr), dtype=np.int64); R0 = np.zeros((npts, nr), dtype=np.int64)
    S1 = np.zeros((npts, ns), dtype=np.int64); S0 = np.zeros((npts, ns), dtype=np.int64)
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
            R1[t, u] = k1[a] * lp[b] % p * iDrk % p
            R0[t, u] = kp[a] * lp[b] % p * iDr % p
        for u, (a, b) in enumerate(ans.mons_s):
            S1[t, u] = kp[a] * l1[b] % p * iDsl % p
            S0[t, u] = kp[a] * lp[b] % p * iDs % p
    return R1, R0, S1, S0


def mv(Mx, x, p):
    x = np.asarray(x, dtype=np.int64) % p
    out = np.zeros(Mx.shape[0], dtype=np.int64)
    blk = 400
    for i in range(0, Mx.shape[1], blk):
        out = (out + (Mx[:, i:i + blk].astype(np.float64)
                      @ x[i:i + blk].astype(np.float64)).astype(np.int64)) % p
    return out


def shiftpair(pd, rest):
    p = pd.p
    ids = [pd.li[x] for x in rest]
    sk = np.ones(pd.npts, dtype=np.int64)
    sl = np.ones(pd.npts, dtype=np.int64)
    for i in ids:
        sk = sk * pd.inck[:, i] % p
        sl = sl * pd.incl[:, i] % p
    return sk, sl


def Ecol(pd, rest):
    """the (E_{M_i.rest}/Phi)_{M_i} column: sum_u c_u(n) PM[u] prod_{rest} incn[.,u]"""
    p = pd.p
    ids = [pd.li[x] for x in rest]
    col = np.zeros(pd.npts, dtype=np.int64)
    for u in range(4):
        pr = pd.PM[:, u].copy()
        for i in ids:
            pr = pr * pd.incn[:, i, u] % p
        col = (col + (pd.cc[u] % p) * pr) % p
    return col


def Acols_standalone(pd, B, stand, us):
    """for each standalone block j in `stand`, the compressed npts x |up| matrix
    of the coefficient of w restricted to up(M_j), and the column index list."""
    p = pd.p
    out = []
    for j in stand:
        up = us[j]
        A = np.zeros((pd.npts, len(up)), dtype=np.int64)
        cols = []
        for c, (jj, rest) in enumerate(up):
            cols.append(jj)
            if not rest:
                A[:, c] = pd.QR
            else:
                sk, sl = shiftpair(pd, rest)
                A[:, c] = (Ecol(pd, rest)
                           - pd.gk * sk % p * pd.RQ1
                           - pd.gl * sl % p * pd.SQ1) % p
        out.append((j, np.array(cols, dtype=np.int64), A))
    return out
