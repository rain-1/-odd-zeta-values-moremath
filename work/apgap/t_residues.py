"""TEST 3: the rational function g_r and the residue mechanism.

    g_r(z) = [ (z+1)(z+2)...(z+r) / ( z(z-1)...(z-r) ) ]^2          (rational!)

    A_Gamma(r,z) = (sin^2 pi z / pi^2) g_r(z)                        (reflection)

Local data at the double pole z=s (0<=s<=r), from (z-s)^2 g_r = phi^2:
    alpha_s = A(r,s)                      = value  Phi(s)
    beta_s  = Res_{z=s} g_r = 2A(r,s)v    = Phi'(s)          -> V_r  (proved, sec 3.2)
    FP_s    = A(r,s) * ch_c2(r,s)         = finite part
and for t > r:
    g_r(r+m) = C(r,m) = ((2r+m)!(m-1)!/((r+m)!)^2)^2          -> the borrow weight

Facts checked here:
  F1  g_r(r+m) == C(r,m)
  F2  FP_s == A(r,s)*ch_c2(r,s)   and   sum_s FP_s == Scc(r)
  F3  beta_s == 2A(r,s)v(r,s)     and   sum_s beta_s == 2 V_r == 0
  F4  Res_{z=s} h_r == A(r,s)(ch_ac+2ch_c2),  h_r = 4 g_r(z) sum_{i<=r} 1/(z+i)
      and   sum_s Res_s h_r == 0                                     (=> R1)
  F5  sum_{s<=r} FP_s + sum_{t=r+1}^{p-1} g_r(t) == 0 (mod p)        (=> R2)
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/apdef')
from fractions import Fraction as F
from core import A, Hs, modp
from gap_core import sigmas, Cfun, Xi, Vr


def local(r, s):
    """(alpha, beta, FP) of g_r at the double pole z=s, from log-derivatives of phi."""
    phi2 = F(A(r, s))
    L1 = sum((F(1, s + i) for i in range(1, r + 1)), F(0)) \
        - sum((F(1, s - j) for j in range(r + 1) if j != s), F(0))
    L2 = -sum((F(1, (s + i) ** 2) for i in range(1, r + 1)), F(0)) \
        + sum((F(1, (s - j) ** 2) for j in range(r + 1) if j != s), F(0))
    return phi2, 2 * phi2 * L1, phi2 * (2 * L1 * L1 + L2)


def res_h(r, s):
    """Res_{z=s} of h_r = 4 g_r(z) T(z),  T(z)=sum_{i=1}^r 1/(z+i)"""
    al, be, _ = local(r, s)
    T = Hs(r + s, 1) - Hs(s, 1)
    Tp = -(Hs(r + s, 2) - Hs(s, 2))
    return 4 * (al * Tp + be * T)


def g(r, t):
    """g_r(t) for integer t not in [0,r]"""
    num = 1
    for i in range(1, r + 1):
        num *= (t + i)
    den = 1
    for j in range(r + 1):
        den *= (t - j)
    return F(num, den) ** 2


PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

if __name__ == '__main__':
    RMAX = 40
    print('F1  g_r(r+m) == C(r,m)                      :',
          all(g(r, r + m) == Cfun(r, m)
              for r in range(RMAX + 1) for m in range(1, 12)))

    ok2a = ok2b = ok3a = ok3b = ok4a = ok4b = True
    for r in range(RMAX + 1):
        Sa2, Sac, Scc = sigmas(r)
        fps = bes = F(0)
        rs = F(0)
        for s in range(r + 1):
            al, be, fp = local(r, s)
            u = Hs(r + s, 1) - Hs(r - s, 1)
            v = Hs(r + s, 1) + Hs(r - s, 1) - 2 * Hs(s, 1)
            chc = 2 * v * v - (Hs(r + s, 2) - 2 * Hs(s, 2) - Hs(r - s, 2))
            cha = 4 * u * v - 2 * (Hs(r + s, 2) + Hs(r - s, 2))
            ok2a &= (fp == A(r, s) * chc)
            ok3a &= (be == 2 * A(r, s) * v)
            ok4a &= (res_h(r, s) == A(r, s) * (cha + 2 * chc))
            fps += fp; bes += be; rs += res_h(r, s)
        ok2b &= (fps == Scc)
        ok3b &= (bes == 2 * Vr(r) and bes == 0)
        ok4b &= (rs == 0)
    print('F2  FP_s == A(r,s) ch_c2      (r<=%d)        : %s' % (RMAX, ok2a))
    print('    sum_s FP_s == Scc(r)                    :', ok2b)
    print('F3  beta_s == 2A(r,s)v                      :', ok3a)
    print('    sum_s beta_s == 2V_r == 0                :', ok3b)
    print('F4  Res_s h_r == A(r,s)(ch_ac+2 ch_c2)      :', ok4a)
    print('    sum_s Res_s h_r == 0   (=> R1)          :', ok4b)

    print('\nF5  sum_{s<=r} FP_s + sum_{t=r+1}^{p-1} g_r(t) == 0 (mod p)')
    bad = 0; tot = 0
    for p in PRIMES:
        for r in range(p):
            lhs = sum((local(r, s)[2] for s in range(r + 1)), F(0)) \
                + sum((g(r, t) for t in range(r + 1, p)), F(0))
            tot += 1
            if modp(lhs, p) != 0:
                bad += 1
                print('   FAIL p=%d r=%d' % (p, r))
    print('    cells %d  failures %d' % (tot, bad))
