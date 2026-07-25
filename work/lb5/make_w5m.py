"""Export w5_allp.json as a Wolfram Language expression, in FOLDED form.

Labels are '[f|g]xhxs':  f = k-slot monomial in A_r/B_r, g = l-slot monomial,
h = monomial in C_r (argument k+l), s = monomial in N_r (argument n).  The
symmetrised weight is  cf * h * s * (pf        if f == g
                                     pf + pb   otherwise)
with pf = f(k) g(l), pb = f(l) g(k).  Since T is k<->l symmetric,

        sum_{k,l} T * w5  =  sum_{k,l} T * v5 ,
        v5 = sum_terms cf * h * s * (1 if f == g else 2) * f(k) g(l),

which is the exact analogue of the folded weight v used for w3hat (PHASE2_CERTS
section 5.2).  v5 is what the E(w5) weight-lowering step must be applied to.

Writes  w5folded.m  as a single parenthesised expression (safe under Get AND
under `math < file`), plus w5term counts to stdout.

Usage: python3 make_w5m.py [w5_allp.json] [w5folded.m]
"""
import sys, json
from fractions import Fraction as F

SRC = sys.argv[1] if len(sys.argv) > 1 else 'w5_allp.json'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'w5folded.m'

# A_r(x) = H^(r)_{n+x} - H^(r)_x ;  B_r(x) = H^(r)_{n-x} - H^(r)_x
# C_r    = H^(r)_{n+k+l} - H^(r)_{k+l} ;  N_r = H^(r)_n
def letter(nm, slot):
    t, r = nm[0], nm[1]
    if t == 'A':
        return '(HarmonicNumber[n+%s,%s]-HarmonicNumber[%s,%s])' % (slot, r, slot, r)
    if t == 'B':
        return '(HarmonicNumber[n-%s,%s]-HarmonicNumber[%s,%s])' % (slot, r, slot, r)
    raise ValueError(nm)


def cletter(nm):
    r = nm[1]
    return '(HarmonicNumber[n+k+l,%s]-HarmonicNumber[k+l,%s])' % (r, r)


def nletter(nm):
    return 'HarmonicNumber[n,%s]' % nm[1]


d = json.load(open(SRC))
parts = []
nsym = 0
for lab in sorted(d):
    num, den = d[lab]
    c = F(num, den)
    fg, rest = lab.split(']x')
    f, g = fg[1:].split('|')
    h, s = rest.split('x')
    sp = lambda x: [] if x == '1' else x.split('*')
    f, g, h, s = sp(f), sp(g), sp(h), sp(s)
    mult = 1 if f == g else 2
    if f != g:
        nsym += 1
    coef = c * mult
    fac = []
    if coef != 1:
        fac.append('(%d/%d)' % (coef.numerator, coef.denominator))
    fac += [letter(x, 'k') for x in f]
    fac += [letter(x, 'l') for x in g]
    fac += [cletter(x) for x in h]
    fac += [nletter(x) for x in s]
    parts.append('*'.join(fac) if fac else '1')

body = ' +\n  '.join(parts)
with open(OUT, 'w') as fh:
    fh.write('(* folded weight-5 representative: sum_{k,l} T*w5_allp == sum_{k,l} T*v5 *)\n')
    fh.write('(\n  ' + body + '\n)\n')
print('%s: %d terms (%d asymmetric, doubled), wrote %s' % (SRC, len(d), nsym, OUT))
