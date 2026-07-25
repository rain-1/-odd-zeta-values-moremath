"""P1e-refold stage 2: minimise the symbols carried by the DEGREE >= 2 part.

WHY THIS IS THE RIGHT OBJECTIVE FOR THE E-ROUTE.
    E(w) = sum_tau G_tau (tau.w - w) .
For a monomial m of letter-degree 1 and constant coefficient, tau.m - m is RATIONAL
(each letter is a sum of a rational function over an n-window), so degree-1 monomials
contribute NOTHING to E's letter content.  For a product m1 m2,
    tau.(m1 m2) - m1 m2 = m1 d2 + m2 d1 + d1 d2 ,  d_i rational,
so the letters of E(w) are exactly the letters appearing in the DEGREE >= 2 part of w.
Check: v's degree>=2 part is -1/2 A2(k)A1(k) - 3/2 A2(k)B1(k) - 3/4 A2(k)C1
       - 1/4 A2(k)A1(l), letters {A2(k),A1(k),B1(k),C1,A1(l)} -> 9 symbols,
       which is exactly PHASE2_CERTS 18.17's measured count for E(v).

So: minimise |symbols(degree >= 2 part)|, with the degree-1 columns free.
Two searches are run:
  (S)  whole-summand symbols  (the 18.17 headline target, answered in run1.py)
  (E)  degree>=2 symbols only (the target for the route that is actually built)
"""
import sys, os, time, json
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from w3full import (FullBasis, design, rref_aug, LSYM, ALL_SYMBOLS, SYMIDX, Q1, Q2)

N = int(sys.argv[1]) if len(sys.argv) > 1 else 240
q = int(sys.argv[2]) if len(sys.argv) > 2 else Q1
SMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 9

B = FullBasis()
cache = os.path.join(HERE, 'DF_w3_%d_%d.npz' % (N, q))
if os.path.exists(cache):
    z = np.load(cache); M, b = z['M'], z['b']
else:
    M, b = design(B, N, q); np.savez_compressed(cache, M=M, b=b)
print('basis %d cols, design %s, q=%d' % (len(B), M.shape, q), flush=True)

r0, piv0, inc0, A0 = rref_aug(M, b, q)
Mc, bc = A0[:r0, :-1].copy(), A0[:r0, -1].copy()
print('rank %d ; compressed to %d rows' % (r0, r0), flush=True)

colsym = np.array([sum(1 << SYMIDX[s] for lt in B.letters(e) for s in LSYM[lt])
                   for e in B.els], dtype=np.int64)
coldeg = np.array([B.degree(e) for e in B.els])
pc = lambda x: bin(int(x)).count('1')

deg1 = np.nonzero(coldeg <= 1)[0]
print('degree<=1 columns (free for the E-route): %d  -> %s'
      % (len(deg1), [B.label(B.els[i]) for i in deg1]), flush=True)

# ---------------- closed symbol masks (unions of letter symbol sets) ----------
letters = sorted(LSYM)
lmask = {lt: sum(1 << SYMIDX[s] for s in LSYM[lt]) for lt in letters}
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


def test(sel):
    if sel.size == 0:
        return False
    _, _, inc, _ = rref_aug(Mc[:, sel], bc, q)
    return not inc


def symnames(m):
    return sorted(ALL_SYMBOLS[i] for i in range(len(ALL_SYMBOLS)) if m >> i & 1)


for tag, dmask in (('S  whole summand', coldeg >= 0), ('E  degree>=2 only', coldeg >= 2)):
    print('\n=== search %s ===' % tag, flush=True)
    restricted = np.nonzero(dmask)[0]
    freecols = np.nonzero(~dmask)[0]
    found = None
    for s in sorted(bylevel):
        t0 = time.time(); hits = []
        for m in bylevel[s]:
            sel = np.concatenate([freecols,
                                  restricted[(colsym[restricted] & ~m) == 0]])
            if test(np.unique(sel)):
                hits.append(m)
        print('  symbols=%d : %5d masks, %3d consistent  (%.1f s)'
              % (s, len(bylevel[s]), len(hits), time.time() - t0), flush=True)
        if hits:
            found = (s, hits)
            for m in hits[:20]:
                print('     -> %s' % (symnames(m),), flush=True)
            break
    if found is None:
        print('  NONE with <= %d symbols' % SMAX, flush=True)
    json.dump({'tag': tag, 'min': found[0] if found else None,
               'masks': [symnames(m) for m in (found[1] if found else [])]},
              open(os.path.join(HERE, 'search_%s.json' % tag.split()[0]), 'w'), indent=1)
