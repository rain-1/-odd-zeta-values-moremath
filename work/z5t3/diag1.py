"""diag1.py -- locate the inconsistency of the n<=NS live1 system.

Loads the cached system, computes the canonical solution, and reports the
distribution of nonzero residual rows over (n, k, l, component).  Also
extracts one explicit left-null obstruction functional if asked (--null).
"""
import sys, pickle
import numpy as np

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import fastlin

P = 4194301
NS = int(sys.argv[1]) if len(sys.argv) > 1 else 11

dat = np.load('sys_%d_n%d.npz' % (P, NS))
A, b = dat['A'], dat['b']
meta = pickle.load(open('sys_%d_n%d_names.pkl' % (P, NS), 'rb'))
names, ri = meta['names'], meta['rowinfo']
print('system', A.shape)

x, rk, piv, nbad = fastlin.solve(A, b, P)
print('rank %d nbad %d' % (rk, nbad))
resid = (A @ (x % P) - b) % P
bad = np.nonzero(resid)[0]
print('nonzero residual rows:', len(bad))
from collections import Counter
bycomp = Counter(ri[i][3] for i in bad)
byn = Counter(ri[i][0] for i in bad)
print('by component:', dict(bycomp))
print('by n:', dict(byn))
bykl = Counter((ri[i][1] - ri[i][2]) for i in bad)
print('by k-l:', dict(sorted(bykl.items())))
bysum = Counter((ri[i][1] + ri[i][2] - ri[i][0]) for i in bad)
print('by k+l-n:', dict(sorted(bysum.items())))
print('sample bad rows:', [ri[i] for i in bad[:30]])
