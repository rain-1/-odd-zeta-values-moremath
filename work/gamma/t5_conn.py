"""T5: BZ connection constants on all three rays to ~250 digits (Birkhoff/Stokes
method, independent of the prior Neville extrapolation), then Gamma-value PSLQ."""
import sys, json, time
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma')
from mpmath import mp, mpf, mpmathify, nstr, pslq, zeta, pi, log, sqrt, polyroots, gamma
from frobkappa import birkhoff
from bzop import QS, A as Aexpr, B as Bexpr, C as Cexpr, D as Dexpr
from fractions import Fraction
import sympy as sp

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 520
DPS_HI = int(sys.argv[2]) if len(sys.argv) > 2 else 3200
DPS = int(sys.argv[3]) if len(sys.argv) > 3 else 400
M = int(sys.argv[4]) if len(sys.argv) > 4 else 200
SAMPLES = [NMAX - 100, NMAX - 50, NMAX]

n = sp.Symbol('n')
Ap = sp.Poly(sp.expand(Aexpr), n).all_coeffs()[::-1]
Bp = sp.Poly(sp.expand(Bexpr), n).all_coeffs()[::-1]
Cp = sp.Poly(sp.expand(Cexpr), n).all_coeffs()[::-1]
Dp = sp.Poly(sp.expand(Dexpr), n).all_coeffs()[::-1]
def ev(p, k):
    s = Fraction(0)
    for c in reversed(p):
        s = s * k + int(c)
    return s

# ---- exact ladders
seeds = {'Q': [Fraction(1), Fraction(21), Fraction(2989)],
         'P': [Fraction(0), Fraction(87, 4), Fraction(1190161, 384)],
         'Ph': [Fraction(0), Fraction(101, 4), Fraction(344923, 96)]}
lad = {k: list(v) for k, v in seeds.items()}
t0 = time.time()
for k in lad:
    u = lad[k]
    for m in range(2, NMAX):
        nxt = -(ev(Bp, m) * u[m] + ev(Cp, m) * u[m - 1] + ev(Dp, m) * u[m - 2]) / ev(Ap, m)
        u.append(nxt)
print("ladders to n=%d in %.1fs; Q_3=%s" % (NMAX, time.time() - t0, lad['Q'][3]))
assert lad['Q'][3] == 714549

# ---- high-precision cancellation
mp.dps = DPS_HI
z3v, z5v, z2v = zeta(3), zeta(5), zeta(2)
def tompf(fr):
    return mp.mpf(fr.numerator) / mp.mpf(fr.denominator)
vals = {}
for m in SAMPLES:
    Q = tompf(lad['Q'][m]); P = tompf(lad['P'][m]); Ph = tompf(lad['Ph'][m])
    Ip = Q * z5v - P
    Ih = Q * z3v - Ph
    Iv = 2 * Ip + 4 * z2v * Ih
    vals[m] = {'Q': Q, 'Ip': Ip, 'Ih': Ih, 'I': Iv}
    print("n=%d: log10|I'|=%s log10|I|=%s (rel prec left ~%d digits)"
          % (m, nstr(mp.log10(abs(Ip)), 8), nstr(mp.log10(abs(Iv)), 8),
             DPS_HI - int(mp.log10(abs(Q / Iv)))))

# ---- Birkhoff at each root, Stokes constants
mp.dps = DPS
rts = sorted(polyroots([4, -2368, -188, 1], maxsteps=600, extraprec=10 * mp.prec),
             key=lambda t: -abs(t))
L3, L2, L1 = [t.real for t in rts]
print("\nlambda_3=%s  lambda_2=%s  lambda_1=%s" % (nstr(L3, 25), nstr(L2, 25), nstr(L1, 25)))
print("purity gap  log|lambda_2/lambda_1| = %s" % nstr(log(abs(L2 / L1)), 30))
print("rate(min) = %s   rate(mid) = %s" % (nstr(-log(abs(L1)), 25), nstr(-log(abs(L2)), 25)))

def stokes(lam, seq_key, samples):
    alpha, c, chk = birkhoff(QS, lam, M)
    out = {}
    for m in samples:
        v = mpmathify(mp.nstr(vals[m][seq_key], DPS - 20))
        F = mp.mpf(0)
        u = mp.mpf(1) / mp.mpf(m)
        p = mp.mpf(1)
        for k in range(M + 1):
            F += c[k] * p
            p *= u
        out[m] = v / (lam ** m * mp.mpf(m) ** alpha * F)
    return alpha, out

res = {}
for lam, key, nm in [(L3, 'Q', 'A_Q'), (L2, 'Ip', "A_I'"), (L2, 'Ih', 'A_Ihat'), (L1, 'I', 'A_I')]:
    al, o = stokes(lam, key, SAMPLES)
    v = o[SAMPLES[-1]]
    dg = int(-mp.log10(abs(o[SAMPLES[-1]] - o[SAMPLES[-2]]) / abs(v) + mpf(10) ** (-DPS)))
    res[nm] = v
    print("%-8s alpha=%s  = %s   [agree %d digits across n]" % (nm, nstr(al, 6), nstr(v, 60), dg))

print("\nratio A_Ihat/A_I' = %s" % nstr(res['A_Ihat'] / res["A_I'"], 50))
print("   -3/pi^2         = %s" % nstr(-3 / pi ** 2, 50))
print("   difference      = %s" % nstr(res['A_Ihat'] / res["A_I'"] + 3 / pi ** 2, 8))

# ---------------------------------------------------------------- T5 PSLQ
print("\n================ T5: Gamma-value identification ================")
LOGS = [('logpi', log(pi)), ('log2', log(2)), ('log3', log(3)),
        ('log37', log(37)), ('log557', log(557)),
        ('log|z1|', log(abs(1 / L1))), ('log|z2|', log(abs(1 / L2))), ('log|z3|', log(1 / L3))]

def gam_logs(ss):
    out = []
    for s in ss:
        for k in range(1, s):
            from math import gcd
            if gcd(k, s) == 1 and 2 * k < s:
                out.append(('lnG(%d/%d)' % (k, s), log(gamma(mp.mpf(k) / s))))
    return out

def test(label, vec, names, tol, maxc):
    r = pslq(vec, tol=mpf(10) ** (-tol), maxcoeff=maxc, maxsteps=4 * 10 ** 6)
    if r is None:
        print("  %-46s : NONE (dim=%d, tol 1e-%d, |c|<=%.0e)" % (label, len(vec), tol, maxc))
        return None
    print("  %-46s : %s" % (label, " ".join("%+d*%s" % (r[i], names[i])
                                            for i in range(len(names)) if r[i] != 0)))
    return r

TOL = 170
print("\n-- finder validation (must FIND these) --")
g13, g23 = log(gamma(mpf(1) / 3)), log(gamma(mpf(2) / 3))
test("Gamma(1/3)Gamma(2/3)=2pi/sqrt3", [g13, g23, log(pi), log(2), log(3)],
     ['lnG13', 'lnG23', 'logpi', 'log2', 'log3'], TOL, 10 ** 6)
g14, g34 = log(gamma(mpf(1) / 4)), log(gamma(mpf(3) / 4))
test("Gamma(1/4)Gamma(3/4)=pi*sqrt2", [g14, g34, log(pi), log(2)],
     ['lnG14', 'lnG34', 'logpi', 'log2'], TOL, 10 ** 6)
g16 = log(gamma(mpf(1) / 6))
test("Gamma(1/6) duplication", [g16, g13, log(pi), log(2), log(3)],
     ['lnG16', 'lnG13', 'logpi', 'log2', 'log3'], TOL, 10 ** 6)

print("\n-- the BZ constants --")
for nm in ['A_Q', "A_I'", 'A_Ihat', 'A_I']:
    v = res[nm]
    lv = log(abs(v))
    test("log|%s| in span(logs)" % nm, [lv] + [x[1] for x in LOGS],
         ['log|%s|' % nm] + [x[0] for x in LOGS], TOL, 10 ** 8)
for S in [[3], [4], [3, 4], [5], [6], [8], [12], [3, 4, 6], [24]]:
    gl = gam_logs(S)
    if not gl:
        continue
    names = ['log|A_Q|'] + [x[0] for x in gl] + [x[0] for x in LOGS]
    vec = [log(abs(res['A_Q']))] + [x[1] for x in gl] + [x[1] for x in LOGS]
    test("log|A_Q| + Gamma(k/%s)" % S, vec, names, TOL, 10 ** 6)

print("\n-- ratios --")
for a, b in [("A_I'", 'A_Q'), ('A_I', 'A_Q'), ('A_I', "A_I'")]:
    v = res[a] / res[b]
    test("log|%s/%s| in span(logs)" % (a, b), [log(abs(v))] + [x[1] for x in LOGS],
         ['log ratio'] + [x[0] for x in LOGS], TOL, 10 ** 8)
prod = res['A_Q'] * res["A_I'"] * res['A_I']
test("log|A_Q*A_I'*A_I| in span(logs)", [log(abs(prod))] + [x[1] for x in LOGS],
     ['logprod'] + [x[0] for x in LOGS], TOL, 10 ** 8)

json.dump({k: mp.nstr(v, 260) for k, v in res.items()},
          open('/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma/conn.json', 'w'), indent=1)
print("\nsaved conn.json")
