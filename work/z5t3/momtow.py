"""momtow.py -- inhomogeneous moment towers for T3.

For the one-variable kernel R_k(z) = prod(z+i)prod(z+k+i)/prod_{j=0}^n(z-j)^2
and rho a monomial in the lattice blocks Q_r(z) = sum_j (z-j)^{-r}, the sum of
ALL residues of z^m R_k rho equals minus the residue at infinity:

  sum_{l=0}^n Res_{z=l}[z^m R_k rho] = -Res_infty[z^m R_k rho]
                                     = [z^{-m-1}] (R_k rho)(z->infty),

an explicit rational number e(n,k) (power-sum polynomial data).  Locally,
with z = l + w and R_k rho = gamma_k T(n,k,l) w^{-2} E(w) rhoser(w),

  Res_{z=l}[z^m R_k rho] = gamma_k T * sum_{i=0}^m C(m,i) l^{m-i}
                                        [w^{1-i}](E rhoser),

so the fact is  Sigma_l A_kl u(l) = e2(n,k)  with the density
  u(l) = kappa * sum_i C(m,i) l^{m-i} c^{(1-i)}(l),
kappa the A_kl/T normalisation, and c^{(j)} = [w^j](E rhoser) evaluated bare
forms.  These densities carry polynomial l-weights (weight-0 letters) that no
homogeneous null functional has.  Multiplying by k-side letters phi(n,k) and
summing over k gives cost values  c(n) = sum_k phi e2  which are constrained
to vanish (cost rows), so any solution proves Sigma T (target) = 0.
"""
import sys, time, pickle
import numpy as np
from fractions import Fraction as F
from math import comb

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5t3')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')

import fastlin
import eps24
from eps24 import s_mul, ESER, BLOCKS

P = int(sys.argv[sys.argv.index('-p') + 1]) if '-p' in sys.argv else 4194301
NS = (int(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith('-')
      else 20)

# ---------------- mod-p tables ----------------
MMAX = 300
HT = np.zeros((6, MMAX + 1), dtype=np.int64)
INVT = np.zeros(MMAX + 1, dtype=np.int64)
for m_ in range(1, MMAX + 1):
    INVT[m_] = pow(m_, P - 2, P)
    acc = INVT[m_]
    HT[1][m_] = (HT[1][m_ - 1] + acc) % P
    for r in range(2, 6):
        acc = acc * INVT[m_] % P
        HT[r][m_] = (HT[r][m_ - 1] + acc) % P

def hmod(x, r=1):
    return int(HT[r][max(x, 0)])

_fact = [1] * (4 * MMAX)
for i in range(1, 4 * MMAX):
    _fact[i] = _fact[i - 1] * i % P

def kappa_mod(n, k):
    """gamma_k^{-1}-free normalisation: a_l = gamma_k T; A_kl = (-1)^n T/n!;
    we work directly in T-units: Sigma_l T u = e with e in T-units."""
    return 1

# ---------------- rho menu and local series ----------------
RHOS = [((), 0), (('Q1',), 1), (('Q2',), 2), (('Q1', 'Q1'), 2)]

def rho_series(mono):
    s_ = ESER
    for nm in mono:
        s_ = s_mul(s_, BLOCKS[nm][0])
    return s_

RHO_SER = {mono: rho_series(mono) for mono, _ in RHOS}
RHO_QL = {mono: q for mono, q in RHOS}

def eval_form_modp(form, xs):
    tot = 0
    for m, c in form.items():
        v = c.numerator % P * pow(c.denominator % P, P - 2, P) % P
        for (r, a) in m:
            v = v * hmod(xs[a], r) % P
        tot = (tot + v) % P
    return tot

# ---------------- infinity expansion of R_k rho (numeric, mod p) ---------
def powsum(a, b, m):
    """sum_{t=a}^{b} t^m mod P (small ranges, direct)."""
    return sum(pow(t, m, P) for t in range(a, b + 1)) % P

def rk_inf_series(n, k, deg):
    """coefficients c_0..c_deg of R_k(z) = z^{-2}(c_0 + c_1/z + ...)."""
    # log R_k = sum_m [(-1)^(m-1)(S_m(1..n)+S_m(k+1..k+n)) + 2 S_m(0..n)]/(m z^m)
    lg = [0] * (deg + 1)
    for m_ in range(1, deg + 1):
        v = ((-1) ** (m_ - 1) * (powsum(1, n, m_) + powsum(k + 1, k + n, m_))
             + 2 * powsum(0, n, m_)) % P
        lg[m_] = v * pow(m_, P - 2, P) % P
    # exponentiate
    E = [0] * (deg + 1)
    E[0] = 1
    for j in range(1, deg + 1):
        acc = 0
        for m_ in range(1, j + 1):
            acc = (acc + m_ * lg[m_] % P * E[j - m_]) % P
        E[j] = acc * pow(j, P - 2, P) % P
    return E

def q_inf_series(n, r, deg):
    """Q_r(z) = z^{-r} sum_m C(m+r-1,r-1) S_m(0..n) z^{-m} coefficients."""
    out = [0] * (deg + 1)
    for m_ in range(0, deg + 1):
        out[m_] = comb(m_ + r - 1, r - 1) % P * powsum(0, n, m_) % P
    return out

def inf_coeff(n, k, mono, m):
    """[z^{-m-1}] of R_k rho  (equals -Res_infty[z^m R_k rho])."""
    qlat = RHO_QL[mono]
    # R_k rho = z^{-2-qlat} * (series product); need coefficient of z^{-m-1}
    # i.e. series coefficient at index m+1-2-qlat = m-1-qlat
    idx = m - 1 - qlat
    if idx < 0:
        return 0
    deg = idx
    ser = rk_inf_series(n, k, deg)
    for nm in mono:
        r = int(nm[1])
        qs = q_inf_series(n, r, deg)
        new = [0] * (deg + 1)
        for i in range(deg + 1):
            if ser[i]:
                for j in range(deg + 1 - i):
                    new[i + j] = (new[i + j] + ser[i] * qs[j]) % P
        ser = new
    return ser[idx]

# ---------------- density and cost of a moment fact ----------------------
def mom_density(n, k, l, mono, m):
    """u(l) with Sigma_l T(n,k,l) u(l) = e2(n,k) = inf_coeff (T-units).

    Res_{z=l}[z^m R_k rho] = gamma_k T sum_i C(m,i) l^{m-i} [w^{1-i}](E rhoser)
    and the identity divides by gamma_k on both sides; we fold gamma_k into
    the cost instead:  Sigma_l T u = inf_coeff/gamma_k =: cost."""
    s_ = RHO_SER[mono]
    xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
    tot = 0
    for i in range(0, m + 1):
        f = s_.get(1 - i)
        if not f:
            continue
        cv = eval_form_modp(f, xs)
        tot = (tot + comb(m, i) % P * pow(l, m - i, P) % P * cv) % P
    return tot

def gamma_mod(n, k):
    """a_l / T = k!^3 (n-k)!^2 / ((n+k)! n!)  mod P."""
    num = pow(_fact[k], 3, P) * pow(_fact[n - k], 2, P) % P
    den = _fact[n + k] * _fact[n] % P
    return num * pow(den, P - 2, P) % P

# k-side letter monomials, weights 0..3 (args n,k,n+k,n-k)
def phik_menu(wmax=3):
    letters = [(r, a) for r in range(1, wmax + 1) for a in (0, 1, 3, 5)]
    out = [()]
    def rec(start, left, cur):
        if left == 0:
            return
        for ai in range(start, len(letters)):
            r, a = letters[ai]
            if r <= left:
                out.append(tuple(cur + [(r, a)]))
                rec(ai, left - r, cur + [(r, a)])
    rec(0, wmax, [])
    return sorted(set(out))

PHIK = phik_menu()

def phik_val(mono, n, k):
    xs = [n, k, None, n + k, None, n - k]
    v = 1
    for (r, a) in mono:
        v = v * hmod(xs[a], r) % P
    return v

def mom_columns_spec():
    cols = []
    for mono, qlat in RHOS:
        for m in (1, 2, 3):
            for pk in PHIK:
                cols.append(('MT[%s|m%d]x%s' % ('.'.join(mono) or '1', m, pk),
                             (mono, m, pk)))
    return cols

if __name__ == '__main__':
    t0 = time.time()
    spec = mom_columns_spec()
    print('moment-tower columns:', len(spec), flush=True)

    d = np.load('sys3_%d_n%d.npz' % (P, NS))
    A3, B3, D3, t, Lk, DD = d['A'], d['B'], d['D'], d['t'], d['Lk'], d['DD']
    meta = pickle.load(open('live3_blocks_n%d.pkl' % NS, 'rb'))
    cells = meta['cells']
    Ffold = (A3 + Lk[:, None] * B3 % P + DD[:, None] * D3 % P) % P
    b = (t[:, 0] + Lk * t[:, 1] + DD * t[:, 2]) % P

    # sanity: verify the moment identity numerically for a few (n,k,mono,m)
    from math import comb as C_
    def Tmod(n, k, l):
        return (C_(n + k, n) * C_(n, k) ** 2 * C_(n + l, n)
                * C_(n, l) ** 2 * C_(n + k + l, n)) % P
    ok = True
    for (n, k) in ((3, 1), (4, 2), (5, 0), (6, 5)):
        for mono, _ in RHOS:
            for m in (1, 2, 3):
                s = 0
                for l in range(n + 1):
                    s = (s + Tmod(n, k, l) * mom_density(n, k, l, mono, m)) % P
                rhs = inf_coeff(n, k, mono, m) * pow(gamma_mod(n, k),
                                                     P - 2, P) % P
                if s != rhs:
                    ok = False
                    print('MOMENT FAIL', n, k, mono, m, s, rhs)
    print('moment identity sanity:', 'PASS' if ok else 'FAIL', flush=True)
    if not ok:
        sys.exit(1)

    # build columns on cells (symmetrised) + cost values per (column, n)
    ncols = len(spec)
    MT = np.zeros((len(cells), ncols), dtype=np.int64)
    i2 = (P + 1) // 2
    for ci, (n, k, l) in enumerate(cells):
        dens = {}
        for mono, _ in RHOS:
            for m in (1, 2, 3):
                dens[(mono, m, 0)] = mom_density(n, k, l, mono, m)
                dens[(mono, m, 1)] = mom_density(n, l, k, mono, m)
        pkv = {}
        for pk in PHIK:
            pkv[(pk, 0)] = phik_val(pk, n, k)
            pkv[(pk, 1)] = phik_val(pk, n, l)
        for si, (nm, (mono, m, pk)) in enumerate(spec):
            v1 = dens[(mono, m, 0)] * pkv[(pk, 0)] % P
            v2 = dens[(mono, m, 1)] * pkv[(pk, 1)] % P
            MT[ci, si] = (v1 + v2) * i2 % P
        if ci % 400 == 0:
            print('  cell %d/%d %.0fs' % (ci, len(cells), time.time() - t0),
                  flush=True)
    # cost rows: for each n in range, sum_k phi(n,k) * e(n,k) (both orientations
    # give the same after symmetrisation: cost = sum_k phi e, no 1/2)
    nvals = sorted(set(c[0] for c in cells))
    COST = np.zeros((len(nvals), ncols), dtype=np.int64)
    for ni, n in enumerate(nvals):
        for si, (nm, (mono, m, pk)) in enumerate(spec):
            acc = 0
            for k in range(n + 1):
                e = inf_coeff(n, k, mono, m) * pow(gamma_mod(n, k), P - 2, P) % P
                acc = (acc + phik_val(pk, n, k) * e) % P
            COST[ni, si] = acc
    print('cost rows built %.0fs' % (time.time() - t0), flush=True)

    # assemble: [Ffold | MT ; 0 | COST]
    top = np.concatenate([Ffold, MT], axis=1)
    bot = np.concatenate([np.zeros((len(nvals), Ffold.shape[1]),
                                   dtype=np.int64), COST], axis=1)
    A = np.concatenate([top, bot], axis=0)
    bb = np.concatenate([b, np.zeros(len(nvals), dtype=np.int64)])
    x, rk, piv, nbad = fastlin.solve(A, bb, P)
    print('[folded+MT] system %s rank=%d nbad=%d  (was 514 without MT)'
          % (A.shape, rk, nbad), flush=True)
    np.save('mt_x_%d_n%d.npy' % (P, NS), x)
