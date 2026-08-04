"""eps44.py -- the three fits the sporadics paper did not run (tex ~981-984):
full-degree (degree-3 in weight-1 letters) coverage for zeta and eta in their
complete tame spaces, and for F at its seven tame arguments; pure harmonic and
chi-twisted runs for each.  Conventions follow work/SPORADIC_BARE.md exactly:

  B(n) = sum_cells S(n,cell) * w(cell),   w = sum_j c_j prod_t L_t(x_t),
  L = H^(r)(x) = sum_{m<=x} 1/m^r  or  K_chi^(r)(x) = sum_{m<=x} chi(m)/m^r,
  monomials homogeneous of total weight w (SPORADIC_BARE 2.3), all e
  (any number of K-letters), degree <= 3 in weight-1 letters (automatic at
  w <= 3 homogeneous).  B(0)=0, B(1)=1, recurrence for n >= 1.
  eta's bracket: two cells per k (binomials kept separate).
  Verdict guard: excess = rows - rank >= 40; second prime recheck 4194247.

Families (tex table ~250):
  zeta: S=C(n,k)^2 C(n,l) C(k,l) C(k+l,n), R3 (9,3,-27,0), w=3, chi_-3
  eta:  S=(-1)^k C(n,k)^3 [C(4n-5k-1,3n)+C(4n-5k,3n)], R3 (11,5,125,0), w=3, chi_5
  F:    S=(-1)^k 8^(n-k) C(n,k) C(k,l)^3, R2 (17,6,72), w=2, chi_-3
Validation control: Franel pure w=2 at {k,n-k} must come out CONSISTENT and
recover (1/4)H2_k + (3/4)H1_k(H1_k - H1_{n-k}) with exact held-out check.
"""
import sys, time, pickle
import numpy as np
from math import comb, factorial
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
from eps41 import fm, ratrec

P1, P2 = 4194301, 4194247
CHI = {'chi-3': lambda m: (0, 1, -1)[m % 3],
       'chi5':  lambda m: (0, 1, -1, -1, 1)[m % 5]}

# ---------------- families ----------------
class Fam:
    pass

def mk_fams():
    fams = {}

    z = Fam(); z.name = 'zeta'; z.w = 3; z.chi = 'chi-3'
    z.rec = ('R3', 9, 3, -27, 0)
    z.forms = ['n', 'k', 'n-k', 'l', 'n-l', 'k-l', 'k+l-n']
    def z_cells(n):
        return [(k, l) for k in range(n + 1)
                for l in range(max(0, n - k), k + 1)]
    z.cells = z_cells
    def z_args(n, c):
        k, l = c
        return [n, k, n - k, l, n - l, k - l, k + l - n]
    z.args = z_args
    z.Sx = lambda n, c: (comb(n, c[0]) ** 2 * comb(n, c[1]) * comb(c[0], c[1])
                         * comb(c[0] + c[1], n))
    fams['zeta'] = z

    e = Fam(); e.name = 'eta'; e.w = 3; e.chi = 'chi5'
    e.rec = ('R3', 11, 5, 125, 0)
    e.forms = ['n', 'k', '2k', '3k', '4k', '5k',
               'n-k', 'n-2k', 'n-3k', 'n-4k', 'n-5k']
    e.cells = lambda n: [(k, t) for k in range(n // 5 + 1) for t in (0, 1)]
    def e_args(n, c):
        k = c[0]
        return [n, k, 2 * k, 3 * k, 4 * k, 5 * k,
                n - k, n - 2 * k, n - 3 * k, n - 4 * k, n - 5 * k]
    e.args = e_args
    e.Sx = lambda n, c: ((-1) ** c[0] * comb(n, c[0]) ** 3
                         * (comb(4 * n - 5 * c[0] - 1 + c[1], 3 * n)
                            if 4 * n - 5 * c[0] - 1 + c[1] >= 0 else 0))
    fams['eta'] = e

    f = Fam(); f.name = 'F'; f.w = 2; f.chi = 'chi-3'
    f.rec = ('R2', 17, 6, 72, 0)
    f.forms = ['n', 'k', 'n-k', 'l', 'k-l', 'n-l', 'n-k+l']
    f.cells = lambda n: [(k, l) for k in range(n + 1) for l in range(k + 1)]
    def f_args(n, c):
        k, l = c
        return [n, k, n - k, l, k - l, n - l, n - k + l]
    f.args = f_args
    f.Sx = lambda n, c: ((-1) ** c[0] * 8 ** (n - c[0]) * comb(n, c[0])
                         * comb(c[0], c[1]) ** 3)
    fams['F'] = f

    fr = Fam(); fr.name = 'franel'; fr.w = 2; fr.chi = 'chi-3'
    fr.rec = ('R2', 7, 2, -8, 0)
    fr.forms = ['k', 'n-k']
    fr.cells = lambda n: [(k,) for k in range(n + 1)]
    fr.args = lambda n, c: [c[0], n - c[0]]
    fr.Sx = lambda n, c: comb(n, c[0]) ** 3
    fams['franel'] = fr
    return fams

def A_of(fam, n):
    return sum(fam.Sx(n, c) for c in fam.cells(n))

def rec_check(fam, NCH=12):
    typ, a, b, c, d = fam.rec
    Av = [A_of(fam, n) for n in range(NCH + 2)]
    for n in range(1, NCH):
        if typ == 'R2':
            r = ((n + 1) ** 2 * Av[n + 1] - (a * n * n + a * n + b) * Av[n]
                 + c * n * n * Av[n - 1])
        else:
            r = ((n + 1) ** 3 * Av[n + 1]
                 - (2 * n + 1) * (a * n * n + a * n + b) * Av[n]
                 + n * (c * n * n + d) * Av[n - 1])
        assert r == 0, (fam.name, 'A recurrence FAILS at n=%d: %s' % (n, r))
    print('  %s: A(n) direct summation satisfies recurrence, n<=%d: PASS'
          % (fam.name, NCH), flush=True)

def Bseq(fam, N):
    typ, a, b, c, d = fam.rec
    B = [F(0), F(1)]
    for n in range(1, N + 1):
        if typ == 'R2':
            nxt = F((a * n * n + a * n + b) * B[n] - c * n * n * B[n - 1],
                    (n + 1) ** 2)
        else:
            nxt = F((2 * n + 1) * (a * n * n + a * n + b) * B[n]
                    - n * (c * n * n + d) * B[n - 1], (n + 1) ** 3)
        B.append(nxt)
    return B

# ---------------- letters & monomials ----------------
def letter_list(fam, twisted):
    """[(typ,r,ai)] typ 0=H, 1=K; grouped: returns (letters, w1idx, w2idx, wWidx)"""
    NAr = len(fam.forms)
    typs = (0, 1) if twisted else (0,)
    letters = [(t, r, a) for r in range(1, fam.w + 1) for t in typs
               for a in range(NAr)]
    return letters

def monomials(fam, letters):
    li = {L: i for i, L in enumerate(letters)}
    w1 = [i for i, (t, r, a) in enumerate(letters) if r == 1]
    monos = []
    if fam.w == 2:
        monos += [(i,) for i, (t, r, a) in enumerate(letters) if r == 2]
        monos += [tuple(sorted(p)) for p in cwr(w1, 2)]
    else:
        monos += [(i,) for i, (t, r, a) in enumerate(letters) if r == 3]
        w2 = [i for i, (t, r, a) in enumerate(letters) if r == 2]
        monos += [tuple(sorted((i, j))) for i in w2 for j in w1]
        monos += [tuple(sorted(p)) for p in cwr(w1, 3)]
    return sorted(set(monos))

# ---------------- modular tables ----------------
def tables(fam, p, XMAX):
    NAr = len(fam.forms)
    chi = CHI[fam.chi]
    Ht = np.zeros((fam.w + 1, XMAX + 1), dtype=np.int64)
    Kt = np.zeros((fam.w + 1, XMAX + 1), dtype=np.int64)
    for m in range(1, XMAX + 1):
        im = pow(m, p - 2, p)
        acc = 1
        cm = chi(m) % p
        for r in range(1, fam.w + 1):
            acc = acc * im % p
            Ht[r][m] = (Ht[r][m - 1] + acc) % p
            Kt[r][m] = (Kt[r][m - 1] + cm * acc) % p
    FMAX = 4 * XMAX + 4
    fact = np.zeros(FMAX + 1, dtype=np.int64); fact[0] = 1
    for m in range(1, FMAX + 1):
        fact[m] = fact[m - 1] * m % p
    ifact = np.zeros(FMAX + 1, dtype=np.int64)
    ifact[FMAX] = pow(int(fact[FMAX]), p - 2, p)
    for m in range(FMAX, 0, -1):
        ifact[m - 1] = ifact[m] * m % p
    return Ht, Kt, fact, ifact

def cell_arrays(fam, n, p, fact, ifact):
    """args matrix [nforms, ncells], S vector mod p (vectorized)."""
    def C(a, b):
        a = np.asarray(a); b = np.asarray(b)
        ok = (b >= 0) & (a >= b) & (a >= 0)
        av = np.where(ok, a, 0); bv = np.where(ok, b, 0)
        return np.where(ok, fact[av] * ifact[bv] % p * ifact[av - bv] % p, 0)
    if fam.name == 'zeta':
        ks, ls = [], []
        for k in range(n + 1):
            for l in range(max(0, n - k), k + 1):
                ks.append(k); ls.append(l)
        k = np.array(ks, dtype=np.int64); l = np.array(ls, dtype=np.int64)
        S = (C(n, k) ** 2 % p * C(n, l) % p * C(k, l) % p * C(k + l, n) % p)
        args = np.stack([np.full_like(k, n), k, n - k, l, n - l, k - l,
                         k + l - n])
    elif fam.name == 'eta':
        kk = np.arange(n // 5 + 1, dtype=np.int64)
        k = np.repeat(kk, 2)
        t = np.tile(np.array([0, 1], dtype=np.int64), len(kk))
        sgn = np.where(k % 2 == 0, 1, p - 1)
        S = sgn * C(n, k) % p
        S = S * C(n, k) % p * C(n, k) % p * C(4 * n - 5 * k - 1 + t, 3 * n) % p
        args = np.stack([np.full_like(k, n), k, 2 * k, 3 * k, 4 * k, 5 * k,
                         n - k, n - 2 * k, n - 3 * k, n - 4 * k, n - 5 * k])
    elif fam.name == 'F':
        ks, ls = [], []
        for k in range(n + 1):
            for l in range(k + 1):
                ks.append(k); ls.append(l)
        k = np.array(ks, dtype=np.int64); l = np.array(ls, dtype=np.int64)
        sgn = np.where(k % 2 == 0, 1, p - 1)
        p8 = np.array([pow(8, int(n - kv), p) for kv in range(n + 1)],
                      dtype=np.int64)
        ckl = C(k, l)
        S = sgn * p8[k] % p * C(n, k) % p * ckl % p * ckl % p * ckl % p
        args = np.stack([np.full_like(k, n), k, n - k, l, k - l, n - l,
                         n - k + l])
    elif fam.name == 'franel':
        k = np.arange(n + 1, dtype=np.int64)
        cnk = C(n, k)
        S = cnk * cnk % p * cnk % p
        args = np.stack([k, n - k])
    return args % (10 ** 9), S

# ---------------- design matrix ----------------
def build_design(fam, p, N, twisted, verbose=True):
    letters = letter_list(fam, twisted)
    monos = monomials(fam, letters)
    ncol = len(monos)
    Ht, Kt, fact, ifact = tables(fam, p, N + 1)
    w1 = [i for i, (t, r, a) in enumerate(letters) if r == 1]
    M = np.zeros((N, ncol), dtype=np.int64)
    t0 = time.time()
    for n in range(1, N + 1):
        args, S = cell_arrays(fam, n, p, fact, ifact)
        Larr = np.empty((len(letters), args.shape[1]), dtype=np.int64)
        for i, (t, r, a) in enumerate(letters):
            Larr[i] = (Ht if t == 0 else Kt)[r][args[a]]
        row = M[n - 1]
        # cache S*Li and S*Li*Lj for weight-1 letters
        SL = {}
        for j, m in enumerate(monos):
            if len(m) == 1:
                row[j] = int(np.dot(S, Larr[m[0]]) % p)
            elif len(m) == 2:
                i0 = m[0]
                if i0 not in SL:
                    SL[i0] = S * Larr[i0] % p
                row[j] = int(np.dot(SL[i0], Larr[m[1]]) % p)
            else:
                key = (m[0], m[1])
                if key not in SL:
                    if m[0] not in SL:
                        SL[m[0]] = S * Larr[m[0]] % p
                    SL[key] = SL[m[0]] * Larr[m[1]] % p
                row[j] = int(np.dot(SL[key], Larr[m[2]]) % p)
        if verbose and n % 200 == 0:
            print('    design rows through n=%d (%.0fs)' % (n, time.time() - t0),
                  flush=True)
    return M, monos, letters

def rref_aug(M, rhs, p):
    """RREF of [M | rhs]; returns (rank, consistent, particular sol or None,
    pivot cols)."""
    A = np.concatenate([M % p, rhs[:, None] % p], axis=1)
    m, nc = A.shape
    piv = []
    r = 0
    for c in range(nc - 1):
        nz = np.nonzero(A[r:, c])[0]
        if len(nz) == 0:
            continue
        pr = r + nz[0]
        if pr != r:
            A[[r, pr]] = A[[pr, r]]
        A[r] = A[r] * pow(int(A[r, c]), p - 2, p) % p
        col = A[:, c].copy(); col[r] = 0
        mask = np.nonzero(col)[0]
        if len(mask):
            A[mask] = (A[mask] - col[mask, None] * A[r][None, :]) % p
        piv.append(c)
        r += 1
        if r == m:
            break
    consistent = not any(A[r:, -1] % p) if r < m else True
    sol = None
    if consistent:
        sol = np.zeros(nc - 1, dtype=np.int64)
        for i, c in enumerate(piv):
            sol[c] = A[i, -1]
    return len(piv), consistent, sol, piv

# ---------------- exact letters for held-out verification ----------------
def exact_letters(fam, XMAX):
    chi = CHI[fam.chi]
    H = {r: [F(0)] for r in range(1, fam.w + 1)}
    K = {r: [F(0)] for r in range(1, fam.w + 1)}
    for m in range(1, XMAX + 1):
        for r in range(1, fam.w + 1):
            H[r].append(H[r][-1] + F(1, m ** r))
            K[r].append(K[r][-1] + F(chi(m), m ** r))
    return H, K

def exact_verify(fam, monos, letters, coefs, Bx, ns):
    H, K = exact_letters(fam, max(ns) + 1)
    ok = True
    for n in ns:
        tot = F(0)
        for c in fam.cells(n):
            xs = fam.args(n, c)
            wv = F(0)
            for m, cf in zip(monos, coefs):
                if cf == 0:
                    continue
                v = cf
                for i in m:
                    t, r, a = letters[i]
                    v *= (H if t == 0 else K)[r][xs[a]]
                wv += v
            tot += fam.Sx(n, c) * wv
        if tot != Bx[n]:
            print('    EXACT held-out MISMATCH n=%d: %s != %s' % (n, tot, Bx[n]))
            ok = False
    return ok

def fmt_mono(fam, letters, m):
    return '*'.join('%s%d[%s]' % ('HK'[letters[i][0]], letters[i][1],
                                  fam.forms[letters[i][2]]) for i in m)

# ---------------- runner ----------------
def run_fit(fam, twisted, N, Bx, holdout=12):
    tag = '%s %s' % (fam.name, 'harm+%s' % fam.chi if twisted else 'pure')
    t0 = time.time()
    M, monos, letters = build_design(fam, P1, N, twisted)
    rhs = np.array([fm(Bx[n], P1) for n in range(1, N + 1)], dtype=np.int64)
    # fit on n>holdout, hold out n=1..holdout for exact verification
    fit = slice(holdout, N)
    rank, cons, sol, piv = rref_aug(M[fit], rhs[fit], P1)
    rows = N - holdout
    excess = rows - rank
    print('[%s] p=%d cols=%d rows=%d(fit n=%d..%d) rank=%d excess=%d -> %s '
          '(%.0fs)' % (tag, P1, M.shape[1], rows, holdout + 1, N, rank, excess,
                       'CONSISTENT' if cons else 'INCONSISTENT',
                       time.time() - t0), flush=True)
    assert excess >= 40, 'excess guard violated'
    # second prime
    M2, _, _ = build_design(fam, P2, N, twisted, verbose=False)
    rhs2 = np.array([fm(Bx[n], P2) for n in range(1, N + 1)], dtype=np.int64)
    rank2, cons2, sol2, _ = rref_aug(M2[fit], rhs2[fit], P2)
    print('  second prime %d: rank=%d -> %s  (agree: %s)'
          % (P2, rank2, 'CONSISTENT' if cons2 else 'INCONSISTENT',
             rank == rank2 and cons == cons2), flush=True)
    if not cons:
        return {'tag': tag, 'cols': M.shape[1], 'rank': rank, 'excess': excess,
                'consistent': False, 'p2_agrees': rank == rank2 and not cons2}
    # extraction: solution of the fit system; check it on ALL rows incl 1..12
    resid = (M.dot(sol) - rhs) % P1
    modp_all = not resid.any()
    print('  mod-p check on all rows n=1..%d incl held-out: %s'
          % (N, 'PASS' if modp_all else 'FAIL'), flush=True)
    coefs = []
    recon_ok = True
    for v in sol:
        rr = ratrec(int(v), P1)
        if rr is None:
            recon_ok = False
            rr = None
        coefs.append(rr)
    nz = [(fmt_mono(fam, letters, m), c) for m, c in zip(monos, coefs) if c]
    print('  reconstructed weight: %d nonzero terms' % len(nz))
    for s, c in nz[:60]:
        print('    %s * %s' % (c, s))
    okx = None
    if recon_ok:
        okx = exact_verify(fam, monos, letters, coefs, Bx,
                           list(range(1, holdout + 1)))
        print('  EXACT-Q held-out verification n=1..%d: %s'
              % (holdout, 'PASS' if okx else 'FAIL'), flush=True)
        # cross-check solution at second prime: reduce coefs mod P2, residual
        c2 = np.array([fm(c, P2) for c in coefs], dtype=np.int64)
        r2 = (M2.dot(c2) - rhs2) % P2
        print('  reconstructed solution verifies at second prime on all rows:',
              'PASS' if not r2.any() else 'FAIL', flush=True)
    with open('eps44_%s%s.pkl' % (fam.name, '_tw' if twisted else ''),
              'wb') as fh:
        pickle.dump({'family': fam.name, 'twisted': twisted, 'monos': monos,
                     'letters': letters, 'coefs': coefs,
                     'forms': fam.forms, 'exact_holdout': okx}, fh)
    print('  saved -> eps44_%s%s.pkl' % (fam.name, '_tw' if twisted else ''))
    return {'tag': tag, 'cols': M.shape[1], 'rank': rank, 'excess': excess,
            'consistent': True, 'exactQ': okx, 'nterms': len(nz)}

if __name__ == '__main__':
    t0 = time.time()
    fams = mk_fams()
    results = []
    # validation control: Franel must be CONSISTENT and exact-verify
    print('=== VALIDATION CONTROL: franel pure, args {k,n-k} ===')
    fr = fams['franel']
    rec_check(fr)
    Bx = Bseq(fr, 140)
    r = run_fit(fr, False, 140, Bx)
    assert r['consistent'] and r.get('exactQ'), 'control failed'
    print('control OK\n', flush=True)

    todo = [('F', False, 140), ('F', True, 260),
            ('zeta', False, 260), ('zeta', True, 880),
            ('eta', False, 520), ('eta', True, 2650)]
    if len(sys.argv) > 1:
        want = sys.argv[1].split(',')
        todo = [t for t in todo if t[0] in want]
    done_rc = set()
    for name, tw, N in todo:
        fam = fams[name]
        if name not in done_rc:
            rec_check(fam)
            done_rc.add(name)
        Bx = Bseq(fam, N)
        results.append(run_fit(fam, tw, N, Bx))
        print(flush=True)
    print('=== VERDICT TABLE ===')
    for r in results:
        if r['consistent']:
            print('  %-22s cols=%4d rank=%4d excess=%3d CONSISTENT '
                  '(%d terms, exact-Q held-out %s)'
                  % (r['tag'], r['cols'], r['rank'], r['excess'], r['nterms'],
                     r['exactQ']))
        else:
            print('  %-22s cols=%4d rank=%4d excess=%3d INCONSISTENT '
                  '(2nd prime agrees: %s)'
                  % (r['tag'], r['cols'], r['rank'], r['excess'],
                     r['p2_agrees']))
    print('total %.0fs' % (time.time() - t0))
