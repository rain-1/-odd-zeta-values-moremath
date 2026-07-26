"""Adaptive cascade: solve the J scalar WZ blocks in decreasing monomial
degree, choosing each block's ansatz from the MEASURED pole structure of its
right-hand side (univariate rational reconstruction in k and in l).

Phase A records an ansatz table; phase B replays it at many (n,p).
"""
import numpy as np
import zla, solve, ratrec
from solve import Ansatz, lf

KFAM = ([('k+%d' % j, (1, 0, 1, 0), -j) for j in (1, 2, 3)]
        + [('n+k+%d' % j, (j, 1, 1, 0), None) for j in range(1, 7)]
        + [('n+%d-k' % j, (j, 1, -1, 0), None) for j in range(0, 7)])
LFAM = ([('l+%d' % j, (1, 0, 0, 1), -j) for j in (1, 2, 3)]
        + [('n+l+%d' % j, (j, 1, 0, 1), None) for j in range(1, 7)]
        + [('n+%d-l' % j, (j, 1, 0, -1), None) for j in range(0, 7)])
KLFAM = [('k+l+%d' % j, (j, 0, 1, 1), None) for j in (1, 2, 3, 4)]


def _roots(fam, n, other, var, p):
    out = []
    for nm, form, fixed in fam:
        c, cn, ck, cl = form
        # solve  form(n,k,l) = 0  for the running variable
        if var == 'k':
            coef = ck; rest = c + cn * n + cl * other
        else:
            coef = cl; rest = c + cn * n + ck * other
        out.append((nm, (-rest) * pow(coef % p, p - 2, p) % p))
    return out


class Cascade:
    def __init__(self, pd):
        self.pd = pd
        self.p, self.n = pd.p, pd.n
        self.F = zla.Fp(pd.p)
        self.coefs = {}
        self.ansatz = {}
        self.rvals = np.zeros((pd.J, pd.npts), dtype=np.int64)
        self.svals = np.zeros((pd.J, pd.npts), dtype=np.int64)
        self.done = np.zeros(pd.J, dtype=bool)
        self.solvers = {}

    # --- f_i at an arbitrary point, using the already-solved higher blocks ---
    def f_at(self, i, k, l):
        pd, F, p, n = self.pd, self.F, self.p, self.n
        tot = zla.el_to_vec(F, pd.B, zla.rhs_element(F, pd.w, n, k, l))[i]
        gk = zla.gk_val(F, n, k, l); gl = zla.gl_val(F, n, k, l)
        Sk = zla.shift_matrix(F, pd.B, 'k', n, k, l)
        Sl = zla.shift_matrix(F, pd.B, 'l', n, k, l)
        for j in range(pd.J):
            if not self.done[j]: continue
            A = self.ansatz[j]
            nk = (Sk[j][i] - (1 if i == j else 0)) % p
            nl = (Sl[j][i] - (1 if i == j else 0)) % p
            if nk: tot = (tot - gk * nk % p * A.eval_r(self.coefs[j], n, k + 1, l, p)) % p
            if nl: tot = (tot - gl * nl % p * A.eval_s(self.coefs[j], n, k, l + 1, p)) % p
        return tot % p

    def f_vec(self, i):
        pd, p = self.pd, self.p
        rhs = pd.bvec[:, i].copy()
        for j in range(pd.J):
            if not self.done[j]: continue
            nk = pd.Nk[:, i, j]
            if nk.any(): rhs = (rhs - pd.gk * nk % p * self.rvals[j]) % p
            nl = pd.Nl[:, i, j]
            if nl.any(): rhs = (rhs - pd.gl * nl % p * self.svals[j]) % p
        return rhs

    # ------------------------------------------------ pole-structure probe --
    def probe(self, i, var, other=987654321, npt=110, maxdeg=55):
        p, n = self.p, self.n
        xs, vs = [], []
        x = 1237
        while len(xs) < npt:
            x += 1
            try:
                v = self.f_at(i, x, other) if var == 'k' else self.f_at(i, other, x)
            except ZeroDivisionError:
                continue
            xs.append(x); vs.append(v)
        r = ratrec.null_min_deg(vs, xs, p, maxdeg)
        if r is None: return None
        num, den = r
        fam = (KFAM if var == 'k' else LFAM) + KLFAM
        m, rest = ratrec.factor_mult(den, _roots(fam, n, other, var, p), p)
        return dict(dnum=len(num) - 1, dden=len(den) - 1, fac=m,
                    unfactored=len(rest) - 1)

    def design(self, i, slack=2, verbose=True):
        """pick an ansatz for block i from the measured poles"""
        pk = self.probe(i, 'k'); pl = self.probe(i, 'l')
        if pk is None or pl is None: raise RuntimeError('probe failed at %d' % i)
        if pk['unfactored'] or pl['unfactored']:
            raise RuntimeError('unfactored denominator at block %d: %s %s'
                               % (i, pk, pl))
        forms = {}
        for nm, form, _ in KFAM + LFAM + KLFAM:
            forms[nm] = form
        D = []
        seen = set()
        for src in (pk['fac'], pl['fac']):
            for nm in src:
                if nm in ('k+1', 'k+2', 'k+3', 'l+1', 'l+2', 'l+3'): continue
                if nm.startswith('k+l+'):
                    nm = 'k+l+1'          # only the unshifted one belongs in D
                if nm in seen: continue
                seen.add(nm); D.append((forms[nm], 1))
        dkD = sum(m * abs(f[2]) for f, m in D)
        dlD = sum(m * abs(f[3]) for f, m in D)
        gk = pk['dnum'] - pk['dden']
        gl = pl['dnum'] - pl['dden']
        dk = dkD + max(gk, 0) + slack
        dl = dlD + max(gl, 0) + slack
        A = Ansatz(D, D, dk, dl, dk, dl)
        if verbose:
            print('   block %-16s D=%-46s deg=(%d,%d) nc=%d  [growth %d,%d]'
                  % (str(self.pd.B[i]), solve.dstr(D), dk, dl, A.nc, gk, gl))
        return A

    def get_solver(self, A):
        key = A.key()
        if key not in self.solvers:
            self.solvers[key] = solve.LevelSolver(self.pd, A)
        return self.solvers[key]

    def solve_block(self, i, A):
        pd, p = self.pd, self.p
        LS = self.get_solver(A)
        rhs = self.f_vec(i)
        x, nbad = LS.solve(rhs)
        if nbad: return nbad
        self.coefs[i] = x; self.ansatz[i] = A
        self.rvals[i] = np.array([A.eval_r(x, pd.n, k + 1, l, p)
                                  for (k, l) in pd.pts], dtype=np.int64)
        self.svals[i] = np.array([A.eval_s(x, pd.n, k, l + 1, p)
                                  for (k, l) in pd.pts], dtype=np.int64)
        self.done[i] = True
        return 0

    def run_adaptive(self, escalate=(0, 2, 4, 6), verbose=True):
        pd = self.pd
        order = sorted(range(pd.J), key=lambda i: (-pd.deg[i], i))
        table = {}
        for i in order:
            A0 = self.design(i, slack=2, verbose=verbose)
            ok = None
            for extra in escalate:
                A = Ansatz(A0.Dr, A0.Ds, A0.par[0] + extra, A0.par[1] + extra,
                           A0.par[2] + extra, A0.par[3] + extra)
                if A.nc > pd.npts / 1.4:
                    if verbose: print('     ! nc=%d too big for npts=%d' % (A.nc, pd.npts))
                    break
                nbad = self.solve_block(i, A)
                if nbad == 0:
                    ok = A; break
                if verbose: print('     escalate +%d : bad=%d' % (extra, nbad))
            if ok is None:
                raise RuntimeError('block %s (%d) NOT SOLVABLE with these ansaetze'
                                   % (str(pd.B[i]), i))
            table[i] = ok
            if verbose: print('     -> solved, nc=%d' % ok.nc)
        return table

    def run_fixed(self, table):
        pd = self.pd
        order = sorted(range(pd.J), key=lambda i: (-pd.deg[i], i))
        bad = {}
        for i in order:
            bad[i] = self.solve_block(i, table[i])
        return bad

    # ------------------------------------------------------ full residual --
    def residual(self, npt=40, seed=999):
        """check the FULL module identity  b = gk Sk r(k+1) - r + gl Sl s(l+1) - s
        at fresh random points, independent of the sample set used to solve."""
        pd, F, p, n = self.pd, self.F, self.p, self.n
        rng = np.random.default_rng(seed)
        bad = 0; tested = 0
        while tested < npt:
            k = int(rng.integers(2, p - 2)); l = int(rng.integers(2, p - 2))
            try:
                b = zla.el_to_vec(F, pd.B, zla.rhs_element(F, pd.w, n, k, l))
                gk = zla.gk_val(F, n, k, l); gl = zla.gl_val(F, n, k, l)
                Sk = zla.shift_matrix(F, pd.B, 'k', n, k, l)
                Sl = zla.shift_matrix(F, pd.B, 'l', n, k, l)
                rv = [self.ansatz[j].eval_r(self.coefs[j], n, k + 1, l, p)
                      for j in range(pd.J)]
                r0 = [self.ansatz[j].eval_r(self.coefs[j], n, k, l, p)
                      for j in range(pd.J)]
                sv = [self.ansatz[j].eval_s(self.coefs[j], n, k, l + 1, p)
                      for j in range(pd.J)]
                s0 = [self.ansatz[j].eval_s(self.coefs[j], n, k, l, p)
                      for j in range(pd.J)]
            except ZeroDivisionError:
                continue
            tested += 1
            for i in range(pd.J):
                acc = 0
                for j in range(pd.J):
                    acc = (acc + gk * Sk[j][i] % p * rv[j] + gl * Sl[j][i] % p * sv[j]) % p
                acc = (acc - r0[i] - s0[i] - b[i]) % p
                if acc: bad += 1
        return tested, bad
