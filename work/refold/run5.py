"""P1e-refold stage 5: EXACT construction + held-out verification of the two
Pareto-optimal representatives, and the PROVED-KERNEL membership test.

(A)  w9  : S = 9 symbols (whole summand), E = 8   -- the 18.17 metric optimum
(B)  w7  : S = 10, E = 7                          -- the E(w)-metric optimum
(C)  is  w3hat - w  in the span of the PROVED kernel identities
     (Lemma Phi (P0) and Lemma Phi_2 (P1),(P2),(P3) of PHASE2_CANCEL section 3,
      times k-free multipliers, plus the k<->l mirrors)?
     If yes, Theorem B for w3hat follows from the certificate for w.
"""
import sys, os, json
import numpy as np
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from w3full import FullBasis, rref_aug, LSYM, ALL_SYMBOLS, SYMIDX, Q1, Q2
from exact import solve_exact, sums, mono_val
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import Ph, T, Hs                                      # noqa

B = FullBasis()
z = np.load(os.path.join(HERE, 'DF_w3_240_%d.npz' % Q1))
M, b = z['M'], z['b']
r0, _, _, A0 = rref_aug(M, b, Q1)
Mc, bc = A0[:r0, :-1].copy(), A0[:r0, -1].copy()
colsym = np.array([sum(1 << SYMIDX[s] for lt in B.letters(e) for s in LSYM[lt])
                   for e in B.els], dtype=np.int64)
coldeg = np.array([B.degree(e) for e in B.els])
pc = lambda x: bin(int(x)).count('1')
lmask = {lt: sum(1 << SYMIDX[s] for s in LSYM[lt]) for lt in sorted(LSYM)}


def mk(L):
    m = 0
    for x in L:
        m |= lmask[x]
    return m


def mono_of(e):
    """the folded monomial of a basis element, as a tuple of letter names"""
    i, j, ci, ni = e
    return (tuple('%s(k)' % x for x in B.km[i][0])
            + tuple('%s(l)' % x for x in B.km[j][0])
            + tuple(B.cm[ci][0]) + tuple(B.nm[ni][0]))


# --------------------------------------------------------------- (A) and (B)
CASES = {
    'w9  (S=9,  E=8)': np.nonzero((colsym & ~mk(['A1(k)', 'A2(k)', 'B1(k)',
                                                 'A1(l)', 'B1(l)', 'N3'])) == 0)[0],
    'w7  (S=10, E=7)': np.unique(np.concatenate([
        np.nonzero(coldeg <= 1)[0],
        np.nonzero((coldeg >= 2) &
                   ((colsym & ~mk(['A1(k)', 'A2(k)', 'B1(k)', 'A1(l)'])) == 0))[0]])),
}

OUT = {}
for tag, sel in CASES.items():
    monos = [mono_of(B.els[c]) for c in sel]
    print('\n=== %s :  %d candidate monomials ===' % (tag, len(monos)), flush=True)
    NF = list(range(1, 26))
    NC = [26, 28, 30, 33, 36, 40]
    x, free = solve_exact(monos, NF, NC)
    if x is None:
        print('  EXACT FIT INCONSISTENT -- mod-q result not confirmed', flush=True)
        continue
    used = [(monos[i], x[i]) for i in range(len(monos)) if x[i] != 0]
    S = 0
    E = 0
    for mu, c in used:
        mm = 0
        for lt in mu:
            mm |= lmask[lt]
        S |= mm
        if len(mu) >= 2:
            E |= mm
    print('  %d nonzero monomials;  S = %d symbols, E = %d symbols'
          % (len(used), pc(S), pc(E)), flush=True)
    for mu, c in used:
        print('     %-28s  %s' % ('*'.join(mu), c), flush=True)
    print('  S-symbols: %s'
          % sorted(ALL_SYMBOLS[i] for i in range(len(ALL_SYMBOLS)) if S >> i & 1), flush=True)
    print('  E-symbols: %s'
          % sorted(ALL_SYMBOLS[i] for i in range(len(ALL_SYMBOLS)) if E >> i & 1), flush=True)
    OUT[tag] = {'monomials': [['*'.join(mu), str(c)] for mu, c in used],
                'S_symbols': sorted('H^(%d)_{%s}' % (r, a)
                                    for (a, r) in
                                    (ALL_SYMBOLS[i] for i in range(len(ALL_SYMBOLS))
                                     if S >> i & 1)),
                'E_symbols': sorted('H^(%d)_{%s}' % (r, a)
                                    for (a, r) in
                                    (ALL_SYMBOLS[i] for i in range(len(ALL_SYMBOLS))
                                     if E >> i & 1)),
                'S': pc(S), 'E': pc(E)}

json.dump(OUT, open(os.path.join(HERE, 'wtilde3.json'), 'w'), indent=1)
print('\nwrote wtilde3.json', flush=True)
