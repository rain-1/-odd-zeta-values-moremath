"""eps27.py -- weight-5 bridge, round 4: ENDPOINT-range elementary jets.

eps26 added elementary-symmetric pole cancellations on the double-zero middle
range B=(k,n] (EB) and on the full numerator multiset (EN).  It did NOT add
the elementary symmetric functions of the two SIMPLE-zero endpoint ranges

    A = (0, k]      (reciprocals 1/(z+i), 1 <= i <= k),
    C = (n, n+k]    (reciprocals 1/(z+i), n < i <= n+k),

nor of their union.  An elementary symmetric function e_r of a set of simple
poles has only SIMPLE poles at each member point, so e_r(A), e_r(C), e_r(AUC)
are admissible against the simple zeros of R_k with ledger cost 1 per range,
at every degree r -- exactly the 'weighted endpoint jet' the pole ledger on
power sums forbids.

Families added:
  (i)  residue generators R[mono]xphi with monomials over the enlarged
       alphabet BLOCKS + EB + EN + EA + EC + EAC (must contain a new block);
  (ii) value towers EV[mono|range] and derivative towers DV[mono] for the
       enlarged monomials, same validity rules as eps25/eps26.
"""

import sys, time, pickle
import numpy as np
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')

import eps24
import eps25
import eps26
from eps24 import (f_add, f_scale, s_mul, ONE, ESER, PHI, BLOCKS,
                   GEN_FORMS, GEN_NAMES, form_to_vec_modp, block_sumrange,
                   hdiff, f_mul)
from eps25 import NEWF, NEWN, RANGES
from eps26 import (EF as EF26, EN as EN26, elementary_series,
                   EBLOCKS as EBLOCKS26, rank_rows, row_echelon)
from eps22 import MON, MIDX, NM, SIG, DELTA5, build_rows

# ---------------- new elementary blocks ----------------
PS_A = {r: block_sumrange(7, 2, r) for r in range(1, 5)}   # (0,k]
PS_C = {r: block_sumrange(8, 4, r) for r in range(1, 5)}   # (n,n+k]
PS_AC = {r: eps26.s_add(PS_A[r], PS_C[r]) for r in range(1, 5)}

EA = {r: elementary_series(PS_A, r) for r in range(2, 5)}
EC = {r: elementary_series(PS_C, r) for r in range(2, 5)}
EAC = {r: elementary_series(PS_AC, r) for r in range(2, 5)}

NEWBLOCKS = dict(EBLOCKS26)
for r in range(2, 5):
    NEWBLOCKS['EA%d' % r] = (EA[r], r, (1, 0, 0))
    NEWBLOCKS['EC%d' % r] = (EC[r], r, (0, 0, 1))
    NEWBLOCKS['EX%d' % r] = (EAC[r], r, (1, 0, 1))

NEWNAMES = set(n for n in NEWBLOCKS if n.startswith(('EA', 'EC', 'EX')))

monomials = []
block_names = list(NEWBLOCKS)

def enumerate_blocks(index, current, weight, ledger):
    if index == len(block_names):
        if any(name in NEWNAMES for name in current):
            monomials.append(tuple(current))
        return
    name = block_names[index]
    _, block_weight, block_ledger = NEWBLOCKS[name]
    repetitions = 0
    while True:
        new_weight = weight + repetitions * block_weight
        new_ledger = tuple(ledger[i] + repetitions * block_ledger[i]
                           for i in range(3))
        if (new_weight > 4 or new_ledger[0] > 1
                or new_ledger[1] > 2 or new_ledger[2] > 1):
            break
        enumerate_blocks(index + 1, current + [name] * repetitions,
                         new_weight, new_ledger)
        repetitions += 1

enumerate_blocks(0, [], 0, (0, 0, 0))
print('new endpoint-elementary monomials:', len(monomials))

XF, XN = [], []
for mono in monomials:
    weight = sum(NEWBLOCKS[name][1] for name in mono)
    series = ESER
    for name in mono:
        series = s_mul(series, NEWBLOCKS[name][0])
    base = series.get(1, {})
    if not base:
        continue
    for pm, pf in PHI[4 - weight]:
        XF.append(f_mul(base, pf))
        XN.append('R[%s]x%s' % ('.'.join(mono), pm))

# value / derivative towers over the enlarged monomials
for mono in monomials:
    weight = sum(NEWBLOCKS[name][1] for name in mono)
    if weight > 3:
        continue
    ledger = tuple(sum(NEWBLOCKS[name][2][i] for name in mono)
                   for i in range(3))
    q_lattice = sum(int(name[1]) for name in mono if name.startswith('Q'))
    pole_order = 2 + q_lattice
    series = ESER
    for name in mono:
        series = s_mul(series, NEWBLOCKS[name][0])
    coefficients = {s: series.get(2 - s, {}) for s in range(1, pole_order + 1)}
    valid = {'A': ledger[0] == 0, 'B': ledger[1] <= 1, 'C': ledger[2] == 0}
    for range_name, ((lo, hi), regions) in RANGES.items():
        if not all(valid[region] for region in regions):
            continue
        base = {}
        for s in range(1, pole_order + 1):
            if coefficients[s]:
                base = f_add(base, f_mul(coefficients[s], hdiff(s, hi, lo)),
                             F((-1) ** s))
        if not base:
            continue
        for pm, pf in PHI[3 - weight]:
            XF.append(f_mul(base, pf))
            XN.append('EV[%s|%s]x%s' % ('.'.join(mono), range_name, pm))
    if weight <= 2 and ledger[1] == 0:
        base = {}
        for s in range(1, pole_order + 1):
            if coefficients[s]:
                base = f_add(base,
                             f_mul(coefficients[s], hdiff(s + 1, 4, 7)),
                             F(s * (-1) ** s))
        if base:
            for pm, pf in PHI[2 - weight]:
                XF.append(f_mul(base, pf))
                XN.append('DV[%s]x%s' % ('.'.join(mono), pm))

print('eps27 new generators:', len(XF))

if __name__ == '__main__':
    prime = int(sys.argv[1]) if len(sys.argv) > 1 else 4194301
    rows, _ = build_rows(prime, 40)

    all_forms = GEN_FORMS + NEWF + EF26 + XF
    all_names = GEN_NAMES + NEWN + EN26 + XN
    vectors = np.zeros((len(all_forms), NM), dtype=np.int64)
    for i, form in enumerate(all_forms):
        vectors[i] = form_to_vec_modp(form, prime)

    bad = []
    start = time.time()
    for lo in range(0, len(all_forms), 64):
        hi = min(lo + 64, len(all_forms))
        values = rows.dot(vectors[lo:hi].T) % prime
        for j in range(hi - lo):
            if values[:, j].any():
                bad.append(lo + j)
    print('calibration failures:', len(bad), 'of', len(all_forms),
          '(%.1fs)' % (time.time() - start))
    if bad:
        print('first failures:', [all_names[i] for i in bad[:30]])

    keep = [i for i in range(len(all_forms)) if i not in set(bad)]
    good = vectors[keep]
    inv2 = pow(2, prime - 2, prime)
    sym = (good + good[:, SIG]) * inv2 % prime

    target = np.zeros(NM, dtype=np.int64)
    for mono, coefficient in DELTA5.items():
        target[MIDX[mono]] = (coefficient.numerator % prime
                              * pow(coefficient.denominator % prime,
                                    prime - 2, prime)) % prime
    target = (target + target[SIG]) * inv2 % prime

    old_count = len(GEN_FORMS) + len(NEWF) + len(EF26)
    old_good = [j for j, original in enumerate(keep) if original < old_count]
    rank_old = rank_rows(sym[old_good], prime)
    rank_new = rank_rows(sym, prime)
    rank_target = rank_rows(np.vstack([sym, target[None, :]]), prime)
    print('ranks old/new/with target:', rank_old, rank_new, rank_target)
    print('VERDICT:', 'BRIDGE IN SPAN' if rank_target == rank_new
          else 'still missing')
    if rank_target != rank_new:
        basis, pivots = row_echelon(sym, prime)
        residual = target.copy()
        for row, pivot in zip(basis, pivots):
            if residual[pivot]:
                residual = (residual - residual[pivot] * row) % prime
        support = np.nonzero(residual)[0]
        print('quotient residual support:', len(support))
