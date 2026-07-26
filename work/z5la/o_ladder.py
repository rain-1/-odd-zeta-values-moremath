"""Exact rational ladders  Q_n, P_n, Phat_n  and the residual  X_n = (L_BZ . Phat)_n.
These are the initial values the order-m fallback argument needs."""
from fractions import Fraction as Fr
from math import comb
import zla

_H = {}


def H(r, x):
    if x < 0: raise ValueError('H^(%d)_%d' % (r, x))
    key = (r, x)
    if key not in _H:
        _H[key] = sum(Fr(1, j ** r) for j in range(1, x + 1))
    return _H[key]


def T(n, k, l):
    return (comb(n + k, n) * comb(n, k) ** 2 * comb(n + l, n)
            * comb(n, l) ** 2 * comb(n + k + l, n))


def w3hat(n, k, l):
    Psi = (Fr(1, 2) * H(1, n + k) - Fr(1, 2) * H(1, n + l)
           + H(1, n - k) - H(1, n - l)
           - Fr(3, 2) * H(1, k) + Fr(3, 2) * H(1, l))
    return H(3, n + k) - Psi * H(2, n + k)


def w5(n, k, l):
    al = H(1, n + k) - H(1, k) - H(1, n + l) + H(1, l)
    be = H(1, n - k) - H(1, k) - H(1, n - l) + H(1, l)
    Psi = al / 2 + be
    S2 = (H(2, n + k) - H(2, k)) + (H(2, n + l) - H(2, l))
    return (H(5, n + k) + Fr(1, 2) * (al - be) * H(4, n + k)
            + (S2 / 4 - al * Psi / 2) * H(3, n + k))


def ladder(f, N):
    out = []
    for n in range(N + 1):
        s = Fr(0)
        for k in range(n + 1):
            for l in range(n + 1):
                t = T(n, k, l)
                if t: s += t * f(n, k, l)
        out.append(s)
    return out


if __name__ == '__main__':
    N = 22
    Q = ladder(lambda n, k, l: Fr(1), N)
    Ph = ladder(w3hat, N)
    print('Q_n  n=0..3 :', Q[:4])
    print('Phat n=0..4 :', Ph[:5])
    known = [Fr(0), Fr(101, 4), Fr(344923, 96), Fr(3710571371, 4320),
             Fr(602417685937, 2304)]
    print('Phat matches ZETA5_CLOSEDFORM ladder n=0..4 :', Ph[:5] == known)
    print('Q matches 1,21,2989,714549 :', Q[:4] == [1, 21, 2989, 714549])
    bad = []
    for n in range(0, N - 3 + 1):
        c = zla.cc(n)
        for name, seq in (('Q', Q), ('Phat', Ph)):
            v = sum(Fr(c[i]) * seq[n + i] for i in range(4))
            if v != 0: bad.append((name, n, v))
    print('L_BZ . Q  and  L_BZ . Phat  vanish for n = 0..%d :' % (N - 3),
          'ALL ZERO' if not bad else bad)
    import pickle
    pickle.dump(dict(Q=Q, Phat=Ph), open('ladder_w3.pkl', 'wb'))
    print('leading coeff c_3(n) = 2(n+3)^5(2n+5)a0(n),  a0(n)=41218n^3+198849n^2+320790n+173057')
    print('c_3(n) > 0 for every n >= 0 :', all(zla.cc(n)[3] > 0 for n in range(0, 200)))
