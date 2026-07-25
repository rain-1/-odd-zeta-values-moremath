import json, sys
from fractions import Fraction as F
from math import comb
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import Hs, vp

def load(fn='/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/w5_allp.json'):
    d = json.load(open(fn)); terms=[]
    for lab,(num,den) in d.items():
        fg,rest = lab.split(']x'); f,g = fg[1:].split('|'); h,s = rest.split('x')
        sp = lambda x: [] if x=='1' else x.split('*')
        terms.append((F(num,den), sp(f), sp(g), sp(h), sp(s)))
    return terms

TERMS = load()

def w5(n,k,l,terms=None):
    terms = terms or TERMS
    def L(nm,i):
        t,r = nm[0], int(nm[1])
        return (Hs(n+i,r)-Hs(i,r)) if t=='A' else (Hs(n-i,r)-Hs(i,r))
    tot=F(0)
    for cf,f,g,h,s in terms:
        v=cf
        for nm in h: v *= Hs(n+k+l,int(nm[1])) - Hs(k+l,int(nm[1]))
        for nm in s: v *= Hs(n,int(nm[1]))
        pf=F(1)
        for nm in f: pf*=L(nm,k)
        for nm in g: pf*=L(nm,l)
        if f==g:
            tot += v*pf
        else:
            pb=F(1)
            for nm in f: pb*=L(nm,l)
            for nm in g: pb*=L(nm,k)
            tot += v*(pf+pb)
    return tot

def v5(n,k,l,terms=None):
    return w5(n,k,l,terms) - Hs(n,5)

def Tl(a,b,c):
    return comb(a+b,a)*comb(a,b)**2*comb(a+c,a)*comb(a,c)**2*comb(a+b+c,a)
