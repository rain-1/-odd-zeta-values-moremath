"""T3: p-adic towers for the BZ cellular pair (Q_n; P_n -> zeta(5), Ph_n -> zeta(3))."""
import sys, pickle
sys.set_int_max_str_digits(3000000)
from fractions import Fraction as F
from padic import vp, dstr, agree, zeta_p, zeta_p_sh, frac_mod
from t1_towers import strip
from lll import padic_relation, rat_recon

FN = sys.argv[1] if len(sys.argv) > 1 else "bz_lad5000.pkl"
lad = pickle.load(open(FN, "rb"))
NMAX = max(lad['Q'])
print("BZ ladders loaded to n =", NMAX)

def ratio(num, den, p, prec):
    """(num/den) as (v, unit mod p^prec); num,den given as (a,b) integer pairs."""
    n1, d1 = num; n2, d2 = den
    va, ua = strip(n1, p); vb, ub = strip(d1, p)
    vc, uc = strip(n2, p); vd, ud = strip(d2, p)
    M = p**prec
    v = (va - vb) - (vc - vd)
    u = (ua % M) * pow(ub % M, -1, M) % M * (ud % M) % M * pow(uc % M, -1, M) % M
    return v, u

def tower(p, a, NMAX):
    out, s = [], 0
    while a*p**s <= NMAX:
        out.append((s, a*p**s)); s += 1
    return out

def run(row, W, p, a, prec):
    """L_s = p^{W s} row_n / Q_n along n = a p^s.  returns list of (s,n,v,u) plus agreements."""
    t = tower(p, a, NMAX)
    if len(t) < 3: return None
    vals = []
    for s, n in t:
        if n not in lad[row] or lad[row][n][0] == 0:
            vals.append((s, n, None, None)); continue
        v, u = ratio(lad[row][n], lad['Q'][n], p, prec)
        vals.append((s, n, v + W*s, u))
    if any(v is None for _, _, v, _ in vals): return None
    mv = min(v for _, _, v, _ in vals)
    res = [(s, n, v, (u * p**(v - mv)) % p**prec) for s, n, v, u in vals]
    ag = [agree(res[i][3], res[i-1][3], p, prec) for i in range(1, len(res))]
    return vals, mv, res, ag

print("="*104)
print("T3 : BZ towers.  P-row weight 5 (P_n/Q_n -> zeta(5)),  Ph-row weight 3 (Ph_n/Q_n -> zeta(3))")
print("="*104)
for p in [5, 7, 11, 13]:
    prec = 40
    print("\n===== p = %d =====" % p)
    for row, W in (('P', 5), ('Ph', 3)):
        for a in range(1, 8):
            r = run(row, W, p, a, prec)
            if r is None: continue
            vals, mv, res, ag = r
            print("  %-3s w=%d a=%d  s=0..%d (n=%d)  v_p(p^{%ds}row/Q) = %s   agreement: %s"
                  % (row, W, a, vals[-1][0], vals[-1][1], W,
                     [v for _, _, v, _ in vals], ag))
