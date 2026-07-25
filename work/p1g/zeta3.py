"""P1g CONTROL: run the *identical* experiment on Apery's zeta(3) case, where the
answer is known (the classical weight IS cell-wise integral).

  T_A(n,k) = C(n,k)^2 C(n+k,k)^2 ,   a_n = sum_k T_A(n,k) c(n,k) ,
  c(n,k)   = H^(3)_n + (1/2) R^(3)(n,k) ,   R^(3) the Apery-type letter.

Fit  a_n = sum_k T_A(n,k) w3(n,k)  with w3 a Q-combination of weight-3 monomials in
  {A_r(k), B_r(k)} x {N_r}                (harmonic alphabet)
  {A_r(k), B_r(k), R_r(k)} x {N_r}        (R-extended alphabet)
and impose the CELL-WISE integrality conditions d3 <= v_p T_A = 2*alpha.

Usage: python3 zeta3.py KSPEC N q
"""
import sys
import numpy as np
from fractions import Fraction as F
from collections import defaultdict
from math import comb

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from rfit import rref
from rlet import R_tab

KSPEC = sys.argv[1].split(',') if len(sys.argv) > 1 else ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']
N = int(sys.argv[2]) if len(sys.argv) > 2 else 300
q = int(sys.argv[3]) if len(sys.argv) > 3 else 33554393
NLET = ['N1', 'N2', 'N3']
W = 3


def monos(letters, wmax, maxfac):
    wt = {a: int(a[1]) for a in letters}
    names = sorted(wt)
    res = {(): 0}
    cur = [((), 0)]
    for _ in range(maxfac):
        nxt = []
        for mono, w in cur:
            start = names.index(mono[-1]) if mono else 0
            for i in range(start, len(names)):
                if w + wt[names[i]] <= wmax:
                    nm = mono + (names[i],)
                    if nm not in res:
                        res[nm] = w + wt[names[i]]
                        nxt.append((nm, w + wt[names[i]]))
        cur = nxt
    return res


KM = sorted(monos(KSPEC, W, W).items())
NM = sorted(monos(NLET, W, W).items())
ELS = [(i, j) for i, (_, wk) in enumerate(KM) for j, (_, wn) in enumerate(NM)
       if wk + wn == W]
print('K=%s  basis %d cols (%d k-monomials)' % (sys.argv[1], len(ELS), len(KM)), flush=True)


def label(e):
    i, j = e
    return '%s x %s' % ('*'.join(KM[i][0]) or '1', '*'.join(NM[j][0]) or '1')


# ------------------------------------------------------------------ design matrix
def htab(M, q):
    H = {r: np.zeros(M + 1, dtype=np.int64) for r in (1, 2, 3)}
    for r in (1, 2, 3):
        acc = 0
        for m in range(1, M + 1):
            acc = (acc + pow(pow(m, q - 2, q), r, q)) % q
            H[r][m] = acc
    return H


def rowvals(n, q):
    H = htab(2 * n + 1, q)
    k = np.arange(n + 1)
    L = {}
    for r in (1, 2, 3):
        L['A%d' % r] = (H[r][n + k] - H[r][k]) % q
        L['B%d' % r] = (H[r][n - k] - H[r][k]) % q
    Rt = R_tab(n, q, 3)
    for r in (1, 2, 3):
        L['R%d' % r] = Rt[r] % q
    Ln = {'N%d' % r: int(H[r][n]) for r in (1, 2, 3)}
    cnk = np.array([comb(n, i) % q for i in range(n + 1)], dtype=np.int64)
    cpk = np.array([comb(n + i, i) % q for i in range(n + 1)], dtype=np.int64)
    TA = cnk * cnk % q * cpk % q * cpk % q
    out = np.zeros(len(ELS), dtype=np.int64)
    for e, (i, j) in enumerate(ELS):
        v = TA.copy()
        for nm in KM[i][0]:
            v = v * L[nm] % q
        s = 1
        for nm in NM[j][0]:
            s = s * Ln[nm] % q
        out[e] = int(v.sum() % q) * s % q
    # target a_n = sum_k T_A (H3_n + R3/2)
    half = pow(2, q - 2, q)
    tgt = int((TA * ((int(H[3][n]) + Rt[3] % q * half) % q) % q).sum() % q)
    return out, tgt


M = np.zeros((N, len(ELS)), dtype=np.int64)
b = np.zeros(N, dtype=np.int64)
for i, n in enumerate(range(1, N + 1)):
    M[i], b[i] = rowvals(n, q)

# ------------------------------------------------------------------ depth conditions
# alpha = 1 pattern: A_r -> u^r + Zp ; R_r -> rho_r u + Zp ; B_r, N_r -> Zp.  cap = 2.
ONE = {(0, ()): F(1)}


def pmul(P, Q):
    R = defaultdict(F)
    for (u1, s1), c1 in P.items():
        for (u2, s2), c2 in Q.items():
            R[(u1 + u2, tuple(sorted(s1 + s2)))] += c1 * c2
    return {kk: v for kk, v in R.items() if v}


def letter(nm):
    t, r = nm[0], int(nm[1])
    if t == 'A':
        return {(0, (('a', r),)): F(1), (r, ()): F(1)}
    if t == 'B':
        return {(0, (('b', r),)): F(1)}
    if t == 'R':
        return {(0, (('R', r),)): F(1), (1, (('rho', r),)): F(1)}
    if t == 'N':
        return {(0, (('n', r),)): F(1)}
    raise ValueError(nm)


CAP = 2
rows = defaultdict(lambda: [F(0)] * len(ELS))
for e, (i, j) in enumerate(ELS):
    P = ONE
    for nm in KM[i][0]:
        P = pmul(P, letter(nm))
    for nm in NM[j][0]:
        P = pmul(P, letter(nm))
    for (u, sym), v in P.items():
        if u > CAP:
            rows[(u, sym)][e] += v
C = []
for kk, vec in rows.items():
    if any(vec):
        den = 1
        for v in vec:
            den = den * v.denominator // np.gcd(den, v.denominator)
        C.append([int(v * den) % q for v in vec])
Cq = np.array(C, dtype=np.int64) if C else np.zeros((0, len(ELS)), np.int64)
print('condition rows: %d' % len(C), flush=True)

rM, _, incM, _ = rref(M, b, q)
rC, _, _, _ = rref(Cq, np.zeros(len(Cq), np.int64), q)
A = np.concatenate([M, Cq], axis=0)
rhs = np.concatenate([b, np.zeros(len(Cq), np.int64)])
rA, piv, inc, R = rref(A, rhs, q)
rAug, _, _, _ = rref(np.concatenate([A, rhs.reshape(-1, 1)], axis=1),
                     np.zeros(len(rhs), np.int64), q)
print('rank(fit)=%d rank(cond)=%d rank(joint)=%d nullity=%d INCONSISTENT=%s DEFECT=%d'
      % (rM, rC, rA, len(ELS) - rA, inc, rAug - rA), flush=True)
if not inc:
    x = np.zeros(len(ELS), dtype=np.int64)
    for i, c in enumerate(piv):
        x[c] = R[i, -1] % q
    nzl = [label(ELS[c]) for c in range(len(ELS)) if x[c]]
    print('  a solution exists; %d nonzero coords, e.g. %s' % (len(nzl), nzl[:8]), flush=True)
