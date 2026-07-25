import sys, pickle
sys.set_int_max_str_digits(3000000)
from fractions import Fraction as Fr
from math import log
from padic import vp, dstr, agree, zeta_p, zeta_p_sh, frac_mod
from t1_towers import fmod, tower_indices
from lll import padic_relation, rat_recon

D = pickle.load(open("t1_data.pkl", "rb")); data = D["data"]; NMAX = D["NMAX"]
W = 3
PREC = {5: 24, 7: 21, 11: 15, 13: 15}

def Lambda(p, a, prec):
    t = [(s, n) for s, n in tower_indices(p, NMAX, a) if n in data]
    if len(t) < 2: return None
    s, n = t[-1]
    r = fmod(*data[n], p, prec + 12)
    if r is None: return None
    v, u = r
    return v + W*s, u, W*s + W, n    # (valuation, unit mod p^{prec+12}, certified digits, n)

def report(name, vals, p, K, thresh_bits):
    rels = padic_relation(vals, p, K)
    out = []
    for norm, c, chk in rels[:3]:
        h = max(abs(x) for x in c)
        out.append((h, c))
    return out

print("="*104)
print("T2 : integer-relation search  c0*1 + c1*zeta_p(3) + c2*Lambda_a = 0  (mod p^K), heights reported")
print("     genuine relation must have height << p^(K/3) (the LLL noise floor)")
print("="*104)
for p in [5, 7, 11, 13]:
    K = PREC[p]
    z3 = zeta_p(3, p, K + 12)
    noise = p**(K/3.0)
    print("\n--- p=%d,  K=%d,  LLL noise floor  p^(K/3) = %.3g ---" % (p, K, noise))
    for a in range(1, p):
        r = Lambda(p, a, K + 12)
        if r is None: continue
        v, u, cert, n = r
        KK = min(K, cert + min(0, v))
        SH = max(0, -v)
        Lsh = (u * p**(v + SH)) % p**KK
        vals = [1 % p**KK, z3 % p**KK, Lsh]
        best = report("", vals, p, KK, 0)
        # also 2-term: is p^SH*Lambda_a / zeta_p(3) rational?
        vals2 = [z3 % p**KK, Lsh]
        best2 = padic_relation(vals2, p, KK)[:2]
        print("  a=%2d v=%2d K'=%2d | 3-term best heights: %s | 2-term (z3,Lam): %s"
              % (a, v, KK, [(h, c) for h, c in best],
                 [(max(abs(x) for x in c), c) for _, c, _ in best2]))
