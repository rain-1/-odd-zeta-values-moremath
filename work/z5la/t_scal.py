import numpy as np, zla, solve, fastlin, qrow, ratrec
from solve import Ansatz, KL1, KL2, NK, NL, MK, ML
p = 4194301; n = 5
F = zla.Fp(p)
w = zla.weight_element(F,'w3'); B = zla.closure_basis(w); J=len(B)
rf, sf = qrow.make_evals(n,p)
fixedidx = {B.index(m): int(w[m]) for m in w}
def fval(i,k,l):
    tot = zla.el_to_vec(F,B,zla.rhs_element_mixed(F,w,n,k,l,{}))[i]
    gk = zla.gk_val(F,n,k,l); gl = zla.gl_val(F,n,k,l)
    Sk = zla.shift_matrix_mixed(F,B,'k',n,k,l,{}); Sl = zla.shift_matrix_mixed(F,B,'l',n,k,l,{})
    for j,wj in fixedidx.items():
        a=(Sk[j][i]-(1 if i==j else 0))%p; b=(Sl[j][i]-(1 if i==j else 0))%p
        if a: tot=(tot-gk*a%p*(wj*rf(n,k+1,l)%p))%p
        if b: tot=(tot-gl*b%p*(wj*sf(n,k,l+1)%p))%p
    return tot%p
def probe(i,var,other=987654):
    xs=[];vs=[];x=1000
    while len(xs)<130:
        x+=1
        try: v = fval(i,x,other) if var=='k' else fval(i,other,x)
        except ZeroDivisionError: continue
        xs.append(x);vs.append(v)
    r=ratrec.null_min_deg(vs,xs,p,60)
    if r is None: return None
    num,den=r
    if var=='k':
        roots=[('k+%d'%j,-j) for j in (1,2,3)]+[('n+k+%d'%j,-n-j) for j in range(1,7)]+\
              [('n+%d-k'%j,n+j) for j in range(0,7)]+[('k+l+%d'%j,(-other-j)%p) for j in (1,2,3)]+\
              [('n+k+l+%d'%j,(-n-other-j)%p) for j in (1,2,3)]
    else:
        roots=[('l+%d'%j,-j) for j in (1,2,3)]+[('n+l+%d'%j,-n-j) for j in range(1,7)]+\
              [('n+%d-l'%j,n+j) for j in range(0,7)]+[('k+l+%d'%j,(-other-j)%p) for j in (1,2,3)]+\
              [('n+k+l+%d'%j,(-n-other-j)%p) for j in (1,2,3)]
    m,rest = ratrec.factor_mult(den,roots,p)
    return len(num)-1,len(den)-1,m,len(rest)-1
for i in range(J):
    if i in fixedidx: continue
    for var in ('k','l'):
        r=probe(i,var)
        print('f%-14s %s : num=%2d den=%2d %s rest=%d'%(str(B[i]),var,r[0],r[1],r[2],r[3]), flush=True)
