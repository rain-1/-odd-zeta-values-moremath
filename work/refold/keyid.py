"""The single identity that performs the refold:
      sum_{k,l} T * [ A2(k)*Psi_l + A2(l)*Psi_k ] = 0 ,
      Psi_k = A1(k) + 3 B1(k),   Psi_l = (3/2) C1 + (1/2) A1(l).
Equivalently  sum T [ 3 A2(k)C1 + A2(k)A1(l) + 2 A2(l)A1(k) + 6 A2(l)B1(k) ] = 0.
Verified exactly over Q, and located inside the PROVED kernel span."""
import sys, os
import numpy as np
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import T, Hs
from exact import sums
import kernel_proved as KP
from w3full import rref_aug, Q1

monos = [('A2(k)','C1'), ('A2(k)','A1(l)'), ('A2(l)','A1(k)'), ('A2(l)','B1(k)')]
co    = [F(3),           F(1),              F(2),              F(6)]
S = sums([tuple(sorted(m)) for m in monos], range(0, 26))
bad = [n for n in range(0, 26) if sum(co[i]*S[n][i] for i in range(4)) != 0]
print('EXACT: sum T [3 A2(k)C1 + A2(k)A1(l) + 2 A2(l)A1(k) + 6 A2(l)B1(k)] = 0 '
      'for n=0..25 : %s' % ('ALL ZERO' if not bad else 'FAIL %s' % bad), flush=True)

v = KP.tovec(KP.lp((3,('A2(k)','C1')), (1,('A2(k)','A1(l)')),
                   (2,('A2(l)','A1(k)')), (6,('A2(l)','B1(k)'))))
anti=[]
for e in KP.B.els:
    i,j,ci,ni = e
    if i==j: continue
    w = np.zeros(len(KP.B), dtype=np.int64); w[KP.EIDX[e]]=1; w[KP.EIDX[(j,i,ci,ni)]]=Q1-1
    anti.append(w)
GALL = np.concatenate([KP.G, np.array(anti,dtype=np.int64)], axis=0)
r1,_,_,_ = rref_aug(GALL, np.zeros(len(GALL),dtype=np.int64), Q1)
r2,_,_,_ = rref_aug(np.concatenate([GALL, v.reshape(1,-1)]),
                    np.zeros(len(GALL)+1,dtype=np.int64), Q1)
print('in PROVED span (Lemma-Phi species + folding): %s  (%d -> %d)' % (r1==r2, r1, r2), flush=True)
# and against the Lemma-Phi species alone
rA,_,_,_ = rref_aug(KP.G, np.zeros(len(KP.G),dtype=np.int64), Q1)
rB,_,_,_ = rref_aug(np.concatenate([KP.G, v.reshape(1,-1)]),
                    np.zeros(len(KP.G)+1,dtype=np.int64), Q1)
print('in Lemma-Phi species alone (no folding):      %s  (%d -> %d)' % (rA==rB, rA, rB), flush=True)
