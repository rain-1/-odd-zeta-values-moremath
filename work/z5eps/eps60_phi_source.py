"""eps60_phi_source.py -- identify the companion SOURCE Phi(q) = t sigma^r/(P F)
for all fifteen sporadic pairs (Sol's flagship steps 1-2).

Background: the proved companion theorem gives B = F theta_q^{-r} Phi with
Phi = t sigma^r / (P F)  (eps52's Psi, construction verified n<=20 all 15).
Classical prediction (Beukers): Phi is a weight-(r+1) modular form on the
family's level -- weight 3 for the R2 six, weight 4 for the order-3 nine.

This script: exact q-series of Phi to q^26, mu-rescale (same mu as t),
integrality verdict, eta-quotient classification, and exact fit in a
per-level basis of weight-(r+1) Eisenstein series + eta-product cusp forms.
The Eisenstein/cuspidal split of Phi is the deliverable.

All arithmetic exact (Fraction).  Labels: identifications are coefficientwise
to q^25 -- [VERIFIED], never proof.
"""

import sys, os, json
from fractions import Fraction as F_

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import eps48_modular_nome as M
N = int(os.environ.get("EPS48_N", 26))
M.N = N
from eps48_modular_nome import smul, sinv, sexp, srevert, compose, gseries
import sympy as sp
th = sp.symbols('th')

FAMS = [
    # name, order(tp), a, b, c, d, level, chi, limit
    ('A',     2, 7, 2, -8, 0,   6,  '1',   'z2/4'),
    ('B',     2, 9, 3, 27, 0,  36,  'x-3', 'none'),
    ('C',     2, 10, 3, 9, 0,   6,  'x-3', 'L(x-3,2)/2'),
    ('D',     2, 11, 3, -1, 0,  5,  '1',   'z2/5'),
    ('E',     2, 12, 4, 32, 0,  8,  'x-4', 'G/2'),
    ('Ff',    2, 17, 6, 72, 0, 12,  'x-3', '5L(x-3,2)/8'),
    ('alpha', 3, 10, 4, 64, 0, 12,  '1',   '7z3/24'),
    ('gamma', 3, 17, 5, 1, 0,   6,  '1',   'z3/6'),
    ('delta', 3, 7, 3, 81, 0,  12,  '1',   'none'),
    ('eps',   3, 12, 4, 16, 0,  8,  '1',   '7z3/32'),
    ('zeta',  3, 9, 3, -27, 0,  9,  'x-3', 'L(x-3,3)/3'),
    ('eta',   3, 11, 5, 125, 0, 20, 'x5',  'none'),
    ('s7',    3, 13, 4, -27, 3, 0,  '1',   'z2/7'),
    ('s10',   3, 6, 2, -64, 4,  0,  '1',   'z2/5'),
    ('s18',   3, 14, 6, 192, -12, 0,'x-3', 'L(x-3,2)/2'),
]

def seqs(tp, a, b, c, d, n_top):
    A = [F_(1)]
    for n in range(n_top):
        if tp == 2:
            if n == 0:
                A.append(F_(b))
            else:
                A.append((F_(a*n*n + a*n + b)*A[n] - F_(c*n*n)*A[n-1])
                         / F_((n+1)**2))
        else:
            if n == 0:
                A.append(F_(b))
            else:
                A.append((F_((2*n+1)*(a*n*n + a*n + b))*A[n]
                          - F_(n*(c*n*n + d))*A[n-1]) / F_((n+1)**3))
    return A

def phi_series(name, tp, a, b, c, d):
    """exact Phi(q) = t sigma^r / (P F), plus tq for mu detection."""
    if tp == 2:
        Pj = [th**2, -sp.expand(a*th**2 + a*th + b), sp.expand(c*(th+1)**2)]
        pa, pc = -a, c
    else:
        Pj = [th**3, -sp.expand((2*th+1)*(a*th**2 + a*th + b)),
              sp.expand((th+1)*(c*(th+1)**2 + d))]
        pa, pc = -2*a, c
    A = seqs(tp, a, b, c, d, N + 2)
    y0 = A[:N+1]
    g = gseries(Pj, y0)
    qser = smul([F_(0), F_(1)] + [F_(0)]*(N-1), sexp(smul(g, sinv(y0))))
    tq = srevert(qser)
    Fq = compose(y0, tq)
    T = [tq[i+1] for i in range(N)] + [F_(0)]
    thT = [F_(i)*T[i] for i in range(len(T))]
    corr = smul(thT, sinv(T))
    sigma = list(corr)
    sigma[0] = F_(1) + corr[0]
    t2 = smul(tq, tq)
    P = [F_(0)]*(N+1); P[0] = F_(1)
    for i in range(N+1):
        P[i] += F_(pa)*tq[i] + F_(pc)*t2[i]
    sw = sigma
    for _ in range(tp - 1):
        sw = smul(sw, sigma)
    Phi = smul(smul(tq, sw), smul(sinv(P), sinv(Fq)))
    return tq, Fq, Phi

# ---- rescale (same convention as eps51: hat s_n = s_n mu^{shift-n}) ----
def detect_rescale(t):
    from sympy import primefactors
    dens = [t[i].denominator for i in range(2, min(8, len(t)))]
    if all(dd == 1 for dd in dens):
        return F_(1)
    cands = set()
    d2 = t[2].denominator
    n2 = t[2].numerator
    for s in (1, -1):
        cands.add(F_(s*d2))
        if abs(n2) > 1:
            for pf in primefactors(abs(n2)):
                cands.add(F_(s, pf)); cands.add(F_(s*pf))
    cands.add(F_(-1))
    for mu in sorted(cands, key=lambda x: (abs(x.denominator), abs(x))):
        if mu == 0: continue
        if all((t[n]*mu**(1-n)).denominator == 1 for n in range(2, N+1)):
            return mu
    return None

def rescale(ser, mu, shift=0):
    return [ser[n]*mu**(shift-n) for n in range(len(ser))]

# ---- eta classification (from eps51) ----
def product_exponents(ser, lead=0):
    s = ser[lead:] + [F_(0)]*lead
    assert s[0] != 0
    s = [x/s[0] for x in s]
    L = [F_(0)]*(N+1)
    sp_ = [F_(n)*s[n] for n in range(len(s))]
    dl = smul(sp_, sinv(s), N)
    for n in range(1, N+1):
        L[n] = dl[n]/n
    c = {}
    for n in range(1, N+1):
        acc = n*L[n]
        for j in range(1, n):
            if n % j == 0:
                acc += c[j]*j
        c[n] = -acc/n
    return c

def classify_exponents(c, upto=None):
    upto = upto or N
    vals = [c[j] for j in range(1, upto+1)]
    if any(v.denominator != 1 for v in vals):
        return ('nonintegral-exponents', None)
    iv = [int(v) for v in vals]
    for L in range(1, 37):
        e = {}; ok = True
        for m in range(1, upto+1):
            s = sum(e.get(dd, 0) for dd in range(1, m) if m % dd == 0)
            e[m] = iv[m-1] - s
            if m > L and e[m] != 0:
                ok = False; break
        if ok:
            return ('eta L<=%d' % L, {m: e[m] for m in e if e[m]})
    return ('integral, aperiodic', iv[:12])

# ---- bases ----
def chi_m3(dd): return [0, 1, -1][dd % 3]
def chi_m4(dd): return [0, 1, 0, -1][dd % 4]
def chi_5(dd):  return [0, 1, -1, -1, 1][dd % 5]

def eis_char(w, chi, mode, n=N):
    out = [F_(0)]*(n+1)
    for m in range(1, n+1):
        s = 0
        for dd in range(1, m+1):
            if m % dd == 0:
                s += (chi(dd)*dd**(w-1) if mode == 1
                      else chi(m//dd)*dd**(w-1))
        out[m] = F_(s)
    return out

def Ek(k, n=N):
    """normalized 1 - (2k/B_k) sum sigma_{k-1} q^m; use E4 = 1+240..."""
    from fractions import Fraction
    coef = {2: -24, 4: 240, 6: -504}[k]
    out = [F_(0)]*(n+1); out[0] = F_(1)
    for m in range(1, n+1):
        out[m] = F_(coef*sum(dd**(k-1) for dd in range(1, m+1) if m % dd == 0))
    return out

def qd(ser, dd, n=N):
    out = [F_(0)]*(n+1)
    for i, x in enumerate(ser):
        if i*dd <= n:
            out[i*dd] = x
    return out

def eta_pow(exps, n=N):
    """prod_m (prod_k (1-q^{mk}))^{e_m}, WITH the q^{sum m e_m /24} prefactor
    when integral; returns (shift, series) with shift = sum m e_m / 24 if in Z
    else builds without prefactor (shift None)."""
    from eps48_modular_nome import eta_quot
    ser = eta_quot(exps, n)
    tot = sum(m*e for m, e in exps.items())
    if tot % 24 == 0:
        sh = tot // 24
        out = [F_(0)]*(n+1)
        for i in range(n+1-sh):
            out[i+sh] = ser[i]
        return out
    return None

CUSP = {
    # weight 4 eta-product newforms as exponent dicts
    '5.4':  {1: 4, 5: 4},
    '6.4':  {1: 2, 2: 2, 3: 2, 6: 2},
    '8.4':  {2: 4, 4: 4},
    '9.4':  {3: 8},
}

def basis_for(level, weight, chi):
    basis, names = [], []
    one = [F_(1)] + [F_(0)]*N
    basis.append(one); names.append('1')
    divs = [dd for dd in range(1, 37) if level % dd == 0] if level else [1,2,3,4]
    if weight == 3:
        chs = {'x-3': chi_m3, 'x-4': chi_m4, 'x5': chi_5}
        for cn, cf in chs.items():
            cond = {'x-3': 3, 'x-4': 4, 'x5': 5}[cn]
            if level and level % cond != 0:
                continue
            for mode in (1, 2):
                base = eis_char(3, cf, mode)
                for dd in divs:
                    if level and (cond*dd) > level*2: pass
                    basis.append(qd(base, dd))
                    names.append('E3[%s,m%d](q^%d)' % (cn, mode, dd))
    else:  # weight 4
        e4 = Ek(4)
        for dd in divs:
            basis.append(qd(e4, dd)); names.append('E4(q^%d)' % dd)
        if chi == 'x5' and level % 5 == 0:
            for mode in (1, 2):
                base = eis_char(4, chi_5, mode)
                for dd in divs:
                    basis.append(qd(base, dd))
                    names.append('E4[x5,m%d](q^%d)' % (mode, dd))
        # cusp forms whose level divides `level` (with embeddings)
        for key, exps in CUSP.items():
            lv = int(key.split('.')[0])
            if level == 0 or level % lv:
                continue
            f = eta_pow(exps)
            if f is None: continue
            for dd in [x for x in divs if lv*x and level % (lv*x) == 0]:
                basis.append(qd(f, dd)); names.append('f%s(q^%d)' % (key, dd))
    return basis, names

def fit_series(target, basis, upto=N):
    rows = min(upto+1, len(target))
    aug = [[bb[r] if r < len(bb) else F_(0) for bb in basis] + [target[r]]
           for r in range(rows)]
    ncol = len(basis); r = 0; piv = []
    for cidx in range(ncol):
        pr = None
        for t in range(r, rows):
            if aug[t][cidx] != 0:
                pr = t; break
        if pr is None: continue
        aug[r], aug[pr] = aug[pr], aug[r]
        pv = aug[r][cidx]
        aug[r] = [x/pv for x in aug[r]]
        for t in range(rows):
            if t != r and aug[t][cidx] != 0:
                f = aug[t][cidx]
                aug[t] = [x - f*y for x, y in zip(aug[t], aug[r])]
        piv.append(cidx); r += 1
    for t in range(r, rows):
        if aug[t][ncol] != 0:
            return None
    x = [F_(0)]*ncol
    for t, cidx in enumerate(piv):
        x[cidx] = aug[t][ncol]
    return x

if __name__ == '__main__':
    results = {}
    for (name, tp, a, b, c, d, level, chi, lim) in FAMS:
        tq, Fq, Phi = phi_series(name, tp, a, b, c, d)
        mu = detect_rescale(tq)
        rec = dict(order=tp, level=level, chi=chi, limit=lim,
                   weight=tp+1, mu=str(mu))
        if mu is None:
            print('%-6s: no rescale' % name, flush=True)
            results[name] = rec; continue
        Ph = rescale(Phi, mu, shift=1)
        intP = all(x.denominator == 1 for x in Ph)
        rec['Phi_integral'] = intP
        rec['Phi_coeffs'] = [str(x) for x in Ph[:15]]
        cls = classify_exponents(product_exponents(Ph, lead=1)) if intP \
            else ('--', None)
        rec['Phi_eta_class'] = [cls[0], {str(k): v for k, v in cls[1].items()}
                                if isinstance(cls[1], dict) else cls[1]]
        print('%-6s: mu=%-4s Phi integral: %s  eta-class: %s'
              % (name, mu, intP, cls[0]), flush=True)
        if isinstance(cls[1], dict):
            print('        eta exponents:', cls[1])
        # basis fit at weight r+1
        basis, names = basis_for(level, tp+1, chi)
        x = fit_series(Ph, basis)
        if x is not None:
            nz = [(names[i], str(x[i])) for i in range(len(x)) if x[i]]
            rec['fit'] = nz
            print('        FIT (wt %d, lvl %s):' % (tp+1, level), nz)
        else:
            rec['fit'] = None
            print('        no fit in wt-%d level-%s basis (%d vectors)'
                  % (tp+1, level, len(basis)))
        results[name] = rec
    with open(os.path.join(HERE, 'eps60_results.json'), 'w') as fh:
        json.dump(results, fh, indent=1, default=str)
    print('saved eps60_results.json')
