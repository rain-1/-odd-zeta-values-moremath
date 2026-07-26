import sys, os, json
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import mindens, wtools as W, cert4, cert2, cert3
import bare, frw, cert, family, joint, fastlin, ratrec, qrow
from solve import dval
p=W.P1; n=int(sys.argv[1]); m=3
B=W.B
maximal,letters,zero_j=cert2.blocks_of(B)
dc=json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
w=W.to_p([Fr(c) for c in dc['coeffs']],p)
act=[j for j in letters if any(cert.divide(B[j],B[jj]) is not None and w[jj] for jj in range(len(B)))]
print('act letters:',[B[j][0] for j in act])
for which in ('k','l'):
    cls=cert4.classes(B,which)
    keep=[]; skip=[]
    for key,js in cls.items():
        js2=[j for j in js if j in act or j==zero_j or j in maximal]
        if not js2 or all(j in maximal for j in js2): skip.append(key); continue
        keep.append((key,[('%s'%('*'.join(B[j]) if B[j] else '1')) for j in js2]))
    print('%s-direction: %d classes need a constraint:'%(which,len(keep)))
    for key,mem in keep: print('    class %-28s members: %s'%('*'.join(key) if key else '1',mem))
