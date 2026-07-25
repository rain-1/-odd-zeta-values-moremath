"""DIG-1  T1/T2 : exact machinery for the parametrised p-adic Volkenborn family.

    R_n(t) = C^n * (2t+n)^delta * prod_c (t+theta'_c)_{L_c} / (t)_{n+1}^A
    S_n    = Int_{Z_p} R_n^{(m)}(t+theta0) dt
           = rho_0 + sum_{i=1}^{A} (-1)^m (i)_m rho_i * J_{i+m}
    J_u    = Int_{Z_p} dt/(t+theta0)^u = sum_k binom(-u,k) B_k theta0^{-u-k}   (Volkenborn
             moments Int t^k dt = B_k ; Lai-Sprang 2023 Lemma 7)
    rho_i  = sum_k r_{i,k},   rho_0 = -(-1)^m sum_{i,k} r_{i,k} (i)_{m+1} T_{k,i+m+1},
    T_{k,u}= sum_{nu=0}^{k-1} (nu+theta0)^{-u}          (translation: LSZ Lemma 5)

Everything is exact (Fraction / int).  p-adic valuations of S_n come from an exact
truncated Volkenborn series, so v_p(S_n) is certified up to the stated cutoff.
"""
from fractions import Fraction as Fr
from functools import lru_cache
import math
import sympy


# ---------------------------------------------------------------- helpers
def vp(x, p):
    if x == 0:
        return None
    num, den = (x, 1) if isinstance(x, int) else (x.numerator, x.denominator)
    v = 0
    while num % p == 0:
        num //= p; v += 1
    while den % p == 0:
        den //= p; v -= 1
    return v


@lru_cache(maxsize=None)
def bern(k):
    return Fr(sympy.bernoulli(k))          # B_1 = -1/2 convention (sympy >=1.12: bernoulli(1) = 1/2?)


@lru_cache(maxsize=None)
def bern_volkenborn(k):
    """Volkenborn moments Int_{Z_p} t^k dt = B_k with B_1 = -1/2."""
    b = Fr(sympy.bernoulli(k))
    if k == 1:
        b = Fr(-1, 2)
    return b


@lru_cache(maxsize=None)
def dn(n):
    d = 1
    for i in range(1, n + 1):
        d = d * i // math.gcd(d, i)
    return d


def series_exp(c, N):
    """exp(sum_{i>=1} c[i] eps^i) truncated at eps^N, c a dict/list of Fractions."""
    out = [Fr(0)] * (N + 1)
    out[0] = Fr(1)
    for i in range(1, N + 1):
        # out[i] = (1/i) sum_{j=1}^{i} j*c[j]*out[i-j]
        s = Fr(0)
        for j in range(1, i + 1):
            if c[j]:
                s += j * c[j] * out[i - j]
        out[i] = s / i
    return out


class Family:
    """One point of the parameter space; all objects computed exactly."""

    def __init__(self, p, theta0, shifts, A, m=0, delta=0, C=None, lengths=None):
        self.p = p
        self.theta0 = Fr(theta0)
        self.shifts = [Fr(s) for s in shifts]
        self.A = A
        self.m = m
        self.delta = delta
        self.lengths = lengths            # list of (a,b): length = a*n+b ; default (1,0)
        self.C = C                        # normalising constant (int); None -> forced value

    # ---------- the forced normalisation ---------------------------------
    def vpC(self, lengths_weighted=True):
        """v_p of the forced normalisation:  sum_c l'_c * lambda_c + A/(p-1)."""
        tot = Fr(0)
        for c, s in enumerate(self.shifts):
            lam = Fr(1) if (self.lengths is None or not lengths_weighted) else Fr(self.lengths[c][0])
            tot += max(0, -vp(s, self.p)) * lam
        return tot + Fr(self.A, self.p - 1)

    def Cn(self, n):
        """C^n as an exact integer: p^{ceil(n*vpC)} (the forced p-power)."""
        if self.C is not None:
            return self.C ** n
        e = self.vpC() * n
        return self.p ** int(math.ceil(e))

    def length(self, c, n):
        if self.lengths is None:
            return n
        a, b = self.lengths[c]
        return int(a * n + b)

    # ---------- partial fractions ----------------------------------------
    def partial_fractions(self, n):
        """r[i][k] for 1<=i<=A, 0<=k<=n  (exact Fractions)."""
        A, p = self.A, self.p
        Cn = self.Cn(n)
        r = [[Fr(0)] * (n + 1) for _ in range(A + 1)]
        for k in range(n + 1):
            # f(eps) = R_n(-k+eps)*(eps)^A  -> need coefficients up to eps^{A-1}
            f0 = Fr(Cn)
            c = [Fr(0)] * A                       # log-series coefficients
            # numerator Pochhammers
            for ci, th in enumerate(self.shifts):
                L = self.length(ci, n)
                for j in range(L):
                    a = th - k + j
                    f0 *= a
                    ai = Fr(1)
                    for i in range(1, A):
                        ai /= a
                        c[i] += Fr((-1) ** (i - 1), i) * ai
            # denominator (t)_{n+1}^A with the (t+k)^A factor removed
            for j in range(n + 1):
                if j == k:
                    continue
                a = Fr(j - k)
                f0 /= a ** A
                ai = Fr(1)
                for i in range(1, A):
                    ai /= a
                    c[i] -= A * Fr((-1) ** (i - 1), i) * ai
            ser = series_exp([Fr(0)] + c[1:] + [Fr(0)], A - 1)
            ser = [f0 * x for x in ser]
            # well-poised factor (2t+n)^delta = (n-2k+2eps)^delta
            if self.delta:
                w0, w1 = Fr(n - 2 * k), Fr(2)
                new = [Fr(0)] * A
                for i in range(A):
                    if i < len(ser):
                        new[i] += w0 * ser[i]
                    if i >= 1 and i - 1 < len(ser):
                        new[i] += w1 * ser[i - 1]
                ser = new
            for i in range(1, A + 1):
                lam = A - i
                r[i][k] = ser[lam] if lam < len(ser) else Fr(0)
        return r

    # ---------- the linear form ------------------------------------------
    def form(self, n, r=None):
        """returns (rho0, {u: coefficient of J_u}, rho[i])."""
        if r is None:
            r = self.partial_fractions(n)
        A, m, th0 = self.A, self.m, self.theta0
        rho = [Fr(0)] * (A + 1)
        for i in range(1, A + 1):
            rho[i] = sum(r[i])
        sgn = Fr((-1) ** m)
        Jc = {}
        for i in range(1, A + 1):
            poch = Fr(1)
            for t in range(m):
                poch *= (i + t)
            if rho[i]:
                Jc[i + m] = Jc.get(i + m, Fr(0)) + sgn * poch * rho[i]
        # rational part
        # T[k][u] = sum_{nu<k} (nu+th0)^{-u}
        umax = A + m + 1
        T = [[Fr(0)] * (umax + 2) for _ in range(n + 2)]
        for k in range(1, n + 1):
            for u in range(1, umax + 2):
                T[k][u] = T[k - 1][u] + Fr(1) / (Fr(k - 1) + th0) ** u
        rho0 = Fr(0)
        for i in range(1, A + 1):
            poch = Fr(1)
            for t in range(m + 1):
                poch *= (i + t)
            u = i + m + 1
            s = Fr(0)
            for k in range(1, n + 1):
                if r[i][k]:
                    s += r[i][k] * T[k][u]
            rho0 -= sgn * poch * s
        return rho0, Jc, rho

    # ---------- p-adic value of J_u ---------------------------------------
    def J(self, u, prec):
        """Int dt/(t+theta0)^u = sum_k binom(-u,k) B_k theta0^{-u-k}, exact to p^prec."""
        p, th0 = self.p, self.theta0
        l = -vp(th0, p)                     # depth
        tot = Fr(0)
        k = 0
        while True:
            term = Fr(int(sympy.binomial(-u, k))) * bern_volkenborn(k) * th0 ** (-u - k)
            v = vp(term, p)
            if v is not None and v > prec:
                break
            tot += term
            k += 1
            if k > prec // max(1, l) + 40:
                break
        return tot

    def S_value(self, n, prec, r=None):
        """S_n as an exact rational approximation valid to p^prec (J_u truncated)."""
        rho0, Jc, rho = self.form(n, r)
        S = rho0
        for u, c in Jc.items():
            S += c * self.J(u, prec)
        return S, rho0, Jc, rho
