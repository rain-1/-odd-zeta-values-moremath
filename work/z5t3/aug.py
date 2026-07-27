"""aug.py -- test whether T3's folded certificate needs Q(n) coefficients.

Loads the cached n<=20 folded system and augments columns with n- and n^2-
scaled copies (equivalently: allows coefficient polynomials in n of degree
<= 2, which after clearing denominators is the creative-telescoping-style
certificate shape).  Also reports the bad-row distribution of the
unaugmented system.
"""
import sys, pickle
import numpy as np
from collections import Counter

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import fastlin

P = 4194301
NS = int(sys.argv[1]) if len(sys.argv) > 1 else 20
DEG = int(sys.argv[2]) if len(sys.argv) > 2 else 2

d = np.load('sys3_%d_n%d.npz' % (P, NS))
A3, B3, D3, t, Lk, DD = d['A'], d['B'], d['D'], d['t'], d['Lk'], d['DD']
meta = pickle.load(open('live3_blocks_n%d.pkl' % NS, 'rb'))
cells = meta['cells']
ns = np.array([c[0] for c in cells], dtype=np.int64)

F = (A3 + Lk[:, None] * B3 % P + DD[:, None] * D3 % P) % P
b = (t[:, 0] + Lk * t[:, 1] + DD * t[:, 2]) % P

x, rk, piv, nbad = fastlin.solve(F, b, P)
print('[deg 0] rank=%d nbad=%d rows=%d' % (rk, nbad, F.shape[0]), flush=True)

blocks = [F]
for dg in range(1, DEG + 1):
    blocks.append(F * (ns[:, None] ** dg % P) % P)
Faug = np.concatenate(blocks, axis=1)
print('augmented shape', Faug.shape, flush=True)
x, rk, piv, nbad = fastlin.solve(Faug, b, P)
print('[deg %d] rank=%d nbad=%d' % (DEG, rk, nbad), flush=True)
if nbad == 0:
    # holdout
    dh = np.load('sys3_%d_h%d.npz' % (P, NS + 1))
    Ah, Bh, Dh, th = dh['A'], dh['B'], dh['D'], dh['t']
    Lkh, DDh = dh['Lk'], dh['DD']
    Fh = (Ah + Lkh[:, None] * Bh % P + DDh[:, None] * Dh % P) % P
    bh = (th[:, 0] + Lkh * th[:, 1] + DDh * th[:, 2]) % P
    nh = np.full(Fh.shape[0], NS + 1, dtype=np.int64)
    hb = [Fh]
    for dg in range(1, DEG + 1):
        hb.append(Fh * (nh[:, None] ** dg % P) % P)
    Fhaug = np.concatenate(hb, axis=1)
    resid = (Fhaug @ (x % P) - bh) % P
    print('HOLDOUT nonzero: %d of %d' % (int(np.count_nonzero(resid)),
                                         len(bh)), flush=True)
    np.save('aug_x_%d_n%d.npy' % (P, NS), x)
