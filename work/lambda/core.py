"""Core exact machinery for the Lambda hunt (task M1).

Apery zeta(3) pair via the INTEGER recurrence  u_{n+1} = c_n u_n - n^6 u_{n-1},
c_n = 34n^3+51n^2+27n+5,  alpha_n = (n!)^3 a_n,  beta_n = (n!)^3 b_n,
so f(n) = b_n/a_n = beta_n/alpha_n exactly.   [validated in PADIC_SEAM.md]

Everything exact: Fractions for small n, ints mod p^K for deep towers.
"""
from fractions import Fraction as Fr
from math import comb
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "padic_seam"))

# ---------------------------------------------------------------- p-adic basics
def vp(x, p):
    if x == 0:
        return None
    if isinstance(x, int):
        num, den = x, 1
    else:
        num, den = x.numerator, x.denominator
    v = 0
    while num % p == 0:
        num //= p; v += 1
    while den % p == 0:
        den //= p; v -= 1
    return v

def frac_mod(x, p, prec):
    M = p**prec
    num, den = (x, 1) if isinstance(x, int) else (x.numerator, x.denominator)
    assert den % p != 0, "not p-integral: %s" % x
    return num % M * pow(den, -1, M) % M

def digits(r, p, prec):
    d = []
    for _ in range(prec):
        d.append(r % p); r //= p
    return d

def dstr(r, p, prec):
    return " ".join(str(x) for x in digits(r % p**prec, p, prec))

def agree(x, y, p, cap):
    """number of leading p-adic digits on which x == y (ints mod p^cap)."""
    d = (x - y) % p**cap
    if d == 0:
        return cap
    v = 0
    while d % p == 0:
        d //= p; v += 1
    return v

def vp_int_mod(x, p, cap):
    """valuation of x mod p^cap (returns cap if x==0 mod p^cap)."""
    x %= p**cap
    if x == 0:
        return cap
    v = 0
    while x % p == 0:
        x //= p; v += 1
    return v

# ---------------------------------------------------------------- Apery pair
def apery_exact(N):
    """alpha_n, beta_n (exact ints) for n = 0..N.  f(n) = beta/alpha."""
    A = [1, 5]
    B = [0, 6]
    for n in range(1, N):
        c = 34*n**3 + 51*n**2 + 27*n + 5
        A.append(c*A[n] - n**6*A[n-1])
        B.append(c*B[n] - n**6*B[n-1])
    return A, B

def f_exact(N):
    A, B = apery_exact(N)
    return [Fr(B[n], A[n]) if A[n] else None for n in range(N+1)]

def apery_mod(N, M, want):
    """alpha_n, beta_n mod M for n=0..N; returns {n:(alpha,beta)} for n in want."""
    want = set(want)
    a0, a1 = 1 % M, 5 % M
    b0, b1 = 0 % M, 6 % M
    out = {}
    if 0 in want: out[0] = (a0, b0)
    if 1 in want: out[1] = (a1, b1)
    for n in range(1, N):
        c = 34*n**3 + 51*n**2 + 27*n + 5
        n6 = n**6
        a0, a1 = a1, (c*a1 - n6*a0) % M
        b0, b1 = b1, (c*b1 - n6*b0) % M
        if n+1 in want:
            out[n+1] = (a1, b1)
    return out

# --------------------------------------------------------- generic Apery-like
# (n+1)^2 u_{n+1} = (a n^2 + a n + b) u_n - c n^2 u_{n-1}         (R2), weight 2
# (n+1)^3 u_{n+1} = (2n+1)(a n^2+a n+b) u_n - n(c n^2 + d) u_{n-1} (R3), weight 3
def gen_mod(kind, par, N, M, want, Binit=None):
    """Integer-normalised (u_n -> (n!)^k u_n) recurrences mod M.
       kind=2: v_{n+1} = P(n) v_n - c n^4 v_{n-1},  P(n)=a n^2+a n+b
       kind=3: v_{n+1} = (2n+1)P(n) v_n - n(c n^2+d) n^6/n^3 ... (see below)
       Returns {n:(A,B)} with f(n) = B/A."""
    want = set(want)
    if kind == 2:
        aa, bb, cc = par
        # v_n = (n!)^2 u_n:  v_{n+1} = P(n) v_n - c n^4 v_{n-1}
        A = [1 % M, bb % M]
        Bv = [0 % M, 1 % M]
        step = lambda n: (aa*n*n + aa*n + bb, cc*n**4)
    else:
        aa, bb, cc, dd = par
        # v_n = (n!)^3 u_n:  v_{n+1} = (2n+1)P(n) v_n - n(c n^2+d) n^6/n^3 v_{n-1}
        #   original: (n+1)^3 u_{n+1} = (2n+1)P u_n - n(cn^2+d) u_{n-1}
        #   times (n!)^3:  v_{n+1} = (2n+1)P v_n - n(cn^2+d) n^3 v_{n-1}
        A = [1 % M, bb % M]
        Bv = [0 % M, 1 % M]
        step = lambda n: ((2*n+1)*(aa*n*n + aa*n + bb), n*(cc*n*n + dd)*n**3)
    out = {}
    if 0 in want: out[0] = (A[0], Bv[0])
    if 1 in want: out[1] = (A[1], Bv[1])
    a0, a1 = A
    b0, b1 = Bv
    for n in range(1, N):
        P, Q = step(n)
        a0, a1 = a1, (P*a1 - Q*a0) % M
        b0, b1 = b1, (P*b1 - Q*b0) % M
        if n+1 in want:
            out[n+1] = (a1, b1)
    return out

def gen_exact(kind, par, N):
    if kind == 2:
        aa, bb, cc = par
        A = [1, bb]; Bv = [0, 1]
        for n in range(1, N):
            P = aa*n*n + aa*n + bb; Q = cc*n**4
            A.append(P*A[n] - Q*A[n-1]); Bv.append(P*Bv[n] - Q*Bv[n-1])
    else:
        aa, bb, cc, dd = par
        A = [1, bb]; Bv = [0, 1]
        for n in range(1, N):
            P = (2*n+1)*(aa*n*n + aa*n + bb); Q = n*(cc*n*n + dd)*n**3
            A.append(P*A[n] - Q*A[n-1]); Bv.append(P*Bv[n] - Q*Bv[n-1])
    return A, Bv

def vp_fact(n, p):
    """v_p(n!)"""
    s = 0; q = p
    while q <= n:
        s += n//q; q *= p
    return s
