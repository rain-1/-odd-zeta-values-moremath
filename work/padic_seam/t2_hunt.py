import sys, pickle
sys.set_int_max_str_digits(3000000)
from fractions import Fraction as Fr
from padic import vp, dstr, zeta_p, zeta_p_sh, frac_mod
from t1_towers import fmod, tower_indices, collect
from lll import padic_relation, rat_recon

D = pickle.load(open("t1_data.pkl", "rb")); data = D["data"]; NMAX = D["NMAX"]
W = 3
PREC = {5: 23, 7: 21, 11: 15, 13: 15}

def Lam(p, a):
    """(v, unit mod p^BIG, certified digits n)"""
    t = [(s, n) for s, n in tower_indices(p, NMAX, a) if n in data]
    if len(t) < 2: return None
    s, n = t[-1]
    r = fmod(*data[n], p, PREC[p] + 20)
    if r is None: return None
    v, u = r
    return v + W*s, u, W*s + W, n

def as_pair(p, a):
    r = Lam(p, a)
    if r is None: return None
    v, u, cert, n = r
    return v, u, min(PREC[p], cert)

def quo(v1, u1, v2, u2, p, K):
    """(p^v1 u1)/(p^v2 u2) as (val, unit mod p^K)"""
    return v1 - v2, u1 * pow(u2 % p**K, -1, p**K) % p**K

print("="*100)
print("T2 hunt: normalisation-free tests on the Apery tower limits Lambda_a")
print("  Lambda_a := lim_s p^{3s} b_{a p^s}/a_{a p^s}   (independent of b -> b + c*a; scales with b -> lam*b)")
print("="*100)
for p in [5, 7, 11, 13]:
    K = PREC[p]
    z3 = zeta_p(3, p, K + 20)
    print("\n=== p = %d  (working precision p^%d) ===" % (p, K))
    L1 = as_pair(p, 1)
    print("  v_p(Lambda_a), a=1..p-1:", [as_pair(p, a)[0] for a in range(1, p)])
    # (A) is Lambda_a / Lambda_1 rational?
    print("  (A) Lambda_a / Lambda_1  rational reconstruction (noise floor height ~ p^(K/2)=%.3g):" % p**(K/2.0))
    for a in range(2, p):
        r = as_pair(p, a)
        if r is None: continue
        KK = min(r[2], L1[2])
        v, u = quo(r[0], r[1], L1[0], L1[1], p, KK + 5)
        SH = max(0, -v)
        x = (u * p**(v + SH)) % p**KK
        rr = rat_recon(x, p, KK)
        h = max(abs(rr.numerator), rr.denominator) if rr else None
        print("      a=%2d  v=%3d  K'=%2d   p^%d*(Lam_a/Lam_1) = %s   height %s"
              % (a, v, KK, SH, rr, h))
    # (B) is Lambda_1 / zeta_p(3) rational?  (2-term LLL, noise floor sqrt(p^K))
    KK = L1[2]
    SH = max(0, -L1[0])
    x = (L1[1] * p**(L1[0] + SH)) % p**KK
    rel = padic_relation([z3 % p**KK, x], p, KK)[:1]
    print("  (B) 2-term (zeta_p(3), p^%d Lambda_1) mod p^%d -> best %s   (noise floor %.3g)"
          % (SH, KK, rel, (p**KK)**0.5))
    # (C) 3-term with 1
    rel3 = padic_relation([1, z3 % p**KK, x], p, KK)[:1]
    print("  (C) 3-term (1, zeta_p(3), p^%d Lambda_1) -> best %s   (noise floor %.3g)"
          % (SH, rel3, p**(KK/3.0)))
