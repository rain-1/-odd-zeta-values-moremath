"""FREE-WEIGHT telescoper search.

Fix the operator  L = A . L_BZ  with A = sum_{t=0}^{m-3} a_t S_n^t  and the
a-vector NUMERICALLY GIVEN (a = (1) is L_BZ itself at m = 3; a = the L-tilde
direction at m = 4).  Then the whole certificate system is LINEAR in the weight
coefficients w as well as in the cofactors, so we can ask directly

      for WHICH weights w in the bare weight-3 span is L a telescoper of T.w ?

Structure exploited (identical to o_scan.py's, one level up):
  * (S^d)_{ij} != 0  iff  M_i | M_j ;
  * every strict multiple of a LETTER in the degree-<=2 weight-3 span is a
    MAXIMAL monomial, and a maximal block is solved in closed form by
    Theorem R  (r_j = w_j sum_t a_t r^(t)) -- LINEARLY in w;
  * hence each of the 18 letter blocks is a STANDALONE scalar problem

        gk r(k+1,l) - r + gl s(k,l+1) - s  =  A_L(k,l) . w ,

    and its admissible set is  { w : A_L w in Im(Msc) }, extracted by ONE
    elimination of [Msc | A_{L_1} | ... | A_{L_18}]  (o_scan.asubspaces).

The intersection over the 18 blocks is a NECESSARY condition on w.
"""
import sys, time
import numpy as np

sys.path.insert(0, '../z5la')
import zla, solve, fastlin, ratrec, ordm, o_scan, qrow
from solve import Ansatz, dval
import bare

P = 4194301
P2 = 4194287
P3 = 4194277


# --------------------------------------------------------------- ansatz -----

def dens(m):
    K1, L1 = ordm.K1, ordm.L1
    NK, NL, NKL = ordm.NK, ordm.NL, ordm.NKL
    KL = [(j, 0, 1, 1) for j in range(0, 12)]
    for _j in range(12):
        solve.NAMES[KL[_j]] = 'k+l+%d' % _j
    out = {}
    # E1: the family the predecessor used (no (k+l+j) beyond 2, no (n+k+l+j))
    out['E1'] = [(K1, 1), (L1, 1), (KL[1], 1), (KL[2], 1)] \
        + [(NK[j], 1) for j in range(1, m + 1)] + [(NL[j], 1) for j in range(1, m + 1)]
    # F1: generous -- every linear form that any letter of the 9-symbol bare
    # alphabet can put in a denominator, with the multiplicities the measured
    # () block of Z5CF_TELESCOPER 3.3 needed
    out['F1'] = [(K1, 2), (L1, 2)] \
        + [(KL[j], 1) for j in range(1, m + 3)] \
        + [(NK[j], 2) for j in range(1, m + 1)] + [(NL[j], 2) for j in range(1, m + 1)] \
        + [(NKL[j], 1) for j in range(1, m + 1)]
    # F2: F1 with cube multiplicities on the k,l side
    out['F2'] = [(K1, 3), (L1, 3)] \
        + [(KL[j], 2) for j in range(1, m + 3)] \
        + [(NK[j], 2) for j in range(1, m + 1)] + [(NL[j], 2) for j in range(1, m + 1)] \
        + [(NKL[j], 2) for j in range(1, m + 1)]
    return out


# ------------------------------------------------------------- point data ---

class PD:
    def __init__(self, p, n, m, npts, B, avec, seed=4242):
        self.p, self.n, self.m, self.npts, self.B = p, n, m, npts, B
        self.J = len(B)
        self.na = m - 2
        self.avec = [x % p for x in avec]
        assert len(self.avec) == self.na
        rng = np.random.default_rng(seed + p % 1000003 + 7919 * n + 31 * m)
        pts = []
        bad = 0
        while len(pts) < npts:
            k = int(rng.integers(2, p - 2)); l = int(rng.integers(2, p - 2))
            if self._ok(k, l):
                pts.append((k, l))
            else:
                bad += 1
                if bad > 200000:
                    raise RuntimeError('no sample points')
        self.pts = pts
        self._build()

    def _ok(self, k, l):
        p, n, m = self.p, self.n, self.m
        chk = [k, l, k + 1, l + 1, k + 2, l + 2]
        for j in range(0, m + 8):
            chk += [k + l + j, n + k + j, n + l + j, n + k + l + j,
                    n + j - k, n + j - l, n + j, k + l + j + 1]
        for c in chk:
            if c % p == 0:
                return False
        return True

    def _build(self):
        p, n, m, B = self.p, self.n, self.m, self.B
        npts, na, J = self.npts, self.na, self.J
        F = zla.Fp(p)
        letters = sorted({L for mm in B for L in mm})
        self.letters = letters
        li = {L: i for i, L in enumerate(letters)}
        nl = len(letters)
        self.gk = np.zeros(npts, dtype=np.int64)
        self.gl = np.zeros(npts, dtype=np.int64)
        # inc_n_tot[t, L, a] , inck[t,L], incl[t,L]
        self.incn = np.zeros((npts, nl, m + 1), dtype=np.int64)
        self.inck = np.zeros((npts, nl), dtype=np.int64)
        self.incl = np.zeros((npts, nl), dtype=np.int64)
        self.PM = np.zeros((npts, m + 1), dtype=np.int64)
        self.RQ1 = np.zeros(npts, dtype=np.int64)
        self.SQ1 = np.zeros(npts, dtype=np.int64)
        self.QR = np.zeros(npts, dtype=np.int64)      # the Q-row RHS = A_L[(L,)]
        cc = [zla.cc(n + t) for t in range(na)]
        rs = [qrow.make_evals(n + t, p) for t in range(na)]

        def inv(x):
            return pow(int(x) % p, p - 2, p)

        def hstep(r, x):
            """H^(r)_{x+1} - H^(r)_x = 1/(x+1)^r"""
            return inv(pow((x + 1) % p, r, p))

        for tpt, (k, l) in enumerate(self.pts):
            self.gk[tpt] = int(ordm.gkm(F, n, k, l, m))
            self.gl[tpt] = int(ordm.glm(F, n, k, l, m))
            for i in range(m + 1):
                self.PM[tpt, i] = ordm.Pm_p(n, k, l, i, m, p)
            for L in letters:
                r, a = bare.LETTERS[L]
                cn, ck, cl = bare.ARGS[a]
                d = bare.delta(L, m)
                i = li[L]
                # n-increments:  tot(a) = L(n+a) - L(n+d)
                for aa in range(m + 1):
                    tot = 0
                    if cn:
                        if aa > d:
                            for ii in range(d, aa):
                                x = cn * (n + ii) + ck * k + cl * l
                                tot = (tot + hstep(r, x)) % p
                        elif aa < d:
                            for ii in range(aa, d):
                                x = cn * (n + ii) + ck * k + cl * l
                                tot = (tot - hstep(r, x)) % p
                    self.incn[tpt, i, aa] = tot
                xb = cn * (n + d) + ck * k + cl * l
                self.inck[tpt, i] = (hstep(r, xb) if ck == 1 else
                                     (-inv(pow(xb % p, r, p)) % p if ck == -1 else 0))
                self.incl[tpt, i] = (hstep(r, xb) if cl == 1 else
                                     (-inv(pow(xb % p, r, p)) % p if cl == -1 else 0))
            # Theorem-R cofactor  sum_t a_t r^(t)
            R1 = 0; S1 = 0; QR = 0
            for t in range(na):
                at = self.avec[t]
                if at == 0:
                    continue
                rf, sf = rs[t]
                N = n + t
                fk1 = ordm.Pm_p(n, k + 1, l, t, m, p) * inv(ordm.P03_p(N, k + 1, l, p)) % p
                fl1 = ordm.Pm_p(n, k, l + 1, t, m, p) * inv(ordm.P03_p(N, k, l + 1, p)) % p
                R1 = (R1 + at * (rf(0, k + 1, l) * fk1 % p)) % p
                S1 = (S1 + at * (sf(0, k, l + 1) * fl1 % p)) % p
                for u in range(4):
                    QR = (QR + at * (cc[t][u] % p) % p * int(self.PM[tpt, t + u])) % p
            self.RQ1[tpt] = R1; self.SQ1[tpt] = S1; self.QR[tpt] = QR
        self.li = li
        self.cc = cc


# ---------------------------------------------------------- the A columns ---

def Acols(pd, blocks):
    """A_L[t, j]  for each constraint letter L in blocks."""
    p, m, na, B = pd.p, pd.m, pd.na, pd.B
    npts, J = pd.npts, pd.J
    li = pd.li
    idx = {mm: j for j, mm in enumerate(B)}
    out = []
    for L in blocks:
        mstar = (L,)
        us = bare.upset(B, mstar)                 # [(j, rest)]
        A = np.zeros((npts, J), dtype=np.int64)
        jself = idx[mstar]
        A[:, jself] = pd.QR
        for j, rest in us:
            if j == jself:
                continue
            ids = [li[x] for x in rest]
            # (E_{M_j}/Phi)_{L}  =  sum_t a_t sum_u c_u(n+t) PM[t+u] * prod inc_n[.][t+u]
            col = np.zeros(npts, dtype=np.int64)
            for t in range(na):
                at = pd.avec[t]
                if at == 0:
                    continue
                for u in range(4):
                    a = t + u
                    pr = pd.PM[:, a].copy()
                    for i in ids:
                        pr = pr * pd.incn[:, i, a] % p
                    col = (col + at * (pd.cc[t][u] % p) % p * pr) % p
            sk = np.ones(npts, dtype=np.int64)
            sl = np.ones(npts, dtype=np.int64)
            for i in ids:
                sk = sk * pd.inck[:, i] % p
                sl = sl * pd.incl[:, i] % p
            col = (col - pd.gk * sk % p * pd.RQ1
                   - pd.gl * sl % p * pd.SQ1) % p
            A[:, j] = col
        out.append(A)
    return out


def scal_mat(pd, ans):
    p, n, npts = pd.p, pd.n, pd.npts
    nc, nr = ans.nc, len(ans.mons_r)
    M = np.zeros((npts, nc), dtype=np.int64)
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
            M[t, u] = (gk * k1[a] % p * lp[b] % p * iDrk - kp[a] * lp[b] % p * iDr) % p
        for u, (a, b) in enumerate(ans.mons_s):
            M[t, nr + u] = (gl * kp[a] % p * l1[b] % p * iDsl - kp[a] * lp[b] % p * iDs) % p
    return M


# ------------------------------------------------------------------- run ----

def run(n, m, dname, slack, avec=None, p=P, maxdeg=2, npts=None, verbose=True,
        blocks=None, seed=4242):
    B, tops = bare.span_w3(maxdeg=maxdeg)
    J = len(B)
    if avec is None:
        avec = [1] + [0] * (m - 3)
    D = dens(m)[dname]
    dk0 = sum(mu * abs(f[2]) for f, mu in D)
    dl0 = sum(mu * abs(f[3]) for f, mu in D)
    dk, dl = dk0 + slack, dl0 + slack
    ans = Ansatz(D, D, dk, dl, dk, dl, force_k=0, force_l=0)
    if npts is None:
        npts = int(1.35 * (ans.nc + J)) + 20
    t0 = time.time()
    pd = PD(p, n, m, npts, B, avec, seed=seed)
    if blocks is None:
        blocks = [L for L in pd.letters if bare.LWT[L] <= 2]
    As = Acols(pd, blocks)
    Msc = scal_mat(pd, ans)
    subs, rank = o_scan.asubspaces(Msc, As, p)
    t1 = time.time()
    tv = [(nm, np.array(bare.el_to_vec(B, el, p), dtype=np.int64))
          for nm, el in bare.testvecs()]
    info = []
    for t, L in enumerate(blocks):
        ns = subs[t]
        info.append((L, len(ns), [inspan(ns, v, p, J) for _, v in tv]))
    inter = o_scan.intersect(subs, J, p)
    if verbose:
        print('n=%d m=%d %s slack=%d deg=(%d,%d) nc=%d J=%d rows=%d ratio=%.2f '
              'rank(Msc)=%d  [%.0fs]'
              % (n, m, dname, slack, dk, dl, ans.nc, J, npts,
                 npts / (ans.nc + J), rank, t1 - t0), flush=True)
        hdr = '    %-8s %5s  ' % ('block', 'dim') + ' '.join('%-11s' % nm for nm, _ in tv)
        print(hdr, flush=True)
        for L, d, fl in info:
            print('    %-8s %5d  ' % (L, d)
                  + ' '.join('%-11s' % ('YES' if a else '.') for a in fl), flush=True)
        print('    >>> INTERSECTION over %d blocks: dim %d  ' % (len(blocks), len(inter))
              + ' '.join('%s:%s' % (nm, 'YES' if inspan(inter, v, p, J) else '.')
                         for nm, v in tv), flush=True)
    return dict(pd=pd, ans=ans, subs=subs, inter=inter, blocks=blocks, B=B,
                info=info, rank=rank, npts=npts, nc=ans.nc)


def inspan(ns, v, p, J):
    if not ns:
        return False
    M = np.array(ns, dtype=np.int64) % p
    r0 = len(solve.rref(M.copy(), p)[1])
    r1 = len(solve.rref(np.concatenate([M, v.reshape(1, -1) % p], axis=0), p)[1])
    return r1 == r0


if __name__ == '__main__':
    n = int(sys.argv[1]); m = int(sys.argv[2]); dname = sys.argv[3]
    slack = int(sys.argv[4])
    run(n, m, dname, slack)
