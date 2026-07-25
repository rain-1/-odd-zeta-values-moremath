"""T3 zoo: standard p-adic constants, computed exactly.

 - Fermat quotients q_p(a) = (a^{p-1}-1)/p                     (exact rational)
 - Wolstenholme quotients w1 = H_{p-1}/p^2, w2 = H^{(2)}_{p-1}/p (exact rationals)
 - Bernoulli B_{p-3}                                            (exact rational)
 - Iwasawa log_p(x) = (1/(p-1)) log(x^{p-1}),  log(1+y)=sum (-1)^{k+1} y^k/k
 - zeta_p(3), zeta_p(5)  (Kubota-Leopoldt, validated implementation of ../padic_seam/padic.py)
 - unit root of the weight-4 level-8 newform eta(2z)^4 eta(4z)^4 attached to the
   Apery zeta(3) numbers (Beukers): root of x^2 - a_p x + p^3 with v_p = 0.
"""
import sys, os
from fractions import Fraction as Fr
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "padic_seam"))
import padic as KL
from pnum import P

def fermat_quot(a, p):
    return Fr(a**(p-1) - 1, p)

def wolstenholme(p):
    H1 = sum(Fr(1, m) for m in range(1, p))
    H2 = sum(Fr(1, m*m) for m in range(1, p))
    return Fr(H1, p*p), Fr(H2, p)

def bern(k):
    return KL.bern(k)

def iwasawa_log(x, p, K):
    """log_p(x) for x a p-unit rational; = (1/(p-1)) * log(x^{p-1}), exact series."""
    x = Fr(x)
    y = x**(p-1) - 1
    assert y.denominator % p != 0
    v = _vp(y.numerator, p)
    assert v >= 1, "x^{p-1} not 1 mod p"
    W = K + 12
    acc = P.zero(p)
    yy = P.from_frac(p, y, W)
    term = P.from_frac(p, 1, W)
    k = 1
    while k*v - _vp(k, p) <= K + 6:
        term = term * yy                       # y^k
        acc = acc + term / P.from_frac(p, Fr((-1)**(k+1) * k), W)
        k += 1
    return (acc / P.from_frac(p, p-1, W)).trunc(K)

def _vp(n, p):
    v = 0
    while n % p == 0:
        n //= p; v += 1
    return v

def iwasawa_log2(x, p, K):
    """same, written straightforwardly with Fractions then reduced (cross-check)."""
    x = Fr(x)
    y = x**(p-1) - 1
    v = _vp(y.numerator, p)
    tot = Fr(0)
    k = 1
    while k*v - (_vp(k, p) if k % p == 0 else 0) <= K + 6:
        tot += Fr((-1)**(k+1), k) * y**k
        k += 1
    return P.from_frac(p, tot / (p-1), K)

def zeta_p_val(s, p, K):
    """zeta_p(s) as a P.  SH covers both the (p-1)|(s-1) pole and the p | (s-1)
       divisibility of the 1/(s-1) prefactor in the Volkenborn series."""
    SH = 1 + _vp(s - 1, p) if s != 1 else 1
    v = KL.zeta_p_sh(s, p, K + 2 + SH, SH)
    return P(p, -SH, v, K + 2 + SH)

def eta448_coeffs(N):
    """q-expansion of eta(2z)^4 eta(4z)^4 = q * prod (1-q^{2n})^4 (1-q^{4n})^4,
       the weight-4 level-8 newform attached (Beukers) to the Apery zeta(3) numbers."""
    C = [0]*(N+1)
    C[0] = 1
    def mulpow(C, step, e):
        for _ in range(e):
            D = [0]*(N+1)
            for i, c in enumerate(C):
                if not c: continue
                # multiply by (1 - q^{step*n}) for all n: do it as a product below
                pass
            return C
        return C
    # straightforward: build prod (1-q^{2n})^4 (1-q^{4n})^4 by repeated multiplication
    P_ = [0]*(N+1); P_[0] = 1
    for step in (2, 4):
        for _ in range(4):
            for n in range(step, N+1, step):
                # multiply P_ by (1 - q^n)
                for i in range(N, n-1, -1):
                    P_[i] -= P_[i-n]
    return [0] + P_[:N]      # shift by q

def unit_root(p, K, ap=None):
    """root of x^2 - a_p x + p^3 = 0 with v_p(x)=0, by Hensel from x = a_p mod p."""
    if ap is None:
        C = eta448_coeffs(p+1)
        ap = C[p]
    if ap % p == 0:
        return None, ap                      # supersingular: no unit root in Z_p
    M = p**(K+2)
    x = ap % M
    for _ in range(2*K + 10):
        f = (x*x - ap*x + p**3) % M
        d = (2*x - ap) % M
        x = (x - f * pow(d, -1, M)) % M
    assert (x*x - ap*x + p**3) % p**K == 0
    return P(p, 0, x, K), ap

if __name__ == "__main__":
    for p in (5, 7, 11, 13):
        K = 20
        print("p =", p)
        print("   q_p(2) =", fermat_quot(2, p), " q_p(3) =", fermat_quot(3, p))
        w1, w2 = wolstenholme(p)
        print("   H_{p-1}/p^2 =", w1, "  H2_{p-1}/p =", w2, "  B_{p-3} =", bern(p-3))
        l2, l2b = iwasawa_log(2, p, K), iwasawa_log2(2, p, K)
        print("   log_p(2) =", l2, " cross-check equal:", l2.key(K-2) == l2b.key(K-2))
        l4 = iwasawa_log(4, p, K)
        print("   log_p(4) - 2 log_p(2) is zero:", (l4 - l2*2).is_zero(),
              " log_p(4)=", l4)
        z3 = zeta_p_val(3, p, K)
        print("   zeta_p(3) =", z3)
        u, ap = unit_root(p, K)
        print("   a_p(eta(2z)^4eta(4z)^4) =", ap, " unit root =", u)
