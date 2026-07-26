"""eps22.py -- WEIGHT 5: does Delta5 = B5 - (33/4) w5sym reduce to one-variable sums?

Test:  exists antisym a with  Phi5 . (sym(Delta5) + a) = 0,
i.e.   Phi5 . a = -Phi5 . sym(Delta5)   consistent over the antisym subspace.
(Equivalent to sym(Delta5) in sym(ker Phi5); NO here excludes every
per-fixed-variable mechanism, including all Z5CF_BARNES / Z5_ORDER0 functionals.)

Monomial space: weight-5 monomials, degree <= 5, letters H^(r)_x, r=1..5,
x in the 9 bare args.  3753 monomials.  Phi5 rows = per-(n,k) sums over l.
numpy mod-p.
"""
import sys, time
import numpy as np
from math import comb
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr
from collections import Counter

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
import core

NA = 9
PERM = [0, 2, 1, 4, 3, 6, 5, 7, 8]

# ---------------- monomial basis: multisets of (r, arg) with sum r = 5 ----------------
LETTERS = [(r, a) for r in range(1, 6) for a in range(NA)]   # 45
LIDX = {la: i for i, la in enumerate(LETTERS)}

MON = []
def gen_partition_monos():
    parts_list = [
        [5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
    for parts in parts_list:
        cnt = Counter(parts)
        # choose a multiset of args for each distinct r
        groups = sorted(cnt.items())          # [(r, mult)...]
        def rec(gi, chosen):
            if gi == len(groups):
                mono = []
                for (r, _), args in zip(groups, chosen):
                    for a in args:
                        mono.append((r, a))
                MON.append(tuple(sorted(mono)))
                return
            r, mult = groups[gi]
            for args in cwr(range(NA), mult):
                rec(gi + 1, chosen + [args])
        rec(0, [])
gen_partition_monos()
MON = sorted(set(MON))
MIDX = {m: i for i, m in enumerate(MON)}
NM = len(MON)
print('weight-5 monomials:', NM)
assert NM == 3753

def mon_sigma(m):
    return tuple(sorted((r, PERM[a]) for (r, a) in m))
SIG = np.array([MIDX[mon_sigma(m)] for m in MON], dtype=np.int64)

# ---------------- Delta5 exact expansion ----------------
# family-1 t=1 letter data (per-arg coefficient of H^r_x)
Ll = [F(0), F(0), F(3), F(0), F(-1), F(0), F(-2), F(1), F(-1)]
L1 = [2 * v for v in Ll]
L2 = [F(-4), F(-8), F(10), F(-17, 4), F(-7, 4), F(0), F(8), F(2), F(-2)]
L3 = [F(0), F(0), F(24), F(0), F(-5, 3), F(0), F(-64, 3), F(8, 3), F(-8, 3)]
L4 = [F(0), F(-68), F(68), F(31, 32), F(-31, 32), F(-64), F(64), F(4), F(-4)]
L5 = [F(0), F(528, 5), F(528, 5), F(37, 40), F(37, 40), F(-512, 5), F(-512, 5),
      F(32, 5), F(-32, 5)]
ALPHA = [F(0), F(-1), F(1), F(1), F(-1), F(0), F(0), F(0), F(0)]
BETA_ = [F(0), F(-1), F(1), F(0), F(0), F(1), F(-1), F(0), F(0)]
PSI = [a / 2 + b for a, b in zip(ALPHA, BETA_)]
AMB = [a - b for a, b in zip(ALPHA, BETA_)]

VEC = {}
def addmono(m, c):
    if c:
        VEC[m] = VEC.get(m, F(0)) + c

def add_w1_prod(rlist, veclist, coef):
    """add coef * prod_i (veclist[i] . H^{rlist[i]})   -- generic product of forms"""
    def rec(i, mono, c):
        if c == 0: return
        if i == len(rlist):
            addmono(tuple(sorted(mono)), c)
            return
        v = veclist[i]
        for a in range(NA):
            if v[a]:
                rec(i + 1, mono + [(rlist[i], a)], c * v[a])
    rec(0, [], coef)

E = lambda a: [F(1) if i == a else F(0) for i in range(NA)]

# B5 = L5 + L1L4 + L2L3 + 1/2 L1^2 L3 + 1/2 L1 L2^2 + 1/6 L1^3 L2 + 1/120 L1^5
add_w1_prod([5], [L5], F(1))
add_w1_prod([4, 1], [L4, L1], F(1))
add_w1_prod([3, 2], [L3, L2], F(1))
add_w1_prod([3, 1, 1], [L3, L1, L1], F(1, 2))
add_w1_prod([2, 2, 1], [L2, L2, L1], F(1, 2))
add_w1_prod([2, 1, 1, 1], [L2, L1, L1, L1], F(1, 6))
add_w1_prod([1, 1, 1, 1, 1], [L1] * 5, F(1, 120))
# minus (33/4) * w5sym
c = F(-33, 4)
add_w1_prod([5], [E(3)], c / 2); add_w1_prod([5], [E(4)], c / 2)
add_w1_prod([4, 1], [E(3), AMB], c / 4); add_w1_prod([4, 1], [E(4), AMB], -c / 4)
# (C/2)(H3_{n+k}+H3_{n+l}),  C = 1/4(A2k+A2l) - 1/2 alpha Psi
A2SUM = {3: F(1), 4: F(1), 1: F(-1), 2: F(-1)}
for x3 in (3, 4):
    for a, ca in A2SUM.items():
        add_w1_prod([3, 2], [E(x3), E(a)], c / 2 * F(1, 4) * ca)
    add_w1_prod([3, 1, 1], [E(x3), ALPHA, PSI], -c / 4)

DELTA5 = VEC

# ---------------- exact sanity ----------------
H = core.Hs
def eval_delta5(n, k, l):
    xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
    s = F(0)
    for m, cc in DELTA5.items():
        v = cc
        for (r, a) in m:
            v *= H(xs[a], r)
        s += v
    return s

def direct_delta5(n, k, l):
    xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
    Lv = []
    for LV, r in ((L1, 1), (L2, 2), (L3, 3), (L4, 4), (L5, 5)):
        Lv.append(sum(LV[a] * H(xs[a], r) for a in range(NA)))
    l1, l2, l3, l4, l5 = Lv
    B5 = (l5 + l1 * l4 + l2 * l3 + l1 * l1 * l3 / 2 + l1 * l2 * l2 / 2
          + l1 ** 3 * l2 / 6 + l1 ** 5 / 120)
    al = sum(ALPHA[a] * H(xs[a], 1) for a in range(NA))
    be = sum(BETA_[a] * H(xs[a], 1) for a in range(NA))
    ps = al / 2 + be
    Cw = (H(n + k, 2) + H(n + l, 2) - H(k, 2) - H(l, 2)) / 4 - al * ps / 2
    w5 = (F(1, 2) * (H(n + k, 5) + H(n + l, 5))
          + (al - be) / 4 * (H(n + k, 4) - H(n + l, 4))
          + Cw / 2 * (H(n + k, 3) + H(n + l, 3)))
    return B5 - F(33, 4) * w5

bad = 0
for n in range(5):
    for k in range(n + 1):
        for l in range(n + 1):
            if eval_delta5(n, k, l) != direct_delta5(n, k, l):
                bad += 1
print('Delta5 expansion == direct, n<=4:', 'PASS' if bad == 0 else 'FAIL %d' % bad)
s = [sum(core.T(n, k, l) * eval_delta5(n, k, l)
         for k in range(n + 1) for l in range(n + 1)) for n in range(6)]
print('double sum T*Delta5 = 0, n<=5:', 'PASS' if all(v == 0 for v in s) else 'FAIL', flush=True)

# ---------------- Phi5 rows (numpy, mod p) ----------------
def build_rows(p, NROWS):
    # var-part factorisation: varying args {2,4,6,7,8}, const args {0,1,3,5}
    VARARGS = [2, 4, 6, 7, 8]
    VMAP = {a: i for i, a in enumerate(VARARGS)}
    var_parts = {}
    mono_var = np.zeros(NM, dtype=np.int64)
    mono_const = []   # list of (r,a) const letters per monomial
    for i, m in enumerate(MON):
        vp = tuple(sorted((r, VMAP[a]) for (r, a) in m if a in VMAP))
        cp = tuple((r, a) for (r, a) in m if a not in VMAP)
        if vp not in var_parts:
            var_parts[vp] = len(var_parts)
        mono_var[i] = var_parts[vp]
        mono_const.append(cp)
    NV = len(var_parts)
    vp_list = [None] * NV
    for vp, idx in var_parts.items():
        vp_list[idx] = vp
    print('distinct var-parts:', NV, flush=True)

    HM = 3 * NROWS + 2
    Ht = np.zeros((6, HM + 1), dtype=np.int64)
    for m_ in range(1, HM + 1):
        im = pow(m_, p - 2, p)
        acc = im
        Ht[1][m_] = (Ht[1][m_ - 1] + acc) % p
        for r in range(2, 6):
            acc = acc * im % p
            Ht[r][m_] = (Ht[r][m_ - 1] + acc) % p

    rows = []
    rowinfo = []
    for n in range(NROWS + 1):
        lv = np.arange(n + 1, dtype=np.int64)
        # T-values per k as needed inside loop
        for k in range(n + 1):
            xs_var = [lv, n + lv, n - lv, k + lv, n + k + lv]
            # varying letter table [5 args][r]
            VL = np.zeros((5, 6, n + 1), dtype=np.int64)
            for ai in range(5):
                for r in range(1, 6):
                    VL[ai, r] = Ht[r][xs_var[ai]]
            # var-part values
            VP = np.ones((NV, n + 1), dtype=np.int64)
            for vi, vp in enumerate(vp_list):
                acc = np.ones(n + 1, dtype=np.int64)
                for (r, ai) in vp:
                    acc = acc * VL[ai, r] % p
                VP[vi] = acc
            # T vector over l
            ck = comb(n + k, n) * comb(n, k) ** 2
            Tv = np.array([(ck * comb(n + l_, n) * comb(n, l_) ** 2
                            * comb(n + k + l_, n)) % p for l_ in range(n + 1)],
                          dtype=np.int64)
            W = (VP * Tv[None, :] % p).sum(axis=1) % p          # [NV]
            # const parts
            xc = {0: n, 1: k, 3: n + k, 5: n - k}
            cvals = np.ones(NM, dtype=np.int64)
            # build const value per monomial (vectorised by precomputed lists is
            # overkill; do it in python once per (n,k) -- 3753 small products)
            for i, cp in enumerate(mono_const):
                v = 1
                for (r, a) in cp:
                    v = v * Ht[r][xc[a]] % p
                cvals[i] = v
            row = cvals * W[mono_var] % p
            rows.append(row)
            rowinfo.append((n, k))
        if n % 10 == 0:
            print('  rows through n =', n, flush=True)
    return np.array(rows, dtype=np.int64), rowinfo

def elim_rank(Mx, p, aug=0):
    """Gaussian elimination mod p, returns (rank_full, rank_without_last_aug_cols).
    Mx modified in place. aug = number of trailing augmentation columns."""
    m, ncols = Mx.shape
    r = 0
    core_cols = ncols - aug
    rank_core = None
    for c in range(ncols):
        if c == core_cols:
            rank_core = r
        col = Mx[r:, c] % p
        nz = np.nonzero(col)[0]
        if len(nz) == 0:
            continue
        pr = r + nz[0]
        if pr != r:
            Mx[[r, pr]] = Mx[[pr, r]]
        inv = pow(int(Mx[r, c]), p - 2, p)
        Mx[r] = Mx[r] * inv % p
        col = Mx[:, c].copy()
        col[r] = 0
        mask = np.nonzero(col)[0]
        if len(mask):
            Mx[mask] = (Mx[mask] - col[mask, None] * Mx[r][None, :]) % p
        r += 1
        if r == m:
            break
    if rank_core is None:
        rank_core = r
    return r, rank_core

if __name__ == '__main__':
    p = 2147483647
    NROWS = int(sys.argv[1]) if len(sys.argv) > 1 else 58
    t0 = time.time()
    rows, rowinfo = build_rows(p, NROWS)
    print('Phi5:', rows.shape, '%.1fs' % (time.time() - t0), flush=True)

    # calibration: Ll * H4_n  must be in kernel  (per-fixed-k residue fact F1-mirror)
    cal = np.zeros(NM, dtype=np.int64)
    fm = lambda fr: fr.numerator % p * pow(fr.denominator % p, p - 2, p) % p
    for b in range(NA):
        if Ll[b]:
            m = tuple(sorted([(4, 0), (1, b)]))
            cal[MIDX[m]] = fm(Ll[b])
    resid = int(((rows * cal[None, :] % p).sum(axis=1) % p).max())
    print('calibration Ll*H4_n in ker(Phi5):', 'PASS' if resid == 0 else 'FAIL')

    # Delta5 mod p, symmetrised
    d5 = np.zeros(NM, dtype=np.int64)
    for m, cc in DELTA5.items():
        d5[MIDX[m]] = fm(cc)
    i2 = pow(2, p - 2, p)
    d5s = (d5 + d5[SIG]) * i2 % p

    # antisym orbit pairs
    idx = np.arange(NM)
    pairs = [(i, int(SIG[i])) for i in range(NM) if i < SIG[i]]
    print('antisym dim:', len(pairs))

    # A = Phi5 restricted to antisym basis (column i - column sigma(i)); rhs
    A = np.zeros((rows.shape[0], len(pairs) + 1), dtype=np.int64)
    for j, (i, si) in enumerate(pairs):
        A[:, j] = (rows[:, i] - rows[:, si]) % p
    A[:, -1] = (-((rows * d5s[None, :] % p).sum(axis=1) % p)) % p
    t0 = time.time()
    rfull, rcore = elim_rank(A, p, aug=1)
    print('rank(A) = %d, rank([A|rhs]) = %d  (%.1fs)' % (rcore, rfull, time.time() - t0))
    print('VERDICT: sym(Delta5) %s sym(ker Phi5)'
          % ('IN' if rfull == rcore else 'NOT IN'))
