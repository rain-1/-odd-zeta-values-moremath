"""eps49_zeta_companion.py -- the companion of family zeta in modular letters.

Derivation (exact, see MODULAR_COACTION_PROBE.md Part C):
  y_B := sum B(n) t^n  (B(0)=0, B(1)=1 second solution)  satisfies
      L_t(y_B) = t                     (the n=0 boundary term, exactly),
  and with the MUM kernel {F, F log q, F (log q)^2/2} the operator factors
      L_t = (P3(t)/sigma^3) * F * theta_q^3 * (1/F),
      P3(t) = 1 - 2a t + c t^2   (leading theta^3 coefficient),
      sigma = theta_q log t = q t'(q)/t(q).
  Hence the COMPANION FORMULA in modular letters:

      B(n) = [t^n]  F(q) * Theta(q),
      Theta = theta_q^{-3} Psi = sum_{m>=1} Psi_m q^m / m^3,
      Psi   = t * sigma^3 / (P3(t(q)) * F(q)).

Verification: exact over Q for n <= NCHK, for zeta (9,3,-27,0) and the
control gamma = Apery zeta(3) (17,5,1,0).
"""

import sys
from fractions import Fraction as F_

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import eps48_modular_nome as M
from eps48_modular_nome import (smul, sinv, sexp, srevert, compose,
                                A_seq_R3, gseries, N)
import sympy as sp

th = sp.symbols('th')
NCHK = 22


def run_family(name, a, b, c, d):
    Aser = A_seq_R3(a, b, c, d, N + 2)
    Pj = [th**3,
          -sp.expand((2 * th + 1) * (a * th**2 + a * th + b)),
          sp.expand((th + 1) * (c * (th + 1)**2 + d))]
    y0 = Aser[:N + 1]
    g = gseries(Pj, y0)
    ratio = smul(g, sinv(y0))
    qser = smul([F_(0), F_(1)] + [F_(0)] * (N - 1), sexp(ratio))   # q(t)
    tq = srevert(qser)                                             # t(q)
    Fq = compose(y0, tq)                                           # F(q)
    # sigma = theta_q log t = 1 + theta(T)/T with t = q*T
    T = [tq[i + 1] for i in range(N)] + [F_(0)]
    thT = [F_(i) * T[i] for i in range(len(T))]
    sigma = [F_(1)] * 1 + [F_(0)] * N
    corr = smul(thT, sinv(T))
    sigma = [F_(1) + corr[0] if i == 0 else corr[i] for i in range(N + 1)]
    sigma[0] = F_(1) + corr[0]
    # P3(t(q)) = 1 - 2a t + c t^2
    t2 = smul(tq, tq)
    P3 = [F_(1) - 2 * a * tq[i] + c * t2[i] if i == 0
          else F_(-2 * a) * tq[i] + F_(c) * t2[i] for i in range(N + 1)]
    P3[0] = F_(1)
    sig3 = smul(sigma, smul(sigma, sigma))
    Psi = smul(smul(tq, sig3), smul(sinv(P3), sinv(Fq)))
    Theta = [F_(0)] + [Psi[m] / F_(m) ** 3 for m in range(1, N + 1)]
    yq = smul(Fq, Theta)
    bt = compose(yq, qser)          # back to t-coordinate
    # recurrence second solution
    B = [F_(0), F_(1)]
    for n in range(1, N + 1):
        B.append((F_((2 * n + 1) * (a * n * n + a * n + b)) * B[n]
                  - F_(n * (c * n * n + d)) * B[n - 1]) / F_((n + 1) ** 3))
    ok = all(bt[n] == B[n] for n in range(NCHK + 1))
    print('%s: companion formula B(n) = [t^n] F * theta^{-3}(t sigma^3/(P3 F))'
          '  == recurrence B(n), n<=%d: %s'
          % (name, NCHK, 'PASS' if ok else 'FAIL'))
    if not ok:
        for n in range(NCHK + 1):
            if bt[n] != B[n]:
                print('  first mismatch n=%d: %s vs %s' % (n, bt[n], B[n]))
                break
    return ok, (tq, Fq, Psi)


if __name__ == '__main__':
    ok1, _ = run_family('gamma (Apery z3 control)', 17, 5, 1, 0)
    ok2, dat = run_family('zeta', 9, 3, -27, 0)
    if ok2:
        tq, Fq, Psi = dat
        print('\nzeta modular data:')
        print('  F(q)   = (9E2(q^9)-E2(q))/8 (proved-identified to q^26)')
        print('  Psi(q) coeffs:', [str(x) for x in Psi[:14]])
