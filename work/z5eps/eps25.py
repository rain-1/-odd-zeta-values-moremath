"""eps25.py -- weight-5 assembly, round 2: add the evaluation towers.

New proved families (same P-factor mechanism, calibrated before use):
 (c) VALUE tower:  (R_k rho)(-j) = 0 whenever zero-order of R_k at -j exceeds
     pole-order of rho there.  Partial-fraction expansion + range sums:
        sum_l sum_{s=1}^{q} (-1)^s c_s(l) (H^s_{beta+l}-H^s_{alpha+l}) = 0,
     c_s = [w^{2-s}] of E * rho-series (q = 2 + lattice-pole order of rho).
     Region validity: A=(0,k]: ledgerA=0 ; B=(k,n]: ledgerB<=1 ; C=(n,n+k]: ledgerC=0.
 (d) DERIVATIVE tower: (R_k rho)'(-j) = 0 on B when rho regular there (double zeros):
        sum_l sum_s s(-1)^s c_s(l) (H^{s+1}_{n+l}-H^{s+1}_{k+l}) = 0.
 (e) V5, the (L5) anti-diagonal residue at weight 5 (G6-analogue):
        2 H3diff(kl->nkl) + (Lk+Ll) H2diff + (LkLl-C2) H1diff,  x phi2.
"""
import sys, time, pickle
import numpy as np
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')

import eps24
from eps24 import (f_add, f_scale, f_mul, ONE, L, f_weight, s_mul, ESER,
                   BLOCKS, RHO_MONOS, PHI, LKf, LLf, LKLL_C2, hdiff,
                   GEN_FORMS, GEN_NAMES, form_to_vec_modp)
from eps22 import MON, MIDX, NM, SIG, DELTA5, build_rows

# region unions -> (alpha-arg, beta-arg), regions covered
RANGES = {
    'A':   ((2, 7), ('A',)),
    'B':   ((7, 4), ('B',)),
    'C':   ((4, 8), ('C',)),
    'AB':  ((2, 4), ('A', 'B')),
    'BC':  ((7, 8), ('B', 'C')),
    'ABC': ((2, 8), ('A', 'B', 'C')),
}

def ledger_of(mono):
    A = B = C = q = 0
    for nm in mono:
        led = BLOCKS[nm][2]
        A += led[0]; B += led[1]; C += led[2]
        if nm.startswith('Q'):
            q += int(nm[1])
    return A, B, C, q

NEWF, NEWN = [], []

for mono in RHO_MONOS:
    wt = sum(BLOCKS[nm][1] for nm in mono)
    if wt > 3: continue
    A, B, C, qlat = ledger_of(mono)
    q = 2 + qlat
    s_ = ESER
    for nm in mono:
        s_ = s_mul(s_, BLOCKS[nm][0])
    cs = {s: s_.get(2 - s, {}) for s in range(1, q + 1)}
    # ---- value tower ----
    okreg = {'A': A == 0, 'B': B <= 1, 'C': C == 0}
    for rnm, ((lo, hi), regs) in RANGES.items():
        if not all(okreg[r] for r in regs): continue
        base = {}
        for s in range(1, q + 1):
            if cs[s]:
                base = f_add(base, f_mul(cs[s], hdiff(s, hi, lo)), F((-1) ** s))
        if not base: continue
        assert f_weight(base) == {wt + 2}, (mono, rnm, f_weight(base))
        for pm, pf in PHI[3 - wt]:
            NEWF.append(f_mul(base, pf))
            NEWN.append('EV[%s|%s]x%s' % ('.'.join(mono) if mono else '1', rnm, pm))
    # ---- derivative tower (region B only, rho regular there) ----
    if wt <= 2 and B == 0:
        base = {}
        for s in range(1, q + 1):
            if cs[s]:
                base = f_add(base, f_mul(cs[s], hdiff(s + 1, 4, 7)), F(s * (-1) ** s))
        if base:
            assert f_weight(base) == {wt + 3}
            for pm, pf in PHI[2 - wt]:
                NEWF.append(f_mul(base, pf))
                NEWN.append('DV[%s]x%s' % ('.'.join(mono) if mono else '1', pm))

# ---- V5 ----
v5 = f_add(f_add(f_scale(hdiff(3, 8, 7), F(2)),
                 f_mul(f_add(LKf, LLf), hdiff(2, 8, 7))),
           f_mul(LKLL_C2, hdiff(1, 8, 7)))
for pm, pf in PHI[2]:
    NEWF.append(f_mul(v5, pf))
    NEWN.append('V5x%s' % (pm,))

print('new generators (towers + V5):', len(NEWF))

if __name__ == '__main__':
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 2147483647
    NROWS = 40
    t0 = time.time()
    rows, _ = build_rows(p, NROWS)
    print('Phi5 rows:', rows.shape, '%.1fs' % (time.time() - t0), flush=True)

    allF = GEN_FORMS + NEWF
    allN = GEN_NAMES + NEWN
    Gv = np.zeros((len(allF), NM), dtype=np.int64)
    for i, f in enumerate(allF):
        Gv[i] = form_to_vec_modp(f, p)
    t0 = time.time()
    bad = []
    for i in range(Gv.shape[0]):
        r = (rows * Gv[i][None, :] % p).sum(axis=1) % p
        if r.any(): bad.append(allN[i])
    print('calibration: %d of %d FAIL (%.0fs)' % (len(bad), Gv.shape[0], time.time() - t0))
    if bad: print('  failing (first 25):', bad[:25])
    keepi = [i for i in range(Gv.shape[0]) if allN[i] not in set(bad)]
    Gk = Gv[keepi]; knames = [allN[i] for i in keepi]

    i2 = pow(2, p - 2, p)
    fm = lambda fr: fr.numerator % p * pow(fr.denominator % p, p - 2, p) % p
    d5 = np.zeros(NM, dtype=np.int64)
    for m, cc in DELTA5.items():
        d5[MIDX[m]] = fm(cc)
    d5s = (d5 + d5[SIG]) * i2 % p
    Gs = (Gk + Gk[:, SIG]) * i2 % p

    def elim(Mx):
        m, nc = Mx.shape
        r = 0
        for c in range(nc):
            col = Mx[r:, c] % p
            nz = np.nonzero(col)[0]
            if len(nz) == 0: continue
            pr = r + nz[0]
            if pr != r: Mx[[r, pr]] = Mx[[pr, r]]
            inv = pow(int(Mx[r, c]), p - 2, p)
            Mx[r] = Mx[r] * inv % p
            col2 = Mx[:, c].copy(); col2[r] = 0
            nzr = np.nonzero(col2)[0]
            if len(nzr): Mx[nzr] = (Mx[nzr] - col2[nzr, None] * Mx[r][None, :]) % p
            r += 1
            if r == m: break
        return r

    rG = elim(Gs.copy())
    rGd = elim(np.vstack([Gs, d5s[None, :]]))
    print('rank sym(all gens) = %d ; with sym(Delta5) = %d -> %s'
          % (rG, rGd, 'IN SPAN' if rGd == rG else 'NOT IN SPAN'))

    if rGd == rG:
        # solve for a combination: least-structure approach -- rref on [Gs^T | d5s]
        A = np.vstack([Gs, d5s[None, :]]).T % p   # NM x (ng+1)
        m, nc = A.shape
        r = 0; piv = []
        for c in range(nc - 1):
            col = A[r:, c] % p
            nz = np.nonzero(col)[0]
            if len(nz) == 0: continue
            pr = r + nz[0]
            if pr != r: A[[r, pr]] = A[[pr, r]]
            inv = pow(int(A[r, c]), p - 2, p)
            A[r] = A[r] * inv % p
            col2 = A[:, c].copy(); col2[r] = 0
            nzr = np.nonzero(col2)[0]
            if len(nzr): A[nzr] = (A[nzr] - col2[nzr, None] * A[r][None, :]) % p
            piv.append(c); r += 1
        # consistency: rows beyond r must have 0 in last column
        ok = not A[r:, -1].any()
        print('solve consistent:', ok, ' pivots:', len(piv))
        x = np.zeros(nc - 1, dtype=np.int64)
        for i, c in enumerate(piv):
            x[c] = A[i, -1] % p
        # verify mod p
        resid = (Gs.T @ x % p - d5s) % p if False else None
        chk = np.zeros(NM, dtype=np.int64)
        for c in range(nc - 1):
            if x[c]:
                chk = (chk + x[c] * Gs[c]) % p
        print('mod-p residual max:', int(((chk - d5s) % p).max()))
        nzc = [(knames[c], int(x[c])) for c in range(nc - 1) if x[c]]
        print('nonzero coefficients:', len(nzc))
        with open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/eps25_combo_%d.pkl' % p, 'wb') as fh:
            pickle.dump({'x': x, 'names': knames, 'nz': nzc}, fh)
        from eps2 import ratrec
        print('sample coefficients (first 30, rational-reconstructed):')
        for nm, v in nzc[:30]:
            rr = ratrec(v, p)
            print('   %-40s %s' % (nm, '%d/%d' % rr if rr and rr[1] != 1 else (rr[0] if rr else v)))
