"""Tools for JOB 1: the 12-dimensional affine family as an exact-Q object.

Cost model used throughout (stated in Z5STAR_CERT.md):
  J        = |divisibility closure of supp(w)|  =  #Lean component identities
           = 1 + #letters(w) + #deg-2 monomials(w)          (deg-1 h3's count as letters)
  N_hard   = 1 + #{h1_*, h2_* letters}   -- the blocks that need a GENUINE
             cofactor pair.  The remaining J - N_hard blocks are MAXIMAL and
             their cofactor is  w_j * r_Q  (Theorem R): one already-certified
             Q-row identity, instantiated.
"""
import sys, os, itertools
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
sys.path.insert(1, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import bare

P1 = 4194301
P2 = 4194287

B, TOPS = bare.span_w3(maxdeg=2)
J109 = len(B)
IDX = {m: j for j, m in enumerate(B)}


# ----------------------------------------------------------- mod-p <-> Q ----

def ratrec1(a, p, bound=None):
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


def to_Q(v, p):
    out = []
    for x in v:
        q = ratrec1(int(x) % p, p)
        if q is None:
            return None
        out.append(q)
    return out


def to_p(v, p):
    return np.array([int(Fr(c).numerator) % p * pow(int(Fr(c).denominator) % p, p - 2, p) % p
                     for c in v], dtype=np.int64)


# ---------------------------------------------------------- sigma (k<->l) ---

SIGPERM = np.array([IDX[tuple(sorted(bare.sigma_letter(L) for L in m))] for m in B])


def sig(v):
    """sigma acting on a coefficient vector (works for Q lists and np arrays)"""
    out = [0] * J109
    for j in range(J109):
        out[SIGPERM[j]] = v[j]
    if isinstance(v, np.ndarray):
        return np.array(out, dtype=v.dtype)
    return out


def symQ(v):
    s = sig(v)
    return [Fr(v[j] + s[j], 2) for j in range(J109)]


def antiQ(v):
    s = sig(v)
    return [Fr(v[j] - s[j], 2) for j in range(J109)]


# ---------------------------------------------------------------- support ---

def support(v):
    return [j for j in range(J109) if v[j] != 0]


def stats(v):
    """(J, N_hard, n_mono, letters, deg2, h3s)"""
    sup = support(v)
    letters = set()
    deg2 = 0
    h3s = 0
    for j in sup:
        m = B[j]
        for L in m:
            letters.add(L)
        if len(m) == 2:
            deg2 += 1
        elif len(m) == 1 and bare.LWT[m[0]] == 3:
            h3s += 1
    hard = sorted(L for L in letters if bare.LWT[L] <= 2)
    Jc = 1 + len(letters) + deg2
    return dict(J=Jc, N_hard=1 + len(hard), n_mono=len(sup), letters=sorted(letters),
                hard_letters=hard, deg2=deg2, h3=h3s,
                symmetric=(sig(v) == list(v) if not isinstance(v, np.ndarray)
                           else bool((sig(v) == v).all())))


def show(v, name=''):
    st = stats(v)
    print('%-14s support %2d  J=%2d  N_hard=%2d  letters=%2d (h1/h2: %d)  deg2=%2d  sym=%s'
          % (name, st['n_mono'], st['J'], st['N_hard'], len(st['letters']),
             len(st['hard_letters']), st['deg2'], st['symmetric']))
    return st


def render(v):
    out = []
    for j in support(v):
        out.append(('*'.join(B[j]) if B[j] else '1', Fr(v[j])))
    return out


# ------------------------------------------------------- exact Q evaluation -

_HC = {}


def H(r, x):
    if x <= 0:
        return Fr(0)
    key = (r, x)
    if key in _HC:
        return _HC[key]
    v = H(r, x - 1) + Fr(1, x ** r)
    _HC[key] = v
    return v


from math import comb


def T(n, k, l):
    if k > n or l > n:
        return 0
    return (comb(n + k, n) * comb(n, k) ** 2 * comb(n + l, n)
            * comb(n, l) ** 2 * comb(n + k + l, n))


def wval(v, n, k, l):
    s = Fr(0)
    for j in support(v):
        c = Fr(v[j])
        for L in B[j]:
            r, a = bare.LETTERS[L]
            cn, ck, cl = bare.ARGS[a]
            c *= H(r, cn * n + ck * k + cl * l)
        s += c
    return s


def sumTw(v, n):
    s = Fr(0)
    for k in range(n + 1):
        for l in range(n + 1):
            t = T(n, k, l)
            if t:
                s += t * wval(v, n, k, l)
    return s


def phat_ladder():
    import pickle
    return pickle.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la/ladder_w3.pkl',
                            'rb'))['Phat']


def check_rep(v, N=20, verbose=True):
    ref = phat_ladder()
    bad = []
    for n in range(N + 1):
        if sumTw(v, n) != ref[n]:
            bad.append(n)
    if verbose:
        print('   exact Q  sum T*w = Phat, n=0..%d : %s'
              % (N, 'ALL EQUAL' if not bad else 'FAIL at %s' % bad[:4]))
    return not bad


def check_kernel(v, N=20, verbose=True):
    bad = [n for n in range(N + 1) if sumTw(v, n) != 0]
    if verbose:
        print('   exact Q  sum T*v = 0, n=0..%d : %s'
              % (N, 'ALL ZERO' if not bad else 'FAIL at %s' % bad[:4]))
    return not bad


# ------------------------------------------------------------ linear algebra
def rrefQ(rows):
    """exact rref over Q; rows = list of lists of Fraction. returns (R, pivots)"""
    M = [[Fr(x) for x in r] for r in rows]
    nr = len(M)
    nc = len(M[0]) if nr else 0
    piv = []
    r = 0
    for c in range(nc):
        pr = None
        for i in range(r, nr):
            if M[i][c] != 0:
                pr = i
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        inv = Fr(1) / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(nr):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(nc)]
        piv.append(c)
        r += 1
        if r == nr:
            break
    return M[:r], piv


def solveQ(A, b):
    """solve A x = b over Q (A: list of rows, len(b)=len(A)). Returns (x, ok)."""
    nr = len(A)
    nc = len(A[0])
    aug = [[Fr(x) for x in A[i]] + [Fr(b[i])] for i in range(nr)]
    R, piv = rrefQ(aug)
    if any(c == nc for c in piv):
        return None, False
    x = [Fr(0)] * nc
    for i, c in enumerate(piv):
        x[c] = R[i][nc]
    return x, True
