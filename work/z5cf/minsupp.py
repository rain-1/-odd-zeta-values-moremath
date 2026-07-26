"""Minimum-support search:  smallest S with b in colspace(M_S).

Random projection to L rows (candidates verified against the full system).
For support size t: enumerate prefixes of size t-2, eliminate them, quotient by b,
then hash-match the remaining columns (two columns with parallel images span b
together with the prefix).
"""
import sys, os, time, itertools, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from design2 import build, monomials, sym_orbits, monname, rref
from bare import Q1, lad_mod

W = int(sys.argv[1]); KEY = sys.argv[2]; DMAX = int(sys.argv[3])
SY = tuple(int(x) for x in sys.argv[4].split(','))
N = int(sys.argv[5]); TMAX = int(sys.argv[6]) if len(sys.argv) > 6 else 5
q = Q1
L = 24

mons = sym_orbits(monomials(W, DMAX, SY))
_, M = build(W, N, q, mons=mons)
M = M % q
b = np.array([lad_mod(KEY, n, q) for n in range(N + 1)], dtype=np.int64)
NC = len(mons)
print('%d columns, %d rows' % (NC, N + 1), flush=True)

rng = np.random.default_rng(20260726)
Pr = rng.integers(0, q, size=(L, N + 1))
A0 = np.array([[int(sum(int(Pr[i, n]) * int(M[n, j]) for n in range(N + 1)) % q)
                for j in range(NC)] for i in range(L)], dtype=np.int64)
c0 = np.array([int(sum(int(Pr[i, n]) * int(b[n]) for n in range(N + 1)) % q)
               for i in range(L)], dtype=np.int64)


def elim(A, c, j):
    col = A[:, j]
    nz = np.nonzero(col)[0]
    if nz.size == 0:
        return None
    p = int(nz[0])
    iv = pow(int(col[p]), q - 2, q)
    rowA = A[p] * iv % q
    rowc = int(c[p]) * iv % q
    keep = np.array([i for i in range(A.shape[0]) if i != p])
    return ((A[keep] - col[keep][:, None] * rowA[None, :]) % q,
            (c[keep] - col[keep] * rowc) % q)


def quotient_by_c(A, c):
    nz = np.nonzero(c)[0]
    if nz.size == 0:
        return None
    p = int(nz[0])
    iv = pow(int(c[p]), q - 2, q)
    coef = A[p] * iv % q                     # per-column coefficient along c
    keep = np.array([i for i in range(A.shape[0]) if i != p])
    return (A[keep] - c[keep][:, None] * coef[None, :]) % q


def norm_keys(V):
    rows, cols = V.shape
    nzm = V != 0
    has = nzm.any(axis=0)
    first = np.argmax(nzm, axis=0)
    piv = V[first, np.arange(cols)]
    inv = np.ones(cols, dtype=np.int64)
    for j in range(cols):
        if has[j]:
            inv[j] = pow(int(piv[j]), q - 2, q)
    Vn = V * inv % q
    return [Vn[:, j].tobytes() if has[j] else None for j in range(cols)], has


def verify(S):
    S = list(S)
    _, r1, _ = rref(M[:, S], q)
    _, r2, _ = rref(np.hstack([M[:, S], b[:, None]]), q)
    return r1 == r2


t0 = time.time()
found = None
for j in range(NC):
    if verify([j]):
        found = [j]; break
if found is None:
    for t in range(2, TMAX + 1):
        npre = 0
        for pre in itertools.combinations(range(NC), t - 2):
            Ai, ci = A0, c0
            ok = True
            for j in pre:
                r = elim(Ai, ci, j)
                if r is None:
                    ok = False; break
                Ai, ci = r
            if not ok:
                continue
            npre += 1
            V = quotient_by_c(Ai, ci)
            if V is None:
                continue
            keys, has = norm_keys(V)
            seen = {}
            pset = set(pre)
            for j in range(NC):
                if j in pset or not has[j]:
                    continue
                kk = keys[j]
                if kk in seen:
                    S = list(pre) + [seen[kk], j]
                    if verify(S):
                        found = S; break
                else:
                    seen[kk] = j
            if found:
                break
        if found:
            break
        print('   none at size %d (%d prefixes, %.1fs)' % (t, npre, time.time() - t0), flush=True)

if found:
    print('\nMINIMUM SUPPORT = %d' % len(found))
    for j in sorted(found):
        print('   ', monname(mons[j]))
else:
    print('\nno support of size <= %d' % TMAX)
print('%.1fs' % (time.time() - t0))
