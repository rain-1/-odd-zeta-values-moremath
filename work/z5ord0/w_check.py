"""Independent check of the section-7 universal coefficients and of the three
target identities as finite statements (VERIFIED range, not proof)."""
import sys
from fractions import Fraction as Fr

import sympy as sp

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5barnes')
import universal as univ

import o0core as C
import weights as W
import evalq as E


def rat(x):
    x = sp.Rational(x)
    return Fr(int(x.p), int(x.q))


def reduced(expr):
    poly = sp.Poly(sp.expand(expr), univ.z2, univ.z3, univ.z4, univ.z5,
                   univ.z23)
    out = 0
    for mon, c in poly.terms():
        e2, e3, e4, e5, e23 = mon
        if (e2, e3) == (2, 0):
            out += c * sp.Rational(5, 2) * univ.z4
        elif (e2, e3) == (1, 1):
            out += c * univ.z23
        else:
            out += (c * univ.z2 ** e2 * univ.z3 ** e3 * univ.z4 ** e4
                    * univ.z5 ** e5 * univ.z23 ** e23)
    return sp.expand(out)


CACHE = {}


def icoef(k, l, p, q):
    key = (k, l, p, q)
    if key not in CACHE:
        e = reduced(univ.universal(k, l, p, q))
        CACHE[key] = {
            'z2': rat(e.coeff(univ.z2)), 'z3': rat(e.coeff(univ.z3)),
            'z4': rat(e.coeff(univ.z4)), 'z5': rat(e.coeff(univ.z5)),
            'z23': rat(e.coeff(univ.z23)),
            'one': rat(e.subs({univ.z2: 0, univ.z3: 0, univ.z4: 0,
                               univ.z5: 0, univ.z23: 0})),
        }
    return CACHE[key]


def check_sec7(N=5):
    bad = []
    for k in range(N + 1):
        for l in range(N + 1):
            hk, hl, hkl = E.Hs(k, 1), E.Hs(l, 1), E.Hs(k + l, 1)
            h2k, h2l, h2kl = E.Hs(k, 2), E.Hs(l, 2), E.Hs(k + l, 2)
            want = {
                (1, 1, 'z3'): Fr(2),
                (1, 2, 'z3'): 2 * (hk - hkl),
                (2, 1, 'z3'): 2 * (hl - hkl),
                (2, 2, 'z3'): 2 * (h2k + h2l - 2 * h2kl),
                (1, 1, 'z2'): hk + hl - 2 * hkl,
                (1, 2, 'z2'): h2l - 2 * h2kl,
                (2, 1, 'z2'): h2k - 2 * h2kl,
                (1, 2, 'z4'): Fr(17, 4),
                (2, 1, 'z4'): Fr(17, 4),
                (1, 1, 'z4'): Fr(0),
                (2, 2, 'z4'): Fr(0),
                (1, 1, 'z5'): Fr(0),
                (1, 2, 'z5'): Fr(0),
                (2, 1, 'z5'): Fr(0),
                (2, 2, 'z5'): Fr(2),
                (2, 2, 'z23'): Fr(4),
            }
            for (p, q, tag), v in want.items():
                got = icoef(k, l, p, q)[tag]
                if got != v:
                    bad.append((k, l, p, q, tag, got, v))
    print('section-7 coefficient check on 0<=k,l<=%d : %s'
          % (N, 'PASS' if not bad else 'FAIL %s' % bad[:4]))
    return not bad


def main():
    check_sec7(5)
    for name, el in (('T0 = L_k+L_l', W.w_cal()), ('T1 = coeff_z3(W_B)', W.w_t1())):
        print('%-22s support=%d  maxdeg=%d  weights=%s'
              % (name, len(el), max(len(m) for m in el),
                 sorted({sum(C.lwt(L) for L in m) for m in el})))
        vals = [E.weighted_sum(el, n) for n in range(0, 9)]
        print('   sum_{k,l} T*w  for n=0..8 :', vals)


if __name__ == '__main__':
    main()
