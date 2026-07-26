"""z5la -- WZ certificates for the compact odd-zeta weights by LINEAR ALGEBRA
over the explicitly known shift-closure module basis.  No Groebner engine.

Base is  Phi(n,k,l) = T(n+3,k,l) / prod_{j=1..3} (n+j)(n+k+j)(n+l+j)(n+k+l+j)
(pole free for n,k,l >= 0), with  T(n+i,k,l) = Phi * P_i,  deg P_i = 12.

Everything below works over an abstract field F (Fraction or F_p) supplied by the
caller, evaluated at a *numeric* point (n,k,l).  Module elements are dicts
    { monomial (sorted tuple of letter names) : field element }.

Key structural fact used throughout: every letter shifts to *itself plus a
rational function*, so every shift matrix is UNIPOTENT with respect to the
grading by number of letter factors.  The certificate system therefore
decomposes into J independent SCALAR WZ problems, all with the same operator
        f  =  gk * r(n,k+1,l) - r(n,k,l) + gl * s(n,k,l+1) - s(n,k,l)
solved in order of decreasing monomial degree.
"""
from fractions import Fraction as Fr
import itertools

# ---------------------------------------------------------------- fields ----

class FQ:
    """exact rationals"""
    zero = Fr(0)
    one = Fr(1)
    def frac(self, a, b):
        if b == 0:
            raise ZeroDivisionError('FQ.frac by 0')
        return Fr(a, b)
    def add(self, *xs):
        s = Fr(0)
        for x in xs: s += x
        return s
    def mul(self, a, b): return a * b
    def neg(self, a): return -a
    def cst(self, q): return Fr(q)
    def iszero(self, a): return a == 0

class Fp:
    def __init__(self, p):
        self.p = p
        self.zero = 0
        self.one = 1
    def frac(self, a, b):
        p = self.p
        b %= p
        if b == 0:
            raise ZeroDivisionError('Fp.frac by 0 mod p')
        return (a % p) * pow(b, p - 2, p) % p
    def add(self, *xs): return sum(xs) % self.p
    def mul(self, a, b): return a * b % self.p
    def neg(self, a): return (-a) % self.p
    def cst(self, q):
        q = Fr(q)
        return self.frac(q.numerator, q.denominator)
    def iszero(self, a): return a % self.p == 0

# --------------------------------------------------------------- letters ----
# letter -> {'n': inc, 'k': inc, 'l': inc};  inc(F,n,k,l) -> field element
# H^(r)_{x+1} = H^(r)_x + 1/(x+1)^r  is the ONLY analytic input.

def _z(F, n, k, l): return F.zero

LETTERS = {
    'xk': {'n': _z,
           'k': lambda F, n, k, l: F.frac(1, (k + 1)),
           'l': _z},                                   # H_k
    'xl': {'n': _z, 'k': _z,
           'l': lambda F, n, k, l: F.frac(1, (l + 1))},  # H_l
    'yk': {'n': lambda F, n, k, l: F.frac(1, (n - k + 1)),
           'k': lambda F, n, k, l: F.frac(-1, (n - k)),
           'l': _z},                                   # H_{n-k}
    'yl': {'n': lambda F, n, k, l: F.frac(1, (n - l + 1)),
           'k': _z,
           'l': lambda F, n, k, l: F.frac(-1, (n - l))},  # H_{n-l}
    'zk': {'n': lambda F, n, k, l: F.frac(1, (n + k + 1)),
           'k': lambda F, n, k, l: F.frac(1, (n + k + 1)),
           'l': _z},                                   # H_{n+k}
    'zl': {'n': lambda F, n, k, l: F.frac(1, (n + l + 1)),
           'k': _z,
           'l': lambda F, n, k, l: F.frac(1, (n + l + 1))},  # H_{n+l}
    'S2': {'n': lambda F, n, k, l: F.add(F.frac(1, (n + k + 1) ** 2),
                                         F.frac(1, (n + l + 1) ** 2)),
           'k': lambda F, n, k, l: F.add(F.frac(1, (n + k + 1) ** 2),
                                         F.frac(-1, (k + 1) ** 2)),
           'l': lambda F, n, k, l: F.add(F.frac(1, (n + l + 1) ** 2),
                                         F.frac(-1, (l + 1) ** 2))},
    # S2 = H2_{n+k} - H2_k + H2_{n+l} - H2_l  (a legitimate composite letter:
    # closed under all three shifts, which is what shrinks the weight-5 module
    # from 64 to 58)
}
for _r in (2, 3, 4, 5):
    LETTERS['u%d' % _r] = {
        'n': (lambda r: lambda F, n, k, l: F.frac(1, (n + k + 1) ** r))(_r),
        'k': (lambda r: lambda F, n, k, l: F.frac(1, (n + k + 1) ** r))(_r),
        'l': _z}                                        # H^(r)_{n+k}

# ------------------------------------------------- module element algebra ----

def mono_mul(m1, m2):
    return tuple(sorted(m1 + m2))

def el_add(F, a, b, c=None):
    """a + c*b  (c a field element or None for 1)"""
    out = dict(a)
    for m, v in b.items():
        w = v if c is None else F.mul(c, v)
        if m in out:
            s = F.add(out[m], w)
            if F.iszero(s): del out[m]
            else: out[m] = s
        else:
            if not F.iszero(w): out[m] = w
    return out

def el_mul(F, a, b):
    out = {}
    for m1, v1 in a.items():
        for m2, v2 in b.items():
            m = mono_mul(m1, m2)
            w = F.mul(v1, v2)
            if m in out:
                s = F.add(out[m], w)
                if F.iszero(s): del out[m]
                else: out[m] = s
            else:
                if not F.iszero(w): out[m] = w
    return out

def el_scale(F, a, c):
    out = {}
    for m, v in a.items():
        w = F.mul(c, v)
        if not F.iszero(w): out[m] = w
    return out

def subst(F, el, incs):
    """replace each letter L by (L + incs[L]) and expand."""
    out = {}
    for m, v in el.items():
        cur = {(): v}
        for L in m:
            inc = incs.get(L, F.zero)
            fac = {(L,): F.one}
            if not F.iszero(inc): fac[()] = inc
            cur = el_mul(F, cur, fac)
        out = el_add(F, out, cur)
    return out

# ------------------------------------------------------------- the weights --

def weight_element(F, which):
    """w as a dict {monomial: constant} -- constants only, letters at base n."""
    C = F.cst
    if which == 'q0':
        return {(): C(1)}
    if which == 'w3':
        # Psi = (1/2)zk - (1/2)zl + yk - yl - (3/2)xk + (3/2)xl
        Psi = {('zk',): C(Fr(1, 2)), ('zl',): C(Fr(-1, 2)),
               ('yk',): C(1), ('yl',): C(-1),
               ('xk',): C(Fr(-3, 2)), ('xl',): C(Fr(3, 2))}
        w = el_add(F, {('u3',): C(1)}, el_mul(F, Psi, {('u2',): C(1)}), C(-1))
        return w
    if which == 'w5':
        al = {('zk',): C(1), ('xk',): C(-1), ('zl',): C(-1), ('xl',): C(1)}
        be = {('yk',): C(1), ('xk',): C(-1), ('yl',): C(-1), ('xl',): C(1)}
        Psi = el_add(F, el_scale(F, al, C(Fr(1, 2))), be)
        amb = el_add(F, al, be, C(-1))              # alpha - beta
        w = {('u5',): C(1)}
        w = el_add(F, w, el_mul(F, amb, {('u4',): C(1)}), C(Fr(1, 2)))
        w = el_add(F, w, el_mul(F, {('S2',): C(1)}, {('u3',): C(1)}), C(Fr(1, 4)))
        w = el_add(F, w, el_mul(F, el_mul(F, al, Psi), {('u3',): C(1)}), C(Fr(-1, 2)))
        return w
    raise ValueError(which)

def closure_basis(w):
    """downward closure of the support of w under divisibility = the shift
    closure module basis.  Ordered by DECREASING degree (triangular order)."""
    seen = set()
    for m in w:
        for r in range(len(m) + 1):
            for sub in itertools.combinations(m, r):
                seen.add(tuple(sorted(sub)))
    return sorted(seen, key=lambda m: (-len(m), m))

# ------------------------------------------- L_BZ coefficients and the P_i --

def a0(n): return 41218 * n ** 3 + 198849 * n ** 2 + 320790 * n + 173057
def B8(n):
    return (3874492 * n ** 8 + 59373972 * n ** 7 + 394148190 * n ** 6
            + 1481084196 * n ** 5 + 3447878810 * n ** 4 + 5095855458 * n ** 3
            + 4673546679 * n ** 2 + 2433871008 * n + 551502039)
def B9(n):
    return (48802112 * n ** 9 + 967468896 * n ** 8 + 8488000862 * n ** 7
            + 43246197636 * n ** 6 + 140983768422 * n ** 5
            + 304912330849 * n ** 4 + 437406946975 * n ** 3
            + 401272692378 * n ** 2 + 213593890911 * n + 50257929339)

def cc(n):
    return [(n + 1) ** 5 * (n + 2) * a0(n + 1),
            -2 * (n + 2) * B8(n),
            -2 * B9(n),
            2 * (n + 3) ** 5 * (2 * n + 5) * a0(n)]

def Pi(n, k, l, i):
    v = 1
    for j in range(1, i + 1):
        v *= (n + j) * (n + k + j) * (n + l + j) * (n + k + l + j)
    a = 1
    b = 1
    for j in range(i + 1, 4):
        a *= (n + j - k)
        b *= (n + j - l)
    return v * a * a * b * b

def gk_val(F, n, k, l):
    return F.frac((n + 3 - k) ** 2 * (n + k + 1) * (n + k + l + 1),
                  (k + 1) ** 3 * (k + l + 1))

def gl_val(F, n, k, l):
    return F.frac((n + 3 - l) ** 2 * (n + l + 1) * (n + k + l + 1),
                  (l + 1) ** 3 * (k + l + 1))

# --------------------------------------------------------- the RHS vector ---

def w_shift_n(F, w, i, n, k, l):
    """w(n+i, k, l) expanded in the base letters at (n,k,l)."""
    incs = {}
    for L in LETTERS:
        tot = F.zero
        for j in range(1, i + 1):
            tot = F.add(tot, LETTERS[L]['n'](F, n + j - 1, k, l))
        incs[L] = tot
    return subst(F, w, incs)

def rhs_element(F, w, n, k, l):
    """ E_w / Phi = sum_i c_i(n) P_i(n,k,l) w(n+i,k,l) """
    C = cc(n)
    out = {}
    for i in range(4):
        co = F.mul(F.cst(C[i]), F.cst(Pi(n, k, l, i)))
        out = el_add(F, out, w_shift_n(F, w, i, n, k, l), co)
    return out

def shift_matrix(F, basis, d, n, k, l):
    """S^d as list of columns: col j = coefficient vector of shift(basis[j])."""
    idx = {m: j for j, m in enumerate(basis)}
    incs = {L: LETTERS[L][d](F, n, k, l) for L in LETTERS}
    cols = []
    for m in basis:
        img = subst(F, {m: F.one}, incs)
        v = [F.zero] * len(basis)
        for mm, c in img.items():
            v[idx[mm]] = c
        cols.append(v)
    return cols

def el_to_vec(F, basis, el):
    idx = {m: j for j, m in enumerate(basis)}
    v = [F.zero] * len(basis)
    for m, c in el.items():
        if m not in idx:
            raise KeyError('monomial %r outside the closure basis' % (m,))
        v[idx[m]] = c
    return v


# ------------------------------------------------- MIXED-BASE normalisation --
# The n-family letters may be normalised at base (n + delta_L) rather than at
# base n.  Choosing delta = 3 for the letters H^(r)_{n-k}, H^(r)_{n-l} makes
# P_a's double zeros prod_{j=a+1..3}(n+j-k)^2 cancel the poles 1/(n+j-k)^r that
# the normalisation introduces, so the RHS has NO pole interior to the
# telescoping range (this is exactly Z5CF_CERT 5.5's "second pole source").

BASE3 = {'yk': 3, 'yl': 3}

def w_shift_mixed(F, w, a, n, k, l, base):
    """w(n+a,k,l) expanded in the letters based at (n+delta_L, k, l)"""
    incs = {}
    for L in LETTERS:
        d = base.get(L, 0)
        tot = F.zero
        if a > d:
            for i in range(d, a):
                tot = F.add(tot, LETTERS[L]['n'](F, n + i, k, l))
        elif a < d:
            for i in range(a, d):
                tot = F.add(tot, F.neg(LETTERS[L]['n'](F, n + i, k, l)))
        incs[L] = tot
    return subst(F, w, incs)

def shift_matrix_mixed(F, basis, d, n, k, l, base):
    idx = {m: j for j, m in enumerate(basis)}
    incs = {L: LETTERS[L][d](F, n + base.get(L, 0), k, l) for L in LETTERS}
    cols = []
    for m in basis:
        img = subst(F, {m: F.one}, incs)
        v = [F.zero] * len(basis)
        for mm, c in img.items():
            v[idx[mm]] = c
        cols.append(v)
    return cols

def rhs_element_mixed(F, w, n, k, l, base):
    C = cc(n)
    out = {}
    for i in range(4):
        co = F.mul(F.cst(C[i]), F.cst(Pi(n, k, l, i)))
        out = el_add(F, out, w_shift_mixed(F, w, i, n, k, l, base), co)
    return out
