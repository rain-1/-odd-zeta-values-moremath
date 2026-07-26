"""Fast mod-p evaluation of the already-CERTIFIED Q-row Phi-certificate
(work/z5cf/Qrow_phicert.m).  Its identity is
    sum_i c_i(n) P_i(n,k,l) = gk*r(n,k+1,l) - r + gl*s(n,k,l+1) - s
which is exactly the top-monomial block of both weight rows (H3_{n+k} for w3,
H5_{n+k} for w5), so that block needs no solving.
"""
import os, re, pickle
import numpy as np
import sympy as sp

SRC = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5cf/Qrow_phicert.m'
CACHE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la/qrow_cache.pkl'

def _grab(s, key):
    i = s.index('"%s" ->' % key) + len('"%s" ->' % key)
    depth = 0; j = i
    while j < len(s):
        c = s[j]
        if c in '([{': depth += 1
        elif c in ')]}': depth -= 1
        if depth < 0: break
        if depth == 0 and c == ',' and re.match(r'\s*"', s[j + 1:]): break
        j += 1
    return s[i:j]

def _load():
    if os.path.exists(CACHE):
        return pickle.load(open(CACHE, 'rb'))
    s = open(SRC).read()
    n, k, l = sp.symbols('n k l')
    out = {}
    for key in ('r_num', 'r_den', 's_num', 's_den'):
        txt = _grab(s, key).replace('^', '**').replace('\n', ' ')
        e = sp.sympify(txt, locals={'n': n, 'k': k, 'l': l})
        P = sp.Poly(sp.expand(e), n, k, l)
        out[key] = {tuple(m): int(c) for m, c in zip(P.monoms(), P.coeffs())}
    pickle.dump(out, open(CACHE, 'wb'))
    return out

_D = None

def _dd():
    global _D
    if _D is None: _D = _load()
    return _D

def _arr2d(coefs, n, p):
    """collapse the n-variable: return dict {(j,m): value mod p}"""
    out = {}
    npow = {}
    for (i, j, m), c in coefs.items():
        if i not in npow: npow[i] = pow(n % p, i, p)
        out[(j, m)] = (out.get((j, m), 0) + c % p * npow[i]) % p
    return out

def make_evals(n, p):
    """returns (rfun, sfun) with rfun(n,k,l)->int mod p (n ignored, baked in)"""
    D = _dd()
    A = {key: _arr2d(D[key], n, p) for key in D}
    def mk(numk, denk):
        NU = A[numk]; DE = A[denk]
        def f(_n, k, l):
            kk = k % p; ll = l % p
            kp = {}; lp = {}
            def K(a):
                if a not in kp: kp[a] = pow(kk, a, p)
                return kp[a]
            def L(b):
                if b not in lp: lp[b] = pow(ll, b, p)
                return lp[b]
            num = 0
            for (j, m), c in NU.items():
                if c: num = (num + c * K(j) % p * L(m)) % p
            den = 0
            for (j, m), c in DE.items():
                if c: den = (den + c * K(j) % p * L(m)) % p
            return num * pow(den, p - 2, p) % p
        return f
    return mk('r_num', 'r_den'), mk('s_num', 's_den')

def exact():
    """exact sympy expressions (n,k,l) for r and s"""
    D = _dd()
    n, k, l = sp.symbols('n k l')
    def build(key):
        return sum(c * n ** i * k ** j * l ** m for (i, j, m), c in D[key].items())
    return (build('r_num'), build('r_den'), build('s_num'), build('s_den'))
