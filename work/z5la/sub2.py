"""2-block necessary subsystem {('u2','xk'), ('xk',)} for weight 3.
Its equations involve ONLY those two blocks' unknowns, so its inconsistency
implies inconsistency of the whole certificate system."""
import numpy as np, zla, solve, fastlin
from solve import Ansatz, dval

def build(pd, A, i1, j2):
    """i1 = low block (xk), j2 = high block (u2 xk)"""
    p, n, N = pd.p, pd.n, pd.npts
    nc = A.nc; nr = len(A.mons_r)
    M = np.zeros((2*N, 2*nc), dtype=np.int64)
    rhs = np.zeros(2*N, dtype=np.int64)
    dmax = max(max(a,b) for a,b in A.mons_r+A.mons_s)+2
    for t,(k,l) in enumerate(pd.pts):
        gk, gl = int(pd.gk[t]), int(pd.gl[t])
        iDr = pow(dval(A.Dr,n,k,l,p),p-2,p);  iDrk = pow(dval(A.Dr,n,k+1,l,p),p-2,p)
        iDs = pow(dval(A.Ds,n,k,l,p),p-2,p);  iDsl = pow(dval(A.Ds,n,k,l+1,p),p-2,p)
        kp=[pow(k%p,a,p) for a in range(dmax)]; lp=[pow(l%p,b,p) for b in range(dmax)]
        k1=[pow((k+1)%p,a,p) for a in range(dmax)]; l1=[pow((l+1)%p,b,p) for b in range(dmax)]
        vr1=np.array([k1[a]*lp[b]%p*iDrk%p for a,b in A.mons_r],dtype=np.int64)
        vr0=np.array([kp[a]*lp[b]%p*iDr%p  for a,b in A.mons_r],dtype=np.int64)
        vs1=np.array([kp[a]*l1[b]%p*iDsl%p for a,b in A.mons_s],dtype=np.int64)
        vs0=np.array([kp[a]*lp[b]%p*iDs%p  for a,b in A.mons_s],dtype=np.int64)
        Sk = (pd.Nk[t]+np.eye(pd.J,dtype=np.int64))%p
        Sl = (pd.Nl[t]+np.eye(pd.J,dtype=np.int64))%p
        # block order in columns: [0]=i1(xk) , [1]=j2(u2xk)
        for row_i,(i,off) in enumerate(((j2,0),(i1,N))):
            row = off+t
            for col_b,j in ((0,i1),(1,j2)):
                a_k = int(Sk[i,j]); a_l = int(Sl[i,j])
                base = col_b*nc
                if a_k: M[row, base:base+nr] = gk*a_k%p*vr1%p
                if a_l: M[row, base+nr:base+nc] = gl*a_l%p*vs1%p
            bb = (0 if i==i1 else 1)*nc
            M[row, bb:bb+nr] = (M[row, bb:bb+nr]-vr0)%p
            M[row, bb+nr:bb+nc] = (M[row, bb+nr:bb+nc]-vs0)%p
            rhs[row] = pd.bvec[t,i]
    return M, rhs
