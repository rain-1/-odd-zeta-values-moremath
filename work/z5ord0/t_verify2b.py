"""SENSITIVE checks of the target-2 derivation.

Step (4) of t_verify2.py compares three quantities that are all ZERO, so it
cannot detect an algebra error.  Here every displayed identity has BOTH SIDES
GENERICALLY NONZERO, so an off-by-one or a wrong symmetry step would show.
"""
import sys
from fractions import Fraction as Fr

import evalq as E
import t_struct as S
import weights as W


def check(tag, rows):
    ok = all(r[-1] for r in rows)
    print('  %-58s %s' % (tag, 'PASS' if ok else 'FAIL'))
    if not ok:
        for r in rows[:3]:
            if not r[-1]:
                print('     ', r)
    return ok


def s1(nmax=6):
    """cellwise  L_k - L_l = -2 Psi,  Psi = alpha/2 + beta."""
    rows = []
    lk, ll = W.Lk(), W.Ll()
    for n in range(nmax + 1):
        for k in range(n + 1):
            for l in range(n + 1):
                A1 = lambda x: E.Hs(n + x, 1) - E.Hs(x, 1)
                B1 = lambda x: E.Hs(n - x, 1) - E.Hs(x, 1)
                al = A1(k) - A1(l); be = B1(k) - B1(l)
                psi = al / 2 + be
                got = E.el_val(lk, n, k, l) - E.el_val(ll, n, k, l)
                rows.append((n, k, l, got == -2 * psi))
    return check('(S1) L_k - L_l = -2 Psi, cellwise', rows)


def s2(nmax=8):
    """cellwise  H^(r)_{n+k} - H^(r)_{k+l} = sum_{j=l+1}^{n} 1/(k+j)^r"""
    rows = []
    for n in range(nmax + 1):
        for k in range(n + 1):
            for l in range(n + 1):
                for r in (2, 3):
                    s = sum((Fr(1, (k + j) ** r) for j in range(l + 1, n + 1)),
                            Fr(0))
                    rows.append((n, k, l, r,
                                 E.Hs(n + k, r) - E.Hs(k + l, r) == s))
    return check('(S2) H^(r)_{n+k}-H^(r)_{k+l} = sum_{j=l+1}^n (k+j)^-r', rows)


def s3(nmax=7):
    """symmetry reductions -- both sides generically nonzero."""
    r1, r2, r3 = [], [], []
    for n in range(nmax + 1):
        a1 = a2 = Fr(0)
        b1 = b2 = Fr(0)
        c1 = c2 = Fr(0)
        for k in range(n + 1):
            for l in range(n + 1):
                A, B, C, D = S.coefs(n, k, l)
                a1 += A * (E.Hs(n + k, 3) + E.Hs(n + l, 3))
                a2 += 2 * A * E.Hs(n + k, 3)
                b1 += (B - C) * (E.Hs(n + k, 2) - E.Hs(n + l, 2))
                b2 += 2 * B * (E.Hs(n + k, 2) - E.Hs(n + l, 2))
                c1 += (B + C) * E.Hs(k + l, 2)
                c2 += 2 * B * E.Hs(k + l, 2)
        r1.append((n, a1, a2, a1 == a2))
        r2.append((n, b1, b2, b1 == b2))
        r3.append((n, c1, c2, c1 == c2))
    ok = (check('(S3a) sum A (H3_{n+k}+H3_{n+l}) = 2 sum A H3_{n+k}', r1)
          and check('(S3b) sum (B-C)(H2_{n+k}-H2_{n+l}) = 2 sum B (...)', r2)
          and check('(S3c) sum (B+C) H2_{k+l} = 2 sum B H2_{k+l}', r3))
    print('       (sample nonzero values at n=%d: %s , %s , %s)'
          % (nmax, r1[-1][1] != 0, r2[-1][1] != 0, r3[-1][1] != 0))
    return ok


def s4(nmax=7):
    """4 sum A w3sym = 4 sum A H3_{n+k} + 2 sum B (H2_{n+k}-H2_{n+l});
    both sides generically NONZERO."""
    rows = []
    w3 = W.compact_w3sym()
    for n in range(nmax + 1):
        lhs = rhs = Fr(0)
        for k in range(n + 1):
            for l in range(n + 1):
                A, B, C, D = S.coefs(n, k, l)
                lhs += 4 * A * E.el_val(w3, n, k, l)
                rhs += 4 * A * E.Hs(n + k, 3)
                rhs += 2 * B * (E.Hs(n + k, 2) - E.Hs(n + l, 2))
        rows.append((n, lhs, rhs, lhs == rhs))
    ok = check('(S4) 4 sum A w3sym = 4 sum A H3_{n+k} + 2 sum B (H2 diff)', rows)
    print('       (LHS at n=%d is %s -> nonzero: %s)'
          % (nmax, rows[-1][1], rows[-1][1] != 0))
    return ok


def s5(nmax=7):
    """the pieces of Delta separately -- X1 and X2 are generically NONZERO and
    each equals its g'-side counterpart."""
    rows = []
    for n in range(nmax + 1):
        X1 = X2 = Fr(0)
        Y1 = Y2 = Fr(0)
        Bh = Fr(0)
        for k in range(n + 1):
            for l in range(n + 1):
                A, B, C, D = S.coefs(n, k, l)
                X1 += 4 * A * (E.Hs(n + k, 3) - E.Hs(k + l, 3))
                X2 += 2 * B * (E.Hs(n + k, 2) - E.Hs(n + l, 2) - E.Hs(k + l, 2))
                Bh += 2 * B * E.Hs(n + l, 2)
                for j in range(l + 1, n + 1):
                    Y1 += 4 * A / Fr((k + j) ** 3)
                    Y2 += 2 * B / Fr((k + j) ** 2)
        rows.append((n, X1, Y1, X2, Y2 - Bh, Bh,
                     X1 == Y1 and X2 == Y2 - Bh and Bh == 0))
    ok = check('(S5) X1 = Y1 , X2 = Y2 - 2 sum B H2_{n+l} , that term = 0', rows)
    print('       (X1 at n=%d = %s ; X2 = %s ; both nonzero: %s)'
          % (nmax, rows[-1][1], rows[-1][3],
             rows[-1][1] != 0 and rows[-1][3] != 0))
    return ok


if __name__ == '__main__':
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    print('SENSITIVE checks of the target-2 structural derivation')
    ok = all([s1(6), s2(8), s3(nmax), s4(nmax), s5(nmax)])
    print('OVERALL: %s' % ('ALL SENSITIVE CHECKS PASS' if ok else 'FAILURE'))
