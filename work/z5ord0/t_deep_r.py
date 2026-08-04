"""Sharp necessary condition (t_deep closed-subsystem test) applied to the
eps31 residual r -- the single missing weight-5 identity of the Delta5 bridge.

For each maximal (under containment) monomial m0 of r with mk/ml-weight
within cap, the equations indexed by blocks containing m0 form a closed
subsystem with rhs c at m0; inconsistency at depth D excludes an order-zero
certificate whose ansatz respects the cap, at that inflation depth, for THIS
representative of the residual class.
"""
import pickle, sys
import numpy as np

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5ord0')
import o0core as C
import joint0 as J
import t_deep as TD

AR = ['n', 'k', 'l', 'pk', 'pl', 'mk', 'ml', 'kl', 'pkl']

R = pickle.load(open(
    '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/eps31_residual.pkl',
    'rb'))
W = {}
for m, c in R.items():
    W[tuple(sorted(C.lname(r, AR[a]) for r, a in m))] = c

# maximal monomials under containment (as multisets)
from collections import Counter
def contains(big, small):
    cb, cs = Counter(big), Counter(small)
    return all(cb[x] >= v for x, v in cs.items())

monos = list(W)
maximal = [m for m in monos
           if not any(m != m2 and contains(m2, m) for m2 in monos)]
print('residual monomials %d, maximal %d' % (len(monos), len(maximal)))

# candidate m0: maximal, mkwt<=1, mlwt<=1, prefer high degree
cand = [m for m in maximal if C.mkwt(m) <= 1 and C.mlwt(m) <= 1]
cand.sort(key=lambda m: (-len(m), m))
print('admissible m0 candidates:', len(cand))
for m in cand[:6]:
    print('  ', m, W[m])

W1 = [C.lname(1, a) for a in ('k', 'l', 'pk', 'pl', 'mk', 'ml', 'kl', 'pkl')]

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    nm0 = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    for m0 in cand[:nm0]:
        c = W[m0]
        cc = int(c.numerator) * pow(int(c.denominator), J.P1 - 2, J.P1) % J.P1
        print('m0 =', m0, ' c =', c, flush=True)
        for fam in ('G1', 'G2', 'G3'):
            for depth, deg in ((1, 8), (2, 6), (3, 4)):
                nc = (deg + 1) ** 2
                npts = int(2.8 * nc) + 20
                try:
                    TD.run(n, m0, cc, W1, depth, TD.FAM[fam], deg, npts,
                           label='%s/depth%d/deg%d' % (fam, depth, deg))
                except MemoryError:
                    print('  MEMORY at %s/depth%d/deg%d' % (fam, depth, deg),
                          flush=True)
