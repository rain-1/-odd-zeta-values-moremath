"""Which COMBINATION of standalone-block families is the minimal excluder?
Caches the per-block conditions (intersected over several n) and then runs the
affine representative test on every subset of the five block families."""
import sys, pickle, itertools, os
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5w5')
import fastlin, ratrec
import w5span as W
import pd5, scan5, affine

p = int(sys.argv[1]) if len(sys.argv) > 1 else pd5.P1
dname = sys.argv[2] if len(sys.argv) > 2 else 'H1'
slack = int(sys.argv[3]) if len(sys.argv) > 3 else 10
nlist = [int(x) for x in sys.argv[4].split(',')] if len(sys.argv) > 4 else [13, 17]
cache = 'cond_%s_s%d_p%d_%s.pkl' % (dname, slack, p, '-'.join(map(str, nlist)))
if os.path.exists(cache):
    byblock, B = pickle.load(open(cache, 'rb'))
else:
    byblock = {}; B = None
    for n in nlist:
        r = scan5.run(n, dname, slack, p=p, verbose=True)
        B = r['B']
        for j, rows in r['byblock'].items():
            byblock.setdefault(j, []).extend(rows)
    pickle.dump((byblock, B), open(cache, 'wb'))
J = len(B)
A5 = np.load('A5_p%d.npy' % p); b5 = np.load('b5_p%d.npy' % p)
print('A5 rows = %d ; J = %d ; blocks = %d' % (A5.shape[0], J, len(byblock)))
typ = {}
for j in byblock:
    typ.setdefault(tuple(sorted(W.LWT[L] for L in B[j])), []).append(j)
keys = sorted(typ)
print('families:', {str(k): len(v) for k, v in typ.items()})
res = {}
for rsz in range(1, len(keys) + 1):
    for combo in itertools.combinations(keys, rsz):
        rows = [x for k in combo for j in typ[k] for x in byblock[j]]
        C = np.array(rows, dtype=np.int64) % p
        ns = ratrec.nullspace(C, p)
        Wb = np.array(ns, dtype=np.int64) % p
        if Wb.shape[0] == 0:
            print('   %-34s dim W = 0' % '+'.join(str(k) for k in combo)); continue
        Mt = affine.mmod(A5, Wb.T, p)
        x, rank, pv, nbad = fastlin.solve(Mt, b5 % p, p)
        tag = '+'.join(str(k) for k in combo)
        res[combo] = nbad
        # minimal excluder?
        mini = nbad > 0 and all(res.get(tuple(c), 0) == 0
                                for c in itertools.combinations(combo, rsz - 1))
        print('   %-40s dim W = %-5d rank A5(W) = %-4d nbad = %-4d %s%s'
              % (tag, Wb.shape[0], rank, nbad, 'NO ' if nbad else 'YES',
                 '  <-- MINIMAL EXCLUDING SUBSET' if mini else ''))
