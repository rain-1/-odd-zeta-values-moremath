"""eps32.py -- round 7: NESTED (harmonic-weighted) jets.

New proved blocks (each is O(1/z), off-lattice poles inside the numerator
zero ranges of R_k, same residue-lemma mechanism as eps24):

  NQr   = sum_{j=0}^n H_j^(r)     /(z-j)      lattice, harmonic-weighted
  NQr'  = sum_{j=0}^n H_{n-j}^(r) /(z-j)      lattice, reversed weights
  NEAr  = sum_{i=1}^{k}     H_i^(r)/(z+i)     endpoint range A, ledger (1,0,0)
  NEBr  = sum_{i=k+1}^{n}   H_i^(r)/(z+i)     middle range B,  ledger (0,1,0)
  NECr  = sum_{i=n+1}^{n+k} H_i^(r)/(z+i)     endpoint range C, ledger (0,0,1)

Their residues introduce NESTED letters, encoded (code, arg):
  code 100+10r+s : nu_{r,s}(x)  = sum_{j=0..n, j!=x} H_j^(r)/(x-j)^s,
                   args x in {k,l,n-k,n-l}
  code 300+10r+s : muA_{r,s} -- at arg l: sum_{i<=k} H_i^(r)/(l+i)^s;
                   at arg k (the k<->l mirror): sum_{i<=l} H_i^(r)/(k+i)^s
  code 400+10r+s : muC analogously on (n, n+that-side]
  code 500+10r+s : muB analogously on (that-side, n]
The k<->l involution acts by the arg permutation only (codes fixed).

The target sym(Delta5) is nested-free; a span combination must cancel all
nested letters in the free ring.  Span test: eps27-level pure-ring generators
+ nested generators, lazy index, random projection mod p.

Calibration: every nested generator is checked numerically as a per-(n,k)
row identity for n <= NCAL.
"""

import sys, time, pickle, os
import numpy as np
from math import comb
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import core
import eps24, eps25, eps26, eps27
from eps24 import (f_add, f_scale, f_mul, ONE, L, s_mul, ESER, PHI)
from eps22 import DELTA5

PERM = [0, 2, 1, 4, 3, 6, 5, 7, 8]
NCAL = 11          # calibration rows n <= NCAL
PMAXS = 6          # series depth needed: [w^1] with poles order <= 2+4

# ---------------- nested blocks as series ----------------
def nu_letter(r, s):  return 100 + 10 * r + s
def muA_letter(r, s): return 300 + 10 * r + s
def muC_letter(r, s): return 400 + 10 * r + s
def muB_letter(r, s): return 500 + 10 * r + s

def block_NQ(r):
    s = {-1: {((r, 2),): F(1)}}
    for m in range(0, PMAXS + 1):
        s[m] = {((nu_letter(r, m + 1), 2),): F((-1) ** m)}
    return s

def block_NQrev(r):
    s = {-1: {((r, 6),): F(1)}}
    for m in range(0, PMAXS + 1):
        s[m] = {((nu_letter(r, m + 1), 6),): F(-1)}
    return s

def block_NE(r, code_fn):
    s = {}
    for m in range(0, PMAXS + 1):
        s[m] = {((code_fn(r, m + 1), 2),): F((-1) ** m)}
    return s

NBLOCKS = {}
for r in range(1, 4):
    NBLOCKS['NQ%d' % r] = (block_NQ(r), r + 1, (0, 0, 0))
    NBLOCKS['NR%d' % r] = (block_NQrev(r), r + 1, (0, 0, 0))
    NBLOCKS['NA%d' % r] = (block_NE(r, muA_letter), r + 1, (1, 0, 0))
    NBLOCKS['NB%d' % r] = (block_NE(r, muB_letter), r + 1, (0, 1, 0))
    NBLOCKS['NC%d' % r] = (block_NE(r, muC_letter), r + 1, (0, 0, 1))

ALPH = dict(eps27.NEWBLOCKS)
ALPH.update(NBLOCKS)
NESTED = set(NBLOCKS)

names = list(ALPH)
monos = []
def enum(idx, cur, wt, led, nnest):
    if idx == len(names):
        if nnest >= 1:
            monos.append(tuple(cur))
        return
    nm = names[idx]
    _, w, ld = ALPH[nm]
    rep = 0
    while True:
        nw = wt + rep * w
        nl = tuple(led[i] + rep * ld[i] for i in range(3))
        if nw > 4 or nl[0] > 1 or nl[1] > 2 or nl[2] > 1:
            break
        enum(idx + 1, cur + [nm] * rep, nw, nl,
             nnest + (rep if nm in NESTED else 0))
        rep += 1
enum(0, [], 0, (0, 0, 0), 0)
print('nested rho-monomials:', len(monos), flush=True)

_CACHE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/eps32_nf.pkl'
if os.path.exists(_CACHE):
    with open(_CACHE, 'rb') as fh:
        NF, NN = pickle.load(fh)
    print('nested generators (cached):', len(NF), flush=True)
else:
    NF, NN = [], []
    t0 = time.time()
    for mono in monos:
        wt = sum(ALPH[nm][1] for nm in mono)
        s = ESER
        for nm in mono:
            s = s_mul(s, ALPH[nm][0])
        base = s.get(1, {})
        if not base:
            continue
        for pm, pf in PHI[4 - wt]:
            NF.append(f_mul(base, pf))
            NN.append('N[%s]x%s' % ('.'.join(mono), pm))
    print('nested generators:', len(NF), '(%.0fs)' % (time.time() - t0),
          flush=True)
    with open(_CACHE, 'wb') as fh:
        pickle.dump((NF, NN), fh)

# ---------------- numeric letter evaluation (mod p) ----------------
def make_env(n, k, p):
    """value arrays over l = 0..n (mod p) for every letter needed."""
    HM = 3 * n + 2
    Ht = np.zeros((10, HM + 1), dtype=np.int64)
    for m_ in range(1, HM + 1):
        im = pow(m_, p - 2, p)
        acc = 1
        for r in range(1, 10):
            acc = acc * im % p
            Ht[r][m_] = (Ht[r][m_ - 1] + acc) % p
    lv = np.arange(n + 1, dtype=np.int64)
    xsv = [np.full(n + 1, n), np.full(n + 1, k), lv, np.full(n + 1, n + k),
           n + lv, np.full(n + 1, n - k), n - lv, k + lv, n + k + lv]
    inv = np.array([pow(int(x), p - 2, p) if x % p else 0
                    for x in range(-(2 * n + 1), 2 * n + 2)], dtype=np.int64)
    def invp(x):     # x array of ints in [-2n-1, 2n+1] excluding 0
        return inv[x + 2 * n + 1]
    NU = {}
    for r in range(1, 4):
        base = np.zeros(n + 1, dtype=np.int64)
        for s in range(1, PMAXS + 2):
            tab = np.zeros(n + 1, dtype=np.int64)
            for x in range(n + 1):
                j = np.arange(n + 1)
                j = j[j != x]
                iv = invp(x - j)
                tab[x] = int((Ht[r][j] * pow_arr(iv, s, p) % p).sum() % p)
            NU[(r, s)] = tab
    def mu_val(fam, r, s, a):
        out = np.zeros(n + 1, dtype=np.int64)
        for l in range(n + 1):
            rng, ev = (k, l) if a == 2 else (l, k)
            if fam == 3:
                lo, hi = 1, rng
            elif fam == 5:
                lo, hi = rng + 1, n
            else:
                lo, hi = n + 1, n + rng
            if hi < lo:
                continue
            i = np.arange(lo, hi + 1)
            iv = np.array([pow(int(ev + ii), p - 2, p) for ii in i],
                          dtype=np.int64)
            out[l] = int((Ht[r][i] * pow_arr(iv, s, p) % p).sum() % p)
        return out
    def letter(code, a):
        if code == 0:
            return xsv[a] % p
        if code < 100:
            return Ht[code][xsv[a]]
        if code < 200:
            r, s = divmod(code - 100, 10)
            return NU[(r, s)][xsv[a]]
        fam, rs = divmod(code, 100)
        r, s = divmod(rs, 10)
        return mu_val(fam, r, s, a)
    return letter

def pow_arr(a, s, p):
    out = a.copy()
    for _ in range(s - 1):
        out = out * a % p
    return out

def gen_value_modp(form, n, k, p, letter, Tv):
    tot = 0
    cache = {}
    acc = np.zeros(n + 1, dtype=np.int64)
    for mono, c in form.items():
        v = np.full(n + 1, (c.numerator % p)
                    * pow(c.denominator % p, p - 2, p) % p, dtype=np.int64)
        for la in mono:
            if la not in cache:
                cache[la] = letter(*la)
            v = v * cache[la] % p
        acc = (acc + v) % p
    return int((acc * Tv % p).sum() % p)

def mon_sigma(m):
    return tuple(sorted((c, PERM[a]) for (c, a) in m))

if __name__ == '__main__':
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 4194301
    # ---------------- calibration ----------------
    t0 = time.time()
    badset = set()
    pts = []
    for n in (6, NCAL):
        for k in sorted(set([0, 1, n // 2, n - 1, n])):
            pts.append((n, k))
    for (n, k) in pts:
        letter = make_env(n, k, p)
        Tv = np.array([core.T(n, k, l) % p for l in range(n + 1)],
                      dtype=np.int64)
        # shared letter cache across all forms at this point
        cache = {}
        def letter_cached(code, a):
            key = (code, a)
            if key not in cache:
                cache[key] = letter(code, a)
            return cache[key]
        for i, f in enumerate(NF):
            if i in badset:
                continue
            acc = np.zeros(n + 1, dtype=np.int64)
            for mono, c in f.items():
                v = np.full(n + 1, (c.numerator % p)
                            * pow(c.denominator % p, p - 2, p) % p,
                            dtype=np.int64)
                for la in mono:
                    v = v * letter_cached(*la) % p
                acc = (acc + v) % p
            if int((acc * Tv % p).sum() % p):
                badset.add(i)
        print('  point (%d,%d): cumulative failures %d (%.0fs)'
              % (n, k, len(badset), time.time() - t0), flush=True)
    bad = sorted(badset)
    print('calibration failures: %d of %d' % (len(bad), len(NF)), flush=True)
    if bad:
        print('first failures:', [NN[i] for i in bad[:15]])
    keepN = [i for i in range(len(NF)) if i not in badset]

    # ---------------- span test ----------------
    OLDF = eps24.GEN_FORMS + eps25.NEWF + eps26.EF + eps27.XF
    ALLF = OLDF + [NF[i] for i in keepN]
    monoset = set()
    for f in ALLF:
        monoset.update(f.keys())
    monoset.update(DELTA5.keys())
    monoset.update(mon_sigma(m) for m in list(monoset))
    EMON = sorted(monoset)
    EIDX = {m: i for i, m in enumerate(EMON)}
    NEM = len(EMON)
    ESIG = np.array([EIDX[mon_sigma(m)] for m in EMON], dtype=np.int64)
    print('extended monomials in play:', NEM, flush=True)

    V = np.zeros((len(ALLF), NEM), dtype=np.int64)
    for i, f in enumerate(ALLF):
        for m, c in f.items():
            V[i, EIDX[m]] = (V[i, EIDX[m]] + c.numerator % p
                             * pow(c.denominator % p, p - 2, p)) % p
    inv2 = pow(2, p - 2, p)
    Gs = (V + V[:, ESIG]) * inv2 % p
    tgt = np.zeros(NEM, dtype=np.int64)
    for m, c in DELTA5.items():
        tgt[EIDX[m]] = (c.numerator % p
                        * pow(c.denominator % p, p - 2, p)) % p
    tgt = (tgt + tgt[ESIG]) * inv2 % p

    import eps28
    NP = min(len(ALLF) + 400, NEM)
    for trial in range(2):
        rng = np.random.default_rng(4242 + trial)
        R = rng.integers(0, p, size=(NEM, NP), dtype=np.int64)
        GP = np.zeros((Gs.shape[0], NP), dtype=np.int64)
        for lo in range(0, NEM, 2048):
            hi = min(lo + 2048, NEM)
            GP = (GP + Gs[:, lo:hi].dot(R[lo:hi])) % p
        tP = tgt.dot(R) % p
        print('projection %d computed' % trial, flush=True)
        r1 = eps28.elim_rank(GP.copy(), p)
        r2 = eps28.elim_rank(np.vstack([GP, tP[None, :]]), p)
        print('projection %d: rank %d, with target %d -> %s'
              % (trial, r1, r2,
                 'IN SPAN' if r1 == r2 else 'still missing'), flush=True)
