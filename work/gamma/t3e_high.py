"""T3e: ~450-digit kappa/lambda for BZ, Apery-zeta(3), Apery-zeta(2); then
identification at tol 1e-380 with hygienic bases and explicit residual checks."""
import sys, json, time
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma')
from mpmath import mp, mpf, nstr, pslq, zeta, pi, log, sqrt, polyroots
from frobkappa import kappa_series, slog
from bzop import QS
from fractions import Fraction

DPS = int(sys.argv[1]) if len(sys.argv) > 1 else 520
K = int(sys.argv[2]) if len(sys.argv) > 2 else 16
M = int(sys.argv[3]) if len(sys.argv) > 3 else 260
NN = int(sys.argv[4]) if len(sys.argv) > 4 else 800
TOL = int(sys.argv[5]) if len(sys.argv) > 5 else 380
mp.dps = DPS

rts = sorted(polyroots([4, -2368, -188, 1], maxsteps=600, extraprec=10 * mp.prec),
             key=lambda r: -abs(r))
lam3 = rts[0].real
q3 = [[0, 0, 0, 1], [-5, -27, -51, -34], [1, 3, 3, 1]]
q2 = [[0, 0, 1], [-3, -11, -11], [-1, -2, -1]]
OPS = {'BZ': (QS, lam3), 'A3': (q3, 17 + 12 * sqrt(2)), 'A2': (q2, (11 + 5 * sqrt(5)) / 2)}
res = {}
for name, (qs, lam) in OPS.items():
    t0 = time.time()
    r, al, c, ch = kappa_series(qs, lam, 0, K, M, [NN - 100, NN])
    kap, kapb = r[NN][0], r[NN - 100][0]
    dg = min(int(-mp.log10(abs(kap[i] - kapb[i]) / abs(kap[i]) + mpf(10) ** (-DPS)))
             for i in range(2, K + 1))
    res[name] = {'kappa': kap, 'lambda': slog(kap, K), 'S0': r[NN][1], 'alpha': al}
    print("%s: alpha=%s  S0=%s  self-agree %d digits  [%.0fs]"
          % (name, nstr(al, 6), nstr(r[NN][1], 50), dg, time.time() - t0))

z2 = zeta(2)
def zprod_basis(w):
    out = []
    def rec(rem, minodd, name, val):
        if rem % 2 == 0 and rem >= 0:
            out.append((name + ('z2^%d' % (rem // 2) if rem > 0 else '1'), val * z2 ** (rem // 2)))
        o = minodd
        while o <= rem:
            rec(rem - o, o, name + 'z%d.' % o, val * zeta(o))
            o += 2
    rec(w, 3, '', mp.mpf(1))
    return out

def allw(w):
    out, seen = [], set()
    for ww in list(range(2, w + 1)):
        for nm, v in zprod_basis(ww):
            if nm not in seen:
                seen.add(nm); out.append((nm, v))
    out = [('1', mp.mpf(1))] + [x for x in out if x[0] != '1']
    return out

def tryid(label, val, bs, tol=TOL, maxc=10 ** 14):
    names = [b[0] for b in bs]
    if len(bs) >= 2:
        intern = pslq([b[1] for b in bs], tol=mpf(10) ** (-tol), maxcoeff=maxc, maxsteps=10 ** 6)
        if intern is not None:
            print("   %-14s : BASIS DEGENERATE" % label); return None
    rr = pslq([val] + [b[1] for b in bs], tol=mpf(10) ** (-tol), maxcoeff=maxc, maxsteps=4 * 10 ** 6)
    if rr is None or rr[0] == 0:
        print("   %-14s : NONE  (dim=%d, tol 1e-%d, |c|<=%.0e)" % (label, len(bs), tol, maxc))
        return None
    c0 = rr[0]
    resid = sum(mpf(rr[i]) * ([val] + [b[1] for b in bs])[i] for i in range(len(rr)))
    terms = " ".join("%+s*%s" % (Fraction(-rr[i + 1], c0), names[i])
                     for i in range(len(names)) if rr[i + 1] != 0)
    print("   %-14s = %s      [resid 1e%d, maxcoef %.1e]"
          % (label, terms, int(mp.log10(abs(resid) + mpf(10) ** (-DPS))), max(abs(x) for x in rr)))
    return rr

print("\n=== BZ: graded test (weight-j basis only) ===")
for j in range(2, K + 1):
    tryid("kappa_%d" % j, res['BZ']['kappa'][j], zprod_basis(j))
print("\n=== BZ: inhomogeneous test (all weights <= j) ===")
for j in range(2, min(K, 10) + 1):
    tryid("kappa_%d" % j, res['BZ']['kappa'][j], allw(j))
for j in range(2, min(K, 10) + 1):
    tryid("lambda_%d" % j, res['BZ']['lambda'][j], allw(j))

print("\n=== A3 / A2 control: same inhomogeneous test (should stay graded) ===")
for nm in ['A3', 'A2']:
    for j in range(2, min(K, 8) + 1):
        tryid("%s kappa_%d" % (nm, j), res[nm]['kappa'][j], allw(j))

json.dump({n: {'kappa': [mp.nstr(x, 420) for x in res[n]['kappa']],
               'lambda': [mp.nstr(x, 420) for x in res[n]['lambda']],
               'S0': mp.nstr(res[n]['S0'], 420)} for n in res},
          open('/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma/kappas_hi.json', 'w'), indent=1)
print("\nsaved kappas_hi.json")
