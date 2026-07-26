"""The LEFT-HAND SIDE of the certificate: the 42 components of E_{w*}/Phi as
cleared polynomials of Z[n,k,l].  Measured, for the Lean client glue.

  (E_w/Phi)_i = sum_{mj >= mi} w_j sum_{u=0..3} c_u(n) P_u(n,k,l) prod_{L in mj/mi} incn(L,u)

incn(L,u) has denominators (n+j), (n+k+j), (n+l+j), (n+k+l+j) for j = 1,2,3 (the
mk/ml families are already cancelled by P_u's double zeros -- that is (P-int)).
The clearing denominator is computed PER COMPONENT as the max total letter weight
sharing each argument, then the cleared component is interpolated mod p on a
product grid and its monomials are counted.
"""
import sys, os, time, json
from fractions import Fraction as Fr
import numpy as np
HERE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'
sys.path.insert(0, HERE)
sys.path.insert(1, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
sys.path.insert(2, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import wtools as W
import bare, zla

M = 3
FAM = {'n': (1, 0, 0), 'pk': (1, 1, 0), 'pl': (1, 0, 1), 'pkl': (1, 1, 1)}


def divide(mi, mj):
    rest = list(mj)
    for L in mi:
        if L in rest:
            rest.remove(L)
        else:
            return None
    return tuple(sorted(rest))


def exponents(mi, wQ):
    """per-argument clearing exponent = max over quotients of the total weight"""
    E = {a: 0 for a in FAM}
    for mj in wQ:
        rest = divide(mi, mj)
        if rest is None:
            continue
        acc = {a: 0 for a in FAM}
        for L in rest:
            r, a = bare.LETTERS[L]
            if a in FAM:
                acc[a] += r
        for a in FAM:
            E[a] = max(E[a], acc[a])
    return E


def Dc_val(E, n, k, l, p):
    v = 1
    for a, (cn, ck, cl) in FAM.items():
        if not E[a]:
            continue
        for j in (1, 2, 3):
            v = v * pow((cn * n + ck * k + cl * l + j) % p, E[a], p) % p
    return v


def Pm(n, k, l, i, p):
    v = 1
    for j in range(1, i + 1):
        v = v * ((n + j) % p) % p * ((n + k + j) % p) % p \
            * ((n + l + j) % p) % p * ((n + k + l + j) % p) % p
    a = 1; b = 1
    for j in range(i + 1, M + 1):
        a = a * ((n + j - k) % p) % p
        b = b * ((n + j - l) % p) % p
    return v * a % p * a % p * b % p * b % p


def incn(L, n, k, l, aa, p):
    r, a = bare.LETTERS[L]
    cn, ck, cl = bare.ARGS[a]
    d = bare.delta(L, M)
    if cn == 0:
        return 0
    tot = 0
    if aa > d:
        for ii in range(d, aa):
            x = (cn * (n + ii) + ck * k + cl * l + 1) % p
            tot = (tot + pow(pow(x, r, p), p - 2, p)) % p
    elif aa < d:
        for ii in range(aa, d):
            x = (cn * (n + ii) + ck * k + cl * l + 1) % p
            tot = (tot - pow(pow(x, r, p), p - 2, p)) % p
    return tot % p


def comp_val(mi, wQ, E, n, k, l, p, cc):
    s = 0
    for mj, wj in wQ.items():
        rest = divide(mi, mj)
        if rest is None:
            continue
        wjp = int(Fr(wj).numerator) % p * pow(int(Fr(wj).denominator) % p, p - 2, p) % p
        for u in range(4):
            pr = Pm(n, k, l, u, p)
            if not pr:
                continue
            for L in rest:
                pr = pr * incn(L, n, k, l, u, p) % p
                if not pr:
                    break
            if pr:
                s = (s + wjp * (cc[u] % p) % p * pr) % p
    return s * Dc_val(E, n, k, l, p) % p


def interp1(xs, ys, p):
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
    return coef


def measure(mi, wQ, p, verbose=False):
    E = exponents(mi, wQ)
    tot = sum(E.values())
    Dn = 9 + 12 + 3 * tot
    Dk = 6 + 3 * (E['pk'] + E['pkl'])
    Dl = 6 + 3 * (E['pl'] + E['pkl'])
    NS = list(range(60, 60 + Dn + 1))
    KS = list(range(0, Dk + 1))
    LS = list(range(0, Dl + 1))
    cube = {}
    for n in NS:
        cc = zla.cc(n)
        for k in KS:
            ys = [comp_val(mi, wQ, E, n, k, l, p, cc) for l in LS]
            cube[(n, k)] = interp1(LS, ys, p)
    mid = {}
    for n in NS:
        for b in range(Dl + 1):
            ys = [cube[(n, k)][b] for k in KS]
            co = interp1(KS, ys, p)
            for a in range(Dk + 1):
                mid.setdefault((a, b), {})[n] = co[a]
    out = {}
    for (a, b), d in mid.items():
        ys = [d[n] for n in NS]
        co = interp1(NS, ys, p)
        for e, c in enumerate(co):
            if c:
                out[(e, a, b)] = c
    dn = max((m[0] for m in out), default=0)
    dk = max((m[1] for m in out), default=0)
    dl = max((m[2] for m in out), default=0)
    return dict(E=E, nmono=len(out), deg=(dn, dk, dl), bound=(Dn, Dk, Dl))


if __name__ == '__main__':
    p = W.P1
    d = json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
    wQ = {(() if nm == '1' else tuple(nm.split('*'))): Fr(c)
          for nm, c in zip(d['basis'], d['coeffs']) if Fr(c) != 0}
    import itertools
    clo = sorted({tuple(sorted(s)) for m in wQ for r in range(len(m) + 1)
                  for s in itertools.combinations(m, r)},
                 key=lambda m: (len(m), m))
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    print('%-24s %-22s %8s %-14s' % ('component', 'clearing exponents',
                                     'monomials', '(deg_n,deg_k,deg_l)'))
    T = 0
    t0 = time.time()
    for mi in clo:
        nm = '*'.join(mi) if mi else '1'
        if only and nm not in only:
            continue
        r = measure(mi, wQ, p)
        T += r['nmono']
        print('%-24s %-22s %8d %-14s  [%.0fs]'
              % (nm, ''.join('%s^%d ' % (a, e) for a, e in sorted(r['E'].items()) if e),
                 r['nmono'], str(r['deg']), time.time() - t0), flush=True)
    print('TOTAL over %d components: %d monomials' % (len(clo), T))
