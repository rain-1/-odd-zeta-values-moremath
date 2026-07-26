"""Which standalone blocks are responsible for the weight-5 exclusion?

Rebuilds the per-block conditions at several n, intersects them over n, and then
runs the affine representative test  { w : conditions, A5 w = b5 }  for
increasing subsets of the blocks.  Reports the smallest subset that already
excludes, and the size of the violation.
"""
import sys, pickle, time
from collections import Counter
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5w5')
import solve, fastlin, ratrec
import w5span as W
import pd5, scan5, affine


def afftest(rows, J, p, A5, b5, label):
    C = np.array(rows, dtype=np.int64) % p if rows else np.zeros((0, J), np.int64)
    ns = ratrec.nullspace(C, p) if C.shape[0] else [np.eye(J, np.int64)[i] for i in range(J)]
    Wb = np.array(ns, dtype=np.int64) % p
    if Wb.shape[0] == 0:
        print('   %-42s dim W = 0' % label); return
    Mt = affine.mmod(A5, Wb.T, p)
    x, rank, pv, nbad = fastlin.solve(Mt, b5 % p, p)
    kd = Wb.shape[0] - rank
    print('   %-42s dim W = %-5d  dim A5(W) = %-4d  dim(W&K5) = %-4d  nbad = %-4d  %s'
          % (label, Wb.shape[0], rank, kd, nbad, 'YES' if nbad == 0 else 'NO'))
    return nbad


if __name__ == '__main__':
    p = int(sys.argv[1]) if len(sys.argv) > 1 else pd5.P1
    dname = sys.argv[2] if len(sys.argv) > 2 else 'H1'
    slack = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    nlist = [int(x) for x in sys.argv[4].split(',')] if len(sys.argv) > 4 else [13, 17]
    A5 = np.load('A5_p%d.npy' % p); b5 = np.load('b5_p%d.npy' % p)
    w5 = np.load('w5vec_p%d.npy' % p)
    byblock = {}
    B = None
    for n in nlist:
        r = scan5.run(n, dname, slack, p=p, verbose=True)
        B = r['B']; J = r['J']; us = r['us']
        for j, rows in r['byblock'].items():
            byblock.setdefault(j, []).extend(rows)
    print('\nA5: %d rows ; rank(A5) = %d' % (A5.shape[0], fastlin.rank_only(A5, p)[0]))
    # types
    typ = {}
    for j in byblock:
        typ.setdefault(tuple(sorted(W.LWT[L] for L in B[j])), []).append(j)
    print('\n--- affine representative test, by block subset ---')
    allrows = []
    for key, js in sorted(typ.items()):
        rows = [x for j in js for x in byblock[j]]
        allrows += rows
        afftest(rows, J, p, A5, b5, 'type %s only (%d blocks)' % (str(key), len(js)))
    # h4 blocks alone -- the RIGOROUSLY gauge-complete subfamily
    h4 = [j for j in byblock if len(B[j]) == 1]
    afftest([x for j in h4 for x in byblock[j]], J, p, A5, b5,
            'h4_* only (%d blocks, gauge-complete)' % len(h4))
    afftest(allrows, J, p, A5, b5, 'ALL %d standalone blocks' % len(byblock))
    # is w5 itself admissible per block?
    bad = 0
    for j, rows in byblock.items():
        for row in rows:
            if int((row.astype(object) @ w5.astype(object)) % p):
                bad += 1; break
    print('\n   blocks that REJECT w5 itself: %d of %d' % (bad, len(byblock)))
