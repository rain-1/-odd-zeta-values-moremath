"""Per-block size table from the 1-prime reconstruction."""
import os,sys,pickle,json
from fractions import Fraction as Fr
import numpy as np
HERE='/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'
sys.path.insert(0,HERE)
import mindens, wtools as W, cert3, cert2, cert4
import bare, cert
B=W.B
maximal,letters,zero_j=cert2.blocks_of(B)
dc=json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
w=W.to_p([Fr(c) for c in dc['coeffs']],W.P1)
act=[j for j in letters if any(cert.divide(B[j],B[jj]) is not None and w[jj] for jj in range(len(B)))]
ansL=cert3.mk('M0',8,0,0); ans0=cert3.mk('M0',12,0,0)
d=pickle.load(open(os.path.join(HERE,'reco_degs.pkl'),'rb'))
res=d['res']
nrL=len(ansL.mons_r); nr0=len(ans0.mons_r)
def block_of(c):
    if c<len(act)*ansL.nc:
        b=c//ansL.nc; off=c%ansL.nc
        return ('%s'%B[act[b]][0], 'rho' if off<nrL else 'sigma',
                ansL.mons_r[off] if off<nrL else ansL.mons_s[off-nrL])
    off=c-len(act)*ansL.nc
    return ('()','rho' if off<nr0 else 'sigma',
            ans0.mons_r[off] if off<nr0 else ans0.mons_s[off-nr0])
agg={}
for c,(dn,dd) in res.items():
    if dn is None: continue
    nm,which,(a,b)=block_of(c)
    key=(nm,which)
    e=agg.setdefault(key,dict(deg_n=0,dk=0,dl=0,nmono=0,tot=0))
    degn=dn+19-dd
    e['deg_n']=max(e['deg_n'],degn); e['dk']=max(e['dk'],a); e['dl']=max(e['dl'],b)
    e['nmono']+=1; e['tot']+=degn+1
print('%-8s %-6s %7s %5s %5s %9s %12s'%('block','part','deg_n','deg_k','deg_l','(k,l)-mons','<=monomials'))
T=0; TM=0
for key in sorted(agg):
    e=agg[key]
    print('%-8s %-6s %7d %5d %5d %9d %12d'%(key[0],key[1],e['deg_n'],e['dk'],e['dl'],e['nmono'],e['tot']))
    T+=e['tot']; TM+=e['nmono']
print('%-8s %-6s %7s %5s %5s %9d %12d'%('TOTAL','','','','',TM,T))
