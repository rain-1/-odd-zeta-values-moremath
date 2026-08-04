"""eps52_eichler_all.py -- the Eichler-companion construction across all
fifteen sporadic pairs.

Construction (derived in MODULAR_COACTION_PROBE.md Part C):
  y_B = sum B(n)t^n satisfies L(y_B) = t  (B(0)=0, B(1)=1; exact boundary),
  and IF the Frobenius kernel through the nome is {F, F log q [, F log^2q/2]}
  then L = (P(t)/sigma^w) F theta_q^w (1/F), so

      B(n) = [t^n]  F(q) * theta_q^{-w}( t sigma^w / (P F) ),
      P_R2 = 1 - a t + c t^2,      P_R3 = 1 - 2a t + c t^2   (d-term is
      lower order in theta, so it does not enter the leading coefficient;
      for R3 with d != 0 the theta^3-coefficient is still 1 - 2at + ct^2).

For order-2 (R2) the kernel condition is automatic (Frobenius); for
order-3 (R3) it is the geometric/Sym^2 property and the exact match of the
construction against the recurrence B(n) is precisely its test.

Verdict per family: PASS/FAIL of exact coefficient match, n <= NCHK.
"""

import sys
from fractions import Fraction as F_

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
from eps48_modular_nome import (smul, sinv, sexp, srevert, compose,
                                gseries, N)
import sympy as sp

th = sp.symbols('th')
NCHK = 20

FAMS = [
    # name, type, a, b, c, d
    ('A/Franel', 2, 7, 2, -8, 0),
    ('B',        2, 9, 3, 27, 0),
    ('C',        2, 10, 3, 9, 0),
    ('D',        2, 11, 3, -1, 0),
    ('E',        2, 12, 4, 32, 0),
    ('F',        2, 17, 6, 72, 0),
    ('alpha',    3, 10, 4, 64, 0),
    ('gamma',    3, 17, 5, 1, 0),
    ('delta',    3, 7, 3, 81, 0),
    ('epsilon',  3, 12, 4, 16, 0),
    ('zeta',     3, 9, 3, -27, 0),
    ('eta',      3, 11, 5, 125, 0),
    ('s7',       3, 13, 4, -27, 3),
    ('s10',      3, 6, 2, -64, 4),
    ('s18',      3, 14, 6, 192, -12),
]

def seqs(tp, a, b, c, d, n_top):
    A = [F_(1)]
    B = [F_(0), F_(1)]
    for n in range(n_top):
        if tp == 2:
            if n == 0:
                A.append(F_(b))
            else:
                A.append((F_(a * n * n + a * n + b) * A[n]
                          - F_(c * n * n) * A[n - 1]) / F_((n + 1) ** 2))
                B.append((F_(a * n * n + a * n + b) * B[n]
                          - F_(c * n * n) * B[n - 1]) / F_((n + 1) ** 2))
        else:
            if n == 0:
                A.append(F_(b))
            else:
                A.append((F_((2 * n + 1) * (a * n * n + a * n + b)) * A[n]
                          - F_(n * (c * n * n + d)) * A[n - 1])
                         / F_((n + 1) ** 3))
                B.append((F_((2 * n + 1) * (a * n * n + a * n + b)) * B[n]
                          - F_(n * (c * n * n + d)) * B[n - 1])
                         / F_((n + 1) ** 3))
    return A, B

def run(name, tp, a, b, c, d):
    w = tp
    A, B = seqs(tp, a, b, c, d, N + 2)
    if tp == 2:
        Pj = [th**2, -sp.expand(a * th**2 + a * th + b),
              sp.expand(c * (th + 1)**2)]
        Ppoly = lambda t1, t2: (F_(1) if 0 else 0)  # placeholder
        pa, pc = -a, c
    else:
        Pj = [th**3, -sp.expand((2 * th + 1) * (a * th**2 + a * th + b)),
              sp.expand((th + 1) * (c * (th + 1)**2 + d))]
        pa, pc = -2 * a, c
    y0 = A[:N + 1]
    g = gseries(Pj, y0)
    qser = smul([F_(0), F_(1)] + [F_(0)] * (N - 1),
                sexp(smul(g, sinv(y0))))
    tq = srevert(qser)
    Fq = compose(y0, tq)
    T = [tq[i + 1] for i in range(N)] + [F_(0)]
    thT = [F_(i) * T[i] for i in range(len(T))]
    corr = smul(thT, sinv(T))
    sigma = list(corr)
    sigma[0] = F_(1) + corr[0]
    t2 = smul(tq, tq)
    P = [F_(0)] * (N + 1)
    P[0] = F_(1)
    for i in range(N + 1):
        P[i] += F_(pa) * tq[i] + F_(pc) * t2[i]
    sw = sigma
    for _ in range(w - 1):
        sw = smul(sw, sigma)
    Psi = smul(smul(tq, sw), smul(sinv(P), sinv(Fq)))
    Theta = [F_(0)] + [Psi[m] / F_(m) ** w for m in range(1, N + 1)]
    yq = smul(Fq, Theta)
    bt = compose(yq, qser)
    ok = all(bt[n] == B[n] for n in range(NCHK + 1))
    mism = None
    if not ok:
        for n in range(NCHK + 1):
            if bt[n] != B[n]:
                mism = n
                break
    # nome integrality fingerprint
    intq = all(x.denominator == 1 for x in tq[:19])
    return ok, mism, intq

if __name__ == '__main__':
    print('%-10s | order | t(q) integral? | construction B(n) match (n<=%d)'
          % ('family', NCHK))
    for (name, tp, a, b, c, d) in FAMS:
        try:
            ok, mism, intq = run(name, tp, a, b, c, d)
            print('%-10s |   %d   | %s | %s%s'
                  % (name, tp, 'YES' if intq else 'no ',
                     'PASS' if ok else 'FAIL',
                     '' if ok else ' (first mismatch n=%s)' % mism),
                  flush=True)
        except Exception as e:
            print('%-10s |   %d   | ERROR: %s' % (name, tp, e), flush=True)
