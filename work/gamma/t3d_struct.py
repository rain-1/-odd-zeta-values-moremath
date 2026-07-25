"""T3d: why do the BZ kappa's leave the MZV ring at weight 6?
Hypotheses tested
  H1  kappa_j(BZ) is inhomogeneous: lies in span of ALL MZV products of weight <= j.
  H2  kappa(s) = N(s) * G(s) with N(s) = I(s)/(I_5 s^5) the *rational* part of the
      indicial polynomial (BV Thm 30), G weight-graded.
  H3  log kappa involves Hurwitz zeta at the OTHER local exponents at z=0
      (1/2 and the three roots of 41218x^3-172113x^2+240582x-112558) -- the
      hypergeometric/Gamma shape of BV Prop 26 / Kerr Ex 6.7.
"""
import sys, json
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma')
from mpmath import mp, mpf, nstr, pslq, zeta, pi, log, sqrt, polyroots, mpc, psi, factorial
from frobkappa import kappa_series, slog, sdiv, smul
from bzop import QS
from fractions import Fraction

DPS = int(sys.argv[1]) if len(sys.argv) > 1 else 300
K = int(sys.argv[2]) if len(sys.argv) > 2 else 13
TOL = int(sys.argv[3]) if len(sys.argv) > 3 else 195
mp.dps = DPS

rts = sorted(polyroots([4, -2368, -188, 1], maxsteps=400, extraprec=8 * mp.prec),
             key=lambda r: -abs(r))
lam3 = rts[0].real
r, alpha, cser, _ = kappa_series(QS, lam3, 0, K, 200, [600])
kap = r[600][0]
lam = slog(kap, K)

z2 = zeta(2)
def zprod_basis(w):
    out = []
    def rec(rem, minodd, name, val):
        if rem % 2 == 0 and rem >= 0:
            out.append((name + ('z2^%d' % (rem // 2) if rem > 0 else '1'),
                        val * z2 ** (rem // 2)))
        o = minodd
        while o <= rem:
            rec(rem - o, o, name + 'z%d.' % o, val * zeta(o))
            o += 2
    rec(w, 3, '', mp.mpf(1))
    return out

def allw_basis(w):
    out = [('1', mp.mpf(1))]
    for ww in range(2, w + 1):
        out += zprod_basis(ww)
    # remove duplicate '1' entries
    seen, res_ = set(), []
    for nm, v in out:
        if nm in seen:
            continue
        seen.add(nm)
        res_.append((nm, v))
    return res_

def tryid(label, val, bs, tol=TOL, maxc=10 ** 12):
    names = [b[0] for b in bs]
    intern = pslq([b[1] for b in bs], tol=mpf(10) ** (-tol), maxcoeff=maxc,
                  maxsteps=10 ** 6) if len(bs) >= 2 else None
    if intern is not None:
        print("   %-16s : BASIS DEGENERATE %s" % (label, intern))
        return None
    rr = pslq([val] + [b[1] for b in bs], tol=mpf(10) ** (-tol), maxcoeff=maxc,
              maxsteps=2 * 10 ** 6)
    if rr is None or rr[0] == 0:
        print("   %-16s : NONE  (dim=%d, tol 1e-%d, |c|<=%.0e)" % (label, len(bs), tol, maxc))
        return None
    c0 = rr[0]
    terms = " ".join("%+s*%s" % (Fraction(-rr[i + 1], c0), names[i])
                     for i in range(len(names)) if rr[i + 1] != 0)
    print("   %-16s = %s" % (label, terms))
    return rr

print("=== H1: inhomogeneous?  kappa_j in span(all MZV products of weight <= j) ===")
for j in range(5, min(K, 9) + 1):
    tryid("kappa_%d" % j, kap[j], allw_basis(j))
    tryid("lambda_%d" % j, lam[j], allw_basis(j))

print("\n=== H2: divide by the rational indicial factor N(s)=I(s)/(I_5 s^5) ===")
# I(s) = q_0(s);  q_0 = 2 s^5 (2s-1)(41218 s^3 -172113 s^2 +240582 s -112558)
Npoly = [mp.mpf(x) for x in [225116, -931396, 1306554, -770888, 164872]]
Npoly = [x / Npoly[0] for x in Npoly]
Ns = [Npoly[i] if i < len(Npoly) else mp.mpf(0) for i in range(K + 1)]
G = sdiv(kap, Ns, K)
G2 = smul(kap, Ns, K)
lg = slog(G, K)
for j in range(2, min(K, 9) + 1):
    tryid("G_%d=(k/N)_%d" % (j, j), G[j], zprod_basis(j))
for j in range(2, min(K, 9) + 1):
    tryid("logG_%d" % j, lg[j], zprod_basis(j))
for j in range(2, min(K, 8) + 1):
    tryid("(k*N)_%d" % j, G2[j], zprod_basis(j))

print("\n=== H3: Hurwitz zeta at the other local exponents at z=0 ===")
cub = polyroots([41218, -172113, 240582, -112558], maxsteps=400, extraprec=8 * mp.prec)
print("  cubic exponents:", [nstr(x, 25) for x in cub])
print("  (2s-1) exponent: 1/2")
def T(k):
    """sum over the 3 cubic exponents of Hurwitz zeta(k, rho)  (rho may be complex)"""
    s = mp.mpf(0) * mpc(1)
    for x in cub:
        s += mp.zeta(k, x)
    return s.real if abs(s.imag) < mpf(10) ** (-DPS + 30) else s
def Tm(k):
    """same but at 1-rho"""
    s = mp.mpf(0) * mpc(1)
    for x in cub:
        s += mp.zeta(k, 1 - x)
    return s.real if abs(s.imag) < mpf(10) ** (-DPS + 30) else s
for j in [2, 3, 4, 5, 6, 7]:
    bs = zprod_basis(j) + [('T%d' % j, T(j))]
    tryid("lambda_%d +T" % j, lam[j], bs)
for j in [6, 7]:
    bs = zprod_basis(j) + [('T%d' % j, T(j)), ('Tm%d' % j, Tm(j))]
    tryid("lambda_%d +T,Tm" % j, lam[j], bs)

print("\n=== H3b: does lambda_j involve log(c) / cubic-field logs after all? ===")
Lc = log(1 / lam3)
zr = polyroots([1, -188, -2368, 4], maxsteps=400, extraprec=8 * mp.prec)  # z^3-188z^2-2368z+4
print("  singularities z:", [nstr(x, 20) for x in zr])
L2 = log(abs(zr[1].real if abs(zr[1].imag) < 1e-30 else zr[1]))
L1 = log(abs(zr[0].real if abs(zr[0].imag) < 1e-30 else zr[0]))
for j in [6, 7]:
    bs = zprod_basis(j) + [('Lc^%d' % j, Lc ** j)] + \
         [('z%d*Lc^%d' % (j - m, m), (zeta(j - m) if j - m >= 2 else mp.mpf(1)) * Lc ** m)
          for m in range(1, j - 1)]
    tryid("lambda_%d +logs" % j, lam[j], bs, maxc=10 ** 10)
