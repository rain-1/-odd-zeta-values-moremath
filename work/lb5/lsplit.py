"""M4: how the section 18.1 letter-split decomposes E(w)/T's support.

l-FREE letters live in slots 'k' (argument k or n-k or n+k) and 'n' (argument n).
l-DEPENDENT letters live in slots 'l' (argument l / n+l) and 'c' (argument k+l / n+k+l).

A support monomial m splits as m = m_free * m_dep.  In the l-elimination:
  * m_dep == ()  -> the whole letter monomial pulls OUT of the l-sum -> RANK 1
  * m_dep != ()  -> remnant; its l-module has rank 2^|m_dep| (each l-dependent
    letter contributes {letter, 1} because Delta_l(letter) is rational).
"""
import sys, json
from itertools import combinations
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')

def monomial(lab):
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
    out = set()
    for r in range(len(m)):
        for c in combinations(range(len(m)), r):
            out.add(tuple(sorted(m[i] for i in c)))
    return out

for fn in sys.argv[1:]:
    d = json.load(open(fn))
    distinct = set(monomial(lab) for lab in d)
    supp = set()
    for m in distinct:
        supp |= proper_divisors(m)
    free, dep = [], []
    for s in supp:
        dpart = tuple(x for x in s if x[1] in ('l', 'c'))
        (dep if dpart else free).append((s, dpart))
    # group the l-dependent monomials by their l-dependent PART: each distinct
    # l-dependent part is one remnant class of rank 2^|part|
    classes = {}
    for s, dpart in dep:
        classes.setdefault(dpart, []).append(s)
    print('=== %s ===' % fn.split('/')[-1])
    print('  support of E(w)/T            : %d' % len(supp))
    print('  l-FREE monomials (rank 1)    : %d' % len(free))
    print('  l-DEPENDENT monomials        : %d' % len(dep))
    print('  distinct l-dependent PARTS   : %d  (= number of remnant classes per tau)' % len(classes))
    byrank = {}
    for dpart, ms in classes.items():
        r = 2 ** len(dpart)
        byrank.setdefault(r, []).append(len(ms))
    for r in sorted(byrank):
        print('     l-rank %-4d : %3d classes, covering %4d support monomials'
              % (r, len(byrank[r]), sum(byrank[r])))
    print('  --- per-tau problem counts (x5 taus) ---')
    print('    rank-1 problems  : %d  (5 x %d)' % (5 * len(free), len(free)))
    print('    remnant problems : %d  (5 x %d), max l-rank %d'
          % (5 * len(classes), len(classes), max(2 ** len(dp) for dp in classes)))
