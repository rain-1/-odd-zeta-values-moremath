"""eps4.py -- tensor sweep for the FULL 9-letter deformation space.

Per-cell scalars:
  weight-1 (5): X = D1-contraction, Y = V1-contraction (the sym null space N1),
                U1,U2,U3 = antisym differences H_k-H_l, H_{n+k}-H_{n+l}, H_{n-k}-H_{n-l}
  weight-r (9): h_r[c] for the 6 sym classes  +  w_r[j] antisym diffs, j=0,1,2
Tensors:  Sigma T * (products of these) for every product of total weight <= 5
that the epsilon-expansion of exp(sum eps^m L_m) can need, with
L1 = a X + b Y + alpha.U  (S1 in the 2-dim sym null space is necessary; antisym free).

Saved to eps4_tensors_<p>.pkl.
"""
import sys, pickle
from math import comb
from itertools import combinations_with_replacement as cwr

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
import core

NMAX = 30
D1VEC = (0, -3, 1, 2, -2, 2)
V1VEC = (2, 1, -2, -1, 2, 0)

# index sets
I5 = list(range(5))     # V
I9 = list(range(9))     # weight-r letters: 0..5 sym classes, 6..8 antisym pairs
I6 = list(range(6))

V_MON = {d: list(cwr(I5, d)) for d in range(6)}   # monomials in V of degree d


def sweep(p, nmax=NMAX):
    HM = 3 * nmax + 2
    H = [[0] * (HM + 1) for _ in range(6)]
    for m in range(1, HM + 1):
        im = pow(m, p - 2, p); acc = im
        H[1][m] = (H[1][m - 1] + acc) % p
        for r in range(2, 6):
            acc = acc * im % p
            H[r][m] = (H[r][m - 1] + acc) % p

    TN = {}
    # keys: ('V',d,mono) ; ('VH',d,mono,r,a) ; ('VHH',d,mono,(r1,a1),(r2,a2)) ; ...
    # organise as dict of lists over n
    def newkey(k):
        TN[k] = [0] * (nmax + 1)

    for d in range(1, 6):
        for mo in V_MON[d]: newkey(('V', mo))
    for r, dmax in ((2, 3), (3, 2), (4, 1)):
        for d in range(0, dmax + 1):
            for mo in V_MON[d]:
                for a in I9:
                    newkey(('VH', mo, r, a))
    for a in I9:
        newkey(('VH', (), 5, a))
    # H2*H2 with V-degree <= 1 ; H2*H3 with V-degree 0
    for d in range(0, 2):
        for mo in V_MON[d]:
            for a, b_ in cwr(I9, 2):
                newkey(('VHH', mo, 2, a, 2, b_))
    for a in I9:
        for b_ in I9:
            newkey(('VHH', (), 2, a, 3, b_))

    keys = list(TN.keys())
    print('tensor count:', len(keys))

    for n in range(nmax + 1):
        for k in range(n + 1):
            ck = comb(n + k, n) * comb(n, k) ** 2
            for l in range(n + 1):
                t = (ck * comb(n + l, n) * comb(n, l) ** 2
                     * comb(n + k + l, n)) % p
                # letters
                sym_args = [(n,), (k, l), (n + k, n + l), (n - k, n - l),
                            (k + l,), (n + k + l,)]
                pair_args = [(k, l), (n + k, n + l), (n - k, n - l)]
                hs = {}     # hs[r] = list of 9 letter values
                for r in range(1, 6):
                    row = [sum(H[r][x] for x in a) % p for a in sym_args]
                    row += [(H[r][a[0]] - H[r][a[1]]) % p for a in pair_args]
                    hs[r] = row
                V = [0] * 5
                V[0] = sum(D1VEC[c] * hs[1][c] for c in range(6)) % p
                V[1] = sum(V1VEC[c] * hs[1][c] for c in range(6)) % p
                V[2], V[3], V[4] = hs[1][6], hs[1][7], hs[1][8]
                # monomial values
                mv = {(): 1}
                for d in range(1, 6):
                    for mo in V_MON[d]:
                        mv[mo] = mv[mo[:-1]] * V[mo[-1]] % p
                # accumulate
                for key in keys:
                    kind = key[0]
                    if kind == 'V':
                        val = mv[key[1]]
                    elif kind == 'VH':
                        _, mo, r, a = key
                        val = mv[mo] * hs[r][a] % p
                    else:
                        _, mo, r1, a, r2, b_ = key
                        val = mv[mo] * hs[r1][a] % p * hs[r2][b_] % p
                    TN[key][n] = (TN[key][n] + t * val) % p
        if n % 10 == 0:
            print('  n =', n, 'done')
    return TN


if __name__ == '__main__':
    for p in (2147483647, 2147483629):
        print('prime', p)
        TN = sweep(p)
        with open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/eps4_tensors_%d.pkl' % p, 'wb') as f:
            pickle.dump({'NMAX': NMAX, 'p': p, 'TN': TN}, f)
        print('saved tensors for', p)
