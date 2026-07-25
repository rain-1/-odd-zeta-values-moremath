"""T1: p-adic tower limits for the classical Apery zeta(3) pair.

alpha_n = (n!)^3 a_n,  beta_n = (n!)^3 b_n  satisfy the INTEGER recurrence
    u_{n+1} = (34n^3+51n^2+27n+5) u_n - n^6 u_{n-1},
  alpha_0=1, alpha_1=5;  beta_0=0, beta_1=6.
(derived from Apery's (n+1)^3 u_{n+1} = (34n^3+..) u_n - n^3 u_{n-1}.)
f(n) := b_n/a_n = beta_n/alpha_n  -- exact rational, no factorials needed.
"""
import sys, json, pickle
from padic import vp, digits, dstr, agree

def collect(NMAX, want):
    """run the integer recurrence, return {n: (alpha_n, beta_n)} for n in want."""
    want = set(want)
    out = {}
    A0, A1 = 1, 5
    B0, B1 = 0, 6
    if 0 in want: out[0] = (A0, B0)
    if 1 in want: out[1] = (A1, B1)
    for n in range(1, NMAX):
        c = 34*n**3 + 51*n**2 + 27*n + 5
        n6 = n**6
        A0, A1 = A1, c*A1 - n6*A0
        B0, B1 = B1, c*B1 - n6*B0
        if n+1 in want: out[n+1] = (A1, B1)
    return out

def strip(x, p):
    """(v, x/p^v) with p not dividing x/p^v; power-doubling, O(log v) big divisions."""
    if x == 0: return None, 0
    v = 0; k = 1; pk = p
    while True:
        q, r = divmod(x, pk)
        if r: break
        x = q; v += k; k *= 2; pk *= pk
    while k > 1:
        k //= 2; pk = p**k
        q, r = divmod(x, pk)
        if r == 0: x = q; v += k
    return v, x

def fmod(alpha, beta, p, prec):
    """f(n)=beta/alpha as (valuation v, unit u mod p^prec)."""
    if beta == 0: return None
    va, ua = strip(alpha, p)
    vb, ub = strip(beta, p)
    M = p**prec
    return vb - va, ub % M * pow(ua % M, -1, M) % M

def tower_indices(p, NMAX, a):
    ns, s = [], 0
    while a*p**s <= NMAX:
        ns.append((s, a*p**s)); s += 1
    return ns

def branch_indices(p, NMAX, n0, rs):
    """branch n_{s} = p*n_{s-1} + r_s"""
    ns, n, s = [], n0, 0
    while n <= NMAX:
        ns.append((s, n))
        n = p*n + (rs[s] if s < len(rs) else rs[-1] if rs else 0)
        s += 1
    return ns
