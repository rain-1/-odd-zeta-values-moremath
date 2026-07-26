"""The 15 sporadic families as CELL GENERATORS.

Each family provides
    idx(n)          -> dict argname -> np.int64 array of argument values, one entry per cell
    Smod(n, fac)    -> np.int64 array of summand values mod fac.q
    Sexact(n)       -> list of python ints (exact summand values)
    args            -> list of argument names available (all bare, i.e. H^(r)_x)
    tame            -> the subset of args with 0 <= x <= n on the whole support
    w, D            -> weight, character discriminant (None = trivial)

A "cell" is one term of the (possibly double, possibly bracketed) binomial sum.
Bracketed families (eta, s18) get TWO cells per k, with the bracket's two binomials
kept separate so their Gamma-arguments differ -- a strictly larger ansatz.
"""
import numpy as np
from math import comb, factorial


class Fac:
    def __init__(self, M, q):
        self.M, self.q = M, q
        f = np.ones(M + 1, dtype=np.int64)
        for i in range(1, M + 1):
            f[i] = f[i - 1] * i % q
        fi = np.ones(M + 1, dtype=np.int64)
        fi[M] = pow(int(f[M]), q - 2, q)
        for i in range(M, 0, -1):
            fi[i - 1] = fi[i] * i % q
        self.f, self.fi = f, fi

    def b(self, top, bot):
        """binomial mod q, vectorised; 0 unless 0 <= bot <= top."""
        q = self.q
        top = np.asarray(top, dtype=np.int64)
        bot = np.asarray(bot, dtype=np.int64)
        ok = (bot >= 0) & (top >= bot) & (top >= 0)
        t = np.where(ok, top, 0)
        bb = np.where(ok, bot, 0)
        v = self.f[t] * self.fi[bb] % q * self.fi[t - bb] % q
        return np.where(ok, v, 0)

    def pw(self, base, e):
        q = self.q
        e = np.asarray(e, dtype=np.int64)
        out = np.ones(e.shape, dtype=np.int64)
        mx = int(e.max()) if e.size else 0
        tabl = np.ones(mx + 1, dtype=np.int64)
        for i in range(1, mx + 1):
            tabl[i] = tabl[i - 1] * base % q
        return tabl[np.where(e < 0, 0, e)] * np.where(e < 0, 0, 1)


def _ebin(top, bot):
    if bot < 0 or top < bot or top < 0:
        return 0
    return comb(top, bot)


class Fam:
    label = ''
    w = 2
    D = None
    args = ()
    tame = ()
    note = ''
    maxtop = 2          # factorial table must reach maxtop*n + 8

    def ks(self, n):
        raise NotImplementedError

    def idx(self, n):
        raise NotImplementedError

    def Smod(self, n, fac):
        raise NotImplementedError

    def Sexact(self, n):
        raise NotImplementedError


# ============================================================ (R2) Zagier six

class A(Fam):
    label, w, D = 'A', 2, None
    args = ('n', 'k', 'n-k', 'n+k', '2k', '2n-2k', '2n')
    tame = ('n', 'k', 'n-k')
    note = 'Franel  sum C(n,k)^3'

    def idx(self, n):
        k = np.arange(n + 1, dtype=np.int64)
        return {'n': np.full(n + 1, n, dtype=np.int64), 'k': k, 'n-k': n - k,
                'n+k': n + k, '2k': 2 * k, '2n-2k': 2 * (n - k),
                '2n': np.full(n + 1, 2 * n, dtype=np.int64)}

    def Smod(self, n, fac):
        k = np.arange(n + 1, dtype=np.int64)
        c = fac.b(n, k)
        return c * c % fac.q * c % fac.q

    def Sexact(self, n):
        return [comb(n, k) ** 3 for k in range(n + 1)]


class Bseq(Fam):
    label, w, D = 'B', 2, -3
    args = ('n', 'k', '3k', 'n-3k', '2k', 'n+k', 'n-k', '2n', '4k', 'n-2k')
    tame = ('n', 'k', '3k', 'n-3k', '2k', 'n-k', 'n-2k')   # 3k<=n on the support
    note = 'sum (-1)^k 3^(n-3k) C(n,3k)(3k)!/k!^3'
    maxtop = 2

    def idx(self, n):
        k = np.arange(n // 3 + 1, dtype=np.int64)
        return {'n': np.full(k.size, n, dtype=np.int64), 'k': k, '3k': 3 * k,
                'n-3k': n - 3 * k, '2k': 2 * k, 'n+k': n + k, 'n-k': n - k,
                '2n': np.full(k.size, 2 * n, dtype=np.int64), '4k': 4 * k, 'n-2k': n - 2 * k}

    def Smod(self, n, fac):
        q = fac.q
        k = np.arange(n // 3 + 1, dtype=np.int64)
        s = fac.b(n, 3 * k) * fac.b(3 * k, k) % q * fac.b(2 * k, k) % q
        s = s * fac.pw(3, n - 3 * k) % q
        return np.where(k % 2 == 1, (-s) % q, s)

    def Sexact(self, n):
        return [(-1) ** k * 3 ** (n - 3 * k) * comb(n, 3 * k) * factorial(3 * k) // factorial(k) ** 3
                for k in range(n // 3 + 1)]


class Cseq(Fam):
    label, w, D = 'C', 2, -3
    args = ('n', 'k', 'n-k', '2k', 'n+k', '2n-2k', '2n', '2n-k', '3k', '3n-3k', '3n')
    tame = ('n', 'k', 'n-k')
    maxtop = 4
    note = 'sum C(n,k)^2 C(2k,k)'

    def idx(self, n):
        k = np.arange(n + 1, dtype=np.int64)
        return {'n': np.full(n + 1, n, dtype=np.int64), 'k': k, 'n-k': n - k,
                '2k': 2 * k, 'n+k': n + k, '2n-2k': 2 * (n - k),
                '2n': np.full(n + 1, 2 * n, dtype=np.int64), '2n-k': 2 * n - k,
                '3k': 3 * k, '3n-3k': 3 * (n - k),
                '3n': np.full(n + 1, 3 * n, dtype=np.int64)}

    def Smod(self, n, fac):
        q = fac.q
        k = np.arange(n + 1, dtype=np.int64)
        c = fac.b(n, k)
        return c * c % q * fac.b(2 * k, k) % q

    def Sexact(self, n):
        return [comb(n, k) ** 2 * comb(2 * k, k) for k in range(n + 1)]


class D(Fam):
    label, w, D = 'D', 2, None
    args = ('n', 'k', 'n-k', 'n+k', '2k', '2n')
    tame = ('n', 'k', 'n-k')
    note = 'Apery zeta(2)  sum C(n,k)^2 C(n+k,n)'

    def idx(self, n):
        k = np.arange(n + 1, dtype=np.int64)
        return {'n': np.full(n + 1, n, dtype=np.int64), 'k': k, 'n-k': n - k,
                'n+k': n + k, '2k': 2 * k,
                '2n': np.full(n + 1, 2 * n, dtype=np.int64)}

    def Smod(self, n, fac):
        q = fac.q
        k = np.arange(n + 1, dtype=np.int64)
        c = fac.b(n, k)
        return c * c % q * fac.b(n + k, n) % q

    def Sexact(self, n):
        return [comb(n, k) ** 2 * comb(n + k, n) for k in range(n + 1)]


class E(Fam):
    label, w, D = 'E', 2, -4
    args = ('n', 'k', 'n-k', '2k', '2n-2k', 'n+k', '2n', '2n-k')
    tame = ('n', 'k', 'n-k')
    note = 'sum C(n,k) C(2k,k) C(2(n-k),n-k)'

    def idx(self, n):
        k = np.arange(n + 1, dtype=np.int64)
        return {'n': np.full(n + 1, n, dtype=np.int64), 'k': k, 'n-k': n - k,
                '2k': 2 * k, '2n-2k': 2 * (n - k), 'n+k': n + k,
                '2n': np.full(n + 1, 2 * n, dtype=np.int64), '2n-k': 2 * n - k}

    def Smod(self, n, fac):
        q = fac.q
        k = np.arange(n + 1, dtype=np.int64)
        return fac.b(n, k) * fac.b(2 * k, k) % q * fac.b(2 * (n - k), n - k) % q

    def Sexact(self, n):
        return [comb(n, k) * comb(2 * k, k) * comb(2 * (n - k), n - k) for k in range(n + 1)]


class E2(Fam):
    """SECOND representation of Zagier's (d):  A(n) = sum_k 4^(n-2k) C(n,2k) C(2k,k)^2.
    Support 2k <= n, so ALL Gamma-arguments n, k, 2k, n-2k lie in [0,n]: fully TAME."""
    label, w, D = 'E2', 2, -4
    args = ('n', 'k', '2k', 'n-2k', 'n-k', '4k', '2n-2k', '2n', 'n+k', '2n-4k')
    tame = ('n', 'k', '2k', 'n-2k', 'n-k')
    note = 'E, second form: sum 4^(n-2k) C(n,2k) C(2k,k)^2'

    def _k(self, n):
        return np.arange(n // 2 + 1, dtype=np.int64)

    def idx(self, n):
        k = self._k(n)
        return {'n': np.full(k.size, n, dtype=np.int64), 'k': k, '2k': 2 * k,
                'n-2k': n - 2 * k, 'n-k': n - k, '4k': 4 * k, '2n-2k': 2 * (n - k),
                '2n': np.full(k.size, 2 * n, dtype=np.int64), 'n+k': n + k,
                '2n-4k': 2 * n - 4 * k}

    def Smod(self, n, fac):
        q = fac.q
        k = self._k(n)
        c = fac.b(2 * k, k)
        return fac.b(n, 2 * k) * c % q * c % q * fac.pw(4, n - 2 * k) % q

    def Sexact(self, n):
        return [4 ** (n - 2 * k) * comb(n, 2 * k) * comb(2 * k, k) ** 2
                for k in range(n // 2 + 1)]


class Fseq(Fam):
    """double sum: S(n,k,l) = (-1)^k 8^(n-k) C(n,k) C(k,l)^3."""
    label, w, D = 'F', 2, -3
    args = ('n', 'k', 'n-k', 'l', 'k-l', 'n+k', '2l', '2k-2l', 'n-l', 'n-k+l')
    tame = ('n', 'k', 'n-k', 'l', 'k-l', 'n-l', 'n-k+l')
    note = 'sum (-1)^k 8^(n-k) C(n,k) Franel(k)'

    def _kl(self, n):
        i, j = np.triu_indices(n + 1)
        return j.astype(np.int64), i.astype(np.int64)      # k = j >= l = i

    def idx(self, n):
        k, l = self._kl(n)
        return {'n': np.full(k.size, n, dtype=np.int64), 'k': k, 'n-k': n - k,
                'l': l, 'k-l': k - l, 'n+k': n + k, '2l': 2 * l, '2k-2l': 2 * (k - l),
                'n-l': n - l, 'n-k+l': n - k + l}

    def Smod(self, n, fac):
        q = fac.q
        k, l = self._kl(n)
        c = fac.b(k, l)
        s = fac.b(n, k) * c % q * c % q * c % q
        s = s * fac.pw(8, n - k) % q
        return np.where(k % 2 == 1, (-s) % q, s)

    def Sexact(self, n):
        kk, ll = self._kl(n)
        return [(-1) ** int(k) * 8 ** (n - int(k)) * comb(n, int(k)) * comb(int(k), int(l)) ** 3
                for k, l in zip(kk, ll)]


# ============================================================ (R3) AZ six + Cooper

class alpha(Fam):
    label, w, D = 'alpha', 3, None
    args = ('n', 'k', 'n-k', '2k', '2n-2k', 'n+k', '2n')
    tame = ('n', 'k', 'n-k')
    note = 'Domb  sum C(n,k)^2 C(2k,k) C(2(n-k),n-k)'

    def idx(self, n):
        k = np.arange(n + 1, dtype=np.int64)
        return {'n': np.full(n + 1, n, dtype=np.int64), 'k': k, 'n-k': n - k,
                '2k': 2 * k, '2n-2k': 2 * (n - k), 'n+k': n + k,
                '2n': np.full(n + 1, 2 * n, dtype=np.int64)}

    def Smod(self, n, fac):
        q = fac.q
        k = np.arange(n + 1, dtype=np.int64)
        c = fac.b(n, k)
        return c * c % q * fac.b(2 * k, k) % q * fac.b(2 * (n - k), n - k) % q

    def Sexact(self, n):
        return [comb(n, k) ** 2 * comb(2 * k, k) * comb(2 * (n - k), n - k) for k in range(n + 1)]


class gamma(Fam):
    label, w, D = 'gamma', 3, None
    args = ('n', 'k', 'n-k', 'n+k', '2k', '2n')
    tame = ('n', 'k', 'n-k')
    note = 'Apery zeta(3)  sum C(n,k)^2 C(n+k,n)^2'

    def idx(self, n):
        k = np.arange(n + 1, dtype=np.int64)
        return {'n': np.full(n + 1, n, dtype=np.int64), 'k': k, 'n-k': n - k,
                'n+k': n + k, '2k': 2 * k,
                '2n': np.full(n + 1, 2 * n, dtype=np.int64)}

    def Smod(self, n, fac):
        q = fac.q
        k = np.arange(n + 1, dtype=np.int64)
        c = fac.b(n, k) * fac.b(n + k, n) % q
        return c * c % q

    def Sexact(self, n):
        return [comb(n, k) ** 2 * comb(n + k, n) ** 2 for k in range(n + 1)]


class delta(Fam):
    label, w, D = 'delta', 3, None
    args = ('n', 'k', '3k', 'n-3k', '2k', 'n+k', 'n-k')
    tame = ('n', 'k', '3k', 'n-3k', '2k', 'n-k')
    note = 'AZ  sum (-1)^k 3^(n-3k) C(n,3k) C(n+k,n) (3k)!/k!^3'

    def idx(self, n):
        k = np.arange(n // 3 + 1, dtype=np.int64)
        return {'n': np.full(k.size, n, dtype=np.int64), 'k': k, '3k': 3 * k,
                'n-3k': n - 3 * k, '2k': 2 * k, 'n+k': n + k, 'n-k': n - k}

    def Smod(self, n, fac):
        q = fac.q
        k = np.arange(n // 3 + 1, dtype=np.int64)
        s = fac.b(n, 3 * k) * fac.b(3 * k, k) % q * fac.b(2 * k, k) % q
        s = s * fac.b(n + k, n) % q * fac.pw(3, n - 3 * k) % q
        return np.where(k % 2 == 1, (-s) % q, s)

    def Sexact(self, n):
        return [(-1) ** k * 3 ** (n - 3 * k) * comb(n, 3 * k) * comb(n + k, n)
                * factorial(3 * k) // factorial(k) ** 3 for k in range(n // 3 + 1)]


class eps(Fam):
    """support is ceil(n/2) <= k <= n, so 2k-n and 2n-2k are BOTH in [0,n]: tame."""
    label, w, D = 'eps', 3, None
    args = ('n', 'k', 'n-k', '2k', '2k-n', '2n-2k', 'n+k')
    tame = ('n', 'k', 'n-k', '2k-n', '2n-2k')
    note = 'sum C(n,k)^2 C(2k,n)^2'

    def _k(self, n):
        return np.arange((n + 1) // 2, n + 1, dtype=np.int64)

    def idx(self, n):
        k = self._k(n)
        return {'n': np.full(k.size, n, dtype=np.int64), 'k': k, 'n-k': n - k,
                '2k': 2 * k, '2k-n': 2 * k - n, '2n-2k': 2 * (n - k), 'n+k': n + k}

    def Smod(self, n, fac):
        q = fac.q
        k = self._k(n)
        c = fac.b(n, k) * fac.b(2 * k, n) % q
        return c * c % q

    def Sexact(self, n):
        return [comb(n, k) ** 2 * _ebin(2 * k, n) ** 2 for k in range((n + 1) // 2, n + 1)]


class zeta_(Fam):
    """double sum C(n,k)^2 C(n,l) C(k,l) C(k+l,n); support l<=k<=n and k+l>=n."""
    label, w, D = 'zeta', 3, -3
    args = ('n', 'k', 'n-k', 'l', 'n-l', 'k-l', 'k+l', 'k+l-n')
    tame = ('n', 'k', 'n-k', 'l', 'n-l', 'k-l', 'k+l-n')
    note = 'sum_{k,l} C(n,k)^2 C(n,l) C(k,l) C(k+l,n)'

    def _kl(self, n):
        i, j = np.triu_indices(n + 1)
        k, l = j.astype(np.int64), i.astype(np.int64)
        m = (k + l) >= n
        return k[m], l[m]

    def idx(self, n):
        k, l = self._kl(n)
        return {'n': np.full(k.size, n, dtype=np.int64), 'k': k, 'n-k': n - k,
                'l': l, 'n-l': n - l, 'k-l': k - l, 'k+l': k + l, 'k+l-n': k + l - n}

    def Smod(self, n, fac):
        q = fac.q
        k, l = self._kl(n)
        c = fac.b(n, k)
        return (c * c % q * fac.b(n, l) % q * fac.b(k, l) % q * fac.b(k + l, n) % q)

    def Sexact(self, n):
        kk, ll = self._kl(n)
        return [comb(n, int(k)) ** 2 * comb(n, int(l)) * comb(int(k), int(l))
                * _ebin(int(k) + int(l), n) for k, l in zip(kk, ll)]


class eta(Fam):
    """(-1)^k C(n,k)^3 [ C(4n-5k-1,3n) + C(4n-5k,3n) ]; TWO cells per k.
    Cell 0 top = 4n-5k-1, cell 1 top = 4n-5k.  't' = top, 'tb' = top-3n."""
    label, w, D = 'eta', 3, 5
    args = ('n', 'k', 'n-k', '3n', 't', 'tb', '2k', 'n-5k',
            '3k', '4k', '5k', 'n-2k', 'n-3k', 'n-4k')
    tame = ('n', 'k', 'n-k', 'tb', '2k', 'n-5k',
            '3k', '4k', '5k', 'n-2k', 'n-3k', 'n-4k')
    maxtop = 4
    note = 'sum (-1)^k C(n,k)^3 (C(4n-5k-1,3n)+C(4n-5k,3n))'

    def _k(self, n):
        k = np.arange(n // 5 + 1, dtype=np.int64)
        return np.concatenate([k, k]), np.concatenate([np.zeros(k.size, dtype=np.int64),
                                                       np.ones(k.size, dtype=np.int64)])

    def idx(self, n):
        k, j = self._k(n)
        t = 4 * n - 5 * k - 1 + j
        return {'n': np.full(k.size, n, dtype=np.int64), 'k': k, 'n-k': n - k,
                '3n': np.full(k.size, 3 * n, dtype=np.int64), 't': t, 'tb': t - 3 * n,
                '2k': 2 * k, 'n-5k': n - 5 * k, '3k': 3 * k, '4k': 4 * k, '5k': 5 * k,
                'n-2k': n - 2 * k, 'n-3k': n - 3 * k, 'n-4k': n - 4 * k}

    def Smod(self, n, fac):
        q = fac.q
        k, j = self._k(n)
        c = fac.b(n, k)
        s = c * c % q * c % q * fac.b(4 * n - 5 * k - 1 + j, 3 * n) % q
        return np.where(k % 2 == 1, (-s) % q, s)

    def Sexact(self, n):
        out = []
        for j in (0, 1):
            for k in range(n // 5 + 1):
                out.append((-1) ** k * comb(n, k) ** 3 * _ebin(4 * n - 5 * k - 1 + j, 3 * n))
        return out


class s7(Fam):
    label, w, D = 's7', 2, None
    args = ('n', 'k', 'n-k', 'n+k', '2k', '2k-n', '2n-2k')
    tame = ('n', 'k', 'n-k', '2k-n', '2n-2k')
    note = 'Cooper s7  sum C(n,k)^2 C(n+k,k) C(2k,n)'

    def _k(self, n):
        return np.arange((n + 1) // 2, n + 1, dtype=np.int64)

    def idx(self, n):
        k = self._k(n)
        return {'n': np.full(k.size, n, dtype=np.int64), 'k': k, 'n-k': n - k,
                'n+k': n + k, '2k': 2 * k, '2k-n': 2 * k - n, '2n-2k': 2 * (n - k)}

    def Smod(self, n, fac):
        q = fac.q
        k = self._k(n)
        c = fac.b(n, k)
        return c * c % q * fac.b(n + k, k) % q * fac.b(2 * k, n) % q

    def Sexact(self, n):
        return [comb(n, k) ** 2 * comb(n + k, k) * _ebin(2 * k, n)
                for k in range((n + 1) // 2, n + 1)]


class s10(Fam):
    label, w, D = 's10', 2, None
    args = ('n', 'k', 'n-k', 'n+k', '2k', '2n-2k')
    tame = ('n', 'k', 'n-k')
    note = 'Cooper s10  sum C(n,k)^4'

    def idx(self, n):
        k = np.arange(n + 1, dtype=np.int64)
        return {'n': np.full(n + 1, n, dtype=np.int64), 'k': k, 'n-k': n - k,
                'n+k': n + k, '2k': 2 * k, '2n-2k': 2 * (n - k)}

    def Smod(self, n, fac):
        q = fac.q
        k = np.arange(n + 1, dtype=np.int64)
        c = fac.b(n, k)
        c2 = c * c % q
        return c2 * c2 % q

    def Sexact(self, n):
        return [comb(n, k) ** 4 for k in range(n + 1)]


class s18(Fam):
    """(-1)^k C(n,k)C(2k,k)C(2n-2k,n-k)[C(2n-3k-1,n)+C(2n-3k,n)]; two cells per k."""
    label, w, D = 's18', 2, -3
    args = ('n', 'k', 'n-k', '2k', '2n-2k', 't', 'tb', 'n-3k', '3k', 'n-2k')
    tame = ('n', 'k', 'n-k', '2k', 'tb', 'n-3k', '3k', 'n-2k')
    maxtop = 2
    note = 'Cooper s18'

    def _k(self, n):
        k = np.arange(n // 3 + 1, dtype=np.int64)
        return np.concatenate([k, k]), np.concatenate([np.zeros(k.size, dtype=np.int64),
                                                       np.ones(k.size, dtype=np.int64)])

    def idx(self, n):
        k, j = self._k(n)
        t = 2 * n - 3 * k - 1 + j
        return {'n': np.full(k.size, n, dtype=np.int64), 'k': k, 'n-k': n - k,
                '2k': 2 * k, '2n-2k': 2 * (n - k), 't': t, 'tb': t - n, 'n-3k': n - 3 * k,
                '3k': 3 * k, 'n-2k': n - 2 * k}

    def Smod(self, n, fac):
        q = fac.q
        k, j = self._k(n)
        s = fac.b(n, k) * fac.b(2 * k, k) % q * fac.b(2 * (n - k), n - k) % q
        s = s * fac.b(2 * n - 3 * k - 1 + j, n) % q
        return np.where(k % 2 == 1, (-s) % q, s)

    def Sexact(self, n):
        out = []
        for j in (0, 1):
            for k in range(n // 3 + 1):
                out.append((-1) ** k * comb(n, k) * comb(2 * k, k) * comb(2 * (n - k), n - k)
                           * _ebin(2 * n - 3 * k - 1 + j, n))
        return out


FAMS = {}
for _c in (A, Bseq, Cseq, D, E, E2, Fseq, alpha, gamma, delta, eps, zeta_, eta, s7, s10, s18):
    _o = _c()
    FAMS[_o.label] = _o

ORDER = ['A', 'B', 'C', 'D', 'E', 'F', 'alpha', 'gamma', 'delta', 'eps',
         'zeta', 'eta', 's7', 's10', 's18']
