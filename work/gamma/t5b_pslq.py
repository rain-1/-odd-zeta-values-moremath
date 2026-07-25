"""T5b: Gamma-value PSLQ for the BZ connection constants, with a HYGIENIC log
basis (the trap: log|z1|+log|z2|+log|z3| = log 4 exactly, since the singular
cubic is z^3-188z^2-2368z+4, product of roots = -4)."""
import sys, json
from math import gcd
from mpmath import mp, mpf, mpmathify, nstr, pslq, zeta, pi, log, sqrt, gamma, polyroots

mp.dps = int(sys.argv[1]) if len(sys.argv) > 1 else 300
TOL = int(sys.argv[2]) if len(sys.argv) > 2 else 240
res = {k: mpmathify(v) for k, v in
       json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma/conn.json')).items()}
rts = sorted(polyroots([4, -2368, -188, 1], maxsteps=600, extraprec=10 * mp.prec),
             key=lambda t: -abs(t))
L3, L2, L1 = [t.real for t in rts]
z1, z2, z3 = 1 / L1, 1 / L2, 1 / L3        # the three finite singularities
print("check z1*z2*z3 = %s (should be -4)" % nstr(z1 * z2 * z3, 20))

# hygienic: drop log|z3|, keep log2 (they are dependent)
BASE = [('logpi', log(pi)), ('log2', log(2)), ('log3', log(3)),
        ('log37', log(37)), ('log557', log(557)),
        ('log|z1|', log(abs(z1))), ('log|z2|', log(abs(z2)))]

def gam_logs(ss):
    out = []
    for s in ss:
        for k in range(1, s):
            if gcd(k, s) == 1 and 2 * k < s:
                out.append(('lnG(%d/%d)' % (k, s), log(gamma(mp.mpf(k) / s))))
    return out

def test(label, vec, names, tol=TOL, maxc=10 ** 8, require_target=True):
    intern = pslq(vec[1:], tol=mpf(10) ** (-tol), maxcoeff=maxc, maxsteps=10 ** 6)
    if intern is not None:
        print("  %-44s : BASIS DEGENERATE %s" % (label, [c for c in intern]))
        return None
    r = pslq(vec, tol=mpf(10) ** (-tol), maxcoeff=maxc, maxsteps=4 * 10 ** 6)
    if r is None:
        print("  %-44s : NONE (dim=%d, tol 1e-%d, |c|<=%.0e)" % (label, len(vec), tol, maxc))
        return None
    if require_target and r[0] == 0:
        print("  %-44s : SPURIOUS (zero coefficient on target)" % label)
        return None
    print("  %-44s : %s" % (label, " ".join("%+d*%s" % (r[i], names[i])
                                            for i in range(len(names)) if r[i] != 0)))
    return r

print("\n-- finder validation (must FIND) --")
test("G(1/3)G(2/3) = 2pi/sqrt3",
     [log(gamma(mpf(1) / 3)), log(gamma(mpf(2) / 3)), log(pi), log(2), log(3)],
     ['lnG13', 'lnG23', 'logpi', 'log2', 'log3'], require_target=False)
test("G(1/3) duplication -> G(1/6)",
     [log(gamma(mpf(1) / 6)), log(gamma(mpf(1) / 3)), log(pi), log(2), log(3)],
     ['lnG16', 'lnG13', 'logpi', 'log2', 'log3'], require_target=False)
# CONTROL: the Apery zeta(3) Stokes constant IS a closed form -- the finder must get it
SA = (1 + sqrt(2)) ** 2 / (mpf(2) ** (mpf(9) / 4) * pi ** (mpf(3) / 2))
test("Apery-zeta(3) S(0) = (1+r2)^2/(2^(9/4)pi^(3/2))",
     [log(SA), log(1 + sqrt(2)), log(2), log(pi)],
     ['logS0', 'log(1+r2)', 'log2', 'logpi'])

print("\n-- BZ connection constants, log-linear over {pi,2,3,37,557,z1,z2} --")
for nm in ['A_Q', "A_I'", 'A_Ihat', 'A_I']:
    test("log|%s|" % nm, [log(abs(res[nm]))] + [x[1] for x in BASE],
         ['log|%s|' % nm] + [x[0] for x in BASE], maxc=10 ** 10)

print("\n-- adjoining Gamma(k/s) --")
for S in [[3], [4], [6], [5], [8], [12], [24], [3, 4], [3, 4, 6], [3, 4, 6, 8, 12]]:
    gl = gam_logs(S)
    if not gl:
        continue
    names = ['log|A_Q|'] + [x[0] for x in gl] + [x[0] for x in BASE]
    vec = [log(abs(res['A_Q']))] + [x[1] for x in gl] + [x[1] for x in BASE]
    test("log|A_Q| + G(k/%s)" % S, vec, names, maxc=10 ** 6)

print("\n-- ratios and products --")
tests = {"A_I'/A_Q": res["A_I'"] / res['A_Q'], 'A_I/A_Q': res['A_I'] / res['A_Q'],
         "A_I/A_I'": res['A_I'] / res["A_I'"],
         "A_Q*A_I'*A_I": res['A_Q'] * res["A_I'"] * res['A_I'],
         "A_Q^2": res['A_Q'] ** 2, "A_Q*A_I": res['A_Q'] * res['A_I']}
for nm, v in tests.items():
    test("log|%s|" % nm, [log(abs(v))] + [x[1] for x in BASE],
         ['log|%s|' % nm] + [x[0] for x in BASE], maxc=10 ** 10)

print("\n-- algebraicity of A_Q * pi^e (degree <= 8) --")
for e in ['0', '1/2', '1', '3/2', '2', '5/2', '3', '-3/2', '-1/2']:
    from fractions import Fraction as F
    ee = F(e)
    v = res['A_Q'] * pi ** (mpf(ee.numerator) / ee.denominator)
    for deg in [3, 6, 8]:
        r = pslq([v ** k for k in range(deg + 1)], tol=mpf(10) ** (-TOL),
                 maxcoeff=10 ** 12, maxsteps=10 ** 6)
        if r is not None:
            print("  A_Q*pi^%s algebraic deg %d : %s" % (e, deg, r))
    else:
        pass
print("  (no output above = A_Q*pi^e not algebraic of degree<=8, |c|<=1e12, tol 1e-%d)" % TOL)

print("\n-- is A_Q in the cubic field times pi^e ? --")
for e in ['-3/2', '-1/2', '0', '1/2', '3/2']:
    from fractions import Fraction as F
    ee = F(e)
    v = res['A_Q'] * pi ** (mpf(ee.numerator) / ee.denominator)
    r = pslq([v, mp.mpf(1), z3, z3 ** 2], tol=mpf(10) ** (-TOL), maxcoeff=10 ** 20,
             maxsteps=10 ** 6)
    print("  A_Q*pi^%-5s in Q(z3): %s" % (e, r))
