"""T4: the LSZ zeta_2(5) ledger -- exact denominators of rho_{n,0}, rho_{n,3}.

LSZ recursion (their eq:rec):
 (n+1)^5 r_{n+1} - 32(2n+1)(8n^4+16n^3+20n^2+12n+3) r_n + 2^16 n^5 r_{n-1} = 0.
Initial data from Lemma 15(b): rho_{0,0}=0, rho_{1,0}=-1024; rho_{0,3}=768, rho_{1,3}=73728.
Also rho_n (integer solution) with rho_0=1, rho_1=96 and rho_{n,3}=768 rho_n.
"""
import sys
from fractions import Fraction as F
from math import log, gcd
sys.set_int_max_str_digits(3000000)

def C(n): return 32*(2*n+1)*(8*n**4+16*n**3+20*n**2+12*n+3)

def gen(r0, r1, N):
    out = [F(r0), F(r1)]
    for n in range(1, N):
        out.append((C(n)*out[n] - 2**16*n**5*out[n-1]) / F((n+1)**5))
    return out

def dlog(n):
    """log of lcm(1..n) via sieve"""
    s = 0.0
    sieve = [True]*(n+1)
    for p in range(2, n+1):
        if sieve[p]:
            for q in range(p*p, n+1, p): sieve[q] = False
            k = 1
            while p**(k+1) <= n: k += 1
            s += k*log(p)
    return s

def dn_exp(n):
    """exact d_n = lcm(1..n) as an integer factorisation-free product"""
    from math import isqrt
    res = 1
    sieve = [True]*(n+1)
    for p in range(2, n+1):
        if sieve[p]:
            for q in range(p*p, n+1, p): sieve[q] = False
            k = p
            while k*p <= n: k *= p
            res *= k
    return res

N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
r0 = gen(0, -1024, N)          # rho_{n,0}
r3 = gen(768, 73728, N)        # rho_{n,3}
rho = gen(1, 96, N)            # the integer solution

print("check rho_{n,3} = 768 rho_n :", all(r3[n] == 768*rho[n] for n in range(N)))
print("check rho_n integral        :", all(rho[n].denominator == 1 for n in range(min(N, 200))))
print("check LSZ determinant formula rho_{n,0}rho_{n+1,3}-rho_{n+1,0}rho_{n,3} = 3*2^{16n+18}/(n+1)^5 :",
      all(r0[n]*r3[n+1] - r0[n+1]*r3[n] == F(3*2**(16*n+18), (n+1)**5) for n in range(min(N-1, 60))))

print("\n n   den(rho_{n,0}) vs d_n^5 :  log(den)/n   5*log(d_n)/n   ratio   [LSZ need <5]")
for n in [20, 50, 100, 200, 300, 400, 600, 800, 1000, 1500, 2000]:
    if n >= N: break
    den = r0[n].denominator
    dn = dn_exp(n)
    ok5 = (dn**5) % den == 0
    ok4 = (dn**4) % den == 0
    ok3 = (dn**3) % den == 0
    g = gcd(den, dn**5)
    ld = log(den)
    print("  %4d  d_n^5 kills? %-5s d_n^4? %-5s d_n^3? %-5s | log(den)/n = %.4f  (5 log d_n /n = %.4f)"
          % (n, ok5, ok4, ok3, ld/n, 5*dlog(n)/n))

# per-prime valuations: is v_p(rho_{n,0}) > -5 v_p(d_n) systematically?
print("\n per-prime denominator ledger:  e_p(n) := -v_p(rho_{n,0}),  L_p = floor(log_p n)")
for n in [200, 400, 800]:
    if n >= N: break
    den = r0[n].denominator
    print("  n=%d:" % n, end=" ")
    out = []
    for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        v = 0; d = den
        while d % p == 0: d //= p; v += 1
        L = 0
        while p**(L+1) <= n: L += 1
        out.append("p=%d: e=%d vs 5L=%d" % (p, v, 5*L))
    print("; ".join(out))
