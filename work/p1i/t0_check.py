"""Sanity: the p-adic evaluator agrees with exact Fraction arithmetic."""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1i')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1d')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from pad import Ctx, Level, load_w5
from w5eval import v5 as v5_exact, TERMS
from core import vp as vp_exact
from fractions import Fraction as F

W5 = '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/w5_allp.json'
terms = load_w5(W5)
bad = 0; tot = 0
for p in (5, 7, 11):
    ctx = Ctx(p, 40)
    for n in (3, 6, 12, 13):
        lev = Level(ctx, n, terms)
        for k in range(n + 1):
            for l in range(n + 1):
                x = lev.v5(k, l)
                e = v5_exact(n, k, l)
                tot += 1
                if e == 0:
                    ok = (x[1] == 0)
                else:
                    ve = vp_exact(e, p)
                    ok = (x[1] != 0 and x[0] == ve)
                    if ok:
                        # compare the unit too
                        num, den = e.numerator, e.denominator
                        while num % p == 0: num //= p
                        while den % p == 0: den //= p
                        m = p ** x[2]
                        u = (num % m) * pow(den, -1, m) % m
                        ok = (u == x[1])
                if not ok:
                    bad += 1
                    if bad < 5:
                        print('MISMATCH p=%d n=%d k=%d l=%d padic=%s exact_v=%s'
                              % (p, n, k, l, x, (vp_exact(e, p) if e else 'ZERO')))
print('checked %d cells, mismatches = %d' % (tot, bad))
