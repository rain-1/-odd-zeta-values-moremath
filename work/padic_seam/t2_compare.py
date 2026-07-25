import sys, pickle
sys.set_int_max_str_digits(3000000)
from fractions import Fraction as Fr
from padic import vp, dstr, agree, zeta_p, zeta_p_sh, frac_mod
from t1_towers import fmod, tower_indices
from lll import padic_relation, rat_recon

D = pickle.load(open("t1_data.pkl", "rb"))
data = D["data"]
PRIMES = [5, 7, 11, 13]
W = 3

def Lambda(p, a, NMAX, prec):
    """limit of p^{3s} b_{a p^s}/a_{a p^s}, returned as (v, unit mod p^prec, ndigits_certain)"""
    t = [x for x in tower_indices(p, NMAX, a)]
    t = [(s, n) for s, n in t if n in data]
    if len(t) < 2: return None
    s, n = t[-1]
    A, B = data[n]
    r = fmod(A, B, p, prec + 10)
    if r is None: return None
    v, u = r
    v += W*s
    # certified digits: L_inf = L_s  mod p^{3s + 3 + v}   (depth-3 descent), be conservative
    cert = W*s + W
    return v, u % p**prec, cert, n

print("="*100)
print("T2 : comparison of tower limits Lambda_a with zeta_p(3) = L_p(3, omega^{-2})")
print("="*100)
NMAX = D["NMAX"]
for p in PRIMES:
    K = {5: 22, 7: 19, 11: 14, 13: 14}[p]
    z3 = zeta_p(3, p, K)
    print("\n--- p = %d ---   zeta_p(3) mod p^%d = %d" % (p, K, z3))
    print("    zeta_p(3) base-%d digits (LSF): %s" % (p, dstr(z3, p, min(K, 16))))
    for a in range(1, p):
        r = Lambda(p, a, NMAX, K + 6)
        if r is None: continue
        v, u, cert, n = r
        KK = min(K, cert + min(0, v))          # usable precision on the SHIFTED value
        # value = p^v * u ; compare against zeta_p(3) after clearing p^v
        SH = max(0, -v)
        Lsh = (u * p**(v + SH)) % p**KK        # p^SH * Lambda_a, p-integral
        z3sh = (z3 * p**SH) % p**KK
        # 1) is Lambda_a - zeta_p(3) rational?
        diff = (Lsh - z3sh) % p**KK
        rr = rat_recon(diff, p, KK)
        # 2) is Lambda_a itself rational?
        r0 = rat_recon(Lsh, p, KK)
        print("  a=%2d  v_p=%2d  cert %2d digits (n=%d)   Lam-zeta rational? %s   Lam rational? %s"
              % (a, v, KK, n, ("YES  p^%d*(Lam-z3) = %s" % (SH, rr)) if rr else "no",
                 ("YES  p^%d*Lam = %s" % (SH, r0)) if r0 else "no"))
