"""T2 step 2: the kappa-vector of the Brown-Zudilin order-9 operator at its
nearest conifold z_3 = 1/lambda_3 (lambda_3 = 592.079...)."""
import sys, time, pickle
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma')
from mpmath import mp, mpf, nstr, polyroots, mpmathify
from frobkappa import kappa_series, poly_shift_taylor
from bzop import QS
from fractions import Fraction

mp.dps = int(sys.argv[1]) if len(sys.argv) > 1 else 220
K = int(sys.argv[2]) if len(sys.argv) > 2 else 13
M = int(sys.argv[3]) if len(sys.argv) > 3 else 130
NS = [int(x) for x in (sys.argv[4].split(',') if len(sys.argv) > 4 else ['300', '400'])]

# ---- sanity: exact a_n(0) must be Q_n = 1, 21, 2989, ...
a = [Fraction(1)]
for m in range(1, 8):
    num = Fraction(0)
    for j in range(1, 4):
        if m - j < 0:
            continue
        num -= Fraction(sum(QS[j][i] * (m - j) ** i for i in range(len(QS[j])))) * a[m - j]
    den = Fraction(sum(QS[0][i] * m ** i for i in range(len(QS[0]))))
    a.append(num / den)
print("a_n(0) =", [str(x) for x in a[:5]], " (BZ Q_n: 1, 21, 2989, ...)")

# ---- lambda_3 = largest root of 4L^3 - 2368L^2 - 188L + 1
rts = polyroots([4, -2368, -188, 1], maxsteps=200, extraprec=4 * mp.prec)
rts = sorted([r.real if abs(r.imag) < mpf(10) ** (-mp.dps + 20) else r for r in rts],
             key=lambda r: -abs(r))
lam3, lam2, lam1 = rts[0], rts[1], rts[2]
print("lambda_3 =", nstr(lam3, 30))
print("lambda_2 =", nstr(lam2, 30))
print("lambda_1 =", nstr(lam1, 30))
print("z_3 = 1/lambda_3 =", nstr(1 / lam3, 30))

t0 = time.time()
res, alpha, c, chk = kappa_series(QS, lam3, 0, K, M, NS)
print("\nchar.residual = %s   alpha = %s   [%.1fs]" % (nstr(chk, 5), nstr(alpha, 25),
                                                      time.time() - t0))
kap = res[NS[-1]][0]
kapb = res[NS[-2]][0]
S0 = res[NS[-1]][1]
print("Stokes S(0) = A_Q = %s" % nstr(S0, 60))
print("  (DEFECT_IDENTIFY 150-digit value: 0.06667642572715676784165334063934544446963)")
print("  S(0) self-agreement across n: %s" % nstr(abs(res[NS[-1]][1] - res[NS[-2]][1]) / abs(S0), 5))
print()
for i in range(K + 1):
    d = abs(kap[i] - kapb[i])
    rel = d / (abs(kap[i]) + mpf(10) ** (-mp.dps))
    print("kappa_%-2d = %s   [agree %d digits]" % (
        i, nstr(kap[i], min(mp.dps - 5, 70)),
        int(-mp.log10(rel + mpf(10) ** (-mp.dps)))))

with open('/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma/bz_kappa.pkl', 'wb') as f:
    pickle.dump({'dps': mp.dps, 'K': K, 'M': M, 'NS': NS,
                 'kappa': [mp.nstr(x, mp.dps) for x in kap],
                 'kappa_prev': [mp.nstr(x, mp.dps) for x in kapb],
                 'S0': mp.nstr(S0, mp.dps), 'alpha': mp.nstr(alpha, 30)}, f)
print("\nsaved bz_kappa.pkl")
