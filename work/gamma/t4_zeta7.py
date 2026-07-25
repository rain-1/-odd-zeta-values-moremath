"""T4: the zeta(7) family (Rivoal/Zudilin, order-4 deg-19 recurrence from the
prior campaign) as an independent test of the rate-purity conservation law.

  q_j(x) = c_{4-j}(x + j - 4)   for  sum_k c_k(n) u_{n+k} = 0.
  Indicial polynomial I(s) = q_0(s) = c_4(s-4).  Test: does s=0 have multiplicity 7?
"""
import sys, json, time
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma')
import sympy as sp
from mpmath import mp, mpf, nstr, pslq, zeta, polyroots, sqrt, log
from frobkappa import kappa_series, slog
from fractions import Fraction

J = json.load(open('/home/ubuntu/fable-episode-2/zeta-math/worthiness/zeta7_q_recurrence.json'))
C = J['Cpoly']
print("order=%s deg=%s certified=%s char_lead=%s" % (J['order'], J['deg'], J.get('certified'),
                                                     J.get('char_lead')))
x = sp.Symbol('x')
def shiftpoly(coeffs, d):
    p = sum(sp.Integer(c) * x ** i for i, c in enumerate(coeffs))
    return sp.Poly(sp.expand(p.subs(x, x + d)), x)

QS7 = []
for j in range(5):
    p = shiftpoly(C[4 - j], j - 4)
    QS7.append([int(p.coeff_monomial(x ** i)) for i in range(p.degree() + 1)])

I = sp.Poly(sum(sp.Integer(c) * x ** i for i, c in enumerate(QS7[0])), x)
print("\nIndicial polynomial I(s) = q_0(s) = c_4(s-4):")
fac = sp.factor(I.as_expr())
print("  factored:", fac)
mult0 = 0
e = I.as_expr()
while sp.simplify(sp.together(e / x)).is_polynomial(x) if False else True:
    q, r = sp.div(sp.Poly(e, x), sp.Poly(x, x))
    if r.as_expr() != 0:
        break
    e = q.as_expr()
    mult0 += 1
print("  multiplicity of the exponent 0 at z=0 :  m = %d" % mult0)
print("  => RPC prediction: recurrence order r = 1 + floor(m/2) = %d ; actual r = %d"
      % (1 + mult0 // 2, J['order']))

# characteristic polynomial from leading coefficients
lead = [QS7[j][-1] for j in range(5)]
print("\nleading coeffs:", lead)
L = sp.Symbol('L')
ch = sp.expand(sum(sp.Integer(lead[j]) * L ** (4 - j) for j in range(5)) / sp.Integer(lead[0]))
print("char poly (monic):", sp.expand(ch))

# ---- kappa vector
DPS = int(sys.argv[1]) if len(sys.argv) > 1 else 260
K = int(sys.argv[2]) if len(sys.argv) > 2 else 12
M = int(sys.argv[3]) if len(sys.argv) > 3 else 200
NN = int(sys.argv[4]) if len(sys.argv) > 4 else 700
TOL = int(sys.argv[5]) if len(sys.argv) > 5 else 180
mp.dps = DPS
cc = [mp.mpf(int(sp.Poly(ch, L).coeff_monomial(L ** i))) for i in range(5)]
rr = sorted(polyroots(list(reversed(cc)), maxsteps=600, extraprec=10 * mp.prec),
            key=lambda t: -abs(t))
print("roots:", [nstr(t, 20) for t in rr])
lam = rr[0].real
t0 = time.time()
KI = K + 4          # 3 eps-orders are lost clearing the n=1 resonance
A0 = [0,0,0,1] + [0]*(KI)   # a_0(s)=s^3
r, alpha, cser, chk = kappa_series(QS7, lam, 0, KI, M, [NN - 100, NN], a0=A0)
for nkey in list(r):
    r[nkey] = (r[nkey][0][:K+1], r[nkey][1])
kap, kapb = r[NN][0], r[NN - 100][0]
dg = min(int(-mp.log10(abs(kap[i] - kapb[i]) / abs(kap[i]) + mpf(10) ** (-DPS)))
         for i in range(2, K + 1))
print("alpha = %s   S0 = %s   self-agree %d digits  [%.0fs]"
      % (nstr(alpha, 20), nstr(r[NN][1], 40), dg, time.time() - t0))
lamb = slog(kap, K)

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
    out, seen = [('1', mp.mpf(1))], {'1'}
    for ww in range(2, w + 1):
        for nm, v in zprod_basis(ww):
            if nm not in seen:
                seen.add(nm); out.append((nm, v))
    return out
def tryid(label, val, bs, tol=TOL, maxc=10 ** 14):
    names = [b[0] for b in bs]
    rr2 = pslq([val] + [b[1] for b in bs], tol=mpf(10) ** (-tol), maxcoeff=maxc,
               maxsteps=4 * 10 ** 6)
    if rr2 is None or rr2[0] == 0:
        print("   %-14s : NONE (dim=%d, tol 1e-%d)" % (label, len(bs), tol)); return None
    c0 = rr2[0]
    print("   %-14s = %s" % (label, " ".join(
        "%+s*%s" % (Fraction(-rr2[i + 1], c0), names[i])
        for i in range(len(names)) if rr2[i + 1] != 0)))
    return rr2

print("\nkappa/lambda of the zeta(7) operator:")
for i in range(K + 1):
    print("  kappa_%-2d = %s" % (i, nstr(kap[i], 40)))
print("\n graded test:")
for j in range(2, K + 1):
    tryid("kappa_%d" % j, kap[j], zprod_basis(j))
for j in range(2, K + 1):
    tryid("lambda_%d" % j, lamb[j], zprod_basis(j))
print("\n inhomogeneous test:")
for j in range(2, min(K, 9) + 1):
    tryid("kappa_%d" % j, kap[j], allw(j))
for j in range(2, min(K, 9) + 1):
    tryid("lambda_%d" % j, lamb[j], allw(j))
json.dump({'kappa': [mp.nstr(v, 200) for v in kap], 'lambda': [mp.nstr(v, 200) for v in lamb],
           'S0': mp.nstr(r[NN][1], 200), 'alpha': mp.nstr(alpha, 30), 'm': mult0},
          open('/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma/z7_kappa.json', 'w'), indent=1)
