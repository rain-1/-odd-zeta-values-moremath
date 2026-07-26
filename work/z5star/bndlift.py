"""Lift the boundary certificate Nu(n,j) to Z[n,j] by CRT over the same primes.

Nu(n,j) = sum_{t=0}^{12} c_t(n) j^t ;  c_t is reconstructed as a rational function
of n mod each prime, put over the common denominator dnb(n), interpolated, and
CRT-lifted.  Same self-describing output shape as the cofactors.
"""
import os, sys, time, pickle, json
os.environ.setdefault('OMP_NUM_THREADS', '1')
from fractions import Fraction as Fr
from math import gcd
import numpy as np
HERE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'
sys.path.insert(0, HERE)
sys.path.insert(1, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import ratrec
from emit import interp, crt, ratlift


def pmul(a, b, p):
    o = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                o[i + j] = (o[i + j] + x * y) % p
    return ratrec.trim(o)


def pmod(a, b, p):
    a = list(a); db = len(b) - 1; ib = pow(b[-1] % p, p - 2, p)
    while len(a) - 1 >= db and any(a):
        d = len(a) - 1
        if a[-1] == 0:
            a.pop(); continue
        c = a[-1] * ib % p
        for i in range(db + 1):
            a[d - db + i] = (a[d - db + i] - c * b[i]) % p
        a.pop()
    return ratrec.trim(a)


def pgcd(a, b, p):
    a = ratrec.trim(a); b = ratrec.trim(b)
    while len(b) > 1 or (len(b) == 1 and b[0]):
        a, b = b, pmod(a, b, p)
    return a


def pdiv(a, b, p):
    a = list(a); db = len(b) - 1; ib = pow(b[-1] % p, p - 2, p); q = [0] * (len(a) - db)
    while len(a) - 1 >= db:
        d = len(a) - 1
        if a[-1] == 0:
            a.pop(); continue
        c = a[-1] * ib % p; q[d - db] = c
        for i in range(db + 1):
            a[d - db + i] = (a[d - db + i] - c * b[i]) % p
        a.pop()
    return ratrec.trim(q)


if __name__ == '__main__':
    d = pickle.load(open(os.path.join(HERE, 'bndsweep.pkl'), 'rb'))
    data, ns, ps = d['data'], d['ns'], d['ps']
    NU = d['DEGJ'] + 1
    p0 = ps[0]
    xs = [n for n in ns if data.get((n, p0)) is not None]
    print('boundary lift: %d sample n, %d primes, %d coefficients'
          % (len(xs), len(ps), NU), flush=True)
    # --- common n-denominator from the first prime
    L = [1]
    degs = []
    for t in range(NU):
        vals = [int(data[(n, p0)][t]) for n in xs]
        if not any(vals):
            degs.append((None, None)); continue
        r = ratrec.null_min_deg(vals, xs, p0, 60)
        if r is None:
            print('   coefficient %d: reconstruction FAILED' % t); degs.append((None, None)); continue
        num, den = r
        degs.append((len(num) - 1, len(den) - 1))
        if len(den) > 1:
            g = pgcd(L, den, p0)
            L = pmul(L, pdiv(den, g, p0), p0)
    print('   deg(num)/deg(den) per coefficient:', degs, flush=True)
    print('   common n-denominator degree = %d' % (len(L) - 1), flush=True)
    roots = []
    for a in range(-90, 91):
        if ratrec.polyval(L, a % p0, p0) == 0:
            cur = list(L); m = 0
            while len(cur) > 1 and ratrec.polyval(cur, a % p0, p0) == 0:
                cur, _ = ratrec.divide_out(cur, a % p0, p0); m += 1
            roots.append((a, m))
    print('   integer roots (n = r, multiplicity):', roots,
          '-> accounted %d of %d' % (sum(m for _, m in roots), len(L) - 1), flush=True)

    def dnb(n):
        v = 1
        for r, m in roots:
            v *= (n - r) ** m
        return v
    # --- interpolate  c_t(n)*dnb(n)  per prime, CRT, lift
    nhold = 6
    fit = xs[:-nhold]; hold = xs[-nhold:]
    polys = {}
    for p in ps:
        dv = [dnb(n) % p for n in fit]
        for t in range(NU):
            ys = [int(data[(n, p)][t]) * dv[i] % p for i, n in enumerate(fit)]
            polys[(p, t)] = interp(fit, ys, p)
    bad = 0
    for p in ps:
        for n in hold:
            v = data.get((n, p))
            if v is None:
                continue
            for t in range(NU):
                acc = 0
                for a in reversed(polys[(p, t)]):
                    acc = (acc * n + a) % p
                if acc != int(v[t]) * dnb(n) % p:
                    bad += 1
    print('   HELD-OUT: %d mismatches over %d x %d x %d identities'
          % (bad, len(hold), NU, len(ps)), flush=True)
    D = max(len(polys[(p, t)]) for p in ps for t in range(NU)) - 1
    out = {}
    unl = 0
    for t in range(NU):
        vec = []
        for e in range(D + 1):
            rs = [polys[(p, t)][e] if e < len(polys[(p, t)]) else 0 for p in ps]
            x, M = crt(rs, ps)
            q = ratlift(x, M)
            if q is None:
                unl += 1
            vec.append(q)
        out[t] = vec
    print('   unliftable: %d of %d' % (unl, NU * (D + 1)), flush=True)
    terms = []
    for t, vec in out.items():
        for e, q in enumerate(vec):
            if q is not None and q != 0:
                terms.append(((e, t), q))
    den = 1
    for _, q in terms:
        den = den * q.denominator // gcd(den, q.denominator)
    ints = [(m, int(q * den)) for m, q in terms]
    g = 0
    for _, v in ints:
        g = gcd(g, abs(v))
    if g > 1:
        ints = [(m, v // g) for m, v in ints]
        den = Fr(den, g)
    dn_ = max(m[0] for m, _ in ints); dj = max(m[1] for m, _ in ints)
    bits = max(abs(v).bit_length() for _, v in ints)
    jmon = len({m[1] for m, _ in ints})
    print('   Nu: %d monomials, bidegree (n,j) = (%d,%d), %d distinct j-powers, '
          'max coefficient %d bits, scale %s'
          % (len(ints), dn_, dj, jmon, bits, den), flush=True)
    doc = dict(
        what='boundary certificate for the () collapse class of the w* order-3 '
             'certificate, in the (B-bot)-satisfying gauge',
        identity='g(j)*u(n,j+1) - u(n,j) = R(n,j),  R = rho_()(n,0,j) + sigma_()(n,j,0)',
        g='(n+3-j)^2*(n+j+1)^2/(j+1)^4',
        u='Nu(n,j) / ( (j+1)*(n+j+1)*(n+j+2)*(n+j+3) * dnb(n) * scale )',
        dnb='*'.join('(n%+d)^%d' % (-r, m) for r, m in roots) if roots else '1',
        scale=str(den),
        monomial_key='[e_n, e_j]',
        boundary='G(n,j) = Phi(n,0,j)*u(n,j) ; G(n,n+4) = 0 since Phi(n,0,n+4) = 0 '
                 '(C(n+3,n+4) = 0) ; G(n,0) = 0 since u(n,0) = 0',
        unliftable_coefficients=unl,
        WARNING='COMPLETE' if unl == 0 else 'INCOMPLETE',
        terms=[[list(m), v] for m, v in sorted(ints)])
    json.dump(doc, open(os.path.join(HERE, 'CERT_boundary_sparse.json'), 'w'), indent=1)
    print('   written CERT_boundary_sparse.json', flush=True)
