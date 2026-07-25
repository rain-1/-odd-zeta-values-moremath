"""Instrument validation for polyfit: reproduce a KNOWN positive and a KNOWN negative."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from polyfit import PolySpec, pdesign
from w3full import rref_aug, Q1, Q2

def go(L, dp, dm, N, q=Q1, dmin=0):
    sp = PolySpec(L, dp, dm, deg_min=dmin, deg_max=dm)
    M, b = pdesign(sp, N, q)
    r, piv, inc, A = rref_aug(M, b, q)
    print('  L=%-58s dp=%d dm=%d cols=%-4d rows=%d rank=%-4d %s'
          % (','.join(L), dp, dm, len(sp), N, r, 'CONSISTENT' if not inc else 'inconsistent'), flush=True)
    return not inc

print('POSITIVE control -- v lives here (12 symbols):')
go(['A1(k)','A2(k)','A3(k)','B1(k)','C1','N3','A1(l)'], 0, 3, 200)
print('POSITIVE control, second prime:')
go(['A1(k)','A2(k)','A3(k)','B1(k)','C1','N3','A1(l)'], 0, 3, 200, q=Q2)
print('NEGATIVE control -- pole-free alphabet (B and N only) must fail (v_p(Phat)=-1):')
go(['B1(k)','B2(k)','B3(k)','B1(l)','B2(l)','B3(l)','N1','N2','N3'], 2, 3, 600)
print('NEGATIVE control -- the 8-symbol best of stage 1, with dp=0:')
go(['A1(k)','A2(k)','B1(k)','A1(l)'], 0, 3, 200)
print('POSITIVE control -- the 9-symbol winner of stage 1 (dp=0, must be CONSISTENT):')
go(['A1(k)','A2(k)','B1(k)','A1(l)','B1(l)','N3'], 0, 3, 200)
