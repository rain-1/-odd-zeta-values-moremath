"""Measure the alphabet of the universal coefficients needed for targets 2, 3."""
import sys
from fractions import Fraction as Fr

import alpha as A
import w_check as WC

CELLS = [(k, l) for k in range(0, 8) for l in range(0, 8)]
HELD = [(k, l) for k in range(8, 11) for l in range(0, 11)]


def target(p, q, tag):
    return lambda k, l: WC.icoef(k, l, p, q)[tag]


def probe(name, p, q, tag, weight):
    f = target(p, q, tag)
    for use_biv in (False, True):
        B = A.basis(weight, use_euler=True, use_biv=use_biv)
        ok, coef = A.fit(f, B, CELLS, tag='%s biv=%d' % (name, use_biv))
        if ok:
            bad = []
            for (k, l) in HELD:
                got = sum((c * fn(k, l) for c, (_, fn) in zip(coef, B)), Fr(0))
                if got != f(k, l):
                    bad.append((k, l))
            print('     held-out %d cells: %s'
                  % (len(HELD), 'PASS' if not bad else 'FAIL %s' % bad[:3]))
            if not bad:
                return coef, B
    return None, None


if __name__ == '__main__':
    print('=== weight-3 coefficient  [zeta2] I22 ===')
    probe('[z2]I22', 2, 2, 'z2', 3)
    print('=== weight-3 coefficient  [1] I11 ===')
    probe('[1]I11', 1, 1, 'one', 3)
    print('=== weight-4 coefficients [1] I12 / I21 ===')
    probe('[1]I12', 1, 2, 'one', 4)
    print('=== weight-5 coefficient  [1] I22 ===')
    probe('[1]I22', 2, 2, 'one', 5)
