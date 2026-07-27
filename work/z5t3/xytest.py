"""xytest.py -- mod-p calibration of the XY 2-variable jets + effect on the
folded n<=20 deficit.

(1) global nullcheck  Sigma_{k,l} T u = 0  for n = 3..7 (mod p);
(2) per-fiber check (expected to FAIL -- that's what makes them new);
(3) append symmetrised XY columns to the cached folded system and re-solve.
"""
import sys, pickle
import numpy as np
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5t3')
import fastlin
import xyjets
from eps22 import MON, MIDX, NM, SIG

P = 4194301
NS = 20

M = xyjets.menu()
print('XY columns:', len(M), flush=True)

def form_vec(f):
    v = np.zeros(NM, dtype=np.int64)
    for m, c in f.items():
        v[MIDX[m]] = (v[MIDX[m]] + c.numerator % P
                      * pow(c.denominator % P, P - 2, P)) % P
    return v

G = np.zeros((len(M), NM), dtype=np.int64)
for i, (nm, f) in enumerate(M):
    G[i] = form_vec(f)
i2 = (P + 1) // 2
Gs = (G + G[:, SIG]) * i2 % P

# harmonic tables
MM = 90
HT = np.zeros((6, MM + 1), dtype=np.int64)
for m in range(1, MM + 1):
    inv = pow(m, P - 2, P)
    acc = inv
    HT[1][m] = (HT[1][m - 1] + acc) % P
    for r in range(2, 6):
        acc = acc * inv % P
        HT[r][m] = (HT[r][m - 1] + acc) % P

def monvals(n, k, l):
    xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
    lv = {}
    for r in range(1, 6):
        for a in range(9):
            lv[(r, a)] = int(HT[r][max(xs[a], 0)])
    out = np.empty(NM, dtype=np.int64)
    for i, m in enumerate(MON):
        v = 1
        for la in m:
            v = v * lv[la] % P
        out[i] = v
    return out

from math import comb
def Tmod(n, k, l):
    return (comb(n + k, n) * comb(n, k) ** 2 * comb(n + l, n)
            * comb(n, l) ** 2 * comb(n + k + l, n)) % P

# (1) global nullcheck + (2) per-fiber
for n in (3, 4, 5, 6, 7):
    tot = np.zeros(len(M), dtype=np.int64)
    fib_bad = 0
    for k in range(n + 1):
        fib = np.zeros(len(M), dtype=np.int64)
        for l in range(n + 1):
            mv = monvals(n, k, l)
            vals = G @ mv % P
            w = Tmod(n, k, l)
            tot = (tot + w * vals) % P
            fib = (fib + w * vals) % P
        if fib.any():
            fib_bad += 1
    print('n=%d: global bad %d/%d ; fibers with nonzero sums: %d/%d'
          % (n, int(np.count_nonzero(tot % P)), len(M), fib_bad, n + 1),
          flush=True)

# (3) folded system with XY appended
d = np.load('sys3_%d_n%d.npz' % (P, NS))
A3, B3, D3, t, Lk, DD = d['A'], d['B'], d['D'], d['t'], d['Lk'], d['DD']
meta = pickle.load(open('live3_blocks_n%d.pkl' % NS, 'rb'))
cells = meta['cells']
Ffold = (A3 + Lk[:, None] * B3 % P + DD[:, None] * D3 % P) % P
b = (t[:, 0] + Lk * t[:, 1] + DD * t[:, 2]) % P
XYcols = np.zeros((len(cells), len(M)), dtype=np.int64)
for ci, (n, k, l) in enumerate(cells):
    mv = monvals(n, k, l)
    XYcols[ci] = Gs @ mv % P
Fx = np.concatenate([Ffold, XYcols], axis=1)
x, rk, piv, nbad = fastlin.solve(Fx, b, P)
print('[folded+XY] rank=%d nbad=%d (was rank 2778 nbad 514)' % (rk, nbad),
      flush=True)
