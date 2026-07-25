"""T3 driver: the weight-5 decomposition hunt.

Usage:  python3 hunt.py <tag> <N> <depth2:0|1> <maxfac_k> <maxfac_c> <maxfac_n> [target]
Writes  hunt_<tag>.json  with rank / consistency / validation results.
"""
import sys, time, json
import numpy as np
from fit import *
from run_fit import build_basis

def main():
    tag = sys.argv[1]; N = int(sys.argv[2]); d2 = bool(int(sys.argv[3]))
    mfk, mfc, mfn = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    target = sys.argv[7] if len(sys.argv) > 7 else 'P'
    W = int(sys.argv[8]) if len(sys.argv) > 8 else 5
    raw = bool(int(sys.argv[9])) if len(sys.argv) > 9 else False
    kl = ['A%d' % r for r in range(1, 6)] + ['B%d' % r for r in range(1, 6)]
    cl = ['C%d' % r for r in range(1, 6)]
    nl = ['N%d' % r for r in range(1, 6)] + ['M%d' % r for r in range(1, 6)]
    z = ['%d%d' % (a, b) for a in range(1, 5) for b in range(1, 5) if 3 <= a + b <= 5]
    if d2:
        kl += ['ZA' + s for s in z] + ['ZB' + s for s in z] + ['YA' + s for s in z]
        cl += ['ZC' + s for s in z] + ['YC' + s for s in z]
        nl += ['ZN' + s for s in z] + ['ZM' + s for s in z]
    if raw:
        kl += ['R%d' % r for r in range(1, 6)]
        cl += ['RC%d' % r for r in range(1, 6)]
        if d2:
            kl += ['ZR' + s for s in z]
            cl += ['ZRC' + s for s in z]
    B = build_basis(W, d2, mfk, mfc, mfn, maxr=5, kletters=kl, cletters=cl,
                    nletters=nl, raw=raw)
    print('[%s] basis=%d  |Sk|=%d |Sc|=%d |Sn|=%d  N=%d' %
          (tag, len(B), len(B.km), len(B.cm), len(B.nm), N), flush=True)
    Y = lad_ext(target, N + 1, Q1)
    t0 = time.time()
    M = np.zeros((N, len(B)), dtype=np.int64); b = np.zeros(N, dtype=np.int64)
    for i, n in enumerate(range(1, N + 1)):
        M[i] = row(n, Q1, B, depth2=d2, maxr=5, raw=raw); b[i] = Y[n]
        if n % 100 == 0:
            print('   n=%d  %.0fs' % (n, time.time() - t0), flush=True)
    print('[%s] matrix %dx%d in %.0fs' % (tag, N, len(B), time.time() - t0), flush=True)
    np.save('M_%s.npy' % tag, M); np.save('b_%s.npy' % tag, b)
    res = {'tag': tag, 'basis': len(B), 'N': N, 'depth2': d2,
           'mf': [mfk, mfc, mfn], 'target': target, 'W': W, 'raw': raw}
    r, piv, inc, A = rref(M, b, Q1)
    rM, _, _, _ = rref(M, np.zeros(N, dtype=np.int64), Q1)
    res['rank_aug'] = r; res['rank_M'] = rM; res['inconsistent'] = inc
    res['excess_equations'] = N - rM
    print('[%s] rank(M)=%d  rank([M|b])=%d  INCONSISTENT=%s  excess=%d' %
          (tag, rM, r, inc, N - rM), flush=True)
    if not inc and N - rM > 0:
        # genuine positive: record a particular solution
        x = np.zeros(M.shape[1], dtype=np.int64)
        for i, c in enumerate(piv):
            x[c] = A[i, -1] % q0 if False else A[i, -1] % Q1
        np.save('x_%s.npy' % tag, x)
        res['solution_saved'] = True
        res['labels'] = [B.label(e) for e in B.els]
    json.dump(res, open('hunt_%s.json' % tag, 'w'), indent=1)
    print('[%s] written' % tag, flush=True)

if __name__ == '__main__':
    main()
