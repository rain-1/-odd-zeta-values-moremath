"""T3 -- the conjectural seven: B, C, F, delta, zeta, eta, s18.
Bare alphabet, with bare twisted letters at the right conductor.
Tame args first (a hit there is PROVED by Theorem LB immediately)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fit import probe, minimize, extract_exact
from fams import FAMS

which = sys.argv[1] if len(sys.argv) > 1 else 'B'
N = int(sys.argv[2]) if len(sys.argv) > 2 else 200
HO = list(range(N + 1, N + 6))


def run(lab, args, ex=True, **kw):
    kw.setdefault('N', N)
    kw.setdefault('holdout', HO)
    kw.setdefault('extract', ex)
    r = probe(lab, args, **kw)
    if r.get('terms'):
        m = minimize(lab, r['mons'], kw['N'], r['pivots'], verbose=False)
        print('      -> minimized to %d columns' % len(m))
        extract_exact(lab, r['mons'], kw['N'], m, holdout=HO)
    return r


print('=' * 78)
print('T3  %s   N=%d rows, held-out %d..%d' % (which, N, HO[0], HO[-1]))
F = FAMS[which]
print('  w=%d  chi=D%s   tame=%s   full=%s' % (F.w, F.D, list(F.tame), list(F.args)))
print('=' * 78)

if which == 'B':
    print('\n-- B tame, chi_{-3} homogeneous e=1')
    run('B', ['n', 'k', '3k', 'n-3k', '2k', 'n-k'], discs=(-3,), chi_hom=1)
    print('\n-- B tame, all monomials')
    run('B', ['n', 'k', '3k', 'n-3k', '2k', 'n-k'], discs=(-3,))
    print('\n-- B tame, pure harmonic (control)')
    run('B', ['n', 'k', '3k', 'n-3k', '2k', 'n-k'])
    print('\n-- B full args (incl non-tame n+k) + chi_{-3}')
    run('B', ['n', 'k', '3k', 'n-3k', '2k', 'n-k', 'n+k'], discs=(-3,), ex=False)

if which == 'delta':
    print('\n-- delta tame, pure harmonic w=3 (chi trivial)')
    run('delta', ['n', 'k', '3k', 'n-3k', '2k', 'n-k'])
    print('\n-- delta tame + n+k (non-tame)')
    run('delta', ['n', 'k', '3k', 'n-3k', '2k', 'n-k', 'n+k'], ex=False)
    print('\n-- delta tame + chi_{-3} letters (control on the character)')
    run('delta', ['n', 'k', '3k', 'n-3k', '2k'], discs=(-3,), ex=False)

if which == 'C':
    print('\n-- C tame, chi_{-3} homogeneous')
    run('C', ['n', 'k', 'n-k'], discs=(-3,), chi_hom=1)
    print('\n-- C tame, all monomials, chi_{-3}')
    run('C', ['n', 'k', 'n-k'], discs=(-3,))
    print('\n-- C full args + chi_{-3}  (LBW reported inconsistent; re-measure)')
    run('C', ['n', 'k', 'n-k', '2k', '2n-2k', 'n+k'], discs=(-3,), ex=False)

if which == 's18':
    print('\n-- s18 tame, chi_{-3} homogeneous')
    run('s18', ['n', 'k', 'n-k', '2k', 'tb', 'n-3k'], discs=(-3,), chi_hom=1)
    print('\n-- s18 tame, all monomials')
    run('s18', ['n', 'k', 'n-k', '2k', 'tb', 'n-3k'], discs=(-3,))
    print('\n-- s18 tame, pure harmonic (control)')
    run('s18', ['n', 'k', 'n-k', '2k', 'tb', 'n-3k'])
    print('\n-- s18 full args + chi_{-3}')
    run('s18', ['n', 'k', 'n-k', '2k', '2n-2k', 't', 'tb', 'n-3k'], discs=(-3,), ex=False)

if which == 'eta':
    print('\n-- eta tame, chi_5 homogeneous, w=3')
    run('eta', ['n', 'k', 'n-k', 'tb', '2k', 'n-5k'], discs=(5,), chi_hom=1)
    print('\n-- eta tame, pure harmonic (control)')
    run('eta', ['n', 'k', 'n-k', 'tb', '2k', 'n-5k'])
    print('\n-- eta full args + chi_5')
    run('eta', ['n', 'k', 'n-k', '3n', 't', 'tb', '2k', 'n-5k'], discs=(5,), ex=False)

if which == 'F':
    print('\n-- F tame (all args ARE tame), chi_{-3} homogeneous')
    run('F', ['n', 'k', 'n-k', 'l', 'k-l'], discs=(-3,), chi_hom=1)
    print('\n-- F tame, all monomials')
    run('F', ['n', 'k', 'n-k', 'l', 'k-l'], discs=(-3,))
    print('\n-- F tame, pure harmonic (control)')
    run('F', ['n', 'k', 'n-k', 'l', 'k-l'])

if which == 'zeta':
    print('\n-- zeta tame, chi_{-3} homogeneous, w=3')
    run('zeta', ['n', 'k', 'n-k', 'l', 'k-l', 'k+l-n'], discs=(-3,), chi_hom=1)
    print('\n-- zeta tame, pure harmonic (control)')
    run('zeta', ['n', 'k', 'n-k', 'l', 'k-l', 'k+l-n'])
