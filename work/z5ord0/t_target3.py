"""TARGET 3 -- structural triage.

coeff_1(W_B) = [1]I22 + L_k [1]I12 + L_l [1]I21 + (L_k L_l - C_2)[1]I11,
so   sum T coeff_1 = kappa^{-1} [ sum A [1]I22 + 2 sum B [1]I12 + sum D [1]I11 ]
(using C_kl = B_lk and [1]I21(k,l) = [1]I12(l,k), plus D_kl = D_lk).

Structural facts available (all PROVED in Z5CF_BARNES 7.1-7.3):
  (F1) sum_k B_kl = 0 and sum_k D_kl = 0 for each fixed l  (and the mirrors);
  (F2) g_l(j) = 0 for 1 <= j <= n+l;
  (F3) g_l'(j) = 0 for l < j <= n   (DOUBLE zero -- and only double: g_l''(j) != 0).

Consequence of (F1): every additive piece of [1]I12 depending on l ALONE, and
every piece of [1]I11 depending on k alone or l alone, drops out of the
T-weighted sum.  This file measures exactly how much that removes.
"""
import sys
from fractions import Fraction as Fr

import evalq as E
import ratpart as RP
import t_struct as S
import weights as W
from alpha import H, S as Sum, U


def I11(k, l):
    return RP.rat_I(1, 1, k, l)


def I12(k, l):
    return RP.rat_I(1, 2, k, l)


def I22(k, l):
    return RP.rat_I(2, 2, k, l)


def I11_red(k, l):
    """[1]I11 with the univariate pieces (killed by sum_k D = 0) removed."""
    return (-2 * U(k, l, 1, 2) - 2 * U(k, l, 2, 1)
            + 2 * H(k, 2) * H(k + l, 1))


def I12_red(k, l):
    """[1]I12 with the l-only pieces (killed by sum_k B = 0) removed."""
    full = I12(k, l)
    lonly = I12(0, l) - 0  # crude: the l-only part is NOT simply I12(0,l)
    return full


def coeff1_sum(n, use_red=False):
    tot = Fr(0)
    for k in range(n + 1):
        for l in range(n + 1):
            A, B, C, D = S.coefs(n, k, l)
            if use_red:
                tot += A * I22(k, l) + 2 * B * I12(k, l) + D * I11_red(k, l)
            else:
                tot += A * I22(k, l) + 2 * B * I12(k, l) + D * I11(k, l)
    return tot


def direct_sum(n):
    """kappa * sum_{k,l} T coeff_1(W_B), computed cellwise from scratch."""
    kap = S.kappa(n)
    tot = Fr(0)
    lk, ll = W.Lk(), W.Ll()
    for k in range(n + 1):
        for l in range(n + 1):
            T = E.T(n, k, l)
            Lk = E.el_val(lk, n, k, l)
            Ll = E.el_val(ll, n, k, l)
            C2 = E.el_val(W.Cr(2), n, k, l)
            tot += T * (I22(k, l) + Lk * I12(k, l) + Ll * I12(l, k)
                        + (Lk * Ll - C2) * I11(k, l))
    return kap * tot


def target3(n):
    """kappa * [ -1/2 sum T coeff_1(W_B) - sum T w5sym ]  (should be 0)."""
    kap = S.kappa(n)
    w5 = W.compact_w5sym()
    return (-Fr(1, 2) * direct_sum(n)
            - kap * E.weighted_sum(w5, n))


if __name__ == '__main__':
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print('T3 sanity: target 3 holds as a finite statement')
    for n in range(nmax + 1):
        v = target3(n)
        print('   n=%d : %s' % (n, 'PASS' if v == 0 else 'FAIL %s' % v),
              flush=True)
    print('T3 symmetry collapse  sum T coeff_1 == kappa^-1 [A I22 + 2 B I12 + D I11]')
    for n in range(nmax + 1):
        a, b = direct_sum(n), coeff1_sum(n)
        print('   n=%d : %s' % (n, 'PASS' if a == b else 'FAIL %s vs %s' % (a, b)),
              flush=True)
    print('T3 univariate drop in [1]I11 (uses sum_k D = 0):')
    for n in range(nmax + 1):
        a, b = coeff1_sum(n), coeff1_sum(n, use_red=True)
        print('   n=%d : %s' % (n, 'PASS' if a == b else 'FAIL %s vs %s' % (a, b)),
              flush=True)
