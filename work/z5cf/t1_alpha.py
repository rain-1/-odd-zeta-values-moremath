"""Sweep all 64 k<->l-closed sub-alphabets of the nine bare symbols, each with
degree caps 1,2,3(,W), and report consistency of  Y_n = sum_{k,l} T * w."""
import sys, os, time, itertools, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from design2 import build, monomials, sym_orbits, monname, rref, Eng
from bare import Q1, Q2, lad_mod, SYMNAME

W = int(sys.argv[1]); KEY = sys.argv[2]; N = int(sys.argv[3])
q = int(sys.argv[4]) if len(sys.argv) > 4 else Q1
DMAX = int(sys.argv[5]) if len(sys.argv) > 5 else 3

ORB = [(0,), (1, 2), (3, 4), (5, 6), (7,), (8,)]
ORBNAME = ['n', 'k/l', 'n+k/n+l', 'n-k/n-l', 'k+l', 'n+k+l']
TAME = {0, 1, 3}          # orbit indices with all arguments <= n

# ---- build once on the full alphabet, then slice columns ----
t0 = time.time()
allmons = sym_orbits(monomials(W, DMAX))
E = Eng(N, q, W)
Mfull = np.zeros((N + 1, len(allmons)), dtype=np.int64)
for n in range(N + 1):
    Tv, idx = E.cells(n)
    hv = {r: [E.H[r][i] for i in idx] for r in range(1, W + 1)}
    for j, m in enumerate(allmons):
        v = Tv
        for (r, s) in m:
            v = v * hv[r][s] % q
        Mfull[n, j] = int(v.sum() % q)
print('%d monomials (W=%d, deg<=%d), %d rows, %.1fs' % (len(allmons), W, DMAX, N + 1, time.time() - t0), flush=True)
b = np.array([lad_mod(KEY, n, q) for n in range(N + 1)], dtype=np.int64)

monsyms = [set(s for (r, s) in m) for m in allmons]
mondeg = [len(m) for m in allmons]

print('\n  %-34s %4s %5s %5s %5s %6s  %s' % ('alphabet', 'deg', 'cols', 'rkA', 'rkAb', 'excess', 'verdict'))
res = {}
for nb in range(1, 64):
    orbs = [i for i in range(6) if nb >> i & 1]
    syms = set()
    for i in orbs:
        syms |= set(ORB[i])
    name = '+'.join(ORBNAME[i] for i in orbs)
    tame = set(orbs) <= TAME
    for dcap in range(1, DMAX + 1):
        cols = [j for j in range(len(allmons)) if monsyms[j] <= syms and mondeg[j] <= dcap]
        if not cols:
            continue
        A = Mfull[:, cols]
        _, rA, _ = rref(A, q)
        _, rAb, _ = rref(np.hstack([A, b[:, None]]), q)
        ok = rA == rAb
        if ok:
            print('  %-34s %4d %5d %5d %5d %6d  CONSISTENT%s'
                  % (name, dcap, len(cols), rA, rAb, N + 1 - rA, '   <<< TAME' if tame else ''), flush=True)
            res[(name, dcap)] = (len(cols), rA, tame)
            break
print('\ndone %.1fs' % (time.time() - t0))
