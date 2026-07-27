"""fiberprobe.py -- exact fiber sums V(n,k) = Sigma_l T([1]W_B + 2 w5sym).

T3 says Sigma_k V(n,k) = 0.  Inspect V's k-structure: vanishing? symmetry?
telescoping shape?  Exact rational arithmetic.
"""
import sys
from fractions import Fraction as Fr

ROOT = '/home/ubuntu/fable-episode-2/zeta-math-2/work'
for d in ('z5ord0', 'lb5', 'z5t3'):
    sys.path.insert(0, ROOT + '/' + d)

import core
import evalq as E
import weights as W
import t_euler as TE

W5S = W.compact_w5sym()
lk, ll_, c2 = W.Lk(), W.Ll(), W.Cr(2)

def W1(n, k, l):
    Lk = E.el_val(lk, n, k, l)
    Ll = E.el_val(ll_, n, k, l)
    C2 = E.el_val(c2, n, k, l)
    return (TE.r22_fit(k, l) + Lk * TE.r12_fit(k, l)
            + Ll * TE.r12_fit(l, k) + (Lk * Ll - C2) * TE.r11_fit(k, l))

def V(n, k):
    s = Fr(0)
    for l in range(n + 1):
        s += core.T(n, k, l) * (W1(n, k, l)
                                + 2 * E.el_val(W5S, n, k, l))
    return s

for n in range(1, 9):
    vs = [V(n, k) for k in range(n + 1)]
    tot = sum(vs, Fr(0))
    print('n=%d  sum=%s' % (n, tot))
    for k, v in enumerate(vs):
        print('   k=%d  V=%s' % (k, v))
    # partial sums (telescoping test)
    ps = Fr(0)
    parts = []
    for k in range(n + 1):
        ps += vs[k]
        parts.append(ps)
    print('   partial sums:', [str(p) for p in parts])
