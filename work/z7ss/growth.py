"""Rigorous growth-rate bound for single-sum factorial-ratio representations.

If  q_n = sum_k F(n,k),  F(n,k) = z^k prod_j ((a_j n + b_j k)!)^{e_j},
sum e_j a_j = sum e_j b_j = 0,  then with k = t n,

    |F(n,tn)| = exp( n f(t) + O(log n) ),   f(t) = sum_j e_j L_j log L_j + t log|z|,
    L_j = a_j + b_j t   (all L_j >= 0 on the support).

Since q_n is a sum of O(n) such terms,   limsup |q_n|^{1/n} <= exp( max_t f(t) ).

The target growth is mu = 6329.26051..., the dominant root of
L^4 - 6340 L^3 + 67974 L^2 - 6340 L + 1, so ANY representation must satisfy
max_t f(t) >= log mu = 8.75294.

f(t) is LINEAR in the exponent vector e, and the feasible set
{e : sum e a = 0, sum e b = 0, ||e||_1 <= W} is W times a fixed polytope, so

    max over shapes of weight <= W of max_t f(t)  =  W * h,
    h = max_t  max{ c(t).e : A e = 0, ||e||_1 <= 1 },

with the inner max attained at a vertex, i.e. supported on <= 3 coordinates.
Hence  W >= log(mu)/h  is a rigorous lower bound on the weight of ANY single-sum
factorial-ratio representation inside the (A,B) box.
"""
import numpy as np
from itertools import combinations
from math import log
import sys


def mu_target():
    return float(max(np.roots([1, -6340, 67974, -6340, 1]).real))


def forms(A, B):
    return [(a, b) for a in range(A + 1) for b in range(-B, B + 1)
            if not (a == 0 and b <= 0)]


def h_at_t(F, t, Z=1):
    idx = [j for j, (a, b) in enumerate(F) if a + b * t >= 0]
    c = np.array([(lambda L: 0.0 if L <= 0 else L * log(L))(F[j][0] + F[j][1] * t)
                  for j in idx])
    aa = np.array([F[j][0] for j in idx], dtype=float)
    bb = np.array([F[j][1] for j in idx], dtype=float)
    m = len(idx)
    best = 0.0
    tri = np.array(list(combinations(range(m), 3)))
    if len(tri):
        A0 = aa[tri]           # (T,3)
        B0 = bb[tri]
        u = np.stack([A0[:, 1] * B0[:, 2] - A0[:, 2] * B0[:, 1],
                      A0[:, 2] * B0[:, 0] - A0[:, 0] * B0[:, 2],
                      A0[:, 0] * B0[:, 1] - A0[:, 1] * B0[:, 0]], axis=1)
        s = np.abs(u).sum(axis=1)
        good = s > 1e-12
        u = u[good] / s[good, None]
        v = (c[tri[good]] * u).sum(axis=1)
        if len(v):
            best = float(np.max(np.abs(v)))
    return best + t * log(Z)


def scan(A, B, Z=1, T=None, N=1200):
    F = forms(A, B)
    if T is None:
        T = A + 1.0
    ts = np.linspace(0.0, T, N + 1)
    vals = np.array([h_at_t(F, float(x), Z) for x in ts])
    i = int(np.argmax(vals))
    lo, hi = ts[max(0, i - 1)], ts[min(N, i + 1)]
    for _ in range(80):
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if h_at_t(F, m1, Z) < h_at_t(F, m2, Z):
            lo = m1
        else:
            hi = m2
    ts2 = (lo + hi) / 2
    return max(float(vals[i]), h_at_t(F, ts2, Z)), ts2


if __name__ == "__main__":
    mu = mu_target()
    print("target mu =", repr(mu), " log mu =", log(mu))
    print()
    for (A, B) in [(1, 1), (2, 2), (3, 3), (4, 4)]:
        for Z in [1, 4]:
            h, ts = scan(A, B, Z)
            print(f"A={A} B={B} |z|<={Z}:  h = {h:.6f} (t*={ts:.4f})"
                  f"   => any representation needs weight W >= {log(mu)/h:.2f}")
        sys.stdout.flush()
