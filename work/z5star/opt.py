"""JOB 1 -- choose the member of the 12-dimensional affine family.

Loads famlam_p<P>.pkl (the cumulative lam-space from fam.py), rationalises the
affine family over Q, and then answers, in order:

  (Q1) is the family sigma-stable?                       (structure)
  (Q2) is there a member w' with w' - what3 PURELY ANTISYMMETRIC?
       -> if yes the Lean equivalence lemma is one Finset.sum_comm.
  (Q3) what is the minimum of  N_hard = 1 + #{h1_*,h2_* letters}  and of
       J = 1 + #letters + #deg2  over the family, subject to the interior-pole
       constraint (P-int) below?
  (Q4) the smallest symmetric defect: how many symmetric generators of K does
       Lean actually have to prove?

(P-int) INTERIOR-POLE CONSTRAINT (new here, see Z5STAR_CERT 2.4).  Phi's k-step
carries (n+3-k)^2 and P_i carries [prod_{j>i}(n+j-k)]^2, so a letter
H^(r)_{n+3-k} contributes a pole 1/(n+3-k)^r that is only cancelled for r <= 2,
and a MONOMIAL may contribute the sum of its letters' orders.  Hence
   h3_mk, h3_ml, h1_mk*h2_mk, h1_ml*h2_ml   are FORBIDDEN in the support:
they leave an uncancelled pole at k = n+3 (resp. l = n+3), which is an INTERIOR
point of range (n+4) -- exactly the failure mode LEAN_Z5_SCAFFOLD 5.2 describes
for the naive base T(n,k,l).
"""
import sys, os, pickle, itertools
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import wtools as W
import bare

HERE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'

FORBIDDEN = [('h3_mk',), ('h3_ml',),
             tuple(sorted(('h1_mk', 'h2_mk'))), tuple(sorted(('h1_ml', 'h2_ml')))]
FORB_IDX = [W.IDX[m] for m in FORBIDDEN]


def load_family(p=W.P1):
    d = pickle.load(open(os.path.join(HERE, 'famlam_p%d.pkl' % p), 'rb'))
    lam = [np.array(v, dtype=np.int64) % p for v in d['lam']]
    ws = [np.array(v, dtype=np.int64) % p for v in d['ws']]
    nw = len(ws)
    # split lam-space into  lam_0 != 0 (a representative) and lam_0 = 0 (tangent)
    good = [v for v in lam if v[0] % p]
    assert good, 'no representative in the lam-space'
    v0 = good[0]
    iv = pow(int(v0[0]) % p, p - 2, p)
    base = np.zeros(W.J109, dtype=np.int64)
    for a in range(nw):
        base = (base + int(v0[a]) * iv % p * ws[a]) % p
    # tangent: lam with lam_0 = 0
    import solve
    M = np.array(lam, dtype=np.int64) % p
    # reduce so that at most one row has lam_0 != 0
    R, piv, _ = solve.rref(M.copy(), p)
    R = R[:len(piv)]
    tan_lam = [R[i] for i in range(len(piv)) if R[i][0] % p == 0]
    U = []
    for v in tan_lam:
        u = np.zeros(W.J109, dtype=np.int64)
        for a in range(nw):
            u = (u + int(v[a]) % p * ws[a]) % p
        U.append(u)
    return base, U, ws, lam


def rationalise(base, U, p):
    bQ = W.to_Q(base, p)
    assert bQ is not None, 'base did not rationalise'
    UQ = []
    for u in U:
        q = W.to_Q(u, p)
        assert q is not None, 'tangent vector did not rationalise'
        UQ.append(q)
    return bQ, UQ


def affine_solve(bQ, UQ, targets):
    """find lam with  bQ + sum lam_i UQ_i  agreeing with `targets`:
    targets = list of (coordinate j, required value).  Returns (w, ok)."""
    A = [[UQ[i][j] for i in range(len(UQ))] for j, _ in targets]
    rhs = [Fr(val) - Fr(bQ[j]) for j, val in targets]
    x, ok = W.solveQ(A, rhs) if A else ([], True)
    if not ok:
        return None, False
    w = list(bQ)
    for i, c in enumerate(x):
        if c:
            w = [w[t] + c * UQ[i][t] for t in range(W.J109)]
    # verify
    for j, val in targets:
        if w[j] != Fr(val):
            return None, False
    return w, True


def zero_set(bQ, UQ, S):
    """member of the family with w[j] = 0 for every j in S, or None"""
    return affine_solve(bQ, UQ, [(j, 0) for j in S])


def main():
    p = W.P1
    base, U, ws, lam = load_family(p)
    print('lam-space dim %d ; tangent dim %d' % (len(lam), len(U)))
    bQ, UQ = rationalise(base, U, p)
    print('rationalised.  base:', end=' ')
    W.show(bQ, 'base')
    # ---- sanity: base is a representative, U in K
    W.check_rep(bQ, 14)
    for i, u in enumerate(UQ):
        ok = W.check_kernel(u, 10, verbose=False)
        if not ok:
            print('   *** tangent %d NOT in K' % i)
    print('   all %d tangent directions in K (exact Q, n=0..10): OK' % len(UQ))
    pickle.dump(dict(base=bQ, U=UQ), open(os.path.join(HERE, 'familyQ.pkl'), 'wb'))
    return bQ, UQ


if __name__ == '__main__':
    main()
