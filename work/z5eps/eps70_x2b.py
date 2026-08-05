"""eps70_x2b.py -- X-2A embedding table + X-2B (Sol share 6a734412).

Part A (completes Sol's requested table): the K-eigenvector source
s = f0 + ((1+sqrt3)/4) f1 (pure lambda = -i AL-eigencomponent) and its
Galois conjugate.  PARI arithmetic over Q(w), w^2 = 3.  Measure both
embeddings' error bases rho, rho^sigma.  Prediction from the parity
analysis (and eps69's rational-source result): one embedding is
fold-regular (rho ~ 13.93), the other fold-stuck (rho ~ 1); the norm
criterion rho*rho^sigma > e^{2 kappa} = 54.6 fails.

Part B (X-2B): the r=3 apparatus on the SAME t12 family with the
RATIONAL W12-odd cusp source f* = f6(q) - 4 f6(q^2) (weight 4, trivial
character, f*(tau12) = 0 with pure odd parity -- even weight, so parity
IS rational here).  F2 = theta3(q)^4 (weight 2).
  * measure rho: 13.93 would mean the t=-1 cusp obstruction is inactive
    for cusp-form sources (Sol's Q3 answered YES) and score3 = 1.44;
  * d_n^3-integrality of B*_n; kappa profile;
  * X-2B proper: prime-local exponents e_p(n) = v_p(den B*_n) profiled
    by the quadratic character chi_12(p) = kronecker(12,p): test Sol's
    density-1/2 deflation (need effective kappa < log(7+4sqrt3) = 2.634).
"""
import cypari2
import mpmath as mp
from fractions import Fraction as Fr
from math import lcm

NSER = 420
p = cypari2.Pari()
p.allocatemem(4000000000)
p.default('seriesprecision', NSER + 2)

p('t = q*(eta(q)*eta(q^12)/(eta(q^3)*eta(q^4)))^4 + O(q^%d)' % NSER)
p('qt = serreverse(t)')

# ================= PART A: K-eigenvector table =================
mf = p.mfinit([12, 3, p.Mod(7, 12)], 1)
B0, B1 = list(p.mfbasis(mf))
c0 = p.mfcoefs(B0, NSER)
c1 = p.mfcoefs(B1, NSER)
p('cv0 = %s' % str(c0))
p('cv1 = %s' % str(c1))
p('f0 = sum(n=1,%d, cv0[n+1]*q^n) + O(q^%d)' % (NSER - 1, NSER))
p('f1 = sum(n=1,%d, cv1[n+1]*q^n) + O(q^%d)' % (NSER - 1, NSER))
p('F1w = (1 + 2*sum(n=1,25, q^(n^2)))^2 + O(q^%d)' % NSER)
p('w = Mod(y, y^2 - 3)')
p('s_src = f0 + (1+w)/4 * f1')
p('ThA = sum(n=1,%d, polcoeff(s_src, n, q)/n^2 * q^n) + O(q^%d)'
  % (NSER - 1, NSER))
p('yA = F1w*ThA')
p('BserA = subst(yA, q, qt)')
p('AserA = subst(F1w, q, qt)')
NM = NSER - 6
mp.mp.dps = 420
r3 = mp.sqrt(3)


def emb(polmod_str, sign):
    """PARI t_POLMOD in y (mod y^2-3) -> mpf under y -> sign*sqrt3."""
    g = p(polmod_str)
    li = p('liftpol(%s)' % polmod_str)
    a = p('polcoeff(%s, 0, y)' % ('(' + str(li) + ')'))
    b = p('polcoeff(%s, 1, y)' % ('(' + str(li) + ')'))
    return (mp.mpf(Fr(str(a)).numerator) / mp.mpf(Fr(str(a)).denominator)
            + sign * r3 * mp.mpf(Fr(str(b)).numerator)
            / mp.mpf(Fr(str(b)).denominator))


A_ = [Fr(str(p('polcoeff(AserA, %d, q)' % n))) for n in range(NM + 1)]
Af = [mp.mpf(x.numerator) / mp.mpf(x.denominator) for x in A_]
# exact degeneracy test: is B_n A_m - B_m A_n identically 0 (K-exact)?
p('cross(n, m) = polcoeff(BserA, n, q)*polcoeff(AserA, m, q) - polcoeff(BserA, m, q)*polcoeff(AserA, n, q)')
degen = all(str(p('cross(%d, %d)' % (n, NM))) in ('0', 'Mod(0, y^2 - 3)')
            for n in [5, 17, 50, 123, 250])
print('A: exact degeneracy (Lambda identically 0):', degen)
if not degen:
    for sign, tag in [(1, 'id'), (-1, 'sigma')]:
        Bf = [emb('polcoeff(BserA, %d, q)' % n, sign) for n in range(NM + 1)]
        xi = Bf[NM] / Af[NM]
        lam = [Af[n] * xi - Bf[n] for n in range(NM + 1)]
        print('A-embedding %s: xi = %s' % (tag, mp.nstr(xi, 25)))
        for n in [150, 250, 350, NM - 10]:
            if abs(lam[n]) > 0 and abs(lam[n - 30]) > 0:
                print('  n=%3d local error base %.6f' % (n,
                      float((abs(lam[n - 30]) / abs(lam[n])) ** (mp.mpf(1)/30))))
            else:
                print('  n=%3d Lambda below precision (very fast decay '
                      'or exact 0): |lam|=%s' % (n, mp.nstr(abs(lam[n]), 3)))
else:
    xi_id = emb('polcoeff(BserA, %d, q)' % NM, 1) / Af[NM]
    print('A: xi is EXACTLY B_n/A_n stationary = algebraic in K: %s'
          % mp.nstr(xi_id, 25))
    print('A: => the connection value of the eigenvector source is')
    print('   ALGEBRAIC -- the cuspidal period functional VANISHES on the')
    print('   AL-eigenline.  Norm route dead at the source-selection level.')
print('norm criterion needed rho*rho_sigma > e^4 = 54.60')

# ================= PART B: r=3 rational f* apparatus =================
p('f6 = q*(eta(q)*eta(q^2)*eta(q^3)*eta(q^6))^2 + O(q^%d)' % NSER)
p('fstar = f6 - 4*subst(f6, q, q^2)')
p('F2 = (1 + 2*sum(n=1,25, q^(n^2)))^4 + O(q^%d)' % NSER)
p('ThB = sum(n=1,%d, polcoeff(fstar, n, q)/n^3 * q^n) + O(q^%d)'
  % (NSER - 1, NSER))
p('yB = F2*ThB')
p('BserB = subst(yB, q, qt)')
p('AserB = subst(F2, q, qt)')
A3 = [Fr(str(p('polcoeff(AserB, %d, q)' % n))) for n in range(NM + 1)]
B3 = [Fr(str(p('polcoeff(BserB, %d, q)' % n))) for n in range(NM + 1)]
print('\nB: A_n integral: %s;  A_n: %s'
      % (all(x.denominator == 1 for x in A3), [str(x) for x in A3[:7]]))
print('B: B*_n: %s' % [str(x) for x in B3[:6]])
Af3 = [mp.mpf(x.numerator) / mp.mpf(x.denominator) for x in A3]
Bf3 = [mp.mpf(x.numerator) / mp.mpf(x.denominator) for x in B3]
xi3 = Bf3[NM] / Af3[NM]
print('B: xi = %s' % mp.nstr(xi3, 30))
lam3 = [Af3[n] * xi3 - Bf3[n] for n in range(NM + 1)]
for n in [100, 200, 300, NM - 10]:
    print('  n=%3d local error base %.6f'
          % (n, float((abs(lam3[n - 30]) / abs(lam3[n])) ** (mp.mpf(1)/30))))
print('  (0.0718 = fold-stuck; 13.93*t_c = 1 = cusp-limited;'
      ' 0.0718*13.93^2=... elliptic-limited: local base -> t_next)')

# d_n^3 integrality and kappa
dn = 1
d3ok = True
for n in range(1, NM + 1):
    dn = lcm(dn, n)
    if (dn ** 3 * B3[n]).denominator != 1:
        d3ok = False
        break
print('B: d_n^3 * B*_n integral (n<=%d): %s' % (NM, d3ok))
kaps = [(n, float(mp.log(mp.mpf(B3[n].denominator)) / n))
        for n in range(60, NM + 1, 60)]
print('B: kappa profile:', kaps)

# X-2B proper: e_p(n) by quadratic character chi_12(p) = kronecker(12, p)
from sympy import primerange, factorint
print('\nX-2B: prime-local exponents at n = %d (v_p of den):' % NM)
den = B3[NM].denominator
fac = factorint(den)
rows_p, rows_m = [], []
import sympy
for q_ in primerange(5, NM + 1):
    hp = 0
    x = q_
    while x <= NM:
        hp += 1
        x *= q_
    ep = fac.get(q_, 0)
    chi = sympy.jacobi_symbol(12, q_)
    (rows_p if chi == 1 else rows_m).append((q_, ep, 3 * hp))
full_p = sum(1 for (q_, e, m) in rows_p if e == m)
full_m = sum(1 for (q_, e, m) in rows_m if e == m)
print('  chi_12 = +1 primes: %d, full-cost e=3h: %d  -> %s'
      % (len(rows_p), full_p, rows_p[:12]))
print('  chi_12 = -1 primes: %d, full-cost e=3h: %d  -> %s'
      % (len(rows_m), full_m, rows_m[:12]))
print('  Sol needs a density-1/2 class with e <= 3h - 1'
      ' (effective kappa < 2.634)')
