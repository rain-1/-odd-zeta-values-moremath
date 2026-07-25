"""g_hill.py -- maximise the SCALE-FREE objective  (C0 - budget + delta)/budget
over integral directions.  Under the 'equal-degradation' transfer model this is
exactly the quantity that decides zeta_5(3):

    p-adic margin / budget  =  (C0 - budget + delta)/budget  -  0.370431

(0.370431 = 1.175165 - 0.804734 = archimedean minus p-adic smallness ratio at
the totally symmetric point, where the p-adic weight-3 ledger gives
margin = 6 log5/4 - 3 = -0.5858, i.e. (alpha_p-growth)/3 = 0.804734.)

So zeta_5(3) is reached iff  max (C0-budget+delta)/budget > 0.370431.
"""
import itertools, random, sys
from g_group import m_params, delta_limit, admissible
from g_cal import f0, taus

def score(alpha, beta):
    if not admissible(alpha, beta): return None
    m0,m1,m2,m3 = m_params(alpha,beta); bud = 2*m1+m2
    if bud <= 0: return None
    try:
        t = taus(alpha,beta); asr=sorted(alpha); bsr=sorted(beta)
        c=[x for x in t if bsr[1]<x<asr[0]]; h=[x for x in t if x>asr[3]]
        if not c or not h: return None
        C0=-f0(alpha,beta,c[0]); C1=f0(alpha,beta,h[-1])
    except Exception: return None
    d,_,_ = delta_limit(alpha,beta)
    return ((C0-bud+d)/bud, d/bud, C0/bud, bud, d, C0, C1)

def neighbours(alpha, beta):
    out=[]
    for i in range(4):
        for j in range(4):
            for da in (-1,1):
                a=list(alpha); b=list(beta)
                a[i]+=da; b[j]+=da
                out.append((tuple(a),tuple(b)))
    for i in range(4):
        for j in range(i+1,4):
            for d in (-1,1):
                a=list(alpha); a[i]+=d; a[j]-=d
                out.append((tuple(a),tuple(beta)))
                b=list(beta); b[i]+=d; b[j]-=d
                out.append((tuple(alpha),tuple(b)))
    return out

seeds = [((18,17,16,19),(0,7,31,32)), ((6,6,8,6),(0,0,13,13)),
         ((6,7,7,6),(0,2,12,12)), ((13,13,14,14),(0,4,25,25)),
         ((9,9,10,10),(0,3,17,18)), ((16,17,18,19),(0,7,31,32)),
         ((25,26,27,28),(0,10,47,49)), ((11,11,12,12),(0,3,21,22))]
best=None
for s in seeds:
    cur=s; cs=score(*cur)
    if cs is None: continue
    for _ in range(220):
        improved=False
        for nb in neighbours(*cur):
            ns=score(*nb)
            if ns and ns[0] > cs[0]+1e-12:
                cur, cs, improved = nb, ns, True
        if not improved: break
    print(f"  seed {s} -> {cur}  obj={cs[0]:.6f} (delta/bud={cs[1]:.4f}, "
          f"C0/bud={cs[2]:.4f}, bud={cs[3]})")
    if best is None or cs[0]>best[1][0]: best=(cur,cs)
print()
cur,cs = best
mu = (cs[5]+cs[6])/(cs[5]-(cs[3]-cs[4]))
print(f"BEST objective (C0-budget+delta)/budget = {cs[0]:.6f}")
print(f"   at alpha={cur[0]} beta={cur[1]}, budget={cs[3]}, delta={cs[4]:.5f}")
print(f"   delta/budget={cs[1]:.6f}, C0/budget={cs[2]:.6f}, mu(zeta(3))<={mu:.6f}")
print(f"   THRESHOLD for zeta_5(3) (equal-degradation model): 0.370431")
print(f"   => p-adic margin/budget = {cs[0]-0.370431:+.6f}"
      f"   ({'REACHED' if cs[0]>0.370431 else 'short by %.6f'%(0.370431-cs[0])})")
