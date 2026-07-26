"""STRUCTURAL reduction of target 2 (the zeta(2)/compact-weight-3 bridge),
following the mechanism of Z5CF_BARNES section 7.2.

Notation (section 7.2):  A_kl = C22, B_kl = C12, C_kl = C21, D_kl = C11,
    A = kappa T,  B = kappa T L_k,  C = kappa T L_l,  D = kappa T (L_k L_l - C_2),
    kappa = (-1)^n / n!.
After the Barnes translation x = s+n+1, y = t+n+1,

    R_n(x,y) = prod_{i=1}^n (x-i) prod_{i=1}^n (y-i) prod_{i=1}^n (x+y-i)
               / [ prod_{i=0}^n (x+i)^2  prod_{i=0}^n (y+i)^2 ].

Double-pole part in x:   P_k(y) = lim_{x->-k}(x+k)^2 R_n = g_k(y)
Simple-pole part in x:   Q_k(y) = d/dx[(x+k)^2 R_n]|_{x=-k} = g_k(y) Lambda_k(y)
with
    g_k(y) = c_k prod_{i=1}^n (y-i) prod_{i=1}^n (y-k-i) / prod_{i=0}^n (y+i)^2,
    c_k    = prod_{i=1}^n(-k-i) / prod_{i=0,i!=k}^n (i-k)^2 ,
    Lambda_k(y) = -sum_{i=1}^n 1/(k+i) + sum_{i=1}^n 1/(y-k-i)
                  - 2 sum_{i=0,i!=k}^n 1/(i-k).

Partial fractions in y:
    g_k(y) = sum_l [ A_kl/(y+l)^2 + C_kl/(y+l) ],
    Q_k(y) = sum_l [ B_kl/(y+l)^2 + D_kl/(y+l) ].

CLAIMED VANISHING (this file checks both exactly):
    (V1)  g_k(j) = 0   for 1 <= j <= n+k            [both numerator products]
    (V2)  Q_k(j) = 0   for 1 <= j <= k              [Lambda_k has no pole there]

CONSEQUENCE (derived in the report):

  sum_{k,l} T coeff_zeta2(W_B)
      = -4 sum_{k,l} T H^(3)_{k+l}  -  sum_{k,l} T (L_k+L_l) H^(2)_{k+l} .

because the only two terms that are not already of that shape combine into
  -2 sum_k sum_{j=1}^{k} Q_k(j) = 0.
"""
import sys
from fractions import Fraction as Fr

import evalq as E
import o0core as C
import weights as W
import w_check as WC


# --------------------------------------------------------- exact g_k, Q_k ---
def ck(n, k):
    num = Fr(1)
    for i in range(1, n + 1):
        num *= Fr(-k - i)
    den = Fr(1)
    for i in range(0, n + 1):
        if i != k:
            den *= Fr((i - k) ** 2)
    return num / den


def g(n, k, y):
    """g_k(y) at a rational point y (must avoid y = -0..-n)."""
    v = ck(n, k)
    for i in range(1, n + 1):
        v *= Fr(y - i)
    for i in range(1, n + 1):
        v *= Fr(y - k - i)
    for i in range(0, n + 1):
        v /= Fr((y + i) ** 2)
    return v


def Lam(n, k, y):
    s = Fr(0)
    for i in range(1, n + 1):
        s -= Fr(1, k + i)
    for i in range(1, n + 1):
        s += Fr(1, y - k - i)
    for i in range(0, n + 1):
        if i != k:
            s -= 2 * Fr(1, i - k)
    return s


def Q(n, k, y):
    return g(n, k, y) * Lam(n, k, y)


# ------------------------------------------------------ partial-fraction ---
def kappa(n):
    from math import factorial
    return Fr((-1) ** n, factorial(n))


def coefs(n, k, l):
    """A,B,C,D from section 2 of Z5CF_BARNES."""
    kap = kappa(n)
    T = E.T(n, k, l)
    A_ = lambda r, x: E.Hs(n + x, r) - E.Hs(x, r)
    B_ = lambda r, x: E.Hs(n - x, r) - E.Hs(x, r)
    C1 = E.Hs(n + k + l, 1) - E.Hs(k + l, 1)
    C2 = E.Hs(n + k + l, 2) - E.Hs(k + l, 2)
    Lk = -A_(1, k) - C1 - 2 * B_(1, k)
    Ll = -A_(1, l) - C1 - 2 * B_(1, l)
    return kap * T, kap * T * Lk, kap * T * Ll, kap * T * (Lk * Ll - C2)


def check_partial_fractions(nmax=4):
    bad = []
    for n in range(nmax + 1):
        for k in range(n + 1):
            for y in (Fr(1, 3), Fr(5, 7), Fr(-1, 5), Fr(11, 4)):
                gv = qv = Fr(0)
                for l in range(n + 1):
                    A, B, Cc, D = coefs(n, k, l)
                    gv += A / (y + l) ** 2 + Cc / (y + l)
                    qv += B / (y + l) ** 2 + D / (y + l)
                if gv != g(n, k, y):
                    bad.append(('g', n, k, y))
                if qv != Q(n, k, y):
                    bad.append(('Q', n, k, y))
    print('partial fractions of g_k, Q_k vs the C22/C12/C21/C11 table, n<=%d : %s'
          % (nmax, 'PASS' if not bad else 'FAIL %s' % bad[:3]))
    return not bad


def check_vanishing(nmax=8):
    bad1 = bad2 = []
    b1, b2 = [], []
    for n in range(nmax + 1):
        for k in range(n + 1):
            for j in range(1, n + k + 1):
                if g(n, k, j) != 0:
                    b1.append((n, k, j))
            for j in range(1, k + 1):
                if Q(n, k, j) != 0:
                    b2.append((n, k, j))
    print('(V1) g_k(j)=0 for 1<=j<=n+k, n<=%d : %s'
          % (nmax, 'PASS' if not b1 else 'FAIL %s' % b1[:3]))
    print('(V2) Q_k(j)=0 for 1<=j<=k,   n<=%d : %s'
          % (nmax, 'PASS' if not b2 else 'FAIL %s' % b2[:3]))
    return not b1 and not b2


# ---------------------------------------------------------- the reduction ---
def coeff_z2_el():
    """coeff_zeta2(W_B) as a bare module element, using [z2]I22 = -4 H3_{k+l}"""
    from o0core import el_add, el_mul, el_scale, lname
    lk, ll = W.Lk(), W.Ll()
    I22 = {(lname(3, 'kl'),): Fr(-4)}
    I12 = el_add({(lname(2, 'l'),): Fr(1)}, {(lname(2, 'kl'),): Fr(1)}, -2)
    I21 = el_add({(lname(2, 'k'),): Fr(1)}, {(lname(2, 'kl'),): Fr(1)}, -2)
    I11 = el_add(el_add({(lname(1, 'k'),): Fr(1)}, {(lname(1, 'l'),): Fr(1)}),
                 {(lname(1, 'kl'),): Fr(1)}, -2)
    out = I22
    out = el_add(out, el_mul(lk, I12))
    out = el_add(out, el_mul(ll, I21))
    out = el_add(out, el_mul(el_add(el_mul(lk, ll), W.Cr(2), -1), I11))
    return {m: c for m, c in out.items() if c != 0}


def reduced_el():
    """-4 H3_{k+l} - (L_k+L_l) H2_{k+l}"""
    from o0core import el_add, el_mul, lname
    out = {(lname(3, 'kl'),): Fr(-4)}
    out = el_add(out, el_mul(W.w_cal(), {(lname(2, 'kl'),): Fr(1)}), -1)
    return out


def check_reduction(nmax=7):
    """the claimed identity of WEIGHTED SUMS (not cellwise)."""
    a = coeff_z2_el()
    b = reduced_el()
    rows = []
    for n in range(nmax + 1):
        sa = E.weighted_sum(a, n)
        sb = E.weighted_sum(b, n)
        rows.append((n, sa, sb, sa == sb))
    ok = all(r[3] for r in rows)
    print('reduction  sum T coeff_z2(W_B) == -4 sum T H3_{k+l} - sum T (L_k+L_l) H2_{k+l}')
    for n, sa, sb, o in rows:
        print('   n=%d : %s' % (n, 'PASS' if o else 'FAIL %s vs %s' % (sa, sb)))
    return ok


def check_cellwise_z2(nmax=5):
    """is the bare formula for coeff_zeta2(W_B) right CELLWISE?"""
    a = coeff_z2_el()
    bad = []
    for n in range(nmax + 1):
        for k in range(n + 1):
            for l in range(n + 1):
                got = E.el_val(a, n, k, l)
                Lk = E.el_val(W.Lk(), n, k, l)
                Ll = E.el_val(W.Ll(), n, k, l)
                C2 = E.el_val(W.Cr(2), n, k, l)
                want = (WC.icoef(k, l, 2, 2)['z2']
                        + Lk * WC.icoef(k, l, 1, 2)['z2']
                        + Ll * WC.icoef(k, l, 2, 1)['z2']
                        + (Lk * Ll - C2) * WC.icoef(k, l, 1, 1)['z2'])
                if got != want:
                    bad.append((n, k, l))
    print('coeff_zeta2(W_B) bare formula, cellwise n<=%d : %s'
          % (nmax, 'PASS' if not bad else 'FAIL %s' % bad[:3]))
    return not bad


if __name__ == '__main__':
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    check_partial_fractions(4)
    check_vanishing(8)
    check_cellwise_z2(4)
    check_reduction(nmax)
