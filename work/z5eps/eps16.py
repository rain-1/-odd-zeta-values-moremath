"""eps16.py -- EXACT rational verification of the epsilon-deformation, t = 1.

T_eps = T * exp( sum_m eps^m L_m ),  L_m as below (all coefficients exact Q).
Checks, all in exact Fraction arithmetic, n = 0..NEX:
  V1: L1 = -2 * d/dl log T   (per-letter identity)
  V2: [eps^1] Sigma = 0
  V3: [eps^2] Sigma = 0
  V4: [eps^3] Sigma = Phat_n
  V5: [eps^5] Sigma = (33/4) P_n
  V6: [eps^4] Sigma =: X_n  is NOT in span{Q,Phat,P}  (exact rank test)
  V7: e-totals:  e2tot = e4tot = 0,  e3tot = 3*1,  e5tot = 5*(33/4)
"""
import sys
from fractions import Fraction as F
from math import comb

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
import core

NEX = 16

# ---- deformation data at t = 1 (from eps15, CRT-checked at two primes) ----
ALPHA = (F(-3), F(1), F(2))                       # A1 on pairs (k,l),(n+k,n+l),(n-k,n-l)
AB = (F(-1), F(0))                                # S1 = -X (D1-direction)
G = [F(-4), F(1), F(-3), F(4), F(2), F(-2)]       # L2 sym classes
BETA = [F(-9), F(-5, 4), F(-4)]                   # L2 antisym
Y = [F(0), F(12), F(-5, 6), F(-32, 3), F(8, 3), F(-8, 3)]   # L3 sym
GAM = [F(-12), F(5, 6), F(32, 3)]                 # L3 antisym
Z = [F(0), F(0), F(0), F(0), F(4), F(-4)]         # L4 sym
DLT = [F(-68), F(31, 32), F(-64)]                 # L4 antisym
W = [F(0), F(528, 5), F(37, 40), F(-512, 5), F(32, 5), F(-32, 5)]  # L5 sym
T3_EXPECT = F(1)
T5_EXPECT = F(33, 4)

D1VEC = [F(0), F(-3), F(1), F(2), F(-2), F(2)]
V1VEC = [F(2), F(1), F(-2), F(-1), F(2), F(0)]

H = core.Hs
T = core.T


def letters(n, k, l):
    sym = [H(n, 1), 0, 0, 0, 0, 0]
    out = {}
    for r in range(1, 6):
        s = [H(n, r), H(k, r) + H(l, r), H(n + k, r) + H(n + l, r),
             H(n - k, r) + H(n - l, r), H(k + l, r), H(n + k + l, r)]
        a = [H(k, r) - H(l, r), H(n + k, r) - H(n + l, r),
             H(n - k, r) - H(n - l, r)]
        out[r] = (s, a)
    return out


def Lm(n, k, l):
    lt = letters(n, k, l)
    s1, a1 = lt[1]
    X = sum(D1VEC[c] * s1[c] for c in range(6))
    Yv = sum(V1VEC[c] * s1[c] for c in range(6))
    L1 = AB[0] * X + AB[1] * Yv + sum(ALPHA[j] * a1[j] for j in range(3))
    L2 = (sum(G[c] * lt[2][0][c] for c in range(6))
          + sum(BETA[j] * lt[2][1][j] for j in range(3)))
    L3 = (sum(Y[c] * lt[3][0][c] for c in range(6))
          + sum(GAM[j] * lt[3][1][j] for j in range(3)))
    L4 = (sum(Z[c] * lt[4][0][c] for c in range(6))
          + sum(DLT[j] * lt[4][1][j] for j in range(3)))
    L5 = sum(W[c] * lt[5][0][c] for c in range(6))
    return L1, L2, L3, L4, L5


def bell(L1, L2, L3, L4, L5):
    B1 = L1
    B2 = L2 + L1 * L1 / 2
    B3 = L3 + L1 * L2 + L1 ** 3 / 6
    B4 = L4 + L1 * L3 + L2 * L2 / 2 + L1 * L1 * L2 / 2 + L1 ** 4 / 24
    B5 = (L5 + L1 * L4 + L2 * L3 + L1 * L1 * L3 / 2 + L1 * L2 * L2 / 2
          + L1 ** 3 * L2 / 6 + L1 ** 5 / 120)
    return B1, B2, B3, B4, B5


# ---- V1: L1 = -2 d/dl log T ----
bad = 0
for n in range(0, 9):
    for k in range(n + 1):
        for l in range(n + 1):
            lt = letters(n, k, l)
            s1, a1 = lt[1]
            X = sum(D1VEC[c] * s1[c] for c in range(6))
            L1 = AB[0] * X + sum(ALPHA[j] * a1[j] for j in range(3))
            dl = (H(n + l, 1) + H(n + k + l, 1) + 2 * H(n - l, 1)
                  - 3 * H(l, 1) - H(k + l, 1))
            if L1 != -2 * dl:
                bad += 1
print('V1: L1 == -2 d_l log T  cells n<=8:', 'PASS' if bad == 0 else 'FAIL %d' % bad)

# ---- V2..V5 ----
S = {m: [] for m in range(1, 6)}
for n in range(NEX + 1):
    acc = [F(0)] * 5
    for k in range(n + 1):
        for l in range(n + 1):
            t = T(n, k, l)
            B = bell(*Lm(n, k, l))
            for m in range(5):
                acc[m] += t * B[m]
    for m in range(1, 6):
        S[m].append(acc[m - 1])
Qs = [core.Q(n) for n in range(NEX + 1)]
Phs = [core.Ph(n) for n in range(NEX + 1)]
Ps = [core.P(n) for n in range(NEX + 1)]
print('V2: [eps^1] = 0, n = 0..%d:' % NEX, 'PASS' if all(v == 0 for v in S[1]) else 'FAIL')
print('V3: [eps^2] = 0:', 'PASS' if all(v == 0 for v in S[2]) else 'FAIL')
print('V4: [eps^3] = Phat:', 'PASS' if all(S[3][n] == T3_EXPECT * Phs[n] for n in range(NEX + 1)) else 'FAIL')
print('V5: [eps^5] = (33/4) P:', 'PASS' if all(S[5][n] == T5_EXPECT * Ps[n] for n in range(NEX + 1)) else 'FAIL')

# ---- V6: X_n = [eps^4] not in span{Q, Phat, P} ----
X4 = S[4]
# solve on n = 0..2, then test
import itertools
found = False
# generic 3x3 solve
A = [[Qs[n], Phs[n], Ps[n]] for n in range(3)]
b = [X4[n] for n in range(3)]
# Cramer
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
D = det3(A)
if D != 0:
    cs = []
    for j in range(3):
        M = [row[:] for row in A]
        for i in range(3): M[i][j] = b[i]
        cs.append(det3(M) / D)
    resid = [X4[n] - (cs[0]*Qs[n] + cs[1]*Phs[n] + cs[2]*Ps[n]) for n in range(NEX + 1)]
    nz = sum(1 for v in resid if v != 0)
    print('V6: [eps^4] vs span{Q,Phat,P}: best-fit (%s, %s, %s); nonzero residuals at %d of %d n  -> %s'
          % (cs[0], cs[1], cs[2], nz, NEX + 1, 'NOT IN SPAN' if nz else 'IN SPAN ?!'))
print('    X_4 values n=0..4:', X4[:5])

# ---- V7: e-totals ----
mult = [1, 2, 2, 2, 1, 1]
e2t = -2 * sum(m * g for m, g in zip(mult, G))
e3t = 3 * sum(m * y for m, y in zip(mult, Y))
e4t = -4 * sum(m * z for m, z in zip(mult, Z))
e5t = 5 * sum(m * w for m, w in zip(mult, W))
print('V7: e2tot=%s e3tot=%s e4tot=%s e5tot=%s   (expect 0, 3, 0, 165/4 = 5*33/4)'
      % (e2t, e3t, e4t, e5t))
print('    => unnormalised: [eps^3] = -(1)*(Q zeta3 - Phat),  [eps^5] = -(33/4)*(Q zeta5 - P):',
      'FORCED' if (e3t == 3 * T3_EXPECT and e5t == 5 * T5_EXPECT and e2t == 0 and e4t == 0) else 'NO')
