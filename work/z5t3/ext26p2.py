"""ext26p2.py -- full second-prime (-p 4194287) build of the folded+MT
system, n <= 26, from scratch, and solve on n<=25 / holdout 26.

Run:  python ext26p2.py -p 4194287
"""
import sys, time, pickle, os
import numpy as np

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5t3')
import live3 as L3
from live3 import build_all
from live1 import P
import momtow as MT
from momtow import (mom_density, phik_val, inf_coeff, gamma_mod,
                    mom_columns_spec, RHOS, PHIK)
import fastlin

assert MT.P == P, (MT.P, P)
t0 = time.time()
cells = [(n, k, l) for n in range(1, 27)
         for k in range(n + 1) for l in range(n + 1)]
CH = 'sys3_%d_full26.npz' % P
if os.path.exists(CH):
    d = np.load(CH)
    blocks = (d['A'], d['B'], d['D'], d['t'], d['Lk'], d['DD'])
    print('loaded cache', flush=True)
else:
    b = build_all(cells)
    np.savez_compressed(CH, A=b[0], B=b[1], D=b[2], t=np.array(b[3]),
                        Lk=b[4], DD=b[5])
    blocks = (b[0], b[1], b[2], np.array(b[3]), b[4], b[5])
    print('built full26 %.0fs' % (time.time() - t0), flush=True)

A3, B3, D3, t, Lk, DD = blocks
F = (A3 + Lk[:, None] * B3 % P + DD[:, None] * D3 % P) % P
b = (t[:, 0] + Lk * t[:, 1] + DD * t[:, 2]) % P

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
nvals = list(range(1, 27))
COST = np.zeros((len(nvals), len(spec)), dtype=np.int64)
for ni, n in enumerate(nvals):
    for si, (nm, (mono, m, pk)) in enumerate(spec):
        acc = 0
        for k in range(n + 1):
            e = inf_coeff(n, k, mono, m) * pow(gamma_mod(n, k), P - 2, P) % P
            acc = (acc + phik_val(pk, n, k) * e) % P
        COST[ni, si] = acc
print('MT+cost done %.0fs' % (time.time() - t0), flush=True)
np.save('MTcols_%d_n26.npy' % P, MTcols)
np.save('COST_%d_n26.npy' % P, COST)

nrow = np.array([c[0] for c in cells])
for NSOLVE, NHOLD in ((25, 26),):
    mask = nrow <= NSOLVE
    A = np.concatenate([F[mask], MTcols[mask]], axis=1)
    cmask = [ni for ni, n in enumerate(nvals) if n <= NSOLVE]
    crows = np.concatenate([np.zeros((len(cmask), F.shape[1]),
                                     dtype=np.int64), COST[cmask]], axis=1)
    Afull = np.concatenate([A, crows], axis=0)
    bfull = np.concatenate([b[mask], np.zeros(len(cmask), dtype=np.int64)])
    t1 = time.time()
    x, rk, piv, nbad = fastlin.solve(Afull, bfull, P)
    print('[P2 solve n<=%d] %s rank=%d nbad=%d deprows=%d (%.0fs)'
          % (NSOLVE, Afull.shape, rk, nbad, Afull.shape[0] - rk,
             time.time() - t1), flush=True)
    np.save('mt26_x_%d_n%d.npy' % (P, NSOLVE), x)
    if nbad == 0:
        hmask = nrow == NHOLD
        H = np.concatenate([F[hmask], MTcols[hmask]], axis=1)
        resid = (H @ (x % P) - b[hmask]) % P
        nz = int(np.count_nonzero(resid))
        print('   HOLDOUT n=%d: %d of %d nonzero'
              % (NHOLD, nz, int(hmask.sum())), flush=True)
