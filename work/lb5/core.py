"""Core objects for the LB5 closeout campaign.

Conventions (authoritative: work/PROOF_LB5_CAMPAIGN.md):
  T(n,k,l) = C(n+k,n) C(n,k)^2 C(n+l,n) C(n,l)^2 C(n+k+l,n)
  Q_n = sum_{k,l} T(n,k,l)          (BZ DOUBLE sum; Q_1 = 21)
  P_n, Ph_n = P-hat_n               (exact ladders, n <= 360)

Letters (for fixed n):
  A_r(x) = H^(r)_{n+x} - H^(r)_x
  B_r(x) = H^(r)_{n-x} - H^(r)_x
  C_r    = H^(r)_{n+k+l} - H^(r)_{k+l}
  Hn_r   = H^(r)_n
"""
from fractions import Fraction as F
from math import comb
import json, os, functools

LAD = '/home/ubuntu/fable-episode-2/zeta-math/worthiness/falsify_data/'

@functools.lru_cache(maxsize=None)
def ladders():
    out = {}
    for k in ('Q', 'P', 'Ph'):
        d = json.load(open(LAD + 'ladder_%s.json' % k))
        out[k] = {int(n): F(int(v[0]), int(v[1])) for n, v in d.items()}
    return out

def Q(n):  return ladders()['Q'][n]
def P(n):  return ladders()['P'][n]
def Ph(n): return ladders()['Ph'][n]

def T(n, k, l):
    return (comb(n + k, n) * comb(n, k)**2 * comb(n + l, n) * comb(n, l)**2
            * comb(n + k + l, n))

# ---------- harmonic numbers ----------
_H = {}
def Hs(m, r):
    """H^{(r)}_m for m >= 0, exact Fraction."""
    key = (m, r)
    v = _H.get(key)
    if v is not None:
        return v
    if m <= 0:
        v = F(0)
    else:
        v = Hs(m - 1, r) + F(1, m**r)
    _H[key] = v
    return v

# ---------- w3-hat ----------
def w3hat(n, k, l):
    A = lambda r, x: Hs(n + x, r) - Hs(x, r)
    B = lambda r, x: Hs(n - x, r) - Hs(x, r)
    C1 = Hs(n + k + l, 1) - Hs(k + l, 1)
    return (Hs(n, 3) + A(3, k) + A(3, l)
            - F(1, 4) * (A(2, k) * A(1, k) + A(2, l) * A(1, l))
            - F(3, 4) * (A(2, k) * B(1, k) + A(2, l) * B(1, l))
            - F(3, 8) * (A(2, k) + A(2, l)) * C1
            - F(1, 8) * (A(2, k) * A(1, l) + A(2, l) * A(1, k)))

def Phat_from_w3(n):
    return sum(T(n, k, l) * w3hat(n, k, l)
               for k in range(n + 1) for l in range(n + 1))

def Q_from_T(n):
    return sum(T(n, k, l) for k in range(n + 1) for l in range(n + 1))

# ---------- the certified order-3 BZ recurrence (V6b, normalized) ----------
def a0(n): return 41218*n**3 + 198849*n**2 + 320790*n + 173057
def B8(n):
    return (3874492*n**8 + 59373972*n**7 + 394148190*n**6 + 1481084196*n**5
            + 3447878810*n**4 + 5095855458*n**3 + 4673546679*n**2
            + 2433871008*n + 551502039)
def B9(n):
    return (48802112*n**9 + 967468896*n**8 + 8488000862*n**7 + 43246197636*n**6
            + 140983768422*n**5 + 304912330849*n**4 + 437406946975*n**3
            + 401272692378*n**2 + 213593890911*n + 50257929339)
def c0(n): return (n+1)**5 * (n+2) * a0(n+1)
def c1(n): return -2*(n+2)*B8(n)
def c2(n): return -2*B9(n)
def c3(n): return 2*(n+3)**5*(2*n+5)*a0(n)

def rec_residual(Y, n):
    """c0 Y_n + c1 Y_{n+1} + c2 Y_{n+2} + c3 Y_{n+3}; Y a callable n->Fraction."""
    return c0(n)*Y(n) + c1(n)*Y(n+1) + c2(n)*Y(n+2) + c3(n)*Y(n+3)

def vp(x, p):
    """p-adic valuation of a Fraction (or int)."""
    if x == 0: return 10**9
    x = F(x)
    a, b = x.numerator, x.denominator
    v = 0
    while a % p == 0: a //= p; v += 1
    while b % p == 0: b //= p; v -= 1
    return v
