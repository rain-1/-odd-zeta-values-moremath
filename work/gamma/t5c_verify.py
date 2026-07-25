"""T5c: verify the two candidate identities for the BZ connection constants."""
import sys, json
from mpmath import mp, mpf, mpmathify, nstr, pslq, pi, sqrt, log, polyroots
import sympy as sp

mp.dps = int(sys.argv[1]) if len(sys.argv) > 1 else 280
res = {k: mpmathify(v) for k, v in
       json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma/conn.json')).items()}
AQ, AI, AIh, AII = res['A_Q'], res["A_I'"], res['A_Ihat'], res['A_I']
print("A_Q     =", nstr(AQ, 40))
print("A_I'    =", nstr(AI, 40))
print("A_Ihat  =", nstr(AIh, 40))
print("A_I     =", nstr(AII, 40))

print("\n=== (1) product identity ===")
P = AQ * AI * AII
tgt = -pi ** (mpf(5) / 2) / (12 * sqrt(37))
print("  A_Q*A_I'*A_I           =", nstr(P, 60))
print("  -pi^(5/2)/(12 sqrt37)  =", nstr(tgt, 60))
print("  relative difference    =", nstr(abs(P - tgt) / abs(P), 8))
print("  (5328 = 2^4*3^2*37, sqrt5328 = 12 sqrt37)")
# also with Ihat instead of I
for nm, v in [("A_Q*A_Ihat*A_I", AQ * AIh * AII), ("A_Q*A_I'*A_Ihat", AQ * AI * AIh),
              ("A_Q*A_Ihat^2", AQ * AIh ** 2), ("A_Q*A_I'^2", AQ * AI ** 2)]:
    r = pslq([log(abs(v)), log(pi), log(2), log(3), log(37), log(557)],
             tol=mpf(10) ** (-240), maxcoeff=10 ** 8, maxsteps=10 ** 6)
    print("  %-18s log-relation vs {pi,2,3,37,557}: %s" % (nm, r))

print("\n=== (2) algebraicity of A * pi^(5/2) ===")
for nm, v in [('A_Q', AQ), ("A_I'", AI), ('A_Ihat', AIh), ('A_I', AII)]:
    w = v * pi ** (mpf(5) / 2)
    print(" --", nm, ": v*pi^(5/2) =", nstr(w, 40))
    for deg in [2, 3, 4, 6, 8]:
        r = pslq([w ** k for k in range(deg + 1)], tol=mpf(10) ** (-240),
                 maxcoeff=10 ** 14, maxsteps=10 ** 6)
        if r is not None:
            print("     deg %d minpoly coeffs (low->high): %s" % (deg, r))
    # and the square
    for deg in [3, 4]:
        r = pslq([(w ** 2) ** k for k in range(deg + 1)], tol=mpf(10) ** (-240),
                 maxcoeff=10 ** 14, maxsteps=10 ** 6)
        if r is not None:
            print("     (v pi^(5/2))^2 deg %d : %s" % (deg, r))

print("\n=== (3) exact check of the candidate cubic for u = 64 (A_Q pi^(5/2))^2 ===")
u = 64 * (AQ * pi ** (mpf(5) / 2)) ** 2
print("  u =", nstr(u, 50))
val = 37 * u ** 3 - 3219 * u ** 2 - 229 * u - 1
print("  37u^3 - 3219u^2 - 229u - 1 =", nstr(val, 10), "  (rel %s)" % nstr(abs(val) / (37 * u ** 3), 8))
x = sp.Symbol('x')
cub = sp.Poly(37 * x ** 3 - 3219 * x ** 2 - 229 * x - 1, x)
print("  candidate cubic disc =", sp.factorint(sp.discriminant(cub.as_expr(), x)))
print("  BZ singular cubic disc =", sp.factorint(sp.discriminant(x ** 3 - 188 * x ** 2 - 2368 * x + 4, x)))
print("  Galois group same field? cubic roots:", [nstr(mpmathify(str(sp.N(r, 40))), 25)
                                                  for r in sp.nroots(cub, n=45)])
zz = sorted(polyroots([1, -188, -2368, 4], maxsteps=400, extraprec=8 * mp.prec), key=lambda t: t.real)
print("  BZ singularities:", [nstr(t, 25) for t in zz])
print("  is Q(u) = Q(z)?  test u in Q(z3):",
      pslq([u, mp.mpf(1), 1 / mpf(str(sp.N(sp.nroots(sp.Poly(x ** 3 - 188 * x ** 2 - 2368 * x + 4, x), n=300)[1], 300)))],
           tol=mpf(10) ** (-100), maxcoeff=10 ** 10) if False else "see below")
lam3 = 1 / zz[1].real if abs(zz[1].real) < 1 else None
print("  u vs Q(1/z_near) basis {1, L, L^2}, L=lambda_3:",
      pslq([u, mp.mpf(1), 592.0793805346115628484048, 592.0793805346115628484048 ** 2],
           tol=mpf(10) ** (-30), maxcoeff=10 ** 12))
