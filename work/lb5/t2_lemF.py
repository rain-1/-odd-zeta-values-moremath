"""Fast verification of Lemma F (refined fibre-Lucas) over larger primes, mod p^8.

Lemma F.  n = ap+r, 1<=a<p, 0<=r<p, p not dividing Q_a.  For 0<=b,c<=a put
    Tcal(b,c) = sum_{s,t=0}^{p-1} T(n, bp+s, cp+t),
    d(b,c)    = max(0, -v_p( v(a,b,c) )),      v = w3hat - H^(3)_n .
Then   Tcal(b,c)  ==  (Q_n/Q_a) * T(a,b,c)   (mod p^{1+d(b,c)}).
"""
import sys
from math import comb
from fractions import Fraction as F
from core import Q, Ph, Hs, w3hat, vp

CAP = 8

def vp_mod(x, p, cap=CAP):
    """v_p of an integer known mod p^cap; returns cap if x==0 mod p^cap."""
    x %= p**cap
    if x == 0:
        return cap
    v = 0
    while x % p == 0:
        x //= p; v += 1
    return v

def v_weight(n, k, l):
    return w3hat(n, k, l) - Hs(n, 3)

def check(p, amax=None):
    M = p**CAP
    worst = CAP + 1; ncell = 0; nfail = 0; skipped = 0
    for a in range(1, p if amax is None else min(p, amax + 1)):
        if int(Q(a)) % p == 0:
            skipped += 1; continue
        # level-a data
        Ta = {(b, c): comb(a + b, a) * comb(a, b)**2 * comb(a + c, a) * comb(a, c)**2
                      * comb(a + b + c, a) for b in range(a + 1) for c in range(a + 1)}
        dd = {}
        for b in range(a + 1):
            for c in range(a + 1):
                dd[(b, c)] = max(0, -vp(v_weight(a, b, c), p))
        for r in range(p):
            n = a * p + r
            if n > 360:
                continue
            ncell += 1
            c1 = [comb(n + i, n) % M for i in range(n + 1)]
            c2 = [comb(n, i) % M for i in range(n + 1)]
            c3 = [comb(n + i, n) % M for i in range(2 * n + 1)]
            tk = [c1[i] * c2[i] % M * c2[i] % M for i in range(n + 1)]
            # Lam = Q_n / Q_a  mod p^CAP
            Lam = int(Q(n)) % M * pow(int(Q(a)) % M, -1, M) % M
            worstcell = CAP + 1
            for b in range(a + 1):
                lo_k = b * p; hi_k = min(n, b * p + p - 1)
                for c in range(a + 1):
                    lo_l = c * p; hi_l = min(n, c * p + p - 1)
                    acc = 0
                    for k in range(lo_k, hi_k + 1):
                        tkk = tk[k]
                        if tkk == 0:
                            continue
                        s = 0
                        for l in range(lo_l, hi_l + 1):
                            s += tk[l] * c3[k + l] % M
                        acc += tkk * (s % M)
                    acc %= M
                    diff = (acc - Lam * Ta[(b, c)]) % M
                    slack = vp_mod(diff, p) - (1 + dd[(b, c)])
                    worstcell = min(worstcell, slack)
            worst = min(worst, worstcell)
            if worstcell < 0:
                nfail += 1
    return ncell, skipped, nfail, worst

if __name__ == '__main__':
    for p in [int(x) for x in sys.argv[1:]] or [5, 7, 11, 13]:
        ncell, sk, nf, w = check(p)
        print('p=%2d  cells=%4d  (skipped a with p|Q_a: %d)  FAILURES=%d  min slack=%d'
              % (p, ncell, sk, nf, w), flush=True)
