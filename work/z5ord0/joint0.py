"""Joint (all blocks at once) order-zero certificate solver.

Certificate sought:  w = Op(rho, sigma) with
    Op(rho,sigma) = gk rho(n,k+1,l) - rho(n,k,l)
                  + gl sigma(n,k,l+1) - sigma(n,k,l)
in the module  Q(n,k,l) (x) <harmonic monomials>.  Multiplying by T this is
T w = Delta_k(T rho) + Delta_l(T sigma).

sigma := tau(rho) is imposed (WLOG: every target w is k<->l symmetric, and
(rho,sigma) a certificate implies (tau sigma, tau rho) is one too, so the
average has sigma = tau rho; the average also preserves the boundary
conditions).  Concretely sigma_m(n,k,l) = rho_{tau m}(n,l,k).

Ansatz:  rho_m(n,k,l) = N_m(k,l) / D(n,k,l),  N_m of bidegree <= (dk,dl).

BOUNDARY (module level, NOT blockwise):
  bottom   rho|_{k=0} = 0  with the letter specialisation
             h*_k -> 0, h*_pk -> h*_n, h*_mk -> h*_n, h*_kl -> h*_l,
             h*_pkl -> h*_pl, others fixed.
           sigma|_{l=0} = 0 then follows by tau.
           Two ways to impose it:  force_k=1  puts k | N_m for every block
           (sufficient but it annihilates almost all gauge/kernel elements,
           because a kernel element rho0 = gl v(k,l+1) - v(k,l) satisfies
           rho0(0,l)=0 only if v(0,.) solves a first-order recurrence);
           bnd=True imposes the honest module condition as extra rows.
  top      T(n,n+1,l) = 0 identically; the only pole of rho(k+1,l) at k=n is
           the -1/(n-k)^r increment of H^(r)_{n-k}, and gk carries (n-k)^2, so
           the top boundary is automatic when every monomial has
           H_{n-k}-weight <= 1  (mk_cap=1).
"""
import itertools
import sys

import numpy as np

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import fastlin

import o0core as C
from o0core import Ansatz, dstr

P1 = 4194301
P2 = 4194287


def sample_points(n, p, npts, seed=1, k0=False):
    rng = np.random.default_rng(seed)
    pts = []
    guard = 0
    while len(pts) < npts:
        guard += 1
        if guard > 500000:
            raise RuntimeError('no admissible sample points')
        k = 0 if k0 else int(rng.integers(4, p - 4))
        l = int(rng.integers(4, p - 4))
        ok = True
        for (kk, ll) in ((k, l), (k + 1, l), (k, l + 1)):
            for j in range(0, 5):
                for c in (kk + 1 + j, ll + 1 + j, kk + ll + j, n + kk + j,
                          n + ll + j, n + kk + ll + j, n + j - kk, n + j - ll):
                    if c % p == 0:
                        ok = False
        if ok and (k, l) not in pts:
            pts.append((k, l))
    return pts


def spec_k0(mon):
    """the k=0 specialisation of a monomial; None means it vanishes."""
    out = []
    for L in mon:
        r, a = C.parse(L)
        b = C.SPEC_K0[a]
        if b is None:
            return None
        out.append(C.lname(r, b))
    return tuple(sorted(out))


def build_basis(w, maxdeg, alphabet=None, mk_cap=1, extra_letters=()):
    letters = set()
    for m in w:
        letters.update(m)
    letters.update(extra_letters)
    if alphabet is not None:
        letters = set(alphabet)
    letters = sorted(letters)
    B = []
    for d in range(maxdeg + 1):
        for combo in itertools.combinations_with_replacement(letters, d):
            m = tuple(sorted(combo))
            if C.mkwt(m) > mk_cap or C.mlwt(m) > mk_cap:
                continue
            B.append(m)
    Bs = set(B)
    for m in w:
        if m not in Bs:
            raise ValueError('supp(w) not inside B: %r' % (m,))
    for m in B:
        if C.sigma_mon(m) not in Bs:
            raise ValueError('B not tau-closed at %r' % (m,))
    B.sort(key=lambda m: (-len(m), -sum(C.lwt(L) for L in m), m))
    return B


class System:
    def __init__(self, w, n, p, B, ans, npts, seed=1, bnd=False, nbnd=0):
        self.w, self.n, self.p, self.B, self.ans = w, n, p, B, ans
        self.J = len(B)
        self.idx = {m: j for j, m in enumerate(B)}
        self.tau = [self.idx[C.sigma_mon(m)] for m in B]
        self.pts = sample_points(n, p, npts, seed)
        self.npts = npts
        self.bnd = bnd
        self.nbnd = nbnd
        self.bpts = sample_points(n, p, nbnd, seed + 777, k0=True) if bnd else []

    # ------------------------------------------------------------------ rows
    def _vec(self, x, y):
        p, n, ans = self.p, self.n, self.ans
        iD = pow(C.dval(ans.D, n, x, y, p), p - 2, p)
        dmax = self.dmax
        xp = [pow(x % p, a, p) for a in range(dmax)]
        yp = [pow(y % p, a, p) for a in range(dmax)]
        return np.array([xp[a] * yp[b] % p * iD % p for a, b in ans.mons],
                        dtype=np.float64)

    def build(self, rhs_fn=None):
        p, n, B, ans = self.p, self.n, self.B, self.ans
        J, nc, npts = self.J, ans.nc, self.npts
        self.dmax = max(max(a, b) for a, b in ans.mons) + 2
        wvec = []
        for m in B:
            q = self.w.get(m) if self.w is not None else None
            wvec.append(0 if q is None else
                        int(q.numerator) % p * pow(int(q.denominator), p - 2, p) % p)
        # boundary block groups
        groups = {}
        if self.bnd:
            for j, m in enumerate(B):
                mu = spec_k0(m)
                if mu is None:
                    continue
                groups.setdefault(mu, []).append(j)
            groups = {mu: js for mu, js in groups.items()}
        nbrows = len(groups) * len(self.bpts)
        rows = J * npts + nbrows
        cols = J * nc
        M = np.zeros((rows, cols))
        rhs = np.zeros(rows)
        for t, (k, l) in enumerate(self.pts):
            gk = C.gk_val(n, k, l, p)
            gl = C.gl_val(n, k, l, p)
            Sk = C.shift_cols(B, C.KINC, n, k, l, p)
            Sl = C.shift_cols(B, C.LINC, n, k, l, p)
            vr1 = self._vec(k + 1, l)
            vr0 = self._vec(k, l)
            vs1 = self._vec(l + 1, k)
            vs0 = self._vec(l, k)
            for i in range(J):
                r = i * npts + t
                for j in np.nonzero(Sk[i])[0]:
                    c = gk * int(Sk[i, j]) % p
                    if c:
                        M[r, j * nc:(j + 1) * nc] = (
                            M[r, j * nc:(j + 1) * nc] + c * vr1) % p
                for j in np.nonzero(Sl[i])[0]:
                    c = gl * int(Sl[i, j]) % p
                    if c:
                        jj = self.tau[j]
                        M[r, jj * nc:(jj + 1) * nc] = (
                            M[r, jj * nc:(jj + 1) * nc] + c * vs1) % p
                M[r, i * nc:(i + 1) * nc] = (M[r, i * nc:(i + 1) * nc] - vr0) % p
                ii = self.tau[i]
                M[r, ii * nc:(ii + 1) * nc] = (M[r, ii * nc:(ii + 1) * nc] - vs0) % p
                rhs[r] = wvec[i] if rhs_fn is None else rhs_fn(i, t)
        # boundary rows: sum over blocks with the same k=0 image
        r = J * npts
        for mu, js in groups.items():
            for (k0, l0) in self.bpts:
                v = self._vec(0, l0)
                for j in js:
                    M[r, j * nc:(j + 1) * nc] = (M[r, j * nc:(j + 1) * nc] + v) % p
                r += 1
        self.M, self.rhs, self.groups = M, rhs, groups
        return M, rhs

    def solve(self):
        X, rank, piv, nbad = fastlin.solve(self.M.astype(np.int64),
                                           self.rhs.astype(np.int64), self.p)
        self.X, self.rank, self.nbad = X, rank, nbad
        return X, rank, nbad

    # ------------------------------------------------------------- checking
    def op_values(self, X, k, l):
        """the module element Op(rho,sigma) at (k,l), as a vector over B."""
        p, n, B, ans = self.p, self.n, self.B, self.ans
        J, nc = self.J, ans.nc
        gk = C.gk_val(n, k, l, p)
        gl = C.gl_val(n, k, l, p)
        Sk = C.shift_cols(B, C.KINC, n, k, l, p)
        Sl = C.shift_cols(B, C.LINC, n, k, l, p)
        rr1 = [ans.eval_r(X[j * nc:(j + 1) * nc], n, k + 1, l, p) for j in range(J)]
        rr0 = [ans.eval_r(X[j * nc:(j + 1) * nc], n, k, l, p) for j in range(J)]
        ss1 = [ans.eval_r(X[self.tau[j] * nc:(self.tau[j] + 1) * nc], n, l + 1, k, p)
               for j in range(J)]
        ss0 = [ans.eval_r(X[self.tau[j] * nc:(self.tau[j] + 1) * nc], n, l, k, p)
               for j in range(J)]
        out = []
        for i in range(J):
            v = 0
            for j in range(J):
                if Sk[i, j]:
                    v = (v + gk * int(Sk[i, j]) % p * rr1[j]) % p
                if Sl[i, j]:
                    v = (v + gl * int(Sl[i, j]) % p * ss1[j]) % p
            out.append((v - rr0[i] - ss0[i]) % p)
        return out

    def check(self, X, pts):
        p, B = self.p, self.B
        bad = cells = 0
        for (k, l) in pts:
            vals = self.op_values(X, k, l)
            for i, m in enumerate(B):
                q = self.w.get(m)
                wv = 0 if q is None else int(q.numerator) % p * pow(int(q.denominator), p - 2, p) % p
                cells += 1
                if (vals[i] - wv) % p:
                    bad += 1
        return bad, cells


def run(w, n, D, deg, maxdeg, npts, p=P1, seed=1, force_k=0, mk_cap=1,
        alphabet=None, extra_letters=(), label='', bnd=True, nbnd=None,
        verbose=True, rhs_fn=None):
    B = build_basis(w, maxdeg, alphabet=alphabet, mk_cap=mk_cap,
                    extra_letters=extra_letters)
    ans = Ansatz(D, deg, deg, force_k=force_k)
    if nbnd is None:
        nbnd = 2 * (deg + 2)
    S = System(w, n, p, B, ans, npts, seed, bnd=bnd, nbnd=nbnd)
    M, rhs = S.build(rhs_fn=rhs_fn)
    X, rank, nbad = S.solve()
    ratio = M.shape[0] / M.shape[1]
    if verbose:
        print('  %-16s n=%d J=%d nc=%d cols=%d rows=%d(+%d bnd) ratio=%.2f '
              'rank=%d null=%d resid=%d -> %s'
              % (label, n, S.J, ans.nc, M.shape[1], S.J * npts,
                 M.shape[0] - S.J * npts, ratio, rank, M.shape[1] - rank,
                 nbad, 'FOUND' if nbad == 0 else 'no'), flush=True)
    return S, X, nbad
