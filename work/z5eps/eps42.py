"""eps42.py -- QUADRATIC (and cubic) CURVE atom pinning scan, zeta(5) program.

Curve atom us = (u1, u2[, u3]), u_i in Z^3: cell
  T(n + sum_i a_i eps^i, k + sum_i b_i eps^i, l + sum_i c_i eps^i).
Per letter L: shift s_L(eps) = sum_i d_{i,L} eps^i, d_i = dvec(u_i) (the
validated eps41 letter map).  Letter log-multiplier:
  p_L * sum_{j>=1} ((-1)^(j-1)/j) (H^(j)_{x_L} - zeta(j)[j>=2]) s_L(eps)^j
(gamma terms drop: S_1-forms sum_L p_L d_{i,L} == 0 identically, asserted).
So exp( sum_m eps^m (A_m + c_m) ) with
  A_m = sum_L p_L sum_j ((-1)^(j-1)/j) coef_{L,j,m} H^(j)_{x_L},
  coef_{L,j,m} = [eps^m] s_L^j  (polynomial in d_1..d_D),
  c_m  = sum_{j>=2} ((-1)^j/j) zeta(j) S_{j,m},  S_{j,m} = sum_L p_L coef_{L,j,m}.
Full [eps^r] cell = T * sum_{s<=r} K_{r-s} B^H_s;  K = exp series of sum c_m,
a polynomial in z2..z5 of MIXED weight (unlike eps41).  Pinning imposed per
zeta-monomial component (eps41 convention), rows linear in atoms.
"""
import sys, time, pickle
import numpy as np
from math import comb
from fractions import Fraction as F
from itertools import product as iproduct

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
import core
from eps41 import (NA, PVEC, dvec, fm, rref, nullspace, ratrec)

RMAX = 5

# ---------------- curve combinatorics ----------------
def comp_coef(ds, j, m):
    """[eps^m] (sum_i ds[i] eps^{i+1})^j, ds = per-degree d values (one letter)."""
    D = len(ds)
    total = 0
    def rec(i, jr, mr, mult, prod):
        nonlocal total
        if jr == 0:
            if mr == 0:
                total += mult * prod
            return
        if i == D or mr < jr * (i + 1):
            return
        c = 0
        while c <= jr and c * (i + 1) <= mr:
            rec(i + 1, jr - c, mr - c * (i + 1),
                mult * comb(jr, c), prod * ds[i] ** c)
            c += 1
    rec(0, j, m, 1, 1)
    return total

def atom_data(us):
    """Return (lamH, Kser):
    lamH[m] = list of (j, [9 rational coefs of H^(j)_{x_L}]),
    Kser[m] = dict {tau: Fraction} tau = sorted tuple of 'zj' strings."""
    dmat = [dvec(u) for u in us]                # [deg][letter]
    D = len(us)
    lamH, cconst = {}, {}
    for m in range(1, RMAX + 1):
        terms = []
        cm = {}
        for j in range(max(1, (m + D - 1) // D), m + 1):
            coefs = [comp_coef([dmat[i][L] for i in range(D)], j, m)
                     for L in range(NA)]
            if not any(coefs):
                continue
            fac = F((-1) ** (j - 1), j)
            vec = [fac * PVEC[L] * coefs[L] for L in range(NA)]
            terms.append((j, vec))
            S = sum(PVEC[L] * coefs[L] for L in range(NA))
            if j == 1:
                assert S == 0, 'gamma S-form nonzero: %s m=%d' % (us, m)
            elif S:
                cm[('z%d' % j,)] = F((-1) ** j, j) * S
        lamH[m] = terms
        cconst[m] = cm
    # K = exp(sum_m c_m eps^m): m K_m = sum_i i c_i K_{m-i}
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

def bellB(L, p):
    """B^H_1..5 mod p from Lam value arrays L[1..5]."""
    inv = {q: pow(q, p - 2, p) for q in (2, 6, 24, 120)}
    l1, l2, l3, l4, l5 = (L[m] for m in range(1, 6))
    l1_2 = l1 * l1 % p
    B = {1: l1 % p,
         2: (l2 + l1_2 * inv[2]) % p,
         3: (l3 + l1 * l2 + l1_2 * l1 % p * inv[6]) % p,
         4: (l4 + l1 * l3 % p + l2 * l2 % p * inv[2] + l1_2 * l2 % p * inv[2]
             + l1_2 * l1_2 % p * inv[24]) % p,
         5: (l5 + l1 * l4 % p + l2 * l3 % p + l1_2 * l3 % p * inv[2]
             + l1 * l2 % p * l2 % p * inv[2] + l1_2 * l1 % p * l2 % p * inv[6]
             + l1_2 * l1_2 % p * l1 % p * inv[120]) % p}
    return B

# ---------------- VALIDATION ----------------
def validation():
    from mpmath import mp, mpf, gamma as mpgamma, zeta as mpzeta, taylor
    mp.dps = 60
    us = ((0, 0, 1), (0, 1, 0)); n, k, l = 3, 1, 2
    xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
    T0 = core.T(n, k, l)
    lamH, K = atom_data(us)
    Aval = {m: sum(v[L] * core.Hs(xs[L], j) for (j, v) in lamH[m]
                   for L in range(NA)) for m in range(1, 6)}
    from eps41 import bell
    BH = {0: F(1)}
    for s in range(1, 5):
        BH[s] = bell(Aval, s)
    frac = lambda q: mpf(q.numerator) / mpf(q.denominator)
    zval = {'z%d' % j: mpzeta(j) for j in range(2, 6)}
    def knum(m):
        s = mpf(0)
        for t, v in K[m].items():
            term = frac(v)
            for z in t:
                term *= zval[z]
            s += term
        return s
    Knum = {m: knum(m) for m in range(5)}
    coeffs_a = [T0 * sum(Knum[w] * frac(BH[r - w]) for w in range(r + 1))
                for r in range(5)]
    dm = [dvec(u) for u in us]
    def f(e):
        out = mpf(1)
        for L in range(NA):
            out *= mpgamma(xs[L] + 1 + dm[0][L] * e + dm[1][L] * e * e) \
                   ** PVEC[L]
        return out
    coeffs_b = taylor(f, 0, 4, method='quad', radius=mpf(1) / 4)
    ok = True
    for r in range(5):
        ca, cb = coeffs_a[r], coeffs_b[r]
        agree = abs(cb - ca) < mpf(10) ** (-25) * (1 + abs(ca))
        print('  eps^%d: bell=%s  mpmath=%s  %s'
              % (r, mp.nstr(ca, 30), mp.nstr(cb, 30),
                 'AGREE' if agree else 'DISAGREE'))
        ok = ok and agree
    print('VALIDATION (quadratic curve atom):', 'PASS' if ok else 'FAIL',
          flush=True)
    return ok

# ---------------- rows ----------------
def build_rows(ATOMS, p, N):
    Xs = [[] for _ in range(NA)]
    Tm, Ni = [], []
    for n in range(N + 1):
        for k in range(n + 1):
            for l in range(n + 1):
                cell = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
                for a in range(NA):
                    Xs[a].append(cell[a])
                Tm.append(core.T(n, k, l) % p)
                Ni.append(n)
    Xs = np.array(Xs, dtype=np.int64)
    Tm = np.array(Tm, dtype=np.int64)
    Ni = np.array(Ni, dtype=np.int64)
    HM = 3 * N + 1
    Ht = np.zeros((6, HM + 1), dtype=np.int64)
    for m_ in range(1, HM + 1):
        im = pow(m_, p - 2, p)
        acc = 1
        for r in range(1, 6):
            acc = acc * im % p
            Ht[r][m_] = (Ht[r][m_ - 1] + acc) % p
    HX = np.array([[Ht[j][Xs[a]] for a in range(NA)] for j in range(1, 6)])
    nc = Xs.shape[1]
    R = np.zeros((6, len(ATOMS), N + 1), dtype=np.int64)   # s=1..5 used
    Ks = []
    t0 = time.time()
    for ia, us in enumerate(ATOMS):
        lamH, K = atom_data(us)
        Ks.append(K)
        Lam = {}
        for m in range(1, 6):
            acc = np.zeros(nc, dtype=np.int64)
            for (j, vec) in lamH[m]:
                for a in range(NA):
                    if vec[a]:
                        acc = (acc + fm(vec[a], p) * HX[j - 1][a]) % p
            Lam[m] = acc
        B = bellB(Lam, p)
        for s in range(1, 6):
            cellvals = Tm * B[s] % p
            row = np.zeros(N + 1, dtype=np.int64)
            np.add.at(row, Ni, cellvals)
            R[s][ia] = row % p
        if ia % 500 == 499:
            print('  atoms %d/%d  %.0fs' % (ia + 1, len(ATOMS),
                                            time.time() - t0), flush=True)
    lad = core.ladders()
    def L(key, n, dflt):
        return lad[key][n] if n in lad[key] else dflt
    Qv = np.array([fm(L('Q', n, F(1)), p) for n in range(N + 1)])
    Phv = np.array([fm(L('Ph', n, F(0)), p) for n in range(N + 1)])
    Pv = np.array([fm(L('P', n, F(0)), p) for n in range(N + 1)])
    return R, Ks, Qv, Phv, Pv

# ---------------- graded system ----------------
SPAN = {1: (), 2: (), 3: ('Ph', 'Q'), 4: ('Q', 'Ph', 'P'), 5: ('P', 'Q', 'Ph')}

def build_system(ATOMS, R, Ks, Qv, Phv, Pv, p, with_eps4):
    nat = len(ATOMS)
    N = len(Qv) - 1
    LADV = {'Q': Qv, 'Ph': Phv, 'P': Pv}
    rlist = [1, 2, 3, 4, 5] if with_eps4 else [1, 2, 3, 5]
    # tau list per r: all monomials in any K_m, m <= r, plus ()
    blocks = []
    for r in rlist:
        taus = set([()])
        for m in range(1, r + 1):
            for ia in range(nat):
                taus.update(Ks[ia][m].keys())
        for tau in sorted(taus):
            blocks.append((r, tau))
    naux = sum(len(SPAN[r]) for r, _ in blocks)
    nun = nat + naux
    rows, auxinfo = [], []
    bcol, pcols = None, []
    aux = nat
    for r, tau in blocks:
        label = 'r%d' % r + ('' if tau == () else '.' + '*'.join(tau))
        # base[v][n] = sum_{s=0}^{r} kappa_{r-s,tau}(v) R_s[v][n], R_0 = Qv
        base = np.zeros((nat, N + 1), dtype=np.int64)
        for ia in range(nat):
            for s in range(0, r + 1):
                kap = Ks[ia][r - s].get(tau)
                if kap is None:
                    continue
                km = fm(kap, p)
                base[ia] = (base[ia] + km * (R[s][ia] if s else Qv)) % p
        cols = list(range(aux, aux + len(SPAN[r])))
        for j, lname in zip(cols, SPAN[r]):
            auxinfo.append((label, lname))
            if lname == 'P' and r == 5:
                pcols.append(j)
                if tau == ():
                    bcol = j
        for n in range(N + 1):
            row = np.zeros(nun, dtype=np.int64)
            row[:nat] = base[:, n]
            for j, lname in zip(cols, SPAN[r]):
                row[j] = (-int(LADV[lname][n])) % p
            rows.append(row)
        aux += len(cols)
    return np.array(rows, dtype=np.int64), bcol, pcols, auxinfo, nun, blocks

def run_variant(name, ATOMS, R, Ks, Qv, Phv, Pv, p, with_eps4, pklpath=None):
    t0 = time.time()
    M, bcol, pcols, auxinfo, nun, blocks = build_system(
        ATOMS, R, Ks, Qv, Phv, Pv, p, with_eps4)
    basis, rank = nullspace(M, p)
    dim = nun - rank
    nat = len(ATOMS)
    def free(col):
        return any(int(u[col]) for u in basis)
    b_can = free(bcol)
    print('[%s] p=%d: system %s (%d blocks), rank=%d, nullspace dim=%d, '
          'b (tau=1 P-coeff of eps^5) nonzero possible: %s  (%.0fs)'
          % (name, p, M.shape, len(blocks), rank, dim, b_can, time.time() - t0))
    zfree = {auxinfo[c - nat][0]: free(c) for c in pcols if c != bcol}
    print('  zeta-component P-coeffs of eps^5 nonzero possible:', zfree)
    sol = None
    if b_can:
        u = next(u for u in basis if u[bcol])
        sol = u * pow(int(u[bcol]), p - 2, p) % p
        nz = [(ATOMS[i], int(sol[i])) for i in range(nat) if sol[i]]
        print('  solution with b=1: %d nonzero atoms (showing up to 40)' % len(nz))
        for at, val in nz[:40]:
            print('    c%s = %s  (mod-p %d)' % (at, ratrec(val, p), val))
        for j, (lab, lname) in enumerate(auxinfo):
            v = int(sol[nat + j])
            if v:
                print('    aux[%s:%s] = %s  (mod-p %d)'
                      % (lab, lname, ratrec(v, p), v))
        resid = M.dot(sol) % p
        print('  verification M.sol == 0 mod p:',
              'PASS' if not resid.any() else 'FAIL', flush=True)
        if pklpath:
            data = {'p': p, 'atoms': [(tuple(a), int(sol[i]), ratrec(int(sol[i]), p))
                                      for i, a in enumerate(ATOMS) if sol[i]],
                    'aux': [(auxinfo[j], int(sol[nat + j]),
                             ratrec(int(sol[nat + j]), p))
                            for j in range(len(auxinfo)) if sol[nat + j]]}
            with open(pklpath, 'wb') as fh:
                pickle.dump(data, fh)
            print('  saved ->', pklpath)
    return dim, b_can, sol

def make_atoms(u1rng, u2rng, u3rng=None):
    out = []
    if u3rng is None:
        for u1 in iproduct(u1rng, repeat=3):
            for u2 in iproduct(u2rng, repeat=3):
                if u1 == (0, 0, 0) and u2 == (0, 0, 0):
                    continue
                out.append((u1, u2))
    else:
        for u1 in iproduct(u1rng, repeat=3):
            for u2 in iproduct(u2rng, repeat=3):
                for u3 in u3rng:
                    if u1 == (0, 0, 0) and u2 == (0, 0, 0) and u3 == (0, 0, 0):
                        continue
                    out.append((u1, u2, u3))
    return out

if __name__ == '__main__':
    t0 = time.time()
    print('=== VALIDATION: quadratic curve atom u1=(0,0,1), u2=(0,1,0), '
          '(n,k,l)=(3,1,2) ===')
    if not validation():
        sys.exit('validation failed')
    N = 24
    P1, P2 = 4194301, 4194247
    ATOMS = make_atoms(range(-2, 3), range(-1, 2))
    print('\n=== QUADRATIC SCAN: %d atoms (u1 in {-2..2}^3, u2 in {-1,0,1}^3), '
          'N=%d, p=%d ===' % (len(ATOMS), N, P1), flush=True)
    R, Ks, Qv, Phv, Pv = build_rows(ATOMS, P1, N)
    print('rows built %.0fs' % (time.time() - t0), flush=True)
    pos = False
    for name, w4 in (('QUAD A: eps4 pinned', True),
                     ('QUAD B: eps4 unconstrained', False)):
        d, b, s = run_variant(name, ATOMS, R, Ks, Qv, Phv, Pv, P1, w4,
                              pklpath='eps42_solution.pkl' if w4 else
                                      'eps42_solution_B.pkl')
        pos = pos or b
    if pos:
        print('\n=== POSITIVE: confirm at p=%d ===' % P2, flush=True)
        R2, Ks2, Qv2, Phv2, Pv2 = build_rows(ATOMS, P2, N)
        for name, w4 in (('QUAD A p2', True), ('QUAD B p2', False)):
            run_variant(name, ATOMS, R2, Ks2, Qv2, Phv2, Pv2, P2, w4)
    else:
        CAT = make_atoms(range(-1, 2), range(-1, 2),
                         [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0),
                          (0, -1, 0), (0, 0, 1), (0, 0, -1)])
        print('\n=== CUBIC SCAN: %d atoms (u1,u2 in {-1,0,1}^3, u3 in '
              '{0,+-e_i}), N=%d, p=%d ===' % (len(CAT), N, P1), flush=True)
        R3, Ks3, Qv3, Phv3, Pv3 = build_rows(CAT, P1, N)
        print('rows built %.0fs' % (time.time() - t0), flush=True)
        cpos = False
        for name, w4 in (('CUBIC A: eps4 pinned', True),
                         ('CUBIC B: eps4 unconstrained', False)):
            d, b, s = run_variant(name, CAT, R3, Ks3, Qv3, Phv3, Pv3, P1, w4,
                                  pklpath='eps42_solution_cubic.pkl')
            cpos = cpos or b
        if cpos:
            print('\n=== CUBIC POSITIVE: confirm at p=%d ===' % P2, flush=True)
            R4, Ks4, Qv4, Phv4, Pv4 = build_rows(CAT, P2, N)
            for name, w4 in (('CUBIC A p2', True), ('CUBIC B p2', False)):
                run_variant(name, CAT, R4, Ks4, Qv4, Phv4, Pv4, P2, w4)
    print('\ntotal %.0fs' % (time.time() - t0))
