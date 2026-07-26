"""Verify the CLOSED FORMS against EVERY exact ladder value n = 0..360, modulo two
large primes (exact rational arithmetic is infeasible at n = 360: 130321 cells).
Combined with the exact-Fraction check for n <= 34 this pins the identities on the
whole available data set."""
import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from design2 import Eng
from bare import lad_mod

NMAX = 360
for q in (33554393, 33554467):
    E = Eng(NMAX, q, 5)
    bad3, bad5 = [], []
    for n in range(NMAX + 1):
        Tv, idx = E.cells(n)
        H = E.H
        # idx: 0 n, 1 k, 2 l, 3 n+k, 4 n+l, 5 n-k, 6 n-l
        h1 = {s: H[1][idx[s]] for s in (1, 2, 3, 4, 5, 6)}
        al = (h1[3] - h1[1] - h1[4] + h1[2]) % q            # A1(k)-A1(l)
        be = (h1[5] - h1[1] - h1[6] + h1[2]) % q            # B1(k)-B1(l)
        inv2 = pow(2, q - 2, q); inv4 = pow(4, q - 2, q)
        Psi = (al * inv2 + be) % q
        A2k = (H[2][idx[3]] - H[2][idx[1]]) % q
        A2l = (H[2][idx[4]] - H[2][idx[2]]) % q
        H3 = H[3][idx[3]]; H4 = H[4][idx[3]]; H5 = H[5][idx[3]]
        w3 = (H3 - Psi * H[2][idx[3]]) % q
        w5 = (H5 + inv2 * (al - be) % q * H4
              + (inv4 * (A2k + A2l) - inv2 * al % q * Psi) % q * H3) % q
        s3 = int((Tv * w3 % q).sum() % q)
        s5 = int((Tv * w5 % q).sum() % q)
        if s3 != lad_mod('Ph', n, q):
            bad3.append(n)
        if s5 != lad_mod('P', n, q):
            bad5.append(n)
    print('q=%d  n=0..%d :  w3->Phat %s ,  w5->P %s'
          % (q, NMAX, 'ALL PASS' if not bad3 else 'FAIL %s' % bad3[:6],
             'ALL PASS' if not bad5 else 'FAIL %s' % bad5[:6]), flush=True)
