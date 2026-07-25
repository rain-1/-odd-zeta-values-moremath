import sys, pickle
sys.set_int_max_str_digits(3000000)
from padic import vp, dstr, agree, zeta_p, zeta_p_sh
from t1_towers import fmod
from fractions import Fraction as Fr

D = pickle.load(open("t1_data.pkl", "rb"))
data, jobs = D["data"], D["jobs"]

W = 3   # weight

def tower_vals(p, t, prec):
    """returns [(s, n, v, u)] with p^{3s} f(n) = p^v * u,  u unit mod p^prec"""
    out = []
    for s, n in t:
        A, B = data[n]
        r = fmod(A, B, p, prec)
        if r is None: out.append((s, n, None, None)); continue
        v, u = r
        out.append((s, n, v + W*s, u))
    return out

print("="*100)
print("T1 : p-adic Apery towers,  L_s := p^{3s} b_n / a_n  at n = a*p^s  (and general branches)")
print("="*100)
LIMITS = {}
for label, p, t in jobs:
    prec = W*(len(t)) + 6
    vals = tower_vals(p, t, prec)
    if any(v is None for _, _, v, _ in vals): continue
    # convert to residues mod p^{prec} allowing shift: use common shift SHIFT = -min v (>=0)
    mv = min(v for _, _, v, _ in vals)
    resid = []
    for s, n, v, u in vals:
        resid.append((s, n, v, (u * p**(v - mv)) % p**prec))
    # agreement between successive levels
    ag = []
    for i in range(1, len(resid)):
        ag.append(agree(resid[i][3], resid[i-1][3], p, prec))
    top = resid[-1]
    print("\np=%-3d %-28s  levels s=0..%d  (n_max=%d)   min v_p = %d" %
          (p, label, len(t)-1, t[-1][1], mv))
    print("   v_p(p^{3s} f(n_s)) by level:", [v for _, _, v, _ in vals])
    print("   digits of agreement L_s vs L_{s-1}:", ag)
    LIMITS[(p, label)] = (mv, top[3], ag)
pickle.dump(LIMITS, open("t1_limits.pkl", "wb"))
