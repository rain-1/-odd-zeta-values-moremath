"""T2 -- the Lemma-D four: is there a TAME bare-alphabet decomposition?
Tame = every letter argument x satisfies 0 <= x <= n on the whole summation support,
which is exactly hypothesis (H4) of Theorem LB (work/LBW_GENERAL.md).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fit import probe, minimize, extract_exact
from fams import FAMS

N = int(sys.argv[2]) if len(sys.argv) > 2 else 160
HO = list(range(N + 1, N + 7))
which = sys.argv[1] if len(sys.argv) > 1 else 'all'


def run(lab, args, **kw):
    kw.setdefault('N', N)
    kw.setdefault('holdout', HO)
    r = probe(lab, args, **kw)
    if r.get('terms'):
        m = minimize(lab, r['mons'], kw['N'], r['pivots'], verbose=False)
        print('      -> minimized to %d columns' % len(m))
        extract_exact(lab, r['mons'], kw['N'], m, holdout=HO)
    return r


print('=' * 78)
print('T2  TAME BARE-ALPHABET SEARCH, N=%d rows, held-out %d..%d' % (N, HO[0], HO[-1]))
print('=' * 78)

if which in ('all', 'E'):
    print('\n######## E  (Catalan, chi_{-4}) -- THE priority target')
    print('  tame args = %s ; full args = %s' % (list(FAMS["E"].tame), list(FAMS["E"].args)))
    print('\n-- E tame, chi-homogeneous e=1 (H5 as Theorem LB wants)')
    run('E', ['n', 'k', 'n-k'], discs=(-4,), chi_hom=1)
    print('\n-- E tame, ALL monomials (e=0,1,2 mixed; (H5) would fail but check spanning)')
    run('E', ['n', 'k', 'n-k'], discs=(-4,))
    print('\n-- E tame + chi_{-4} AND chi_{-3},chi_8 letters (wrong conductors, control)')
    run('E', ['n', 'k', 'n-k'], discs=(-4, -3, 8))
    print('\n-- E: pure harmonic tame (control: must be inconsistent)')
    run('E', ['n', 'k', 'n-k'])

if which in ('all', 'alpha'):
    print('\n######## alpha (Domb), w=3')
    print('  tame args = %s ; full args = %s' % (list(FAMS["alpha"].tame), list(FAMS["alpha"].args)))
    print('\n-- alpha tame {n,k,n-k}: the ENTIRE tame weight-3 space')
    run('alpha', ['n', 'k', 'n-k'])
    print('\n-- alpha: known non-tame form recoverable? {k,n-k,2k,2n-2k}')
    run('alpha', ['k', 'n-k', '2k', '2n-2k'], extract=False)

if which in ('all', 'eps'):
    print('\n######## eps, w=3   (support n/2<=k<=n so 2k-n and 2n-2k are TAME)')
    print('  tame args = %s ; full args = %s' % (list(FAMS["eps"].tame), list(FAMS["eps"].args)))
    print('\n-- eps tame {n,k,n-k,2k-n,2n-2k}: the ENTIRE tame weight-3 space')
    run('eps', ['n', 'k', 'n-k', '2k-n', '2n-2k'])
    print('\n-- eps tame subsets')
    run('eps', ['k', 'n-k', '2k-n'], extract=False)
    run('eps', ['n', 'k', '2k-n'], extract=False)

if which in ('all', 's7'):
    print('\n######## s7, w=2   (support n/2<=k<=n so 2k-n and 2n-2k are TAME)')
    print('  tame args = %s ; full args = %s' % (list(FAMS["s7"].tame), list(FAMS["s7"].args)))
    print('\n-- s7 tame {n,k,n-k,2k-n,2n-2k}: the ENTIRE tame weight-2 space')
    run('s7', ['n', 'k', 'n-k', '2k-n', '2n-2k'])
