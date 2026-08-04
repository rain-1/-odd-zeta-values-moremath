"""eps54_domb.py -- THE DISCRIMINATING EXPERIMENT for the reachability
dichotomy: jet-scan the Domb family alpha (and epsilon as a second point).

alpha (Domb): S = C(n,k)^2 C(2k,k) C(2(n-k),n-k)
            = n!^2 (2k)! (2n-2k)! / (k!^4 (n-k)!^4),
  R3 (10,4,64,0), principal character, real limit 7*zeta(3)/24,
  modular LEVEL 12 (non-squarefree, per eps51).
epsilon:  S = C(n,k)^2 C(2k,n)^2 = (2k)!^2/(k!^2 (n-k)!^2 (2k-n)!^2),
  R3 (12,4,16,0), principal character, limit 7*zeta(3)/32, LEVEL 8.

Hypotheses in competition (work/SPORADIC_MODULAR_DICTIONARY.md):
  H-char+limit: principal character + real limit  => REACHABLE;
  H-level:      squarefree level                  => REACHABLE
                (12 and 8 are non-squarefree      => UNREACHABLE).
Same protocol as eps43 (linear + quadratic curve atoms, per-zeta-graded
pinning, targets eps^3 then eps^2, two primes).
"""
import sys

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')

from math import comb, factorial
import eps43
from eps43 import Fam, run_family

def mk_new():
    fams = {}
    fams['alpha'] = Fam(
        'alpha', 2,
        [('n', 2, (1, 0)), ('2*k', 1, (0, 2)), ('2*(n-k)', 1, (2, -2)),
         ('k', -4, (0, 1)), ('n-k', -4, (1, -1))],
        lambda n: [(k,) for k in range(n + 1)],
        lambda n, c: 1, ('R3', 10, 4, 64, 0), 3)
    fams['epsF'] = Fam(
        'epsF', 2,
        [('2*k', 2, (0, 2)), ('k', -2, (0, 1)), ('n-k', -2, (1, -1)),
         ('2*k-n', -2, (-1, 2))],
        lambda n: [(k,) for k in range((n + 1) // 2, n + 1)],
        lambda n, c: 1, ('R3', 12, 4, 16, 0), 3)
    return fams

_orig = eps43.A_binom
def A_binom2(name, n):
    if name == 'alpha':
        return sum(comb(n, k) ** 2 * comb(2 * k, k) * comb(2 * (n - k), n - k)
                   for k in range(n + 1))
    if name == 'epsF':
        return sum(comb(n, k) ** 2 * comb(2 * k, n) ** 2
                   for k in range((n + 1) // 2, n + 1))
    return _orig(name, n)
eps43.A_binom = A_binom2

if __name__ == '__main__':
    fams = mk_new()
    order = sys.argv[1].split(',') if len(sys.argv) > 1 else ['alpha', 'epsF']
    allv = {}
    for name in order:
        allv[name] = run_family(fams[name])
    print('\n================ DISCRIMINATING SUMMARY ================')
    for name, v in allv.items():
        for tgt, (b, deg) in sorted(v.items()):
            print('  %-6s eps^%d: %s (%s)'
                  % (name, tgt, 'b != 0 REACHABLE' if b else 'b forced 0', deg))
    print('H-char+limit predicts REACHABLE; H-level predicts UNREACHABLE.')
