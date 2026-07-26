"""Lift  A(n) = sum_{t=0}^{4} a_t(n) S_n^t  to Z[n], exactly.

Method (extends o_areco / o_areduce):

  * per prime p, reconstruct r_t = a_t/a_0 as a REDUCED rational function
    N_t/D_t (one nullspace + polynomial gcd, o_areduce.recon), then normalise
    D_t monic.  This is a canonical normalisation over Q as well.
  * Lambda := monic lcm(D_1..D_4).  Because gcd(A_0,..,A_4) = 1 for the
    primitive integer vector, lcm_t (A_0/gcd(A_0,A_t)) = A_0 up to a scalar, so
        V := ( Lambda, Lambda*N_1/D_1, ..., Lambda*N_4/D_4 )  ==  (A_0..A_4)/lc(A_0)
    exactly, as an identity of vectors of rational polynomials.  Hence the
    mod-p reductions of V at different primes CRT consistently.
  * CRT + rational lift the coefficients of V, then clear denominators and take
    the primitive integer vector.

Verification is against primes that took no part in the fit.
"""
import os, sys, pickle, time
from fractions import Fraction as Fr
import numpy as np
import ratrec
import o_areduce
from o_areduce import pdivmod, pgcd


# ------------------------------------------------------------ poly mod p ----

def pmul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % p
    return ratrec.trim(out)


def pmonic(a, p):
    iv = pow(a[-1] % p, p - 2, p)
    return [c * iv % p for c in a]


def plcm(a, b, p):
    g = pgcd(a, b, p)
    q, r = pdivmod(a, g, p)
    assert len(r) == 1 and r[0] % p == 0, 'lcm: gcd does not divide'
    return pmonic(pmul(q, b, p), p)


# --------------------------------------------------- per-prime polynomial ---

def vec_mod_p(D, p, xs, dbound, verbose=False):
    """the 5 polynomials  V_0..V_4  mod p  (V_0 = Lambda monic)."""
    nums = {}; dens = {}
    for t in range(1, 5):
        vals = [D[(n, p)][t] for n in xs]
        r = o_areduce.recon(vals, xs, p, dbound)
        if r is None: return None, 'no relation at d<=%d' % dbound
        num, den = r
        ok = all(ratrec.polyval(num, x % p, p)
                 == vals[i] * ratrec.polyval(den, x % p, p) % p
                 for i, x in enumerate(xs))
        if not ok: return None, 'a_%d does not fit all samples' % t
        iv = pow(den[-1] % p, p - 2, p)
        nums[t] = [c * iv % p for c in num]
        dens[t] = [c * iv % p for c in den]
    Lam = [1]
    for t in range(1, 5):
        Lam = plcm(Lam, dens[t], p)
    V = [Lam]
    for t in range(1, 5):
        q, r = pdivmod(Lam, dens[t], p)
        assert len(r) == 1 and r[0] % p == 0
        V.append(pmul(q, nums[t], p))
    return V, dict(deg=[len(x) - 1 for x in V],
                   degnd=[(len(nums[t]) - 1, len(dens[t]) - 1) for t in range(1, 5)])


# ------------------------------------------------------------- CRT / lift ---

def crt_pair(x, M, r, p):
    g = pow(M % p, p - 2, p)
    t = (r - x) % p * g % p
    return x + M * t, M * p


def ratlift(a, m):
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


def centered(a, M):
    a %= M
    return a - M if 2 * a > M else a


def common_den(xs, M, k=14, seed=1):
    """SIMULTANEOUS rational reconstruction.  All coefficients of the monic
    normalisation share ONE denominator d = lc(A_0), so a single short lattice
    vector (u_1..u_k, d) recovers it.  Balanced two-term reconstruction needs
    M > 2 H^2;  this needs only M > H^{(k+1)/k} -- half the primes.
    Returns d, or None."""
    from sympy.polys.matrices import DomainMatrix
    from sympy import ZZ
    import random
    N = len(xs)
    k = min(k, N)
    rng = random.Random(seed)
    sel = sorted(rng.sample(range(N), k))
    rows = []
    for j in range(k):
        r = [0] * (k + 1); r[j] = M; rows.append(r)
    rows.append([xs[sel[j]] % M for j in range(k)] + [1])
    L = DomainMatrix([[ZZ(int(v)) for v in r] for r in rows],
                     (k + 1, k + 1), ZZ).lll().to_list()
    cands = set()
    for r in L:
        d = abs(int(r[-1]))
        if d:
            for mult in (1, 2, 3, 4, 6, 8, 12, 24):
                cands.add(d * mult)
    out = []
    for d in sorted(cands):
        us = [centered(d * (x % M), M) for x in xs]
        U = max(1, max(abs(u) for u in us))
        out.append((max(U, d).bit_length(), d, us))
    out.sort()
    return out


def lift_vec(Vs, ps):
    """Vs: list of 5-lists of coefficient lists, one per prime.  -> list of 5
    lists of Fractions, or None if a coefficient will not lift."""
    degs = [len(v) for v in Vs[0]]
    for V in Vs:
        if [len(v) for v in V] != degs: return None, 'degree mismatch across primes'
    out = []
    for i in range(5):
        row = []
        for j in range(degs[i]):
            x, M = Vs[0][i][j] % ps[0], ps[0]
            for u in range(1, len(ps)):
                x, M = crt_pair(x, M, Vs[u][i][j] % ps[u], ps[u])
            q = ratlift(x, M)
            if q is None: return None, 'coefficient (%d,%d) will not lift' % (i, j)
            row.append(q)
        out.append(row)
    return out, None


def primitive(Vq):
    """clear denominators, divide out the integer content, fix the sign."""
    from math import gcd
    den = 1
    for row in Vq:
        for c in row:
            den = den * c.denominator // gcd(den, c.denominator)
    Z = [[int(c * den) for c in row] for row in Vq]
    g = 0
    for row in Z:
        for c in row: g = gcd(g, c)
    if g == 0: return Z
    Z = [[c // g for c in row] for row in Z]
    if Z[0][-1] < 0: Z = [[-c for c in row] for row in Z]
    return Z


# ------------------------------------------------------------------ main ----

def polyval_Z(c, x):
    v = 0
    for a in reversed(c): v = v * x + a
    return v


def _check_mod(Z, V, p):
    sc = None
    for i in range(5):
        zi = ratrec.trim([c % p for c in Z[i]])
        vi = ratrec.trim([c % p for c in V[i]])
        if len(zi) != len(vi): return False
        if sc is None:
            if vi[-1] % p == 0: return False
            sc = zi[-1] * pow(vi[-1], p - 2, p) % p
        if any((zi[j] - sc * vi[j]) % p for j in range(len(zi))): return False
    return True


def try_lift(dbound=70, minsamp=150, kl=16, verbose=True, nres=2):
    """reconstruct + CRT + SIMULTANEOUS rational reconstruction over every prime
    that has enough samples.  Returns (Z, ps) or (None, ps)."""
    D = {}
    for fn in ('a_sweep.pkl', 'a_big.pkl'):
        if os.path.exists(fn): D.update(pickle.load(open(fn, 'rb')))
    ps = []
    for p in sorted(set(q for (nn, q) in D), reverse=True):
        ns = sorted(nn for (nn, q) in D if q == p and D[(nn, q)] is not None)
        if len(ns) >= minsamp: ps.append((p, ns))
    Vs = []
    for p, ns in ps:
        V, inf = vec_mod_p(D, p, ns, dbound)
        if V is None:
            if verbose: print('  p=%d: %s' % (p, inf))
            return None, ps
        Vs.append(V)
    degs = [len(v) for v in Vs[0]]
    for V in Vs:
        if [len(v) for v in V] != degs:
            if verbose: print('  degree mismatch across primes: %s' % degs)
            return None, ps
    nfit = len(ps) - nres
    if nfit < 2: return None, ps
    flat = [(i, j) for i in range(5) for j in range(degs[i])]
    xs = [0] * len(flat); M = 1
    for u in range(nfit):
        p = ps[u][0]
        for t, (i, j) in enumerate(flat):
            xs[t], _ = crt_pair(xs[t], M, Vs[u][i][j] % p, p)
        M *= p
    cands = common_den(xs, M, k=kl)
    from math import gcd
    for bits, d, us in cands:
        Z = [[0] * degs[i] for i in range(5)]
        for t, (i, j) in enumerate(flat): Z[i][j] = us[t]
        g = 0
        for row in Z:
            for c in row: g = gcd(g, c)
        if g == 0: continue
        if g > 1: Z = [[c // g for c in row] for row in Z]
        if Z[0][-1] < 0: Z = [[-c for c in row] for row in Z]
        if all(_check_mod(Z, Vs[u], ps[u][0]) for u in range(nfit, len(ps))):
            if verbose:
                print('  LIFTED: %d fit primes (M = %d bits), %d RESERVED primes '
                      'verify.  deg = %d, max |coef| = %d bits'
                      % (nfit, M.bit_length(), nres, degs[0] - 1,
                         max(max(abs(c) for c in row) for row in Z).bit_length()),
                      flush=True)
            return Z, ps
    if verbose:
        print('  %d fit primes (M = %d bits) + %d reserved: NO LIFT (%d candidates '
              'tried; height exceeds ~M^0.9)' % (nfit, M.bit_length(), nres, len(cands)),
              flush=True)
    return None, ps


def run(nfit_primes=None, dbound=None, store='a_big.pkl', nmax=None):
    D = {}
    for fn in ('a_sweep.pkl', store):
        if os.path.exists(fn):
            D.update(pickle.load(open(fn, 'rb')))
    ps_all = sorted(set(p for (n, p) in D), reverse=True)
    have = {}
    for p in ps_all:
        ns = sorted(n for (n, q) in D if q == p and D[(n, q)] is not None)
        if nmax: ns = [n for n in ns if n <= nmax]
        have[p] = ns
    ps = [p for p in ps_all if len(have[p]) >= 150]
    print('primes with >=150 samples: %d  %s' % (len(ps), ps), flush=True)
    for p in ps:
        print('   p=%d : %d samples n=%d..%d' % (p, len(have[p]), have[p][0], have[p][-1]))
    if nfit_primes is None: nfit_primes = max(2, len(ps) - 2)
    Vs = []; info = None
    for p in ps:
        xs = have[p]
        db = dbound if dbound else min(70, len(xs) // 2 - 3)
        t0 = time.time()
        V, inf = vec_mod_p(D, p, xs, db)
        if V is None:
            print('  p=%d FAILED: %s' % (p, inf), flush=True); return None
        if info is None:
            info = inf
            print('  degrees of (a_0..a_4) : %s' % (inf['deg'],), flush=True)
            print('  (deg num, deg den) of a_t/a_0 : %s' % (inf['degnd'],), flush=True)
        Vs.append(V)
        print('  p=%d reconstructed, deg %s  [%.0fs]' % (p, inf['deg'], time.time() - t0),
              flush=True)
    for kfit in range(2, len(ps) + 1):
        Vq, err = lift_vec(Vs[:kfit], ps[:kfit])
        if Vq is None:
            print('  %d primes: %s' % (kfit, err), flush=True); continue
        Z = primitive(Vq)
        # verify against every prime NOT used in the fit
        ok = True
        for u in range(kfit, len(ps)):
            p = ps[u]
            # compare Z mod p with Vs[u] up to a scalar
            sc = None
            for i in range(5):
                zi = [c % p for c in Z[i]]
                zi = ratrec.trim(zi); vi = ratrec.trim([c % p for c in Vs[u][i]])
                if len(zi) != len(vi): ok = False; break
                if sc is None:
                    sc = zi[-1] * pow(vi[-1], p - 2, p) % p
                if any((zi[j] - sc * vi[j]) % p for j in range(len(zi))):
                    ok = False; break
            if not ok: break
        print('  lift with %d primes -> integer vector, holds at the %d unused primes: %s'
              % (kfit, len(ps) - kfit, ok), flush=True)
        if ok and kfit <= len(ps) - 2:
            return Z, ps, kfit, have
    return None


if __name__ == '__main__':
    r = run(dbound=int(sys.argv[1]) if len(sys.argv) > 1 else None)
    if r:
        Z, ps, kfit, have = r
        pickle.dump(dict(Z=Z, ps=ps, kfit=kfit), open('a_lift.pkl', 'wb'))
        for i in range(5):
            print('a_%d : deg %d, max |coef| bits %d'
                  % (i, len(Z[i]) - 1, max(abs(c) for c in Z[i]).bit_length()))
