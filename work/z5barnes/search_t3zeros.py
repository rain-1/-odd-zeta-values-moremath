"""Discovery search: express Barnes T3 as sharp g/g'/q zero functionals.

This is only a decomposition finder.  A successful output must subsequently
be converted into an exact finite identity; a modular fit is never a proof.
"""
from fractions import Fraction as F
import sys
import numpy as np

sys.path.insert(0, '../z5ord0')
sys.path.insert(0, '../z5la')
import alpha as AL
import evalq as E
import t_euler as TE
import weights as W
import fastlin

P = 4194301


def mq(x):
    x = F(x)
    return x.numerator % P * pow(x.denominator % P, P - 2, P) % P


def h(x, r):
    return AL.H(max(x, 0), r)


def args(kind, n, l, j):
    out = {'j': j, 'l': l, 'jl': j + l}
    if kind == 'overlap':
        out['jml'] = j - l
    return out


def wbasis(weight, kind):
    aa = ['j', 'l', 'jl'] + (['jml'] if kind == 'overlap' else [])
    out = []
    # Single letter.
    for a in aa:
        out.append(('H%d_%s' % (weight, a),
                    lambda n, l, j, a=a: h(args(kind, n, l, j)[a], weight)))
    # H1 * H(weight-1).
    if weight >= 2:
        for a in aa:
            for b in aa:
                out.append(('H1_%s*H%d_%s' % (a, weight - 1, b),
                            lambda n, l, j, a=a, b=b:
                            h(args(kind, n, l, j)[a], 1)
                            * h(args(kind, n, l, j)[b], weight - 1)))
    # At weight 3 include cubic H1 products.
    if weight == 3:
        for ia, a in enumerate(aa):
            for ib in range(ia, len(aa)):
                b = aa[ib]
                for ic in range(ib, len(aa)):
                    c = aa[ic]
                    out.append(('H1_%s*H1_%s*H1_%s' % (a, b, c),
                                lambda n, l, j, a=a, b=b, c=c:
                                h(args(kind, n, l, j)[a], 1)
                                * h(args(kind, n, l, j)[b], 1)
                                * h(args(kind, n, l, j)[c], 1)))
    # Deduplicate names (weight 2 has H1*H1 ordered duplicates).
    seen = set()
    return [(nm, f) for nm, f in out if not (nm in seen or seen.add(nm))]


def jrng(kind, n, l):
    if kind == 'prefix':
        return range(1, l + 1)
    if kind == 'overlap':
        return range(l + 1, n + 1)
    if kind == 'full':
        return range(1, n + l + 1)
    if kind == 'qfull':
        return range(1, n + 1)
    raise KeyError(kind)


def target(n, k, l):
    # Canonical sum is A*a + B*b + D*d, with A,D symmetric.
    a = TE.r22_fit(k, l) + 2 * E.el_val(W.compact_w5sym(), n, k, l)
    b = 2 * TE.r12_fit(k, l)
    d = TE.r11_fit(k, l)
    return a, b, d


def columns():
    cols = []
    # g_l(j)=0.  Canonicalise the A coefficient by symmetrising; B is oriented.
    for kind in ('prefix', 'overlap', 'full'):
        for nm, f in wbasis(3, kind):
            def col(n, k, l, kind=kind, f=f):
                def raw(kk, ll, power):
                    return sum((f(n, ll, j) / F(kk + j) ** power
                                for j in jrng(kind, n, ll)), F(0))
                a = (raw(k, l, 2) + raw(l, k, 2)) / 2
                b = raw(k, l, 1)
                return a, b, F(0)
            cols.append(('g/%s/%s' % (kind, nm), col))
    # g'_l(j)=0 on the overlap.
    for nm, f in wbasis(2, 'overlap'):
        def col(n, k, l, f=f):
            def raw(kk, ll, power):
                return sum((f(n, ll, j) / F(kk + j) ** power
                            for j in jrng('overlap', n, ll)), F(0))
            a = -(raw(k, l, 3) + raw(l, k, 3))
            b = -raw(k, l, 2)
            return a, b, F(0)
        cols.append(('gp/overlap/%s' % nm, col))
    # q_l(j)=0 on 1..n.  Its C coefficient becomes B after k<->l.
    for nm, f in wbasis(2, 'qfull'):
        def col(n, k, l, f=f):
            b = sum((f(n, k, j) / F(l + j) ** 2
                     for j in jrng('qfull', n, k)), F(0))
            d0 = sum((f(n, l, j) / F(k + j)
                      for j in jrng('qfull', n, l)), F(0))
            d1 = sum((f(n, k, j) / F(l + j)
                      for j in jrng('qfull', n, k)), F(0))
            return F(0), b, (d0 + d1) / 2
        cols.append(('q/full/%s' % nm, col))
    # Full two-variable R and its first derivatives vanish on 1<=i,j<=n.
    # The triangle split mirrors the two pieces in the universal sine kernel.
    regions = {
        'square': lambda n: ((i, j) for i in range(1, n + 1)
                             for j in range(1, n + 1)),
        'lower': lambda n: ((i, j) for i in range(1, n + 1)
                            for j in range(i, n + 1)),
        'strict': lambda n: ((i, j) for i in range(1, n + 1)
                             for j in range(i + 1, n + 1)),
        'diag': lambda n: ((i, i) for i in range(1, n + 1)),
    }
    f1s = [
        ('H1_i', lambda n, i, j: h(i, 1)),
        ('H1_j', lambda n, i, j: h(j, 1)),
        ('H1_ij', lambda n, i, j: h(i + j, 1)),
        ('H1_n', lambda n, i, j: h(n, 1)),
        ('inv_i', lambda n, i, j: F(1, i)),
        ('inv_j', lambda n, i, j: F(1, j)),
        ('inv_ij', lambda n, i, j: F(1, i + j)),
    ]

    def rcol(region, f, deriv):
        def raw(n, k, l):
            aa = bb = cc = dd = F(0)
            for i, j in regions[region](n):
                z = f(n, i, j)
                if deriv == 'r':
                    aa += z / F(k + i) ** 2 / F(l + j) ** 2
                    bb += z / F(k + i) / F(l + j) ** 2
                    cc += z / F(k + i) ** 2 / F(l + j)
                    dd += z / F(k + i) / F(l + j)
                elif deriv == 'rx':
                    aa += -2 * z / F(k + i) ** 3 / F(l + j) ** 2
                    bb += -z / F(k + i) ** 2 / F(l + j) ** 2
                    cc += -2 * z / F(k + i) ** 3 / F(l + j)
                    dd += -z / F(k + i) ** 2 / F(l + j)
            return aa, bb, cc, dd

        def col(n, k, l):
            aa, bb, cc, dd = raw(n, k, l)
            aa2, bb2, cc2, dd2 = raw(n, l, k)
            # C_kl = B_lk; A,D are symmetric.
            return (aa + aa2) / 2, bb + cc2, (dd + dd2) / 2
        return col

    for region in regions:
        for nm, f in f1s:
            cols.append(('R/%s/%s' % (region, nm), rcol(region, f, 'r')))
        cols.append(('Rx/%s' % region,
                     rcol(region, lambda n, i, j: F(1), 'rx')))
    return cols


if __name__ == '__main__':
    C = columns()
    cells = [(n, k, l) for n in range(1, 7)
             for k in range(n + 1) for l in range(n + 1)]
    rows, rhs = [], []
    for n, k, l in cells:
        tv = target(n, k, l)
        for comp in range(3):
            rows.append([mq(fn(n, k, l)[comp]) for _, fn in C])
            rhs.append(mq(tv[comp]))
    A = np.array(rows, dtype=np.int64)
    b = np.array(rhs, dtype=np.int64)
    x, rk, piv, bad = fastlin.solve(A, b, P)
    print('rows=%d cols=%d rank=%d bad=%d' % (len(rows), len(C), rk, bad))
    if bad == 0:
        nz = [(C[i][0], int(x[i])) for i in range(len(C)) if x[i] % P]
        print('support', len(nz))
        for z in nz:
            print(z)
