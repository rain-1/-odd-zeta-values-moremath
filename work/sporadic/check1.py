"""Harness sanity layer 0: cells reproduce A(n); Smod == Sexact mod q; args nonneg."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from core import PRIMES, SEQS, gen_A, gen_B
from fams import FAMS, ORDER, Fac

NAME = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F',
        'alpha': 'alpha', 'gamma': 'gamma', 'delta': 'delta', 'eps': 'eps',
        'zeta': 'zeta', 'eta': 'eta', 's7': 's7', 's10': 's10', 's18': 's18'}
PAR = {l: (f, p) for l, f, p, _, _ in SEQS}

NMAX = 14
q = PRIMES[0]
fac = Fac(6 * NMAX + 20, q)
print('%-7s %-6s %-8s %-10s %s' % ('fam', 'w', 'sum=A?', 'Smod=S?', 'arg ranges (n=%d)' % NMAX))
allok = True
for lab in ORDER:
    F = FAMS[lab]
    fam, par = PAR[lab]
    An = gen_A(fam, par, NMAX + 2)
    ok1 = ok2 = True
    for n in range(0, NMAX + 1):
        Se = F.Sexact(n)
        if sum(Se) != An[n]:
            ok1 = False
            print('   %s: sum mismatch n=%d: %s vs %s' % (lab, n, sum(Se), An[n]))
            break
        Sm = F.Smod(n, fac)
        if len(Se) != Sm.size:
            ok2 = False
            print('   %s: length mismatch n=%d: %d vs %d' % (lab, n, len(Se), Sm.size))
            break
        if any((int(Sm[i]) - Se[i]) % q for i in range(len(Se))):
            ok2 = False
            print('   %s: Smod mismatch at n=%d' % (lab, n))
            break
    # argument ranges on the SUPPORT (S != 0) at n = NMAX
    Se = F.Sexact(NMAX)
    ix = F.idx(NMAX)
    sup = [i for i in range(len(Se)) if Se[i] != 0]
    rng = {}
    for a in F.args:
        vals = [int(ix[a][i]) for i in sup]
        rng[a] = (min(vals), max(vals))
    bad = [a for a in F.args if rng[a][0] < 0]
    tam = [a for a in F.args if rng[a][0] >= 0 and rng[a][1] <= NMAX]
    print('%-7s %-6d %-8s %-10s neg:%s' % (lab, F.w, ok1, ok2, bad or '-'))
    print('        declared tame %s' % (list(F.tame),))
    print('        measured tame %s' % (tam,))
    if set(tam) != set(F.tame):
        print('        *** TAME MISMATCH ***')
        allok = False
    allok = allok and ok1 and ok2
print('ALL OK' if allok else 'PROBLEMS')
