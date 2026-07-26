"""What IS the telescoper order of  T . w5  for the one weight-5 representative
we have in closed form?  (Complement to the order-3 exclusion.)

L = A . L_BZ,  A = sum_{t=0}^{m-3} a_t S_n^t, over zla's 58-monomial closure of
w5.  Only the 26 STANDALONE blocks are used (o_scan's default block list is
wrong for w5: 7 letter blocks and () are coupled), so the answer is a NECESSARY
condition on the a-direction -- exactly as at weight 3.

Calibration carried in every run: the block ('u4',) must behave like weight 3's
('u2',) -- it is solvable separately for every t, so an adequate ansatz returns
dimension exactly m-2 there.
"""
import sys, time
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5w5')
import zla, solve, fastlin, ratrec, ordm, o_scan
from solve import Ansatz
import pd5


def structure(which, m):
    F = zla.FQ()
    w = zla.weight_element(F, which)
    B = zla.closure_basis(w)
    supp = set(B.index(mm) for mm in w)
    def up(i):
        out = []
        for j, mj in enumerate(B):
            rest = list(mj); ok = True
            for L in B[i]:
                if L in rest: rest.remove(L)
                else: ok = False; break
            if ok and j != i: out.append(j)
        return out
    maxi = set(i for i in range(len(B)) if not up(i))
    stand = [i for i in range(len(B))
             if i not in maxi and all(j in supp or j in maxi for j in up(i))]
    return B, supp, maxi, stand


def run(which, n, m, dname, slack, p=pd5.P1, npts=None, verbose=True):
    B, supp, maxi, stand = structure(which, m)
    ans, dk, dl = pd5.ansatz(dname, slack, m)
    na = m - 2
    if npts is None:
        npts = int(1.35 * (ans.nc + na)) + 60
    t0 = time.time()
    pd = ordm.PDm(which, p, n, m, npts)
    Acol = ordm.acols(pd)
    blocks = [j for j in stand]
    M = o_scan.scal_mat(pd, ans)
    As = [Acol[i * npts:(i + 1) * npts] for i in blocks]
    subs, rank = o_scan.asubspaces(M, As, p)
    inter = o_scan.intersect(subs, na, p)
    calib = None
    for t, i in enumerate(blocks):
        if pd.B[i] == ('u4',) or pd.B[i] == ('u2',):
            calib = (str(pd.B[i]), len(subs[t]))
    if verbose:
        print('%s n=%d m=%2d %s slack=%d bideg=(%d,%d) nc=%d rows=%d ratio=%.2f '
              'blocks=%d rank=%d  [%.0fs]'
              % (which, n, m, dname, slack, dk, dl, ans.nc, npts,
                 npts / (ans.nc + na), len(blocks), rank, time.time() - t0), flush=True)
        print('    calibration block %s : dim %s  (adequate iff = m-2 = %d)'
              % (calib[0] if calib else '-', calib[1] if calib else '-', na), flush=True)
        print('    >>> COMMON a-directions over the %d standalone blocks: %d %s'
              % (len(blocks), len(inter),
                 ' *** TELESCOPER CANDIDATE ***' if inter else ''), flush=True)
    return len(inter), (calib[1] if calib else None)


if __name__ == '__main__':
    which = sys.argv[1]; n = int(sys.argv[2]); dname = sys.argv[3]
    slack = int(sys.argv[4]); ms = [int(x) for x in sys.argv[5].split(',')]
    for m in ms:
        run(which, n, m, dname, slack)
