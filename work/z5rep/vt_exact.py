"""STEP 1a -- exact rational verification that  sum_{k,l} T(n,k,l) vtilde(n,k,l) = Phat_n
against the exact ladder in work/z5la/ladder_w3.pkl  (n = 0..20).

vtilde = H^(3)_n + 2 A3(k) + (1/2)(A2(l) - A2(k)) * Psi_k ,  Psi_k = A1(k) + 3 B1(k)
A_r(x) = H^(r)_{n+x} - H^(r)_x ,  B_r(x) = H^(r)_{n-x} - H^(r)_x
"""
from fractions import Fraction as Fr
from math import comb
import pickle, sys

_H = {}


def H(r, x):
    if x < 0:
        raise ValueError('H^(%d)_%d' % (r, x))
    key = (r, x)
    if key not in _H:
        _H[key] = sum(Fr(1, j ** r) for j in range(1, x + 1))
    return _H[key]


def T(n, k, l):
    return (comb(n + k, n) * comb(n, k) ** 2 * comb(n + l, n)
            * comb(n, l) ** 2 * comb(n + k + l, n))


def A(r, n, x):
    return H(r, n + x) - H(r, x)


def B(r, n, x):
    return H(r, n - x) - H(r, x)


def vtilde(n, k, l):
    Psi_k = A(1, n, k) + 3 * B(1, n, k)
    return H(3, n) + 2 * A(3, n, k) + Fr(1, 2) * (A(2, n, l) - A(2, n, k)) * Psi_k


def w3hat(n, k, l):
    Psi = (Fr(1, 2) * H(1, n + k) - Fr(1, 2) * H(1, n + l)
           + H(1, n - k) - H(1, n - l)
           - Fr(3, 2) * H(1, k) + Fr(3, 2) * H(1, l))
    return H(3, n + k) - Psi * H(2, n + k)


def ladder(f, N):
    out = []
    for n in range(N + 1):
        s = Fr(0)
        for k in range(n + 1):
            for l in range(n + 1):
                t = T(n, k, l)
                if t:
                    s += t * f(n, k, l)
        out.append(s)
    return out


if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    ref = pickle.load(open('../z5la/ladder_w3.pkl', 'rb'))
    Ph = ref['Phat']
    V = ladder(vtilde, N)
    W = ladder(w3hat, N)
    bad_v = [(n, V[n], Ph[n]) for n in range(N + 1) if V[n] != Ph[n]]
    bad_w = [(n, W[n], Ph[n]) for n in range(N + 1) if W[n] != Ph[n]]
    print('n = 0..%d cells checked (exact Fraction)' % N)
    print('sum T*vtilde == Phat :', 'ALL EQUAL' if not bad_v else bad_v[:3])
    print('sum T*w3hat  == Phat :', 'ALL EQUAL' if not bad_w else bad_w[:3])
    print('Phat[0..4] =', Ph[:5])
    print('V   [0..4] =', V[:5])
    # L_BZ residual on the vtilde ladder
    sys.path.insert(0, '../z5la')
    import zla
    bad = []
    for n in range(0, N - 3 + 1):
        c = zla.cc(n)
        v = sum(Fr(c[i]) * V[n + i] for i in range(4))
        if v != 0:
            bad.append((n, v))
    print('L_BZ . (sum T*vtilde) = 0 for n=0..%d :' % (N - 3),
          'ALL ZERO' if not bad else bad[:3])
