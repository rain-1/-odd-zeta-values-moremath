"""(1) t-wise exact vanishing of sum_s T(r,s,t) Phi_b(s,t).
   (2) does the IN-REGIME restricted sum still vanish mod p?"""
from fractions import Fraction as F
from core import Hs, T, vp

def Phib(r, s, t):
    return (Hs(r+s,1) + Hs(r+s+t,1) - 3*Hs(s,1) + 2*Hs(r-s,1) - Hs(s+t,1))

print("== (1) t-wise exact identity  sum_{s=0}^{r} T(r,s,t) Phi_b(s,t) = 0 ? ==")
bad = 0
for r in range(0, 12):
    for t in range(0, r+2):
        S = sum(T(r,s,t)*Phib(r,s,t) for s in range(r+1))
        if S != 0:
            bad += 1; print('  NONZERO r=%d t=%d : %s' % (r,t,S))
print("  checked r<=11, all t: nonzero count =", bad)

print()
print("== (2) in-regime restricted:  sum_{s,t<=r, r+s+t<p} T(r,s,t) Phi_b  mod p ==")
for p in (5,7,11,13,17,19):
    worst = []
    for r in range(p):
        S = F(0)
        for s in range(r+1):
            for t in range(r+1):
                if r+s+t < p:
                    S += T(r,s,t)*Phib(r,s,t)
        v = vp(S, p) if S != 0 else 99
        worst.append((r, v))
    print(' p=%2d :' % p, ' '.join('r=%d:v=%s' % (r, 'inf' if v==99 else v) for r,v in worst))
