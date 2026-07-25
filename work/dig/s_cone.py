"""DIG-3  s_cone.py -- M1: the ledger + the C_1/delta tension over the FULL cone
at p = 2, measured rather than modelled.

The rank-1 slice at weight 7 is (p,r)=(2,1), M=4, m=3, delta=1 [margin -1.4548]
and (p,r)=(2,2), A=2, m=4 [margin -2.8411].  The remaining freedoms are the
brick LENGTHS (Rhin-Viola direction) and the group saving delta_group.  Both are
evaluated here on the same footing:

    margin  =  (alpha - G)  -  C_1  -  E  +  delta_group
             = [ r sum nu + sum lambda/(p-1) ] log p  -  C_1  -  E  +  delta_group

with, for VWP insets e_j, f_j scaled as e_j = eps_j n, f_j = phi_j n,
    sum lambda = M - 2 sum eps ,   sum nu = M - 2 sum phi ,
    G = (sum lambda + sum nu) log 2      [p=2, r=1, l'=1, 1/(p-1)=1]
and BOTH  C_1 = growth - G  and  E (the true d_n exponent, i.e. A+m+1-delta
MINUS any Phi_n / group saving already present) measured exactly.

DEGREE CONSTRAINT: sum lambda <= sum nu, i.e. sum phi <= sum eps.
With e, f >= 0 this forces sum lambda, sum nu <= M, so G <= 2M log2 with
EQUALITY exactly at the symmetric point -- where C_1 = 0 and delta_group = 0.
That is the p = 2 form of the structural wall.  Measured below.
"""
import sys, os, math
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s_vwp import VWPX, LOG2
from family import dn, vp

LOG = math.log


def odd_part(x):
    while x % 2 == 0:
        x //= 2
    return x


def profile_measure(M, m, eps, phi, unit=6, reps=(2, 3, 4), dwp=1, ref=None):
    """eps, phi are integer multiples of 1/unit; e_j = eps_j*k, f_j = phi_j*k,
    h0 = unit*k.  G and gain are the exact asymptotic values; C_1 and E are
    MEASURED (E in units of d_n, i.e. divided by log d_{h0})."""
    rows = []
    sum_lam = M - 2 * sum(eps) / float(unit)
    sum_nu = M - 2 * sum(phi) / float(unit)
    G = (sum_lam + sum_nu) * LOG2
    gain = (sum_nu + sum_lam) * LOG2
    for k in reps:
        h0 = unit * k
        e = tuple(int(x * k) for x in eps)
        f = tuple(int(x * k) for x in phi)
        try:
            v = VWPX(h0, e, f, dwp)
        except ValueError:
            return None
        if not v.admissible():
            return None
        r = v.partial_fractions()
        rh = v.rho(r)
        r0 = v.rho0(m, r)
        vCn = F(len(v.num) + len(v.den))          # v_2(C^{h0}) = sum lam + sum nu, times h0
        scale = F(2) ** int(math.ceil(float(vCn)))
        mx = max(abs(x) for x in r.values() if x != 0)
        growth = (float(LOG(float(mx))) + float(vCn) * LOG2) / h0
        Emeas = 0
        for x in [r0] + [rh[i] for i in range(2, M + 1) if rh[i]]:
            d = odd_part((x * scale).denominator)   # 2-part is paid by C^n
            kk = 0
            while d > 1:
                g = math.gcd(d, dn(h0))
                if g == 1:
                    kk = 99            # not d_n-smooth
                    break
                d //= g
                kk += 1
            Emeas = max(Emeas, kk)
        rows.append((h0, growth, Emeas))
    h0, gr, Em = rows[-1]
    C1raw = gr - G
    C1 = C1raw if ref is None else C1raw - ref
    return dict(sum_lam=sum_lam, sum_nu=sum_nu, G=G, growth=gr, C1raw=C1raw,
                C1=C1, E=Em, gain=gain, margin=gain - max(0.0, C1) - Em, rows=rows)


if __name__ == "__main__":
    print("=" * 78)
    print("M1 cone : p=2, r=1, VWP.  margin = gain - C_1 - E + delta_group,")
    print("          gain = (sum lam + sum nu) log2, C_1 and E MEASURED.")
    print("=" * 78)
    print("\nrank-1 weight-7 slice: M=4, m=3, delta=1  (E should be 7 at the")
    print("symmetric point; margin there is the -1.4548 nearest miss)\n")
    print("  profile (eps ; phi)                sum_lam sum_nu   G       C_1     "
          "E     gain    margin")
    tests = [
        ((0, 0, 0, 0), (0, 0, 0, 0), "symmetric (the anchor)"),
        ((0, 0, 0, 1), (0, 0, 0, 0), "one numerator brick shortened"),
        ((0, 0, 1, 1), (0, 0, 0, 0), "two numerator bricks shortened"),
        ((0, 0, 0, 2), (0, 0, 0, 0), "one numerator brick shortened x2"),
        ((0, 0, 0, 1), (0, 0, 0, 1), "one num + one pole brick shortened"),
        ((0, 0, 1, 1), (0, 0, 0, 1), "asymmetric lengths, degree-tight"),
        ((0, 0, 1, 2), (0, 0, 0, 1), "stronger asymmetry"),
        ((0, 1, 1, 1), (0, 0, 1, 1), "three shortened"),
    ]
    ref = profile_measure(4, 3, (0,0,0,0), (0,0,0,0), unit=6, reps=(2, 3, 4))["C1raw"]
    print("  [o(n) bias at this h0, from the symmetric control: %+0.4f -- subtracted]" % ref)
    for eps, phi, tag in tests:
        d = profile_measure(4, 3, eps, phi, unit=6, reps=(2, 3, 4), ref=ref)
        if d is None:
            print("  %-34s  (inadmissible)" % (str(eps) + ";" + str(phi)))
            continue
        print("  %-34s  %6.3f %6.3f  %7.4f %+7.4f %5s %7.4f %+8.4f   %s"
              % (str(eps) + ";" + str(phi), d["sum_lam"], d["sum_nu"], d["G"],
                 d["C1"], d["E"], d["gain"], d["margin"], tag))

    print("\n  [the same at the rank-2 weight-{5,7} family M=6, m=1]")
    ref6 = profile_measure(6, 1, (0,)*6, (0,)*6, unit=6, reps=(2, 3, 4))["C1raw"]
    for eps, phi, tag in tests:
        e6 = tuple(list(eps) + [0, 0])
        f6 = tuple(list(phi) + [0, 0])
        d = profile_measure(6, 1, e6, f6, unit=6, reps=(2, 3, 4), ref=ref6)
        if d is None:
            print("  %-34s  (inadmissible)" % (str(e6) + ";" + str(f6)))
            continue
        print("  %-34s  %6.3f %6.3f  %7.4f %+7.4f %5s %7.4f %+8.4f   %s"
              % (str(e6) + ";" + str(f6), d["sum_lam"], d["sum_nu"], d["G"],
                 d["C1"], d["E"], d["gain"], d["margin"], tag))
