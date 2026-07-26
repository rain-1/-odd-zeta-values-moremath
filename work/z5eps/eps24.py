"""eps24.py -- WEIGHT-5 CONSTRUCTIVE ASSEMBLY.

Goal: express sym(Delta5) as an exact monomial-ring combination of proved
one-variable generators.

Kernel (per fixed n,k):  R_k(z) = prod(z+i) prod(z+k+i) / prod_{j=0..n}(z-j)^2
 - poles: z = 0..n (order 2);  numerator zeros: z=-i simple on 1<=i<=k and
   n<i<=n+k, DOUBLE on k<i<=n.
 - local jets at z = l+w:  R_k = C(l) w^{-2} exp( sum (-1)^{m-1} G_m w^m / m ),
   C(l) = T(n,k,l) x (l-independent),  G_m = S1_m + S2_m - 2 S3_m,
   S1_m = H^m_{n+l}-H^m_l, S2_m = H^m_{n+k+l}-H^m_{k+l},
   S3_m = H^m_l + (-1)^m H^m_{n-l}.

(a) residue family:  sum_l Res_{z=l}[ R_k * rho ] = 0  for admissible rho =
    monomials in Q_r = sum_j 1/(z-j)^r (lattice), rk = sum_{i<=k}1/(z+i),
    M1 = sum_{k<i<=n}1/(z+i), M1p = sum_{n<i<=n+k}1/(z+i),
    M2 = sum_{k<i<=n}1/(z+i)^2,  with off-lattice pole ledger
    A(#rk)<=1, B(#M1+2#M2)<=2, C(#M1p)<=1.
(b) evaluation family (numerator zeros), range-summed:
    V1 (g=0, ranges in [0,n+k]), V2 (g'=0, (k,n)), V3 (q=0, ranges in [0,n]),
    V4 (q=g', (n,n+k)).
Each base is multiplied by k-side monomials phi to weight 5.
EVERY generator is calibrated against Phi5 before use.
"""
import sys, time, pickle
import numpy as np
from math import comb
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import core

NA = 9
# args: 0:n 1:k 2:l 3:n+k 4:n+l 5:n-k 6:n-l 7:k+l 8:n+k+l
KARGS = [0, 1, 3, 5]

# ---------------- sparse form algebra: dict{tuple((r,a),...): Fraction} ----------------
def f_add(f1, f2, c=F(1)):
    out = dict(f1)
    for m, v in f2.items():
        out[m] = out.get(m, F(0)) + c * v
        if out[m] == 0: del out[m]
    return out

def f_scale(f, c):
    if c == 0: return {}
    return {m: v * c for m, v in f.items()}

def f_mul(f1, f2):
    out = {}
    for m1, v1 in f1.items():
        for m2, v2 in f2.items():
            m = tuple(sorted(m1 + m2))
            out[m] = out.get(m, F(0)) + v1 * v2
            if out[m] == 0: del out[m]
    return out

ONE = {(): F(1)}
def L(r, a): return {((r, a),): F(1)}

def f_weight(f):
    ws = set(sum(r for (r, a) in m) for m in f)
    return ws

# ---------------- series: dict{power: form}, truncated to power <= PMAX ----------------
PMAX = 7   # need [w^1] after up to 4 orders of later poles; keep margin
def s_mul(s1, s2):
    out = {}
    for p1, f1 in s1.items():
        for p2, f2 in s2.items():
            p = p1 + p2
            if p > PMAX: continue
            pr = f_mul(f1, f2)
            if p in out: out[p] = f_add(out[p], pr)
            else: out[p] = pr
    return out

def s_from(terms):  # dict power->form
    return {p: dict(f) for p, f in terms.items() if f}

# ---------------- jets ----------------
def S1(m): return f_add(L(m, 4), L(m, 2), F(-1))
def S2(m): return f_add(L(m, 8), L(m, 7), F(-1))
def S3(m): return f_add(L(m, 2), L(m, 6), F((-1) ** m))
def GAM(m): return f_add(f_add(S1(m), S2(m)), S3(m), F(-2))

# E(w) = exp(sum x_m w^m), x_m = (-1)^(m-1) GAM(m)/m ; e_j via j*e_j = sum m x_m e_{j-m}
X = {m: f_scale(GAM(m), F((-1) ** (m - 1), m)) for m in range(1, 7)}
Ecoef = {0: dict(ONE)}
for j in range(1, 7):
    acc = {}
    for m in range(1, j + 1):
        acc = f_add(acc, f_mul(f_scale(X[m], F(m)), Ecoef[j - m]))
    Ecoef[j] = f_scale(acc, F(1, j))
ESER = s_from({j: Ecoef[j] for j in range(0, 7)})

# T_m = S3_m ; d-series args
def block_Q(r):
    s = {-r: dict(ONE)}
    for m in range(0, PMAX + 5):
        c = F(comb(m + r - 1, r - 1) * (-1) ** m)
        s[m] = f_scale(S3(m + r), c)
    return s_from(s)

def block_sumrange(hi_arg, lo_arg, power=1):
    """sum over a range of 1/(z+i)^power whose H-differences have args (hi,lo)."""
    s = {}
    for m in range(0, PMAX + 5):
        c = F(comb(m + power - 1, power - 1) * (-1) ** m)
        s[m] = f_scale(f_add(L(m + power, hi_arg), L(m + power, lo_arg), F(-1)), c)
    return s_from(s)

BLOCKS = {
    'Q1': (block_Q(1), 1, (0, 0, 0)),
    'Q2': (block_Q(2), 2, (0, 0, 0)),
    'Q3': (block_Q(3), 3, (0, 0, 0)),
    'Q4': (block_Q(4), 4, (0, 0, 0)),
    'rk': (block_sumrange(7, 2), 1, (1, 0, 0)),      # sum_{i<=k}: H_{k+l}-H_l
    'M1': (block_sumrange(4, 7), 1, (0, 1, 0)),      # k<i<=n:    H_{n+l}-H_{k+l}
    'M1p': (block_sumrange(8, 4), 1, (0, 0, 1)),     # n<i<=n+k:  H_{n+k+l}-H_{n+l}
    'M2': (block_sumrange(4, 7, 2), 2, (0, 2, 0)),   # k<i<=n squared
}

# admissible rho-monomials of weight <= 4
RHO_MONOS = []
names = list(BLOCKS)
def enum(idx, cur, wt, ledger):
    if idx == len(names):
        RHO_MONOS.append(tuple(cur))
        return
    nm = names[idx]
    _, w, led = BLOCKS[nm]
    maxrep = 4
    rep = 0
    while True:
        nl = tuple(ledger[i] + rep * led[i] for i in range(3))
        if wt + rep * w > 4 or nl[0] > 1 or nl[1] > 2 or nl[2] > 1:
            break
        enum(idx + 1, cur + [nm] * rep, wt + rep * w, nl)
        rep += 1
enum(0, [], 0, (0, 0, 0))
RHO_MONOS = sorted(set(tuple(sorted(m)) for m in RHO_MONOS), key=lambda m: (len(m), m))
print('admissible rho-monomials (incl. empty):', len(RHO_MONOS))

def res_form(mono):
    """[w^1] of E(w) * prod blocks  -> the residue weight (weight = wt(rho)+1)."""
    s = ESER
    for nm in mono:
        s = s_mul(s, BLOCKS[nm][0])
    f = s.get(1, {})
    return f

# ---------------- (b) evaluation bases ----------------
LKf = f_add(f_add(f_scale(L(1, 1), F(3)), L(1, 7)),
            f_add(f_add(L(1, 3), L(1, 8)), L(1, 5), F(2)), F(-1))
# L_k = 3H_k + H_{k+l} - H_{n+k} - 2H_{n-k} - H_{n+k+l}
LLf = f_add(f_add(f_scale(L(1, 2), F(3)), L(1, 7)),
            f_add(f_add(L(1, 4), L(1, 8)), L(1, 6), F(2)), F(-1))
C2f = f_add(L(2, 8), L(2, 7), F(-1))
LKLL_C2 = f_add(f_mul(LKf, LLf), C2f, F(-1))

def hdiff(r, hi, lo): return f_add(L(r, hi), L(r, lo), F(-1))

VB = []
# V1 ranges in the (j+l)-argument: endpoints {l(2), k+l(7), n+l(4), n+k+l(8)}
for (lo, hi) in [(2, 7), (2, 4), (2, 8), (7, 4), (7, 8), (4, 8)]:
    VB.append(('V1(%d,%d)' % (lo, hi),
               f_add(hdiff(2, hi, lo), f_mul(LLf, hdiff(1, hi, lo)))))
VB.append(('V2', f_add(f_scale(hdiff(3, 4, 7), F(2)), f_mul(LLf, hdiff(2, 4, 7)))))
for (lo, hi) in [(2, 7), (2, 4), (7, 4)]:
    VB.append(('V3(%d,%d)' % (lo, hi),
               f_add(f_mul(LKf, hdiff(2, hi, lo)), f_mul(LKLL_C2, hdiff(1, hi, lo)))))
VB.append(('V4', f_add(f_add(f_scale(hdiff(3, 8, 4), F(2)),
                             f_mul(f_add(LKf, LLf), hdiff(2, 8, 4))),
                       f_mul(LKLL_C2, hdiff(1, 8, 4)))))

# ---------------- phi multipliers: k-side monomials of weight q ----------------
def phis(q):
    if q == 0: return [((), ONE)]
    out = []
    # multisets of (r,a) with sum r = q, a in KARGS
    letters = [(r, a) for r in range(1, q + 1) for a in KARGS]
    def rec(start, left, cur):
        if left == 0:
            out.append((tuple(cur), None)); return
        for i in range(start, len(letters)):
            r, a = letters[i]
            if r <= left:
                rec(i, left - r, cur + [(r, a)])
    rec(0, q, [])
    res = []
    for mono, _ in out:
        f = ONE
        for (r, a) in mono:
            f = f_mul(f, L(r, a))
        res.append((mono, f))
    return res

PHI = {q: phis(q) for q in range(0, 5)}
print('phi counts:', {q: len(PHI[q]) for q in PHI})

# ---------------- assemble generators ----------------
GEN_FORMS, GEN_NAMES = [], []
for mono in RHO_MONOS:
    wt = sum(BLOCKS[nm][1] for nm in mono)
    base = res_form(mono)
    if not base: continue
    wchk = f_weight(base)
    assert wchk == {wt + 1}, (mono, wchk)
    for pm, pf in PHI[4 - wt]:
        GEN_FORMS.append(f_mul(base, pf))
        GEN_NAMES.append('R[%s]x%s' % ('.'.join(mono) if mono else '1', pm))
for nm, base in VB:
    wt = list(f_weight(base))[0]
    for pm, pf in PHI[5 - wt]:
        GEN_FORMS.append(f_mul(base, pf))
        GEN_NAMES.append('%sx%s' % (nm, pm))
print('total generators:', len(GEN_FORMS))

# ---------------- monomial index (reuse eps22) ----------------
from eps22 import MON, MIDX, NM, SIG, DELTA5

def form_to_vec_modp(f, p):
    v = np.zeros(NM, dtype=np.int64)
    for m, c in f.items():
        v[MIDX[m]] = (v[MIDX[m]] + c.numerator % p
                      * pow(c.denominator % p, p - 2, p)) % p
    return v

if __name__ == '__main__':
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 2147483647
    NROWS = 40
    from eps22 import build_rows
    t0 = time.time()
    rows, _ = build_rows(p, NROWS)
    print('Phi5 rows:', rows.shape, '%.1fs' % (time.time() - t0), flush=True)

    Gv = np.zeros((len(GEN_FORMS), NM), dtype=np.int64)
    for i, f in enumerate(GEN_FORMS):
        Gv[i] = form_to_vec_modp(f, p)
    # calibration
    t0 = time.time()
    bad = []
    for i in range(Gv.shape[0]):
        r = (rows * Gv[i][None, :] % p).sum(axis=1) % p
        if r.any(): bad.append(GEN_NAMES[i])
    print('calibration: %d of %d FAIL (%.0fs)' % (len(bad), Gv.shape[0], time.time() - t0))
    if bad:
        print('  failing (first 20):', bad[:20])
        keepi = [i for i in range(Gv.shape[0]) if GEN_NAMES[i] not in set(bad)]
    else:
        keepi = list(range(Gv.shape[0]))
    Gk = Gv[keepi]
    knames = [GEN_NAMES[i] for i in keepi]

    # sym-projection and membership
    i2 = pow(2, p - 2, p)
    fm = lambda fr: fr.numerator % p * pow(fr.denominator % p, p - 2, p) % p
    d5 = np.zeros(NM, dtype=np.int64)
    for m, cc in DELTA5.items():
        d5[MIDX[m]] = fm(cc)
    d5s = (d5 + d5[SIG]) * i2 % p
    Gs = (Gk + Gk[:, SIG]) * i2 % p

    def elim(Mx):
        m, nc = Mx.shape
        r = 0
        piv = []
        for c in range(nc):
            col = Mx[r:, c] % p
            nz = np.nonzero(col)[0]
            if len(nz) == 0: continue
            pr = r + nz[0]
            if pr != r: Mx[[r, pr]] = Mx[[pr, r]]
            inv = pow(int(Mx[r, c]), p - 2, p)
            Mx[r] = Mx[r] * inv % p
            col2 = Mx[:, c].copy(); col2[r] = 0
            nzr = np.nonzero(col2)[0]
            if len(nzr): Mx[nzr] = (Mx[nzr] - col2[nzr, None] * Mx[r][None, :]) % p
            piv.append(c); r += 1
            if r == m: break
        return r, piv

    t0 = time.time()
    A = Gs.copy()
    rG, _ = elim(A)
    B = np.vstack([Gs, d5s[None, :]])
    rGd, _ = elim(B)
    print('rank sym(gens) = %d ; with sym(Delta5) = %d  (%.0fs) -> %s'
          % (rG, rGd, time.time() - t0,
             'IN SPAN' if rGd == rG else 'NOT IN SPAN'))
    np.save('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/eps24_G_%d.npy' % p, Gs)
    with open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/eps24_names.pkl', 'wb') as fh:
        pickle.dump(knames, fh)
