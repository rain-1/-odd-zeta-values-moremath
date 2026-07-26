"""common n-denominator of the reconstructed cofactors, and its factorisation."""
import os,sys,pickle,time
import numpy as np
HERE='/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'
sys.path.insert(0,HERE); sys.path.insert(1,'/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import ratrec
from multiprocessing import Pool

def pmul(a,b,p):
    o=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): o[i+j]=(o[i+j]+x*y)%p
    return ratrec.trim(o)
def pmod(a,b,p):
    a=list(a); db=len(b)-1; ib=pow(b[-1]%p,p-2,p)
    while len(a)-1>=db and any(a):
        d=len(a)-1
        if a[-1]==0: a.pop(); continue
        c=a[-1]*ib%p
        for i in range(db+1): a[d-db+i]=(a[d-db+i]-c*b[i])%p
        a.pop()
    return ratrec.trim(a)
def pgcd(a,b,p):
    a=ratrec.trim(a); b=ratrec.trim(b)
    while len(b)>1 or (len(b)==1 and b[0]):
        a,b=b,pmod(a,b,p)
    return a
def pdiv(a,b,p):
    a=list(a); db=len(b)-1; ib=pow(b[-1]%p,p-2,p); q=[0]*(len(a)-db)
    while len(a)-1>=db:
        d=len(a)-1
        if a[-1]==0: a.pop(); continue
        c=a[-1]*ib%p; q[d-db]=c
        for i in range(db+1): a[d-db+i]=(a[d-db+i]-c*b[i])%p
        a.pop()
    return ratrec.trim(q)

def job(args):
    j,vals,xs,p=args
    r=ratrec.null_min_deg(vals,xs,p,55)
    return (j,r[1] if r else None)

if __name__=='__main__':
    d=pickle.load(open(os.path.join(HERE,'nsweep_1p.pkl'),'rb'))
    data,ns,ps=d['data'],d['ns'],d['ps']; p=ps[0]
    xs=[n for n in ns if data.get((n,p)) is not None]
    Mv=np.array([data[(n,p)] for n in xs],dtype=np.int64)
    nz=[j for j in range(Mv.shape[1]) if np.count_nonzero(Mv[:,j])]
    t0=time.time()
    dens={}
    with Pool(10) as pool:
        for j,den in pool.imap_unordered(job,[(j,list(Mv[:,j]),xs,p) for j in nz],chunksize=8):
            dens[j]=den
    L=[1]
    for j in nz:
        den=dens[j]
        if den is None or len(den)==1: continue
        g=pgcd(L,den,p)
        L=pmul(L,pdiv(den,g,p),p)
    print('common n-denominator degree = %d   [%.0fs]'%(len(L)-1,time.time()-t0),flush=True)
    # small integer roots?
    roots=[]
    for a in range(-80,81):
        if ratrec.polyval(L,a%p,p)==0:
            cur=list(L); m=0
            while len(cur)>1 and ratrec.polyval(cur,a%p,p)==0:
                cur,_=ratrec.divide_out(cur,a%p,p); m+=1
            roots.append((a,m))
    print('integer roots (n = r, multiplicity):',roots,flush=True)
    tot=sum(m for _,m in roots)
    print('degree accounted for by integer roots: %d of %d'%(tot,len(L)-1),flush=True)
    # 2n+c roots?
    half=[]
    inv2=pow(2,p-2,p)
    for c in range(1,40):
        r=(-c)*inv2%p
        if ratrec.polyval(L,r,p)==0: half.append(c)
    print('roots of the form n = -c/2 :',half,flush=True)
    pickle.dump(dict(L=L,dens=dens,nz=nz,xs=xs,p=p),open(os.path.join(HERE,'lcmden.pkl'),'wb'))
