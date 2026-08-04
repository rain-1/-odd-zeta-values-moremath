"""eps51_dictionary.py -- modular dictionary of the fifteen sporadic pairs.

For each family: exact nome computation (reusing the eps48 instrument's
method), rational rescale detection, integrality verdict, canonical
identification of t(q) and F(q) via infinite-product logarithms
(eta / generalized-eta detection) with Eisenstein fitting as fallback,
and the ASD sweep A(p) mod p vs b_p = [q^p] F(q) at p = 5,7,11,13,17,19,23.

All arithmetic exact (Fraction).  Series order N = 30.
"""

import sys
from fractions import Fraction as F
from math import comb, gcd

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import eps48_modular_nome as M

N = 26
M.N = N   # push series order into the instrument

import sympy as sp
th = sp.symbols('th')

# ---------------- family table ----------------
# (name, type, params, w, chi, limit, first-values sanity)
FAMS = [
    ('A',    'R2', (7, 2, -8),        2, '1',    'z2/4',        [1, 2, 10, 56]),
    ('B',    'R2', (9, 3, 27),        2, 'x-3',  'none',        [1, 3, 9, 21]),
    ('C',    'R2', (10, 3, 9),        2, 'x-3',  'L(x-3,2)/2',  [1, 3, 15, 93]),
    ('D',    'R2', (11, 3, -1),       2, '1',    'z2/5',        [1, 3, 19, 147]),
    ('E',    'R2', (12, 4, 32),       2, 'x-4',  'G/2',         [1, 4, 20, 112]),
    ('Ff',   'R2', (17, 6, 72),       2, 'x-3',  '5L(x-3,2)/8', [1, 6, 42, 312]),
    ('alpha','R3', (10, 4, 64, 0),    3, '1',    '7z3/24',      [1, 4, 28, 256]),
    ('gamma','R3', (17, 5, 1, 0),     3, '1',    'z3/6',        [1, 5, 73, 1445]),
    ('delta','R3', (7, 3, 81, 0),     3, '1',    'none',        [1, 3, 9, 3]),
    ('eps',  'R3', (12, 4, 16, 0),    3, '1',    '7z3/32',      [1, 4, 40, 544]),
    ('zeta', 'R3', (9, 3, -27, 0),    3, 'x-3',  'L(x-3,3)/3',  [1, 3, 27, 309]),
    ('eta',  'R3', (11, 5, 125, 0),   3, 'x5',   'none',        [1, 5, 35, 275]),
    ('s7',   'R3', (13, 4, -27, 3),   2, '1',    'z2/7',        [1, 4, 48, 760]),
    ('s10',  'R3', (6, 2, -64, 4),    2, '1',    'z2/5',        [1, 2, 18, 164]),
    ('s18',  'R3', (14, 6, 192, -12), 2, 'x-3',  'L(x-3,2)/2',  [1, 6, 54, 564]),
]

def build(fam):
    name, typ, par, w, chi, lim, sanity = fam
    if typ == 'R2':
        a, b, c = par
        A = M.A_seq_R2(a, b, c, N + 2)
        Pj = [th**2, -sp.expand(a * th**2 + a * th + b),
              sp.expand(c * (th + 1)**2)]
    else:
        a, b, c, d = par
        A = M.A_seq_R3(a, b, c, d, N + 2)
        Pj = [th**3, -sp.expand((2 * th + 1) * (a * th**2 + a * th + b)),
              sp.expand((th + 1) * (c * (th + 1)**2 + d))]
    return A, Pj

# ---------------- rescale detection ----------------
def detect_rescale(t):
    """find rational mu with t(q/mu) integral: coefficients t_n mu^{1-n} in Z.
    Returns mu (Fraction) or None."""
    from sympy import primefactors
    # candidate mu: denominator lattice; use t2..t5 denominators
    dens = [t[i].denominator for i in range(2, min(8, len(t)))]
    if all(d == 1 for d in dens):
        return F(1)
    # guess base D: den(t_{n}) should divide D^{n-1}
    cands = set()
    d2 = t[2].denominator
    for s in (1, -1):
        cands.add(F(s * d2))
        cands.add(F(s * d2, 1))
    # also numerator growth (t_n could NEED denominator mu<1)
    n2 = t[2].numerator
    for s in (1, -1):
        if abs(n2) > 1:
            for pf in primefactors(abs(n2)):
                cands.add(F(s, pf))
                cands.add(F(s * pf))
    cands.add(F(-1))
    for mu in sorted(cands, key=lambda x: (abs(x.denominator), abs(x))):
        if mu == 0:
            continue
        ok = True
        for n in range(2, N + 1):
            v = t[n] * mu ** (1 - n)
            if v.denominator != 1:
                ok = False
                break
        if ok:
            return mu
    return None

def rescale(ser, mu, shift=0):
    """coefficients of ser(q/mu) * mu^shift : s_n mu^{shift-n}."""
    return [ser[n] * mu ** (shift - n) for n in range(len(ser))]

# ---------------- product-log identification ----------------
def product_exponents(ser, lead=0):
    """ser = q^lead * prod_j (1-q^j)^{c_j}: recover c_j exactly.
    log(ser/q^lead) = sum_j c_j log(1-q^j) = -sum_j c_j sum_k q^{jk}/k."""
    # strip lead
    s = ser[lead:] + [F(0)] * lead
    assert s[0] != 0
    s = [x / s[0] for x in s]
    # log series
    L = [F(0)] * (N + 1)
    # L' = s'/s
    sp_ = [F(n) * s[n] for n in range(len(s))]
    sinv = M.sinv(s, N)
    dl = M.smul(sp_, sinv, N)     # q L'(q) coefficients: n*L_n
    for n in range(1, N + 1):
        L[n] = dl[n] / n
    # L_n = -sum_{j | n} c_j / (n/j)  =>  c_n = -(n L_n - sum_{j|n, j<n} c_j*(j/n)*n...)
    c = {}
    for n in range(1, N + 1):
        acc = L[n]
        for j in range(1, n):
            if n % j == 0 and j in c:
                acc += c[j] * F(j, n)
        c[n] = -acc * F(n, n) if False else -(acc) * n / n
        c[n] = -acc * 1
        # careful: L_n = -sum_{j|n} c_j * (1/(n/j)) = -sum c_j j/n
        # => c_n = -(n L_n + sum_{j|n,j<n} c_j j)/n
    c = {}
    for n in range(1, N + 1):
        acc = n * L[n]
        for j in range(1, n):
            if n % j == 0:
                acc += c[j] * j
        c[n] = -acc / n
    return c

def classify_exponents(c, tol_upto=None):
    upto = tol_upto or N
    vals = [c[j] for j in range(1, upto + 1)]
    if any(v.denominator != 1 for v in vals):
        return ('nonintegral-exponents', None)
    iv = [int(v) for v in vals]
    # eta-quotient: c_j = sum_{m|j} e_m, e supported on m <= 36
    for L in range(1, 37):
        e = {}
        ok = True
        for m in range(1, upto + 1):
            s = sum(e.get(d, 0) for d in range(1, m) if m % d == 0)
            e[m] = iv[m - 1] - s
            if m > L and e[m] != 0:
                ok = False
                break
        if ok:
            supp = {m: e[m] for m in e if e[m]}
            return ('eta L<=%d' % L, supp)
    # generalized eta: c_j periodic mod L
    for L in range(1, 37):
        if all(iv[j] == iv[j + L] for j in range(upto - L)):
            return ('periodic mod %d' % L, iv[:L])
    return ('integral, aperiodic', iv[:12])

# ---------------- Eisenstein bases ----------------
def chi_m3(d): return [0, 1, -1][d % 3]
def chi_m4(d): return [0, 1, 0, -1][d % 4]
def chi_5(d):  return [0, 1, -1, -1, 1][d % 5]

def E2(n=N):
    out = [F(0)] * (n + 1)
    out[0] = F(1)
    for m in range(1, n + 1):
        out[m] = F(-24 * sum(d for d in range(1, m + 1) if m % d == 0))
    return out

def qd(ser, d, n=N):
    out = [F(0)] * (n + 1)
    for i, x in enumerate(ser):
        if i * d <= n:
            out[i * d] = x
    return out

def eis_char(w, chi, mode, n=N):
    """mode 1: sum_{d|m} chi(d) d^{w-1};  mode 2: chi(m/d) d^{w-1}."""
    out = [F(0)] * (n + 1)
    for m in range(1, n + 1):
        s = 0
        for d in range(1, m + 1):
            if m % d == 0:
                s += (chi(d) * d ** (w - 1) if mode == 1
                      else chi(m // d) * d ** (w - 1))
        out[m] = F(s)
    return out

def fit_series(target, basis, upto=N):
    """exact fit target = sum c_i basis_i over Q; None or coeffs."""
    rows = min(upto + 1, len(target))
    aug = [[b[r] if r < len(b) else F(0) for b in basis] + [target[r]]
           for r in range(rows)]
    ncol = len(basis)
    r = 0
    piv = []
    for cidx in range(ncol):
        pr = None
        for t in range(r, rows):
            if aug[t][cidx] != 0:
                pr = t
                break
        if pr is None:
            continue
        aug[r], aug[pr] = aug[pr], aug[r]
        pv = aug[r][cidx]
        aug[r] = [x / pv for x in aug[r]]
        for t in range(rows):
            if t != r and aug[t][cidx] != 0:
                f = aug[t][cidx]
                aug[t] = [x - f * y for x, y in zip(aug[t], aug[r])]
        piv.append(cidx)
        r += 1
    for t in range(r, rows):
        if aug[t][ncol] != 0:
            return None
    x = [F(0)] * ncol
    for t, cidx in enumerate(piv):
        x[cidx] = aug[t][ncol]
    return x

# ---------------- main sweep ----------------
if __name__ == '__main__':
    results = {}
    PRIMES = [5, 7, 11, 13, 17, 19, 23]
    for fam in FAMS:
        name, typ, par, w, chi, lim, sanity = fam
        A, Pj = build(fam)
        assert [int(x) for x in A[:4]] == sanity, (name, A[:6])
        tq, Fq = M.nome(name, w, Pj, A)
        mu = detect_rescale(tq)
        verdict = {}
        verdict.update(dict(w=w, chi=chi, lim=lim))
        if mu is None:
            print('%-6s: NO rational rescale integralizes t(q); den profile %s'
                  % (name, [tq[i].denominator for i in range(1, 9)]), flush=True)
            verdict['integral'] = False
            results[name] = verdict
            continue
        th_ = rescale(tq, mu, shift=1)
        Fh = rescale(Fq, mu, shift=0)
        int_t = all(x.denominator == 1 for x in th_)
        int_F = all(x.denominator == 1 for x in Fh)
        cls_t = classify_exponents(product_exponents(th_, lead=1)) if int_t else ('--', None)
        cls_F = classify_exponents(product_exponents(Fh, lead=0)) if int_F else ('--', None)
        verdict.update(dict(integral=int_t and int_F, mu=str(mu),
                            t_class=cls_t, F_class=cls_F,
                            F_coeffs=[int(x) if x.denominator == 1 else str(x)
                                      for x in Fh[:14]]))
        print('%-6s: mu=%s  t,F integral: %s,%s' % (name, mu, int_t, int_F),
              flush=True)
        print('   t(q):', cls_t)
        print('   F(q):', cls_F)
        # Eisenstein fits for F if not an eta product
        if int_F and cls_F[0].startswith(('integral', 'periodic')):
            fits = {}
            if w == 2:
                e2 = E2()
                basis = [[F(1)] + [F(0)] * N] + \
                        [[d * qd(e2, d)[i] - e2[i] for i in range(N + 1)]
                         for d in (2, 3, 4, 5, 6, 7, 8, 9, 12, 16, 27)]
                bnames = ['1'] + ['%dE2(q^%d)-E2' % (d, d)
                                  for d in (2, 3, 4, 5, 6, 7, 8, 9, 12, 16, 27)]
            else:
                chs = {'x-3': chi_m3, 'x-4': chi_m4, 'x5': chi_5, '1': None}
                basis = [[F(1)] + [F(0)] * N]
                bnames = ['1']
                for cn, cf in chs.items():
                    if cf is None:
                        continue
                    for mode in (1, 2):
                        base = eis_char(3, cf, mode)
                        for d in (1, 2, 3, 4, 5, 9):
                            basis.append(qd(base, d))
                            bnames.append('E3[%s,m%d](q^%d)' % (cn, mode, d))
            x = fit_series(Fh, basis)
            if x is not None:
                nz = [(bnames[i], x[i]) for i in range(len(x)) if x[i]]
                verdict['F_eis_fit'] = [(n_, str(c)) for n_, c in nz]
                print('   F Eisenstein fit:', nz)
            else:
                print('   F Eisenstein fit: none in basis')
        # ASD sweep
        asd = {}
        for p in PRIMES:
            Ap = int(A[p]) % p
            bp = Fh[p]
            bp = int(bp) % p if bp.denominator == 1 else None
            rel = []
            if bp is not None:
                if Ap % p == bp % p:
                    rel.append('A(p)=b_p')
                if (-Ap) % p == bp % p:
                    rel.append('A(p)=-b_p')
            asd[p] = (Ap, bp, rel)
        verdict['asd'] = asd
        agree = [p for p in PRIMES if asd[p][2]]
        print('   ASD A(p) vs b_p mod p: agree at', agree, flush=True)
        results[name] = verdict

    import json
    with open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/'
              'eps51_results.json', 'w') as fh:
        json.dump({k: {kk: (vv if not isinstance(vv, tuple) else list(vv))
                       for kk, vv in v.items()} for k, v in results.items()},
                  fh, indent=1, default=str)
    print('saved eps51_results.json')
