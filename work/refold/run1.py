"""P1e-refold stage 1: build the weight-3 fitting system, validate the instrument
on w3hat, compute ker V, and run the exhaustive minimum-SYMBOL search.

Usage:  python3 run1.py [N] [q]
"""
import sys, os, time, itertools, json
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from w3full import (FullBasis, design, row, rref_aug, solve, LSYM, ALL_SYMBOLS,
                    SYMIDX, Q1, Q2, lad_mod)

N = int(sys.argv[1]) if len(sys.argv) > 1 else 240
q = int(sys.argv[2]) if len(sys.argv) > 2 else Q1
SMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 9

B = FullBasis()
print('basis: %d columns  (k-monomials %d, c-monomials %d, n-monomials %d)'
      % (len(B), len(B.km), len(B.cm), len(B.nm)), flush=True)

# --------------------------------------------------------------- design matrix
cache = os.path.join(HERE, 'DF_w3_%d_%d.npz' % (N, q))
if os.path.exists(cache):
    z = np.load(cache)
    M, b = z['M'], z['b']
    print('loaded %s' % cache, flush=True)
else:
    t0 = time.time()
    M, b = design(B, N, q)
    np.savez_compressed(cache, M=M, b=b)
    print('built design matrix %s in %.1f s' % (M.shape, time.time() - t0), flush=True)

# ------------------------------------------------- INSTRUMENT VALIDATION: w3hat
# w3hat, folded (PHASE2_CERTS 5.2):
#   v = N3 + 2 A3(k) - 1/2 A2(k)A1(k) - 3/2 A2(k)B1(k) - 3/4 A2(k)C1 - 1/4 A2(k)A1(l)
# and also the unfolded symmetric w3hat itself; BOTH must satisfy the system.
km = {m: i for i, (m, w) in enumerate(B.km)}
cm = {m: i for i, (m, w) in enumerate(B.cm)}
nm = {m: i for i, (m, w) in enumerate(B.nm)}
idx = {e: i for i, e in enumerate(B.els)}


def col(f, g, c, s):
    return idx[(km[f], km[g], cm[c], nm[s])]


E = ()
from fractions import Fraction as F

V_FOLD = {                                     # the folded weight  v
    col(E, E, (), ('N3',)): F(1),
    col(('A3',), E, (), ()): F(2),
    col(('A1', 'A2'), E, (), ()): F(-1, 2),
    col(('A2', 'B1'), E, (), ()): F(-3, 2),
    col(('A2',), E, ('C1',), ()): F(-3, 4),
    col(('A2',), ('A1',), (), ()): F(-1, 4),
}
W_SYM = {                                      # the symmetric w3hat
    col(E, E, (), ('N3',)): F(1),
    col(('A3',), E, (), ()): F(1), col(E, ('A3',), (), ()): F(1),
    col(('A1', 'A2'), E, (), ()): F(-1, 4), col(E, ('A1', 'A2'), (), ()): F(-1, 4),
    col(('A2', 'B1'), E, (), ()): F(-3, 4), col(E, ('A2', 'B1'), (), ()): F(-3, 4),
    col(('A2',), E, ('C1',), ()): F(-3, 8), col(E, ('A2',), ('C1',), ()): F(-3, 8),
    col(('A2',), ('A1',), (), ()): F(-1, 8), col(('A1',), ('A2',), (), ()): F(-1, 8),
}


def tomod(d, q):
    x = np.zeros(len(B), dtype=np.int64)
    for c, v in d.items():
        x[c] = (v.numerator % q) * pow(v.denominator % q, q - 2, q) % q
    return x


for name, d in (('v (folded)', V_FOLD), ('w3hat (symmetric)', W_SYM)):
    r = (M @ tomod(d, q) - b) % q
    print('VALIDATION  %-20s residual nonzeros = %d / %d'
          % (name, int((r != 0).sum()), len(r)), flush=True)

# --------------------------------------------------------------- solve, kernel
t0 = time.time()
x, K, rk = solve(M, b, q)
print('rank(M) = %d,  nullity = %d,  consistent = %s   (%.1f s)'
      % (rk, len(B) - rk, x is not None, time.time() - t0), flush=True)

# --------------------------------------------------- compress rows losslessly
r0, piv0, inc0, A0 = rref_aug(M, b, q)
Ared = A0[:r0]                     # r0 x (ncols+1), same ROW SPACE as [M|b]
print('compressed [M|b] to %d rows' % r0, flush=True)
Mc, bc = Ared[:, :-1].copy(), Ared[:, -1].copy()

# --------------------------------------------------------------- symbol census
colsym = []                    # bitmask of symbols used by each column
for e in B.els:
    mask = 0
    for lt in B.letters(e):
        for s in LSYM[lt]:
            mask |= 1 << SYMIDX[s]
    colsym.append(mask)
colsym = np.array(colsym, dtype=np.int64)


def popcount(x):
    return bin(x).count('1')


print('symbols of v (folded)      : %d  %s'
      % (popcount(int(np.bitwise_or.reduce([colsym[c] for c in V_FOLD]))),
         sorted(ALL_SYMBOLS[i] for i in range(len(ALL_SYMBOLS))
                if int(np.bitwise_or.reduce([colsym[c] for c in V_FOLD])) >> i & 1)),
      flush=True)
print('symbols of w3hat symmetric : %d'
      % popcount(int(np.bitwise_or.reduce([colsym[c] for c in W_SYM]))), flush=True)


def consistent(mask):
    sel = np.nonzero((colsym & ~mask) == 0)[0]
    if sel.size == 0:
        return False, 0
    r1, _, inc, _ = rref_aug(Mc[:, sel], bc, q)
    return (not inc), sel.size


# ---- enumerate CLOSED symbol masks (unions of letter symbol sets) by BFS ----
letters = sorted(LSYM)
lmask = {lt: sum(1 << SYMIDX[s] for s in LSYM[lt]) for lt in letters}
seen = {0}
frontier = {0}
bylevel = {}
while frontier:
    nxt = set()
    for m in frontier:
        for lt in letters:
            mm = m | lmask[lt]
            if mm != m and popcount(mm) <= SMAX and mm not in seen:
                seen.add(mm)
                nxt.add(mm)
    frontier = nxt
for m in seen:
    bylevel.setdefault(popcount(m), []).append(m)
print('closed symbol masks up to %d symbols: %d  (%s)'
      % (SMAX, len(seen), {k: len(v) for k, v in sorted(bylevel.items())}), flush=True)

# ------------------------------------------------------------------- search
best = None
for s in sorted(bylevel):
    t0 = time.time()
    hits = []
    for m in bylevel[s]:
        ok, nsel = consistent(m)
        if ok:
            hits.append((m, nsel))
    print('  symbols = %d : %d masks tested, %d CONSISTENT   (%.1f s)'
          % (s, len(bylevel[s]), len(hits), time.time() - t0), flush=True)
    if hits and best is None:
        best = (s, hits)
        for m, nsel in hits[:12]:
            print('      -> %s   (%d columns)'
                  % (sorted(ALL_SYMBOLS[i] for i in range(len(ALL_SYMBOLS)) if m >> i & 1),
                     nsel), flush=True)
        break

if best is None:
    print('NO consistent symbol set with <= %d symbols' % SMAX, flush=True)
