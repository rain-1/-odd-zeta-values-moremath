"""eps28b.py -- round 6-lite: z^2-weighted jets + z-weighted towers.

Adds to the eps28 extended framework:
 (i)  a = 2 residue jets  sum_l Res[R_k z^2 rho] = 0, decay(rho) >= 2;
 (ii) z-weighted VALUE towers: expand R_k z rho in lattice partial fractions;
      evaluating at numerator zeros -j gives range-summed identities whose
      coefficients now carry the polynomial letter l;
 (iii) z-weighted DERIVATIVE towers on the double-zero middle range.

Same lazy extended index and projection rank test as eps28.
"""

import sys, time, pickle, os
import numpy as np
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')

import eps24, eps25, eps26, eps27, eps28
from eps24 import (f_add, f_scale, f_mul, ONE, s_mul, ESER, PHI, hdiff)
from eps25 import RANGES
from eps28 import (ALPH, SER_Z, monos as WMONOS, ALLF as ALLF28,
                   ALLN as ALLN28, mon_sigma)
from eps22 import DELTA5

SER_Z2 = {0: {((0, 2), (0, 2)): F(1)}, 1: {((0, 2),): F(2)}, 2: dict(ONE)}

_CACHE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/eps28b_wf.pkl'
if os.path.exists(_CACHE):
    with open(_CACHE, 'rb') as fh:
        BF, BN = pickle.load(fh)
    print('eps28b generators (cached):', len(BF), flush=True)
else:
    BF, BN = [], []
    t0 = time.time()
    # (i) z^2 jets: decay(rho) = weight >= 2
    for mono in WMONOS:
        wt = sum(ALPH[nm][1] for nm in mono)
        if wt < 2:
            continue
        s = s_mul(ESER, SER_Z2)
        for nm in mono:
            s = s_mul(s, ALPH[nm][0])
        base = s.get(1, {})
        if not base:
            continue
        for pm, pf in PHI[5 - wt]:
            BF.append(f_mul(base, pf))
            BN.append('Rz2[%s]x%s' % ('.'.join(mono), pm))
    print('z^2 jets:', len(BF), '(%.0fs)' % (time.time() - t0), flush=True)

    # (ii)+(iii) z-weighted towers over admissible monomials (incl. empty rho)
    n1 = len(BF)
    for mono in [()] + list(WMONOS):
        wt = sum(ALPH[nm][1] for nm in mono)
        if wt > 3:
            continue
        led = tuple(sum(ALPH[nm][2][i] for nm in mono) for i in range(3))
        qlat = sum(int(nm[1]) for nm in mono if nm.startswith('Q'))
        pole_order = 2 + qlat
        s = s_mul(ESER, SER_Z)
        for nm in mono:
            s = s_mul(s, ALPH[nm][0])
        cs = {t: s.get(2 - t, {}) for t in range(1, pole_order + 1)}
        valid = {'A': led[0] == 0, 'B': led[1] <= 1, 'C': led[2] == 0}
        for rnm, ((lo, hi), regs) in RANGES.items():
            if not all(valid[r] for r in regs):
                continue
            base = {}
            for t in range(1, pole_order + 1):
                if cs[t]:
                    base = f_add(base, f_mul(cs[t], hdiff(t, hi, lo)),
                                 F((-1) ** t))
            if not base:
                continue
            for pm, pf in PHI[3 - wt]:
                BF.append(f_mul(base, pf))
                BN.append('EVz[%s|%s]x%s'
                          % ('.'.join(mono) if mono else '1', rnm, pm))
        if wt <= 2 and led[1] == 0:
            base = {}
            for t in range(1, pole_order + 1):
                if cs[t]:
                    base = f_add(base, f_mul(cs[t], hdiff(t + 1, 4, 7)),
                                 F(t * (-1) ** t))
            if base:
                for pm, pf in PHI[2 - wt]:
                    BF.append(f_mul(base, pf))
                    BN.append('DVz[%s]x%s'
                              % ('.'.join(mono) if mono else '1', pm))
    print('z-weighted towers:', len(BF) - n1, flush=True)
    with open(_CACHE, 'wb') as fh:
        pickle.dump((BF, BN), fh)

ALLF = ALLF28 + BF
ALLN = ALLN28 + BN
N_OLD = len(ALLF28)

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


def vec_modp(f, p):
    v = np.zeros(NEM, dtype=np.int64)
    for m, c in f.items():
        v[EIDX[m]] = (v[EIDX[m]] + c.numerator % p
                      * pow(c.denominator % p, p - 2, p)) % p
    return v


if __name__ == '__main__':
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 4194301
    import eps28 as E28
    E28.EMON, E28.EIDX, E28.NEM = EMON, EIDX, NEM   # reuse row builder
    rows, _ = E28.build_rows_ext(p, 30)
    print('rows:', rows.shape, flush=True)

    V = np.zeros((len(ALLF), NEM), dtype=np.int64)
    for i, f in enumerate(ALLF):
        V[i] = vec_modp(f, p)
    bad = []
    for lo in range(0, len(ALLF), 64):
        hi = min(lo + 64, len(ALLF))
        vals = rows.dot(V[lo:hi].T) % p
        for j in range(hi - lo):
            if vals[:, j].any():
                bad.append(lo + j)
    nb_old = sum(1 for i in bad if i < N_OLD)
    print('calibration failures: old %d, new %d of %d'
          % (nb_old, len(bad) - nb_old, len(BF)), flush=True)
    if len(bad) - nb_old:
        print('first new failures:', [ALLN[i] for i in bad if i >= N_OLD][:15])
    keep = [i for i in range(len(ALLF)) if i not in set(bad)]
    G = V[keep]
    inv2 = pow(2, p - 2, p)
    Gs = (G + G[:, ESIG]) * inv2 % p

    tgt = np.zeros(NEM, dtype=np.int64)
    for m, c in DELTA5.items():
        tgt[EIDX[m]] = (c.numerator % p
                        * pow(c.denominator % p, p - 2, p)) % p
    tgt = (tgt + tgt[ESIG]) * inv2 % p

    NP = len(keep) + 400
    for trial in range(2):
        rng = np.random.default_rng(777 + trial)
        R = rng.integers(0, p, size=(NEM, NP), dtype=np.int64)
        GP = np.zeros((Gs.shape[0], NP), dtype=np.int64)
        for lo in range(0, NEM, 2048):
            hi = min(lo + 2048, NEM)
            GP = (GP + Gs[:, lo:hi].dot(R[lo:hi])) % p
        tP = tgt.dot(R) % p
        print('projection %d computed' % trial, flush=True)
        r1 = E28.elim_rank(GP.copy(), p)
        r2 = E28.elim_rank(np.vstack([GP, tP[None, :]]), p)
        print('projection %d: rank %d, with target %d -> %s'
              % (trial, r1, r2,
                 'IN SPAN' if r1 == r2 else 'still missing'), flush=True)
