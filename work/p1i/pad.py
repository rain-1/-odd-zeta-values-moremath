"""Exact p-adic arithmetic (valuation + unit, tracked precision) and a w5 evaluator.

A number is stored as (v, u, prec):
    value = p^v * u + O(p^{v+prec}),   0 <= u < p^prec,   p does not divide u,
or as the "zero-ish" element (V, 0, 0) meaning  value in p^V Z_p.
All arithmetic is exact in the sense that the reported valuation is never wrong:
the precision bookkeeping is the standard one.
"""
import json, sys
from fractions import Fraction as F

INF = 10 ** 9


class Ctx:
    def __init__(self, p, K=60):
        self.p = p
        self.K = K
        self.pw = [p ** i for i in range(K + 40)]

    # ---- constructors -------------------------------------------------
    def zero(self, V=None):
        return (self.K if V is None else V, 0, 0)

    def fromint(self, x, prec=None):
        p = self.p
        prec = self.K if prec is None else prec
        if x == 0: return (prec, 0, 0)
        v = 0
        while x % p == 0:
            x //= p; v += 1
        return (v, x % self.pw[prec], prec)

    def fromfrac(self, fr, prec=None):
        p = self.p
        prec = self.K if prec is None else prec
        num, den = fr.numerator, fr.denominator
        if num == 0: return (prec, 0, 0)
        v = 0
        while num % p == 0: num //= p; v += 1
        while den % p == 0: den //= p; v -= 1
        m = self.pw[prec]
        return (v, (num % m) * pow(den, -1, m) % m, prec)

    # ---- arithmetic ---------------------------------------------------
    def mul(self, x, y):
        v1, u1, p1 = x; v2, u2, p2 = y
        if u1 == 0 and u2 == 0: return (v1 + v2, 0, 0)
        if u1 == 0: return (v1 + v2, 0, 0)
        if u2 == 0: return (v1 + v2, 0, 0)
        pr = p1 if p1 < p2 else p2
        return (v1 + v2, u1 * u2 % self.pw[pr], pr)

    def add(self, x, y):
        v1, u1, p1 = x; v2, u2, p2 = y
        a1 = v1 + p1; a2 = v2 + p2          # absolute precisions
        A = a1 if a1 < a2 else a2
        if u1 == 0 and u2 == 0: return (A, 0, 0)
        v = v1 if v1 < v2 else v2
        if v > A: return (A, 0, 0)
        S = (u1 * self.pw[v1 - v] if u1 else 0) + (u2 * self.pw[v2 - v] if u2 else 0)
        S %= self.pw[A - v]
        p_ = self.p
        while S and S % p_ == 0:
            S //= p_; v += 1
        pr = A - v
        if S == 0 or pr <= 0: return (A, 0, 0)
        return (v, S % self.pw[pr], pr)

    def sub(self, x, y):
        v2, u2, p2 = y
        return self.add(x, (v2, (-u2) % self.pw[p2] if u2 else 0, p2))

    def val(self, x):
        """valuation; for zero-ish returns (V, True) meaning 'only known >= V'."""
        v, u, pr = x
        return v if u else v            # for zero-ish v is the absolute precision

    def is_exactzero(self, x):
        return x[1] == 0


# ---------------------------------------------------------------------
# harmonic numbers, letters, w5
# ---------------------------------------------------------------------
def load_w5(fn):
    d = json.load(open(fn)); terms = []
    for lab, (num, den) in d.items():
        fg, rest = lab.split(']x'); f, g = fg[1:].split('|'); h, s = rest.split('x')
        sp = lambda x: [] if x == '1' else x.split('*')
        terms.append((F(num, den), sp(f), sp(g), sp(h), sp(s)))
    return terms


class Level:
    """all harmonic data for one level n, prime p."""

    def __init__(self, ctx, n, terms):
        self.ctx = ctx; self.n = n; self.terms = terms
        p = ctx.p; K = ctx.K
        Nmax = 3 * n + 2
        m = ctx.pw[K]
        # prefix sums over j <= x with p ndiv j  of j^{-r}, r=1..5, mod p^K
        PS = [[0] * (Nmax + 1) for _ in range(6)]
        for j in range(1, Nmax + 1):
            if j % p:
                ij = pow(j, -1, m)
                pw = 1
                for r in range(1, 6):
                    pw = pw * ij % m
                    PS[r][j] = pw
        for r in range(1, 6):
            row = PS[r]
            acc = 0
            for j in range(1, Nmax + 1):
                acc = (acc + row[j]) % m
                row[j] = acc
        self.PS = PS
        self.Hcache = {}

    def H(self, N, r):
        """H^{(r)}_N as a p-adic."""
        key = (N, r)
        v = self.Hcache.get(key)
        if v is not None: return v
        ctx = self.ctx; p = ctx.p
        out = ctx.zero(ctx.K)
        e = 0; q = N
        while q > 0:
            s = self.PS[r][q]
            t = ctx.fromint(s, ctx.K) if s else ctx.zero(ctx.K)
            t = (t[0] - e * r, t[1], t[2])
            out = ctx.add(out, t)
            e += 1; q //= p
        self.Hcache[key] = out
        return out

    def letters(self, k, l):
        """dict of the 6 letter families at cell (k,l)."""
        n = self.n; ctx = self.ctx
        A_k = [None] + [ctx.sub(self.H(n + k, r), self.H(k, r)) for r in range(1, 6)]
        A_l = [None] + [ctx.sub(self.H(n + l, r), self.H(l, r)) for r in range(1, 6)]
        B_k = [None] + [ctx.sub(self.H(n - k, r), self.H(k, r)) for r in range(1, 6)]
        B_l = [None] + [ctx.sub(self.H(n - l, r), self.H(l, r)) for r in range(1, 6)]
        C_ = [None] + [ctx.sub(self.H(n + k + l, r), self.H(k + l, r)) for r in range(1, 6)]
        N_ = [None] + [self.H(n, r) for r in range(1, 6)]
        return A_k, A_l, B_k, B_l, C_, N_

    def v5(self, k, l):
        """v5(n,k,l) = w5(n,k,l) - H^{(5)}_n  as a p-adic."""
        ctx = self.ctx
        A_k, A_l, B_k, B_l, C_, N_ = self.letters(k, l)
        def slot(nm, which):
            t = nm[0]; r = int(nm[1])
            if which == 0:
                return A_k[r] if t == 'A' else B_k[r]
            return A_l[r] if t == 'A' else B_l[r]
        tot = ctx.zero(ctx.K)
        for cf, f, g, h, s in self.terms:
            v = ctx.fromfrac(cf)
            for nm in h: v = ctx.mul(v, C_[int(nm[1])])
            for nm in s: v = ctx.mul(v, N_[int(nm[1])])
            pf = v
            for nm in f: pf = ctx.mul(pf, slot(nm, 0))
            for nm in g: pf = ctx.mul(pf, slot(nm, 1))
            tot = ctx.add(tot, pf)
            if f != g:
                pb = v
                for nm in f: pb = ctx.mul(pb, slot(nm, 1))
                for nm in g: pb = ctx.mul(pb, slot(nm, 0))
                tot = ctx.add(tot, pb)
        return ctx.sub(tot, N_[5])
