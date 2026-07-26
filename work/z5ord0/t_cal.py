"""CALIBRATION: w = L_k + L_l, the identity PROVED uniformly in Z5CF_BARNES
section 7.  Known-answer adequacy control (discipline 2 of the brief).

Bottom boundary is the GROUPED module condition (force_k = 0, bnd = True):
at k = 0 the monomials collapse (h*_k dies, h*_pk and h*_mk both become h*_n,
h*_kl -> h*_l, h*_pkl -> h*_pl), so only the sum over each collapse class must
vanish.  Per-block forcing is strictly stronger and destroys the trivial-pair
gauge.
"""
import sys

import joint0 as J
import o0core as C
import weights as W

FAMS = {
    'F1': [(C.K1, 3), (C.L1, 3), (C.KL[1], 1)],
    'F2': [(C.K1, 3), (C.L1, 3), (C.KL[1], 2), (C.KL[2], 1)],
    'F3': [(C.K1, 3), (C.L1, 3), (C.KL[1], 2), (C.KL[2], 1),
           (C.NK[1], 1), (C.NL[1], 1), (C.NKL[1], 1)],
    'F4': [(C.K1, 3), (C.K2, 1), (C.L1, 3), (C.L2, 1), (C.KL[1], 2),
           (C.KL[2], 2), (C.NK[1], 2), (C.NL[1], 2), (C.NKL[1], 1),
           (C.MK[1], 1), (C.ML[1], 1)],
    'F5': [(C.K1, 4), (C.K2, 2), (C.L1, 4), (C.L2, 2), (C.KL[1], 3),
           (C.KL[2], 2), (C.KL[3], 1), (C.NK[1], 2), (C.NK[2], 1),
           (C.NL[1], 2), (C.NL[2], 1), (C.NKL[1], 2), (C.MK[1], 2),
           (C.ML[1], 2)],
}

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    mds = [int(x) for x in (sys.argv[2].split(',') if len(sys.argv) > 2
                            else ['1', '2'])]
    fams = sys.argv[3].split(',') if len(sys.argv) > 3 else list(FAMS)
    degs = [int(x) for x in (sys.argv[4].split(',') if len(sys.argv) > 4
                             else ['6', '8'])]
    w = W.w_cal()
    print('CALIBRATION  w = L_k + L_l   supp=%d   n=%d   grouped bottom '
          'boundary, force_k=0' % (len(w), n), flush=True)
    for md in mds:
        for lab in fams:
            for deg in degs:
                nc = (deg + 1) ** 2
                npts = 3 * nc
                J.run(w, n, FAMS[lab], deg, md, npts, force_k=0, bnd=True,
                      label='md%d/%s/d%d' % (md, lab, deg))
