"""The new representative in closed form, and its exact verification.

  U  =  H_k - 1/2 ( H_{n-k} + H_n + H_{n+k+l} - H_{n+l} )
  V  = -1/2 ( H_k + H_l - H_{n-k} - H_n + H_{n+k} - H_{n+k+l} )

  w* =  H^(3)_k
      +  U * ( H^(2)_k + H^(2)_n + H^(2)_{n+k} - H^(2)_{n-l} )
      +  V * ( H^(2)_l - H^(2)_k )
"""
import sys, os, json
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
os.chdir('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
import bare
import vt_exact as V_
H = V_.H
T = V_.T


def wstar(n, k, l):
    U = H(1, k) - Fr(1, 2) * (H(1, n - k) + H(1, n) + H(1, n + k + l) - H(1, n + l))
    V = -Fr(1, 2) * (H(1, k) + H(1, l) - H(1, n - k) - H(1, n) + H(1, n + k) - H(1, n + k + l))
    return (H(3, k)
            + U * (H(2, k) + H(2, n) + H(2, n + k) - H(2, n - l))
            + V * (H(2, l) - H(2, k)))


def wstar_el():
    """the same object as a {monomial: constant} element over the bare basis"""
    U = {'h1_k': Fr(1), 'h1_mk': Fr(-1, 2), 'h1_n': Fr(-1, 2),
         'h1_pkl': Fr(-1, 2), 'h1_pl': Fr(1, 2)}
    Vv = {'h1_k': Fr(-1, 2), 'h1_l': Fr(-1, 2), 'h1_mk': Fr(1, 2),
          'h1_n': Fr(1, 2), 'h1_pk': Fr(-1, 2), 'h1_pkl': Fr(1, 2)}
    out = {('h3_k',): Fr(1)}
    for tgt, coef in ((['h2_k', 'h2_n', 'h2_pk'], (U, Fr(1))),
                      (['h2_ml'], (U, Fr(-1))),
                      (['h2_l'], (Vv, Fr(1))),
                      (['h2_k'], (Vv, Fr(-1)))):
        src, c = coef
        for t in tgt:
            for L, cc in src.items():
                m = tuple(sorted((L, t)))
                out[m] = out.get(m, Fr(0)) + c * cc
    return {m: c for m, c in out.items() if c != 0}


if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    B, tops = bare.span_w3(maxdeg=2)
    el = wstar_el()
    # 1. the closed form and the fitted vector agree, coefficient by coefficient
    d = json.load(open('wjoint_p4194301_Q.json'))
    fit = {}
    for nm, c in zip(d['basis'], d['coeffs']):
        if Fr(c) != 0:
            fit[tuple(nm.split('*')) if nm != '1' else ()] = Fr(c)
    same = (fit == el)
    print('closed form == fitted weight, monomial by monomial :', same)
    if not same:
        print('  only in closed form:', {k: v for k, v in el.items() if fit.get(k) != v})
        print('  only in fit        :', {k: v for k, v in fit.items() if el.get(k) != v})
    # 2. exact Q:  sum_{k,l} T w* = Phat
    import pickle
    ref = pickle.load(open('../z5la/ladder_w3.pkl', 'rb'))['Phat']
    bad = []
    for n in range(N + 1):
        s = Fr(0)
        for k in range(n + 1):
            for l in range(n + 1):
                t = T(n, k, l)
                if t:
                    s += t * wstar(n, k, l)
        if s != ref[n]:
            bad.append((n, s, ref[n]))
    print('EXACT Q  sum_{k,l} T(n,k,l) w*(n,k,l) = Phat_n , n = 0..%d : %s'
          % (N, 'ALL EQUAL' if not bad else bad[:3]))
    # 3. L_BZ residual on that ladder
    import zla
    Y = []
    for n in range(N + 1):
        s = Fr(0)
        for k in range(n + 1):
            for l in range(n + 1):
                t = T(n, k, l)
                if t:
                    s += t * wstar(n, k, l)
        Y.append(s)
    bad2 = []
    for n in range(0, N - 2):
        c = zla.cc(n)
        v = sum(Fr(c[i]) * Y[n + i] for i in range(4))
        if v != 0:
            bad2.append((n, v))
    print('EXACT Q  L_BZ . (sum T w*) = 0 , n = 0..%d : %s'
          % (N - 3, 'ALL ZERO' if not bad2 else bad2[:3]))
    print('support %d monomials, %d distinct symbols, closure J = %d'
          % (len(el), len({L for m in el for L in m}),
             len(bare.span_w3.__doc__ and __import__('itertools') and
                 sorted({tuple(sorted(s)) for m in el
                         for r in range(len(m) + 1)
                         for s in __import__('itertools').combinations(m, r)}))))
