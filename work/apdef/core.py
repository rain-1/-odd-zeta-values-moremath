"""Core exact arithmetic for the Apery zeta(3) defect study.

    A(n,k) = C(n,k)^2 C(n+k,k)^2
    a_n    = sum_k A(n,k)                       (Apery numbers 1,5,73,1445,...)
    b_n    = sum_k A(n,k) (2 H^(3)_n - H^(3)_k) (Lean: apery_b_harmonic_closed_form)

Both satisfy  m^3 u_m = P(m-1) u_{m-1} - (m-1)^3 u_{m-2},
P(n) = 34n^3+51n^2+27n+5,  so  P(m-1) = 34m^3-51m^2+27m-5.
  a: a_0=1, a_1=5      b: b_0=0, b_1=6
Everything exact (int / Fraction).
"""
from fractions import Fraction as F
from math import comb
from functools import lru_cache

BIG = 10 ** 9


def Pshift(m):
    """P(m-1) = 34m^3 - 51m^2 + 27m - 5"""
    return 34 * m ** 3 - 51 * m ** 2 + 27 * m - 5


# ---------------------------------------------------------------- ladders
_a = [1, 5]
_b = [F(0), F(6)]


def _extend(N):
    while len(_a) <= N:
        m = len(_a)
        _a.append((Pshift(m) * _a[m - 1] - (m - 1) ** 3 * _a[m - 2]) // m ** 3)
    while len(_b) <= N:
        m = len(_b)
        _b.append((Pshift(m) * _b[m - 1] - F((m - 1) ** 3) * _b[m - 2]) / m ** 3)


def av(n):
    _extend(n)
    return _a[n]


def bv(n):
    _extend(n)
    return _b[n]


# ---------------------------------------------------------------- direct sums
def A(n, k):
    return comb(n, k) ** 2 * comb(n + k, k) ** 2


@lru_cache(maxsize=None)
def Hs(m, r):
    """H^(r)_m = sum_{j<=m} j^-r"""
    return sum((F(1, j ** r) for j in range(1, m + 1)), F(0))


def a_direct(n):
    return sum(A(n, k) for k in range(n + 1))


def b_direct(n):
    h = Hs(n, 3)
    return sum(A(n, k) * (2 * h - Hs(k, 3)) for k in range(n + 1))


# ---------------------------------------------------------------- p-adic utils
def vp(x, p):
    if x == 0:
        return BIG
    if isinstance(x, int):
        n, d = x, 1
    else:
        n, d = x.numerator, x.denominator
    v = 0
    while n % p == 0:
        n //= p; v += 1
    while d % p == 0:
        d //= p; v -= 1
    return v


def modpk(x, p, k):
    """image of a p-integral rational in Z/p^k; None if not p-integral"""
    if isinstance(x, int):
        return x % p ** k
    n, d = x.numerator, x.denominator
    if d % p == 0:
        return None
    m = p ** k
    return n % m * pow(d % m, -1, m) % m


def modp(x, p):
    return modpk(x, p, 1)


# ---------------------------------------------------------------- linear algebra
def rank_fp(M, p):
    M = [[x % p for x in row] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c]), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][c], -1, p)
        M[r] = [x * iv % p for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def rref_fp(M, p):
    """returns (rref rows, pivot columns)"""
    M = [[x % p for x in row] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    r = 0
    piv_cols = []
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c]), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][c], -1, p)
        M[r] = [x * iv % p for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(cols)]
        piv_cols.append(c)
        r += 1
        if r == rows:
            break
    return M[:r], piv_cols
