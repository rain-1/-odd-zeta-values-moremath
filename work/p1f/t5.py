"""T5: the p-FREE reduction of (V3)_0.

For n < p, q := p-n, ntil := n-q = 2n-p, every ingredient of (V3)_0 reduces mod p to an
explicit rational function of (n,q) alone (Wilson + the reflections H_{p-1-j} = H_j,
H^(2)_{p-1-j} = -H^(2)_j, and  C(p+m,n)/p = (-1)^{n-m+1}/(n C(n-1,m))  for m < n).

Region I  : k in [0,q-1], lam in [0,ntil]      (l = q+lam)
Region III: ka,la in [0,ntil], ntil <= ka+la <= ntil+q-1   (k=q+ka, l=q+la, rho=ka+la-ntil)

F(n,q) := 2*Sigma_I + Sigma_III   -- computed as an EXACT rational number.
If F == 0 identically in (n,q), (V3)_0 is a p-free hypergeometric identity.
"""
import sys
from fractions import Fraction as F
from math import comb

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1f')
from kform import kforms

_H = {}
def H(m, r=1):
    if m <= 0:
        return F(0)
    k = (m, r)
    v = _H.get(k)
    if v is None:
        v = H(m - 1, r) + F(1, m ** r)
        _H[k] = v
    return v


def symname(s):
    return '%s%d%s' % (s[0], s[1], s[2]) if len(s) == 3 else '%s%d' % (s[0], s[1])


KI = {tuple(sorted(symname(s) for s in sym)): c
      for sym, c in kforms((0, 1, 1, 1))[3].items()}
KIII = {tuple(sorted(symname(s) for s in sym)): c
        for sym, c in kforms((1, 1, 0, 1))[3].items()}


def ev(mon, val):
    x = F(1)
    for s in mon:
        x *= val[s]
    return x


def Fnq(n, q, verbose=False):
    nt = n - q
    assert nt >= 0 and q >= 1
    n2 = F(1, n * n)
    SI = F(0)
    for k in range(0, q):
        for lam in range(0, nt + 1):
            w = ((-1) ** k) * comb(n + k, n) * comb(n, k) ** 2 * comb(n, nt - lam) ** 2
            w = F(w) * n2 / (comb(n - 1, lam) * comb(n - 1, k + lam))
            val = {
                'A1k': H(q - 1 - k) - H(k),      'A2k': -H(q - 1 - k, 2) - H(k, 2),
                'B1k': H(q + k - 1) - H(k),      'B2k': -H(q + k - 1, 2) - H(k, 2),
                'A1l': H(lam) - H(q + lam),      'A2l': H(lam, 2) - H(q + lam, 2),
                'B1l': H(nt - lam) - H(q + lam), 'B2l': H(nt - lam, 2) - H(q + lam, 2),
                'C1': H(k + lam) - H(k + q + lam),
                'C2': H(k + lam, 2) - H(k + q + lam, 2),
                'N1': H(q - 1), 'N2': -H(q - 1, 2),
            }
            SI += w * sum(c * ev(m, val) for m, c in KI.items())
    SIII = F(0)
    for ka in range(0, nt + 1):
        for la in range(0, nt + 1):
            rho = ka + la - nt
            if rho < 0 or rho > q - 1:
                continue
            w = -((-1) ** rho) * comb(n, nt - ka) ** 2 * comb(n, nt - la) ** 2 * comb(n + rho, n)
            w = F(w) * n2 / (comb(n - 1, ka) * comb(n - 1, la))
            val = {
                'A1k': H(ka) - H(q + ka),        'A2k': H(ka, 2) - H(q + ka, 2),
                'B1k': H(nt - ka) - H(q + ka),   'B2k': H(nt - ka, 2) - H(q + ka, 2),
                'A1l': H(la) - H(q + la),        'A2l': H(la, 2) - H(q + la, 2),
                'B1l': H(nt - la) - H(q + la),   'B2l': H(nt - la, 2) - H(q + la, 2),
                'C1': H(q - 1 - rho) - H(rho),
                'C2': -H(q - 1 - rho, 2) - H(rho, 2),
                'N1': H(q - 1), 'N2': -H(q - 1, 2),
            }
            SIII += w * sum(c * ev(m, val) for m, c in KIII.items())
    if verbose:
        print('    SI=%s  SIII=%s' % (SI, SIII))
    return 2 * SI + SIII


if __name__ == '__main__':
    NM = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    for n in range(2, NM + 1):
        for q in range(1, n + 1):
            v = Fnq(n, q)
            print('n=%2d q=%2d  F = %s' % (n, q, '0' if v == 0 else str(v)[:60]))
