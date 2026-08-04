"""eps43.py -- curve-atom pinning scan for the SPORADIC Apery-like families.

Adapts the validated eps41/eps42 machinery (zeta-graded pinning, curve atoms)
to the fifteen-pair setting (papers_out/sporadics/main.tex):
  R2: (n+1)^2 u_{n+1} = (a n^2+a n+b) u_n - c n^2 u_{n-1}
  R3: (n+1)^3 u_{n+1} = (2n+1)(a n^2+a n+b) u_n - n(c n^2+d) u_{n-1}
  B(n): second solution, B(0)=0, B(1)=1, recurrence imposed for n>=1.

Families: franel C(n,k)^3 [control], D C(n,k)^2 C(n+k,n) [control],
zagierB (-1)^k 3^(n-3k) n!/((n-3k)! k!^3), delta (-1)^k 3^(n-3k)
(n+k)!/((n-3k)! k!^4), zeta double sum C(n,k)^2 C(n,l) C(k,l) C(k+l,n).
Prefactors (signs, powers of 3) are deformation-inert.

Atoms: curves u=(u1[,u2]) in Z^dim per degree; per letter L the shift is
s_L(eps) = sum_i <dcoef_L, u_i> eps^i; cell expansion S * exp(sum (A_m+c_m)
eps^m) exactly as eps42 (gamma terms drop: S_1-forms vanish, asserted).
Pinning per zeta-graded component: [eps^1]=0; intermediate orders in
span{A}; target order = b*B + a*A with b != 0 the prize.
"""
import sys, time, pickle
import numpy as np
from math import comb, factorial
from fractions import Fraction as F
from itertools import product as iproduct

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
import core
from eps41 import fm, nullspace, ratrec
from eps42 import comp_coef

RMAX = 3

# ---------------- family specs ----------------
class Fam:
    def __init__(self, name, dim, letters, cells, pref, rec, target):
        self.name, self.dim = name, dim
        self.letters = letters          # list of (argname, p_L, dcoef tuple)
        self.cells = cells              # n -> list of cell tuples
        self.pref = pref                # (n, cell) -> +-3^j int
        self.rec = rec                  # ('R2'|'R3', a, b, c, d)
        self.target = target            # primary target eps order
    def args(self, n, c):
        env = dict(n=n, k=c[0], l=(c[1] if len(c) > 1 else 0))
        return [eval(a, {}, env) for (a, _, _) in self.letters]
    def S(self, n, c):
        v = self.pref(n, c)
        for x, (_, p, _) in zip(self.args(n, c), self.letters):
            assert x >= 0
            v = v * F(factorial(x)) ** p
        assert v.denominator == 1 or True
        return v
    def A(self, n):
        return sum(self.S(n, c) for c in self.cells(n))

def mk_fams():
    fams = {}
    fams['franel'] = Fam(
        'franel', 2,
        [('n', 3, (1, 0)), ('k', -3, (0, 1)), ('n-k', -3, (1, -1))],
        lambda n: [(k,) for k in range(n + 1)],
        lambda n, c: 1, ('R2', 7, 2, -8, 0), 2)
    fams['D'] = Fam(
        'D', 2,
        [('n', 1, (1, 0)), ('k', -3, (0, 1)), ('n-k', -2, (1, -1)),
         ('n+k', 1, (1, 1))],
        lambda n: [(k,) for k in range(n + 1)],
        lambda n, c: 1, ('R2', 11, 3, -1, 0), 2)
    fams['zagierB'] = Fam(
        'zagierB', 2,
        [('n', 1, (1, 0)), ('n-3*k', -1, (1, -3)), ('k', -3, (0, 1))],
        lambda n: [(k,) for k in range(n // 3 + 1)],
        lambda n, c: (-1) ** c[0] * 3 ** (n - 3 * c[0]),
        ('R2', 9, 3, 27, 0), 2)
    fams['delta'] = Fam(
        'delta', 2,
        [('n+k', 1, (1, 1)), ('n-3*k', -1, (1, -3)), ('k', -4, (0, 1))],
        lambda n: [(k,) for k in range(n // 3 + 1)],
        lambda n, c: (-1) ** c[0] * 3 ** (n - 3 * c[0]),
        ('R3', 7, 3, 81, 0), 3)
    fams['zeta'] = Fam(
        'zeta', 3,
        [('n', 2, (1, 0, 0)), ('k', -1, (0, 1, 0)), ('n-k', -2, (1, -1, 0)),
         ('l', -2, (0, 0, 1)), ('n-l', -1, (1, 0, -1)),
         ('k-l', -1, (0, 1, -1)), ('k+l', 1, (0, 1, 1)),
         ('k+l-n', -1, (-1, 1, 1))],
        lambda n: [(k, l) for k in range(n + 1)
                   for l in range(max(0, n - k), k + 1)],
        lambda n, c: 1, ('R3', 9, 3, -27, 0), 3)
    return fams

# table A(n) cross-checks (direct binomial sums, independent of Fam.S)
def A_binom(name, n):
    if name == 'franel':
        return sum(comb(n, k) ** 3 for k in range(n + 1))
    if name == 'D':
        return sum(comb(n, k) ** 2 * comb(n + k, n) for k in range(n + 1))
    if name == 'zagierB':
        return sum((-1) ** k * 3 ** (n - 3 * k) * comb(n, 3 * k)
                   * factorial(3 * k) // factorial(k) ** 3
                   for k in range(n // 3 + 1))
    if name == 'delta':
        return sum((-1) ** k * 3 ** (n - 3 * k) * comb(n, 3 * k)
                   * comb(n + k, n) * factorial(3 * k) // factorial(k) ** 3
                   for k in range(n // 3 + 1))
    if name == 'zeta':
        return sum(comb(n, k) ** 2 * comb(n, l) * comb(k, l) * comb(k + l, n)
                   for k in range(n + 1) for l in range(n + 1))

def rec_check(fam, NCH=12):
    typ, a, b, c, d = fam.rec
    Av = [fam.A(n) for n in range(NCH + 2)]
    for n in range(NCH + 1):
        Ab = A_binom(fam.name, n)
        assert Av[n] == Ab, (fam.name, n, Av[n], Ab)
    for n in range(1, NCH):
        if typ == 'R2':
            r = ((n + 1) ** 2 * Av[n + 1] - (a * n * n + a * n + b) * Av[n]
                 + c * n * n * Av[n - 1])
        else:
            r = ((n + 1) ** 3 * Av[n + 1]
                 - (2 * n + 1) * (a * n * n + a * n + b) * Av[n]
                 + n * (c * n * n + d) * Av[n - 1])
        assert r == 0, (fam.name, 'recurrence fails', n, r)
    return Av

def Bseq(fam, N):
    typ, a, b, c, d = fam.rec
    B = [F(0), F(1)]
    for n in range(1, N):
        if typ == 'R2':
            nxt = ((a * n * n + a * n + b) * B[n] - c * n * n * B[n - 1])
            nxt = F(nxt, (n + 1) ** 2)
        else:
            nxt = ((2 * n + 1) * (a * n * n + a * n + b) * B[n]
                   - n * (c * n * n + d) * B[n - 1])
            nxt = F(nxt, (n + 1) ** 3)
        B.append(nxt)
    return B

# ---------------- atom expansion (generic letters) ----------------
def atom_data(fam, us):
    """lamH[m] = list of (j, [coef per letter]); K[m] = {tau: Fraction}."""
    D = len(us)
    dmat = [[sum(dc[i] * u[i] for i in range(fam.dim))
             for (_, _, dc) in fam.letters] for u in us]   # [deg][letter]
    NL = len(fam.letters)
    lamH, cconst = {}, {}
    for m in range(1, RMAX + 1):
        terms, cm = [], {}
        for j in range(max(1, (m + D - 1) // D), m + 1):
            coefs = [comp_coef([dmat[i][L] for i in range(D)], j, m)
                     for L in range(NL)]
            if not any(coefs):
                continue
            fac = F((-1) ** (j - 1), j)
            vec = [fac * fam.letters[L][1] * coefs[L] for L in range(NL)]
            terms.append((j, vec))
            Sf = sum(fam.letters[L][1] * coefs[L] for L in range(NL))
            if j == 1:
                assert Sf == 0, ('gamma S-form nonzero', fam.name, us, m)
            elif Sf:
                cm[('z%d' % j,)] = F((-1) ** j, j) * Sf
        lamH[m] = terms
        cconst[m] = cm
    K = {0: {(): F(1)}}
    for m in range(1, RMAX + 1):
        acc = {}
        for i in range(1, m + 1):
            for t1, v1 in cconst[i].items():
                for t2, v2 in K[m - i].items():
                    t = tuple(sorted(t1 + t2))
                    acc[t] = acc.get(t, F(0)) + F(i, m) * v1 * v2
        K[m] = {t: v for t, v in acc.items() if v}
    return lamH, K

def bell3(L):
    l1, l2, l3 = L[1], L[2], L[3]
    return {1: l1, 2: l2 + l1 * l1 / 2,
            3: l3 + l1 * l2 + l1 * l1 * l1 / 6}

def bell3_mod(L, p):
    i2, i6 = pow(2, p - 2, p), pow(6, p - 2, p)
    l1, l2, l3 = L[1], L[2], L[3]
    l1_2 = l1 * l1 % p
    return {1: l1 % p, 2: (l2 + l1_2 * i2) % p,
            3: (l3 + l1 * l2 + l1_2 * l1 % p * i6) % p}

def lam_exact(fam, lamH, xs):
    return {m: sum(vec[L] * core.Hs(xs[L], j) for (j, vec) in lamH[m]
                   for L in range(len(fam.letters)))
            for m in range(1, RMAX + 1)}

# monomial expansion of B^H_r for printing / exact identity display
BELL_TERMS3 = {1: [([1], F(1))],
               2: [([2], F(1)), ([1, 1], F(1, 2))],
               3: [([3], F(1)), ([1, 2], F(1)), ([1, 1, 1], F(1, 6))]}

def expand_BH(fam, lamH, r):
    vecs = {}
    for m in range(1, r + 1):
        d = {}
        for (j, vec) in lamH[m]:
            for L in range(len(fam.letters)):
                if vec[L]:
                    d[(j, L)] = d.get((j, L), F(0)) + vec[L]
        vecs[m] = d
    out = {}
    for mlist, coef in BELL_TERMS3[r]:
        def rec(i, mono, cc):
            if cc == 0:
                return
            if i == len(mlist):
                key = tuple(sorted(mono))
                out[key] = out.get(key, F(0)) + cc
                return
            for let, cv in vecs[mlist[i]].items():
                rec(i + 1, mono + [let], cc * cv)
        rec(0, [], coef)
    return {m: v for m, v in out.items() if v}

def fmt_weight(fam, mono):
    parts = []
    for m, cv in sorted(mono.items(), key=lambda t: (len(t[0]), t[0])):
        s = '*'.join('H%d[%s]' % (j, fam.letters[L][0]) for (j, L) in m)
        parts.append('%s * %s' % (cv, s))
    return '\n      '.join(parts) if parts else '0'

# ---------------- validation vs mpmath ----------------
def validate_family(fam, us, n, cell):
    from mpmath import mp, mpf, gamma as mpgamma, zeta as mpzeta, taylor
    mp.dps = 60
    xs = fam.args(n, cell)
    lamH, K = atom_data(fam, us)
    Aval = lam_exact(fam, lamH, xs)
    BH = {0: F(1)}
    BH.update(bell3(Aval))
    frac = lambda q: mpf(q.numerator) / mpf(q.denominator)
    zval = {'z%d' % j: mpzeta(j) for j in range(2, RMAX + 1)}
    Knum = {}
    for m in range(RMAX + 1):
        s = mpf(0)
        for t, v in K.get(m, {}).items():
            term = frac(v)
            for z in t:
                term *= zval[z]
            s += term
        Knum[m] = s
    T0 = F(1)
    for x, (_, p, _) in zip(xs, fam.letters):
        T0 *= F(factorial(x)) ** p
    coeffs_a = [frac(T0) * sum(Knum[w] * frac(BH[r - w])
                               for w in range(r + 1)) for r in range(RMAX + 1)]
    dmat = [[sum(dc[i] * u[i] for i in range(fam.dim))
             for (_, _, dc) in fam.letters] for u in us]
    def f(e):
        out = mpf(1)
        for L, (x, (_, p, _)) in enumerate(zip(xs, fam.letters)):
            sh = sum(dmat[i][L] * e ** (i + 1) for i in range(len(us)))
            out *= mpgamma(x + 1 + sh) ** p
        return out
    coeffs_b = taylor(f, 0, RMAX, method='quad', radius=mpf(1) / 8)
    ok = True
    for r in range(RMAX + 1):
        ca, cb = coeffs_a[r], coeffs_b[r]
        agree = abs(cb - ca) < mpf(10) ** (-25) * (1 + abs(ca))
        if not agree:
            print('    eps^%d: bell=%s mpmath=%s DISAGREE'
                  % (r, mp.nstr(ca, 30), mp.nstr(cb, 30)))
        ok = ok and agree
    print('  validation %s atom %s at (n,cell)=(%d,%s): %s'
          % (fam.name, us, n, cell, 'PASS' if ok else 'FAIL'), flush=True)
    return ok

# ---------------- rows mod p ----------------
def build_rows(fam, ATOMS, p, N):
    NL = len(fam.letters)
    Xs, Sm, Ni = [[] for _ in range(NL)], [], []
    for n in range(N + 1):
        for c in fam.cells(n):
            xs = fam.args(n, c)
            for L in range(NL):
                Xs[L].append(xs[L])
            Sm.append(fm(fam.S(n, c), p))
            Ni.append(n)
    Xs = np.array(Xs, dtype=np.int64)
    Sm = np.array(Sm, dtype=np.int64)
    Ni = np.array(Ni, dtype=np.int64)
    HM = int(Xs.max()) + 1
    Ht = np.zeros((RMAX + 1, HM + 1), dtype=np.int64)
    for m_ in range(1, HM + 1):
        im = pow(m_, p - 2, p)
        acc = 1
        for r in range(1, RMAX + 1):
            acc = acc * im % p
            Ht[r][m_] = (Ht[r][m_ - 1] + acc) % p
    nc = Xs.shape[1]
    R = np.zeros((RMAX + 1, len(ATOMS), N + 1), dtype=np.int64)
    Ks = []
    for ia, us in enumerate(ATOMS):
        lamH, K = atom_data(fam, us)
        Ks.append(K)
        Lam = {}
        for m in range(1, RMAX + 1):
            acc = np.zeros(nc, dtype=np.int64)
            for (j, vec) in lamH[m]:
                for L in range(NL):
                    if vec[L]:
                        acc = (acc + fm(vec[L], p) * Ht[j][Xs[L]]) % p
            Lam[m] = acc
        B = bell3_mod(Lam, p)
        for r in range(1, RMAX + 1):
            row = np.zeros(N + 1, dtype=np.int64)
            np.add.at(row, Ni, Sm * B[r] % p)
            R[r][ia] = row % p
    return R, Ks

# ---------------- system ----------------
def build_system(fam, ATOMS, R, Ks, Av, Bv, p, target):
    nat = len(ATOMS)
    N = len(Av) - 1
    LADV = {'A': Av, 'B': Bv}
    blocks = []
    for r in range(1, target + 1):
        taus = set([()])
        for m in range(1, r + 1):
            for ia in range(nat):
                taus.update(Ks[ia][m].keys())
        span = () if r == 1 else (('A',) if r < target else ('B', 'A'))
        for tau in sorted(taus):
            blocks.append((r, tau, span))
    naux = sum(len(sp) for _, _, sp in blocks)
    nun = nat + naux
    rows, auxinfo = [], []
    bcol, bcols_all = None, []
    aux = nat
    for r, tau, span in blocks:
        label = 'r%d' % r + ('' if tau == () else '.' + '*'.join(tau))
        base = np.zeros((nat, N + 1), dtype=np.int64)
        for ia in range(nat):
            for s in range(0, r + 1):
                kap = Ks[ia][r - s].get(tau) if r - s > 0 else \
                      (F(1) if tau == () else None)
                if kap is None:
                    continue
                base[ia] = (base[ia] + fm(kap, p) * (R[s][ia] if s else Av)) % p
        cols = list(range(aux, aux + len(span)))
        for j, lname in zip(cols, span):
            auxinfo.append((label, lname))
            if lname == 'B' and r == target:
                bcols_all.append(j)
                if tau == ():
                    bcol = j
        for n in range(N + 1):
            row = np.zeros(nun, dtype=np.int64)
            row[:nat] = base[:, n]
            for j, lname in zip(cols, span):
                row[j] = (-int(LADV[lname][n])) % p
            rows.append(row)
        aux += len(cols)
    return np.array(rows, dtype=np.int64), bcol, bcols_all, auxinfo, nun, blocks

# ---------------- exact verification & reporting ----------------
def exact_verify(fam, sol_r, aux_r, blocks, ATOMS, target, Nv=25):
    """sol_r: {atom index: Fraction}; aux_r: {(label,lname): Fraction}.
    Verify every block identity exactly over Q for n <= Nv."""
    Bx = Bseq(fam, Nv + 1)
    lam_cache = {ia: atom_data(fam, ATOMS[ia]) for ia in sol_r}
    ok = True
    for n in range(Nv + 1):
        cells = fam.cells(n)
        Svals = [fam.S(n, c) for c in cells]
        An = sum(Svals)
        # per-atom exact rows R_s[n]
        Rex = {}
        for ia in sol_r:
            lamH, K = lam_cache[ia]
            rs = {0: An}
            bh = [bell3(lam_exact(fam, lamH, fam.args(n, c))) for c in cells]
            for s in range(1, RMAX + 1):
                rs[s] = sum(Sv * b[s] for Sv, b in zip(Svals, bh))
            Rex[ia] = (rs, K)
        for r, tau, span in blocks:
            label = 'r%d' % r + ('' if tau == () else '.' + '*'.join(tau))
            tot = F(0)
            for ia, cv in sol_r.items():
                rs, K = Rex[ia]
                for s in range(0, r + 1):
                    kap = K[r - s].get(tau) if r - s > 0 else \
                          (F(1) if tau == () else None)
                    if kap is not None:
                        tot += cv * kap * rs[s]
            rhs = F(0)
            for lname in span:
                a = aux_r.get((label, lname), F(0))
                rhs += a * (An if lname == 'A' else Bx[n])
            if tot != rhs:
                print('    EXACT MISMATCH n=%d block %s: %s != %s'
                      % (n, label, tot, rhs))
                ok = False
    return ok

def run_scan(fam, ATOMS, Av_int, p, target, N, tag, do_extract=True):
    Av = np.array([fm(F(a), p) for a in Av_int], dtype=np.int64)
    Bx = Bseq(fam, N + 1)
    Bv = np.array([fm(b, p) for b in Bx], dtype=np.int64)
    R, Ks = build_rows(fam, ATOMS, p, N)
    M, bcol, bcolsa, auxinfo, nun, blocks = build_system(
        fam, ATOMS, R, Ks, Av, Bv, p, target)
    basis, rank = nullspace(M, p)
    nat = len(ATOMS)
    b_can = any(int(u[bcol]) for u in basis)
    zeta_b = {auxinfo[c - nat][0]: any(int(u[c]) for u in basis)
              for c in bcolsa if c != bcol}
    print('[%s target eps^%d p=%d] system %s (%d blocks) rank=%d null=%d '
          'b!=0 possible: %s  zeta-comp B: %s'
          % (tag, target, p, M.shape, len(blocks), rank, nun - rank,
             b_can, zeta_b), flush=True)
    if not (b_can and do_extract):
        return b_can, None
    # minimal-support basis vector with b != 0
    cand = [u for u in basis if u[bcol]]
    u = min(cand, key=lambda u: int(np.count_nonzero(u[:nat])))
    sol = u * pow(int(u[bcol]), p - 2, p) % p
    resid = M.dot(sol) % p
    assert not resid.any(), 'mod-p verification failed'
    nz = [(i, int(sol[i])) for i in range(nat) if sol[i]]
    print('  minimal-support solution (b=1): %d atoms' % len(nz))
    sol_r = {}
    aux_r = {}
    recon_ok = True
    for i, val in nz:
        rr = ratrec(val, p)
        if rr is None:
            recon_ok = False
        sol_r[i] = rr
        print('    c%s = %s  (mod-p %d)' % (ATOMS[i], rr, val))
    for j, (lab, ln) in enumerate(auxinfo):
        v = int(sol[nat + j])
        if v:
            rr = ratrec(v, p)
            if rr is None:
                recon_ok = False
            aux_r[(lab, ln)] = rr
            print('    aux[%s:%s] = %s  (mod-p %d)' % (lab, ln, rr, v))
    if not recon_ok:
        print('  rational reconstruction FAILED for some coefficient; '
              'skipping exact-Q verification (mod-p only)')
        return True, (sol, None)
    ok = exact_verify(fam, sol_r, aux_r, blocks, ATOMS, target)
    print('  EXACT-Q verification (all blocks, n<=25):',
          'PASS' if ok else 'FAIL', flush=True)
    # discovered weight, human-readable (tau=1 target component = B^H_target)
    mono = {}
    for ia, cv in sol_r.items():
        lamH, _ = atom_data(fam, ATOMS[ia])
        for m, mc in expand_BH(fam, lamH, target).items():
            mono[m] = mono.get(m, F(0)) + cv * mc
    mono = {m: v for m, v in mono.items() if v}
    bcoef = aux_r.get(('r%d' % target, 'B'), F(0))
    acoef = aux_r.get(('r%d' % target, 'A'), F(0))
    print('  DISCOVERED: sum_cells S(n,.) * w(n,.) = %s * B(n) + %s * A(n), w ='
          % (bcoef, acoef))
    print('      ' + fmt_weight(fam, mono), flush=True)
    with open('eps43_%s_eps%d.pkl' % (fam.name, target), 'wb') as fh:
        pickle.dump({'family': fam.name, 'p': p, 'target': target,
                     'atoms': [(ATOMS[i], int(sol[i]), sol_r[i]) for i, _ in nz],
                     'aux': aux_r, 'weight_monomials': mono,
                     'exactQ_n25': ok}, fh)
    print('  saved -> eps43_%s.pkl' % fam.name)
    return True, (sol, (sol_r, aux_r, mono, bcoef, acoef))

# known control weights as monomial dicts (letter index by name)
def known_weight(fam):
    li = {nm: i for i, (nm, _, _) in enumerate(fam.letters)}
    if fam.name == 'franel':
        k, nk = li['k'], li['n-k']
        w = {((2, k),): F(1, 8), ((2, nk),): F(1, 8),
             ((1, k), (1, k)): F(3, 8), ((1, nk), (1, nk)): F(3, 8)}
        w[tuple(sorted([(1, k), (1, nk)]))] = F(-3, 4)
        return w
    if fam.name == 'D':
        nn, k, nk = li['n'], li['k'], li['n-k']
        w = {((2, nn),): F(1, 5), ((1, k), (1, k)): F(2, 5)}
        w[tuple(sorted([(1, k), (1, nk)]))] = F(-1, 5)
        w[tuple(sorted([(1, k), (1, nn)]))] = F(-1, 5)
        return w
    return None

def control_compare(fam, mono, bcoef, acoef, Nv=20):
    kw = known_weight(fam)
    diff = dict(mono)
    for m, v in kw.items():
        diff[m] = diff.get(m, F(0)) - bcoef * v
    diff = {m: v for m, v in diff.items() if v}
    print('  control compare: discovered - b*known has %d monomials; '
          'checking sum_cells S*diff == a*A(n), n<=%d' % (len(diff), Nv))
    ok = True
    for n in range(Nv + 1):
        tot = F(0)
        for c in fam.cells(n):
            xs = fam.args(n, c)
            wv = F(0)
            for m, cv in diff.items():
                t = cv
                for (j, L) in m:
                    t *= core.Hs(xs[L], j)
                wv += t
            tot += fam.S(n, c) * wv
        if tot != acoef * fam.A(n):
            ok = False
            print('    mismatch n=%d: %s vs %s' % (n, tot, acoef * fam.A(n)))
    print('  control compare (difference = pure A-multiple / null weight):',
          'PASS' if ok else 'FAIL', flush=True)

# ---------------- driver ----------------
def atoms_linear(dim):
    return [(u,) for u in iproduct(range(-2, 3), repeat=dim)
            if any(u)]

def atoms_quad(dim):
    out = []
    for u1 in iproduct(range(-2, 3), repeat=dim):
        for u2 in iproduct(range(-1, 2), repeat=dim):
            if any(u1) or any(u2):
                out.append((u1, u2))
    return out

def run_family(fam, N=28, P1=4194301, P2=4194247):
    t0 = time.time()
    print('\n================ FAMILY %s (dim %d, %s, target eps^%d) ========'
          % (fam.name, fam.dim, fam.rec, fam.target), flush=True)
    Av = rec_check(fam, 12)
    print('  A(n) direct sum == binomial table AND satisfies recurrence, '
          'n<=12: PASS')
    Av = [fam.A(n) for n in range(N + 1)]
    vu = ((0,) * (fam.dim - 1) + (1,), (0, 1) + (0,) * (fam.dim - 2))
    if not validate_family(fam, vu, 7, fam.cells(7)[min(2, len(fam.cells(7)) - 1)]):
        sys.exit('validation failed for family ' + fam.name)
    targets = [fam.target] + [r for r in (2, 3) if r != fam.target]
    verdict = {}
    for target in targets:
        found = False
        for deg, ATOMS in (('linear', atoms_linear(fam.dim)),
                           ('quadratic', atoms_quad(fam.dim))):
            tag = '%s %s' % (fam.name, deg)
            b_can, sol = run_scan(fam, ATOMS, Av, P1, target, N, tag)
            if b_can:
                b2, _ = run_scan(fam, ATOMS, Av, P2, target, N,
                                 tag + ' CONFIRM', do_extract=False)
                print('  second prime %d confirms b!=0: %s' % (P2, b2))
                if sol and sol[1] and fam.name in ('franel', 'D'):
                    _, (sol_r, aux_r, mono, bc, ac) = sol
                    control_compare(fam, mono, bc, ac)
                found = True
                verdict[target] = (True, deg)
                break
        if not found:
            verdict[target] = (False, 'linear+quadratic')
    print('  family %s verdicts: %s  (%.0fs)'
          % (fam.name, verdict, time.time() - t0), flush=True)
    return verdict

if __name__ == '__main__':
    t0 = time.time()
    fams = mk_fams()
    order = ['franel', 'D', 'zagierB', 'delta', 'zeta']
    if len(sys.argv) > 1:
        order = sys.argv[1].split(',')
    allv = {}
    for name in order:
        allv[name] = run_family(fams[name])
    print('\n================ SUMMARY ================')
    for name, v in allv.items():
        for tgt, (b, deg) in sorted(v.items()):
            print('  %-8s eps^%d: %s (%s)'
                  % (name, tgt, 'b != 0 REACHABLE' if b else 'b forced 0', deg))
    print('total %.0fs' % (time.time() - t0))
