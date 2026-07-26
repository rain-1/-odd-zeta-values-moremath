"""INDEPENDENT VERIFICATION of the claimed structural proof of target 2
(Z5CF_BARNES 7.3), step by step.  Everything exact over Q.

Chain to be checked:

 (0)  the Barnes translation:  with x = s+n+1, y = t+n+1,
        R_n = prod_{i=1}^n (x-i)(y-i)(x+y-i) / [prod_{i=0}^n (x+i)^2 (y+i)^2]
      is EXACTLY section 1's
        prod_{j=1}^n(s+j)(t+j) prod_{j=n+2}^{2n+1}(s+t+j)
        / [prod_{j=n+1}^{2n+1}(s+j)^2 (t+j)^2].

 (1)  g_l(x) = lim_{y->-l}(y+l)^2 R_n = c_l P1(x) P2(x) / prod_{i=0}^n (x+i)^2,
      P1 = prod_{r=1}^n (x-r),  P2 = prod_{r=1}^n (x-l-r),
      c_l = prod_{r=1}^n(-l-r) / prod_{i!=l}(i-l)^2  (nonzero),
      and its partial fractions in x are sum_k [A_kl/(x+k)^2 + B_kl/(x+k)].

 (2)  sum_k B_kl = 0 and sum_k D_kl = 0 for every fixed l.

 (3)  DOUBLE ZERO: for l < j <= n, both P1 and P2 vanish at x=j
      (P1 at r=j, needs 1<=j<=n; P2 at r=j-l, needs 1<=j-l<=n), the
      denominator prod_{r=0}^n (j+r)^2 is nonzero for j>=1, so
        g_l(j) = 0  AND  g_l'(j) = 0.

 (4)  the reduction
        Delta := 4 sum A (H3_{n+k}-H3_{k+l}) + 2 sum B (H2_{n+k}-H2_{n+l}-H2_{k+l})
              = sum_l sum_{j=l+1}^n sum_k [4A/(k+j)^3 + 2B/(k+j)^2]
              = -2 sum_l sum_{j=l+1}^n g_l'(j)
      where Delta is exactly
        -4 sum T H3_{k+l} - sum T (L_k+L_l) H2_{k+l} + 4 sum T w3sym
      divided by kappa^{-1}.

 (5)  the target itself, at n = 13..18 (outside the n=0..12 range already
      covered by verify_global.py).
"""
import sys
from fractions import Fraction as Fr
from math import factorial

import evalq as E
import o0core as C
import t_struct as S
import weights as W


# ------------------------------------------------------------------ step 0 --
def R_orig(n, s, t):
    v = Fr(1)
    for j in range(1, n + 1):
        v *= Fr(s + j) * Fr(t + j)
    for j in range(n + 2, 2 * n + 2):
        v *= Fr(s + t + j)
    for j in range(n + 1, 2 * n + 2):
        v /= Fr(s + j) ** 2 * Fr(t + j) ** 2
    return v


def R_xy(n, x, y):
    v = Fr(1)
    for i in range(1, n + 1):
        v *= Fr(x - i) * Fr(y - i) * Fr(x + y - i)
    for i in range(0, n + 1):
        v /= Fr(x + i) ** 2 * Fr(y + i) ** 2
    return v


def step0(nmax=6):
    bad = []
    for n in range(nmax + 1):
        for (a, b) in ((Fr(1, 3), Fr(2, 5)), (Fr(7, 2), Fr(-1, 7)),
                       (Fr(11, 5), Fr(13, 3))):
            x, y = a, b
            s, t = x - n - 1, y - n - 1
            if R_orig(n, s, t) != R_xy(n, x, y):
                bad.append((n, x, y))
    print('(0) Barnes translation of R_n, n<=%d : %s'
          % (nmax, 'PASS' if not bad else 'FAIL %s' % bad[:3]))
    return not bad


# ------------------------------------------------------------------ step 1 --
def step1(nmax=5):
    bad = []
    for n in range(nmax + 1):
        for l in range(n + 1):
            for x in (Fr(1, 3), Fr(9, 4), Fr(-2, 7)):
                lim = R_xy(n, x, -l + Fr(1, 10 ** 6))  # not used; exact below
                # exact limit via the closed form of the residue
                got = S.g(n, l, x)
                # direct: (y+l)^2 R as a rational function evaluated at y=-l
                v = Fr(1)
                for i in range(1, n + 1):
                    v *= Fr(x - i) * Fr(-l - i) * Fr(x - l - i)
                for i in range(0, n + 1):
                    v /= Fr(x + i) ** 2
                for i in range(0, n + 1):
                    if i != l:
                        v /= Fr(i - l) ** 2
                if got != v:
                    bad.append((n, l, x))
    print('(1) closed form of g_l(x) as the double-pole residue, n<=%d : %s'
          % (nmax, 'PASS' if not bad else 'FAIL %s' % bad[:3]))
    return not bad


# ------------------------------------------------------------------ step 2 --
def step2(nmax=9):
    bad = []
    for n in range(nmax + 1):
        for l in range(n + 1):
            sb = sd = Fr(0)
            for k in range(n + 1):
                A, B, Cc, D = S.coefs(n, k, l)
                sb += B
                sd += D
            if sb != 0 or sd != 0:
                bad.append((n, l, sb, sd))
    print('(2) sum_k C12(k,l) = sum_k C11(k,l) = 0, n<=%d : %s'
          % (nmax, 'PASS' if not bad else 'FAIL %s' % bad[:3]))
    return not bad


# ------------------------------------------------------------------ step 3 --
def gprime_pf(n, l, x):
    """g_l'(x) from the partial fractions sum_k [A/(x+k)^2 + B/(x+k)]."""
    v = Fr(0)
    for k in range(n + 1):
        A, B, Cc, D = S.coefs(n, k, l)
        v += -2 * A / Fr(x + k) ** 3 - B / Fr(x + k) ** 2
    return v


def gprime_prod(n, l, x):
    """g_l'(x) from the product form, by the product rule."""
    c = S.ck(n, l)
    P1 = [Fr(x - r) for r in range(1, n + 1)]
    P2 = [Fr(x - l - r) for r in range(1, n + 1)]
    fac = P1 + P2
    N = c
    for f in fac:
        N *= f
    Np = Fr(0)
    for i in range(len(fac)):
        term = c
        for j, f in enumerate(fac):
            if j != i:
                term *= f
        Np += term
    Dd = Fr(1)
    for i in range(0, n + 1):
        Dd *= Fr(x + i) ** 2
    Ddp = Fr(0)
    for i in range(0, n + 1):
        t = Fr(2) * Fr(x + i)
        for j in range(0, n + 1):
            if j != i:
                t *= Fr(x + j) ** 2
        Ddp += t
    return (Np * Dd - N * Ddp) / Dd ** 2


def step3(nmax=9):
    b_pf, b_zero, b_gz = [], [], []
    for n in range(nmax + 1):
        for l in range(n + 1):
            for x in (Fr(1, 3), Fr(9, 4), Fr(-2, 7), Fr(23, 5)):
                if gprime_pf(n, l, x) != gprime_prod(n, l, x):
                    b_pf.append((n, l, x))
            for j in range(1, n + l + 1):
                if S.g(n, l, j) != 0:
                    b_gz.append((n, l, j))
            for j in range(l + 1, n + 1):
                if gprime_pf(n, l, j) != 0:
                    b_zero.append((n, l, j))
    print('(3a) g_l\'(x) partial-fraction form == product form, n<=%d : %s'
          % (nmax, 'PASS' if not b_pf else 'FAIL %s' % b_pf[:3]))
    print('(3b) g_l(j) = 0 for 1<=j<=n+l, n<=%d : %s'
          % (nmax, 'PASS' if not b_gz else 'FAIL %s' % b_gz[:3]))
    print("(3c) g_l'(j) = 0 for l<j<=n  (DOUBLE zero), n<=%d : %s"
          % (nmax, 'PASS' if not b_zero else 'FAIL %s' % b_zero[:3]))
    return not b_pf and not b_zero and not b_gz


# ------------------------------------------------------------------ step 4 --
def delta_direct(n):
    """kappa * [ -4 sum T H3_{kl} - sum T (L_k+L_l) H2_{kl} + 4 sum T w3sym ]"""
    kap = S.kappa(n)
    tot = Fr(0)
    lk, ll = W.Lk(), W.Ll()
    w3 = W.compact_w3sym()
    for k in range(n + 1):
        for l in range(n + 1):
            T = E.T(n, k, l)
            Lk = E.el_val(lk, n, k, l)
            Ll = E.el_val(ll, n, k, l)
            tot += T * (-4 * E.Hs(k + l, 3) - (Lk + Ll) * E.Hs(k + l, 2)
                        + 4 * E.el_val(w3, n, k, l))
    return kap * tot


def delta_middle(n):
    """4 sum A (H3_{n+k}-H3_{k+l}) + 2 sum B (H2_{n+k}-H2_{n+l}-H2_{k+l})"""
    tot = Fr(0)
    for k in range(n + 1):
        for l in range(n + 1):
            A, B, Cc, D = S.coefs(n, k, l)
            tot += 4 * A * (E.Hs(n + k, 3) - E.Hs(k + l, 3))
            tot += 2 * B * (E.Hs(n + k, 2) - E.Hs(n + l, 2) - E.Hs(k + l, 2))
    return tot


def delta_gprime(n):
    """sum_l sum_{j=l+1}^n sum_k [4A/(k+j)^3 + 2B/(k+j)^2] = -2 sum g_l'(j)"""
    tot = Fr(0)
    for l in range(n + 1):
        for j in range(l + 1, n + 1):
            tot += -2 * gprime_pf(n, l, j)
    return tot


def step4(nmax=8):
    rows = []
    for n in range(nmax + 1):
        a, b, c = delta_direct(n), delta_middle(n), delta_gprime(n)
        rows.append((n, a, b, c, a == b and b == c))
    ok = all(r[4] for r in rows)
    print('(4) Delta_direct == Delta_middle == -2 sum_l sum_{j>l} g_l\'(j):')
    for n, a, b, c, o in rows:
        print('    n=%2d : %s   (all three = %s)'
              % (n, 'PASS' if o else 'FAIL %s / %s / %s' % (a, b, c), a))
    return ok


# ------------------------------------------------------------------ step 5 --
def step5(lo=13, hi=18):
    a = S.coeff_z2_el()
    w3 = W.compact_w3sym()
    ok = True
    for n in range(lo, hi + 1):
        lhs = -Fr(1, 4) * E.weighted_sum(a, n)
        rhs = E.weighted_sum(w3, n)
        good = lhs == rhs
        ok = ok and good
        print('    n=%2d : %s' % (n, 'PASS' if good else 'FAIL %s vs %s'
                                  % (lhs, rhs)), flush=True)
    return ok


if __name__ == '__main__':
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    step0(6)
    step1(5)
    step2(9)
    step3(9)
    step4(nmax)
    print('(5) TARGET 2 itself, -1/4 sum T coeff_z2(W_B) == sum T w3sym, n=13..18:')
    step5(13, 18)
