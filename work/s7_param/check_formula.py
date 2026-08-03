"""Independent exact checks for the compact Cooper s_7 companion formula."""

from fractions import Fraction as Q
from math import comb


def H(n, r=1):
    return sum((Q(1, j**r) for j in range(1, n + 1)), Q(0))


def shell(n, k):
    if 2 * k < n:
        return 0
    return comb(n, k) ** 2 * comb(n + k, k) * comb(2 * k, n)


def A(n):
    return sum(shell(n, k) for k in range(n + 1))


def V(n):
    return sum(
        shell(n, k) * (2 * H(2 * k) - 3 * H(k) + H(n - k))
        for k in range(n + 1)
    )


def closed_B(n):
    out = Q(0)
    for k in range(n + 1):
        s = shell(n, k)
        delta = H(k) - H(n - k)
        theta = H(2 * k) - H(k)
        numerator = (
            3 * delta * (2 * theta - delta)
            + 5 * H(k, 2)
            + 2 * H(n, 2)
            - 3 * H(n - k, 2)
        )
        out += s * numerator / 28
    return out


def recurrence_B(N):
    out = [Q(0), Q(1)]
    for n in range(1, N):
        nxt = (
            (2 * n + 1) * (13 * n * n + 13 * n + 4) * out[n]
            + 3 * n * (9 * n * n - 1) * out[n - 1]
        ) / (n + 1) ** 3
        out.append(nxt)
    return out


def vp_integer(x, p):
    if x == 0:
        return 10**9
    out = 0
    while x % p == 0:
        x //= p
        out += 1
    return out


def vp(x, p):
    return vp_integer(x.numerator, p) - vp_integer(x.denominator, p)


if __name__ == "__main__":
    N = 130
    rec = recurrence_B(N)
    for n in range(51):
        assert V(n) == 0, ("V", n, V(n))
        assert closed_B(n) == rec[n], ("B", n, closed_B(n), rec[n])
    print("exact V_n=0 and compact B_n formula verified for 0 <= n <= 50")

    for p in (3, 5, 11):
        for a in range(p):
            for r in range(p):
                difference = p**2 * rec[a * p + r] - rec[a] * A(r)
                assert vp(difference, p) >= 1, ("Lucas", p, a, r, difference)
    print("p^2 companion Lucas law independently checked for p = 3, 5, 11")
