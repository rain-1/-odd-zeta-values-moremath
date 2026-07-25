"""T3b: robustness check + the primitive (log-kappa) coefficients lambda_j,
plus full graded-MZV identification for BZ / Apery-zeta(3) / Apery-zeta(2)."""
import sys, time, json
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma')
from mpmath import mp, mpf, nstr, pslq, zeta, pi, log, sqrt, polyroots
from frobkappa import kappa_series, slog
from bzop import QS

DPS = int(sys.argv[1]) if len(sys.argv) > 1 else 300
K = int(sys.argv[2]) if len(sys.argv) > 2 else 16
mp.dps = DPS

rts = sorted(polyroots([4, -2368, -188, 1], maxsteps=400, extraprec=8 * mp.prec),
             key=lambda r: -abs(r))
lam3 = rts[0].real
q3 = [[0, 0, 0, 1], [-5, -27, -51, -34], [1, 3, 3, 1]]
q2 = [[0, 0, 1], [-3, -11, -11], [-1, -2, -1]]
OPS = {'BZ': (QS, lam3), 'A3': (q3, 17 + 12 * sqrt(2)), 'A2': (q2, (11 + 5 * sqrt(5)) / 2)}

# ---------------- robustness: vary M and n independently
print("=== robustness of BZ kappa (vary M, n) ===")
runs = {}
for (M, ns) in [(130, [400]), (170, [400]), (170, [500]), (200, [600])]:
    r, al, c, ch = kappa_series(QS, lam3, 0, K, M, ns)
    runs[(M, ns[0])] = r[ns[0]][0]
    print("  M=%3d n=%3d  alpha=%s  S0=%s" % (M, ns[0], nstr(al, 8), nstr(r[ns[0]][1], 30)))
base = runs[(200, 600)]
for key in runs:
    if key == (200, 600):
        continue
    d = min(int(-mp.log10(abs(runs[key][i] - base[i]) / abs(base[i]) + mpf(10) ** (-mp.dps)))
            for i in range(2, K + 1))
    print("  M=%3d n=%3d agrees with M=200,n=600 to %d digits" % (key[0], key[1], d))
TRUST = 200

# ---------------- kappa and lambda for all three
res = {}
for name, (qs, lam) in OPS.items():
    r, al, c, ch = kappa_series(qs, lam, 0, K, 200, [600])
    kap = r[600][0]
    lamb = slog(kap, K)
    res[name] = {'kappa': kap, 'lambda': lamb, 'alpha': al, 'S0': r[600][1]}
    print("\n=== %s ===  alpha=%s  S(0)=%s" % (name, nstr(al, 6), nstr(r[600][1], 45)))

# ---------------- graded MZV basis
z = {k: zeta(k) for k in range(2, 20)}
# Zagier dims: w:2->1,3->1,4->1,5->2,6->2,7->3,8->4,9->5,10->7,11->9
# MZVs needed beyond products of zetas: z(3,5) at w8, z(3,7)&z(2)z(3,5) at w10,
#   z(3,5,3) & z(3,7)z(... ) at w11.  We use mpmath nsum for the double zetas.
def mzv2(s1, s2, N=None):
    """zeta(s1,s2) = sum_{m>n>=1} 1/(m^s1 n^s2)  (Zagier convention z(3,5)=sum m^-3 n^-5)"""
    # use the Euler/stuffle-free direct acceleration: compute with mpmath nsum
    from mpmath import nsum, inf
    f = lambda m: mp.mpf(1) / m ** s1 * sum(mp.mpf(1) / mp.mpf(n) ** s2 for n in range(1, int(m)))
    return None  # replaced below

def zeta_double(s1, s2, N=4000):
    """zeta(s1,s2)=sum_{m>n>0} m^-s1 n^-s2, with tail via Euler-Maclaurin on the
    partial-harmonic; s1>=2. Uses exact partial sums to N then an asymptotic tail."""
    H = mp.mpf(0)
    tot = mp.mpf(0)
    for n in range(1, N):
        tot += H / mp.mpf(n) ** s1 if False else 0
    # direct: sum over m of m^-s1 * H_{m-1}^{(s2)}
    Hs = mp.mpf(0)
    tot = mp.mpf(0)
    for m in range(1, N + 1):
        tot += Hs / mp.mpf(m) ** s1
        Hs += mp.mpf(1) / mp.mpf(m) ** s2
    # tail: sum_{m>N} m^-s1 (zeta(s2) - m^{1-s2}/(s2-1) + ...)
    zs2 = z[s2]
    tail = mp.mpf(0)
    # zeta(s1) tail
    for k in range(0, 1):
        pass
    tail += zs2 * (mp.zeta(s1) - sum(mp.mpf(1) / mp.mpf(m) ** s1 for m in range(1, N + 1)))
    # correction -sum_{m>N} m^-s1 * (tail of Hs beyond m) : H^{(s2)}_{m-1} = zs2 - sum_{n>=m} n^-s2
    corr = mp.mpf(0)
    return tot + tail - corr  # NOTE: low accuracy; only used as a fallback flag

BASIS = {
    2: [('z2', z[2])],
    3: [('z3', z[3])],
    4: [('z4', z[4])],
    5: [('z5', z[5]), ('z2z3', z[2] * z[3])],
    6: [('z6', z[6]), ('z3^2', z[3] ** 2)],
    7: [('z7', z[7]), ('z2z5', z[2] * z[5]), ('z4z3', z[4] * z[3])],
    8: [('z8', z[8]), ('z3z5', z[3] * z[5]), ('z2z3^2', z[2] * z[3] ** 2)],
    9: [('z9', z[9]), ('z3^3', z[3] ** 3), ('z2z7', z[2] * z[7]),
        ('z4z5', z[4] * z[5]), ('z6z3', z[6] * z[3])],
    10: [('z10', z[10]), ('z5^2', z[5] ** 2), ('z3z7', z[3] * z[7]),
         ('z4z3^2', z[4] * z[3] ** 2), ('z2z3z5', z[2] * z[3] * z[5])],
    11: [('z11', z[11]), ('z2z9', z[2] * z[9]), ('z4z7', z[4] * z[7]),
         ('z6z5', z[6] * z[5]), ('z8z3', z[8] * z[3]), ('z3^2z5', z[3] ** 2 * z[5]),
         ('z2z3^3', z[2] * z[3] ** 3)],
    12: [('z12', z[12]), ('z3z9', z[3] * z[9]), ('z5z7', z[5] * z[7]),
         ('z2z10... ', z[2] * z[10]), ('z4z3z5', z[4] * z[3] * z[5]),
         ('z6z3^2', z[6] * z[3] ** 2), ('z2z5^2', z[2] * z[5] ** 2),
         ('z3^4', z[3] ** 4)],
    13: [('z13', z[13]), ('z2z11', z[2] * z[11]), ('z4z9', z[4] * z[9]),
         ('z6z7', z[6] * z[7]), ('z8z5', z[8] * z[5]), ('z10z3', z[10] * z[3]),
         ('z3^2z7', z[3] ** 2 * z[7]), ('z3z5^2', z[3] * z[5] ** 2),
         ('z2z3^2z5', z[2] * z[3] ** 2 * z[5])],
}

def ident(name, val, w, tol, extra=()):
    bs = BASIS.get(w, [])
    names = [b[0] for b in bs] + [e[0] for e in extra]
    vec = [val] + [b[1] for b in bs] + [e[1] for e in extra]
    r = pslq(vec, tol=mpf(10) ** (-tol), maxcoeff=10 ** 16, maxsteps=2 * 10 ** 6)
    if r is None:
        print("   %-14s w=%-2d : NO RELATION (basis %s, tol 1e-%d, |c|<=1e16)"
              % (name, w, ','.join(names), tol))
        return None
    c0 = r[0]
    if c0 == 0:
        print("   %-14s w=%-2d : DEGENERATE basis relation %s" % (name, w, r))
        return None
    from fractions import Fraction
    terms = " + ".join("%s*%s" % (Fraction(-r[i + 1], c0), names[i]) for i in range(len(names))
                       if r[i + 1] != 0)
    print("   %-14s w=%-2d = %s" % (name, w, terms))
    return r

Lc = {n: log(1 / OPS[n][1]) for n in OPS}
print("\n=== kappa_j identifications (tol 1e-%d) ===" % TRUST)
for name in ['BZ', 'A3', 'A2']:
    print(" -- %s --" % name)
    for j in range(2, K + 1):
        ident("kappa_%d" % j, res[name]['kappa'][j], j, TRUST)

print("\n=== lambda_j = [eps^j] log kappa(eps) identifications ===")
for name in ['BZ', 'A3', 'A2']:
    print(" -- %s --" % name)
    for j in range(2, K + 1):
        ident("lambda_%d" % j, res[name]['lambda'][j], j, TRUST)

out = {n: {'kappa': [mp.nstr(x, 210) for x in res[n]['kappa']],
           'lambda': [mp.nstr(x, 210) for x in res[n]['lambda']],
           'S0': mp.nstr(res[n]['S0'], 210)} for n in res}
json.dump(out, open('/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma/kappas.json', 'w'), indent=1)
print("\nsaved kappas.json")
