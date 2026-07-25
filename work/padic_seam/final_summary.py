import sys, pickle
sys.set_int_max_str_digits(3000000)
from padic import vp, dstr, zeta_p, zeta_p_sh, Lp_shift
from t1_towers import fmod, tower_indices, strip
from lll import rat_recon

AP = pickle.load(open("t1_data.pkl", "rb")); APD = AP["data"]; APN = AP["NMAX"]
lad = pickle.load(open("bz_lad5000.pkl", "rb")); BN = max(lad['Q'])

def Lam_apery(p, a, prec):
    t = [(s, n) for s, n in tower_indices(p, APN, a) if n in APD]
    s, n = t[-1]
    v, u = fmod(*APD[n], p, prec)
    return v + 3*s, u, 3*(s+1), n

def ratio(num, den, p, prec):
    n1, d1 = num; n2, d2 = den
    va, ua = strip(n1, p); vb, ub = strip(d1, p)
    vc, uc = strip(n2, p); vd, ud = strip(d2, p)
    M = p**prec
    return (va-vb)-(vc-vd), (ua%M)*pow(ub%M,-1,M)%M*(ud%M)%M*pow(uc%M,-1,M)%M

def Lam_bz(row, W, p, a, prec):
    t = [(s, n) for s, n in tower_indices(p, BN, a)]
    s, n = t[-1]
    v, u = ratio(lad[row][n], lad['Q'][n], p, prec)
    return v + W*s, u, 3*(s+1), n

print("="*100)
print("FINAL SUMMARY — explicit tower limits (base-p digits, least significant first)")
print("="*100)
for p in [5, 7, 11, 13]:
    print("\n--- p = %d ---" % p)
    z3 = zeta_p(3, p, 30); z5s = Lp_shift(5, -4, p, 30, SH=1)
    print("  zeta_p(3)            = %s ..." % dstr(z3, p, 12))
    print("  p*zeta_p(5)          = %s ..." % dstr(z5s, p, 12))
    v, u, K, n = Lam_apery(p, 1, 40)
    print("  Apery  Lambda_1 : v_p=%2d, %d certified digits (n=%d)" % (v, K, n))
    print("          p^%d*Lambda_1 = %s ..." % (max(0,-v), dstr(u*p**(v+max(0,-v)) % p**K, p, min(K,12))))
    for row, W in (('P',5), ('Ph',3)):
        v, u, K, n = Lam_bz(row, W, p, 1, 40)
        print("  BZ %-3s Lambda^%s_1 : v_p=%2d, %d certified digits (n=%d)" % (row, row, v, K, n))
        print("          p^%d*Lambda = %s ..." % (max(0,-v), dstr(u*p**(v+max(0,-v)) % p**K, p, min(K,12))))
    # renormalised defect
    vP,uP,KP,_ = Lam_bz('P',5,p,1,40); vH,uH,KH,_ = Lam_bz('Ph',3,p,1,40)
    K = min(KP,KH); vd = vH-vP; ud = uH*pow(uP%p**K,-1,p**K)%p**K
    print("  RENORMALISED DEFECT  hat-c_p(1) : v_p = %d, p^%d*hat-c = %s ..."
          % (vd, max(0,-vd), dstr(ud*p**(vd+max(0,-vd))%p**K, p, min(K,12))))

print("\n" + "="*100)
print("The decisive negative, stated sharply:  the p-adic LINEAR FORMS BLOW UP")
print("="*100)
print("  Bel's criterion needs |a_n + b_n xi|_p <= exp(-alpha n). Ours:")
for p in [5,7,11,13]:
    outs=[]
    for n in [50, 200, 1000, 5000]:
        if n not in APD: continue
        A,B = APD[n]
        vA,_ = strip(A,p); vB,_ = strip(B,p)
        L=0
        while p**(L+1)<=n: L+=1
        outs.append("n=%d: v_p(b_n - zeta_p(3) a_n) - v_p(a_n) = %d (= -3L = %d)"%(n, vB-vA, -3*L))
    print("  p=%2d Apery  : %s" % (p, "; ".join(outs)))
for p in [5,7,11,13]:
    outs=[]
    for n in [50,200,1000,5000]:
        L=0
        while p**(L+1)<=n: L+=1
        vP,_ = ratio(lad['P'][n], lad['Q'][n], p, 5), None
        outs.append("n=%d: v_p(I'_n/Q_n) = %d (= -5L = %d)"%(n, vP[0], -5*L))
    print("  p=%2d BZ P   : %s" % (p, "; ".join(outs)))
print("\n  => |linear form|_p grows like n^3 (Apery) / n^5 (BZ P) / n^3 (BZ Ph):")
print("     the forms DIVERGE p-adically. No Bel/Calegari-type criterion can ever apply.")
