"""Support of E(w)/T for a weight-5 representative -- the number that decides (b).

Each shift tau replaces every letter L by L + (rational), so for a degree-5 monomial
m = L1...L5,

    tau.m - m = sum over NONEMPTY subsets S of  (prod_{i in S} dL_i) * (prod_{i not in S} L_i),

i.e. m contributes exactly its PROPER divisors (degree 0..4) to the support of
E(w)/T.  The rank of the d-finite module that creative telescoping must close is
the size of that union (plus 1 for the constant), so this script computes the
cost driver of the direct route, per PHASE2_CERTS section 10.

Labels are '[f|g]xhxs' as in make_w5m.py: f = k-slot monomial, g = l-slot,
h = C_r monomial (argument k+l), s = N_r monomial (argument n).  Letters are
therefore typed by (name, slot).

Usage: python3 esupp.py w5_allp.json w5_exIII_allp.json ...
"""
import sys, json
from itertools import combinations


def monomial(lab):
    """label -> sorted tuple of (letter, slot) with multiplicity"""
    fg, rest = lab.split(']x')
    f, g = fg[1:].split('|')
    h, s = rest.split('x')
    sp = lambda x: [] if x == '1' else x.split('*')
    out = []
    out += [(t, 'k') for t in sp(f)]
    out += [(t, 'l') for t in sp(g)]
    out += [(t, 'c') for t in sp(h)]
    out += [(t, 'n') for t in sp(s)]
    return tuple(sorted(out))


def proper_divisors(m):
    """all sub-multisets of m of size < len(m) (as sorted tuples)"""
    out = set()
    for r in range(len(m)):
        for c in combinations(range(len(m)), r):
            out.add(tuple(sorted(m[i] for i in c)))
    return out


for fn in sys.argv[1:]:
    d = json.load(open(fn))
    mons = [monomial(lab) for lab in d]
    degs = sorted(set(len(m) for m in mons))
    distinct = set(mons)
    supp = set()
    for m in distinct:
        supp |= proper_divisors(m)
    byw = {}
    for s in supp:
        byw[len(s)] = byw.get(len(s), 0) + 1
    # letters actually used, and how many are rank-1 reachable (weight <= 1)
    letters = set()
    for m in distinct:
        letters |= set(m)
    print('%-28s terms=%-5d distinct monomials=%-5d degrees=%s' %
          (fn.split('/')[-1], len(d), len(distinct), degs))
    print('    distinct letters used      : %d   %s' %
          (len(letters), sorted(letters)))
    print('    support of E(.)/T          : %d' % len(supp))
    print('    by weight                  : %s' %
          ', '.join('%d*w%d' % (byw[w], w) for w in sorted(byw)))
    print('    rank-1 reachable (w<=1)    : %d of %d' %
          (byw.get(0, 0) + byw.get(1, 0), len(supp)))
