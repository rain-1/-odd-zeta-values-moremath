"""Lemma D++ last sub-case:  a+b=p-1, r+s>=p, s<=r, s+t>=p  ==>  v_p(T(n,k,l)) >= 4.
Exhaustive over p in argv."""
import sys
from math import comb
from core import vp
def T(n,k,l):
    return comb(n+k,n)*comb(n,k)**2*comb(n+l,n)*comb(n,l)**2*comb(n+k+l,n)
for p in [int(x) for x in sys.argv[1:]] or [5,7,11,13]:
    n_case = 0; bad = 0; mn = 99
    # also the full Lemma D++ statement
    n_all = 0; bad_all = 0; mn_all = 99
    for a in range(p):
        for r in range(p):
            n = a*p+r
            for b in range(a+1):
                for s in range(p):
                    k = b*p+s
                    if k > n: continue
                    beta = a+b+(1 if r+s>=p else 0)
                    if not (beta >= p and a+b < p): continue
                    for c in range(a+1):
                        for t in range(p):
                            l = c*p+t
                            if l > n: continue
                            v = vp(T(n,k,l), p)
                            n_all += 1; mn_all = min(mn_all,v)
                            if v < 4: bad_all += 1
                            if s <= r and s+t >= p:
                                n_case += 1; mn = min(mn,v)
                                if v < 4: bad += 1
    print('p=%2d  D++ all: %6d triples, failures=%d, min v_p=%d | LAST SUB-CASE (s<=r, s+t>=p): %6d triples, failures=%d, min v_p=%d'
          % (p, n_all, bad_all, mn_all, n_case, bad, mn), flush=True)
