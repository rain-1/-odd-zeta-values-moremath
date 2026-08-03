"""
Fit p0(n)/p2(n) and p1(n)/p2(n) as rational functions of n from scan3 samples,
separately per parity branch.  Cross-validates on held-out points.

Usage: python3 fit_p.py even_scan.txt odd_scan.txt
(files contain lines 'n=<int>: final dim 1' followed by
 '   p (normalized, reconstructed) = [Fraction(a, b), Fraction(c, d), Fraction(1, 1)]')
"""
import sys, re, itertools
import sympy as sp
from fractions import Fraction

nn = sp.Symbol('n')

def parse(fn):
    txt = open(fn).read()
    pts = []
    for m in re.finditer(r'n=(\d+): final dim 1\s*\n\s*p \(normalized, reconstructed\) = \[(.*?)\]', txt):
        n0 = int(m.group(1))
        fr = re.findall(r'Fraction\((-?\d+), (\d+)\)', m.group(2))
        vals = [Fraction(int(a), int(b)) for a, b in fr]
        pts.append((n0, vals))
    return sorted(pts)

def fit_ratio(points, comp, dmax=14):
    """fit points (n0, value) with N(n)/D(n), deg N,D <= d; smallest d that
    fits all but 3 points, validated on the rest."""
    for d in range(2, dmax + 1):
        na = sp.symbols('na0:%d' % (d + 1)); da = sp.symbols('da0:%d' % (d + 1))
        N = sum(c * nn**i for i, c in enumerate(na))
        D = nn**d + sum(c * nn**i for i, c in enumerate(da[:-1]))
        need = 2 * d + 2
        if len(points) < need + 2:
            continue
        fitpts, testpts = points[:need + 1], points[need + 1:]
        eqs = []
        for n0, v in fitpts:
            eqs.append(sp.Eq(N.subs(nn, n0) - sp.Rational(v.numerator, v.denominator) * D.subs(nn, n0), 0))
        sol = sp.solve(eqs, list(na) + list(da[:-1]), dict=True)
        if not sol:
            continue
        s0 = sol[0]
        Nf = N.subs(s0); Df = D.subs(s0)
        if any(str(f).startswith(('na', 'da')) for f in (Nf + Df).free_symbols):
            # underdetermined; set remaining free to 0
            rest = {f: 0 for f in (Nf + Df).free_symbols if str(f).startswith(('na', 'da'))}
            Nf = Nf.subs(rest); Df = Df.subs(rest)
        ratio = sp.cancel(Nf / Df)
        good = all(sp.Rational(v.numerator, v.denominator) == ratio.subs(nn, n0)
                   for n0, v in testpts)
        if good and testpts:
            return sp.cancel(ratio)
    return None

for fn, tag in zip(sys.argv[1:3], ('EVEN', 'ODD')):
    pts = parse(fn)
    print('%s branch: %d points: n in %s' % (tag, len(pts), [p[0] for p in pts]))
    for comp in (0, 1):
        data = [(n0, v[comp]) for n0, v in pts]
        ratio = fit_ratio(data, comp)
        print('  p%d/p2 =' % comp, sp.factor(ratio) if ratio is not None else 'FIT FAILED')
