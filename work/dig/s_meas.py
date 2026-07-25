"""DIG-3  s_meas.py -- EXACT measurement of the three ledger components for any
point of the p = 2 VWP cone, including the m = -1 (primitive) direction that
DIG-1's optimiser skipped (`if m < 0: continue`).

Measured, never fitted:
  alpha   : v_2( C^n * S_n ) / n     with S_n the actual Volkenborn linear form,
            J_u computed from an exact truncated Volkenborn (Bernoulli) series.
  E       : the smallest exponent with  d_n^E * C^n * rho_0  in  Z   (and the
            same test on the zeta-coefficient), i.e. the TRUE denominator cost
            including any Phi_n / group saving already present.
  growth  : log max_{i,k} |C^n r_{i,k}| / n      (so C_1 = growth - G).

  S_n = rho_0 + sum_i (-1)^m (i)_m rho_i J_{i+m},   J_u = int_{Z_2} dt/(t+1/2)^u
  (i)_m = prod_{t<m}(i+t) for m >= 0;  (i)_{-1} = 1/(i-1)   [primitive]
"""
import sys, os, math
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s_vwp import VWPX, asymptotic_ledger, LOG2
from family import dn, bern_volkenborn, vp
import sympy

LOG = math.log


def poch(i, m):
    """(i)_m ; m = -1 gives 1/(i-1) (the primitive convention)."""
    if m == -1:
        return F(1, i - 1)
    out = F(1)
    for t in range(m):
        out *= (i + t)
    return out


_JC = {}


def Jval(u, prec, theta=F(1, 2)):
    """int_{Z_2} dt/(t+theta)^u, exact rational, correct mod 2^prec."""
    key = (u, prec, theta)
    if key in _JC:
        return _JC[key]
    tot = F(0)
    k = 0
    while True:
        term = F(int(sympy.binomial(-u, k))) * bern_volkenborn(k) * theta ** (-u - k)
        v = vp(term, 2)
        if v is not None and v > prec:
            break
        tot += term
        k += 1
        if k > prec + 40:
            break
    _JC[key] = tot
    return tot


def measure(M, m, e=None, f=None, ns=(4, 6, 8, 10), dwp=1, verbose=True,
            do_alpha=True):
    e = e if e is not None else (0,) * M
    f = f if f is not None else (0,) * M
    L = asymptotic_ledger(M, m, dwp)
    vC = 2 * M                                     # v_2(C) at the symmetric point
    rows = []
    for n in ns:
        v = VWPX(n, e, f, dwp)
        r = v.partial_fractions()
        rh = v.rho(r)
        r0 = v.rho0(m, r)
        Cn = F(2) ** (vC * n)
        # ---- E : the d_n exponent that clears rho_0 and the zeta coefficients
        cands = [r0] + [poch(i, m) * rh[i] for i in range(2, M + 1) if rh[i]]
        Eneed = 0
        for x in cands:
            y = x * Cn
            d = y.denominator
            k = 0
            while d > 1:
                g = math.gcd(d, dn(n))
                if g == 1:
                    break
                d //= g
                k += 1
            if d > 1:
                k = None            # not cleared by any power of d_n
            Eneed = None if (k is None or Eneed is None) else max(Eneed, k)
        # ---- growth
        mx = max(abs(x) for x in r.values())
        growth = float(LOG(float(mx)) + vC * n * LOG2) / n
        # ---- alpha (exact 2-adic valuation of the true linear form)
        va = None
        if do_alpha:
            prec = int(3 * vC * n) + 60
            S = r0
            for i in range(2, M + 1):
                if rh[i]:
                    # rho0 here is  -sum r (i)_{m+1} T  (the (-1)^m is a common
                    # overall factor with the J-coefficients, so it is dropped)
                    S += poch(i, m) * rh[i] * Jval(i + m, prec)
            if S != 0:
                va = (vp(S, 2) + vC * n) / n
        rows.append((n, Eneed, growth, va))
    if verbose:
        print("  M=%d m=%2d e=%s f=%s   LEDGER: G=%.4f E=%d alpha=%.4f margin=%+.4f "
              "rank=%d w=%s" % (M, m, e, f, L["G"], L["E"], L["alpha"],
                                L["margin"], L["rank"], L["weights"]))
        print("      n |  E_meas  |  growth/n (G=%.4f) |  alpha_meas/n (pred %.4f = %d log2)"
              % (L["G"], L["alpha"], round(L["alpha"] / LOG2)))
        for n, Ee, g, va in rows:
            print("    %3d |   %-6s |     %8.4f        |    %s"
                  % (n, Ee, g, ("%8.4f  = %.2f log2" % (va * LOG2, va)) if va else "   --"))
    return L, rows


if __name__ == "__main__":
    print("=" * 78)
    print("s_meas  T-A : CONTROLS -- the two published p=2 anchors, measured")
    print("=" * 78)
    print("\n[C1] Beukers R^(B):  M=3, m=0   (published mu(zeta_2(3)) <= 7.177398)")
    measure(3, 0, ns=(6, 10, 14, 18))
    print("\n[C2] LSZ 2025:       M=4, m=1   (published mu(zeta_2(5)) <= 20.342651)")
    measure(4, 1, ns=(6, 10, 14, 18))

    print("\n" + "=" * 78)
    print("s_meas  T-B : THE SKIPPED DIRECTION  m = -1 (primitive, Lai-Sprang Lemma 21)")
    print("=" * 78)
    print("\n[B1] M=4, m=-1  -- the SAME rational function as LSZ, integrated as a")
    print("     primitive instead of differentiated.  Ledger says rank 1, weight 3,")
    print("     E = M+m+1-delta = 3, margin = 8log2-3 = +2.5452, mu <= 4.3574 (!!)")
    measure(4, -1, ns=(6, 10, 14, 18))
    print("\n[B2] M=6, m=-1  -- rank 2, weights {3,5}")
    measure(6, -1, ns=(6, 10, 14))
    print("\n[B3] M=5, m=0   -- rank 2, weights {3,5}, margin +1.9315")
    measure(5, 0, ns=(6, 10, 14))
    print("\n[B4] M=6, m=1   -- rank 2, weights {5,7}, margin +1.3178  (Lai's theorem)")
    measure(6, 1, ns=(6, 10, 14))
