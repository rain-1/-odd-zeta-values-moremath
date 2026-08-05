"""eps69_x2a.py -- X-2A EXECUTED (Sol share 6a734412): the level-12,
r=2 apparatus.  Sol proposed restriction of scalars over Q(sqrt3); the
construction below does better: a Q-RATIONAL fold-vanishing source
exists in the weakly holomorphic space (poles at the t=infinity cusps),
because pole conditions break the Atkin-Lehner eigen-obstruction.

Facts established before this script (PSLQ, 40+ digits):
  * t = t12 = q*(eta1 eta12 / eta3 eta4)^4 is W12-invariant; AL-elliptic
    values 7 -+ 4 sqrt3 (roots of t^2-14t+1), cusp values {0, -1, oo};
  * S_3(12, chi_-4) = <f0, f1> (all-new, integral basis);
  * R  = f1/f0 at the fold      = 2 - 2 sqrt3   (exact, PSLQ);
  * R' = f1/f0 at the conjugate = 2 + 2 sqrt3 = sigma(R).
Hence v := (t-3) f0 - 2 f1 (weakly holomorphic, weight 3, chi_-4,
pole order 1 at the t=oo cusps) satisfies v = 0 at BOTH AL-elliptic
points: the rational conditions at the fold are Galois-forced at the
conjugate.  Both interior branch obstructions die at once; the only
obstructions left are the cusps (t=-1: period defect at worst).

Apparatus (r=2): F = theta3(q)^2 (weight 1, chi_-4; F*v has trivial
character), A_n = [t^n]F, B_n = [t^n](F * theta_q^{-2} v).
Deliverables:
  1. exact A_n, B_n (PARI series, N terms);
  2. fold-vanishing verification for v at both AL points (numeric);
  3. xi = lim B_n/A_n, error base rho of Lambda_n = A_n xi - B_n
     (slope fit; 13.93 = cusp-limited, faster = cusp-free);
  4. denominator profile of B_n: kappa, d_n^2-integrality test;
  5. margin M = log rho - kappa  (WIN iff > 0);
  6. PSLQ of xi against the CM L-values L(f0,2), L(f1,2), sqrt3, pi.
"""
import cypari2
import mpmath as mp
from fractions import Fraction as Fr
from math import lcm

NSER = 420
p = cypari2.Pari()
p.allocatemem(2000000000)
p.default('seriesprecision', NSER + 2)

# ---------------- exact series in PARI ----------------
p('t = q*(eta(q)*eta(q^12)/(eta(q^3)*eta(q^4)))^4 + O(q^%d)' % NSER)
p('F = (1 + 2*sum(n=1,25, q^(n^2)))^2 + O(q^%d)' % NSER)
mf = p.mfinit([12, 3, p.Mod(7, 12)], 1)
B0, B1 = list(p.mfbasis(mf))
c0 = p.mfcoefs(B0, NSER)
c1 = p.mfcoefs(B1, NSER)
p('cv0 = %s' % str(c0))
p('cv1 = %s' % str(c1))
p('f0 = sum(n=1,%d, cv0[n+1]*q^n) + O(q^%d)' % (NSER - 1, NSER))
p('f1 = sum(n=1,%d, cv1[n+1]*q^n) + O(q^%d)' % (NSER - 1, NSER))
p('v = (t - 3)*f0 - 2*f1')
# Eichler integral theta^{-2}: divide coefficient n by n^2
p('Th = sum(n=1,%d, polcoeff(v, n, q)/n^2 * q^n) + O(q^%d)' % (NSER - 1, NSER))
p('y = F*Th')
# invert t(q):  qt(t) with t(qt) = t
p('qt = serreverse(t)')
p('Aser = subst(F, q, qt)')
p('Bser = subst(y, q, qt)')
A = [Fr(str(p('polcoeff(Aser, %d, q)' % n))) for n in range(NSER - 4)]
Bv = [Fr(str(p('polcoeff(Bser, %d, q)' % n))) for n in range(NSER - 4)]
NMAX = len(A) - 1
print('exact series to n = %d' % NMAX)
print('A_n integral:', all(x.denominator == 1 for x in A))
print('A_n:', [str(x) for x in A[:8]])
print('B_n:', [str(x) for x in Bv[:8]])

# ---------------- 2. fold-vanishing verification ----------------
mp.mp.dps = 60
qc = mp.exp(-2 * mp.pi / mp.sqrt(12))
tau2 = (48 + 1j * mp.sqrt(48)) / 168
co0 = [int(c0[n]) for n in range(NSER)]
co1 = [int(c1[n]) for n in range(NSER)]
tc_alg = 7 - 4 * mp.sqrt(3)


def ev(coeffs, q):
    return sum(c * q ** n for n, c in enumerate(coeffs))


tco = [Fr(str(p('polcoeff(t, %d, q)' % n))) for n in range(NSER)]
for name, pt in [('fold', qc), ('conjugate AL', mp.exp(2j * mp.pi * tau2))]:
    tv = ev([mp.mpf(str(x)) for x in tco], pt)
    f0v = ev(co0, pt)
    f1v = ev(co1, pt)
    vv = (tv - 3) * f0v - 2 * f1v
    print('%s: t = %s;  v = %s  (expect 0)' %
          (name, mp.nstr(tv, 12), mp.nstr(abs(vv), 3)))

# ---------------- 3. limit and error base ----------------
mp.mp.dps = 400
Af = [mp.mpf(x.numerator) / mp.mpf(x.denominator) for x in A]
Bf = [mp.mpf(x.numerator) / mp.mpf(x.denominator) for x in Bv]
xi = Bf[NMAX] / Af[NMAX]
print('xi = B/A at n=%d = %s' % (NMAX, mp.nstr(xi, 40)))
lam = [Af[n] * xi - Bf[n] for n in range(NMAX + 1)]
print('log|Lambda_n|/n (error base rho = e^{-slope}):')
for n in [50, 100, 150, 200, 250, 300, 350, NMAX - 10]:
    if abs(lam[n]) > 0:
        print('  n=%3d  |Lambda| = %8s   local base %.6f' %
              (n, mp.nstr(abs(lam[n]), 4),
               float((abs(lam[n - 10]) / abs(lam[n])) ** (mp.mpf(1) / 10))))
rho_est = (abs(lam[NMAX - 60]) / abs(lam[NMAX - 10])) ** (mp.mpf(1) / 50)
print('rho estimate (n~%d): %.8f   (13.9282 = cusp-limited; bigger = free)'
      % (NMAX - 10, float(rho_est)))

# ---------------- 4. denominators ----------------
dn = 1
prof = []
d2ok = True
for n in range(1, NMAX + 1):
    dn = lcm(dn, n)
    if (dn * dn * Bv[n]).denominator != 1:
        d2ok = False
    if n % 30 == 0:
        prof.append((n, mp.log(mp.mpf(Bv[n].denominator)) / n))
print('d_n^2 * B_n integral for all n <= %d: %s' % (NMAX, d2ok))
print('kappa profile (log den / n):',
      [(n, float(x)) for (n, x) in prof])
kap = float(mp.log(mp.mpf(Bv[NMAX].denominator)) / NMAX)
rho_l = float(mp.log(rho_est))
print('MARGIN  M = log rho - kappa = %.4f - %.4f = %.4f  (%s)'
      % (rho_l, kap, rho_l - kap, 'WIN candidate' if rho_l > kap else 'loses'))

# ---------------- 6. save xi for PSLQ vs L-values ----------------
with open('eps69_xi.txt', 'w') as fh:
    fh.write(mp.nstr(xi, 350))
print('xi saved to eps69_xi.txt (350 digits) for the L-value PSLQ pass')
