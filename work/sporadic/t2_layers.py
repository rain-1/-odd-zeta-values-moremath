"""Where exactly does (H4) tameness fail for the Lemma-D four?

Claim to test: on the SURVIVING layer {p does not divide S(n,k)} the wide arguments are
already harmless -- Kummer forces the digits of the wide binomials to be small, so
floor(x/p) = x(a,b) AND floor(x/p) < p even for x = 2k, 2n-2k, 2k-n.  If so, (H3) holds
and every letter K^(r)(floor(x/p)) is p-integral on the surviving layer, and the ENTIRE
obstruction to Theorem LB is confined to the vanishing layer {p | S(n,k)}.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math import comb
from fams import FAMS

ARGS = {'alpha': ['k', 'n-k', '2k', '2n-2k'],
        'eps':   ['k', 'n-k', '2k', '2k-n'],
        's7':    ['n', 'k', 'n-k', '2k'],
        'E':     ['k', '2k', '2n-2k'],
        'gamma': ['n', 'k'],
        'D':     ['n', 'k', 'n-k']}
FORM = {'n': lambda n, k: n, 'k': lambda n, k: k, 'n-k': lambda n, k: n - k,
        '2k': lambda n, k: 2 * k, '2n-2k': lambda n, k: 2 * (n - k),
        '2k-n': lambda n, k: 2 * k - n}


def audit(lab, primes=(5, 7, 11, 13, 17, 19, 23)):
    F = FAMS[lab]
    args = ARGS[lab]
    print('--- %s   decomposition arguments %s' % (lab, args))
    for p in primes:
        surv = van = 0
        h3bad = intbad = 0
        vanmax = 0            # max floor(x/p) over the vanishing layer
        survmax = 0
        for a in range(1, p):
            for r in range(p):
                n = a * p + r
                if n >= p * p:
                    continue
                Se = F.Sexact(n)
                ix = F.idx(n)
                for i in range(len(Se)):
                    s = Se[i]
                    if s == 0:
                        continue
                    k = int(ix['k'][i])
                    b = k // p
                    if s % p:
                        surv += 1
                        for aa in args:
                            x = FORM[aa](n, k)
                            if x // p != FORM[aa](a, b):
                                h3bad += 1
                            if x // p >= p:
                                intbad += 1
                            survmax = max(survmax, x // p)
                    else:
                        van += 1
                        for aa in args:
                            x = FORM[aa](n, k)
                            vanmax = max(vanmax, x // p)
        print('   p=%-3d surviving=%-7d (H3) viol=%-4d  non-integral letters=%-4d '
              'max floor(x/p): surv=%-4d van=%-4d   (p=%d)'
              % (p, surv, h3bad, intbad, survmax, vanmax, p), flush=True)


if __name__ == '__main__':
    labs = sys.argv[1].split(',') if len(sys.argv) > 1 else ['gamma', 'D', 'alpha', 'eps', 's7', 'E']
    for lab in labs:
        audit(lab)
