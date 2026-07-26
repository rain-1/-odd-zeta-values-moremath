"""ORDER-ZERO creative telescoping for the T-weighted Barnes kernel identities.

Target shape
------------
    sum_{k,l=0}^{n}  T(n,k,l) w(n,k,l) = 0      for every n,
    T(n,k,l) = C(n+k,n) C(n,k)^2 C(n+l,n) C(n,l)^2 C(n+k+l,n).

Certificate sought
------------------
    T w = Delta_k R + Delta_l S ,   R = T rho ,  S = T sigma ,
equivalently, dividing by T,

    w = gk * rho(n,k+1,l) - rho(n,k,l) + gl * sigma(n,k,l+1) - sigma(n,k,l)   (*)

    gk = T(n,k+1,l)/T(n,k,l) = (n+k+1)(n-k)^2(n+k+l+1) / [(k+1)^3 (k+l+1)]
    gl = mirror.

rho, sigma live in the module  (rational functions of n,k,l) (x) (harmonic
monomials).  (*) is an identity there; expanding in monomials gives one scalar
equation per monomial, all with the SAME operator
        Op(r,s) = gk r(k+1,l) - r(k,l) + gl s(k,l+1) - s(k,l),
coupled only downward in degree by the unipotent shift matrices.

Boundary
--------
  T(n,n+1,l) = 0 and T(n,k,n+1) = 0 identically (the C(n,k)^2 factor), so the
  top boundary is automatic PROVIDED  gk * rho(k+1,l)  ->  0  as k -> n.  The
  only source of a pole there is the k-increment  -1/(n-k)^r  of the letters
  H^(r)_{n-k}; gk carries (n-k)^2, so any monomial whose H_{n-k}-content has
  total weight <= 1 is safe.  We keep that restriction on rho (call it the
  "mk-weight<=1" rule) and check it explicitly.

  The bottom boundary is the module condition  rho|_{k=0} = 0, sigma|_{l=0} = 0,
  where |_{k=0} is the letter specialisation  h*_k -> 0, h*_pk -> h*_n,
  h*_mk -> h*_n, h*_kl -> h*_l, h*_pkl -> h*_pl.  It is NOT imposed blockwise.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as Fr

import numpy as np

# ------------------------------------------------------------------ letters --
# argument name -> (c_n, c_k, c_l): the letter h{r}_{arg} is H^(r)_{c_n n + c_k k + c_l l}
ARGS = {
    'n':   (1, 0, 0),
    'k':   (0, 1, 0),
    'l':   (0, 0, 1),
    'pk':  (1, 1, 0),
    'pl':  (1, 0, 1),
    'mk':  (1, -1, 0),
    'ml':  (1, 0, -1),
    'kl':  (0, 1, 1),
    'pkl': (1, 1, 1),
}
ARGORDER = ['n', 'k', 'l', 'pk', 'pl', 'mk', 'ml', 'kl', 'pkl']

# k-increment of H^(r)_x under k -> k+1 :  x -> x + c_k, so
#   c_k = +1 : +1/(x+1)^r      c_k = -1 : -1/x^r        c_k = 0 : 0
# expressed as (linear form, sign) with the linear form evaluated at (n,k,l).
KINC = {          # arg -> (cn, ck, cl, const, sign) meaning sign / (form)^r
    'n':   None,
    'k':   ((0, 1, 0, 1), +1),        # 1/(k+1)^r
    'l':   None,
    'pk':  ((1, 1, 0, 1), +1),        # 1/(n+k+1)^r
    'pl':  None,
    'mk':  ((1, -1, 0, 0), -1),       # -1/(n-k)^r
    'ml':  None,
    'kl':  ((0, 1, 1, 1), +1),        # 1/(k+l+1)^r
    'pkl': ((1, 1, 1, 1), +1),        # 1/(n+k+l+1)^r
}
LINC = {
    'n':   None,
    'k':   None,
    'l':   ((0, 0, 1, 1), +1),
    'pk':  None,
    'pl':  ((1, 0, 1, 1), +1),
    'mk':  None,
    'ml':  ((1, 0, -1, 0), -1),
    'kl':  ((0, 1, 1, 1), +1),
    'pkl': ((1, 1, 1, 1), +1),
}

SWAP = {'k': 'l', 'l': 'k', 'pk': 'pl', 'pl': 'pk', 'mk': 'ml', 'ml': 'mk',
        'n': 'n', 'kl': 'kl', 'pkl': 'pkl'}

# k = 0 specialisation of the letter arguments
SPEC_K0 = {'n': 'n', 'k': None, 'l': 'l', 'pk': 'n', 'pl': 'pl',
           'mk': 'n', 'ml': 'ml', 'kl': 'l', 'pkl': 'pl'}
SPEC_L0 = {'n': 'n', 'k': 'k', 'l': None, 'pk': 'pk', 'pl': 'n',
           'mk': 'mk', 'ml': 'n', 'kl': 'k', 'pkl': 'pk'}


def lname(r, a):
    return 'h%d_%s' % (r, a)


def parse(L):
    r, a = L[1:].split('_')
    return int(r), a


def lwt(L):
    return parse(L)[0]


def mkwt(mon):
    """total weight of the H_{n-k} letters in a monomial (the k=n+1 hazard)."""
    return sum(parse(L)[0] for L in mon if parse(L)[1] == 'mk')


def mlwt(mon):
    return sum(parse(L)[0] for L in mon if parse(L)[1] == 'ml')


def sigma_mon(mon):
    return tuple(sorted(lname(parse(L)[0], SWAP[parse(L)[1]]) for L in mon))


# ------------------------------------------------------- module element ------
# element = dict {monomial (sorted tuple) : value}

def el_add(a, b, c=1):
    out = dict(a)
    for m, v in b.items():
        w = c * v
        s = out.get(m, 0) + w
        if s == 0:
            out.pop(m, None)
        else:
            out[m] = s
    return out


def el_mul(a, b):
    out = {}
    for m1, v1 in a.items():
        for m2, v2 in b.items():
            m = tuple(sorted(m1 + m2))
            s = out.get(m, 0) + v1 * v2
            if s == 0:
                out.pop(m, None)
            else:
                out[m] = s
    return out


def el_scale(a, c):
    return {m: c * v for m, v in a.items() if c * v != 0}


def el_sigma(a):
    out = {}
    for m, v in a.items():
        mm = sigma_mon(m)
        s = out.get(mm, 0) + v
        if s == 0:
            out.pop(mm, None)
        else:
            out[mm] = s
    return out


def closure(mons):
    seen = set()
    for m in mons:
        for r in range(len(m) + 1):
            for sub in itertools.combinations(m, r):
                seen.add(tuple(sorted(sub)))
    return sorted(seen, key=lambda m: (-len(m), -sum(lwt(L) for L in m), m))


# ------------------------------------------------------------- mod-p eval ----

def lf(form, n, k, l):
    cn, ck, cl, c0 = form
    return cn * n + ck * k + cl * l + c0


def inc_val(tab, L, n, k, l, p):
    r, a = parse(L)
    e = tab[a]
    if e is None:
        return 0
    form, sgn = e
    d = lf(form, n, k, l) % p
    v = pow(d, p - 2, p)
    v = pow(v, r, p)
    return (sgn * v) % p


def shift_cols(basis, tab, n, k, l, p):
    """matrix Sh with Sh[i][j] = coefficient of basis[i] in shift(basis[j])."""
    idx = {m: j for j, m in enumerate(basis)}
    J = len(basis)
    S = np.zeros((J, J), dtype=np.int64)
    incs = {}
    for m in basis:
        for L in m:
            if L not in incs:
                incs[L] = inc_val(tab, L, n, k, l, p)
    for j, m in enumerate(basis):
        cur = {(): 1}
        for L in m:
            fac = {(L,): 1}
            iv = incs[L]
            if iv:
                fac[()] = iv
            nxt = {}
            for m1, v1 in cur.items():
                for m2, v2 in fac.items():
                    mm = tuple(sorted(m1 + m2))
                    nxt[mm] = (nxt.get(mm, 0) + v1 * v2) % p
            cur = nxt
        for mm, v in cur.items():
            if v % p and mm in idx:
                S[idx[mm], j] = v % p
    return S


def gk_val(n, k, l, p):
    num = (n + k + 1) * pow((n - k) % p, 2, p) % p * ((n + k + l + 1) % p) % p
    den = pow((k + 1) % p, 3, p) * ((k + l + 1) % p) % p
    return num % p * pow(den, p - 2, p) % p


def gl_val(n, k, l, p):
    return gk_val(n, l, k, p)


# ------------------------------------------------------------------ ansatz ---
K1 = (0, 1, 0, 1); K2 = (0, 1, 0, 2); K3 = (0, 1, 0, 3)
L1 = (0, 0, 1, 1); L2 = (0, 0, 1, 2); L3 = (0, 0, 1, 3)
KL = [(0, 1, 1, j) for j in range(0, 6)]
NK = [(1, 1, 0, j) for j in range(0, 6)]
NL = [(1, 0, 1, j) for j in range(0, 6)]
NKL = [(1, 1, 1, j) for j in range(0, 6)]
MK = [(1, -1, 0, j) for j in range(0, 6)]
ML = [(1, 0, -1, j) for j in range(0, 6)]

NAMES = {}
for _f, _s in [(K1, 'k+1'), (K2, 'k+2'), (K3, 'k+3'),
               (L1, 'l+1'), (L2, 'l+2'), (L3, 'l+3')]:
    NAMES[_f] = _s
for _j in range(6):
    NAMES[KL[_j]] = 'k+l+%d' % _j
    NAMES[NK[_j]] = 'n+k+%d' % _j
    NAMES[NL[_j]] = 'n+l+%d' % _j
    NAMES[NKL[_j]] = 'n+k+l+%d' % _j
    NAMES[MK[_j]] = 'n+%d-k' % _j
    NAMES[ML[_j]] = 'n+%d-l' % _j


def dstr(D):
    return '*'.join(NAMES.get(f, str(f)) + ('^%d' % m if m > 1 else '')
                    for f, m in D) or '1'


def dval(D, n, k, l, p):
    v = 1
    for f, m in D:
        v = v * pow(lf(f, n, k, l) % p, m, p) % p
    return v


class Ansatz:
    """rho = Nr(k,l)/Dr with k | Nr enforced by force_k, sigma = tau(rho)."""

    def __init__(self, D, dk, dl, force_k=1):
        self.D = list(D)
        self.dk, self.dl, self.force_k = dk, dl, force_k
        self.mons = [(a, b) for a in range(force_k, dk + 1)
                     for b in range(0, dl + 1)]
        self.nc = len(self.mons)

    def __repr__(self):
        return 'Ansatz(D=%s, bideg=(%d,%d), force_k=%d, nc=%d)' % (
            dstr(self.D), self.dk, self.dl, self.force_k, self.nc)

    def swapD(self):
        out = []
        for (cn, ck, cl, c0), m in self.D:
            out.append(((cn, cl, ck, c0), m))
        return out

    def eval_r(self, coef, n, k, l, p):
        num = 0
        kk, ll = k % p, l % p
        for t, (a, b) in enumerate(self.mons):
            c = int(coef[t]) % p
            if c:
                num = (num + c * pow(kk, a, p) % p * pow(ll, b, p)) % p
        return num * pow(dval(self.D, n, k, l, p), p - 2, p) % p

    def eval_s(self, coef, n, k, l, p):
        """sigma(k,l) = rho(l,k) with the swapped denominator."""
        return self.eval_r(coef, n, l, k, p)
