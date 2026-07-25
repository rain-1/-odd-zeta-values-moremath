import sys
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import Ph, Q, P, vp
from sympy import primerange
worst={}
for p in primerange(5,60):
    m=99
    for n in range(1,p):
        try: v=vp(Ph(n),p)
        except KeyError: break
        m=min(m,v)
    worst[p]=m
print('min_{n<p} v_p(Phat_n):',worst)
# also denominators
import math
for n in range(1,25):
    d=Ph(n).denominator
    print(n, d)
