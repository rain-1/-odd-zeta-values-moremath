"""Weight-5 BZ analogue Q_n = sum_{k1,k2} C(n+k1,n)C(n,k1)^2 C(n+k2,n)C(n,k2)^2 C(n+k1+k2,n).
Find minimal (order,degree) recurrence by modular linear algebra.  Structural comparison
with the weight-7 q_n operator (order 4, deg 19).
"""
from math import comb
import sys

P = (1 << 61) - 1  # prime


def Qmod(n, p):
    s = 0
    for k1 in range(n + 1):
        w1 = comb(n + k1, n) * comb(n, k1) ** 2 % p
        acc = 0
        for k2 in range(n + 1):
            w2 = comb(n + k2, n) * comb(n, k2) ** 2 % p
            acc = (acc + w2 * comb(n + k1 + k2, n)) % p
        s = (s + w1 * acc) % p
    return s


def nullity(seq, order, deg, p, nrows=None):
    ncol = (order + 1) * (deg + 1)
    N = len(seq) - order
    if nrows is None:
        nrows = N
    nrows = min(nrows, N)
    if nrows < ncol + 3:
        return None
    rows = []
    for n in range(nrows):
        row = []
        npow = [pow(n, d, p) for d in range(deg + 1)]
        for j in range(order + 1):
            v = seq[n + j] % p
            for d in range(deg + 1):
                row.append(v * npow[d] % p)
        rows.append(row)
    m = len(rows)
    r = 0
    piv = []
    for c in range(ncol):
        pr = None
        for i in range(r, m):
            if rows[i][c]:
                pr = i
                break
        if pr is None:
            continue
        rows[r], rows[pr] = rows[pr], rows[r]
        inv = pow(rows[r][c], p - 2, p)
        rows[r] = [x * inv % p for x in rows[r]]
        for i in range(r + 1, m):
            if rows[i][c]:
                f = rows[i][c]
                rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[r])]
        piv.append(c)
        r += 1
    return ncol - r


if __name__ == "__main__":
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    seq = [Qmod(n, P) for n in range(NMAX)]
    print("terms:", NMAX)
    found = []
    for order in range(1, 7):
        for deg in range(0, 25):
            ncol = (order + 1) * (deg + 1)
            if len(seq) - order < ncol + 3:
                break
            nu = nullity(seq, order, deg, P)
            if nu and nu > 0:
                print(f"weight-5 Q_n: order={order} deg={deg} nullity={nu}")
                found.append((order, deg, nu))
                break
        if found:
            break
    if not found:
        print("no recurrence found in searched box")
