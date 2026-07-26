"""JOB 1 -- the four questions about the 12-dimensional affine family, exact Q."""
import sys, os, pickle, itertools
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import wtools as W
import opt
import bare

HERE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'
d = pickle.load(open(os.path.join(HERE, 'familyQ.pkl'), 'rb'))
bQ, UQ = d['base'], d['U']
NU = len(UQ)
J = W.J109

wh = [Fr(0)] * J
for m, c in bare.w3hat_el().items():
    wh[W.IDX[m]] = Fr(c)


def in_span(U, v):
    """is v in span(U)? exact Q"""
    R0, p0 = W.rrefQ([list(u) for u in U])
    R1, p1 = W.rrefQ([list(u) for u in U] + [list(v)])
    return len(p1) == len(p0)


def coords(U, v):
    """v = sum x_i U_i ; returns x or None"""
    A = [[U[i][j] for i in range(len(U))] for j in range(J)]
    x, ok = W.solveQ(A, list(v))
    if not ok:
        return None
    chk = [Fr(0)] * J
    for i, c in enumerate(x):
        if c:
            chk = [chk[t] + c * U[i][t] for t in range(J)]
    return x if chk == [Fr(a) for a in v] else None


print('=' * 78)
print('Q1  sigma-stability of the affine family')
print('=' * 78)
sU = [W.sig(u) for u in UQ]
allin = all(in_span(UQ, s) for s in sU)
print('   sigma(U) subset U            : %s' % allin)
sb = W.sig(bQ)
diff = [sb[j] - bQ[j] for j in range(J)]
print('   sigma(base) - base in U      : %s' % in_span(UQ, diff))
print('   => the family is sigma-stable: %s' % (allin and in_span(UQ, diff)))
Usym = [W.symQ(u) for u in UQ]
Uanti = [W.antiQ(u) for u in UQ]
rs = len(W.rrefQ([list(u) for u in Usym])[1])
ra = len(W.rrefQ([list(u) for u in Uanti])[1])
print('   dim U = %d ; dim sym(U) = %d ; dim anti(U) = %d  (%d + %d = %d)'
      % (NU, rs, ra, rs, ra, rs + ra))

print()
print('=' * 78)
print("Q2  is there a member w' with  w' - what3  PURELY ANTISYMMETRIC ?")
print('=' * 78)
# need sym(w') = sym(what3);  sym(w') = sym(base) + sum lam_i sym(U_i)
tgt = [W.symQ(wh)[j] - W.symQ(bQ)[j] for j in range(J)]
A = [[Usym[i][j] for i in range(NU)] for j in range(J)]
x, ok = W.solveQ(A, tgt)
print('   linear system  sum lam_i sym(U_i) = sym(what3) - sym(base)  : %s'
      % ('SOLVABLE' if ok else 'INCONSISTENT'))
if ok:
    w = list(bQ)
    for i, c in enumerate(x):
        if c:
            w = [w[t] + c * UQ[i][t] for t in range(J)]
    dd = [w[t] - wh[t] for t in range(J)]
    print('   antisym check:', all(W.symQ(dd)[t] == 0 for t in range(J)))
    W.show(w, "w'(anti)")
else:
    print('   => NO member of the family differs from what3 by an ANTISYMMETRIC')
    print('      element only.  Structural reason (independent of the solve):')
    print('      the family is sigma-stable and affine, so w\' in family =>')
    print('      sym(w\') = (w\'+sigma w\')/2 in family; sym(w\') = what3^sym would')
    print('      put what3^sym in W_tel, which Z5CF_REP 3.2 EXCLUDED at n=9,11,13,17.')
    # confirm the structural statement inside our own data
    print('      check: what3^sym in the family?  %s'
          % in_span(UQ, [W.symQ(wh)[j] - bQ[j] for j in range(J)]))

print()
print('=' * 78)
print('Q4  the SYMMETRIC DEFECT  d_sym = sym(w) - what3^sym  over the family')
print('=' * 78)
# d_sym ranges over an affine subspace of sym(K).  How small can its
# K-generator count be?
print('   dim of the reachable d_sym affine space = %d' % rs)
dbase = [W.symQ(bQ)[j] - W.symQ(wh)[j] for j in range(J)]
print('   d_sym(base) is nonzero on %d of 109 coordinates' % len(W.support(dbase)))
print('   d_sym = 0 reachable ?  %s' % ('YES' if ok else 'NO'))

print()
print('=' * 78)
print('Q3  minimising  N_hard  and  J  over the family')
print('=' * 78)
print('   (P-int) forbidden monomials:', [('*'.join(m) if m else '1') for m in opt.FORBIDDEN])
print('   base violates (P-int) ?  %s'
      % any(bQ[j] != 0 for j in opt.FORB_IDX))
# which coordinates are constant over the whole family (cannot be changed)?
fixed = [j for j in range(J) if all(u[j] == 0 for u in UQ)]
movable = [j for j in range(J) if j not in fixed]
print('   coordinates constant over the family: %d ; movable: %d'
      % (len(fixed), len(movable)))
nzfixed = [j for j in fixed if bQ[j] != 0]
print('   FORCED-nonzero monomials (constant and nonzero): %d' % len(nzfixed))
for j in nzfixed:
    print('        %-22s %s' % ('*'.join(W.B[j]) if W.B[j] else '1', bQ[j]))
# forced letters
forced_letters = set()
for j in nzfixed:
    for L in W.B[j]:
        forced_letters.add(L)
print('   letters forced to appear: %s' % sorted(forced_letters))

# --- letter elimination feasibility
LETTERS = sorted({L for m in W.B for L in m if bare.LWT[L] <= 2})
elim_ok = {}
for L in LETTERS:
    S = [j for j in range(J) if L in W.B[j]]
    w, ok2 = opt.zero_set(bQ, UQ, S)
    elim_ok[L] = ok2
print('   single-letter elimination feasible for: %s'
      % sorted([L for L, v in elim_ok.items() if v]))
cur_letters = sorted({L for m in W.B for L in m
                      if any(bQ[j] != 0 and L in W.B[j] for j in range(J))
                      and bare.LWT[L] <= 2})
print('   letters currently used (h1/h2): %s' % cur_letters)
cand = [L for L in cur_letters if elim_ok.get(L)]
print('   currently-used letters that can be removed one at a time: %s' % cand)

best = None
for r in range(len(cand), 0, -1):
    found = False
    for S in itertools.combinations(cand, r):
        cols = []
        for L in S:
            cols += [j for j in range(J) if L in W.B[j]]
        cols = sorted(set(cols) | set(opt.FORB_IDX))
        w, ok2 = opt.zero_set(bQ, UQ, cols)
        if ok2:
            st = W.stats(w)
            print('   eliminate %-40s -> N_hard=%d J=%d supp=%d'
                  % (','.join(S), st['N_hard'], st['J'], st['n_mono']))
            if best is None or (st['N_hard'], st['J']) < (best[1]['N_hard'], best[1]['J']):
                best = (w, st, S)
            found = True
    if found:
        break
if best is None:
    print('   no letter can be eliminated; N_hard stays %d' % W.stats(bQ)['N_hard'])
else:
    print('   BEST letter elimination: %s' % (','.join(best[2]),))
    W.show(best[0], 'w_minL')
    pickle.dump(best[0], open(os.path.join(HERE, 'w_minL.pkl'), 'wb'))
