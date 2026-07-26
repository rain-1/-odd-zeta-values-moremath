"""THE ROUTE-DECIDING QUESTION for target 3.

coeff_1(W_B) splits CANONICALLY, straight out of section 8's formula, as

   [1] F^{p,q}_{a,b}
     = (-1)^(p+q-1) sum_i C(p,i) i! (p-i+q-1)!  [1]S_{i+1,p-i+q}(A,d)     <- EULER
     + (-1)^(p+q)   sum_i C(p-1,i)(i+1)!(p+q-2-i)! H_{i+2}(a) H_{p+q-1-i}(a+b)
                                                                          <- PRODUCT

because [1]S_{r,m} consists ENTIRELY of the univariate Euler sums S_{s,j}(b)
and the one bivariate coupled sum U_{r,m}(a,b), while the Z*Z terms are pure
products of ordinary harmonic numbers.  The split is therefore not a fitting
artefact.

QUESTION: does  sum_{k,l} T * (EULER part of coeff_1(W_B))  vanish?
  YES -> target 3 reduces to a pure rational-product identity, the shape that
         has now worked three times (decay / numerator factor / double zero).
  NO  -> the structural route needs a new ingredient.

Also re-verifies both the section-8-derived forms and the Codex FITTED forms
against universal.py at 8 <= k,l < 14, i.e. outside the fit's own check range.
"""
import sys
from fractions import Fraction as Fr
from math import comb, factorial

import evalq as E
import ratpart as RP
import t_struct as S
import weights as W
from alpha import H, S as Sum, U


# ------------------------------------------------------------------ split ---
def F_euler(p, q, a, b):
    out = Fr(0)
    sgn = (-1) ** (p + q - 1)
    for i in range(0, p + 1):
        c = comb(p, i) * factorial(i) * factorial(p - i + q - 1)
        out += sgn * c * RP.rat_S(i + 1, p - i + q, a, b)
    return out


def F_prod(p, q, a, b):
    out = Fr(0)
    sgn = (-1) ** (p + q)
    for i in range(0, p):
        c = comb(p - 1, i) * factorial(i + 1) * factorial(p + q - 2 - i)
        out += sgn * c * H(a, i + 2) * H(a + b, p + q - 1 - i)
    return out


def I_euler(p, q, k, l):
    sgn = (-1) ** (p + q - 2)
    return Fr(sgn, factorial(p - 1) * factorial(q - 1)) * (
        F_euler(p, q, k, l) + F_euler(q, p, l, k))


def I_prod(p, q, k, l):
    sgn = (-1) ** (p + q - 2)
    return Fr(sgn, factorial(p - 1) * factorial(q - 1)) * (
        F_prod(p, q, k, l) + F_prod(q, p, l, k))


# --------------------------------------------------------- Codex fitted r* --
def r11_fit(k, l):
    return ((H(k + l, 1) - H(k, 1) - H(l, 1)) * (H(k, 2) + H(l, 2))
            - H(k, 3) - H(l, 3) + U(k, l, 1, 2) + U(l, k, 1, 2))


def r12_fit(k, l):
    return (-2 * (H(k, 1) + H(l, 1) - H(k + l, 1)) * H(l, 3)
            + H(k, 2) * H(k + l, 2) - H(l, 2) ** 2 / 2
            + H(k + l, 2) * H(l, 2) - Fr(5, 2) * H(l, 4)
            + 2 * Sum(l, 1, 3) - U(k, l, 2, 2))


def r22_fit(k, l):
    return (-2 * (H(k, 2) + H(l, 2)) * (H(k, 3) + H(l, 3))
            + 2 * H(k + l, 3) * (H(k, 2) + H(l, 2))
            + 2 * H(k + l, 2) * (H(k, 3) + H(l, 3))
            - 2 * H(k, 5) - 2 * H(l, 5)
            - 6 * Sum(k, 1, 4) - 6 * Sum(l, 1, 4)
            - 2 * Sum(k, 2, 3) - 2 * Sum(l, 2, 3)
            + 6 * U(k, l, 1, 4) + 6 * U(l, k, 1, 4)
            + 2 * U(k, l, 2, 3) + 2 * U(l, k, 2, 3))


def crosscheck(lo=8, hi=14):
    import w_check as WC
    bd, bf = [], []
    for k in range(lo, hi):
        for l in range(lo, hi):
            want = {pq: WC.icoef(k, l, pq[0], pq[1])['one']
                    for pq in ((1, 1), (1, 2), (2, 1), (2, 2))}
            for pq in want:
                if RP.rat_I(pq[0], pq[1], k, l) != want[pq]:
                    bd.append((k, l) + pq)
            if r11_fit(k, l) != want[(1, 1)]:
                bf.append((k, l, 11))
            if r12_fit(k, l) != want[(1, 2)]:
                bf.append((k, l, 12))
            if r12_fit(l, k) != want[(2, 1)]:
                bf.append((k, l, 21))
            if r22_fit(k, l) != want[(2, 2)]:
                bf.append((k, l, 22))
    print('section-8 DERIVED forms vs universal.py, %d<=k,l<%d : %s'
          % (lo, hi, 'PASS' if not bd else 'FAIL %s' % bd[:4]))
    print('Codex FITTED  forms vs universal.py, %d<=k,l<%d : %s'
          % (lo, hi, 'PASS' if not bf else 'FAIL %s' % bf[:4]))
    return not bd and not bf


# ------------------------------------------------------------- the question -
def euler_sum(n):
    """kappa * sum_{k,l} T * (EULER part of coeff_1(W_B))"""
    kap = S.kappa(n)
    lk, ll = W.Lk(), W.Ll()
    tot = Fr(0)
    for k in range(n + 1):
        for l in range(n + 1):
            T = E.T(n, k, l)
            Lk = E.el_val(lk, n, k, l)
            Ll = E.el_val(ll, n, k, l)
            C2 = E.el_val(W.Cr(2), n, k, l)
            tot += T * (I_euler(2, 2, k, l)
                        + Lk * I_euler(1, 2, k, l)
                        + Ll * I_euler(2, 1, k, l)
                        + (Lk * Ll - C2) * I_euler(1, 1, k, l))
    return kap * tot


def prod_sum(n):
    kap = S.kappa(n)
    lk, ll = W.Lk(), W.Ll()
    tot = Fr(0)
    for k in range(n + 1):
        for l in range(n + 1):
            T = E.T(n, k, l)
            Lk = E.el_val(lk, n, k, l)
            Ll = E.el_val(ll, n, k, l)
            C2 = E.el_val(W.Cr(2), n, k, l)
            tot += T * (I_prod(2, 2, k, l)
                        + Lk * I_prod(1, 2, k, l)
                        + Ll * I_prod(2, 1, k, l)
                        + (Lk * Ll - C2) * I_prod(1, 1, k, l))
    return kap * tot


if __name__ == '__main__':
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    crosscheck(8, 14)
    print()
    print('EULER-PART T-weighted sums (kappa * sum T * Euler part of coeff_1):')
    for n in range(nmax + 1):
        v = euler_sum(n)
        print('   n=%d : %s%s' % (n, v, '   <-- ZERO' if v == 0 else ''),
              flush=True)
