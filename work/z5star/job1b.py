"""JOB 1b -- test the Barnes/Mellin contour-canonical symmetric candidate w_B3.

Reads (never writes) work/z5barnes/{universal,project_w3}.py.
Tests, in this order and with our own machinery:
  1. does w_B3 lie in the degree-<=2 bare span V at all (109 monomials)?
  2. is  sum_{k,l} T*w_B3 = Phat  exactly over Q  (our own range, our own T)?
  3. is w_B3 - what3 purely ANTISYMMETRIC?
  4. is w_B3 in W_tel (the 37-dim order-3 admissible space)?
  5. is w_B3 in the 12-dimensional admissible AFFINE FAMILY (i.e. does the
     coupling () block close for it too)?
"""
import sys, os, pickle
from fractions import Fraction as Fr
import numpy as np

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
sys.path.insert(1, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5barnes')
sys.path.insert(2, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
sys.path.insert(3, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
import wtools as W
import bare
import project_w3 as PB

HERE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 7


def fit_span(nmax, basis):
    """least-structure exact fit of barnes_w3 on all cells n<=nmax over `basis`"""
    triples = [(n, k, l) for n in range(nmax + 1)
               for k in range(n + 1) for l in range(n + 1)]
    rows = []
    rhs = []
    for (n, k, l) in triples:
        row = []
        for m in basis:
            v = Fr(1)
            for L in m:
                r, a = bare.LETTERS[L]
                cn, ck, cl = bare.ARGS[a]
                v *= W.H(r, cn * n + ck * k + cl * l)
            row.append(v)
        rows.append(row)
        rhs.append(Fr(PB.barnes_w3(n, k, l)))
    return triples, rows, rhs


def solve_ls(rows, rhs, ncol):
    """exact solve of an overdetermined consistent system; returns (x, ok, nfree)"""
    aug = [list(map(Fr, r)) + [Fr(b)] for r, b in zip(rows, rhs)]
    R, piv = W.rrefQ(aug)
    if any(c == ncol for c in piv):
        return None, False, 0
    x = [Fr(0)] * ncol
    for i, c in enumerate(piv):
        x[c] = R[i][ncol]
    return x, True, ncol - len(piv)


if __name__ == '__main__':
    print('--- 1. does w_B3 lie in the degree-<=2 bare span V ? ---', flush=True)
    triples, rows, rhs = fit_span(NMAX, W.B)
    x, ok, nfree = solve_ls(rows, rhs, W.J109)
    print('   cells %d, basis %d : %s (free params %d)'
          % (len(triples), W.J109, 'CONSISTENT' if ok else 'INCONSISTENT', nfree))
    if not ok:
        print('   => w_B3 is NOT in the degree-<=2 weight-3 bare span. '
              'It must carry H^(1)H^(1)H^(1) terms.')
        sys.exit(0)
    wB = x
    # held-out cells
    bad = []
    for n in range(NMAX + 1, NMAX + 4):
        for k in range(n + 1):
            for l in range(n + 1):
                if W.wval(wB, n, k, l) != Fr(PB.barnes_w3(n, k, l)):
                    bad.append((n, k, l))
    print('   held-out cells n=%d..%d : %s'
          % (NMAX + 1, NMAX + 3, 'PASS' if not bad else 'FAIL %s' % bad[:3]))
    W.show(wB, 'w_B3')
    print('   symmetric ?', W.sig(wB) == wB)
    pickle.dump(wB, open(os.path.join(HERE, 'wB3.pkl'), 'wb'))
    for nm, c in W.render(wB):
        print('      %-24s %s' % (nm, c))

    print()
    print('--- 2. is  sum T*w_B3 = Phat  exactly over Q ? ---', flush=True)
    W.check_rep(wB, 14)

    print()
    print('--- 3. is  w_B3 - what3  purely ANTISYMMETRIC ? ---', flush=True)
    wh = [Fr(0)] * W.J109
    for m, c in bare.w3hat_el().items():
        wh[W.IDX[m]] = Fr(c)
    dd = [wB[j] - wh[j] for j in range(W.J109)]
    s = W.symQ(dd)
    print('   sym part zero ? %s  (nonzero coords %d)'
          % (all(v == 0 for v in s), len(W.support(s))))

    print()
    print('--- 4/5. admissibility ---', flush=True)
    p = W.P1
    os.chdir('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
    Wc = pickle.load(open('Wcum_m3_F1_s16_p%d_d2.pkl' % p, 'rb'))
    K = np.load('K_d2_p%d.npy' % p)
    import solve as S
    wBp = W.to_p(wB, p)

    def rk(M):
        return len(S.rref(np.array(M, dtype=np.int64).copy() % p, p)[1])
    Wl = [np.array(v, dtype=np.int64) for v in Wc]
    print('   dim W_tel = %d ; w_B3 in W_tel ? %s'
          % (rk(Wl), rk(Wl + [wBp]) == rk(Wl)))
    both = Wl + [np.array(v, dtype=np.int64) for v in K]
    print('   w_B3 in W_tel + K ? %s' % (rk(both + [wBp]) == rk(both)))
    fam = pickle.load(open(os.path.join(HERE, 'familyQ.pkl'), 'rb'))
    bQ, UQ = fam['base'], fam['U']
    diff = [wB[j] - bQ[j] for j in range(W.J109)]
    R0, p0 = W.rrefQ([list(u) for u in UQ])
    R1, p1 = W.rrefQ([list(u) for u in UQ] + [diff])
    print('   w_B3 in the 12-dim admissible AFFINE FAMILY ? %s'
          % (len(p1) == len(p0)))
