"""The Gamma-deformation probe (APERY_DEFECT sec 7.1).
If a Gamma-deformation with L_1=...=L_{w-1}=0 termwise exists, then
[eps^w] = L_w = c * sum_x lambda_x H^(w)_x  -- a DEGREE-1 weight-w weight.
So: is B(n) = sum_cells S * sum_x lambda_x H^(w)_x  (degree 1) solvable?
This is exactly the Gamma-derivable class, and it is a tiny linear system."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fit import probe
from fams import FAMS, ORDER
CHI = {'B': -3, 'C': -3, 'E': -4, 'F': -3, 'zeta': -3, 'eta': 5, 's18': -3}
print('Gamma-derivation probe: degree-1 weight-w bare fit  (H^(w)_x only, + K_chi^(w)_x)')
for lab in ORDER:
    F = FAMS[lab]
    D = CHI.get(lab)
    N = 60
    probe(lab, list(F.args), maxdeg=1, N=N, extract=False, guard=20, tag='deg1')
    if D:
        probe(lab, list(F.args), discs=(D,), maxdeg=1, N=N, extract=False, guard=20, tag='deg1+chi')
