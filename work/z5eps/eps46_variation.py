"""eps46_variation.py -- FIRST APPLICATION of the curve-blindness tool:
do first variations of the BZ family anchor in the L_BZ recurrence?

Object: the l-direction derivative atom
    Qdot(n) := sum_{k,l} T(n,k,l) * Lam1(n,k,l),
    Lam1 = -3H_l + H_{n+l} + 2H_{n-l} - H_{k+l} + H_{n+k+l}
(the first variation of Q_n along the l-shift; equals -L1/2 of family 1).

Anchor test: does  L_BZ(Qdot)(n) = sum_{i=0}^3 r_i(n) * Q(n+i)  hold with
r_i in Q[n] of bounded degree?  Fit exactly over Q on n = 0..N1, verify on
held-out n = N1+1..N2.  A PASS means the variation satisfies an explicit
inhomogeneous L_BZ equation -- the variational anchor exists at order 1.
Also run: the k-direction and n-direction atoms, and the same test with
denominators (r_i with fixed denominator (n+1)(n+2)(n+3) allowed) if the
polynomial fit fails.
"""

import sys
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
import core

H = core.Hs
P_ = [1, -3, -3, 1, 1, -2, -2, -1, 1]

def dmap(v):
    a, b, c = v
    return [a, b, c, a + b, a + c, a - b, a - c, b + c, a + b + c]

def lam1(v, n, k, l):
    xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
    d = dmap(v)
    return sum(F(P_[i] * d[i]) * H(xs[i], 1) for i in range(9) if P_[i] * d[i])

def qdot(v, n):
    return sum(core.T(n, k, l) * lam1(v, n, k, l)
               for k in range(n + 1) for l in range(n + 1))

def lbz(seq, n):
    return (core.c0(n) * seq[n] + core.c1(n) * seq[n + 1]
            + core.c2(n) * seq[n + 2] + core.c3(n) * seq[n + 3])

def fit_module(delta, Qs, N1, N2, deg, denom=None):
    """solve delta(n) = sum_i r_i(n) Q(n+i), r_i poly deg<=deg (/denom(n)),
    exactly over Q via Gaussian elimination; verify held-out."""
    unk = 4 * (deg + 1)
    rows = []
    rhs = []
    for n in range(0, N1 + 1):
        den = denom(n) if denom else F(1)
        row = []
        for i in range(4):
            for j in range(deg + 1):
                row.append(F(n) ** j * Qs[n + i] / den)
        rows.append(row)
        rhs.append(delta[n])
    # Gaussian elimination over Q
    m = len(rows)
    aug = [row + [rhs[t]] for t, row in enumerate(rows)]
    r = 0
    piv = []
    for c in range(unk):
        pr = None
        for t in range(r, m):
            if aug[t][c] != 0:
                pr = t
                break
        if pr is None:
            continue
        aug[r], aug[pr] = aug[pr], aug[r]
        pv = aug[r][c]
        aug[r] = [x / pv for x in aug[r]]
        for t in range(m):
            if t != r and aug[t][c] != 0:
                f = aug[t][c]
                aug[t] = [x - f * y for x, y in zip(aug[t], aug[r])]
        piv.append(c)
        r += 1
        if r == m:
            break
    # consistency of the fit rows
    for t in range(r, m):
        if aug[t][unk] != 0:
            return None, 'inconsistent on fit range'
    x = [F(0)] * unk
    for t, c in enumerate(piv):
        x[c] = aug[t][unk]
    # held-out verification
    for n in range(N1 + 1, N2 + 1):
        den = denom(n) if denom else F(1)
        val = F(0)
        idx = 0
        for i in range(4):
            for j in range(deg + 1):
                val += x[idx] * F(n) ** j * Qs[n + i] / den
                idx += 1
        if val != delta[n]:
            return None, 'held-out FAIL at n=%d' % n
    return x, 'PASS'

if __name__ == '__main__':
    N2 = 34          # need Qdot to N2+3
    NTOP = N2 + 3
    print('computing Qdot sequences to n=%d ...' % NTOP, flush=True)
    DIRS = {'l-shift': (0, 0, 1), 'k-shift': (0, 1, 0), 'n-shift': (1, 0, 0)}
    for name, v in DIRS.items():
        qd = [qdot(v, n) for n in range(NTOP + 1)]
        Qs = [core.Q(n) for n in range(NTOP + 1)]
        delta = [lbz(qd, n) for n in range(N2 + 1)]
        if all(x == 0 for x in delta):
            print('%-8s: L_BZ(Qdot) = 0 identically (n<=%d) -- Qdot is a '
                  'SOLUTION of L_BZ itself' % (name, N2), flush=True)
            continue
        done = False
        for deg in (6, 9, 12, 15):
            N1 = min(N2 - 6, 4 * (deg + 1) // 4 + deg + 6)
            x, verdict = fit_module(delta, Qs, N1, N2, deg)
            if x is not None:
                print('%-8s: ANCHORED  deg<=%d  fit n<=%d, held-out to %d: %s'
                      % (name, deg, N1, N2, verdict), flush=True)
                nz = [(i, j, x[i * (deg + 1) + j]) for i in range(4)
                      for j in range(deg + 1) if x[i * (deg + 1) + j]]
                print('   r_i(n) nonzero terms (i, n-power, coeff):')
                for i, j, cc in nz[:24]:
                    print('     r_%d n^%d : %s' % (i, j, cc))
                done = True
                break
            else:
                print('%-8s: deg<=%d -> %s' % (name, deg, verdict), flush=True)
        if not done:
            x, verdict = fit_module(delta, Qs, N2 - 6, N2, 12,
                                    denom=lambda n: F((n + 1) * (n + 2)
                                                      * (n + 3)))
            print('%-8s: with denominator (n+1)(n+2)(n+3): %s'
                  % (name, verdict), flush=True)
