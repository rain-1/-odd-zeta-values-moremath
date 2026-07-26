"""T4 -- the congruence  p^w B(ap+r) = chi(p) B(a) A(r) (mod p),  exact rational data.

Also: (H3)/(H4) audit on the SURVIVING layer {p does not divide S(n,k)} for the
families whose decomposition is non-tame -- this localises the whole obstruction.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from core import SEQS, gen_A, gen_B, chi
from fams import FAMS, ORDER

PAR = {l: (f, p) for l, f, p, _, _ in SEQS}
CHI = {'A': None, 'B': -3, 'C': -3, 'D': None, 'E': -4, 'F': -3, 'alpha': None,
       'gamma': None, 'delta': None, 'eps': None, 'zeta': -3, 'eta': 5,
       's7': None, 's10': None, 's18': -3}


def vp(x, p):
    if x == 0:
        return 10 ** 9
    n, d = x.numerator, x.denominator
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


def test(lab, primes=(5, 7, 11, 13, 17, 19), NMAX=None):
    fam, par = PAR[lab]
    w = FAMS[lab].w
    D = CHI[lab]
    top = NMAX or max(p * p for p in primes)
    An = gen_A(fam, par, top + 2)
    Bn = gen_B(fam, par, top + 2)
    out = {}
    for p in primes:
        cells = fails = 0
        floors = []
        for a in range(1, p):
            for r in range(0, p):
                n = a * p + r
                if n > top:
                    continue
                c = chi(D, p) if D else 1
                d = Fr(p) ** w * Bn[n] - c * Bn[a] * An[r]
                cells += 1
                v = vp(d, p)
                floors.append(min(v, 9))
                if v < 1:
                    fails += 1
        out[p] = (cells, fails, min(floors) if floors else None)
    return w, D, out


if __name__ == '__main__':
    labs = sys.argv[1].split(',') if len(sys.argv) > 1 else ORDER
    pr = tuple(int(x) for x in sys.argv[2].split(',')) if len(sys.argv) > 2 else (5, 7, 11, 13, 17, 19)
    print('T4: v_p( p^w B(ap+r) - chi(p) B(a) A(r) ) >= 1 ?   1<=a<p, 0<=r<p, exact Q')
    print('%-7s %-3s %-5s %s' % ('fam', 'w', 'chi', '  '.join('p=%d' % p for p in pr)))
    for lab in labs:
        w, D, out = test(lab, pr)
        cellstr = []
        for p in pr:
            c, f, fl = out[p]
            cellstr.append('%d/%d f=%s' % (c - f, c, fl if fl is not None and fl < 9 else '>=9'))
        print('%-7s %-3d %-5s %s' % (lab, w, D or '1', '  '.join(cellstr)), flush=True)
