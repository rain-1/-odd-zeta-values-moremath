"""diag3.py -- locate the 3-component inconsistency at n<=17."""
import sys, pickle
import numpy as np
from collections import Counter

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import fastlin

P = 4194301
d = np.load('sys3_%d_n17.npz' % P)
A3, B3, D3, t, Lk, DD = d['A'], d['B'], d['D'], d['t'], d['Lk'], d['DD']
meta = pickle.load(open('live3_blocks_n17.pkl', 'rb'))
cells = meta['cells']
m, nc = A3.shape
M = np.empty((3 * m, nc), dtype=np.int64)
b = np.empty(3 * m, dtype=np.int64)
M[0::3], M[1::3], M[2::3] = A3, B3, D3
b[0::3], b[1::3], b[2::3] = t[:, 0], t[:, 1], t[:, 2]
x, rk, piv, nbad = fastlin.solve(M, b, P)
print('rank %d nbad %d' % (rk, nbad))
resid = (M @ (x % P) - b) % P
bad = np.nonzero(resid)[0]
print('nonzero-resid rows:', len(bad))
comp = Counter(int(i % 3) for i in bad)
print('by comp (0=a,1=b,2=d):', dict(comp))
byn = Counter(cells[i // 3][0] for i in bad)
print('by n:', dict(sorted(byn.items())))
tot = Counter(c[0] for c in cells)
print('cells per n (x3 rows):', {k: 3 * v for k, v in sorted(tot.items())})
