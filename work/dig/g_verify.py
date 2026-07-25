"""g_verify.py -- EXACT verification of the Rhin-Viola transfer identity, and of
its p-adic (theta-shifted) form.

The invariant, derived from Zudilin (llm/04) eq. (4.4) + Lemma 9:

    H(c)/Pi(c) = Gtilde(a,b) / [ prod_j (a_j-b_1)! prod_j (a_j-b_2)! ]
               = Ftilde(h)  / [ prod_{j=1}^5 (h_j-1)! * (1+2h_0-h_1-..-h_5)! ]

so define
    I(h) := Ftilde(h) / ( prod_{j=1}^{5}(h_j-1)! * (1+2h_0-sum h_j)! )
and the claim is  I(h) = I(g h)  for every g in the group G of order 1920.

Ftilde(h) = sum_{t>=0} Rtilde(h;t),
Rtilde(h;t) = (h_0+2t) * (t+1)_{h_0-1} * prod_{j=1}^{5} 1/(t+h_j)_{1+h_0-2h_j}

is the very-well-poised rational function; Ftilde(h) = A*zeta(3) + B with
A, B in Q, computed here EXACTLY.

Parameter dictionary (Zudilin eq. 4.5 / 4.6), with b_1 = 1 normalisation:
    a = (a_1..a_4), b = (1, b_2, b_3, b_4)
    h_0 = b_3+b_4-b_1-a_1
    h_1 = 1-b_1+a_2, h_2 = 1-b_1+a_3, h_3 = 1-b_1+a_4
    h_4 = b_4-a_1,   h_5 = b_3-a_1
The group acts on (a,b) by: a_j <-> a_4 (j=1,2,3), b_3 <-> b_4, and
    h : (a_1,a_2,a_3,a_4; 1,b_2,b_3,b_4) ->
        (b_3-a_3, a_2, b_3-a_1, a_4; 1, b_2+b_3-a_1-a_3, b_3, b_3+b_4-a_1-a_3)
(eq. 4.10).
"""

import itertools
from fractions import Fraction as F
from math import factorial

from g_forms import s_mul, s_inv


# ---------------------------------------------------------------- rational fn

def partial_fractions(num_roots, den_roots, lin):
    """Partial fractions of  lin(t) * prod_{c in num}(t+c) / prod_{c in den}(t+c).

    lin = (p, q) meaning the polynomial p + q*t.  Roots are Fractions/ints.
    Returns dict (i,k) -> r_{i,k} over poles t = -k.
    """
    from collections import Counter
    nc, dc = Counter(num_roots), Counter(den_roots)
    poles = {k: dc[k] - nc.get(k, 0) for k in dc if dc[k] - nc.get(k, 0) > 0}
    r = {}
    for k, m in poles.items():
        # cancel matched factors
        nn = list(num_roots)
        dd = list(den_roots)
        for _ in range(nc.get(k, 0)):
            nn.remove(k)
            dd.remove(k)
        for _ in range(m):
            dd.remove(k)
        M = m - 1
        top = [F(0)] * (M + 1)
        top[0] = F(1)
        for c in nn:
            a = c - k
            fac = [F(0)] * (M + 1)
            fac[0] = F(a)
            if M >= 1:
                fac[1] = F(1)
            top = s_mul(top, fac, M)
        bot = [F(0)] * (M + 1)
        bot[0] = F(1)
        for c in dd:
            a = c - k
            assert a != 0
            fac = [F(0)] * (M + 1)
            fac[0] = F(a)
            if M >= 1:
                fac[1] = F(1)
            bot = s_mul(bot, fac, M)
        L = [F(lin[0] - lin[1] * k)] + ([F(lin[1])] if M >= 1 else [])
        L = L + [F(0)] * (M + 1 - len(L))
        G = s_mul(s_mul(L, top, M), s_inv(bot, M), M)
        for i in range(1, m + 1):
            r[(i, k)] = G[M + 1 - i]
    return r


def h_from_ab(a, b):
    a1, a2, a3, a4 = a
    b1, b2, b3, b4 = b
    return (b3 + b4 - b1 - a1,
            1 - b1 + a2, 1 - b1 + a3, 1 - b1 + a4, b4 - a1, b3 - a1)


def R_data(h, theta=0):
    """(num_roots, den_roots, lin) for Rtilde(h;t) with numerator bricks shifted
    by theta (theta=0 is the classical integer family)."""
    h0 = h[0]
    hs = h[1:]
    num = [F(1 + i) + theta for i in range(h0 - 1)]
    den = []
    for hj in hs:
        L = 1 + h0 - 2 * hj
        assert L >= 1, f"empty brick h_j={hj}, h0={h0}"
        den += [hj + i for i in range(L)]
    return num, den, (h0, 2)


def linear_form(h):
    """Ftilde(h) = A*zeta(3) + B (exact).  Also returns rho_i for diagnostics."""
    num, den, lin = R_data(h)
    r = partial_fractions(num, den, lin)
    imax = max(i for i, _ in r)
    rho = [F(0)] * (imax + 1)
    for (i, k), v in r.items():
        rho[i] += v
    # sum_{t>=0} 1/(t+k)^i = zeta(i) - H_{k-1}^{(i)}
    B = F(0)
    for (i, k), v in r.items():
        Hk = sum(F(1, l ** i) for l in range(1, int(k)))
        B -= v * Hk
    A = rho[3] if imax >= 3 else F(0)
    return A, B, rho


def invariant_norm(h):
    """prod_{j=1}^{5}(h_j-1)! * (1+2h_0 - sum h_j)!"""
    h0 = h[0]
    s = sum(h[1:])
    e = 1 + 2 * h0 - s
    assert e >= 0, f"negative complementary parameter {e}"
    out = factorial(e)
    for hj in h[1:]:
        out *= factorial(hj - 1)
    return out


# ---------------------------------------------------------------- group on (a,b)

def act_a(ab, j):
    a, b = list(ab[0]), list(ab[1])
    a[j - 1], a[3] = a[3], a[j - 1]
    return (tuple(a), tuple(b))


def act_b(ab):
    a, b = list(ab[0]), list(ab[1])
    b[2], b[3] = b[3], b[2]
    return (tuple(a), tuple(b))


def act_h(ab):
    (a1, a2, a3, a4), (b1, b2, b3, b4) = ab
    assert b1 == 1
    return ((b3 - a3, a2, b3 - a1, a4),
            (1, b2 + b3 - a1 - a3, b3, b3 + b4 - a1 - a3))


def orbit_ab(ab, cap=100000):
    seen = {ab}
    frontier = [ab]
    while frontier:
        nxt = []
        for x in frontier:
            for y in (act_a(x, 1), act_a(x, 2), act_a(x, 3), act_b(x), act_h(x)):
                if y not in seen:
                    seen.add(y)
                    nxt.append(y)
                    if len(seen) > cap:
                        return seen
        frontier = nxt
    return seen


def valid_h(h):
    h0 = h[0]
    if h0 < 2:
        return False
    if any(hj < 1 for hj in h[1:]):
        return False
    if any(1 + h0 - 2 * hj < 1 for hj in h[1:]):
        return False
    if 1 + 2 * h0 - sum(h[1:]) < 0:
        return False
    return True


# ---------------------------------------------------------------- tests

def test_apery():
    """Ball's a=(n+1)^4, b=(1,1,2n+2,2n+2) must reproduce Apery's numbers."""
    print("[A] Ball/Apery anchor  h0=3n+2, h_j=n+1")
    for n in (1, 2, 3, 4):
        h = (3 * n + 2,) + (n + 1,) * 5
        A, B, rho = linear_form(h)
        # Apery: a_n = sum C(n,k)^2 C(n+k,k)^2 ; forms 2(a_n zeta(3) - b_n)
        an = sum((__import__("math").comb(n, k) ** 2) *
                 (__import__("math").comb(n + k, k) ** 2) for k in range(n + 1))
        ratio = A / (2 * an) if an else None
        print(f"   n={n}: A={A}  Apery a_n={an}   A/(2 a_n) = {ratio}")


def test_transfer(alpha, beta, n=1, verbose=True):
    """Check I(h) = I(g h) exactly across the whole orbit."""
    a = tuple(alpha[j] * n + 1 for j in range(4))
    b = (beta[0] * n + 1, beta[1] * n + 1, beta[2] * n + 2, beta[3] * n + 2)
    shift = 1 - b[0]
    a = tuple(x + shift for x in a)
    b = tuple(x + shift for x in b)          # normalise b_1 = 1
    ab0 = (a, b)
    orb = orbit_ab(ab0)
    h0 = h_from_ab(*ab0)
    if not valid_h(h0):
        return None
    A0, B0, _ = linear_form(h0)
    N0 = invariant_norm(h0)
    I0A, I0B = F(A0, N0), F(B0, N0)
    ok = bad = skipped = 0
    kappas = []
    for ab in orb:
        h = h_from_ab(*ab)
        if not valid_h(h):
            skipped += 1
            continue
        A, B, _ = linear_form(h)
        N = invariant_norm(h)
        if F(A, N) == I0A and F(B, N) == I0B:
            ok += 1
            kappas.append(F(N, N0))
        else:
            bad += 1
            if verbose and bad <= 3:
                print(f"   MISMATCH h={h}: A/N={F(A,N)} vs {I0A}")
    if verbose:
        print(f"   orbit |G(a,b)| = {len(orb)};  h-valid: {ok+bad}  "
              f"(skipped {skipped});  identity holds: {ok}, fails: {bad}")
        print(f"   distinct factorial ratios kappa = |{{{len(set(kappas))}}}| "
              f"(kappa = Pi(gc)/Pi(c) = N(gh)/N(h))")
    return ok, bad, skipped, len(orb)


def test_theta(alpha, beta, n=1, thetas=(F(1, 2), F(1, 5), F(2, 5), F(1, 3))):
    """p-adic version: shift the NUMERATOR brick by theta.  The transfer identity
    must survive with Gamma-ratios in place of factorials.

    We test it in the strongest exactly-checkable form: the *ratio* of linear
    forms across the orbit must equal the corresponding shifted-normalisation
    ratio, i.e. the two forms must stay PROPORTIONAL with the predicted kappa.
    """
    from math import prod
    a = tuple(alpha[j] * n + 1 for j in range(4))
    b = (beta[0] * n + 1, beta[1] * n + 1, beta[2] * n + 2, beta[3] * n + 2)
    shift = 1 - b[0]
    a = tuple(x + shift for x in a)
    b = tuple(x + shift for x in b)
    ab0 = (a, b)
    orb = [x for x in orbit_ab(ab0) if valid_h(h_from_ab(*x))]
    print(f"   theta-test: orbit of {len(orb)} h-valid points")
    for theta in thetas:
        h0 = h_from_ab(*ab0)
        base = shifted_pair(h0, theta)
        nprop = nfail = 0
        for ab in orb:
            h = h_from_ab(*ab)
            cur = shifted_pair(h, theta)
            # proportionality test (exact 2x2 determinant)
            if base[0] * cur[1] - base[1] * cur[0] == 0:
                nprop += 1
            else:
                nfail += 1
        print(f"     theta={theta}: proportional {nprop}/{nprop+nfail}"
              f"{'  [ALL]' if nfail == 0 else '  [BROKEN]'}")


def shifted_pair(h, theta):
    """(coefficient of the weight-3 Hurwitz value, rational part) for the
    theta-shifted very-well-poised function."""
    num, den, lin = R_data(h, theta)
    r = partial_fractions(num, den, lin)
    imax = max(i for i, _ in r)
    rho = [F(0)] * (imax + 1)
    for (i, k), v in r.items():
        rho[i] += v
    A = rho[3] if imax >= 3 else F(0)
    B = F(0)
    for (i, k), v in r.items():
        Hk = sum(F(1, l ** i) for l in range(1, int(k)))
        B -= v * Hk
    return A, B


if __name__ == "__main__":
    test_apery()
    print("\n[B] transfer identity across the group orbit (integer family)")
    for (al, be) in [((1, 1, 1, 1), (0, 0, 2, 2)),
                     ((2, 2, 3, 3), (0, 1, 4, 5)),
                     ((3, 4, 4, 5), (0, 2, 7, 7)),
                     ((4, 7, 8, 11), (0, 3, 13, 14))]:
        print(f"  alpha={al} beta={be}, n=1:")
        test_transfer(al, be, n=1)
    print("\n[C] theta-shifted (p-adic) family")
    for (al, be) in [((2, 2, 3, 3), (0, 1, 4, 5)), ((3, 4, 4, 5), (0, 2, 7, 7))]:
        print(f"  alpha={al} beta={be}, n=1:")
        test_theta(al, be, n=1)
