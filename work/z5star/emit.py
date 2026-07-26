"""JOB 3/4 -- lift the cofactors to Z[n,k,l] and emit them in the sparse format
the reflective checker wants:  per block, a list  [[e_n, e_k, e_l], c]  with
c in Z, plus the cleared common denominator.

Normalisation delivered (see Z5STAR_CERT 5):

    rho_j(n,k,l) = Nr_j(n,k,l) / ( dn(n) * D(n,k,l) * scale )
    sig_j(n,k,l) = Ns_j(n,k,l) / ( dn(n) * D(n,k,l) * scale )

    D(n,k,l) = (k+l+1)(n+k+1)(n+k+2)(n+k+3)(n+l+1)(n+l+2)(n+l+3)      [MEASURED]
    dn(n)    = n (n+1)^4 (n+2)^4 (n+3)^2 (n+4)^2 (n+5)^2 (n+6)^2 (n+7)^2   [MEASURED]

The polynomial P_j(n) attached to each (k,l)-monomial is obtained by INTERPOLATION
of  value(n) * dn(n)  through the sweep points -- no rational reconstruction is
needed once dn is known, which is both faster and self-checking (the interpolant
must have degree below the number of samples and must reproduce held-out points).
"""
import os, sys, time, pickle, json
from fractions import Fraction as Fr
import numpy as np
HERE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'
sys.path.insert(0, HERE)
sys.path.insert(1, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')

DN = [(0, 1), (-1, 4), (-2, 4), (-3, 2), (-4, 2), (-5, 2), (-6, 2), (-7, 2)]
DN_STR = 'n*(n+1)^4*(n+2)^4*(n+3)^2*(n+4)^2*(n+5)^2*(n+6)^2*(n+7)^2'
D_STR = '(k+l+1)*(n+k+1)*(n+k+2)*(n+k+3)*(n+l+1)*(n+l+2)*(n+l+3)'


def dn_val(n):
    v = 1
    for r, m in DN:
        v *= (n - r) ** m
    return v


def interp(xs, ys, p):
    """Newton interpolation mod p; returns the coefficient list (ascending)."""
    n = len(xs)
    dd = list(ys)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            dd[i] = (dd[i] - dd[i - 1]) * pow((xs[i] - xs[i - j]) % p, p - 2, p) % p
    coef = [0] * n
    cur = [1] + [0] * (n - 1)
    for j in range(n):
        for t in range(n):
            coef[t] = (coef[t] + dd[j] * cur[t]) % p
        if j + 1 < n:
            new = [0] * n
            for t in range(n - 1, 0, -1):
                new[t] = (new[t] + cur[t - 1]) % p
            for t in range(n):
                new[t] = (new[t] - xs[j] * cur[t]) % p
            cur = new
    while len(coef) > 1 and coef[-1] == 0:
        coef.pop()
    return coef


def crt(rs, ms):
    M0 = 1; x = 0
    for r, m in zip(rs, ms):
        g = pow(M0 % m, m - 2, m)
        t = (r - x) % m * g % m
        x += M0 * t
        M0 *= m
    return x % M0, M0


def ratlift(a, m):
    import math
    bound = math.isqrt(m // 2)
    r0, r1 = m, a % m
    s0, s1 = 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound:
        return None
    return Fr(r1 if s1 > 0 else -r1, abs(s1))


def main(fn, nhold=8):
    d = pickle.load(open(os.path.join(HERE, fn), 'rb'))
    data, ns, ps = d['data'], d['ns'], d['ps']
    xs_all = sorted({n for (n, p) in data if data[(n, p)] is not None})
    fit = xs_all[:-nhold]
    hold = xs_all[-nhold:]
    print('primes %d, fit points %d, held out %d' % (len(ps), len(fit), len(hold)),
          flush=True)
    NCOL = len(data[(fit[0], ps[0])])
    polys = {}                      # (prime, col) -> coefficient list
    t0 = time.time()
    for p in ps:
        dnv = [dn_val(n) % p for n in fit]
        Mv = np.array([data[(n, p)] for n in fit], dtype=np.int64)
        for c in range(NCOL):
            col = Mv[:, c]
            if not col.any():
                polys[(p, c)] = [0]
                continue
            ys = [int(col[i]) * dnv[i] % p for i in range(len(fit))]
            polys[(p, c)] = interp(fit, ys, p)
        print('   prime %d done [%.0fs]' % (p, time.time() - t0), flush=True)
    # ---- held-out check, per prime
    bad = 0
    for p in ps:
        for n in hold:
            v = data.get((n, p))
            if v is None:
                continue
            for c in range(NCOL):
                cf = polys[(p, c)]
                acc = 0
                for a in reversed(cf):
                    acc = (acc * n + a) % p
                if acc != int(v[c]) * dn_val(n) % p:
                    bad += 1
    print('HELD-OUT check: %d mismatches over %d points x %d coefficients x %d primes'
          % (bad, len(hold), NCOL, len(ps)), flush=True)
    # ---- degree agreement across primes, then CRT + rational lift
    degs = {}
    mism = 0
    for c in range(NCOL):
        ls = {len(polys[(p, c)]) for p in ps}
        if len(ls) > 1:
            mism += 1
        degs[c] = max(ls) - 1
    print('degree mismatch across primes for %d coefficients' % mism, flush=True)
    out = {}
    unl = 0
    for c in range(NCOL):
        L = degs[c] + 1
        vec = []
        for j in range(L):
            rs = [polys[(p, c)][j] if j < len(polys[(p, c)]) else 0 for p in ps]
            x, M = crt(rs, ps)
            q = ratlift(x, M)
            if q is None:
                unl += 1
                q = Fr(0)
                vec.append(None)
            else:
                vec.append(q)
        out[c] = vec
    print('unliftable coefficients: %d  [%.0fs]' % (unl, time.time() - t0), flush=True)
    pickle.dump(dict(out=out, degs=degs, fit=fit, hold=hold, ps=ps),
                open(os.path.join(HERE, 'lift_Q.pkl'), 'wb'))
    return out, degs


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'nsweep_6p.pkl',
         int(sys.argv[2]) if len(sys.argv) > 2 else 8)
