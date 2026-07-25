"""Control: does allowing POLYNOMIAL coefficients ever lower the constant-coefficient
minimum?  Test every 8-symbol letter set obtained by deleting one letter from the
9-symbol optimum, and every letter set at 5..8 symbols built from the optimum's
letters, with polynomial coefficients of degree <= DP."""
import sys, os, itertools, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from polyfit import PolySpec, pdesign
from w3full import rref_aug, LSYM, SYMIDX, Q1

DP = int(os.environ.get('DP', 2)); DM = int(os.environ.get('DM', 3))
lm = {lt: sum(1 << SYMIDX[s] for s in LSYM[lt]) for lt in sorted(LSYM)}
pc = lambda x: bin(int(x)).count('1')
BASE = ['A1(k)','A2(k)','B1(k)','A1(l)','B1(l)','N3']       # the 9-symbol optimum
EOPT = ['A1(k)','A2(k)','B1(k)','A2(l)']                    # the proved E=7 optimum
def go(L, N=None):
    sp = PolySpec(sorted(L), DP, DM, deg_min=0, deg_max=DM)
    nc = len(sp); N = N or max(150, nc + max(150, nc//2))
    M, b = pdesign(sp, N, Q1)
    r, piv, inc, A = rref_aug(M, b, Q1)
    m = 0
    for x in L: m |= lm[x]
    print('  %-46s sym=%d cols=%-4d rows=%-4d rank=%-4d excess=%-4d %s'
          % (','.join(sorted(L)), pc(m), nc, N, r, N-r,
             'CONSISTENT' if not inc else 'inconsistent'), flush=True)
    return not inc
print('DP=%d DM=%d -- proper subsets of the 9-symbol optimum:' % (DP, DM), flush=True)
for r in range(1, len(BASE)):
    for sub in itertools.combinations(BASE, r):
        m = 0
        for x in sub: m |= lm[x]
        if pc(m) <= 8: go(list(sub))
print('proper subsets of the proved E=7 optimum:', flush=True)
for r in range(1, len(EOPT)):
    for sub in itertools.combinations(EOPT, r):
        go(list(sub))
print('CONTROL positive (must be CONSISTENT):', flush=True)
go(BASE); go(EOPT + ['A3(k)','N3'])
