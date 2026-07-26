"""Exact-Q checks on the objects the exclusion is stated about.

 (1) w5 as expanded here (27 bare monomials) == zla's independent encoding of
     ZETA5_CLOSEDFORM's w5 (built from the composite letter S2 and the tower
     u3,u4,u5 = H^(r)_{n+k}).
 (2) sum_{k,l=0}^{n} T(n,k,l) w5(n,k,l)  is annihilated by L_BZ, exactly in Q.
 (3) that row is NOT in span_Q{Q_n, Phat_n}: it is the third BZ row.
"""
import sys
from fractions import Fraction as Fr
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5w5')
import zla
import w5span as W


def Hq(r, x, cache={}):
    key = (r, x)
    if key in cache:
        return cache[key]
    s = Fr(0)
    for i in range(1, x + 1):
        s += Fr(1, i ** r)
    cache[key] = s
    return s


def binom(a, b):
    if b < 0 or b > a:
        return 0
    num = 1
    for i in range(b):
        num = num * (a - i) // (i + 1)
    return num


def T(n, k, l):
    return (binom(n + k, n) * binom(n, k) ** 2 * binom(n + l, n)
            * binom(n, l) ** 2 * binom(n + k + l, n))


def evalmono(m, n, k, l):
    v = Fr(1)
    for L in m:
        r, a = W.LETTERS[L]
        cn, ck, cl = W.ARGS[a]
        v *= Hq(r, cn * n + ck * k + cl * l)
    return v


def evalel(el, n, k, l):
    return sum(Fr(c) * evalmono(m, n, k, l) for m, c in el.items())


def zla_w5_eval(n, k, l):
    """zla.weight_element(FQ,'w5') evaluated by substituting the letter values"""
    F = zla.FQ()
    w = zla.weight_element(F, 'w5')
    val = {'xk': Hq(1, k), 'xl': Hq(1, l), 'yk': Hq(1, n - k), 'yl': Hq(1, n - l),
           'zk': Hq(1, n + k), 'zl': Hq(1, n + l),
           'S2': Hq(2, n + k) - Hq(2, k) + Hq(2, n + l) - Hq(2, l)}
    for r in (2, 3, 4, 5):
        val['u%d' % r] = Hq(r, n + k)
    tot = Fr(0)
    for m, c in w.items():
        t = Fr(c)
        for L in m:
            t *= val[L]
        tot += t
    return tot


if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    w5 = W.w5_el()
    w3 = W.w3hat_el()
    print('(1) w5 (this work, %d bare monomials) vs zla weight_element(w5):' % len(w5))
    bad = 0; cells = 0
    for n in range(0, 7):
        for k in range(0, n + 1):
            for l in range(0, n + 1):
                cells += 1
                if evalel(w5, n, k, l) != zla_w5_eval(n, k, l):
                    bad += 1
    print('    %d cells, %d discrepancies' % (cells, bad))
    P = []; Ph = []; Q = []
    for n in range(N + 1):
        sP = Fr(0); sPh = Fr(0); sQ = Fr(0)
        for k in range(n + 1):
            for l in range(n + 1):
                t = T(n, k, l)
                if not t:
                    continue
                sQ += t
                sP += t * evalel(w5, n, k, l)
                sPh += t * evalel(w3, n, k, l)
        P.append(sP); Ph.append(sPh); Q.append(sQ)
        print('    n=%2d  Q=%-14s  Phat=%-22s  P=%s' % (n, sQ, sPh, sP))
    print('(2) L_BZ . (sum T w5) = 0 exactly:')
    bad = 0
    for n in range(N - 2):
        c = zla.cc(n)
        v = sum(Fr(c[i]) * P[n + i] for i in range(4))
        if v != 0:
            bad += 1
            print('    FAIL at n=%d : %s' % (n, v))
    print('    n = 0..%d : %d failures of %d' % (N - 3, bad, N - 2))
    bad = 0
    for n in range(N - 2):
        c = zla.cc(n)
        if sum(Fr(c[i]) * Q[n + i] for i in range(4)) != 0:
            bad += 1
    print('    control L_BZ . Q  : %d failures' % bad)
    bad = 0
    for n in range(N - 2):
        c = zla.cc(n)
        if sum(Fr(c[i]) * Ph[n + i] for i in range(4)) != 0:
            bad += 1
    print('    control L_BZ . Phat : %d failures' % bad)
    print('(3) independence: is P in span{Q, Phat}?')
    import itertools
    M = [[Q[n], Ph[n], P[n]] for n in range(N + 1)]
    # rank over Q by elimination
    rows = [r[:] for r in M]
    rank = 0
    for c in range(3):
        pr = None
        for i in range(rank, len(rows)):
            if rows[i][c] != 0:
                pr = i; break
        if pr is None:
            continue
        rows[rank], rows[pr] = rows[pr], rows[rank]
        pv = rows[rank][c]
        for i in range(len(rows)):
            if i != rank and rows[i][c] != 0:
                f = rows[i][c] / pv
                rows[i] = [rows[i][j] - f * rows[rank][j] for j in range(3)]
        rank += 1
    print('    rank{Q, Phat, P} over n=0..%d  =  %d  (3 means P is a NEW row)'
          % (N, rank))
