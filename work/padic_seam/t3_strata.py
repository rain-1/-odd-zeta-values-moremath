"""T3: the p-adic valuation strata of the three BZ rows (and of the Apery pair)."""
import sys, pickle
from collections import Counter
sys.set_int_max_str_digits(3000000)
from t1_towers import strip

lad = pickle.load(open(sys.argv[1] if len(sys.argv) > 1 else "bz_lad5000.pkl", "rb"))
NMAX = max(lad['Q'])

def v(pair, p):
    a, b = pair
    va, _ = strip(a, p); vb, _ = strip(b, p)
    return va - vb

def L(n, p):
    k = 0
    while p**(k+1) <= n: k += 1
    return k

print("BZ valuation strata, n = 1..%d,  L = floor(log_p n)" % NMAX)
print("   claim: v_p(Q_n) >= 0 ;  v_p(Ph_n/Q_n) = -3L + O(1) ;  v_p(P_n/Q_n) = -5L + O(1)")
for p in [5, 7, 11, 13, 17, 19]:
    cQ, cH, cP = Counter(), Counter(), Counter()
    for n in range(1, min(NMAX, 5000)+1):
        l = L(n, p)
        vq = v(lad['Q'][n], p)
        cQ[vq] += 1
        if lad['Ph'][n][0]: cH[v(lad['Ph'][n], p) - vq + 3*l] += 1
        if lad['P'][n][0]:  cP[v(lad['P'][n], p)  - vq + 5*l] += 1
    print("\n p=%d" % p)
    print("   v_p(Q_n)                : %s" % dict(sorted(cQ.items())))
    print("   v_p(Ph_n/Q_n) + 3L      : %s   (min %d)" % (dict(sorted(cH.items())), min(cH)))
    print("   v_p(P_n/Q_n)  + 5L      : %s   (min %d)" % (dict(sorted(cP.items())), min(cP)))
    # the raw defect exponent
    cD = Counter()
    for n in range(1, min(NMAX, 5000)+1):
        l = L(n, p)
        if lad['Ph'][n][0] and lad['P'][n][0]:
            cD[v(lad['Ph'][n], p) - v(lad['P'][n], p) - 2*l] += 1
    print("   v_p(Ph_n/P_n) - 2L      : %s   (min %d, max %d)" % (dict(sorted(cD.items())), min(cD), max(cD)))
