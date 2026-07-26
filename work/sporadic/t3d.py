"""T3 completion: the COMPLETE tame form-sets for eta, F, zeta (see report sec on
completeness of tame alphabets: for support k in [0,n/m] the tame integer linear forms
are exactly {j k : 1<=j<=m} u {n - j k : 0<=j<=m})."""
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

ETA_TAME = ['n','k','2k','3k','4k','5k','n-k','n-2k','n-3k','n-4k','n-5k']
F_TAME   = ['n','k','n-k','l','k-l','n-l','n-k+l']
Z_TAME   = ['n','k','n-k','l','n-l','k-l','k+l-n']
if job == 'eta':
    auto('eta', ETA_TAME, 3, (5,), 1, maxdeg=2, tag='COMPLETE tame11 d2 hom1', cap=340)
    auto('eta', ETA_TAME, 3, (), maxdeg=3, tag='COMPLETE tame11 pure', cap=700)
if job == 'F':
    auto('F', F_TAME, 2, (-3,), 1, tag='COMPLETE tame7 hom1', cap=200)
    auto('F', F_TAME, 2, (), tag='COMPLETE tame7 pure', cap=200)
    auto('F', F_TAME, 2, (-3,), maxdeg=2, tag='COMPLETE tame7 all', cap=300)
if job == 'zeta':
    auto('zeta', Z_TAME, 3, (-3,), 1, maxdeg=2, tag='COMPLETE tame7 d2 hom1', cap=260)
    auto('zeta', Z_TAME, 3, (), maxdeg=3, tag='COMPLETE tame7 pure', cap=300)
if job == 'etabig':
    probe('eta', ['n','k','n-k','tb','2k','n-5k'], discs=(5,), N=580, extract=False, tag='tame6 all')
