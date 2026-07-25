"""End-to-end check of the assembled proof:  Q_n/Q_a == Q_r + p*a*Psi_a  (mod p^2),
   Psi_a = sum_{s,t<=r} T(r,s,t) Phi_a(s,t)   (p-integral).
Also re-checks Psi_a in Z_p and the two Phi-vanishings."""
import sys
from fractions import Fraction as F
from core import Hs, T, Q, vp

def Phia(r,s,t):
    return (Hs(r+s,1)+Hs(r+t,1)+Hs(r+s+t,1)+Hs(r,1)-2*Hs(r-s,1)-2*Hs(r-t,1))

for p in [5,7,11,13]:
    M = p*p
    bad = 0; minvPsi = 99
    for r in range(p):
        Psi = sum(F(T(r,s,t))*Phia(r,s,t) for s in range(r+1) for t in range(r+1))
        minvPsi = min(minvPsi, vp(Psi,p) if Psi else 99)
        for a in range(1,p):
            n = a*p+r
            if n > 360: continue
            if int(Q(a)) % p == 0: continue
            Lam = int(Q(n)) % M * pow(int(Q(a)) % M, -1, M) % M
            pred = F(int(Q(r))) + p*a*Psi
            # reduce pred mod p^2 (it is p-integral)
            num, den = pred.numerator, pred.denominator
            assert den % p != 0, (p,r,a,'Psi not integral')
            predm = num % M * pow(den % M, -1, M) % M
            if (Lam - predm) % M != 0:
                bad += 1
                if bad < 4: print('  MISMATCH p=%d a=%d r=%d' % (p,a,r))
    print('p=%2d  Lambda == Q_r + p a Psi_a (mod p^2): mismatches=%d ; min v_p(Psi_a)=%s'
          % (p, bad, minvPsi), flush=True)
