"""Rational-reconstruct a mod-p weight vector and verify  sum_{k,l} T w = Phat
EXACTLY over Q for n = 0..N."""
import sys, os
from fractions import Fraction as Fr
from math import comb
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
os.chdir('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
import bare, frw
import vt_exact as V


def ratrec1(a, p, bound=None):
    """Wang's rational reconstruction of a mod p"""
    if bound is None:
        bound = int((p // 2) ** 0.5)
    r0, r1 = p, a % p
    s0, s1 = 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound:
        return None
    return Fr(r1 if s1 > 0 else -r1, abs(s1))


def to_Q(w, p):
    out = []
    for x in w:
        q = ratrec1(int(x) % p, p)
        if q is None:
            return None
        out.append(q)
    return out


def wfun(B, coefs):
    """build the exact weight function w(n,k,l) from the basis + rational coefs"""
    def f(n, k, l):
        s = Fr(0)
        for c, m in zip(coefs, B):
            if c == 0:
                continue
            v = Fr(c)
            for L in m:
                r, a = bare.LETTERS[L]
                cn, ck, cl = bare.ARGS[a]
                v *= V.H(r, cn * n + ck * k + cl * l)
            s += v
        return s
    return f


if __name__ == '__main__':
    fn = sys.argv[1]
    p = int(sys.argv[2]) if len(sys.argv) > 2 else frw.P
    N = int(sys.argv[3]) if len(sys.argv) > 3 else 16
    B, tops = bare.span_w3(maxdeg=2)
    w = np.load(fn)
    Q = to_Q(w, p)
    if Q is None:
        print('rational reconstruction FAILED (coefficients not small)')
        sys.exit(1)
    nz = [(B[j], Q[j]) for j in range(len(B)) if Q[j] != 0]
    print('rational weight, support %d:' % len(nz))
    for m, c in nz:
        print('   %-28s %s' % ('*'.join(m) if m else '1', c))
    dens = sorted({c.denominator for _, c in nz})
    print('denominators:', dens)
    f = wfun(B, Q)
    import pickle
    ref = pickle.load(open('../z5la/ladder_w3.pkl', 'rb'))['Phat']
    bad = []
    for n in range(N + 1):
        s = Fr(0)
        for k in range(n + 1):
            for l in range(n + 1):
                t = V.T(n, k, l)
                if t:
                    s += t * f(n, k, l)
        if s != ref[n]:
            bad.append((n, s, ref[n]))
    print('EXACT Q check  sum_{k,l} T*w = Phat  for n = 0..%d : %s'
          % (N, 'ALL EQUAL' if not bad else bad[:3]))
    import json
    json.dump({'basis': ['*'.join(m) if m else '1' for m in B],
               'coeffs': [str(c) for c in Q]},
              open(fn.replace('.npy', '_Q.json'), 'w'), indent=1)
    print('written', fn.replace('.npy', '_Q.json'))
