"""T1 harness validation: recover the four KNOWN decompositions before trusting anything."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fit import probe, minimize, extract_exact
from core import mname

N = 100
HO = list(range(N + 1, N + 9))

print('=' * 78)
print('T1 VALIDATION  (N=%d fit rows, held-out n=%d..%d, exact Q)' % (N, HO[0], HO[-1]))
print('=' * 78)

print('\n--- gamma (Apery zeta(3)): expect (1/3)H3[n] - (1/6)H3[k], degree 1')
r = probe('gamma', ['n', 'k'], maxdeg=1, N=N, holdout=HO)

print('\n--- A (Franel): expect (1/4)H2[k] + (3/4)Hk(Hk-H[n-k])')
r = probe('A', ['k', 'n-k'], N=N, holdout=HO)

print('\n--- s10 (sum C(n,k)^4): expect (1/5)H2[k] + (4/5)Hk(Hk-H[n-k])')
r = probe('s10', ['k', 'n-k'], N=N, holdout=HO)

print('\n--- D (Apery zeta(2)): expect (1/5)[H2[n] + Hk(2Hk-H[n-k]-H[n])]')
r = probe('D', ['n', 'k', 'n-k'], N=N, holdout=HO)
if r.get('terms'):
    sup = r['pivots']
    m = minimize('D', r['mons'], N, sup)
    print('   minimized support -> %d cols' % len(m))
    extract_exact('D', r['mons'], N, m, holdout=HO)

print('\n--- E: reproduce the KNOWN non-tame chi_{-4} form (sanity for twisted letters)')
r = probe('E', ['k', '2k', '2n-2k'], discs=(-4,), N=N, holdout=HO, chi_hom=1)
if r.get('terms'):
    m = minimize('E', r['mons'], N, r['pivots'])
    print('   minimized support -> %d cols' % len(m))
    extract_exact('E', r['mons'], N, m, holdout=HO)
