"""g_forms.py  --  exact rational coefficients of parametrised p-adic linear forms.

DIG-2 (group half).  Everything here is EXACT (fractions.Fraction / int).

The family
----------
Generalising Lai-Sprang-Zudilin (arXiv:2505.05005, Def. 10)

    R_n(t) = 2^{8n} (2t+n) (t+1/2)_n^4 / (t)_{n+1}^4 ,

we consider the *very-well-poised* family with M numerator bricks and M
denominator bricks, all symmetric about the centre  t = -h0/2 :

    R(t) = (2t + h0)
           * prod_{j=1..M} (t + theta + e_j)_{h0 - 2 e_j}          (numerator)
           / prod_{j=1..M} (t + f_j)_{h0 + 1 - 2 f_j}              (denominator)

(the overall power-of-p constant C^n is irrelevant for the *group* question --
it is a common scalar -- so it is carried separately).

theta = 1/2 recovers p = 2 (LSZ).  theta = a/p^l gives the general p-adic shift.
e = f = 0 is the totally symmetric (LSZ) point.

Structure of the linear form (LSZ Lemma 12 / Lai-Sprang Lemma 21):
partial fractions  R(t) = sum_{i,k} r_{i,k}/(t+k)^i, then

    rho_i    = sum_k r_{i,k}                       (i = 1..M)
    rho_zeta = coefficient of zeta_p(M+1)          (= 384 * rho_3 for LSZ)
    rho_0    = -sum_{i,k} i(i+1) r_{i,k} * sum_{l=1}^{k} (l-1+theta)^{-(i+2)}

The KEY POINT (LSZ Remark 13): these rho's are the *same rational numbers* in
the Archimedean and in the p-adic construction.  So any transfer identity for
them is simultaneously Archimedean and p-adic.
"""

from fractions import Fraction as F
from math import comb, gcd
from functools import lru_cache


# ---------------------------------------------------------------- truncated series

def s_mul(a, b, M):
    """(a*b) truncated at degree M; a, b lists of Fractions."""
    out = [F(0)] * (M + 1)
    for i, ai in enumerate(a):
        if ai == 0 or i > M:
            continue
        for j, bj in enumerate(b):
            if i + j > M:
                break
            if bj:
                out[i + j] += ai * bj
    return out


def s_inv(a, M):
    """1/a truncated at degree M; a[0] != 0."""
    inv0 = 1 / a[0]
    out = [F(0)] * (M + 1)
    out[0] = inv0
    for k in range(1, M + 1):
        acc = F(0)
        for j in range(1, k + 1):
            if j < len(a) and a[j]:
                acc += a[j] * out[k - j]
        out[k] = -acc * inv0
    return out


def prod_linear_series(roots, k, M):
    """Series in eps of  prod_{c in roots} (eps + (c-k))  up to degree M.

    All (c-k) must be non-zero.
    """
    out = [F(0)] * (M + 1)
    out[0] = F(1)
    for c in roots:
        a = c - k
        assert a != 0, "zero shift in prod_linear_series"
        # factor = a * (1 + eps/a)
        fac = [F(0)] * (M + 1)
        fac[0] = a
        if M >= 1:
            fac[1] = F(1)
        out = s_mul(out, fac, M)
    return out


# ---------------------------------------------------------------- the family

class VWP:
    """Very-well-poised parametrised rational function.

    h0    : the well-poised centre parameter (an integer, = n at LSZ point)
    e     : tuple of M non-negative integers (numerator brick insets)
    f     : tuple of M non-negative integers (denominator brick insets)
    theta : Fraction, the p-adic shift (1/2 for LSZ)
    """

    def __init__(self, h0, e, f, theta=F(1, 2)):
        self.h0 = h0
        self.e = tuple(e)
        self.f = tuple(f)
        assert len(e) == len(f)
        self.M = len(e)
        self.theta = F(theta)
        # numerator roots: (t + theta + e_j)_{h0 - 2 e_j}
        self.num = []
        for ej in self.e:
            L = h0 - 2 * ej
            assert L >= 0, "empty/negative numerator brick"
            self.num += [self.theta + ej + i for i in range(L)]
        # denominator roots: (t + f_j)_{h0 + 1 - 2 f_j}
        self.den = []
        for fj in self.f:
            L = h0 + 1 - 2 * fj
            assert L >= 1, "empty/negative denominator brick"
            self.den += [F(fj + i) for i in range(L)]
        self.deg = 1 + len(self.num) - len(self.den)

    # ---- degrees / admissibility

    def admissible(self):
        """deg R <= -2  (kills the zeta_p(3) coefficient) and bricks non-empty."""
        return self.deg <= -2

    def mult(self, k):
        return sum(1 for fj in self.f if fj <= k <= self.h0 - fj)

    # ---- partial fractions

    def partial_fractions(self):
        """dict (i,k) -> r_{i,k}  (exact Fractions), i>=1, 0<=k<=h0."""
        M = self.M
        r = {}
        for k in range(0, self.h0 + 1):
            mk = self.mult(k)
            if mk == 0:
                continue
            # G_k(eps) = (h0 - 2k + 2 eps) * prod_num(eps+(c-k)) / prod_den'(eps+(c-k))
            den_other = [c for c in self.den if c != k]
            # multiplicity check
            assert len(self.den) - len(den_other) == mk
            top = prod_linear_series(self.num, k, mk - 1)
            bot = prod_linear_series(den_other, k, mk - 1)
            lin = [F(self.h0 - 2 * k)] + ([F(2)] if mk - 1 >= 1 else [])
            lin = lin + [F(0)] * (mk - len(lin))
            G = s_mul(s_mul(lin, top, mk - 1), s_inv(bot, mk - 1), mk - 1)
            for i in range(1, mk + 1):
                r[(i, k)] = G[mk - i]
        return r

    # ---- linear form coefficients

    def rho(self, r=None):
        """rho_i = sum_k r_{i,k} for i = 1..M."""
        if r is None:
            r = self.partial_fractions()
        out = [F(0)] * (self.M + 1)
        for (i, k), v in r.items():
            out[i] += v
        return out

    def rho0(self, r=None):
        """rho_0 = -sum_{i,k} i(i+1) r_{i,k} sum_{l=1}^{k} (l-1+theta)^{-(i+2)}.

        (LSZ eq. (def_rho_0) with theta = 1/2: (l-1/2)^{-(i+2)}.)
        """
        if r is None:
            r = self.partial_fractions()
        # H[i][k] = sum_{l=1}^{k} (l - 1 + theta)^{-(i+2)}
        maxi = self.M
        H = [[F(0)] * (self.h0 + 1) for _ in range(maxi + 1)]
        for i in range(1, maxi + 1):
            acc = F(0)
            for k in range(1, self.h0 + 1):
                acc += F(1) / (F(k - 1) + self.theta) ** (i + 2)
                H[i][k] = acc
        tot = F(0)
        for (i, k), v in r.items():
            if k == 0:
                continue
            tot += i * (i + 1) * v * H[i][k]
        return -tot


# ---------------------------------------------------------------- LSZ anchors

def lsz_check():
    """Reproduce LSZ's printed values at the totally symmetric point."""
    ok = True
    expect_rho3 = {0: F(768), 1: F(73728)}
    expect_rho0 = {0: F(0), 1: F(-1024)}
    expect_rn = {0: 1, 1: 96, 2: 14944}
    for n in range(0, 6):
        v = VWP(n, (0, 0, 0, 0), (0, 0, 0, 0), F(1, 2))
        r = v.partial_fractions()
        rho = v.rho(r)
        # LSZ's C^n = 2^{8n} is a scalar we carry separately:
        C = F(2) ** (8 * n)
        rho3 = 384 * rho[3] * C
        rho0 = v.rho0(r) * C
        rho1 = rho[1] * C
        line = f"  n={n}: deg={v.deg} rho1={rho1} rho_zeta={rho3} rho_0={rho0}"
        if n in expect_rho3:
            good = (rho3 == expect_rho3[n] and rho0 == expect_rho0[n])
            ok &= good
            line += "   [LSZ " + ("OK" if good else "MISMATCH") + "]"
        if n in expect_rn:
            good = (rho3 / 768 == expect_rn[n])
            ok &= good
            line += f"  rho_n={rho3/768} " + ("OK" if good else "MISMATCH")
        assert rho1 == 0, f"rho_1 != 0 at n={n}"
        print(line)
    print("  rho_1 = 0 at every n (kills zeta_p(3))  [OK]")
    return ok


if __name__ == "__main__":
    print("[anchor] LSZ totally symmetric point, theta=1/2, M=4:")
    ok = lsz_check()
    print("ANCHORS", "PASS" if ok else "FAIL")
