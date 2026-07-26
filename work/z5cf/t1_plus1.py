"""T1: the degree-1 bare span misses P-hat by exactly one dimension.
Search: degree-1 span + ONE extra weight-3 monomial (degree 2 or 3). Exhaustive."""
import sys, os, numpy as np, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from design import build, monomials, sym_orbits, monname
from bare import Q1, Q2, lad_mod

W = int(sys.argv[1]) if len(sys.argv) > 1 else 3
KEY = sys.argv[2] if len(sys.argv) > 2 else 'Ph'
N = int(sys.argv[3]) if len(sys.argv) > 3 else 40
NEXTRA = int(sys.argv[4]) if len(sys.argv) > 4 else 1
q = Q1

t0 = time.time()
mons, M = build(W, N, q, symmetric=True)
print('built %d symmetric monomials, %d rows, %.1fs' % (len(mons), M.shape[0], time.time() - t0), flush=True)
b = np.array([lad_mod(KEY, n, q) for n in range(N + 1)], dtype=np.int64)

deg1 = [j for j, m in enumerate(mons) if len(m) == 1]
print('degree-1 columns: %d -> %s' % (len(deg1), [monname(mons[j]) for j in deg1]))


def rank_mod(A, q):
    A = [list(map(int, r)) for r in A]
    rows, cols = len(A), len(A[0])
    r = 0
    for c in range(cols):
        p = None
        for i in range(r, rows):
            if A[i][c] % q:
                p = i; break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        iv = pow(A[r][c], q - 2, q)
        A[r] = [x * iv % q for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % q for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


base = M[:, deg1]
rb = rank_mod(base, q)
rbb = rank_mod(np.hstack([base, b[:, None]]), q)
print('base: rank(A)=%d rank(A|b)=%d' % (rb, rbb), flush=True)

hits = []
cands = [j for j in range(len(mons)) if j not in set(deg1)]
print('candidates: %d' % len(cands), flush=True)
import itertools
for extra in itertools.combinations(cands, NEXTRA):
    A = np.hstack([base] + [M[:, [j]] for j in extra])
    ra = rank_mod(A, q)
    rab = rank_mod(np.hstack([A, b[:, None]]), q)
    if ra == rab:
        hits.append((extra, ra))
        print('  HIT  %s   rank=%d' % (' + '.join(monname(mons[j]) for j in extra), ra), flush=True)
print('total hits: %d   (%.1fs)' % (len(hits), time.time() - t0))
