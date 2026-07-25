"""T3: the WEIGHT-2 residue identities (the weight-2 twins of Lemma Phi).

Level-n letters:  A_m(k)=H^(m)_{n+k}-H^(m)_k,  B_m(k)=H^(m)_{n-k}-H^(m)_k,
                  C_m = H^(m)_{n+k+l}-H^(m)_{k+l}.
Phi_b := A_1(k) + 2 B_1(k) + C_1     (Lemma Phi's form, level n, in the k-variable)

Claimed EXACT identities, for every n >= 0 and every fixed 0 <= l <= n:

 (P0)  sum_k T(n,k,l) * Phi_b                                    = 0     [Lemma Phi]
 (P1)  sum_k T(n,k,l) * [ Phi_b*A_1(k) - A_2(k) ]                = 0
 (P2)  sum_k T(n,k,l) * [ Phi_b*C_1     - C_2   ]                = 0
 (P3)  sum_k T(n,k,l) * [ Phi_b*B_1(k) - (Phi_b^2 - A_2(k) - C_2)/2 ] = 0
"""
import sys
from fractions import Fraction as F
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import Hs, T

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 12
bad = [0] * 4
tot = 0
for n in range(0, NMAX + 1):
    for l in range(0, n + 1):
        S = [F(0)] * 4
        for k in range(0, n + 1):
            A1 = Hs(n + k, 1) - Hs(k, 1)
            A2 = Hs(n + k, 2) - Hs(k, 2)
            B1 = Hs(n - k, 1) - Hs(k, 1)
            C1 = Hs(n + k + l, 1) - Hs(k + l, 1)
            C2 = Hs(n + k + l, 2) - Hs(k + l, 2)
            Ph = A1 + 2 * B1 + C1
            t = T(n, k, l)
            S[0] += t * Ph
            S[1] += t * (Ph * A1 - A2)
            S[2] += t * (Ph * C1 - C2)
            S[3] += t * (Ph * B1 - (Ph * Ph - A2 - C2) / 2)
        tot += 1
        for i in range(4):
            if S[i] != 0:
                bad[i] += 1
                if bad[i] < 4:
                    print('  FAIL P%d  n=%d l=%d  value=%s' % (i, n, l, S[i]))
print('n <= %d : %d (n,l) pairs;  failures P0=%d P1=%d P2=%d P3=%d'
      % (NMAX, tot, bad[0], bad[1], bad[2], bad[3]))
