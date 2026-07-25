"""IDENTIFICATION of the central-binomial tower limit  c_p = lim_s C(2p^s, p^s).

Morita:  n! = p^{v_p(n!)} prod_{i>=0} (-1)^{n_i+1} Gamma_p(n_i+1),  n_i = floor(n/p^i).
Hence   C(2p^s,p^s) = (-1)^{s+1} prod_{k=0}^{s} Gamma_p(2p^k+1) / Gamma_p(p^k+1)^2 ,
and since Gamma_p(1+x) = -Gamma_p(x) for x in pZ_p, the k>=1 factors are
Gamma_p(2p^k)/Gamma_p(p^k)^2, whose log is given by Beukers-Vlasenko eq.(2)
    log Gamma_p(x) = Gamma_p'(0) x - sum_{m>=2} zeta_p(m) x^m / m      (|x|_p < 1).
The Gamma_p'(0) terms cancel (2p^k - 2 p^k = 0) and zeta_p(even) = 0, so

    log(c_p / 2) = - sum_{m odd >= 3} zeta_p(m) (2^m - 2)/m * p^m/(1 - p^m).

This is an EXACT closed form for a tower limit in terms of ALL odd p-adic zeta values.
Verified below against the directly computed c_p.
"""
import sys
from fractions import Fraction as Fr
from pnum import P
from t5_split import cbin_tower
import zoo

def exp_p(x, K):
    """exp of x with v_p(x) > 1/(p-1)."""
    p = x.p
    acc = P.from_frac(p, 1, K)
    term = P.from_frac(p, 1, K)
    n = 1
    while True:
        term = term * x / P.from_frac(p, n, K + 10)
        if term.is_zero() or term.v > K + 2:
            break
        acc = acc + term
        n += 1
        if n > 20*K:
            break
    return acc

def c_p_formula(p, K, mmax=None):
    """2 * exp( - sum_{m odd>=3} zeta_p(m)(2^m-2)/m * p^m/(1-p^m) )  to K digits."""
    mmax = mmax or (K + 3)
    tot = P.zero(p)
    for m in range(3, mmax+1, 2):
        z = zoo.zeta_p_val(m, p, K + 4)
        coef = Fr(-(2**m - 2), m) * Fr(p**m, 1 - p**m)
        t = z * P.from_frac(p, coef, K + 4)
        if t.is_zero() or t.v > K + 2:
            continue
        tot = tot + t
    return exp_p(tot, K) * P.from_frac(p, 2, K), tot

if __name__ == "__main__":
    for p in [int(x) for x in sys.argv[1:]] or [5, 7, 11, 13]:
        smax = {5: 9, 7: 7, 11: 6, 13: 5}[p]
        K = 3*(smax+1)
        cb = cbin_tower(p, smax, K + 6)
        direct = cb[smax].trunc(K)
        for s in range(1, smax+1):
            assert cb[s].agree(cb[s-1]) >= 3*s, (p, s, cb[s].agree(cb[s-1]))
        form, arg = c_p_formula(p, K)
        d = direct - form
        print("p=%-3d certified digits %d" % (p, K))
        print("   c_p direct  =", direct.trunc(14))
        print("   c_p formula =", form.trunc(14))
        print("   >>> AGREE to %s digits (of %d certified)"
              % ("ALL" if d.is_zero() else d.v, K))
        # how much of it is zeta_p(3) alone?
        z3 = zoo.zeta_p_val(3, p, K + 4)
        only3 = exp_p(z3 * P.from_frac(p, Fr(-6, 3) * Fr(p**3, 1 - p**3), K+4), K) * P.from_frac(p, 2, K)
        d3 = direct - only3
        print("   truncating the series after zeta_p(3): agrees to %s digits"
              % ("ALL" if d3.is_zero() else d3.v))
