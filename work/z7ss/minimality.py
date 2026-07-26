"""Is the order-4 operator for q_n minimal?  Test lower orders modulo a large prime,
using the 106 modular terms q_0..q_105 mod p = 2000000011.
"""
import sys

P = 2000000011
F = "/home/ubuntu/fable-episode-2/zeta-math/worthiness/_zeta7_state_backup/fleet_2000000011.txt"


def load():
    d = {}
    for line in open(F):
        line = line.strip()
        if not line or "=" not in line:
            continue
        a, b = line.split("=")
        d[int(a)] = int(b) % P
    return [d[i] for i in range(len(d))]


def nullity(seq, order, deg, p):
    ncol = (order + 1) * (deg + 1)
    N = len(seq) - order
    if N < ncol + 2:
        return None
    rows = []
    for n in range(N):
        npow = [pow(n, d, p) for d in range(deg + 1)]
        row = []
        for j in range(order + 1):
            v = seq[n + j] % p
            for d in range(deg + 1):
                row.append(v * npow[d] % p)
        rows.append(row)
    m = len(rows)
    r = 0
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
        r += 1
    return ncol - r


if __name__ == "__main__":
    seq = load()
    print("modular terms:", len(seq))
    for order in range(1, 5):
        best = None
        for deg in range(0, 40):
            ncol = (order + 1) * (deg + 1)
            if len(seq) - order < ncol + 2:
                print(f"  order={order}: exhausted at deg={deg} "
                      f"(need {ncol+2} rows, have {len(seq)-order})")
                break
            nu = nullity(seq, order, deg, P)
            if nu:
                print(f"  order={order} deg={deg}: NULLITY {nu}  <-- recurrence exists")
                best = (deg, nu)
                break
        if best:
            print("   ->", order, best)
