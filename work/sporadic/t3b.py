"""T3 continued: the three cases that were REFUSED for lack of excess equations."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fit import probe
job = sys.argv[1]
if job == 'delta':
    probe('delta', ['n','k','3k','n-3k','2k'], discs=(-3,), N=400, extract=False, tag='tame+chi')
if job == 'eta':
    probe('eta', ['n','k','n-k','tb','2k','n-5k'], discs=(5,), chi_hom=1, N=260, extract=False, tag='tame hom1')
    probe('eta', ['n','k','n-k','tb','2k','n-5k'], discs=(5,), N=520, extract=False, tag='tame all')
if job == 'etabig':
    probe('eta', ['n','k','n-k','tb','2k','n-5k'], discs=(5,), N=580, extract=False, tag='tame all')
if job == 'zeta':
    probe('zeta', ['n','k','n-k','l','k-l','k+l-n'], discs=(-3,), chi_hom=1, N=260, extract=False, tag='tame hom1')
