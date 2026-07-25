"""Driver: fit  Y_n = sum_{k,l} T(n,k,l) w(n,k,l)  in a specified basis."""
import sys, time, json
import numpy as np
from fit import *

def build_basis(W, depth2, maxfac_k, maxfac_c, maxfac_n, maxr=5,
                kletters=None, cletters=None, nletters=None, raw=False):
    """Build the Basis object from name->weight dicts (weights taken from a probe n)."""
    Lk, Lc, Ln = alphabet(6, Q1, depth2=depth2, maxr=maxr, raw=raw)
    wk = {k: v[0] for k, v in Lk.items()}
    wc = {k: v[0] for k, v in Lc.items()}
    wn = {k: v[0] for k, v in Ln.items()}
    if kletters is not None: wk = {k: v for k, v in wk.items() if k in kletters}
    if cletters is not None: wc = {k: v for k, v in wc.items() if k in cletters}
    if nletters is not None: wn = {k: v for k, v in wn.items() if k in nletters}
    km = monos(wk, W, maxfac_k)
    cm = monos(wc, W, maxfac_c)
    nm = monos(wn, W, maxfac_n)
    return Basis(km, cm, nm, W)

def run(target, basis, nfit, nval, q=Q1, depth2=True, maxr=5, verbose=True):
    t0 = time.time()
    M = np.zeros((len(nfit), len(basis)), dtype=np.int64)
    b = np.zeros(len(nfit), dtype=np.int64)
    for i, n in enumerate(nfit):
        M[i] = row(n, q, basis, depth2=depth2, maxr=maxr)
        b[i] = lad_mod(target, n, q)
    if verbose:
        print('  design matrix %dx%d built in %.1fs' % (M.shape[0], M.shape[1], time.time()-t0), flush=True)
    x, r, piv = solve_particular(M, b, q)
    if x is None:
        print('  INCONSISTENT: rank(M)=%d, #eqs=%d, #unk=%d' % (r, len(nfit), len(basis)))
        return None
    print('  consistent: rank=%d, #eqs=%d, #unk=%d, nullity=%d' % (r, len(nfit), len(basis), len(basis)-r))
    ok = True
    for n in nval:
        v = int(row(n, q, basis, depth2=depth2, maxr=maxr) @ x % q)
        if v != lad_mod(target, n, q):
            print('  VALIDATION FAIL at n=%d' % n); ok = False; break
    if ok:
        print('  VALIDATION PASSED on %d held-out levels %s' % (len(nval), (nval[0], nval[-1])))
    return x, r, piv, ok
