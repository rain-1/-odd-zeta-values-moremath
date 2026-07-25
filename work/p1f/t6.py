"""T6 -- THE decisive test.

Hypothesis (DEPTH-CANCELS):  the 42 p-independent (DEPTH) linear conditions of
PHASE2_FINAL 2.3 ALONE already force the aggregate cancellation, i.e. for EVERY
weight-5 form w in the 448-monomial basis satisfying them (not just the members
of the fitting family),

        v_p ( sum_{k,l} T(n,k,l) w(n,k,l) )  >=  0      for every n < p, p >= 5 .

The cell-wise bound only gives >= -1, so this is exactly the missing cancellation.
If true, (BASE) follows from (DEPTH) with NO input from the fitting system.
"""
import sys, random, time
from fractions import Fraction as F
from collections import defaultdict

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1d')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1f')
from depthcond import basis, patterns, elem_expansion
from core import vp, T, Hs
import w5eval


def cond_matrix():
    B = basis()
    caps = patterns()
    NC = len(B.els)
    rows = defaultdict(lambda: [F(0)] * NC)
    for ci, e in enumerate(B.els):
        for pat, cap in caps.items():
            if pat == (0, 0, 0, 1):
                continue
            for (u, sym), v in elem_expansion(B, e, pat).items():
                if u > cap:
                    rows[(pat, u, sym)][ci] += v
    C = [v for v in rows.values() if any(v)]
    return B, C, NC


def rref_Q(M, ncols):
    M = [r[:] for r in M]
    piv = []
    r = 0
    for c in range(ncols):
        pr = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        iv = F(1) / M[r][c]
        M[r] = [x * iv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(ncols)]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    return M[:r], piv


def random_depth_form(R, piv, NC, rnd, mag=9):
    """random x with C x = 0 : free coords random, pivots solved."""
    free = [c for c in range(NC) if c not in piv]
    x = [F(0)] * NC
    for c in free:
        x[c] = F(rnd.randint(-mag, mag))
    for i, c in enumerate(piv):
        x[c] = -sum(R[i][j] * x[j] for j in free if R[i][j])
    return x


def terms_from_vec(B, x):
    out = []
    for ci, e in enumerate(B.els):
        if x[ci] == 0:
            continue
        i, j, cid, nid = e
        f, g = list(B.km[i][0]), list(B.km[j][0])
        h, s = list(B.cm[cid][0]), list(B.nm[nid][0])
        out.append((x[ci], f, g, h, s))
    return out


if __name__ == '__main__':
    t0 = time.time()
    B, C, NC = cond_matrix()
    print('basis %d, condition rows %d (%.0fs)' % (NC, len(C), time.time() - t0), flush=True)
    R, piv = rref_Q(C, NC)
    print('rank(cond) = %d, nullity = %d' % (len(piv), NC - len(piv)), flush=True)
    rnd = random.Random(20260725)
    NTRIAL = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    PR = [5, 7, 11, 13]
    for trial in range(NTRIAL):
        x = random_depth_form(B, piv, NC, rnd) if False else random_depth_form(R, piv, NC, rnd)
        terms = terms_from_vec(B, x)
        print('trial %d: %d nonzero coefficients' % (trial, len(terms)), flush=True)
        for p in PR:
            worst = 99
            cellworst = 99
            for n in range(1, p):
                S = F(0)
                for k in range(n + 1):
                    for l in range(n + 1):
                        v = w5eval.w5(n, k, l, terms)
                        S += T(n, k, l) * v
                        if v:
                            cellworst = min(cellworst, vp(T(n, k, l) * v, p))
                if S:
                    worst = min(worst, vp(S, p))
            print('    p=%2d   min_n v_p(sum T w) = %-4s   min cellwise v_p(T w) = %s'
                  % (p, worst, cellworst), flush=True)
