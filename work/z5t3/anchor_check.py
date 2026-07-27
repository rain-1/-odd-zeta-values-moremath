"""anchor_check.py -- numeric validation of the subtraction anchor.

Claim (the logical spine of the top-row proof):
  Sigma T W_B  =  2 Q_n z5 + 4 Q_n z2z3 + 0*z4 + 0*z3 - 4 [Sigma T w3sym] z2
                  + [Sigma T [1]W_B]                                     (Barnes)
  I_n          =  2 Q_n z5 + 4 Q_n z2z3 - 4 Phat_n z2 - 2 P_n            (BZ)
  middle row: Phat_n = Sigma T w3sym  [PROVED]
  ==> Sigma T [1]W_B = -2 P_n  by real-number subtraction, NO independence.

This script checks, exactly, for small n:
  (1) coefficient-wise: Sigma T W_B against the six-basis display;
  (2) the anchor consequence: Sigma T [1]W_B = -2 P_n (ladder);
  (3) the open bridge T3: Sigma T [1]W_B = -2 Sigma T w5sym.
All exact rational arithmetic; sympy only carries the zeta symbols.
"""
import sys
from fractions import Fraction as Fr

import sympy as sp

ROOT = '/home/ubuntu/fable-episode-2/zeta-math-2/work'
for d in ('z5barnes', 'z5ord0', 'z5la', 'lb5'):
    sys.path.insert(0, ROOT + '/' + d)

import core                      # lb5: T, ladders Q/P/Ph
import evalq as E                # z5ord0 exact letter evaluation
import weights as W              # z5ord0 weight elements
from universal import universal, z2, z3, z4, z5, z23   # z5barnes

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3


def frac(x):
    x = sp.nsimplify(x)
    return x


def wb_sum(n):
    lk, ll, c2 = W.Lk(), W.Ll(), W.Cr(2)
    tot = sp.Integer(0)
    for k in range(n + 1):
        for l in range(n + 1):
            T = core.T(n, k, l)
            Lk = E.el_val(lk, n, k, l)
            Ll = E.el_val(ll, n, k, l)
            C2 = E.el_val(c2, n, k, l)
            wb = (universal(k, l, 2, 2)
                  + sp.Rational(Lk.numerator, Lk.denominator) * universal(k, l, 1, 2)
                  + sp.Rational(Ll.numerator, Ll.denominator) * universal(k, l, 2, 1)
                  + sp.Rational((Lk * Ll - C2).numerator,
                                (Lk * Ll - C2).denominator) * universal(k, l, 1, 1))
            tot += T * wb
    return sp.expand(tot)


def tsum(el, n):
    return sum((core.T(n, k, l) * E.el_val(el, n, k, l)
                for k in range(n + 1) for l in range(n + 1)), Fr(0))


def spr(fr):
    return sp.Rational(fr.numerator, fr.denominator)


ok_all = True
for n in range(NMAX + 1):
    S = wb_sum(n)
    # normalise zeta products of weight <= 5 into the canonical basis
    S = sp.expand(S.subs({z2**2: sp.Rational(5, 2) * z4}))
    S = sp.expand(S.subs({z2 * z3: z23}))
    Q = core.Q(n); P = core.P(n); Ph = core.Ph(n)
    w3s = tsum(W.compact_w3sym(), n)
    w5s = tsum(W.compact_w5sym(), n)
    c = {}
    c['z5'] = S.coeff(z5); c['z23'] = S.coeff(z23)
    c['z4'] = S.coeff(z4); c['z3'] = S.coeff(z3); c['z2'] = S.coeff(z2)
    c['one'] = sp.expand(S - c['z5'] * z5 - c['z23'] * z23 - c['z4'] * z4
                         - c['z3'] * z3 - c['z2'] * z2)
    checks = [
        ('[z5]  = 2Q', sp.simplify(c['z5'] - 2 * spr(Q)) == 0),
        ('[z23] = 4Q', sp.simplify(c['z23'] - 4 * spr(Q)) == 0),
        ('[z4]  = 0', sp.simplify(c['z4']) == 0),
        ('[z3]  = 0', sp.simplify(c['z3']) == 0),
        ('[z2]  = -4 STw3sym', sp.simplify(c['z2'] + 4 * spr(w3s)) == 0),
        ('[z2]  = -4 Phat    (middle row)', sp.simplify(c['z2'] + 4 * spr(Ph)) == 0),
        ('[1]   = -2 P_n     (ANCHOR)', sp.simplify(c['one'] + 2 * spr(P)) == 0),
        ('[1]   = -2 STw5sym (T3 bridge)', sp.simplify(c['one'] + 2 * spr(w5s)) == 0),
    ]
    print('n = %d:' % n)
    for nm, ok in checks:
        print('   %-34s %s' % (nm, 'PASS' if ok else 'FAIL'))
        ok_all = ok_all and ok
print('ALL:', 'PASS' if ok_all else 'FAIL')
