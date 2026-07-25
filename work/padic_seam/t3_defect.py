"""T3: the p-adic defect c_p for the Brown-Zudilin pair, and comparison with zeta_p(5), zeta_p(3)."""
import sys, pickle
sys.set_int_max_str_digits(3000000)
from fractions import Fraction as F
from padic import vp, dstr, agree, zeta_p, zeta_p_sh, Lp_shift, frac_mod
from t1_towers import strip, fmod, tower_indices
from lll import padic_relation, rat_recon

lad = pickle.load(open(sys.argv[1] if len(sys.argv) > 1 else "bz_lad5000.pkl", "rb"))
NMAX = max(lad['Q'])
try:
    AP = pickle.load(open("t1_data.pkl", "rb")); APD = AP["data"]; APN = AP["NMAX"]
except Exception:
    APD = None

def ratio(num, den, p, prec):
    n1, d1 = num; n2, d2 = den
    va, ua = strip(n1, p); vb, ub = strip(d1, p)
    vc, uc = strip(n2, p); vd, ud = strip(d2, p)
    M = p**prec
    return (va - vb) - (vc - vd), (ua % M) * pow(ub % M, -1, M) % M * (ud % M) % M * pow(uc % M, -1, M) % M

def limit(row, W, p, a, prec):
    """(v, unit mod p^prec, certified digits) for lim p^{Ws} row_{ap^s}/Q_{ap^s}"""
    t = [(s, n) for s, n in tower_indices(p, NMAX, a)]
    if len(t) < 3: return None
    s, n = t[-1]
    if n not in lad[row]: return None
    v, u = ratio(lad[row][n], lad['Q'][n], p, prec)
    return v + W*s, u, 3*(s+1)      # depth-3 gain per level  =>  L_inf = L_s mod p^{3(s+1)}

def show(x, v, p, K, nm):
    SH = max(0, -v)
    return (x * p**(v + SH)) % p**K, SH

print("="*104)
print("T3 : the p-adic defect  c_p(a) := Lambda^Ph_a / Lambda^P_a")
print("   Lambda^P_a  = lim_s p^{5s} P_{ap^s}/Q_{ap^s}   (p-adic avatar of  lim I'_n/Q_n , archimedean zeta(5))")
print("   Lambda^Ph_a = lim_s p^{3s} Ph_{ap^s}/Q_{ap^s}  (p-adic avatar of  lim I^_n/Q_n , archimedean zeta(3))")
print("   archimedean:  c = lim I^_n/I'_n = -1/(2 zeta(2)) = -3/pi^2   [PROVED, work/DEFECT_IDENTIFY.md]")
print("="*104)
for p in [5, 7, 11, 13]:
    prec = 40
    z3 = zeta_p(3, p, prec)
    z5sh = Lp_shift(5, -4, p, prec, SH=1)     # p*zeta_p(5)  (zeta_p(5) may have v=-1 at p=5)
    z5v = 0
    if z5sh % p == 0: z5, z5v = z5sh//p, 0
    else: z5, z5v = z5sh, -1                  # zeta_p(5) = z5 * p^{z5v} with z5 unit-ish
    print("\n===== p = %d =====   v_p(zeta_p(5)) = %d" % (p, z5v))
    rows = []
    for a in range(1, min(p, 8)):
        LP = limit('P', 5, p, a, prec)
        LH = limit('Ph', 3, p, a, prec)
        if LP is None or LH is None: continue
        K = min(LP[2], LH[2], prec - 4)
        # defect
        vd = LH[0] - LP[0]
        ud = LH[1] * pow(LP[1] % p**K, -1, p**K) % p**K
        SH = max(0, -vd)
        cval = (ud * p**(vd + SH)) % p**K
        rr = rat_recon(cval, p, K)
        rows.append((a, LP[0], LH[0], vd, K, cval, SH, rr))
        print("  a=%d  v(Lam^P)=%2d  v(Lam^Ph)=%2d  ->  v_p(c_p)=%2d  K=%2d   p^%d*c_p mod p^K = %d"
              % (a, LP[0], LH[0], vd, K, SH, cval))
        print("        digits of c_p (LSF): %s   rational? %s"
              % (dstr(cval, p, min(K, 14)), rr if rr and max(abs(rr.numerator), rr.denominator) < p**(K/2.0)/100 else "no"))
    # a-independence of c_p
    if len(rows) > 1:
        base = rows[0]
        print("  a-independence of c_p:")
        for r in rows[1:]:
            K = min(base[4], r[4])
            same = (base[3] == r[3]) and ((base[5] - r[5]) % p**K == 0)
            ag = agree(base[5], r[5], p, K) if base[3] == r[3] else -1
            print("      c_p(a=%d) vs c_p(a=1): equal=%s  (agree to %d of %d digits)" % (r[0], same, ag, K))
    # relation of the limits to zeta_p(5), zeta_p(3)
    for a in [1, 2]:
        LP = limit('P', 5, p, a, prec); LH = limit('Ph', 3, p, a, prec)
        if LP is None or LH is None: continue
        K = min(LP[2], LH[2], prec - 4)
        xP, sP = show(LP[1], LP[0], p, K, 'P')
        xH, sH = show(LH[1], LH[0], p, K, 'Ph')
        r1 = padic_relation([z5 % p**K, xP], p, K)[:1]
        r2 = padic_relation([z3 % p**K, xH], p, K)[:1]
        r3 = padic_relation([1, z5 % p**K, xP], p, K)[:1]
        r4 = padic_relation([1, z3 % p**K, xH], p, K)[:1]
        nf2 = (p**K)**0.5; nf3 = p**(K/3.0)
        print("  a=%d  K=%d | (zeta_p(5),Lam^P) best h=%s  | (1,z5,Lam^P) h=%s | noise %.3g / %.3g"
              % (a, K, [max(abs(x) for x in c) for _, c, _ in r1], [max(abs(x) for x in c) for _, c, _ in r3], nf2, nf3))
        print("        | (zeta_p(3),Lam^Ph) best h=%s | (1,z3,Lam^Ph) h=%s"
              % ([max(abs(x) for x in c) for _, c, _ in r2], [max(abs(x) for x in c) for _, c, _ in r4]))
