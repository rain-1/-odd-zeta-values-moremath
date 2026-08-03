"""Weight-five bridge: elementary-symmetric endpoint residue generators.

The power-sum generators P_r=sum_i (z+i)^(-r) have poles of order r at
simple zeros of the Barnes numerator.  The elementary combinations e_r have
only simple poles and are therefore admissible.  This script adds e_2,e_3,e_4
on the two simple-zero endpoint ranges and tests the one missing bridge
dimension from eps25.
"""

import sys
import time
import numpy as np
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')

import eps24
import eps25
from eps24 import (f_add, f_scale, s_mul, s_from, ONE, ESER, PHI, BLOCKS,
                   GEN_FORMS, GEN_NAMES, form_to_vec_modp,
                   block_sumrange)
from eps25 import NEWF, NEWN
from eps25 import RANGES
from eps22 import MON, MIDX, NM, SIG, DELTA5, build_rows


def s_add(a, b, scale=F(1)):
    out = {j: dict(v) for j, v in a.items()}
    for j, form in b.items():
        if j in out:
            out[j] = f_add(out[j], form, scale)
        else:
            out[j] = f_scale(form, scale)
    return {j: form for j, form in out.items() if form}


def s_scale(a, scale):
    return {j: f_scale(form, scale) for j, form in a.items() if form}


def elementary_series(power_sums, degree):
    """Newton recursion r e_r=sum_{i=1}^r (-1)^(i-1)e_(r-i) P_i."""
    e = {0: s_from({0: ONE})}
    for r in range(1, degree + 1):
        acc = {}
        for i in range(1, r + 1):
            term = s_mul(e[r - i], power_sums[i])
            acc = s_add(acc, term, F((-1) ** (i - 1)))
        e[r] = s_scale(acc, F(1, r))
    return e[degree]


def endpoint_elementaries(hi, lo):
    ps = {r: block_sumrange(hi, lo, r) for r in range(1, 5)}
    return {r: elementary_series(ps, r) for r in range(2, 5)}


EB = endpoint_elementaries(4, 7)   # k < i <= n

# The two numerator products of R_k have the reciprocal multiset
#   {1/(z+i): 1<=i<=k} union 2*{1/(z+i): k<i<=n}
#       union {1/(z+i): n<i<=n+k}.
# Its elementary symmetric functions have exactly the pole multiplicities
# absorbed by the numerator of R_k, at every degree.  Termwise pole ledgers on
# Newton's power sums miss this global cancellation.
NUMPS = {}
for r in range(1, 5):
    NUMPS[r] = s_add(
        s_add(block_sumrange(7, 2, r),
              block_sumrange(4, 7, r), F(2)),
        block_sumrange(8, 4, r))
ENUM = {r: elementary_series(NUMPS, r) for r in range(2, 5)}

EF, EN = [], []

# Add the endpoint elementaries to the full admissible rho alphabet.  Their
# ledger cost is one (a simple pole) regardless of their harmonic weight.
EBLOCKS = dict(BLOCKS)
for r in range(2, 5):
    # An elementary symmetric function has only a simple pole at each member
    # of its range.  The middle zeros of R_k have order two, so products of
    # two such blocks remain admissible.  This cancellation is invisible if
    # one assigns the pole ledger term-by-term in Newton's power sums.
    EBLOCKS['EB%d' % r] = (EB[r], r, (0, 1, 0))
    EBLOCKS['EN%d' % r] = (ENUM[r], r, (1, 2, 1))

extended_monomials = []
block_names = list(EBLOCKS)

def enumerate_blocks(index, current, weight, ledger):
    if index == len(block_names):
        if any(name.startswith(('EB', 'EN')) for name in current):
            extended_monomials.append(tuple(current))
        return
    name = block_names[index]
    _, block_weight, block_ledger = EBLOCKS[name]
    repetitions = 0
    while True:
        new_weight = weight + repetitions * block_weight
        new_ledger = tuple(ledger[i] + repetitions * block_ledger[i] for i in range(3))
        if (new_weight > 4 or new_ledger[0] > 1
                or new_ledger[1] > 2 or new_ledger[2] > 1):
            break
        enumerate_blocks(index + 1, current + [name] * repetitions,
                         new_weight, new_ledger)
        repetitions += 1

enumerate_blocks(0, [], 0, (0, 0, 0))

for mono in extended_monomials:
    weight = sum(EBLOCKS[name][1] for name in mono)
    series = ESER
    for name in mono:
        series = s_mul(series, EBLOCKS[name][0])
    base = series.get(1, {})
    for pm, pf in PHI[4 - weight]:
        EF.append(eps24.f_mul(base, pf))
        EN.append('R[%s]x%s' % ('.'.join(mono), pm))

# The same enlarged alphabet in the numerator-zero value and derivative
# towers.  A value vanishes when the zero order is strictly larger than the
# pole order; a derivative on the double-zero middle range requires no pole.
for mono in extended_monomials:
    weight = sum(EBLOCKS[name][1] for name in mono)
    if weight > 3:
        continue
    ledger = tuple(sum(EBLOCKS[name][2][i] for name in mono) for i in range(3))
    q_lattice = sum(int(name[1]) for name in mono if name.startswith('Q'))
    pole_order = 2 + q_lattice
    series = ESER
    for name in mono:
        series = s_mul(series, EBLOCKS[name][0])
    coefficients = {s: series.get(2 - s, {}) for s in range(1, pole_order + 1)}

    valid = {'A': ledger[0] == 0, 'B': ledger[1] <= 1, 'C': ledger[2] == 0}
    for range_name, ((lo, hi), regions) in RANGES.items():
        if not all(valid[region] for region in regions):
            continue
        base = {}
        for s in range(1, pole_order + 1):
            if coefficients[s]:
                base = f_add(base,
                             eps24.f_mul(coefficients[s], eps24.hdiff(s, hi, lo)),
                             F((-1) ** s))
        for pm, pf in PHI[3 - weight]:
            EF.append(eps24.f_mul(base, pf))
            EN.append('EV[%s|%s]x%s' % ('.'.join(mono), range_name, pm))

    if weight <= 2 and ledger[1] == 0:
        base = {}
        for s in range(1, pole_order + 1):
            if coefficients[s]:
                base = f_add(
                    base,
                    eps24.f_mul(coefficients[s], eps24.hdiff(s + 1, 4, 7)),
                    F(s * (-1) ** s))
        for pm, pf in PHI[2 - weight]:
            EF.append(eps24.f_mul(base, pf))
            EN.append('DV[%s]x%s' % ('.'.join(mono), pm))

print('elementary endpoint generators:', len(EF))


def rank_rows(matrix, prime):
    matrix = matrix.copy()
    nrows, ncols = matrix.shape
    rank = 0
    for col in range(ncols):
        nz = np.nonzero(matrix[rank:, col] % prime)[0]
        if not len(nz):
            continue
        pivot = rank + nz[0]
        if pivot != rank:
            matrix[[rank, pivot]] = matrix[[pivot, rank]]
        matrix[rank] = matrix[rank] * pow(int(matrix[rank, col]), prime - 2, prime) % prime
        column = matrix[:, col].copy()
        column[rank] = 0
        active = np.nonzero(column)[0]
        if len(active):
            matrix[active] = (matrix[active]
                              - column[active, None] * matrix[rank][None, :]) % prime
        rank += 1
        if rank == nrows:
            break
    return rank


def row_echelon(matrix, prime):
    matrix = matrix.copy()
    nrows, ncols = matrix.shape
    rank = 0
    pivots = []
    for col in range(ncols):
        nz = np.nonzero(matrix[rank:, col] % prime)[0]
        if not len(nz):
            continue
        pivot = rank + nz[0]
        if pivot != rank:
            matrix[[rank, pivot]] = matrix[[pivot, rank]]
        matrix[rank] = matrix[rank] * pow(int(matrix[rank, col]), prime - 2, prime) % prime
        column = matrix[:, col].copy()
        column[rank] = 0
        active = np.nonzero(column)[0]
        if len(active):
            matrix[active] = (matrix[active]
                              - column[active, None] * matrix[rank][None, :]) % prime
        pivots.append(col)
        rank += 1
        if rank == nrows:
            break
    return matrix[:rank], pivots


if __name__ == '__main__':
    prime = int(sys.argv[1]) if len(sys.argv) > 1 else 4194301
    rows, _ = build_rows(prime, 40)

    all_forms = GEN_FORMS + NEWF + EF
    all_names = GEN_NAMES + NEWN + EN
    vectors = np.zeros((len(all_forms), NM), dtype=np.int64)
    for i, form in enumerate(all_forms):
        vectors[i] = form_to_vec_modp(form, prime)

    # Calibrate in chunks; with this prime all dot products fit in int64.
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
        print('first failures:', [all_names[i] for i in bad[:20]])

    keep = [i for i in range(len(all_forms)) if i not in set(bad)]
    good = vectors[keep]
    inv2 = pow(2, prime - 2, prime)
    sym = (good + good[:, SIG]) * inv2 % prime

    target = np.zeros(NM, dtype=np.int64)
    for mono, coefficient in DELTA5.items():
        target[MIDX[mono]] = (coefficient.numerator % prime
                              * pow(coefficient.denominator % prime, prime - 2, prime)) % prime
    target = (target + target[SIG]) * inv2 % prime

    old_count = len(GEN_FORMS) + len(NEWF)
    old_good = [j for j, original in enumerate(keep) if original < old_count]
    rank_old = rank_rows(sym[old_good], prime)
    rank_new = rank_rows(sym, prime)
    rank_target = rank_rows(np.vstack([sym, target[None, :]]), prime)
    print('ranks old/new/with target:', rank_old, rank_new, rank_target)
    print('VERDICT:', 'BRIDGE IN SPAN' if rank_target == rank_new else 'still missing')
    if rank_target != rank_new:
        basis, pivots = row_echelon(sym, prime)
        residual = target.copy()
        for row, pivot in zip(basis, pivots):
            if residual[pivot]:
                residual = (residual - residual[pivot] * row) % prime
        support = np.nonzero(residual)[0]
        print('quotient residual support:', len(support))
        for index in support[:120]:
            value = int(residual[index])
            signed = value if value <= prime // 2 else value - prime
            print(' ', MON[index], signed)
