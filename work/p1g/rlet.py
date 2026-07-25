"""P1g: Apery-type ("R") letters and their exact pole structure.

  R^(a)(n,k) = sum_{m=1}^{k} (-1)^{m-1} / ( m^a C(n,m) C(n+m,m) )        [k-slot]
  D^(a)(n,m) = sum_{j=1}^{m} (-1)^{j-1} / ( j^a C(n+j,j) )               [coupling slot]

Both exact (Fraction) and mod-q versions.  This module also *verifies* the pole
structure that the depth calculus will assume:

  (R1) for p >= 5, n < p, 0 <= k <= n :  v_p(R^(a)(n,k)) >= -1, and  >= 0 unless
       alpha := [n+k >= p] = 1.                                  (Prop 7.2 of PHASE2_CANCEL)
  (D1) for p >= 5, n < p, 0 <= m <= 2n, eps := floor(m/p) :
       if eps = 0 : v_p(D^(a)(n,m)) >= -1, and >= 0 unless [n+m >= p] = kappa.
       if eps = 1 : v_p(D^(a)(n,m)) >= -a   (the j = p term).
"""
import sys
from fractions import Fraction as F
from math import comb

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import vp

MAXR = 5


# ------------------------------------------------------------------ exact
def R_exact(n, k, a):
    s = F(0)
    for m in range(1, k + 1):
        s += F((-1) ** (m - 1), m ** a * comb(n, m) * comb(n + m, m))
    return s


def D_exact(n, m, a):
    s = F(0)
    for j in range(1, m + 1):
        s += F((-1) ** (j - 1), j ** a * comb(n + j, j))
    return s


# ------------------------------------------------------------------ mod q
def R_tab(n, q, maxr=MAXR):
    """{a: array over k=0..n of R^(a)(n,k) mod q}"""
    import numpy as np
    # C(n,m) and C(n+m,m) for m=0..n
    cnm = [1] * (n + 1)
    cpm = [1] * (n + 1)
    for m in range(1, n + 1):
        cnm[m] = cnm[m - 1] * (n - m + 1) % q * pow(m, q - 2, q) % q
        cpm[m] = cpm[m - 1] * (n + m) % q * pow(m, q - 2, q) % q
    out = {}
    for a in range(1, maxr + 1):
        arr = np.zeros(n + 1, dtype=np.int64)
        acc = 0
        for m in range(1, n + 1):
            term = pow(m, q - 2, q)
            term = pow(term, a, q)
            term = term * pow(cnm[m], q - 2, q) % q * pow(cpm[m], q - 2, q) % q
            if m % 2 == 0:
                term = (-term) % q
            acc = (acc + term) % q
            arr[m] = acc
        out[a] = arr
    return out


def D_tab(n, q, maxr=MAXR):
    """{a: array over m=0..2n of D^(a)(n,m) mod q}"""
    import numpy as np
    M = 2 * n
    cpj = [1] * (M + 1)
    for j in range(1, M + 1):
        cpj[j] = cpj[j - 1] * (n + j) % q * pow(j, q - 2, q) % q
    out = {}
    for a in range(1, maxr + 1):
        arr = np.zeros(M + 1, dtype=np.int64)
        acc = 0
        for j in range(1, M + 1):
            term = pow(pow(j, q - 2, q), a, q) * pow(cpj[j], q - 2, q) % q
            if j % 2 == 0:
                term = (-term) % q
            acc = (acc + term) % q
            arr[j] = acc
        out[a] = arr
    return out


# ------------------------------------------------------------------ verification
if __name__ == '__main__':
    PR = [5, 7, 11, 13, 17, 19, 23]
    print('(R1) k-slot Apery letters R^(a)(n,k): pole order and indicator', flush=True)
    for a in range(1, MAXR + 1):
        mx, off, ncell = 0, 0, 0
        for p in PR:
            for n in range(1, p):
                for k in range(n + 1):
                    ncell += 1
                    v = R_exact(n, k, a)
                    d = max(0, -vp(v, p)) if v else 0
                    mx = max(mx, d)
                    if d > 0 and n + k < p:
                        off += 1
        print('   a=%d : cells=%d  max pole order=%d  poles off alpha=1 : %d'
              % (a, ncell, mx, off), flush=True)

    print('(D1) coupling Apery letters D^(a)(n,m): pole order by eps', flush=True)
    for a in range(1, MAXR + 1):
        mx0, mx1, off0, ncell = 0, 0, 0, 0
        for p in PR:
            for n in range(1, p):
                for m in range(2 * n + 1):
                    ncell += 1
                    eps = m // p
                    v = D_exact(n, m, a)
                    d = max(0, -vp(v, p)) if v else 0
                    if eps == 0:
                        mx0 = max(mx0, d)
                        if d > 0 and n + m < p:
                            off0 += 1
                    else:
                        mx1 = max(mx1, d)
        print('   a=%d : cells=%d  max order (eps=0)=%d [off kappa: %d]  max order (eps=1)=%d'
              % (a, ncell, mx0, off0, mx1), flush=True)
