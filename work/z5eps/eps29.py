"""eps29.py -- extract the exact decomposition of sym(Delta5) over the
eps24..eps28 generator span (run only after eps28 reports IN SPAN).

Method: rref on [sym(gens)^T | sym(Delta5)] over F_p (p = 4194301), solve for
a pivot combination, rationally reconstruct each coefficient (Wang bound
sqrt(p/2) ~ 1448), then verify the monomial-ring identity EXACTLY over Q.
The exact check is the deliverable; the mod-p work is only a search.
"""

import sys, time, pickle
import numpy as np
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')

import eps28
from eps28 import (ALLF, ALLN, EMON, EIDX, NEM, ESIG, vec_modp,
                   build_rows_ext, mon_sigma)
from eps22 import DELTA5


def ratrec(a, p, bound):
    """Wang rational reconstruction of a mod p."""
    if a == 0:
        return F(0)
    r0, r1 = p, a % p
    s0, s1 = 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if abs(s1) > bound or r1 == 0 and s1 == 0:
        return None
    if s1 < 0:
        r1, s1 = -r1, -s1
    from math import gcd
    if gcd(r1, s1) != 1:
        return None
    return F(r1, s1)


def sigma_form(f):
    return {mon_sigma(m): c for m, c in f.items()}


def sym_form(f):
    out = {}
    for src, half in ((f, F(1, 2)), (sigma_form(f), F(1, 2))):
        for m, c in src.items():
            out[m] = out.get(m, F(0)) + half * c
            if out[m] == 0:
                del out[m]
    return out


if __name__ == '__main__':
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 4194301
    t0 = time.time()
    rows, _ = build_rows_ext(p, 30)
    V = np.zeros((len(ALLF), NEM), dtype=np.int64)
    for i, f in enumerate(ALLF):
        V[i] = vec_modp(f, p)
    bad = set()
    for lo in range(0, len(ALLF), 64):
        hi = min(lo + 64, len(ALLF))
        vals = rows.dot(V[lo:hi].T) % p
        for j in range(hi - lo):
            if vals[:, j].any():
                bad.add(lo + j)
    print('calibration failures:', len(bad))
    keep = [i for i in range(len(ALLF)) if i not in bad]
    inv2 = pow(2, p - 2, p)
    G = V[keep]
    Gs = (G + G[:, ESIG]) * inv2 % p

    tgt = np.zeros(NEM, dtype=np.int64)
    for m, c in DELTA5.items():
        tgt[EIDX[m]] = (c.numerator % p
                        * pow(c.denominator % p, p - 2, p)) % p
    tgt = (tgt + tgt[ESIG]) * inv2 % p

    # rref on the transpose [Gs^T | tgt]
    A = np.vstack([Gs, tgt[None, :]]).T % p     # NEM x (ng+1)
    m, nc = A.shape
    r, piv = 0, []
    t1 = time.time()
    for c in range(nc - 1):
        nz = np.nonzero(A[r:, c] % p)[0]
        if not len(nz):
            continue
        pr = r + nz[0]
        if pr != r:
            A[[r, pr]] = A[[pr, r]]
        A[r] = A[r] * pow(int(A[r, c]), p - 2, p) % p
        col = A[:, c].copy(); col[r] = 0
        nzr = np.nonzero(col)[0]
        if len(nzr):
            A[nzr] = (A[nzr] - col[nzr, None] * A[r][None, :]) % p
        piv.append(c)
        r += 1
        if r % 100 == 0:
            print('  pivots:', r, '%.0fs' % (time.time() - t1), flush=True)
    ok = not A[r:, -1].any()
    print('solve consistent:', ok, ' rank:', r, '%.0fs' % (time.time() - t1))
    if not ok:
        sys.exit('target NOT in span at this prime -- abort')

    x = np.zeros(nc - 1, dtype=np.int64)
    for i, c in enumerate(piv):
        x[c] = A[i, -1] % p
    chk = np.zeros(NEM, dtype=np.int64)
    for c in np.nonzero(x)[0]:
        chk = (chk + x[c] * Gs[c]) % p
    print('mod-p residual max:', int(((chk - tgt) % p).max()))

    knames = [ALLN[i] for i in keep]
    nz = [(int(c), knames[c], int(x[c])) for c in np.nonzero(x)[0]]
    print('nonzero coefficients:', len(nz))

    bound = int((p // 2) ** 0.5)
    coeffs = {}
    fails = []
    for c, nm, v in nz:
        rr = ratrec(v, p, bound)
        if rr is None:
            fails.append((nm, v))
        else:
            coeffs[c] = rr
    print('reconstruction failures:', len(fails))
    for nm, v in fails[:10]:
        print('   FAIL', nm, v)
    if fails:
        sys.exit('need two-prime CRT -- abort')

    # ---------- EXACT verification over Q ----------
    print('exact verification over Q ...', flush=True)
    acc = {}
    for c, q in coeffs.items():
        for mmm, cc in sym_form(ALLF[keep[c]]).items():
            acc[mmm] = acc.get(mmm, F(0)) + q * cc
            if acc[mmm] == 0:
                del acc[mmm]
    tgt_exact = sym_form(dict(DELTA5))
    diff = dict(tgt_exact)
    for mmm, cc in acc.items():
        diff[mmm] = diff.get(mmm, F(0)) - cc
        if diff[mmm] == 0:
            del diff[mmm]
    print('EXACT IDENTITY:', 'PASS -- 0 mismatches' if not diff
          else 'FAIL -- %d mismatching monomials' % len(diff))
    if diff:
        for mmm in list(diff)[:10]:
            print('  ', mmm, diff[mmm])
    out = {'coeffs': {ALLN[keep[c]]: (q.numerator, q.denominator)
                      for c, q in coeffs.items()},
           'prime': p, 'exact_pass': not diff}
    with open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/'
              'eps29_combo.pkl', 'wb') as fh:
        pickle.dump(out, fh)
    print('saved eps29_combo.pkl  (%.0fs total)' % (time.time() - t0))
