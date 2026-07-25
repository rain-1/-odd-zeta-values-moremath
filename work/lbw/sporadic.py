"""The 15 sporadic Apery-like sequences (Malik-Straub Tables 1,2 = arXiv:1508.00297)
and their canonical secondary solutions B(n)  [B(0)=0, B(1)=1, recurrence for n>=1].

Recurrence (2):  (n+1)^2 u_{n+1} = (a n^2 + a n + b) u_n - c n^2 u_{n-1}
Recurrence (3):  (n+1)^3 u_{n+1} = (2n+1)(a n^2 + a n + b) u_n - n(c n^2 + d) u_{n-1}
"""
from fractions import Fraction as F
from math import comb, factorial

# ---------------------------------------------------------------- sequence table
# name, family(2 or 3), params, binomial-sum lambda (or None)

def _franel(n):        return sum(comb(n,k)**3 for k in range(n+1))
def _apery2(n):        return sum(comb(n,k)**2*comb(n+k,n) for k in range(n+1))
def _C(n):             return sum(comb(n,k)**2*comb(2*k,k) for k in range(n+1))
def _E(n):             return sum(comb(n,k)*comb(2*k,k)*comb(2*(n-k),n-k) for k in range(n+1))
def _B(n):             return sum((-1)**k*3**(n-3*k)*comb(n,3*k)*factorial(3*k)//factorial(k)**3
                                  for k in range(n//3+1))
def _F(n):             return sum((-1)**k*8**(n-k)*comb(n,k)*sum(comb(k,l)**3 for l in range(k+1))
                                  for k in range(n+1))
def _delta(n):         return sum((-1)**k*3**(n-3*k)*comb(n,3*k)*comb(n+k,n)*factorial(3*k)//factorial(k)**3
                                  for k in range(n//3+1))
def gbin(m, k):
    """generalized binomial C(m,k), k>=0 integer, m any integer."""
    if k < 0: return 0
    if m >= 0: return comb(m, k) if k <= m else 0
    num = 1
    for i in range(k): num *= (m - i)
    return num // factorial(k)

def _eta(n):
    if n == 0: return 1
    return sum((-1)**k*comb(n,k)**3*(gbin(4*n-5*k-1,3*n)+gbin(4*n-5*k,3*n))
               for k in range(n//5+1))
def _alpha(n):         return sum(comb(n,k)**2*comb(2*k,k)*comb(2*(n-k),n-k) for k in range(n+1))
def _eps(n):           return sum(comb(n,k)**2*comb(2*k,n)**2 for k in range(n+1))
def _zeta_(n):         return sum(comb(n,k)**2*comb(n,l)*comb(k,l)*comb(k+l,n)
                                  for k in range(n+1) for l in range(n+1))
def _gamma(n):         return sum(comb(n,k)**2*comb(n+k,n)**2 for k in range(n+1))
def _s7(n):            return sum(comb(n,k)**2*comb(n+k,k)*comb(2*k,n) for k in range(n+1))
def _s10(n):           return sum(comb(n,k)**4 for k in range(n+1))
def _s18(n):
    if n == 0: return 1
    return sum((-1)**k*comb(n,k)*comb(2*k,k)*comb(2*(n-k),n-k)*
               (comb(2*n-3*k-1,n)+comb(2*n-3*k,n)) for k in range(n//3+1))

SEQS = [
    # label,   fam, params,            binomial sum,  Zagier/ASZ note
    ("A",      2, (7, 2, -8),          _franel,  "Franel  sum C(n,k)^3           [Zagier A = ASZ (a)]"),
    ("B",      2, (9, 3, 27),          _B,       "sum (-1)^k 3^(n-3k) C(n,3k)(3k)!/k!^3  [Zagier B = (f)]"),
    ("C",      2, (10, 3, 9),          _C,       "sum C(n,k)^2 C(2k,k)           [Zagier C = (c)]"),
    ("D",      2, (11, 3, -1),         _apery2,  "Apery zeta(2)  sum C(n,k)^2C(n+k,n)  [Zagier D = (b)]"),
    ("E",      2, (12, 4, 32),         _E,       "sum C(n,k)C(2k,k)C(2(n-k),n-k) [Zagier E = (d)]"),
    ("F",      2, (17, 6, 72),         _F,       "sum (-1)^k 8^(n-k) C(n,k) sum_l C(k,l)^3 [Zagier F = (g)]"),
    ("alpha",  3, (10, 4, 64, 0),      _alpha,   "Domb  sum C(n,k)^2C(2k,k)C(2(n-k),n-k)"),
    ("gamma",  3, (17, 5, 1, 0),       _gamma,   "Apery zeta(3)  sum C(n,k)^2C(n+k,n)^2"),
    ("delta",  3, (7, 3, 81, 0),       _delta,   "Almkvist-Zudilin  sum (-1)^k3^(n-3k)C(n,3k)C(n+k,n)(3k)!/k!^3"),
    ("eps",    3, (12, 4, 16, 0),      _eps,     "sum C(n,k)^2 C(2k,n)^2"),
    ("zeta",   3, (9, 3, -27, 0),      _zeta_,   "sum C(n,k)^2C(n,l)C(k,l)C(k+l,n)"),
    ("eta",    3, (11, 5, 125, 0),     _eta,     "sum (-1)^k C(n,k)^3 (C(4n-5k-1,3n)+C(4n-5k,3n))"),
    ("s7",     3, (13, 4, -27, 3),     _s7,      "Cooper s7  sum C(n,k)^2C(n+k,k)C(2k,n)"),
    ("s10",    3, (6, 2, -64, 4),      _s10,     "Cooper s10 sum C(n,k)^4"),
    ("s18",    3, (14, 6, 192, -12),   _s18,     "Cooper s18 (see eq (s18))"),
]

def coeffs(fam, par):
    """return (P(n), Q(n)) with (n+1)^e u_{n+1} = P(n) u_n - Q(n) u_{n-1}, e=2 or 3."""
    if fam == 2:
        a, b, c = par
        return (lambda n: a*n*n + a*n + b), (lambda n: c*n*n), 2
    else:
        a, b, c, d = par
        return (lambda n: (2*n+1)*(a*n*n + a*n + b)), (lambda n: n*(c*n*n + d)), 3

def gen_A(fam, par, N):
    P, Q, e = coeffs(fam, par)
    u = [F(1)]          # u[0] = A(0) = 1 ; A(-1)=0
    prev = F(0)
    for n in range(0, N):
        nxt = (P(n)*u[n] - Q(n)*prev) / F((n+1)**e)
        prev = u[n]; u.append(nxt)
    return u

def gen_B(fam, par, N):
    P, Q, e = coeffs(fam, par)
    u = [F(0), F(1)]    # B(0)=0, B(1)=1 ; recurrence for n>=1
    for n in range(1, N):
        nxt = (P(n)*u[n] - Q(n)*u[n-1]) / F((n+1)**e)
        u.append(nxt)
    return u
