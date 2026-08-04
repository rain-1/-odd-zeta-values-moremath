"""eps41.py -- directional-atom pinning scan for the zeta(5) program.

Atom v=(alpha,beta,gamma): deformed cell T(n+a*eps, k+b*eps, l+g*eps).
Exact expansion T*exp(sum_m eps^m Lam_m^v), Lam_m^v = ((-1)^(m-1)/m) *
sum_L p_L d_L^m H^{(m)}_{x_L}, letters x_L in
[n,k,l,n+k,n+l,n-k,n-l,k+l,n+k+l], p = [1,-3,-3,1,1,-2,-2,-1,1],
d = [a,b,g,a+b,a+g,a-b,a-g,b+g,a+b+g].

VALIDATION 1: atom (0,0,1), n=3,k=1,l=2 vs direct sympy gamma-product series.
SCAN: atoms in {-2..2}^3\\{0}; pin [eps^1]=[eps^2]=0, [eps^3] in span{Phat,Q},
[eps^4] in span{Q,Phat,P} (variant A) or free (variant B),
[eps^5] = b*P + span{Q,Phat} with b != 0 the prize.
"""
import sys, time
import numpy as np
from fractions import Fraction as F
from itertools import product as iproduct

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
import core

NA = 9
PVEC = [1, -3, -3, 1, 1, -2, -2, -1, 1]

def dvec(v):
    a, b, g = v
    return [a, b, g, a + b, a + g, a - b, a - g, b + g, a + b + g]

# Bell polynomials B_r in terms of Lam_1..Lam_5 (values or symbols)
def bell(L, r):
    l1, l2, l3, l4, l5 = L[1], L[2], L[3], L[4], L[5]
    if r == 1: return l1
    if r == 2: return l2 + l1 * l1 / 2
    if r == 3: return l3 + l1 * l2 + l1**3 / 6
    if r == 4: return l4 + l1 * l3 + l2 * l2 / 2 + l1 * l1 * l2 / 2 + l1**4 / 24
    return (l5 + l1 * l4 + l2 * l3 + l1 * l1 * l3 / 2 + l1 * l2 * l2 / 2
            + l1**3 * l2 / 6 + l1**5 / 120)

# ---------- monomial-dict expansion of B_r^v (eps22 style), used in validation ----
BELL_TERMS = {
    1: [([1], F(1))],
    2: [([2], F(1)), ([1, 1], F(1, 2))],
    3: [([3], F(1)), ([1, 2], F(1)), ([1, 1, 1], F(1, 6))],
    4: [([4], F(1)), ([1, 3], F(1)), ([2, 2], F(1, 2)), ([1, 1, 2], F(1, 2)),
        ([1, 1, 1, 1], F(1, 24))],
    5: [([5], F(1)), ([1, 4], F(1)), ([2, 3], F(1)), ([1, 1, 3], F(1, 2)),
        ([1, 2, 2], F(1, 2)), ([1, 1, 1, 2], F(1, 6)),
        ([1, 1, 1, 1, 1], F(1, 120))],
}

def lam_vec(v, m):
    """Lam_m^v as per-arg coefficient vector (of letters H^{(m)}_{x_L})."""
    d = dvec(v)
    c = F((-1) ** (m - 1), m)
    return [c * PVEC[a] * F(d[a]) ** m for a in range(NA)]

def expand_atom(v, r):
    """B_r^v as dict {sorted tuple of (m, argindex): Fraction}."""
    vecs = {m: lam_vec(v, m) for m in range(1, r + 1)}
    out = {}
    for mlist, coef in BELL_TERMS[r]:
        def rec(i, mono, c):
            if c == 0:
                return
            if i == len(mlist):
                key = tuple(sorted(mono))
                out[key] = out.get(key, F(0)) + c
                if out[key] == 0:
                    del out[key]
                return
            vv = vecs[mlist[i]]
            for a in range(NA):
                if vv[a]:
                    rec(i + 1, mono + [(mlist[i], a)], c * vv[a])
        rec(0, [], coef)
    return out

def eval_mono_dict(D, xs):
    s = F(0)
    for m, cc in D.items():
        val = cc
        for (r, a) in m:
            val *= core.Hs(xs[a], r)
        s += val
    return s

# ---------------- constant (zeta) part ----------------
def Smom(v, m):
    d = dvec(v)
    return sum(PVEC[a] * d[a] ** m for a in range(NA))

# Full Lam_m = A_m + c_m with A_m the H-part above and constants
#   c_1 = -gamma * S_1(v)  (identically 0: S_1 == 0 for all atoms, asserted below)
#   c_m = ((-1)^m / m) * zeta(m) * S_m(v),  m >= 2.
# exp(sum c_m eps^m) = sum_j K_j eps^j; K_j homogeneous of zeta-weight j:
#   K_0=1, K_1=0, K_2=c_2, K_3=c_3, K_4=c_4+c_2^2/2, K_5=c_5+c_2*c_3
# so [eps^r](cell) = T * sum_w K_w(v) * B^H_{r-w}(v), with B^H_0 = 1.
# kappa coefficients (rational, per atom) of each zeta-monomial tau:
def kappas(v):
    S2, S3, S4, S5 = (Smom(v, m) for m in (2, 3, 4, 5))
    return {('z2',): F(S2, 2), ('z3',): F(-S3, 3),
            ('z4',): F(S4, 4), ('z2', 'z2'): F(S2, 2) ** 2 / 2,
            ('z5',): F(-S5, 5), ('z2', 'z3'): F(S2, 2) * F(-S3, 3)}

TAU_W = {('z2',): 2, ('z3',): 3, ('z4',): 4, ('z2', 'z2'): 4,
         ('z5',): 5, ('z2', 'z3'): 5}

# ---------------- VALIDATION STEP 1 ----------------
def validation():
    import sympy as sp
    v = (0, 0, 1); n, k, l = 3, 1, 2
    xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
    d = dvec(v)
    T0 = core.T(n, k, l)
    assert Smom(v, 1) == 0
    # (a) Lam/Bell construction: H-part via monomial dicts + zeta constants
    Lval = {m: sum(lam_vec(v, m)[a] * core.Hs(xs[a], m) for a in range(NA))
            for m in range(1, 6)}
    BH = {0: F(1)}
    for r in (1, 2, 3):
        BH[r] = bell(Lval, r)
        md = expand_atom(v, r)
        assert eval_mono_dict(md, xs) == BH[r], 'mono-dict mismatch r=%d' % r
    kap = kappas(v)
    zval = {'z2': sp.zeta(2), 'z3': sp.zeta(3), 'z4': sp.zeta(4), 'z5': sp.zeta(5)}
    Knum = {0: sp.Integer(1), 1: sp.Integer(0)}
    for w in (2, 3):
        Knum[w] = sum(sp.Rational(kap[t].numerator, kap[t].denominator)
                      * sp.prod(zval[z] for z in t)
                      for t in kap if TAU_W[t] == w)
    coeffs_a = [T0 * sum(Knum[w] * sp.Rational(BH[r - w].numerator,
                                               BH[r - w].denominator)
                         for w in range(r + 1)) for r in range(4)]
    # (b) direct sympy gamma product
    eps = sp.symbols('eps')
    f = sp.prod(sp.gamma(xs[a] + 1 + d[a] * eps) ** PVEC[a] for a in range(NA))
    ser = sp.series(f, eps, 0, 4).removeO()
    ok = True
    for r in range(4):
        cb = sp.N(ser.coeff(eps, r), 30)
        ca = sp.N(coeffs_a[r], 30)
        agree = abs(cb - ca) < 10 ** (-20) * (1 + abs(ca))
        print('  eps^%d: bell=%s  sympy=%s  %s'
              % (r, ca, cb, 'AGREE' if agree else 'DISAGREE'))
        ok = ok and agree
    print('VALIDATION 1:', 'PASS' if ok else 'FAIL', flush=True)
    return ok

# ---------------- rows mod p ----------------
def fm(fr, p):
    fr = F(fr)
    return fr.numerator % p * pow(fr.denominator % p, p - 2, p) % p

def build_all(p, N):
    """Return ATOMS list, R[r][ia][n] mod p, and ladder vectors Qv,Phv,Pv."""
    ATOMS = [v for v in iproduct(range(-2, 3), repeat=3) if v != (0, 0, 0)]
    # cells
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
    HX = np.array([[Ht[m][Xs[a]] for a in range(NA)] for m in range(1, 6)])
    inv = {q: pow(q, p - 2, p) for q in range(1, 121)}
    R = np.zeros((6, len(ATOMS), N + 1), dtype=np.int64)
    for ia, v in enumerate(ATOMS):
        d = dvec(v)
        Lam = {}
        for m in range(1, 6):
            cm = (-1) ** (m - 1) * inv[m] % p
            acc = np.zeros(Xs.shape[1], dtype=np.int64)
            for a in range(NA):
                co = cm * (PVEC[a] * d[a] ** m % p) % p
                if co:
                    acc = (acc + co * HX[m - 1][a]) % p
            Lam[m] = acc
        l1, l2, l3, l4, l5 = (Lam[m] for m in range(1, 6))
        i2, i6, i24, i120 = inv[2], inv[6], inv[24], inv[120]
        l1_2 = l1 * l1 % p
        B = {1: l1,
             2: (l2 + l1_2 * i2) % p,
             3: (l3 + l1 * l2 + l1_2 % p * l1 % p * i6) % p,
             4: (l4 + l1 * l3 % p + l2 * l2 % p * i2 + l1_2 * l2 % p * i2
                 + l1_2 * l1_2 % p * i24) % p,
             5: (l5 + l1 * l4 % p + l2 * l3 % p + l1_2 * l3 % p * i2
                 + l1 * l2 % p * l2 % p * i2 + l1_2 * l1 % p * l2 % p * i6
                 + l1_2 * l1_2 % p * l1 % p * i120) % p}
        for r in range(1, 6):
            cellvals = Tm * (B[r] % p) % p
            R[r][ia] = np.zeros(N + 1, dtype=np.int64)
            np.add.at(R[r][ia], Ni, cellvals)
            R[r][ia] %= p
    lad = core.ladders()
    def L(key, n, dflt):
        return lad[key][n] if n in lad[key] else dflt
    Qv = np.array([fm(L('Q', n, F(1)), p) for n in range(N + 1)])
    Phv = np.array([fm(L('Ph', n, F(0)), p) for n in range(N + 1)])
    Pv = np.array([fm(L('P', n, F(0)), p) for n in range(N + 1)])
    return ATOMS, R, Qv, Phv, Pv

# ---------------- linear algebra mod p ----------------
def rref(M, p):
    M = M.copy() % p
    m, nc = M.shape
    piv = []
    r = 0
    for c in range(nc):
        nz = np.nonzero(M[r:, c])[0]
        if len(nz) == 0:
            continue
        pr = r + nz[0]
        if pr != r:
            M[[r, pr]] = M[[pr, r]]
        M[r] = M[r] * pow(int(M[r, c]), p - 2, p) % p
        col = M[:, c].copy(); col[r] = 0
        mask = np.nonzero(col)[0]
        if len(mask):
            M[mask] = (M[mask] - col[mask, None] * M[r][None, :]) % p
        piv.append(c)
        r += 1
        if r == m:
            break
    return M, piv

def nullspace(M, p):
    R_, piv = rref(M, p)
    nc = M.shape[1]
    free = [c for c in range(nc) if c not in piv]
    basis = []
    for fc in free:
        x = np.zeros(nc, dtype=np.int64)
        x[fc] = 1
        for i, pc in enumerate(piv):
            x[pc] = (-int(R_[i, fc])) % p
        basis.append(x)
    return basis, len(piv)

def ratrec(x, p):
    """Rational reconstruction of x mod p."""
    x %= p
    a, b, u, v = p, x, 0, 1
    while b * b * 2 > p:
        q = a // b
        a, b, u, v = b, a - q * b, v, u - q * v
    if v == 0 or abs(v) * abs(v) * 2 > p:
        return None
    if v < 0:
        b, v = -b, -v
    return F(b, v)

# ---------------- the scan ----------------
def block_list(with_eps4):
    """Each block: (label, s = which pure-H row R_s, tau = zeta-monomial or (),
    span = tuple of ladder names allowed).  Derived from
    [eps^r] = sum_w K_w(v) B^H_{r-w}; tau components of full weight r are
    automatic Q-multiples (skipped for r>=3; scalar constraint for r=2)."""
    B = [('r1', 1, (), ()),
         ('r2', 2, (), ()),
         ('r2.z2*Q  (scalar)', 0, ('z2',), 'SCALAR'),
         ('r3', 3, (), ('Ph', 'Q')),
         ('r3.z2', 1, ('z2',), ('Ph', 'Q'))]
    if with_eps4:
        B += [('r4', 4, (), ('Q', 'Ph', 'P')),
              ('r4.z2', 2, ('z2',), ('Q', 'Ph', 'P')),
              ('r4.z3', 1, ('z3',), ('Q', 'Ph', 'P'))]
    B += [('r5', 5, (), ('P', 'Q', 'Ph')),
          ('r5.z2', 3, ('z2',), ('P', 'Q', 'Ph')),
          ('r5.z3', 2, ('z3',), ('P', 'Q', 'Ph')),
          ('r5.z4', 1, ('z4',), ('P', 'Q', 'Ph')),
          ('r5.z2^2', 1, ('z2', 'z2'), ('P', 'Q', 'Ph'))]
    return B

def build_system(ATOMS, R, Qv, Phv, Pv, p, with_eps4):
    nat = len(ATOMS)
    N = len(Qv) - 1
    LADV = {'Q': Qv, 'Ph': Phv, 'P': Pv}
    blocks = block_list(with_eps4)
    naux = sum(len(b[3]) for b in blocks if b[3] != 'SCALAR')
    nun = nat + naux
    rows = []
    auxinfo = []          # (label, ladder) per aux column, in order
    bcol = None
    pcols = []            # all P aux columns of r5-family blocks
    aux = nat
    for label, s, tau, span in blocks:
        if tau:
            kap = np.array([fm(kappas(v)[tau], p) for v in ATOMS],
                           dtype=np.int64)
        else:
            kap = np.ones(nat, dtype=np.int64)
        if span == 'SCALAR':
            row = np.zeros(nun, dtype=np.int64)
            row[:nat] = kap        # sum_v c_v kappa(v) = 0  (times Q_n)
            rows.append(row)
            continue
        base = (R[s] * kap[:, None]) % p if s > 0 else \
               (kap[:, None] * Qv[None, :]) % p
        cols = list(range(aux, aux + len(span)))
        for j, lname in zip(cols, span):
            auxinfo.append((label, lname))
            if lname == 'P' and label.startswith('r5'):
                pcols.append(j)
                if label == 'r5':
                    bcol = j
        for n in range(N + 1):
            row = np.zeros(nun, dtype=np.int64)
            row[:nat] = base[:, n]
            for j, lname in zip(cols, span):
                row[j] = (-int(LADV[lname][n])) % p
            rows.append(row)
        aux += len(span)
    return np.array(rows, dtype=np.int64), bcol, pcols, auxinfo, nun

def run_variant(name, ATOMS, R, Qv, Phv, Pv, p, with_eps4):
    M, bcol, pcols, auxinfo, nun = build_system(ATOMS, R, Qv, Phv, Pv, p,
                                                with_eps4)
    basis, rank = nullspace(M, p)
    dim = nun - rank
    def forced_zero(col):
        eb = np.zeros((1, nun), dtype=np.int64); eb[0, col] = 1
        _, r2 = nullspace(np.vstack([M, eb]), p)
        return r2 == rank
    b_can = not forced_zero(bcol)
    print('[%s] p=%d: system %s, rank=%d, nullspace dim=%d, '
          'b (tau=1 P-coeff of eps^5) nonzero possible: %s'
          % (name, p, M.shape, rank, dim, b_can))
    assert b_can == any(int(u[bcol]) for u in basis), 'b-coordinate consistency'
    zc = [c for c in pcols if c != bcol]
    zeta_b = [not forced_zero(c) for c in zc]
    print('  zeta-component P-coeffs of eps^5 nonzero possible:',
          dict(zip([auxinfo[c - len(ATOMS)][0] for c in zc], zeta_b)))
    sol = None
    if b_can:
        u = next(u for u in basis if u[bcol])
        sol = u * pow(int(u[bcol]), p - 2, p) % p   # normalize b = 1
        nz = [(ATOMS[i], int(sol[i])) for i in range(len(ATOMS)) if sol[i]]
        print('  solution with b=1: %d nonzero atoms' % len(nz))
        for at, val in nz:
            print('    c%s = %s  (mod-p %d)' % (at, ratrec(val, p), val))
        for j, (lab, lname) in enumerate(auxinfo):
            v = int(sol[len(ATOMS) + j])
            if v:
                print('    aux[%s:%s] = %s  (mod-p %d)' % (lab, lname,
                                                           ratrec(v, p), v))
        resid = M.dot(sol) % p
        print('  verification M.sol == 0 mod p:',
              'PASS' if not resid.any() else 'FAIL', flush=True)
        # explicit condition re-check on the tau=1 components
        c = sol[:len(ATOMS)]
        s = {r: (R[r].T.dot(c)) % p for r in range(1, 6)}
        ok = (not s[1].any()) and (not s[2].any())
        A = {(lab, ln): int(sol[len(ATOMS) + j])
             for j, (lab, ln) in enumerate(auxinfo)}
        ok &= not ((s[3] - A[('r3', 'Ph')] * Phv - A[('r3', 'Q')] * Qv) % p).any()
        if with_eps4:
            ok &= not ((s[4] - A[('r4', 'Q')] * Qv - A[('r4', 'Ph')] * Phv
                        - A[('r4', 'P')] * Pv) % p).any()
        ok &= not ((s[5] - A[('r5', 'P')] * Pv - A[('r5', 'Q')] * Qv
                    - A[('r5', 'Ph')] * Phv) % p).any()
        print('  explicit tau=1 condition re-check:', 'PASS' if ok else 'FAIL')
    return dim, b_can, sol

if __name__ == '__main__':
    t0 = time.time()
    print('=== VALIDATION STEP 1: atom (0,0,1), n=3,k=1,l=2 ===')
    if not validation():
        sys.exit('validation failed -- p/d conventions wrong')
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    P1, P2 = 4194301, 4194247
    print('\n=== SCAN, N = %d, prime %d ===' % (N, P1), flush=True)
    ATOMS, R, Qv, Phv, Pv = build_all(P1, N)
    # sanity: atoms (1,0,0)+(0,1,0)+(0,0,1)... no fixed identity; instead check
    # sum_kl T*B_1 for atom (0,0,1) at small n against exact
    v = (0, 0, 1); ia = ATOMS.index(v)
    ex = sum(core.T(2, k, l) * eval_mono_dict(expand_atom(v, 1),
             [2, k, l, 2 + k, 2 + l, 2 - k, 2 - l, k + l, 2 + k + l])
             for k in range(3) for l in range(3))
    assert R[1][ia][2] == fm(ex, P1), 'row sanity'
    print('row sanity (exact vs mod-p, atom (0,0,1), r=1, n=2): PASS')
    print('atoms:', len(ATOMS), ' build %.1fs' % (time.time() - t0), flush=True)

    results = {}
    for name, w4 in (('A: eps4 pinned to span{Q,Phat,P}', True),
                     ('B: eps4 unconstrained', False)):
        results[name] = run_variant(name, ATOMS, R, Qv, Phv, Pv, P1, w4)

    if any(rv[1] for rv in results.values()):
        print('\n=== POSITIVE FINDING: second prime %d ===' % P2, flush=True)
        ATOMS2, R2, Qv2, Phv2, Pv2 = build_all(P2, N)
        for name, w4 in (('A: eps4 pinned to span{Q,Phat,P}', True),
                         ('B: eps4 unconstrained', False)):
            run_variant(name, ATOMS2, R2, Qv2, Phv2, Pv2, P2, w4)
        print('\n=== robustness: N = %d, prime %d ===' % (N + 12, P1), flush=True)
        ATOMS3, R3, Qv3, Phv3, Pv3 = build_all(P1, N + 12)
        for name, w4 in (('A: eps4 pinned to span{Q,Phat,P}', True),
                         ('B: eps4 unconstrained', False)):
            run_variant(name, ATOMS3, R3, Qv3, Phv3, Pv3, P1, w4)
    print('\ntotal %.1fs' % (time.time() - t0))
