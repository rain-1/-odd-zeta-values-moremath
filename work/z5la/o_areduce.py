"""Fast degree determination for a_t(n)/a_0(n): one nullspace at a generous
degree bound, then cancel by polynomial gcd mod p.  (null_min_deg's search from
d = 0 is O(maxdeg) nullspaces and is far too slow at these degrees.)"""
import pickle, sys
import numpy as np
import ratrec


def pdivmod(a, b, p):
    a = list(a); db = len(b) - 1
    inv = pow(b[db] % p, p - 2, p)
    q = [0] * max(0, len(a) - db)
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i] * inv % p
        q[i - db] = c
        if c:
            for j in range(db + 1):
                a[i - db + j] = (a[i - db + j] - c * b[j]) % p
    return ratrec.trim(q), ratrec.trim(a[:db] if db else [0])


def pgcd(a, b, p):
    a = ratrec.trim(a); b = ratrec.trim(b)
    while len(b) > 1 or b[0] % p:
        _, r = pdivmod(a, b, p)
        a, b = b, r
    return a


def recon(vals, xs, p, d):
    M = len(xs); nc = 2 * (d + 1)
    assert M > nc, (M, nc)
    A = np.zeros((M, nc), dtype=np.int64)
    for t, x in enumerate(xs):
        xp = 1
        for j in range(d + 1):
            A[t, j] = xp
            A[t, d + 1 + j] = (-vals[t] * xp) % p
            xp = xp * (x % p) % p
    ns = ratrec.nullspace(A, p)
    if not ns: return None
    v = ns[0]
    num = ratrec.trim(v[:d + 1]); den = ratrec.trim(v[d + 1:])
    g = pgcd(num, den, p)
    if len(g) > 1:
        num, _ = pdivmod(num, g, p)
        den, _ = pdivmod(den, g, p)
    return num, den


if __name__ == '__main__':
    fn = sys.argv[1] if len(sys.argv) > 1 else 'a_sweep.pkl'
    d = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    D = pickle.load(open(fn, 'rb'))
    p = 4194301
    xs = sorted(n for (n, q) in D if q == p and D[(n, q)] is not None)
    print('prime %d, %d samples n = %d .. %d' % (p, len(xs), min(xs), max(xs)), flush=True)
    if d == 0: d = len(xs) // 2 - 3
    for t in range(1, 5):
        vals = [D[(n, p)][t] for n in xs]
        r = recon(vals, xs, p, d)
        if r is None:
            print('a_%d/a_0 : no relation at d <= %d' % (t, d), flush=True); continue
        num, den = r
        ok = all(ratrec.polyval(num, x % p, p) == vals[i] * ratrec.polyval(den, x % p, p) % p
                 for i, x in enumerate(xs))
        print('a_%d/a_0 : deg num = %3d , deg den = %3d   (fits all %d samples: %s)'
              % (t, len(num) - 1, len(den) - 1, len(xs), ok), flush=True)
