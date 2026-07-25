"""THE STRUCTURE THEOREM, verified order by order.

  Atil_1 = lim_s a_{p^s} = sum_{i>=0} sum_{p!|j, 0<j<=p^i} [ c_p(p^i,j) c_p(p^i+j,j) ]^2
           (the (i,j) block has valuation exactly 2i;  (i,j)=(0,1) is the k=n term)
           = 1 + c(2,1)^2 + sum_{j=1}^{p-1}[c(p,j)c(p+j,j)]^2 + O(p^4)

  Btil_1 = h_p(1) Atil_1 + sum over (k-block i, m-block i') of
             [c_p(p^i,j)c_p(p^i+j,j)]^2 * (-1)^{j'-1} p^{3 i'} / (2 j'^3 c_p(p^{i'},j') c_p(p^{i'}+j',j'))
           the (i,i') term has valuation 2i + 3i' with i' <= i ... leading terms:
             (0,0): c(2,1)^2 * 1/(2 c(2,1))        = c(2,1)/2                       [v=0]
             (0,1): c(2,1)^2 * sum_{j'=1}^{p-1} (-1)^{j'-1}p^3/(2 j'^3 c(p,j')c(p+j',j'))  [v=3]
  so  Lambda_1 = h_p(1) + (c(2,1)/2 + X_3 + O(p^5)) / Atil_1 .
"""
import sys
from fractions import Fraction as Fr
from pnum import P
from t2_ansatz import load
from t3_harm import h_p
from t7_kaz import kaz_direct

def cc(a, b, p, K, cache={}):
    key = (a, b, p, K)
    if key not in cache:
        cache[key] = kaz_direct(a, b, p, K)[0]
    return cache[key]

def main(p, K=9):
    dat, _ = load(p)
    L, At, Bt = dat[1]["L"], dat[1]["At"], dat[1]["Bt"]
    print("=" * 72); print("p =", p, "  certified digits:", L.prec)
    c21 = cc(2, 1, p, K)
    # ---- Atil_1 order by order
    S0 = P.from_frac(p, 1, K) + c21*c21
    d = At - S0
    print("  Atil_1 = 1 + c(2,1)^2 + ? :  first discrepancy at v_p = %s (expect 2)"
          % (d.v if not d.is_zero() else "inf"))
    blk1 = P.zero(p)
    for j in range(1, p):
        t = cc(p, j, p, K) * cc(p+j, j, p, K)
        blk1 = blk1 + t*t
    S1 = S0 + blk1
    d1 = At - S1
    print("  Atil_1 = ... + sum_j [c(p,j)c(p+j,j)]^2 :  discrepancy at v_p = %s (expect 4)"
          % (d1.v if not d1.is_zero() else "inf"))
    # ---- Lambda_1 order by order
    H = h_p(1, p, L.prec + 4)
    lead = c21 / P.from_frac(p, 2, K)
    e0 = (L - H) * At - lead
    print("  (Lambda_1-h_p(1))*Atil_1 = c(2,1)/2 + ? : discrepancy at v_p = %s (expect 3)"
          % (e0.v if not e0.is_zero() else "inf"))
    X3 = P.zero(p)
    for j in range(1, p):
        den = cc(p, j, p, K) * cc(p+j, j, p, K) * P.from_frac(p, 2*j**3, K)
        X3 = X3 + P.from_frac(p, (-1)**(j-1) * p**3, K) / den
    X3 = X3 * (c21*c21)
    e1 = e0 - X3
    print("  ... + c(2,1)^2 sum_j (-1)^{j-1}p^3/(2j^3 c(p,j)c(p+j,j)) : discrepancy at v_p = %s (expect 5)"
          % (e1.v if not e1.is_zero() else "inf"))
    return dict(c21=c21, At=At, L=L, H=H)

if __name__ == "__main__":
    for p in [int(x) for x in sys.argv[1:]] or [7, 11, 13]:
        main(p)
