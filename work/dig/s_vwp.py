"""DIG-3  s_vwp.py -- the very-well-poised p-adic cone at p = 2, theta = 1/2, EXACT.

This is the family that actually carries every known p-adic result at p = 2
(Beukers R^(B), LSZ, Lai A_n/B_n), written with the two O(1) freedoms that the
DIG-1 ledger is blind to because they do not move any asymptotic rate:

    R(t) = (2t + h0)^d  *  prod_{j=1..M} (t + 1/2 + e_j)_{h0 - 2 e_j}
                         /  prod_{j=1..M} (t + f_j)_{h0 + 1 - 2 f_j}

  * e_j, f_j in Z  ("insets"): bounded translations of the bricks.  For bounded
    e, f every asymptotic ledger quantity is UNCHANGED
        sum lambda = M - 2 sum e / h0  ->  M ,   sum nu -> M,
        v_2(C) = sum lambda + sum nu   ->  2M ,  G -> 2M log 2,
        alpha = 2G  (every brick is aligned: 1/2 + e_j + 1/2 = integer),
        E = M + m   (= A + m + 1 - delta with A = M, delta = 1),
        C_1 = 0  (the bricks stay co-located to leading order).
    They move only the RATIONAL coefficients rho_i -- i.e. exactly the rank.

  * the derivative order m: S = int_{Z_2} R^{(m)}(t + 1/2) dt
        = rho_0 + sum_i (-1)^m (i)_m rho_i J_{i+m},  J_u = u 2^u om^-u zeta_2(u+1,1/2)
    so the weights are w_i = i + m + 1.

THE PARITY LAW  [PROVED here, VERIFIED below]:  R(-h0-t) = -(-1)^M R(t), hence
    r_{i,h0-k} = -(-1)^{M+i} r_{i,k}   and   rho_i = 0 whenever i + M is even.
Together with zeta_2(even) = 0 and rho_1 = 0 (deg R <= -2) this fixes the rank:
    M even:  surviving i odd >= 3, m odd,  weights {m+4, m+6, ..., m+M}
    M odd :  surviving i even >= 2, m even, weights {m+3, m+5, ..., m+M}
and the LEDGER MARGIN of the whole family is
    margin(M, m) = 2M log2 - (M + m) = M(2 log 2 - 1) - m,
which is POSITIVE for every weight once M is large enough.  The only obstruction
to zeta_2(7) is therefore RANK, not size.  Everything in this module exists to
test whether the rank can be brought down to 1 at weight 7.
"""
from fractions import Fraction as F
from functools import lru_cache
import math, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

LOG2 = math.log(2.0)


# ----------------------------------------------------------------- series utils
def s_mul(a, b, M):
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
    """series in eps of prod_{c in roots} (eps + (c - k)) up to eps^M."""
    out = [F(0)] * (M + 1)
    out[0] = F(1)
    for c in roots:
        a = c - k
        if a == 0:
            raise ValueError("zero shift")
        fac = [F(0)] * (M + 1)
        fac[0] = a
        if M >= 1:
            fac[1] = F(1)
        out = s_mul(out, fac, M)
    return out


# ----------------------------------------------------------------- the family
class VWPX:
    """VWP rational function with insets; theta = 1/2 (p = 2, r = 1).

    h0     : the scale parameter (= n)
    e, f   : tuples of M integers (numerator / denominator insets, any sign)
    dwp    : 0 or 1, the (2t+h0) well-poised factor
    """

    def __init__(self, h0, e, f, dwp=1, theta=F(1, 2)):
        self.h0, self.e, self.f = h0, tuple(e), tuple(f)
        self.M = len(e)
        assert len(f) == self.M
        self.dwp = dwp
        self.theta = F(theta)
        self.num = []
        for ej in self.e:
            L = h0 - 2 * ej
            if L < 0:
                raise ValueError("negative numerator brick")
            self.num += [self.theta + ej + i for i in range(L)]
        self.den = []
        for fj in self.f:
            L = h0 + 1 - 2 * fj
            if L < 1:
                raise ValueError("empty denominator brick")
            self.den += [F(fj + i) for i in range(L)]
        self.deg = dwp + len(self.num) - len(self.den)

    def admissible(self):
        return self.deg <= -2

    def mult(self, k):
        return sum(1 for fj in self.f if fj <= k <= self.h0 - fj)

    def partial_fractions(self):
        r = {}
        for k in range(0, self.h0 + 1):
            mk = self.mult(k)
            if mk == 0:
                continue
            den_other = [c for c in self.den if c != k]
            top = prod_linear_series(self.num, k, mk - 1)
            bot = prod_linear_series(den_other, k, mk - 1)
            if self.dwp:
                lin = [F(self.h0 - 2 * k)] + ([F(2)] if mk >= 2 else [])
                lin = lin + [F(0)] * max(0, mk - len(lin))
            else:
                lin = [F(1)] + [F(0)] * max(0, mk - 1)
            G = s_mul(s_mul(lin, top, mk - 1), s_inv(bot, mk - 1), mk - 1)
            for i in range(1, mk + 1):
                r[(i, k)] = G[mk - i]
        return r

    def rho(self, r=None):
        if r is None:
            r = self.partial_fractions()
        out = [F(0)] * (self.M + 1)
        for (i, k), v in r.items():
            out[i] += v
        return out

    def rho0(self, m, r=None):
        """rho_0 for derivative order m:
        rho_0 = -(-1)^m sum_{i,k} r_{i,k} (i)_{m+1} T_{k,i+m+1},
        T_{k,u} = sum_{nu<k} (nu + theta)^{-u}."""
        if r is None:
            r = self.partial_fractions()
        maxi = self.M
        umax = maxi + m + 1
        T = [[F(0)] * (umax + 1) for _ in range(self.h0 + 2)]
        for k in range(1, self.h0 + 1):
            base = F(k - 1) + self.theta
            for u in range(1, umax + 1):
                T[k][u] = T[k - 1][u] + F(1) / base ** u
        tot = F(0)
        for (i, k), v in r.items():
            if k == 0 or v == 0:
                continue
            poch = F(1)
            for t in range(m + 1):
                poch *= (i + t)
            tot += v * poch * T[k][i + m + 1]
        return -tot   # LSZ printed-sign convention (overall sign is irrelevant)

    # ---------- ledger of this point -------------------------------------
    def ledger(self, m):
        """exact-in-the-limit ledger:  (G, E, alpha, beta, margin, weights)."""
        M = self.M
        sum_lam = F(len(self.num), self.h0)          # sum lambda_c  (per h0)
        sum_nu = F(len(self.den), self.h0)           # sum nu_d
        vpC = sum_lam + sum_nu                       # l' = r = 1, 1/(p-1) = 1
        G = float(vpC) * LOG2
        gain = float(sum_nu * 1 + sum_lam) * LOG2    # r*sum nu + sum lam/(p-1)
        alpha = G + gain
        E = M + m + 1 - self.dwp
        beta = G + E
        ws = [i + m + 1 for i in range(2, M + 1)
              if (i + M) % 2 == 1 and (i + m + 1) % 2 == 1]
        return dict(G=G, E=E, alpha=alpha, beta=beta, margin=alpha - beta,
                    weights=ws, rank=len(ws),
                    mu=(alpha / (alpha - beta)) if alpha > beta else None)


def asymptotic_ledger(M, m, dwp=1):
    """the h0 -> infinity ledger of the whole VWP(M) family at derivative order m."""
    G = 2 * M * LOG2
    alpha = 2 * G
    E = M + m + 1 - dwp
    beta = G + E
    ws = [i + m + 1 for i in range(2, M + 1)
          if (i + M) % 2 == 1 and (i + m + 1) % 2 == 1]
    return dict(G=G, E=E, alpha=alpha, beta=beta, margin=G - E, weights=ws,
                rank=len(ws), mu=(alpha / (G - E)) if G > E else None)


# ----------------------------------------------------------------- validation
def anchors():
    print("=" * 78)
    print("s_vwp ANCHORS -- the module must reproduce DIG-1's validated objects")
    print("=" * 78)
    ok = True

    # (1) LSZ: M = 4, e = f = 0, C^n = 2^{8n}, m = 1.
    print("\n[A1] LSZ 2025 (M=4, symmetric, m=1):  rho_zeta = 384 rho_3 * 2^{8n},"
          " rho_0 * 2^{8n}")
    exp3 = {0: F(768), 1: F(73728)}
    exp0 = {0: F(0), 1: F(-1024)}
    expn = {0: 1, 1: 96, 2: 14944}
    for n in range(0, 5):
        v = VWPX(n, (0,) * 4, (0,) * 4)
        r = v.partial_fractions()
        rh = v.rho(r)
        C = F(2) ** (8 * n)
        r3, r0 = 384 * rh[3] * C, v.rho0(1, r) * C
        tag = ""
        if n in exp3:
            good = (r3 == exp3[n] and r0 == exp0[n])
            ok &= good
            tag += "  [LSZ printed: %s]" % ("OK" if good else "MISMATCH")
        if n in expn:
            good = (r3 / 768 == expn[n])
            ok &= good
            tag += "  rho_n=%s %s" % (r3 / 768, "OK" if good else "MISMATCH")
        assert rh[1] == 0
        print("   n=%d deg=%d rho_3=%s rho_0=%s%s" % (n, v.deg, r3, r0, tag))

    # (2) the parity law
    print("\n[A2] parity law  rho_i = 0 whenever i + M is even   (R(-h0-t) = -(-1)^M R(t))")
    for M in (3, 4, 5, 6, 7):
        for n in (4, 5, 6):
            v = VWPX(n, (0,) * M, (0,) * M)
            rh = v.rho()
            zer = [i for i in range(1, M + 1) if rh[i] == 0]
            pred = [i for i in range(1, M + 1) if (i + M) % 2 == 0]
            pred1 = sorted(set(pred) | {1})     # rho_1 = 0 also by degree
            good = set(pred1) <= set(zer)
            ok &= good
            if n == 4:
                print("   M=%d  zero rho_i = %s   predicted %s   %s"
                      % (M, zer, pred1, "OK" if good else "MISMATCH"))

    # (3) Beukers R^(B) (M=3, m=0) and the ledger reproduction of the 3 measures
    print("\n[A3] asymptotic ledger of the VWP family, checked against DIG-1")
    print("     M   m   weights          rank  G        E   margin     mu")
    for (M, m, tag) in [(3, 0, "Beukers R^(B) = zeta_2(3), mu 7.177398"),
                        (4, 1, "LSZ = zeta_2(5), mu 20.342651"),
                        (5, 0, "rank 2 {3,5}"), (5, 2, "rank 2 {5,7}"),
                        (6, 1, "Lai: one of zeta_2(5), zeta_2(7)"),
                        (6, 3, "rank 2 {7,9}"), (7, 0, "rank 3 {3,5,7}"),
                        (8, 1, "rank 3 {5,7,9}"), (4, 3, "zeta_2(7) rank 1 -- the nearest miss"),
                        (9, 0, "rank 4 {3,5,7,9}"), (10, 1, "rank 4 {5,7,9,11}")]:
        L = asymptotic_ledger(M, m)
        print("   %3d %3d   %-16s %3d  %7.4f  %2d  %+8.4f   %s   %s"
              % (M, m, str(L["weights"]), L["rank"], L["G"], L["E"], L["margin"],
                 ("%.6f" % L["mu"]) if L["mu"] else "  --      ", tag))
    return ok


if __name__ == "__main__":
    ok = anchors()
    print("\n" + "=" * 78)
    print("s_vwp ANCHOR VERDICT:", "PASS" if ok else "FAIL")
    print("=" * 78)
