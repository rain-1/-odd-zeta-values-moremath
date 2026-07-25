"""P1e-refold stage 4: extract explicit representatives at the two optima found in
run1/run2, report their full census, and (Pareto) explore the trade-off between
   S = symbols of the whole summand   and   E = symbols of the degree>=2 part.
"""
import sys, os, json, time
import numpy as np
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from w3full import FullBasis, design, rref_aug, LSYM, ALL_SYMBOLS, SYMIDX, Q1, Q2

N = 240
B = FullBasis()
z = np.load(os.path.join(HERE, 'DF_w3_%d_%d.npz' % (N, Q1)))
M, b = z['M'], z['b']
r0, _, _, A0 = rref_aug(M, b, Q1)
Mc, bc = A0[:r0, :-1].copy(), A0[:r0, -1].copy()

colsym = np.array([sum(1 << SYMIDX[s] for lt in B.letters(e) for s in LSYM[lt])
                   for e in B.els], dtype=np.int64)
coldeg = np.array([B.degree(e) for e in B.els])
pc = lambda x: bin(int(x)).count('1')
letters = sorted(LSYM)
lmask = {lt: sum(1 << SYMIDX[s] for s in LSYM[lt]) for lt in letters}


def mk(L):
    m = 0
    for x in L:
        m |= lmask[x]
    return m


def solve_sub(sel, q=Q1):
    r, piv, inc, A = rref_aug(Mc[:, sel], bc, q)
    if inc:
        return None, None, r
    x = np.zeros(len(sel), dtype=np.int64)
    for i, c in enumerate(piv):
        x[c] = A[i, -1] % q
    free = [c for c in range(len(sel)) if c not in set(piv)]
    K = np.zeros((len(free), len(sel)), dtype=np.int64)
    for a, fc in enumerate(free):
        K[a, fc] = 1
        for i, c in enumerate(piv):
            K[a, c] = (-A[i, fc]) % q
    return x, K, r


def report(sel, x, tag):
    used = [sel[i] for i in range(len(sel)) if x[i] % Q1]
    Ssym = 0
    Esym = 0
    for c in used:
        Ssym |= int(colsym[c])
        if coldeg[c] >= 2:
            Esym |= int(colsym[c])
    print('%-28s : %2d monomials,  S=%d symbols, E=%d symbols'
          % (tag, len(used), pc(Ssym), pc(Esym)), flush=True)
    return used, Ssym, Esym


# ------------------------------------------------------------- the two optima
S_OPT = ['A1(k)', 'A2(k)', 'B1(k)', 'A1(l)', 'B1(l)', 'N3']
E_OPT = ['A1(k)', 'A2(k)', 'B1(k)', 'A1(l)']

print('=== S-optimum: letters %s ===' % S_OPT, flush=True)
m = mk(S_OPT)
sel = np.nonzero((colsym & ~m) == 0)[0]
x, K, r = solve_sub(sel)
print('  columns %d, rank %d, kernel dim %d' % (len(sel), r, len(sel) - r), flush=True)
report(sel, x, 'particular solution')

print('\n=== E-optimum: degree>=2 restricted to %s, degree<=1 free ===' % E_OPT, flush=True)
m = mk(E_OPT)
sel = np.unique(np.concatenate([np.nonzero(coldeg <= 1)[0],
                                np.nonzero((coldeg >= 2) & ((colsym & ~m) == 0))[0]]))
x, K, r = solve_sub(sel)
print('  columns %d, rank %d, kernel dim %d' % (len(sel), r, len(sel) - r), flush=True)
used, Ss, Es = report(sel, x, 'particular solution')
for c in used:
    print('       %-24s deg=%d' % (B.label(B.els[c]), coldeg[c]), flush=True)

# --------------------------------------------------------------- Pareto sweep
print('\n=== Pareto: min S for each achievable E ===', flush=True)
seen, frontier = {0}, {0}
SMAX = 10
while frontier:
    nxt = set()
    for mm in frontier:
        for lt in letters:
            m2 = mm | lmask[lt]
            if m2 != mm and pc(m2) <= SMAX and m2 not in seen:
                seen.add(m2); nxt.add(m2)
    frontier = nxt
byE = {}
for mE in seen:
    if pc(mE) > 9:
        continue
    d2 = np.nonzero((coldeg >= 2) & ((colsym & ~mE) == 0))[0]
    if d2.size == 0:
        continue
    for mS in seen:
        if (mE | mS) != mS or pc(mS) > 10:
            continue
        d1 = np.nonzero((coldeg <= 1) & ((colsym & ~mS) == 0))[0]
        sel = np.unique(np.concatenate([d1, d2]))
        key = (pc(mE), pc(mS))
        if key in byE:
            continue
        _, _, inc, _ = rref_aug(Mc[:, sel], bc, Q1)
        if not inc:
            byE[key] = (mE, mS, len(sel))
best = {}
for (e, s), v in byE.items():
    if e not in best or s < best[e][0]:
        best[e] = (s, v)
for e in sorted(best):
    s, (mE, mS, nsel) = best[e]
    print('   E=%d  ->  min S=%d   (E-letters %s ; S-letters %s)'
          % (e, s,
             sorted(ALL_SYMBOLS[i] for i in range(len(ALL_SYMBOLS)) if mE >> i & 1),
             sorted(ALL_SYMBOLS[i] for i in range(len(ALL_SYMBOLS)) if mS >> i & 1)),
          flush=True)
