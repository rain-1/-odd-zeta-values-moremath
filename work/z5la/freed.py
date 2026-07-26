import numpy as np, sys, zla, solve, fastlin, joint
from solve import Ansatz, KL1, NK, NL
p = 4194301; n = 5
def freed(which, D, deg, npts, morders, base=None, force=(1,1)):
    pd = solve.PointData(which, p, n, npts=npts, base=base)
    A = Ansatz(D,D,deg,deg,deg,deg,force_k=force[0],force_l=force[1])
    M,_,_ = joint.build(pd, A)
    J = pd.J; F = pd.F
    mmax = max(morders)
    W = np.zeros((J*npts, mmax+1), dtype=np.int64)
    for t,(k,l) in enumerate(pd.pts):
        for a in range(mmax+1):
            el = zla.w_shift_mixed(F, pd.w, a, n, k, l, pd.base)
            v = zla.el_to_vec(F, pd.B, zla.el_scale(F, el, F.cst(zla.Pi(n,k,l,a))))
            for i in range(J): W[i*npts+t, a] = v[i]
    R0,_ = fastlin.rank_only(M, p)
    print('  %s J=%d nc=%d cols=%d rows=%d rank(M)=%d nullity=%d'%(which,J,A.nc,M.shape[1],M.shape[0],R0,M.shape[1]-R0), flush=True)
    for m in morders:
        Mm = np.concatenate([M, (-W[:, :m+1])%p], axis=1)
        R1,_ = fastlin.rank_only(Mm, p)
        print('     order<=%d : rank=%d  -> %d telescoper direction(s)'%(m, R1, (m+1)-(R1-R0)), flush=True)
if __name__=='__main__':
    which = sys.argv[1]
    print('CONTROL: Q-row' if which=='q0' else 'WEIGHT '+which, flush=True)
    if which=='q0':
        freed('q0', [(KL1,1)], 12, 400, [3,4])
    else:
        for D,deg in (([],10), ([(KL1,1)],10),
                      ([(KL1,1)]+[(NK[j],1) for j in (1,2,3)]+[(NL[j],1) for j in (1,2,3)],12)):
            freed('w3', D, deg, 260, [3,4,5,6,8], base=zla.BASE3)
