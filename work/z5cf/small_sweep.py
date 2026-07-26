"""Focused sweep: SMALL bare alphabets at FULL degree (weight 5), with a hard guard
on the number of excess equations."""
import sys, os, time, itertools, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from design2 import build, monomials, sym_orbits, monname, rref
from bare import Q1, Q2, lad_mod, SYMNAME

W = int(sys.argv[1]); KEY = sys.argv[2]; N = int(sys.argv[3])
q = int(sys.argv[4]) if len(sys.argv) > 4 else Q1
MINEX = int(sys.argv[5]) if len(sys.argv) > 5 else 40

ORB = [(0,), (1, 2), (3, 4), (5, 6), (7,), (8,)]
ORBNAME = ['n', 'k/l', 'n+k/n+l', 'n-k/n-l', 'k+l', 'n+k+l']
TAME = {0, 1, 3}

b = np.array([lad_mod(KEY, n, q) for n in range(N + 1)], dtype=np.int64)
print('W=%d target=%s N=%d q=%d  (guard: excess >= %d)' % (W, KEY, N, q, MINEX), flush=True)
print('%-30s %4s %6s %6s %6s %8s  %s' % ('alphabet', 'deg', 'cols', 'rkA', 'rkAb', 'excess', 'verdict'))
t0 = time.time()
for nb in range(1, 64):
    orbs = [i for i in range(6) if nb >> i & 1]
    syms = sorted(set(s for i in orbs for s in ORB[i]))
    name = '+'.join(ORBNAME[i] for i in orbs)
    tame = set(orbs) <= TAME
    for dcap in range(1, W + 1):
        mons = sym_orbits(monomials(W, dcap, syms))
        if len(mons) > N + 1 - MINEX:
            break
        _, M = build(W, N, q, mons=mons)
        _, rA, _ = rref(M, q)
        if N + 1 - rA < MINEX:
            break
        _, rAb, _ = rref(np.hstack([M, b[:, None]]), q)
        if rA == rAb:
            print('%-30s %4d %6d %6d %6d %8d  CONSISTENT%s'
                  % (name, dcap, len(mons), rA, rAb, N + 1 - rA,
                     '   <<< TAME' if tame else ''), flush=True)
            break
    else:
        continue
print('done %.1fs' % (time.time() - t0))
