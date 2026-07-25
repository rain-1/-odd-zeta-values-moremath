"""T2 step 1: validate the kappa engine on the two Apery operators."""
import sys, time
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma')
from mpmath import mp, mpf, sqrt, zeta, pi, nstr, pslq, mpmathify
from frobkappa import kappa_series

mp.dps = int(sys.argv[1]) if len(sys.argv) > 1 else 160
K = int(sys.argv[2]) if len(sys.argv) > 2 else 12
M = int(sys.argv[3]) if len(sys.argv) > 3 else 80
NS = [int(x) for x in (sys.argv[4].split(',') if len(sys.argv) > 4 else ['300', '400'])]

print("mp.dps=%d  K=%d  M=%d  n=%s" % (mp.dps, K, M, NS))

def report(name, qs, lam, exact_stokes=None):
    t0 = time.time()
    res, alpha, c, chk = kappa_series(qs, lam, 0, K, M, NS)
    print("\n=== %s ===" % name)
    print("  char.residual = %s   alpha = %s" % (nstr(chk, 5), nstr(alpha, 20)))
    ks = [res[n][0] for n in NS]
    print('  Stokes S(0) = %s' % nstr(res[NS[-1]][1], 40))
    print('  S(0) agreement between n: %s' % nstr(abs(res[NS[-1]][1]-res[NS[-2]][1])/abs(res[NS[-1]][1]), 5))
    # agreement between the two n
    for i in range(K + 1):
        d = abs(ks[-1][i] - ks[-2][i])
        rel = d / (abs(ks[-1][i]) + mpf(10) ** (-mp.dps))
        print("  kappa_%-2d = %s   [agree %d digits]" % (
            i, nstr(ks[-1][i], min(mp.dps - 5, 60)),
            int(-mp.log10(rel + mpf(10) ** (-mp.dps)))))
    print("  time %.1fs" % (time.time() - t0))
    return ks[-1], alpha, c

# ---------- Apery zeta(3):  L = D^3 - t(34D^3+51D^2+27D+5) + t^2 (D+1)^3
q3 = [[0, 0, 0, 1], [-5, -27, -51, -34], [1, 3, 3, 1]]
lam3 = 17 + 12 * sqrt(2)
k3, a3, c3 = report("Apery zeta(3), c = 17-12sqrt2", q3, lam3)

z = [None, None] + [zeta(i) for i in range(2, K + 4)]
print("\n  --- identifications (BV Ex.29 / GZ2 (47)) ---")
tgt = {2: -2 * z[2], 3: mpf(17) / 6 * z[3], 4: 2 * z[4]}
for i, t in tgt.items():
    print("   kappa_%d - target = %s" % (i, nstr(k3[i] - t, 8)))
print("   kappa_5              = %s" % nstr(k3[5], 50))
print("   (7/3)z5 - (17/3)z2z3 = %s" % nstr(mpf(7) / 3 * z[5] - mpf(17) / 3 * z[2] * z[3], 50))
print("   (7/5)z5 - (17/3)z2z3 = %s" % nstr(mpf(7) / 5 * z[5] - mpf(17) / 3 * z[2] * z[3], 50))
print("   diff vs 7/3 form     = %s" % nstr(k3[5] - (mpf(7) / 3 * z[5] - mpf(17) / 3 * z[2] * z[3]), 8))
print("   diff vs 7/5 form     = %s" % nstr(k3[5] - (mpf(7) / 5 * z[5] - mpf(17) / 3 * z[2] * z[3]), 8))
if K >= 6:
    print("   kappa_6 - (4/945)pi^6 - 4z3^2 = %s" %
          nstr(k3[6] - mpf(4) / 945 * pi ** 6 - 4 * z[3] ** 2, 8))
if K >= 7:
    print("   kappa_7 - (-7/9 pi^2 z5 + 7/108 pi^4 z3 - 5/3 z7) = %s" %
          nstr(k3[7] - (-mpf(7) / 9 * pi ** 2 * z[5] + mpf(7) / 108 * pi ** 4 * z[3]
                        - mpf(5) / 3 * z[7]), 8))
if K >= 8:
    print("   kappa_8 - (-11/37800 pi^8 + 6 z5z3 - 4/3 pi^2 z3^2) = %s" %
          nstr(k3[8] - (-mpf(11) / 37800 * pi ** 8 + 6 * z[5] * z[3]
                        - mpf(4) / 3 * pi ** 2 * z[3] ** 2), 8))
if K >= 9:
    print("   kappa_9 - GZ2(47) = %s" %
          nstr(k3[9] - (mpf(8) / 9 * z[9] + mpf(34) / 9 * z[3] ** 3 + mpf(5) / 9 * pi ** 2 * z[7]
                        + mpf(149) / 11340 * pi ** 6 * z[3] + mpf(5) / 54 * pi ** 4 * z[5]), 8))
if K >= 10:
    print("   kappa_10 - GZ2(47) = %s" %
          nstr(k3[10] - (-mpf(107) / 249480 * pi ** 10 - 4 * z[5] ** 2 - 8 * z[3] * z[7]
                         + mpf(4) / 45 * pi ** 4 * z[3] ** 2 - 2 * pi ** 2 * z[3] * z[5]), 8))

# Stokes constant closed form check: A_n ~ (1+sqrt2)^{4n+2}/(2^{9/4} pi^{3/2} n^{3/2})
print("\n  --- Stokes constant control ---")
print("   predicted S(0) = (1+sqrt2)^2/(2^{9/4} pi^{3/2}) = %s" %
      nstr((1 + sqrt(2)) ** 2 / (mpf(2) ** mpf('2.25') * pi ** mpf('1.5')), 30))

# ---------- Apery zeta(2): L = D^2 - t(11D^2+11D+3) - t^2 (D+1)^2
q2 = [[0, 0, 1], [-3, -11, -11], [-1, -2, -1]]
lam2 = (11 + 5 * sqrt(5)) / 2
k2, a2, c2 = report("Apery zeta(2)/Beauville D, c = (-11+5sqrt5)/2", q2, lam2)
print("\n  --- identifications (BV Ex.28 / RV Table 2 case D) ---")
print("   kappa_2 + (7/5)z2  = %s" % nstr(k2[2] + mpf(7) / 5 * z[2], 8))
print("   kappa_3 - 2 z3     = %s" % nstr(k2[3] - 2 * z[3], 8))
print("   kappa_4 - (1/2)z4  = %s" % nstr(k2[4] - mpf(1) / 2 * z[4], 8))
print("   kappa_5 - (z5-3z2z3) = %s" % nstr(k2[5] - (z[5] - 3 * z[2] * z[3]), 8))
print("   kappa_6            = %s" % nstr(k2[6], 50))
print("   (87/16)z6 + (5/2)z3^2 = %s" % nstr(mpf(87) / 16 * z[6] + mpf(5) / 2 * z[3] ** 2, 50))
print("   (87/16)z6 - (5/2)z3^2 = %s" % nstr(mpf(87) / 16 * z[6] - mpf(5) / 2 * z[3] ** 2, 50))
print("   diff vs (+) form   = %s" % nstr(k2[6] - (mpf(87) / 16 * z[6] + mpf(5) / 2 * z[3] ** 2), 8))
print("   diff vs (-) form   = %s" % nstr(k2[6] - (mpf(87) / 16 * z[6] - mpf(5) / 2 * z[3] ** 2), 8))
if K >= 7:
    print("   kappa_7 - (-55/8 z7 - 5/2 z5z2 - 5/4 z3z4) = %s" %
          nstr(k2[7] - (-mpf(55) / 8 * z[7] - mpf(5) / 2 * z[5] * z[2]
                        - mpf(5) / 4 * z[3] * z[4]), 8))
