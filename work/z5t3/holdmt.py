"""holdmt.py -- holdout test of the folded+MT solution at n = NS+1."""
import sys, pickle
import numpy as np

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5t3')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import momtow as MTm
from momtow import (P, mom_density, phik_val, inf_coeff, gamma_mod,
                    mom_columns_spec, RHOS, PHIK)

NS = int(sys.argv[1]) if len(sys.argv) > 1 else 20
NH = NS + 1

x = np.load('mt_x_%d_n%d.npy' % (P, NS))
dh = np.load('sys3_%d_h%d.npz' % (P, NH))
Ah, Bh, Dh, th = dh['A'], dh['B'], dh['D'], dh['t']
Lkh, DDh = dh['Lk'], dh['DD']
Fh = (Ah + Lkh[:, None] * Bh % P + DDh[:, None] * Dh % P) % P
bh = (th[:, 0] + Lkh * th[:, 1] + DDh * th[:, 2]) % P
hcells = [(NH, k, l) for k in range(NH + 1) for l in range(NH + 1)]
assert len(hcells) == Fh.shape[0]

spec = mom_columns_spec()
i2 = (P + 1) // 2
MT = np.zeros((len(hcells), len(spec)), dtype=np.int64)
for ci, (n, k, l) in enumerate(hcells):
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
        MT[ci, si] = (dens[(mono, m, 0)] * pkv[(pk, 0)]
                      + dens[(mono, m, 1)] * pkv[(pk, 1)]) * i2 % P
cost = np.zeros(len(spec), dtype=np.int64)
for si, (nm, (mono, m, pk)) in enumerate(spec):
    acc = 0
    for k in range(NH + 1):
        e = inf_coeff(NH, k, mono, m) * pow(gamma_mod(NH, k), P - 2, P) % P
        acc = (acc + phik_val(pk, NH, k) * e) % P
    cost[si] = acc

Full = np.concatenate([Fh, MT], axis=1)
resid = (Full @ (x % P) - bh) % P
nz = int(np.count_nonzero(resid))
crow = int((cost * x[Fh.shape[1]:] % P).sum() % P)
print('HOLDOUT n=%d: cell rows nonzero %d of %d ; cost-row residual %d'
      % (NH, nz, len(bh), crow))
