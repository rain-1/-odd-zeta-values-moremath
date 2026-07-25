import json, math
from fractions import Fraction as F
from math import gcd
W='/home/ubuntu/fable-episode-2/zeta-math/worthiness/falsify_data/'
d={k:json.load(open(W+'ladder_%s.json'%k)) for k in ('P','Ph')}
def g(k,n):
    v=d[k][str(n)]; return F(int(v[0]),int(v[1]))
def dlcm(n):
    L=1
    for i in range(1,n+1): L=L*i//gcd(L,i)
    return L
print("=== WEIGHT-5 SHARP DENOMINATOR LAW (361 exact terms) ===")
for mult,lab in ((1,'d^5'),(12,'12*d^5'),(2,'2*d^5'),(6,'6*d^5')):
    okP=sum(1 for n in range(361) if (mult*dlcm(n)**5)%g('P',n).denominator==0)
    print(f"  den(P_n) | {lab:8s} : {okP}/361")
for mult,lab in ((1,'d^4'),(12,'12*d^4'),(1,'d^5')):
    e=4 if 'd^4' in lab else 5
    okH=sum(1 for n in range(361) if (mult*dlcm(n)**e)%g('Ph',n).denominator==0)
    print(f"  den(Ph_n)| {lab:8s} : {okH}/361")
