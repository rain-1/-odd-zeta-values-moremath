"""T3: identify the BZ kappa's against graded MZV bases (incl. reciprocal
periods pi^{-2k}) and against the Apery operators' kappa's."""
import sys, time
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma')
from mpmath import mp, mpf, nstr, pslq, zeta, pi, log, sqrt, polyroots, mpmathify, identify
from frobkappa import kappa_series
from bzop import QS

DPS = int(sys.argv[1]) if len(sys.argv) > 1 else 220
K = int(sys.argv[2]) if len(sys.argv) > 2 else 13
M = int(sys.argv[3]) if len(sys.argv) > 3 else 130
NS = [int(x) for x in (sys.argv[4].split(',') if len(sys.argv) > 4 else ['300', '400'])]
mp.dps = DPS

rts = sorted(polyroots([4, -2368, -188, 1], maxsteps=300, extraprec=6 * mp.prec),
             key=lambda r: -abs(r))
lam3 = rts[0].real
resB, alB, cB, _ = kappa_series(QS, lam3, 0, K, M, NS)
kB = resB[NS[-1]][0]
kBp = resB[NS[-2]][0]

q3 = [[0, 0, 0, 1], [-5, -27, -51, -34], [1, 3, 3, 1]]
resA, alA, cA, _ = kappa_series(q3, 17 + 12 * sqrt(2), 0, K, M, NS)
kA = resA[NS[-1]][0]
q2 = [[0, 0, 1], [-3, -11, -11], [-1, -2, -1]]
resD, alD, cD, _ = kappa_series(q2, (11 + 5 * sqrt(5)) / 2, 0, K, M, NS)
kD = resD[NS[-1]][0]

# trustworthy digits
TRUST = min(int(-mp.log10(abs(kB[i] - kBp[i]) / abs(kB[i]) + mpf(10) ** (-mp.dps)))
            for i in range(2, K + 1))
print("BZ kappa trusted to ~%d digits (n=%d vs %d)" % (TRUST, NS[-2], NS[-1]))
WORK = TRUST - 15
mp.dps = DPS  # keep

z = {k: zeta(k) for k in range(2, K + 4)}
L3 = log(1 / lam3)          # log(c), c = z_3
LG = {'log(c)': L3, 'log2': log(2), 'log37': log(37), 'log557': log(557)}

def show(name, vec, basis_names, tol_digits, maxcoeff=10**14, maxsteps=10**6):
    r = pslq(vec, tol=mpf(10) ** (-tol_digits), maxcoeff=maxcoeff, maxsteps=maxsteps)
    print("   %-58s -> %s" % (name, r))
    return r

print("\n=== BZ kappa values ===")
for i in range(K + 1):
    print("  kappa_%-2d = %s" % (i, nstr(kB[i], 45)))

print("\n=== weight-graded identification, tol = %d digits ===" % WORK)
# weight 2
print(" kappa_2:")
show("[k2, z2]", [kB[2], z[2]], None, WORK)
print("   kappa_2 + 4*zeta(2) =", nstr(kB[2] + 4 * z[2], 10))
# weight 3
print(" kappa_3:")
show("[k3, z3]", [kB[3], z[3]], None, WORK)
show("[k3, z3, z2*Lc, Lc^3]", [kB[3], z[3], z[2] * L3, L3 ** 3], None, WORK)
show("[k3, z3, z2*Lc, Lc^3, Lc*z2... ]", [kB[3], z[3], z[2] * L3, L3 ** 3, L3], None, WORK)
print("   kappa_3/zeta(3) =", nstr(kB[3] / z[3], 40))
# weight 4
print(" kappa_4:")
show("[k4, z4]", [kB[4], z[4]], None, WORK)
show("[k4, z4, z3*Lc, z2*Lc^2, Lc^4]", [kB[4], z[4], z[3] * L3, z[2] * L3 ** 2, L3 ** 4], None, WORK)
print("   kappa_4/zeta(4) =", nstr(kB[4] / z[4], 40))
print("   kappa_4/zeta(2)^2 =", nstr(kB[4] / z[2] ** 2, 40))
# weight 5 -- THE TARGET
print(" kappa_5  (the first HIGHER Frobenius constant, m(rho)=5):")
show("[k5, z5, z2z3]", [kB[5], z[5], z[2] * z[3]], None, WORK)
show("[k5, z5, z2z3, z4*Lc, z3*Lc^2, z2*Lc^3, Lc^5]",
     [kB[5], z[5], z[2] * z[3], z[4] * L3, z[3] * L3 ** 2, z[2] * L3 ** 3, L3 ** 5], None, WORK)
print("   kappa_5/zeta(5) =", nstr(kB[5] / z[5], 40))
# weight 6,7
print(" kappa_6:")
show("[k6, z6, z3^2]", [kB[6], z[6], z[3] ** 2], None, WORK)
print(" kappa_7:")
show("[k7, z7, z2z5, z3z4]", [kB[7], z[7], z[2] * z[5], z[3] * z[4]], None, WORK)
print(" kappa_8:")
show("[k8, z8, z3z5, z2z3^2]", [kB[8], z[8], z[3] * z[5], z[2] * z[3] ** 2], None, WORK)

print("\n=== reciprocal-period tests (the DEFECT lesson) ===")
for i in range(2, min(K, 8) + 1):
    v = [kB[i]] + [pi ** (-2 * k) for k in range(0, 5)]
    show("k%d in span{pi^{-2k}, k=0..4}" % i, v, None, WORK, maxcoeff=10 ** 10)

print("\n=== against Apery kappa's ===")
for i in range(2, K + 1):
    show("[kB_%d, kA_%d]" % (i, i), [kB[i], kA[i]], None, WORK)
for i in range(2, K + 1):
    show("[kB_%d, kA_%d, kD_%d]" % (i, i, i), [kB[i], kA[i], kD[i]], None, WORK)
