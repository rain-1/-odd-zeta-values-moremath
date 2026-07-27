"""ext26.py -- build n=22..26 blocks, assemble the full folded+MT system on
n<=25 (holdout 26) and n<=26, and solve.

Reuses cached blocks for n<=20 and n=21; builds only the new cells.
"""
import sys, time, pickle
import numpy as np

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5t3')
import live3 as L3
from live3 import build_all, P
import momtow as MT
from momtow import (mom_density, phik_val, inf_coeff, gamma_mod,
                    mom_columns_spec, RHOS, PHIK)
import fastlin

t0 = time.time()
NEW = [(n, k, l) for n in range(22, 27)
       for k in range(n + 1) for l in range(n + 1)]
import os
if os.path.exists('sys3_%d_n22_26.npz' % P):
    d = np.load('sys3_%d_n22_26.npz' % P)
    blocksN = (d['A'], d['B'], d['D'], d['t'], d['Lk'], d['DD'])
    print('loaded cached 22..26 blocks', flush=True)
else:
    b = build_all(NEW)
    np.savez_compressed('sys3_%d_n22_26.npz' % P,
                        A=b[0], B=b[1], D=b[2], t=np.array(b[3]),
                        Lk=b[4], DD=b[5])
    blocksN = (b[0], b[1], b[2], np.array(b[3]), b[4], b[5])
    print('built 22..26 blocks %.0fs' % (time.time() - t0), flush=True)

d20 = np.load('sys3_%d_n20.npz' % P)
d21 = np.load('sys3_%d_h21.npz' % P)
meta20 = pickle.load(open('live3_blocks_n20.pkl', 'rb'))
cells20 = meta20['cells']
cells21 = [(21, k, l) for k in range(22) for l in range(22)]
cells = cells20 + cells21 + NEW

def fold(dd):
    A, B, D, t, Lk, DD = dd
    F = (A + Lk[:, None] * B % P + DD[:, None] * D % P) % P
    b = (t[:, 0] + Lk * t[:, 1] + DD * t[:, 2]) % P
    return F, b

F20, b20 = fold((d20['A'], d20['B'], d20['D'], d20['t'], d20['Lk'], d20['DD']))
F21, b21 = fold((d21['A'], d21['B'], d21['D'], d21['t'], d21['Lk'], d21['DD']))
FN, bN = fold(blocksN)
F = np.concatenate([F20, F21, FN], axis=0)
b = np.concatenate([b20, b21, bN])
print('base folded system', F.shape, '%.0fs' % (time.time() - t0), flush=True)

spec = mom_columns_spec()
i2 = (P + 1) // 2
MTcols = np.zeros((len(cells), len(spec)), dtype=np.int64)
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
        MTcols[ci, si] = (dens[(mono, m, 0)] * pkv[(pk, 0)]
                          + dens[(mono, m, 1)] * pkv[(pk, 1)]) * i2 % P
    if ci % 1000 == 0:
        print('  MT cell %d/%d %.0fs' % (ci, len(cells), time.time() - t0),
              flush=True)
np.save('MTcols_%d_n26.npy' % P, MTcols)

nvals = list(range(1, 27))
COST = np.zeros((len(nvals), len(spec)), dtype=np.int64)
for ni, n in enumerate(nvals):
    for si, (nm, (mono, m, pk)) in enumerate(spec):
        acc = 0
        for k in range(n + 1):
            e = inf_coeff(n, k, mono, m) * pow(gamma_mod(n, k), P - 2, P) % P
            acc = (acc + phik_val(pk, n, k) * e) % P
        COST[ni, si] = acc
np.save('COST_%d_n26.npy' % P, COST)
print('MT+cost built %.0fs' % (time.time() - t0), flush=True)

nrow = np.array([c[0] for c in cells])
for NSOLVE, NHOLD in ((25, 26), (26, None)):
    mask = nrow <= NSOLVE
    A = np.concatenate([F[mask], MTcols[mask]], axis=1)
    cmask = [ni for ni, n in enumerate(nvals) if n <= NSOLVE]
    crows = np.concatenate([np.zeros((len(cmask), F.shape[1]),
                                     dtype=np.int64), COST[cmask]], axis=1)
    Afull = np.concatenate([A, crows], axis=0)
    bfull = np.concatenate([b[mask], np.zeros(len(cmask), dtype=np.int64)])
    t1 = time.time()
    x, rk, piv, nbad = fastlin.solve(Afull, bfull, P)
    print('[solve n<=%d] %s rank=%d nbad=%d deprows=%d (%.0fs)'
          % (NSOLVE, Afull.shape, rk, nbad, Afull.shape[0] - rk,
             time.time() - t1), flush=True)
    np.save('mt26_x_%d_n%d.npy' % (P, NSOLVE), x)
    if nbad == 0 and NHOLD is not None:
        hmask = nrow == NHOLD
        H = np.concatenate([F[hmask], MTcols[hmask]], axis=1)
        resid = (H @ (x % P) - b[hmask]) % P
        nz = int(np.count_nonzero(resid))
        crow = int((COST[NHOLD - 1] * x[F.shape[1]:] % P).sum() % P)
        print('   HOLDOUT n=%d: %d of %d nonzero; cost resid %d'
              % (NHOLD, nz, int(hmask.sum()), crow), flush=True)
        supp = int(np.count_nonzero(x % P))
        print('   support:', supp, flush=True)
