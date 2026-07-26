"""T1 first shot: is P-hat_n = sum_{k,l} T * (linear combination of bare H^(3)_alpha)?
   And the weight-5 analogue for P_n with H^(5)_alpha.
   Also sanity: Q_n = sum T (constant weight)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bare import *

N = int(sys.argv[1]) if len(sys.argv) > 1 else 26
EXTRA = len(sys.argv) > 2 and sys.argv[2] == 'extra'

for q in (Q1, Q2):
    S = Sums(N, q, maxr=5, extra=EXTRA)
    syms = S.syms
    print('=== q=%d, N=%d, %d symbols: %s' % (q, N, len(syms), [s[0] for s in syms]))
    # sanity: Q_n
    monos0 = [()]
    rowsQ = []
    for n in range(0, N + 1):
        rowsQ.append(S.eval(n, monos0)[0])
    bad = [n for n in range(N + 1) if rowsQ[n] != lad_mod('Q', n, q)]
    print('   sanity Q_n = sum T : %s' % ('OK' if not bad else 'MISMATCH %s' % bad[:5]))

    for (key, W) in (('Ph', 3), ('P', 5)):
        monos = [((W, i),) for i in range(len(syms))]
        A, b = [], []
        for n in range(0, N + 1):
            A.append(S.eval(n, monos))
            b.append(lad_mod(key, n, q))
        ok, rA, rAb, sol = consistent(A, b, q)
        print('   %-3s  weight %d, degree-1 bare: rows=%d cols=%d rank(A)=%d rank(A|b)=%d  -> %s'
              % (key, W, len(A), len(monos), rA, rAb, 'CONSISTENT' if ok else 'INCONSISTENT'))
        if ok:
            print('        solution:', [(syms[i][0], sol[i]) for i in range(len(syms)) if sol[i]])
