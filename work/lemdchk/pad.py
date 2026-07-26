"""Fixed-precision p-adic arithmetic for the Lemma-D vanishing-layer audit.

A rational x with v_p(x) >= -SC is represented by the integer  A = x * p^SC  mod p^T.
Then v_p(x) = v_p(A) - SC, correct as long as v_p(A) < T.
Everything below is exact integer arithmetic; no floating point anywhere.
"""
from math import comb
from fractions import Fraction as Fr

INF = 10 ** 6


def vp_int(x, p, cap=None):
    if x == 0:
        return INF if cap is None else cap
    v = 0
    while x % p == 0:
        x //= p
        v += 1
        if cap is not None and v >= cap:
            return cap
    return v


def vp_fr(x, p):
    if x == 0:
        return INF
    return vp_int(x.numerator, p) - vp_int(x.denominator, p)


def vp_fact(n, p):
    """v_p(n!) by Legendre."""
    v, q = 0, p
    while q <= n:
        v += n // q
        q *= p
    return v


def vp_binom(t, b, p):
    """exact v_p(C(t,b)); 0 if the binomial vanishes is NOT handled (caller checks)."""
    return vp_fact(t, p) - vp_fact(b, p) - vp_fact(t - b, p)


def chi4(m):
    if m % 2 == 0:
        return 0
    return 1 if m % 4 == 1 else -1


class Tables:
    """scaled p-adic partial sums.

    Hs[r][y] = ( sum_{m<=y} 1/m^r ) * p^(2r)   mod p^T          (scale 2r)
    Ks[r][y] = ( sum_{m<=y} chi_{-4}(m)/m^r ) * p^(2r)  mod p^T (scale 2r)

    2r is enough scale as long as every argument y satisfies y < p^3
    (so the deepest p-power dividing any m <= y is p^2).
    """

    def __init__(self, p, T, Y, rmax=3, want_K=False):
        assert Y < p ** 3, 'scale 2r insufficient for arguments >= p^3'
        self.p, self.T, self.Y = p, T, Y
        M = p ** T
        self.M = M
        self.Hs = {}
        self.Ks = {}
        for r in range(1, rmax + 1):
            sc = p ** (2 * r)
            arr = [0] * (Y + 1)
            s = 0
            for m in range(1, Y + 1):
                e = 0
                mm = m
                while mm % p == 0:
                    mm //= p
                    e += 1
                # p^(2r) / m^r = p^(2r - e r) * (m')^(-r)
                s = (s + p ** (2 * r - e * r) * pow(pow(mm, r, M), -1, M)) % M
                arr[m] = s
            self.Hs[r] = arr
            if want_K:
                arrk = [0] * (Y + 1)
                s = 0
                for m in range(1, Y + 1):
                    c = chi4(m)
                    if c:
                        e = 0
                        mm = m
                        while mm % p == 0:
                            mm //= p
                            e += 1
                        s = (s + c * p ** (2 * r - e * r) * pow(pow(mm, r, M), -1, M)) % M
                    arrk[m] = s
                self.Ks[r] = arrk

    def get(self, kind, r, y):
        """scaled value (scale 2r); y<0 -> 0."""
        if y < 0:
            return 0
        a = self.Hs[r] if kind == 'H' else self.Ks[r]
        return a[y]


def verify_tables(tab, p, ys, rmax=3, want_K=False):
    """cross-check the scaled tables against exact Fractions on a sample of y."""
    bad = []
    for y in ys:
        for r in range(1, rmax + 1):
            ex = sum(Fr(1, m ** r) for m in range(1, y + 1))
            A = tab.get('H', r, y)
            # A should equal ex * p^(2r) mod p^T
            num = ex * Fr(p) ** (2 * r)
            if vp_fr(num, p) < 0:
                bad.append(('scale', y, r))
                continue
            want = (num.numerator * pow(num.denominator % tab.M, -1, tab.M)) % tab.M
            if want != A:
                bad.append(('H', y, r, want, A))
            if want_K:
                exk = sum(Fr(chi4(m), m ** r) for m in range(1, y + 1))
                Ak = tab.get('K', r, y)
                numk = exk * Fr(p) ** (2 * r)
                wantk = (numk.numerator * pow(numk.denominator % tab.M, -1, tab.M)) % tab.M
                if wantk != Ak:
                    bad.append(('K', y, r, wantk, Ak))
    return bad
