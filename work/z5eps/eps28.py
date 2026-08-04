"""eps28.py -- weight-5 bridge, round 5: z-WEIGHTED lattice/endpoint jets.

New proved family:  for any ledger-admissible rho (as in eps24/26/27) and
a >= 1 with a <= decay(rho),

    sum_l Res_{z=l} [ R_k(z) * z^a * rho(z) ] = 0 ,

because R_k z^a rho = O(z^{-2}) and the off-lattice poles are unchanged.
The residue of the z-weighted kernel is NOT expressible in the pure
harmonic-monomial ring: expanding z^a = (l+w)^a mixes a polynomial letter
l (k after the k<->l mirror) with a weight-(w+1) harmonic layer.  We
therefore extend the monomial ring by polynomial letters (0, arg) whose
value is the arg itself, and run the span test in the extended graded space

    {weight-5 monomials}  (+)  {k,l} x {weight-6 monomials}     (a = 1).

Everything is calibrated numerically against the per-(n,k) rows before use.
Rank tests use two independent random column projections mod p.
"""

import sys, time, pickle
import numpy as np
from math import comb
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import core
import eps24, eps25, eps26, eps27
from eps24 import (f_add, f_scale, f_mul, ONE, L, s_mul, ESER, PHI,
                   block_Q, hdiff)
from eps25 import NEWF, NEWN
from eps26 import EF as EF26, EN as EN26
from eps27 import XF as XF27, XN as XN27, NEWBLOCKS
from eps22 import DELTA5

PERM = [0, 2, 1, 4, 3, 6, 5, 7, 8]

# ---------------- alphabet: eps27's + Q5 ----------------
ALPH = dict(NEWBLOCKS)
ALPH['Q5'] = (block_Q(5), 5, (0, 0, 0))

# z = l + w as a series (a = 1)
SER_Z = {0: {((0, 2),): F(1)}, 1: dict(ONE)}

# ---------------- enumerate admissible weighted monomials ----------------
names = list(ALPH)
monos = []
def enum(idx, cur, wt, led):
    if idx == len(names):
        if cur:
            monos.append(tuple(cur))
        return
    nm = names[idx]
    _, w, ld = ALPH[nm]
    rep = 0
    while True:
        nw = wt + rep * w
        nl = tuple(led[i] + rep * ld[i] for i in range(3))
        if nw > 5 or nl[0] > 1 or nl[1] > 2 or nl[2] > 1:
            break
        enum(idx + 1, cur + [nm] * rep, nw, nl)
        rep += 1
enum(0, [], 0, (0, 0, 0))
print('weighted rho-monomials:', len(monos), flush=True)

_CACHE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/eps28_wf.pkl'
import os
if os.path.exists(_CACHE):
    with open(_CACHE, 'rb') as fh:
        WF, WN = pickle.load(fh)
    print('z-weighted generators (cached):', len(WF), flush=True)
else:
    WF, WN = [], []
    t0 = time.time()
    for mono in monos:
        wt = sum(ALPH[nm][1] for nm in mono)
        s = s_mul(ESER, SER_Z)
        for nm in mono:
            s = s_mul(s, ALPH[nm][0])
        base = s.get(1, {})
        if not base:
            continue
        for pm, pf in PHI[5 - wt]:
            WF.append(f_mul(base, pf))
            WN.append('Rz[%s]x%s' % ('.'.join(mono), pm))
    print('z-weighted generators:', len(WF), '(%.0fs)' % (time.time() - t0),
          flush=True)
    with open(_CACHE, 'wb') as fh:
        pickle.dump((WF, WN), fh)

# ---------------- lazy extended monomial index ----------------
def mon_sigma(m):
    return tuple(sorted((r, PERM[a]) for (r, a) in m))

ALLF = eps24.GEN_FORMS + NEWF + EF26 + XF27 + WF
ALLN = eps24.GEN_NAMES + NEWN + EN26 + XN27 + WN
N_OLD = len(ALLF) - len(WF)

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

# ---------------- rows ----------------
def build_rows_ext(p, NROWS):
    # varying args {2,4,6,7,8} plus poly letter (0,2); const {0,1,3,5},(0,1),(0,0)
    VAR = {2: 0, 4: 1, 6: 2, 7: 3, 8: 4}
    var_parts, mono_var, mono_const = {}, np.zeros(NEM, dtype=np.int64), []
    for i, m in enumerate(EMON):
        vp = tuple(sorted((r, VAR[a]) for (r, a) in m if a in VAR))
        cp = tuple((r, a) for (r, a) in m if a not in VAR)
        if vp not in var_parts:
            var_parts[vp] = len(var_parts)
        mono_var[i] = var_parts[vp]
        mono_const.append(cp)
    NV = len(var_parts)
    vp_list = [None] * NV
    for vp, idx in var_parts.items():
        vp_list[idx] = vp
    print('  distinct var-parts:', NV, flush=True)

    HM = 3 * NROWS + 2
    RMAX = 8
    Ht = np.zeros((RMAX + 1, HM + 1), dtype=np.int64)
    for m_ in range(1, HM + 1):
        im = pow(m_, p - 2, p)
        acc = im
        Ht[1][m_] = (Ht[1][m_ - 1] + acc) % p
        for r in range(2, RMAX + 1):
            acc = acc * im % p
            Ht[r][m_] = (Ht[r][m_ - 1] + acc) % p

    rows, rowinfo = [], []
    for n in range(NROWS + 1):
        lv = np.arange(n + 1, dtype=np.int64)
        for k in range(n + 1):
            xs_var = [lv, n + lv, n - lv, k + lv, n + k + lv]
            VL = np.zeros((5, 9, n + 1), dtype=np.int64)
            for ai in range(5):
                for r in range(1, 9):
                    VL[ai, r] = Ht[r][xs_var[ai]]
            VP = np.ones((NV, n + 1), dtype=np.int64)
            for vi, vp in enumerate(vp_list):
                acc = np.ones(n + 1, dtype=np.int64)
                for (r, ai) in vp:
                    acc = acc * (VL[ai, r] if r else lv % p) % p
                VP[vi] = acc
            ck = comb(n + k, n) * comb(n, k) ** 2
            Tv = np.array([(ck * comb(n + l_, n) * comb(n, l_) ** 2
                            * comb(n + k + l_, n)) % p
                           for l_ in range(n + 1)], dtype=np.int64)
            W = (VP * Tv[None, :] % p).sum(axis=1) % p
            xc = {0: n, 1: k, 3: n + k, 5: n - k}
            cvals = np.ones(NEM, dtype=np.int64)
            for i, cp in enumerate(mono_const):
                v = 1
                for (r, a) in cp:
                    v = v * (Ht[r][xc[a]] if r else xc[a] % p) % p
                cvals[i] = v
            rows.append(cvals * W[mono_var] % p)
            rowinfo.append((n, k))
        if n % 10 == 0:
            print('  rows through n =', n, flush=True)
    return np.array(rows, dtype=np.int64), rowinfo


def vec_modp(f, p):
    v = np.zeros(NEM, dtype=np.int64)
    for m, c in f.items():
        v[EIDX[m]] = (v[EIDX[m]] + c.numerator % p
                      * pow(c.denominator % p, p - 2, p)) % p
    return v


def elim_rank(Mx, p):
    m, nc = Mx.shape
    r = 0
    for c in range(nc):
        nz = np.nonzero(Mx[r:, c] % p)[0]
        if not len(nz):
            continue
        pr = r + nz[0]
        if pr != r:
            Mx[[r, pr]] = Mx[[pr, r]]
        Mx[r] = Mx[r] * pow(int(Mx[r, c]), p - 2, p) % p
        col = Mx[:, c].copy(); col[r] = 0
        nzr = np.nonzero(col)[0]
        if len(nzr):
            Mx[nzr] = (Mx[nzr] - col[nzr, None] * Mx[r][None, :]) % p
        r += 1
        if r == m:
            break
    return r


if __name__ == '__main__':
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 4194301
    NROWS = 34
    rows, _ = build_rows_ext(p, NROWS)
    print('rows:', rows.shape, flush=True)

    V = np.zeros((len(ALLF), NEM), dtype=np.int64)
    t0 = time.time()
    for i, f in enumerate(ALLF):
        V[i] = vec_modp(f, p)
    print('vectorised (%.0fs)' % (time.time() - t0), flush=True)

    bad = []
    for lo in range(0, len(ALLF), 64):
        hi = min(lo + 64, len(ALLF))
        vals = rows.dot(V[lo:hi].T) % p
        for j in range(hi - lo):
            if vals[:, j].any():
                bad.append(lo + j)
    nbad_old = sum(1 for i in bad if i < N_OLD)
    nbad_new = len(bad) - nbad_old
    print('calibration failures: old %d, z-weighted %d of %d'
          % (nbad_old, nbad_new, len(WF)), flush=True)
    if nbad_new:
        print('first new failures:',
              [ALLN[i] for i in bad if i >= N_OLD][:15])
    keep = [i for i in range(len(ALLF)) if i not in set(bad)]
    G = V[keep]
    inv2 = pow(2, p - 2, p)
    Gs = (G + G[:, ESIG]) * inv2 % p

    tgt = np.zeros(NEM, dtype=np.int64)
    for m, c in DELTA5.items():
        tgt[EIDX[m]] = (c.numerator % p
                        * pow(c.denominator % p, p - 2, p)) % p
    tgt = (tgt + tgt[ESIG]) * inv2 % p

    for trial in range(2):
        rng = np.random.default_rng(1234 + trial)
        R = rng.integers(0, p, size=(NEM, 3200), dtype=np.int64)
        GP = np.zeros((Gs.shape[0], R.shape[1]), dtype=np.int64)
        for lo in range(0, NEM, 2048):
            hi = min(lo + 2048, NEM)
            GP = (GP + Gs[:, lo:hi].dot(R[lo:hi])) % p
        tP = tgt.dot(R) % p
        print('projection %d computed' % trial, flush=True)
        r1 = elim_rank(GP.copy(), p)
        r2 = elim_rank(np.vstack([GP, tP[None, :]]), p)
        print('projection %d: rank %d, with target %d -> %s'
              % (trial, r1, r2,
                 'IN SPAN' if r1 == r2 else 'still missing'), flush=True)
