"""The tower-harmonic constant.

b_n = a_n H_3(n) + c_n  (Apery's classical formula), so
   Lambda_a = lim p^{3s} f(a p^s) = h_p(a) + C_p(a),
   h_p(a) := lim_s p^{3s} H_3(a p^s),   C_p(a) := lim_s p^{3s} c_{n_s}/a_{n_s}.

EXACT identity (no limit needed):  p^{3s} H_3(a p^s) = sum_{i=0}^{s} p^{3i} S_i(a),
   S_i(a) = sum_{k <= a p^i, p !| k} k^{-3},
because the p-divisible layer of H_3 contributes p^{-3} H_3(a p^{s-1}).
Hence   h_p(a) = sum_{i>=0} p^{3i} S_i(a)   (convergent: v_p(S_i) grows like i/2).
Only i < K/4 matters for K digits, since S_i = 0 mod p^{N} whenever i >= N.
"""
import sys
from fractions import Fraction as Fr
from pnum import P

def S_i(a, i, p, K):
    """sum_{k <= a p^i, p !| k} k^{-3}  mod p^K   (exact, p-integral)."""
    M = p**K
    tot = 0
    n = a * p**i
    for k in range(1, n+1):
        if k % p:
            tot += pow(k*k*k % M, -1, M)
    return tot % M

def h_p(a, p, K, verbose=False):
    """the tower-harmonic constant, to K digits.  Exact."""
    acc = P.zero(p)
    i = 0
    while 3*i < K:
        N = K - 3*i
        if i >= N:                       # S_i == 0 mod p^N
            break
        s = P(p, 0, S_i(a, i, p, N), N).rescale(3*i)
        acc = acc + s
        if verbose:
            print("     i=%d v(p^{3i}S_i)=%s" % (i, s.v if not s.is_zero() else "inf"))
        i += 1
    return acc.trunc(K)

def h_direct(a, s, p, K):
    """p^{3s} H_3(a p^s) computed straight from the definition (cross-check)."""
    n = a * p**s
    tot = Fr(0)
    for m in range(1, n+1):
        tot += Fr(1, m**3)
    return P.from_frac(p, tot * Fr(p)**(3*s), K)

if __name__ == "__main__":
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    K = 20
    print("cross-check h_p(a) against p^{3s}H_3(ap^s) for growing s, p=%d" % p)
    for a in (1, 2, 3):
        H = h_p(a, p, K)
        print("  a=%d  h_p = %s" % (a, H))
        for s in range(0, 4):
            d = h_direct(a, s, p, K)
            print("      s=%d  p^{3s}H_3 agrees to %d digits (expect >= %d)"
                  % (s, H.agree(d), 3*(s+1)))
