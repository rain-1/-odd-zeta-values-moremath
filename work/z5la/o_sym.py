"""Exact SYMBOLIC shift matrices S_k, S_l over Q(n,k,l) for the 15-element
weight-3 closure basis at order m = 7, in the MIXED base (yk, yl based at n+m).

zla is field-generic, so it runs verbatim over a sympy 'field'.
"""
import sympy as sp
import zla

n, k, l = sp.symbols('n k l')


class FS:
    zero = sp.Integer(0)
    one = sp.Integer(1)
    def frac(self, a, b): return sp.together(sp.Integer(1) * a / b)
    def add(self, *xs):
        s = sp.Integer(0)
        for x in xs: s = s + x
        return sp.together(s)
    def mul(self, a, b): return sp.together(a * b)
    def neg(self, a): return -a
    def cst(self, q): return sp.nsimplify(q)
    def iszero(self, a): return sp.simplify(a) == 0


def matrices(m=7, which='w3'):
    F = FS()
    w = zla.weight_element(F, which)
    B = zla.closure_basis(w)
    base = {'yk': m, 'yl': m}
    out = {}
    for d in ('k', 'l'):
        cols = zla.shift_matrix_mixed(F, B, d, n, k, l, base)
        M = sp.zeros(len(B), len(B))
        for j in range(len(B)):
            for i in range(len(B)):
                M[i, j] = sp.simplify(cols[j][i])
        out[d] = M
    return B, w, out


def Pm_sym(i, m=7):
    v = sp.Integer(1)
    for j in range(1, i + 1):
        v *= (n + j) * (n + k + j) * (n + l + j) * (n + k + l + j)
    a = sp.Integer(1); b = sp.Integer(1)
    for j in range(i + 1, m + 1):
        a *= (n + j - k); b *= (n + j - l)
    return v * a ** 2 * b ** 2


def rhs_sym(m=7, which='w3'):
    """V[t][i] = coefficient of M_i in  sum_u c_u(n+t) P^{(m)}_{t+u} w(n+t+u),
    the right-hand side of block i, exactly in Q(n,k,l)."""
    F = FS()
    w = zla.weight_element(F, which)
    B = zla.closure_basis(w)
    base = {'yk': m, 'yl': m}
    V = []
    for t in range(m - 2):
        C = zla.cc(n + t)
        el = {}
        for u in range(4):
            co = sp.expand(C[u] * Pm_sym(t + u, m))
            el = zla.el_add(F, el, zla.w_shift_mixed(F, w, t + u, n, k, l, base), co)
        V.append([sp.cancel(sp.together(el.get(mm, sp.Integer(0)))) for mm in B])
    return B, V


if __name__ == '__main__':
    B, w, S = matrices()
    print('basis (M_1..M_%d):' % len(B))
    for i, mm in enumerate(B):
        print('  M_%-2d = %s' % (i + 1, '*'.join(mm) if mm else '1'))
    for d in ('k', 'l'):
        print('\nS_%s  (nonzero off-diagonal entries; diagonal is 1)' % d)
        for i in range(len(B)):
            for j in range(len(B)):
                if i != j and S[d][i, j] != 0:
                    print('  (M_%d <- M_%d) : %s' % (i + 1, j + 1, sp.factor(S[d][i, j])))
