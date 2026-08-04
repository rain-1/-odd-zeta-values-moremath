"""eps47_tower2.py -- SECOND rung of the variational tower, n-direction.

Cell: T(n+eps,k,l) = T * exp(A1 eps + A2 eps^2 + ...) with (d_L in {0,1},
so all gamma/zeta constants vanish: S_m = S_1 = 0):
    A1 = sum_L p_L d_L H1_{x_L},   A2 = -(1/2) sum_L p_L d_L H2_{x_L}.
First variation  QD1(n) = sum T*A1  (eps46: L(QD1) = -sum c_i' Q(n+i)).
Second variation QD2(n) = [eps^2] sum = sum T*(A1^2/2 + A2);  d^2Q/dn^2 = 2*QD2.

Twice-differentiated recurrence prediction:
    sum_i [ c_i''(n) Q(n+i) + 2 c_i'(n) QD1(n+i) + c_i(n) * 2*QD2(n+i) ] = 0.

Boundary audit for the second derivative: continuation cells k>n (or l>n)
have a DOUBLE zero from 1/Gamma(n-k+1)^2, so their second n-derivative
still vanishes at integer n (first derivative of a double zero is zero);
cells with both k>n and l>n vanish to fourth order.  Hence d^2/dn^2 of the
continued sum at integer n equals the finite-range sum of cell second
derivatives.  Exact test over Q for n <= NMAX.
"""
import sys
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
import core
import sympy as sp

H = core.Hs
P_ = [1, -3, -3, 1, 1, -2, -2, -1, 1]
D_ = [1, 0, 0, 1, 1, 1, 1, 0, 1]          # n-direction letter shifts

def a12(n, k, l):
    xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
    a1 = sum(F(P_[i] * D_[i]) * H(xs[i], 1) for i in range(9) if P_[i] * D_[i])
    a2 = -F(1, 2) * sum(F(P_[i] * D_[i]) * H(xs[i], 2)
                        for i in range(9) if P_[i] * D_[i])
    return a1, a2

def qd12(n):
    s1 = F(0)
    s2 = F(0)
    for k in range(n + 1):
        for l in range(n + 1):
            t = core.T(n, k, l)
            a1, a2 = a12(n, k, l)
            s1 += t * a1
            s2 += t * (a1 * a1 / 2 + a2)
    return s1, s2

nsym = sp.symbols('n')
a0p = 41218 * nsym**3 + 198849 * nsym**2 + 320790 * nsym + 173057
B8 = (3874492*nsym**8 + 59373972*nsym**7 + 394148190*nsym**6
      + 1481084196*nsym**5 + 3447878810*nsym**4 + 5095855458*nsym**3
      + 4673546679*nsym**2 + 2433871008*nsym + 551502039)
B9 = (48802112*nsym**9 + 967468896*nsym**8 + 8488000862*nsym**7
      + 43246197636*nsym**6 + 140983768422*nsym**5 + 304912330849*nsym**4
      + 437406946975*nsym**3 + 401272692378*nsym**2 + 213593890911*nsym
      + 50257929339)
CS = [sp.expand((nsym+1)**5*(nsym+2)*a0p.subs(nsym, nsym+1)),
      sp.expand(-2*(nsym+2)*B8), sp.expand(-2*B9),
      sp.expand(2*(nsym+3)**5*(2*nsym+5)*a0p)]
C0 = [sp.Poly(c, nsym) for c in CS]
C1 = [sp.Poly(sp.diff(c, nsym), nsym) for c in CS]
C2 = [sp.Poly(sp.diff(c, nsym, 2), nsym) for c in CS]
ev = lambda P, m: F(int(P.eval(m)))

if __name__ == '__main__':
    NMAX = 15
    qd = [qd12(n) for n in range(NMAX + 4)]
    Q = [core.Q(n) for n in range(NMAX + 4)]
    ok = True
    for m in range(NMAX + 1):
        tot = F(0)
        for i in range(4):
            tot += (ev(C2[i], m) * Q[m + i]
                    + 2 * ev(C1[i], m) * qd[m + i][0]
                    + ev(C0[i], m) * 2 * qd[m + i][1])
        if tot != 0:
            ok = False
            print('n=%d SECOND-VARIATION MISMATCH: %s' % (m, tot))
    print('TOWER RUNG 2 (n-direction):',
          'PASS exact Q, n<=%d' % NMAX if ok else 'FAIL')
