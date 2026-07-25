"""Minimal exact p-adic number with explicit precision:  x = p^v * (u + O(p^prec)),
u a unit mod p^prec (or u==0 meaning "zero to that precision").  All exact ints."""

INF = 10**9      # absolute precision of an EXACT zero

class P:
    __slots__ = ("p", "v", "u", "prec")

    def __init__(self, p, v, u, prec):
        self.p, self.v, self.u, self.prec = p, v, u % p**prec if prec > 0 else 0, prec
        self._norm()

    def _norm(self):
        p = self.p
        if self.prec <= 0:
            self.u = 0; self.prec = 0; return
        if self.u == 0:
            return
        while self.u % p == 0:
            self.u //= p; self.v += 1; self.prec -= 1
            if self.prec == 0:
                self.u = 0; return

    @staticmethod
    def zero(p):
        return P(p, INF, 0, 0)

    @staticmethod
    def from_frac(p, x, prec):
        """x a Fraction/int, exact -> P with the given precision."""
        from fractions import Fraction as Fr
        x = Fr(x)
        if x == 0:
            return P(p, INF, 0, 0)
        num, den = x.numerator, x.denominator
        v = 0
        while num % p == 0: num //= p; v += 1
        while den % p == 0: den //= p; v -= 1
        M = p**prec
        return P(p, v, num % M * pow(den % M, -1, M) % M, prec)

    def is_zero(self):
        return self.u == 0

    def val(self):
        return self.v if self.u else None

    def __add__(self, o):
        p = self.p
        if self.u == 0: return P(p, o.v, o.u, min(o.prec, self.v + self.prec - o.v)) if o.u else P(p, 0, 0, 0)
        if o.u == 0: return P(p, self.v, self.u, min(self.prec, o.v + o.prec - self.v))
        v = min(self.v, o.v)
        # absolute precision = min of absolute precisions
        ap = min(self.v + self.prec, o.v + o.prec)
        prec = ap - v
        if prec <= 0: return P(p, v, 0, 0)
        M = p**prec
        u = (self.u * p**(self.v - v) + o.u * p**(o.v - v)) % M
        return P(p, v, u, prec)

    def __neg__(self):
        return P(self.p, self.v, (-self.u) % self.p**self.prec if self.prec else 0, self.prec)

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        p = self.p
        if isinstance(o, int):
            o = P(p, 0, o % p**max(self.prec, 1), max(self.prec, 1)) if o % p else P.from_frac(p, o, max(self.prec, 1))
        if self.u == 0 or o.u == 0:
            return P(p, self.v + o.v, 0, 0)
        prec = min(self.prec, o.prec)
        return P(p, self.v + o.v, self.u * o.u % p**prec, prec)

    def inv(self):
        p = self.p
        assert self.u, "inverse of zero"
        return P(p, -self.v, pow(self.u, -1, p**self.prec), self.prec)

    def __truediv__(self, o):
        if isinstance(o, int):
            o = P.from_frac(self.p, o, max(self.prec, 1))
        return self * o.inv()

    def trunc(self, n):
        """cap the RELATIVE precision at n digits."""
        n = min(n, self.prec)
        return P(self.p, self.v, self.u % self.p**n if n > 0 else 0, max(n, 0))

    def rescale(self, k):
        """multiply by p^k"""
        return P(self.p, self.v + k, self.u, self.prec)

    def digits(self, m=None):
        m = m or self.prec
        d = []
        r = self.u
        for _ in range(min(m, self.prec)):
            d.append(r % self.p); r //= self.p
        return d

    def __repr__(self):
        return "P(p=%d, v=%d, prec=%d, [%s])" % (
            self.p, self.v, self.prec,
            " ".join(map(str, self.digits(min(self.prec, 12)))))

    def agree(self, o):
        """number of digits of agreement of the two numbers, in ABSOLUTE terms:
           returns v_p(self-o) capped at min absolute precision."""
        d = self - o
        cap = min(self.v + self.prec, o.v + o.prec)
        return cap if d.is_zero() else d.v

    def key(self, n):
        """canonical (v, u mod p^n) for hashing/comparison, n <= prec."""
        assert n <= self.prec, "precision %d < %d" % (self.prec, n)
        return (self.v, self.u % self.p**n)


def fact_unit(n, p, prec):
    """p-free part of n!  mod p^prec  (exact)."""
    M = p**prec
    r = 1
    while n:
        blk = 1
        for m in range(1, n + 1):
            if m % p:
                blk = blk * m % M
        r = r * blk % M
        n //= p
    return r
