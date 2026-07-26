"""T3 wide-alphabet runs for the never-attempted conjectural families.
N is chosen automatically so that excess >= 50 whenever affordable."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import monomials
from fit import probe, keys_of
job = sys.argv[1]

def auto(lab, args, w, discs=(), hom=None, maxdeg=None, extra=60, cap=700, tag=''):
    mons = monomials(keys_of(w, discs), args, w, maxdeg, hom)
    N = min(cap, len(mons) + extra)
    return probe(lab, args, w=w, discs=discs, chi_hom=hom, maxdeg=maxdeg, N=N,
                 mons=mons, extract=False, tag=tag or ('%dcols' % len(mons)))

if job == 'C':
    auto('C', ['n','k','n-k','2k','3k','3n-3k'], 2, (-3,), tag='conductor-3 args')
    auto('C', ['n','k','n-k','2k','3k','3n-3k','n+k','2n-2k'], 2, (-3,), 1, tag='wide hom1')
    auto('C', ['n','k','n-k','2k','n+k','2n-2k','2n','2n-k','3k','3n-3k','3n'], 2, (-3,), 1, tag='all11 hom1')
if job == 'B':
    auto('B', ['n','k','3k','n-3k','2k','n-k','n-2k','n+k','2n','4k'], 2, (-3,), 1, tag='wide10 hom1')
    auto('B', ['n','k','3k','n-3k','2k','n-k','n-2k'], 2, (-3,), tag='tame7 all')
if job == 's18':
    auto('s18', ['n','k','n-k','2k','2n-2k','t','tb','n-3k','3k','n-2k'], 2, (-3,), 1, tag='wide10 hom1')
    auto('s18', ['n','k','n-k','2k','tb','n-3k','3k','n-2k'], 2, (-3,), tag='tame8 all')
if job == 'F':
    auto('F', ['n','k','n-k','l','k-l','2l','2k-2l','n+k'], 2, (-3,), tag='wide8 all', cap=260)
if job == 'zeta':
    auto('zeta', ['n','k','n-k','l','n-l','k-l','k+l','k+l-n'], 3, (-3,), 1, maxdeg=2, tag='wide8 d2 hom1', cap=300)
    auto('zeta', ['n','k','n-k','l','k-l'], 3, (-3,), 1, tag='tame5 hom1', cap=300)
if job == 'delta':
    auto('delta', ['n','k','3k','n-3k','2k','n-k','n+k'], 3, (), maxdeg=3, tag='full7')
    auto('delta', ['n','k','3k','n-3k','2k','n-k'], 3, (-3,), 1, maxdeg=2, tag='tame6 d2 hom1')
if job == 'eta':
    auto('eta', ['n','k','n-k','tb','2k','n-5k'], 3, (5,), maxdeg=2, tag='tame6 d2 all')
    auto('eta', ['n','k','n-k','3n','t','tb','2k','n-5k'], 3, (5,), 1, maxdeg=2, tag='wide8 d2 hom1', cap=400)
