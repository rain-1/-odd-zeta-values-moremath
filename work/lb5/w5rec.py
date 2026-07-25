"""Does  S_n := sum_{k,l} T(n,k,l) w5_allp(n,k,l)  satisfy L_BZ, far beyond the fit range?

The fit that produced w5_allp used levels up to N=600 but only 313 independent equations;
this is an independent forward check: evaluate S_n mod q from the explicit representative
and (i) test the order-3 BZ recurrence residual, (ii) search for the minimal recurrence.
"""
import sys, json, time
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from fit import Q1, Q2, row, lad_mod
from depthcond import basis
_argv=sys.argv; sys.argv=['guessrec','60']
from guessrec import guess
sys.argv=_argv

FN = sys.argv[1] if len(sys.argv) > 1 else 'w5_allp.json'
N = int(sys.argv[2]) if len(sys.argv) > 2 else 120
q = Q1

B = basis()
labels = [B.label(e) for e in B.els]
d = json.load(open(FN))
unknown = [k for k in d if k not in set(labels)]
print('%s: %d terms, %d unknown labels' % (FN, len(d), len(unknown)), flush=True)
x = np.zeros(len(B.els), dtype=np.int64)
for i, lab in enumerate(labels):
    if lab in d:
        num, den = d[lab]
        x[i] = num % q * pow(den % q, q - 2, q) % q

t0 = time.time()
S = []
for n in range(N + 1):
    S.append(int(row(n, q, B) @ x % q))
print('evaluated n=0..%d in %.0fs' % (N, time.time() - t0), flush=True)

# (i) compare with the exact ladder P_n where available, then the L_BZ residual
def a0(n): return 41218*n**3 + 198849*n**2 + 320790*n + 173057
def B8(n):
    return (3874492*n**8 + 59373972*n**7 + 394148190*n**6 + 1481084196*n**5
            + 3447878810*n**4 + 5095855458*n**3 + 4673546679*n**2
            + 2433871008*n + 551502039)
def B9(n):
    return (48802112*n**9 + 967468896*n**8 + 8488000862*n**7 + 43246197636*n**6
            + 140983768422*n**5 + 304912330849*n**4 + 437406946975*n**3
            + 401272692378*n**2 + 213593890911*n + 50257929339)

badlad = [n for n in range(min(N, 360) + 1) if S[n] != lad_mod('P', n, q)]
print('mismatches vs exact ladder P_n (mod q), n<=%d: %s' % (min(N, 360), badlad[:6]),
      '(count %d)' % len(badlad), flush=True)

bad = []
for n in range(N - 2):
    r = ((n+1)**5*(n+2)*a0(n+1)*S[n] - 2*(n+2)*B8(n)*S[n+1]
         - 2*B9(n)*S[n+2] + 2*(n+3)**5*(2*n+5)*a0(n)*S[n+3]) % q
    if r: bad.append(n)
print('L_BZ residual nonzero at n in %s  (count %d of %d)' % (bad[:6], len(bad), N-2), flush=True)

print('minimal recurrence guess:', guess(S), flush=True)
