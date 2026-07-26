"""The subset analysis on the k<->l SYMMETRIC subspace.

W_tel, K5 and the affine set {w : A5 w = b5} are all sigma-stable (T(n,k,l) =
T(n,l,k), the certificate system is sigma-equivariant with rho <-> sigma), so a
non-empty intersection contains a symmetric point: searching Sym is WLOG.
[PROVED]  This halves the width (697 orbits of 1270 monomials) and is what makes
the >= 1.3 rows/columns discipline affordable for every subset verdict.
"""
import sys, pickle, itertools, os
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5w5')
import fastlin, ratrec, solve
import w5span as W
import pd5, scan5, affine

p = int(sys.argv[1]) if len(sys.argv) > 1 else pd5.P1
dname = sys.argv[2] if len(sys.argv) > 2 else 'H1'
slack = int(sys.argv[3]) if len(sys.argv) > 3 else 10
nlist = [int(x) for x in sys.argv[4].split(',')] if len(sys.argv) > 4 else [13, 17]
suf = sys.argv[5] if len(sys.argv) > 5 else ''
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
idx = {m: j for j, m in enumerate(B)}
orbits = []
seen = set()
for m in B:
    if m in seen: continue
    sm = W.sigma_mono(m)
    seen.add(m); seen.add(sm)
    orbits.append((idx[m],) if sm == m else (idx[m], idx[sm]))
S = np.zeros((J, len(orbits)), dtype=np.int64)
for t, o in enumerate(orbits):
    for j in o: S[j, t] = 1
print('J = %d ; sigma-orbits (dim Sym) = %d' % (J, len(orbits)))
A5 = np.load('A5%s_p%d.npy' % (suf, p)); b5 = np.load('b5%s_p%d.npy' % (suf, p))
AS = affine.mmod(A5, S, p)
print('A5 rows = %d ; rank(A5.S) = %d' % (AS.shape[0], fastlin.rank_only(AS, p)[0]))
w5 = np.load('w5vec%s_p%d.npy' % (suf, p))
typ = {}
for j in byblock:
    typ.setdefault(tuple(sorted(W.LWT[L] for L in B[j])), []).append(j)
keys = sorted(typ)
res = {}
print('%-40s %6s %7s %6s %6s %6s' % ('subset (symmetric subspace)', 'dimW', 'rows/W', 'rkA5W', 'nbad', 'verdict'))
for rsz in range(1, len(keys) + 1):
    for combo in itertools.combinations(keys, rsz):
        if any(res.get(tuple(c), 0) > 0 for c in itertools.combinations(combo, rsz - 1)) and rsz > 1:
            res[combo] = 1; continue          # supersets of a NO are NO
        rows = [x for k in combo for j in typ[k] for x in byblock[j]]
        C = affine.mmod(np.array(rows, dtype=np.int64) % p, S, p)
        ns = ratrec.nullspace(C, p)
        Wb = np.array(ns, dtype=np.int64) % p
        if Wb.shape[0] == 0:
            print('   %-37s dim W = 0' % '+'.join(map(str, combo))); res[combo] = 1; continue
        Mt = affine.mmod(AS, Wb.T, p)
        x, rank, pv, nbad = fastlin.solve(Mt, b5 % p, p)
        res[combo] = nbad
        mini = nbad > 0 and all(res.get(tuple(c), 0) == 0 for c in itertools.combinations(combo, rsz - 1))
        print('   %-37s %6d %7.2f %6d %6d %6s%s'
              % ('+'.join(map(str, combo)), Wb.shape[0], AS.shape[0] / max(Wb.shape[0], 1),
                 rank, nbad, 'NO' if nbad else 'YES',
                 '  <-- MINIMAL EXCLUDER' if mini else ''))
