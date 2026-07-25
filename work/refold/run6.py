"""P1e-refold stage 7: the symbol minimisation restricted to the PROVED affine set

    w3hat + span( Lemma-Phi species  +  k<->l folding moves )

Only representatives in this set deliver THEOREM B ITSELF (Phat = sum T*w3hat)
once certified; a representative outside it certifies a different identity and
leaves sum T*(w3hat - w) = 0 as an uncertified obligation of the same difficulty
(PHASE2_CERTS section 1, transposed to weight 3).
"""
import sys, os, json, time
import numpy as np
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from w3full import FullBasis, rref_aug, LSYM, SYMIDX, ALL_SYMBOLS, Q1
import kernel_proved as KP                       # builds G (Phi species) and Ganti

B = KP.B
G = KP.G
EIDX = KP.EIDX
M, b = KP.M, KP.b
anti = []
for e in B.els:
    i, j, ci, ni = e
    if i == j:
        continue
    v = np.zeros(len(B), dtype=np.int64)
    v[EIDX[e]] = 1
    v[EIDX[(j, i, ci, ni)]] = Q1 - 1
    anti.append(v)
GALL = np.concatenate([G, np.array(anti, dtype=np.int64)], axis=0)
w3 = KP.tovec(KP.W3HAT)

colsym = np.array([sum(1 << SYMIDX[s] for lt in B.letters(e) for s in LSYM[lt])
                   for e in B.els], dtype=np.int64)
coldeg = np.array([B.degree(e) for e in B.els])
pc = lambda x: bin(int(x)).count('1')
lmask = {lt: sum(1 << SYMIDX[s] for s in LSYM[lt]) for lt in sorted(LSYM)}


def reachable(sel):
    """is there x supported on `sel` with x - w3 in span(GALL) ?"""
    Z = np.setdiff1d(np.arange(len(B)), sel)
    if Z.size == 0:
        return True
    A = GALL[:, Z].T % Q1                       # (|Z| x #gens)
    rhs = (-w3[Z]) % Q1
    _, _, inc, _ = rref_aug(A, rhs, Q1)
    return not inc


# --- validation: v (the folded w3hat) must be reachable, and is 12 symbols -----
vsel = np.array(sorted(EIDX[e] for e in B.els
                       if KP.tovec(KP.VFOLD)[EIDX[e]] != 0))
print('VALIDATION: v reachable = %s' % reachable(vsel), flush=True)

SMAX = int(os.environ.get('SMAX', 12))
letters = sorted(LSYM)
seen, frontier = {0}, {0}
while frontier:
    nxt = set()
    for m in frontier:
        for lt in letters:
            mm = m | lmask[lt]
            if mm != m and pc(mm) <= SMAX and mm not in seen:
                seen.add(mm); nxt.add(mm)
    frontier = nxt
bylevel = {}
for m in seen:
    bylevel.setdefault(pc(m), []).append(m)
print('closed masks <= %d symbols: %d' % (SMAX, len(seen)), flush=True)

for tag, dmask in (('S  whole summand', coldeg >= 0), ('E  degree>=2 only', coldeg >= 2)):
    print('\n=== PROVED-AFFINE search, %s ===' % tag, flush=True)
    restricted = np.nonzero(dmask)[0]
    freecols = np.nonzero(~dmask)[0]
    for s in sorted(bylevel):
        t0 = time.time()
        hits = []
        for m in bylevel[s]:
            sel = np.unique(np.concatenate(
                [freecols, restricted[(colsym[restricted] & ~m) == 0]]))
            if reachable(sel):
                hits.append(m)
        print('  symbols=%d : %5d masks, %3d reachable  (%.1f s)'
              % (s, len(bylevel[s]), len(hits), time.time() - t0), flush=True)
        if hits:
            for m in hits[:6]:
                print('     -> %s'
                      % sorted(ALL_SYMBOLS[i] for i in range(len(ALL_SYMBOLS))
                               if m >> i & 1), flush=True)
            break
