"""Discovery: span T3 by Laurent coefficients of R(x,m-x)=0 at x=-t.

For 1 <= m <= n the numerator factor P(x+y)=P(m) makes the full rational
function identically zero.  Its constant Laurent coefficient at x=-t is a
global A/B/C/D relation.  This is stronger than evaluating R at ordinary
positive lattice points and naturally introduces the finite prefixes seen in
the coupled Euler sums.

Modular output is discovery only.  Any successful vector must be reconstructed
as an exact finite identity before it is used in the proof.
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
import search_t3zeros as OLD

P = 4194301


def mq(x):
    x = F(x)
    return x.numerator % P * pow(x.denominator % P, P - 2, P) % P


def h(x, r=1):
    return AL.H(max(x, 0), r)


def target(n, k, l):
    a = TE.r22_fit(k, l) + 2 * E.el_val(W.compact_w5sym(), n, k, l)
    b = 2 * TE.r12_fit(k, l)
    d = TE.r11_fit(k, l)
    return a, b, d


REGIONS = {
    'all': lambda n: ((t, m) for t in range(n + 1)
                      for m in range(1, n + 1)),
    'tle': lambda n: ((t, m) for t in range(n + 1)
                      for m in range(1, n + 1) if t <= m),
    'tlt': lambda n: ((t, m) for t in range(n + 1)
                      for m in range(1, n + 1) if t < m),
    'tge': lambda n: ((t, m) for t in range(n + 1)
                      for m in range(1, n + 1) if t >= m),
    'tgt': lambda n: ((t, m) for t in range(n + 1)
                      for m in range(1, n + 1) if t > m),
    'sumle': lambda n: ((t, m) for t in range(n + 1)
                        for m in range(1, n + 1) if t + m <= n),
    'sumlt': lambda n: ((t, m) for t in range(n + 1)
                        for m in range(1, n + 1) if t + m < n),
    'sumge': lambda n: ((t, m) for t in range(n + 1)
                        for m in range(1, n + 1) if t + m >= n),
    'sumgt': lambda n: ((t, m) for t in range(n + 1)
                        for m in range(1, n + 1) if t + m > n),
}
for _c in (-2, -1, 0, 1, 2):
    REGIONS[f'sumle{_c:+d}'] = (
        lambda n, c=_c: ((t, m) for t in range(n + 1)
                         for m in range(1, n + 1) if t + m <= n + c))
    REGIONS[f'sumeq{_c:+d}'] = (
        lambda n, c=_c: ((t, m) for t in range(n + 1)
                         for m in range(1, n + 1) if t + m == n + c))

WEIGHTS = [
    ('one', lambda n, t, m: F(1)),
    ('H_t', lambda n, t, m: h(t)),
    ('H_m', lambda n, t, m: h(m)),
    ('H_tm', lambda n, t, m: h(t + m)),
    ('H_n', lambda n, t, m: h(n)),
    ('inv_m', lambda n, t, m: F(1, m)),
    ('inv_tm', lambda n, t, m: F(1, t + m)),
]

# The full weight-one alphabet induced by T, with (k,l) replaced by the
# Laurent lattice indices (t,m).  Zero arguments are assigned H_0=0; inverse
# letters are included only when their argument is positive throughout the
# chosen cell.
HARGS = [
    ('n', lambda n, t, m: n),
    ('t', lambda n, t, m: t),
    ('m', lambda n, t, m: m),
    ('nt', lambda n, t, m: n + t),
    ('nm', lambda n, t, m: n + m),
    ('nmt', lambda n, t, m: n - t),
    ('nmm', lambda n, t, m: n - m),
    ('tm', lambda n, t, m: t + m),
    ('ntm', lambda n, t, m: n + t + m),
]
for _nm, _arg in HARGS:
    if not any(nm == 'H_' + _nm for nm, _ in WEIGHTS):
        WEIGHTS.append(('H_' + _nm,
                        lambda n, t, m, arg=_arg: h(arg(n, t, m))))
for _nm, _arg in HARGS:
    # These four are always >=1 on m>=1, n>=1.
    if _nm in ('n', 'm', 'nm', 'ntm'):
        WEIGHTS.append(('inv_' + _nm,
                        lambda n, t, m, arg=_arg: F(1, arg(n, t, m))))


def raw(n, k, l, region, wt, typ, order=0):
    """Coefficient of A/B/C/D before k<->l canonicalisation."""
    out = F(0)
    for t, m in REGIONS[region](n):
        z = wt(n, t, m)
        e = F(m + t + l)
        if k == t:
            # constant terms of eps^-2(e-eps)^-2,
            # eps^-1(e-eps)^-2, eps^-2(e-eps)^-1,
            # eps^-1(e-eps)^-1.
            table0 = {
                'A': F(3) / e**4, 'B': F(2) / e**3,
                'C': F(1) / e**3, 'D': F(1) / e**2,
            }
            table1 = {
                'A': F(4) / e**5, 'B': F(3) / e**4,
                'C': F(1) / e**4, 'D': F(1) / e**3,
            }
            out += z * (table0 if order == 0 else table1)[typ]
        else:
            q = F(k - t)
            powers = {'A': (2, 2), 'B': (1, 2),
                      'C': (2, 1), 'D': (1, 1)}
            a, b = powers[typ]
            if order == 0:
                out += z / (q**a * e**b)
            else:
                out += z * (-F(a) / (q**(a + 1) * e**b)
                            + F(b) / (q**a * e**(b + 1)))
    return out


def column(region, wt, order=0):
    def col(n, k, l):
        aa = raw(n, k, l, region, wt, 'A', order)
        aa2 = raw(n, l, k, region, wt, 'A', order)
        bb = raw(n, k, l, region, wt, 'B', order)
        # Sum C_kl*c_kl = sum B_kl*c_lk.
        cswap = raw(n, l, k, region, wt, 'C', order)
        dd = raw(n, k, l, region, wt, 'D', order)
        dd2 = raw(n, l, k, region, wt, 'D', order)
        return (aa + aa2) / 2, bb + cswap, (dd + dd2) / 2
    return col


def raw_vertical(n, k, l, region, wt, typ, order=0):
    """Regular Laurent coefficient of R(x,j)=0 at x=-t.

    The k=t terms have only negative powers (y=j is fixed), hence contribute
    zero to coefficients eps^r for r>=0.
    """
    out = F(0)
    powers = {'A': (2, 2), 'B': (1, 2),
              'C': (2, 1), 'D': (1, 1)}
    a, b = powers[typ]
    for t, j in REGIONS[region](n):
        if k == t:
            continue
        z = wt(n, t, j)
        q, e = F(k - t), F(j + l)
        if order == 0:
            out += z / (q**a * e**b)
        else:
            out += -z * F(a) / (q**(a + 1) * e**b)
    return out


def column_vertical(region, wt, order=0):
    def col(n, k, l):
        aa = raw_vertical(n, k, l, region, wt, 'A', order)
        aa2 = raw_vertical(n, l, k, region, wt, 'A', order)
        bb = raw_vertical(n, k, l, region, wt, 'B', order)
        cswap = raw_vertical(n, l, k, region, wt, 'C', order)
        dd = raw_vertical(n, k, l, region, wt, 'D', order)
        dd2 = raw_vertical(n, l, k, region, wt, 'D', order)
        return (aa + aa2) / 2, bb + cswap, (dd + dd2) / 2
    return col


if __name__ == '__main__':
    cols = OLD.columns()
    cols += [(f'Laurent0/{rg}/{nm}', column(rg, wt))
             for rg in REGIONS for nm, wt in WEIGHTS]
    cols += [(f'Laurent1/{rg}', column(rg, lambda n, t, m: F(1), 1))
             for rg in REGIONS]
    cols += [(f'Vertical0/{rg}/{nm}', column_vertical(rg, wt))
             for rg in REGIONS for nm, wt in WEIGHTS]
    cols += [(f'Vertical1/{rg}',
              column_vertical(rg, lambda n, t, j: F(1), 1))
             for rg in REGIONS]
    cells = [(n, k, l) for n in range(1, 8)
             for k in range(n + 1) for l in range(n + 1)]
    rows, rhs = [], []
    for n, k, l in cells:
        tv = target(n, k, l)
        vals = [fn(n, k, l) for _, fn in cols]
        for comp in range(3):
            rows.append([mq(v[comp]) for v in vals])
            rhs.append(mq(tv[comp]))
    A = np.array(rows, dtype=np.int64)
    b = np.array(rhs, dtype=np.int64)
    x, rk, piv, bad = fastlin.solve(A, b, P)
    print('rows=%d cols=%d rank=%d bad=%d' % (len(rows), len(cols), rk, bad))
    if bad == 0:
        for i, (nm, _) in enumerate(cols):
            if x[i] % P:
                print(nm, int(x[i]))
