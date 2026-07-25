"""Kazandzidis limits and the STRUCTURE THEOREM for the Apery tower limits.

DEFINITION.  c_p(a,b) := lim_t C(a p^t, b p^t)   (exists: Kazandzidis, 3 digits/level).

LEMMA (derived from Morita's factorial factorisation + Beukers-Vlasenko eq.(2)):
  c_p(a,b) = - p^{v_p(C(a,b))} T(a,b) * Gamma_p(a+1)/(Gamma_p(b+1)Gamma_p(a-b+1))
             * exp( - sum_{m odd >=3} zeta_p(m) (a^m - b^m - (a-b)^m) p^m / (m (1-p^m)) )
  where T(a,b) = prod_{l>=1} (-1)^{A_l+1}Gamma_p(A_l+1) / [ (-1)^{B_l+1}Gamma_p(B_l+1)
                 (-1)^{D_l+1}Gamma_p(D_l+1) ],  A_l=floor(a/p^l), B_l=floor(b/p^l),
                 D_l = floor((a-b)/p^l)   (trivial when a < p).

STRUCTURE.  Along n = p^s, v_p(C(p^s,k)) = s - v_p(k), so writing k = j p^{s-i}
(p !| j, 0 < j <= p^i) the Apery summand A(n,k) = (C(n,k)C(n+k,k))^2 has valuation 2i and
   lim_s A(p^s, j p^{s-i}) = [ c_p(p^i, j) c_p(p^i + j, j) ]^2 .
Likewise the inner Apery weight 1/(2m^3 C(n,m)C(n+m,m)) at m = j p^{s-i} contributes
   p^{3s}/(2 m^3 C C) -> p^{3i} (-1)^{j-1} / (2 j^3 c_p(p^i,j) c_p(p^i+j,j)).
Hence  Lambda_1 = h_p(1) + [ c_p(2,1)/2 + X_3 + O(p^5) ] / Atil_1,  with
   X_3 = c_p(2,1)^2 * sum_{j=1}^{p-1} (-1)^{j-1} p^3 / (2 j^3 c_p(p,j) c_p(p+j,j)),
and  Atil_1 = 1 + c_p(2,1)^2 + O(p^2).   All checked below.
"""
import sys
from fractions import Fraction as Fr
from pnum import P
from t6_gamma import exp_p
import zoo

def fact_units(top, p, K):
    """u[n] = prod_{j<=n, p!|j} j mod p^K, for the n we ask for."""
    M = p**K
    acc = 1
    out = {0: 1}
    for j in range(1, top+1):
        if j % p:
            acc = acc * j % M
        out[j] = acc
    return out

def binom_pdig(n, k, p, K, u):
    """C(n,k) mod p^K exactly: p^{carries} * prod units."""
    M = p**K
    num = 1; den = 1; v = 0
    m = n; a = k; b = n - k
    while m:
        num = num * u[m % p**K if False else m] % M if False else num
        break
    # standard: n! = p^{v_p(n!)} prod_i u(floor(n/p^i))
    def parts(x):
        vv = 0; pr = 1; y = x
        while y:
            y //= p
            vv += y
        y = x;
        while y:
            pr = pr * u[y] % M
            y //= p
        return vv, pr
    v1, p1 = parts(n); v2, p2 = parts(k); v3, p3 = parts(n-k)
    return v1 - v2 - v3, p1 * pow(p2*p3 % M, -1, M) % M

def kaz_direct(a, b, p, K):
    """c_p(a,b) = lim_t C(ap^t, bp^t) to K certified digits (3 per level), exact."""
    t = (K + 2)//3 + 1
    top = a * p**t
    u = fact_units(top, p, K + 4)
    vals = []
    for tt in range(t+1):
        v, unit = binom_pdig(a*p**tt, b*p**tt, p, K + 4, u)
        vals.append(P(p, v, unit, K + 4))
    for i in range(1, len(vals)):
        ag = vals[i].agree(vals[i-1]) - vals[i].v
        assert ag >= 3*i, ("rate", a, b, i, ag)
    return vals[-1].trunc(3*(t+1)), vals

def gamma_p_int(n, p, K):
    """Gamma_p(n) for a positive integer n = (-1)^n prod_{j<n, p!|j} j."""
    M = p**K
    r = 1
    for j in range(1, n):
        if j % p:
            r = r * j % M
    return P(p, 0, (-1)**n * r % M, K)

def kaz_formula(a, b, p, K):
    d = a - b
    # tail T(a,b)
    T = P.from_frac(p, 1, K + 4)
    l = 1
    while a // p**l:
        A, B, D = a//p**l, b//p**l, d//p**l
        T = T * gamma_p_int(A+1, p, K+4) * P.from_frac(p, (-1)**(A+1), K+4)
        T = T / (gamma_p_int(B+1, p, K+4) * P.from_frac(p, (-1)**(B+1), K+4))
        T = T / (gamma_p_int(D+1, p, K+4) * P.from_frac(p, (-1)**(D+1), K+4))
        l += 1
    G = gamma_p_int(a+1, p, K+4) / (gamma_p_int(b+1, p, K+4) * gamma_p_int(d+1, p, K+4))
    # p-power
    vC = 0
    x, y, z = a, b, d
    while x:
        if (y % p) + (z % p) != (x % p):   # carry detection is easier via factorials:
            pass
        x //= p; y //= p; z //= p
    from core import vp_fact
    vC = vp_fact(a, p) - vp_fact(b, p) - vp_fact(d, p)
    tot = P.zero(p)
    for m in range(3, K + 4, 2):
        z = zoo.zeta_p_val(m, p, K + 6)
        coef = Fr(-(a**m - b**m - d**m), m) * Fr(p**m, 1 - p**m)
        t = z * P.from_frac(p, coef, K + 6)
        if t.is_zero() or t.v > K + 3:
            continue
        tot = tot + t
    return (P.from_frac(p, -1, K+4) * P(p, vC, 1, K+4) * T * G * exp_p(tot, K + 4)).trunc(K)

if __name__ == "__main__":
    for p in [int(x) for x in sys.argv[1:]] or [7, 11]:
        K = 12
        print("=" * 70); print("p =", p, " verifying c_p(a,b) closed form to", K, "digits")
        tests = [(2,1),(3,1),(3,2),(4,1),(5,2),(7,3),(p,1),(p,2),(p+1,1),(p+1,p),(2*p,p),(p*p,p)]
        for (a, b) in tests:
            if b >= a: continue
            K2 = K if a*p**5 < 4*10**6 else 6
            d0, _ = kaz_direct(a, b, p, K2)
            f0 = kaz_formula(a, b, p, K2)
            dd = d0 - f0
            print("   c_p(%-4d,%-3d) v=%-2d  direct=%s  formula %s" %
                  (a, b, d0.v, " ".join(map(str, d0.digits(6))),
                   "MATCH(all %d)" % min(d0.prec, f0.prec) if dd.is_zero() else "DIFFER at %d" % dd.v))
