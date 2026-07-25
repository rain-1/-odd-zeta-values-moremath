"""Experiment 1: base case from the ladder; and cellwise depth vs vT at level a<p."""
import sys, json
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from fractions import Fraction as F
from math import comb
from core import P, Q, Hs, vp, T

PR=[5,7,11,13,17,19,23,29,31,37,41,43,47]
print("== ladder base case: min_{n<p} v_p(P_n), v_p(W_n) ==")
for p in PR:
    mP=99; mW=99; argP=None
    for n in range(1,p):
        vP=vp(P(n),p)
        W=P(n)-Hs(n,5)*Q(n)
        vW=vp(W,p) if W else 10**9
        if vP<mP: mP=vP; argP=n
        mW=min(mW,vW)
    print("  p=%2d  min v_p(P_n)=%d (n=%s)   min v_p(W_n)=%d"%(p,mP,argP,mW))
