"""Reconstruct  A(n) = sum_{t=0}^{4} a_t(n) S_n^t  exactly.

The a-direction is unique up to scale at every n, so a_t/a_0 is a well-defined
rational function of n.  Reconstruct it mod several primes (denominator made
monic, which is a canonical normalisation over Q as well), CRT the coefficients
and lift them to Q.
"""
import os, sys, time, pickle
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('MKL_NUM_THREADS', '1')
from fractions import Fraction as Fr
import numpy as np

PRIMES = [4194301, 4194287, 4194277, 4194271, 4194247, 4194217, 4194199, 4194191]
SLACK = 16
M = 7


def one(args):
    n, p = args
    import o_scan
    r = o_scan.run('w3', n, M, 'E1', SLACK, p=p, verbose=False)
    if len(r['inter']) != 1: return (n, p, None)
    v = [int(x) % p for x in r['inter'][0]]
    inv = pow(v[0], p - 2, p) if v[0] else None
    if inv is None: return (n, p, None)
    return (n, p, [x * inv % p for x in v])


def sweep(ps, ns, nproc=11):
    from multiprocessing import Pool
    jobs = [(n, p) for p in ps for n in ns]
    out = {}
    with Pool(nproc) as pool:
        for n, p, v in pool.imap_unordered(one, jobs):
            out[(n, p)] = v
    return out


# --------------------------------------------------------- rational recon ---

def ratfun(vals, xs, p, maxdeg=60):
    import ratrec
    r = ratrec.null_min_deg(vals, xs, p, maxdeg)
    if r is None: return None
    num, den = r
    lead = den[-1]
    iv = pow(lead % p, p - 2, p)
    return ([c * iv % p for c in num], [c * iv % p for c in den])


def crt(rs, ms):
    M0 = 1; x = 0
    for r, m in zip(rs, ms):
        g = pow(M0 % m, m - 2, m)
        t = (r - x) % m * g % m
        x += M0 * t
        M0 *= m
    return x % M0, M0


def ratlift(a, m):
    """recover u/v with |u|,|v| <= sqrt(m/2) from a = u/v mod m"""
    import math
    bound = int(math.isqrt(m // 2))
    r0, r1 = m, a % m
    s0, s1 = 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound: return None
    return Fr(r1 if s1 > 0 else -r1, abs(s1))


if __name__ == '__main__':
    ns = list(range(3, 3 + 96))
    nprimes = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    ps = PRIMES[:nprimes]
    t0 = time.time()
    data = sweep(ps, ns)
    ok = {p: [n for n in ns if data[(n, p)] is not None] for p in ps}
    print('samples per prime: %s   [%.0fs]' % ({p: len(v) for p, v in ok.items()},
                                               time.time() - t0), flush=True)
    pickle.dump(data, open('a_sweep.pkl', 'wb'))
    recon = {}
    for t in range(1, 5):
        percoef = {}
        deg = None
        good = True
        for p in ps:
            xs = ok[p]
            vals = [data[(n, p)][t] for n in xs]
            r = ratfun(vals, xs, p)
            if r is None:
                print('a_%d: reconstruction FAILED mod %d' % (t, p)); good = False; break
            num, den = r
            if deg is None: deg = (len(num), len(den))
            elif deg != (len(num), len(den)):
                print('a_%d: degree mismatch %s vs %s' % (t, deg, (len(num), len(den))))
                good = False; break
            percoef[p] = (num, den)
        if not good: continue
        num_q = []; den_q = []
        for which, idx in (('num', 0), ('den', 1)):
            outl = []
            L = len(percoef[ps[0]][idx])
            for j in range(L):
                rs = [percoef[p][idx][j] for p in ps]
                x, Mod = crt(rs, ps)
                q = ratlift(x, Mod)
                outl.append(q)
            if idx == 0: num_q = outl
            else: den_q = outl
        recon[t] = (num_q, den_q)
        bad = sum(1 for c in num_q + den_q if c is None)
        print('a_%d/a_0 : deg num=%d deg den=%d   unlifted coefficients: %d'
              % (t, len(num_q) - 1, len(den_q) - 1, bad), flush=True)
    pickle.dump(recon, open('a_recon.pkl', 'wb'))
