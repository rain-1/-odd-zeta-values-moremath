"""M0 (P1e S5): is the weight-5 fitting system consistent when the support is
restricted to letter monomials of DEGREE <= D ?

Rationale (PHASE2_CERTS §15.2): the support of E(w)/T -- the rank of the d-finite
module that creative telescoping must close for (T1-top) -- grows like 2^d per
degree-d monomial and not at all with the weight.  w3hat's folded form has degree
<= 2 and support 6; every known w5 has degree 4-5 terms and support 184-220.
So the ONLY cheap experiment that can change (T1-top)'s cost class is:

    does [fit ; depth-conditions] stay CONSISTENT after deleting every column
    whose monomial has more than D letter factors?

Usage:
  python3 degfit.py MODE KSPEC CSPEC NSPEC N q [DLIST]
     MODE   base | vt2[:sel] | strong | exIII | exI          (rdepth.caps_for)
     KSPEC  AB | ABR | ABY | ABRY | comma-list
     CSPEC  C  | CD  | CV  | CDV   | comma-list
     NSPEC  N  | NZ  | comma-list
     DLIST  comma-separated degree caps, default 2,3,4,5

Prints, for each D: #columns kept, rank(fit|D), fit-alone consistency,
#condition rows, rank(joint|D), consistency, and the defect
rank[A|rhs] - rank[A]  (0 iff consistent).
"""
import sys, time, os
import numpy as np

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from rfit import (AB, KL, CL, DL, NL, YL, VL, ZL, build_basis, row, rref, lad_ext)
import rdepth

SH = {'AB': AB, 'ABR': KL, 'ABY': AB + YL, 'ABRY': KL + YL,
      'C': CL, 'CD': CL + DL, 'CV': CL + VL, 'CDV': CL + DL + VL,
      'N': NL, 'NZ': NL + ZL}

MODE = sys.argv[1]
kl = SH.get(sys.argv[2], sys.argv[2].split(','))
cl = SH.get(sys.argv[3], sys.argv[3].split(','))
nl = SH.get(sys.argv[4], sys.argv[4].split(','))
N = int(sys.argv[5])
q = int(sys.argv[6])
DLIST = [int(x) for x in (sys.argv[7].split(',') if len(sys.argv) > 7 else
                          ['2', '3', '4', '5'])]
useD = any(x[0] == 'D' for x in cl)
nested = any(x[0] in 'YVZ' for x in kl + cl + nl)

B = build_basis(kletters=kl, cletters=cl, nletters=nl, useD=useD, nested=nested)
NC = len(B)


def degree(e):
    i, j, ci, ni = e
    return (len(B.km[i][0]) + len(B.km[j][0])
            + len(B.cm[ci][0]) + len(B.nm[ni][0]))


degs = np.array([degree(e) for e in B.els])
hist = {d: int((degs == d).sum()) for d in sorted(set(degs.tolist()))}
print('MODE=%s  K=%s C=%s N=%s   basis %d cols   N=%d q=%d'
      % (MODE, sys.argv[2], sys.argv[3], sys.argv[4], NC, N, q), flush=True)
print('degree histogram: %s' % hist, flush=True)

# ---------------------------------------------------------------- design matrix
tag = 'DF_%s_%s_%s_%d_%d' % (sys.argv[2], sys.argv[3], sys.argv[4], N, q)
fn = '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/%s.npz' % tag
if os.path.exists(fn):
    z = np.load(fn, allow_pickle=True)
    M, b = z['M'], z['b']
    assert M.shape == (N, NC), 'cached matrix shape mismatch'
    print('loaded cached design matrix %s' % fn, flush=True)
else:
    t0 = time.time()
    Y = lad_ext('P', N + 1, q)
    M = np.zeros((N, NC), dtype=np.int64)
    b = np.zeros(N, dtype=np.int64)
    for i, n in enumerate(range(1, N + 1)):
        M[i] = row(n, q, B, useD=useD, nested=nested)
        b[i] = Y[n]
    np.savez_compressed(fn, M=M, b=b)
    print('built design matrix (%.1f s) -> %s' % (time.time() - t0, fn), flush=True)

caps = rdepth.caps_for(MODE, refine_eps=useD)

# ---------------------------------------------------------------- full system
allels = list(B.els)


def run(mask, tagd):
    B.els = [e for e, m in zip(allels, mask) if m]
    nc = len(B.els)
    if nc == 0:
        print('  D=%s : no columns' % tagd, flush=True)
        return
    Md = M[:, mask]
    t0 = time.time()
    C = [] if os.environ.get('NOCOND') else rdepth.condition_rows(B, caps)
    Cq = (np.array([[int(v) % q for v in r] for r in C], dtype=np.int64) if C
          else np.zeros((0, nc), np.int64))
    rM, _, incM, _ = rref(Md, b, q)
    A = np.concatenate([Md, Cq], axis=0)
    rhs = np.concatenate([b, np.zeros(len(Cq), np.int64)])
    rA, piv, inc, _ = rref(A, rhs, q)
    rAug, _, _, _ = rref(np.concatenate([A, rhs.reshape(-1, 1)], axis=1),
                         np.zeros(len(rhs), np.int64), q)
    print('  D<=%s : cols=%-5d rank(fit)=%-4d fitINCONS=%-5s condrows=%-4d '
          'rank(joint)=%-4d nullity=%-4d INCONSISTENT=%-5s defect=%d  (%.1f s)'
          % (tagd, nc, rM, incM, len(C), rA, nc - rA, inc, rAug - rA,
             time.time() - t0), flush=True)
    B.els = allels


for D in DLIST:
    run(degs <= D, D)
B.els = allels
