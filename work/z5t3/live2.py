"""live2.py -- round 2 on T3: weighted value towers + inverse weights + folding.

New column families (all still proved-null mechanisms):
  TX   weighted value towers:  0 = sum_{j in range} phi(j) * (R_k rho)(-j)
       for rho a monomial in the lattice blocks Q_r (no off-lattice poles, so
       (R_k rho)(-j) = 0 on the whole zero range (0, n+k]).  Expanding
       R_k rho = sum_l sum_s c_{l,s}/(z-l)^s  (exact, O(z^-2), no poly part)
       gives the null form  u(l) = sum_s (-1)^s c_s(l) * XS_s,
       XS_s = sum_{j in range} phi(j)/(j+l)^s,  s <= 2 + wt(rho).
       phi = any j-weight; this is what produces the high-power crossed
       letters  sum_j phi(j)/(j+l)^{3,4,5}  that the target's U-letters need.
  EXTW inverse-power weights (1/j^s, 1/(j+l)^s factors) added to the g/gp/q
       evaluation towers.
Folding: B_kl = A_kl L_k and D_kl = A_kl(L_k L_l - C_2) with bare L's, so the
three component rows per cell can be folded into ONE density row:
  f = a + L_k b + (L_k L_l - C_2) d.
Cellwise folded identity still implies  Sigma T [1]W_B = -2 Sigma T w5sym.
"""
import sys, time, pickle
import numpy as np
from fractions import Fraction as F

import live1 as L1
from live1 import (P, ROOT, HT, INV, invz, mq, hmod, old_columns_spec,
                   old_col_val, sal_cell_block, fold, REGION_NAMES,
                   SAL_WEIGHTS, target_modp, old_jrng, old_weval)
import fastlin
import weights as W
import evalq as E

NSOLVE = int(sys.argv[sys.argv.index('-n') + 1]) if '-n' in sys.argv else 12
NHOLD = int(sys.argv[sys.argv.index('-H') + 1]) if '-H' in sys.argv else 13
FOLDED = '--folded' in sys.argv

# ---------------------------------------------------------------- TX towers --
import eps24
from eps24 import s_mul, ESER, BLOCKS

TX_RHOS = [((), 0), (('Q1',), 1), (('Q2',), 2), (('Q1', 'Q1'), 2),
           (('Q3',), 3), (('Q1', 'Q2'), 3), (('Q1', 'Q1', 'Q1'), 3)]

def tx_cs_forms(mono):
    s_ = ESER
    for nm in mono:
        s_ = s_mul(s_, BLOCKS[nm][0])
    qlat = sum(BLOCKS[nm][1] for nm in mono)
    return {s: s_.get(2 - s, {}) for s in range(1, 2 + qlat + 1)}, qlat

TX_CS = {mono: tx_cs_forms(mono) for mono, _ in TX_RHOS}

# phi menu: monomials in H^(r)_j (r<=3) and j^-s (s<=3), exact weight w
def phi_menu(w):
    atoms = [(1, 'H'), (2, 'H'), (3, 'H'), (1, 'i'), (2, 'i'), (3, 'i')]
    out = []
    def rec(start, left, cur):
        if left == 0:
            out.append(tuple(cur))
            return
        for ai in range(start, len(atoms)):
            r, t = atoms[ai]
            if r <= left:
                rec(ai, left - r, cur + [(r, t)])
    rec(0, w, [])
    return out

def phi_val(spec, j):
    v = 1
    for (r, t) in spec:
        v = v * (hmod(j, r) if t == 'H' else int(INV[j]) if r == 1
                 else pow(int(INV[j]), r, P)) % P
    return v

TX_RANGES = ['A', 'B', 'C', 'AB', 'BC', 'ABC']
def tx_range(rname, n, kk):
    return {'A': (1, kk), 'B': (kk + 1, n), 'C': (n + 1, n + kk),
            'AB': (1, n), 'BC': (kk + 1, n + kk), 'ABC': (1, n + kk)}[rname]

def tx_columns_spec():
    cols = []
    for mono, qlat in TX_RHOS:
        for rname in TX_RANGES:
            for phi in phi_menu(3 - qlat):
                cols.append(('TX[%s|%s]x%s' % ('.'.join(mono) or '1',
                                               rname, phi), (mono, rname, phi)))
    return cols

def eval_form_modp(form, n, k, l):
    xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
    tot = 0
    for m, c in form.items():
        v = c.numerator % P * pow(c.denominator % P, P - 2, P) % P
        for (r, a) in m:
            v = v * hmod(xs[a], r) % P
        tot = (tot + v) % P
    return tot

def tx_col_val(spec, n, k, l):
    mono, rname, phi = spec
    cs, qlat = TX_CS[mono]
    i2 = (P + 1) // 2
    tot = 0
    for (kk, ll) in ((k, l), (l, k)):
        u = 0
        lo, hi = tx_range(rname, n, kk)
        if hi >= lo:
            # XS_s for all s at once
            xs_ = [0] * (2 + qlat + 1)
            for j in range(lo, hi + 1):
                pv = phi_val(phi, j)
                ijl = invz(j + ll)
                cur = pv
                for s in range(1, 2 + qlat + 1):
                    cur = cur * ijl % P
                    xs_[s] = (xs_[s] + cur) % P
            for s in range(1, 2 + qlat + 1):
                if cs.get(s):
                    csv = eval_form_modp(cs[s], n, kk, ll)
                    u = (u + (-1) ** s * csv * xs_[s]) % P
        tot = (tot + u) % P
    return tot * i2 % P

# ------------------------------------------------- extended g/gp/q weights ---
def ext_wbasis(weight, kind):
    """monomials with at least one inverse atom; H letters at j,l,jl(,jml),
    inverse powers at j, jl."""
    hargs = ['j', 'l', 'jl'] + (['jml'] if kind == 'overlap' else [])
    atoms = []
    for r in range(1, weight + 1):
        for a in hargs:
            atoms.append((r, 'H', a))
        for a in ('j', 'jl'):
            atoms.append((r, 'i', a))
    out = []
    def rec(start, left, cur, ninv):
        if left == 0:
            if ninv > 0:
                out.append(tuple(cur))
            return
        for ai in range(start, len(atoms)):
            r, t, a = atoms[ai]
            if r <= left:
                rec(ai, left - r, cur + [(r, t, a)], ninv + (t == 'i'))
    rec(0, weight, [], 0)
    return [('E' + str(spec), spec) for spec in out]

def ext_weval(spec, n, l, j):
    v = 1
    for (r, t, a) in spec:
        x = {'j': j, 'l': l, 'jl': j + l, 'jml': j - l}[a]
        if t == 'H':
            v = v * hmod(x, r) % P
        else:
            v = v * pow(invz(x), r, P) % P if x != 0 else 0
        if v == 0 and t == 'i' and x == 0:
            return 0
    return v

def extw_columns_spec():
    cols = []
    for kind in ('prefix', 'overlap', 'full'):
        for nm, spec in ext_wbasis(3, kind):
            cols.append(('gx/%s/%s' % (kind, nm), ('g', kind, spec)))
    for nm, spec in ext_wbasis(2, 'overlap'):
        cols.append(('gpx/overlap/%s' % nm, ('gp', 'overlap', spec)))
    for nm, spec in ext_wbasis(2, 'qfull'):
        cols.append(('qx/full/%s' % nm, ('q', 'qfull', spec)))
    # q-tower with k-indicator subranges (weights may depend on the f-slot arg)
    for rng in ('qpre', 'qover'):
        for nm, spec in ext_wbasis(2, 'qfull') + [('W' + nm, sp) for nm, sp
                                                  in _plain_wb(2)]:
            cols.append(('q_%s/%s' % (rng, nm), ('q' + rng, 'qfull', spec)))
    return cols

def _plain_wb(weight):
    out = []
    hargs = ['j', 'l', 'jl']
    atoms = [(r, 'H', a) for r in range(1, weight + 1) for a in hargs]
    res = []
    def rec(start, left, cur):
        if left == 0:
            res.append(tuple(cur))
            return
        for ai in range(start, len(atoms)):
            r, t, a = atoms[ai]
            if r <= left:
                rec(ai, left - r, cur + [(r, t, a)])
    rec(0, weight, [])
    return [(str(sp), sp) for sp in res]

def extw_col_val(spec, n, k, l):
    typ, kind, data = spec
    i2 = (P + 1) // 2
    if typ == 'g':
        a1 = b1 = 0
        for j in old_jrng(kind, n, l):
            fv = ext_weval(data, n, l, j)
            ikj = invz(k + j)
            a1 = (a1 + fv * (ikj * ikj % P)) % P
            b1 = (b1 + fv * ikj) % P
        a2 = 0
        for j in old_jrng(kind, n, k):
            fv = ext_weval(data, n, k, j)
            ilj = invz(l + j)
            a2 = (a2 + fv * (ilj * ilj % P)) % P
        return ((a1 + a2) * i2 % P, b1, 0)
    if typ == 'gp':
        a1 = b1 = 0
        for j in old_jrng('overlap', n, l):
            fv = ext_weval(data, n, l, j)
            ikj = invz(k + j)
            ikj2 = ikj * ikj % P
            a1 = (a1 + fv * (ikj2 * ikj % P)) % P
            b1 = (b1 + fv * ikj2) % P
        a2 = 0
        for j in old_jrng('overlap', n, k):
            fv = ext_weval(data, n, k, j)
            ilj = invz(l + j)
            a2 = (a2 + fv * (ilj * ilj % P * ilj % P)) % P
        return ((-(a1 + a2)) % P, (-b1) % P, 0)
    # q towers; jrange may be restricted by the f-slot variable
    def q_rng(kk):
        if typ == 'qqpre':
            return range(1, min(kk, n) + 1)
        if typ == 'qqover':
            return range(min(kk, n) + 1, n + 1)
        return range(1, n + 1)
    b = 0
    for j in q_rng(k):
        fv = ext_weval(data, n, k, j)
        ilj = invz(l + j)
        b = (b + fv * (ilj * ilj % P)) % P
    d0 = 0
    for j in q_rng(l):
        d0 = (d0 + ext_weval(data, n, l, j) * invz(k + j)) % P
    d1 = 0
    for j in q_rng(k):
        d1 = (d1 + ext_weval(data, n, k, j) * invz(l + j)) % P
    return (0, b, (d0 + d1) * i2 % P)

# ---------------------------------------------------------------- assembly ---
def build_all(cells, verbose=True):
    t0 = time.time()
    oldspec = old_columns_spec()
    salnames = []
    for rg in REGION_NAMES:
        for wn in SAL_WEIGHTS:
            salnames.append(('L0/%s/%s' % (rg, wn), rg, wn, 0, 'L'))
    for rg in REGION_NAMES:
        salnames.append(('L1/%s' % rg, rg, 'one', 1, 'L'))
    for rg in REGION_NAMES:
        for wn in SAL_WEIGHTS:
            salnames.append(('V0/%s/%s' % (rg, wn), rg, wn, 0, 'V'))
    for rg in REGION_NAMES:
        salnames.append(('V1/%s' % rg, rg, 'one', 1, 'V'))
    wi_of = {wn: i for i, wn in enumerate(SAL_WEIGHTS)}
    txspec = tx_columns_spec()
    extspec = extw_columns_spec()

    from eps22 import MON, NM, SIG
    forms = eps24.GEN_FORMS + __import__('eps25').NEWF
    Gv = np.zeros((len(forms), NM), dtype=np.int64)
    for i, f in enumerate(forms):
        Gv[i] = eps24.form_to_vec_modp(f, P)
    i2 = (P + 1) // 2
    SymG = (Gv + Gv[:, SIG]) * i2 % P

    names = ([nm for nm, _ in oldspec] + [s[0] for s in salnames]
             + [nm for nm, _ in txspec] + [nm for nm, _ in extspec]
             + ['EPS/%d' % i for i in range(len(forms))])
    lk, ll_, c2 = W.Lk(), W.Ll(), W.Cr(2)

    rowsA, rowsB, rowsD, tgt, Lks, DDs, cellinfo = [], [], [], [], [], [], []
    for ci, (n, k, l) in enumerate(cells):
        blocks = sal_cell_block(n, k, l)
        rowA, rowB, rowD = [], [], []
        for nm, spec in oldspec:
            a, b, d = old_col_val(spec, n, k, l)
            rowA.append(a); rowB.append(b); rowD.append(d)
        for nm, rg, wn, order, kindLV in salnames:
            vals = blocks[rg][0 if kindLV == 'L' else 1]
            a, b, d = fold(vals, wi_of[wn], 0, order)
            rowA.append(a); rowB.append(b); rowD.append(d)
        for nm, spec in txspec:
            a = tx_col_val(spec, n, k, l)
            rowA.append(a); rowB.append(0); rowD.append(0)
        for nm, spec in extspec:
            a, b, d = extw_col_val(spec, n, k, l)
            rowA.append(a); rowB.append(b); rowD.append(d)
        xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
        lv = {}
        for r in range(1, 6):
            for a9 in range(9):
                lv[(r, a9)] = hmod(xs[a9], r)
        mv = np.empty(NM, dtype=np.int64)
        for im, m in enumerate(MON):
            v = 1
            for la in m:
                v = v * lv[la] % P
            mv[im] = v
        av = SymG @ mv % P
        rowA.extend(int(v) for v in av)
        rowB.extend([0] * len(av)); rowD.extend([0] * len(av))
        rowsA.append(rowA); rowsB.append(rowB); rowsD.append(rowD)
        tgt.append(target_modp(n, k, l))
        Lks.append(mq(E.el_val(lk, n, k, l)))
        Lll = mq(E.el_val(ll_, n, k, l))
        C2v = mq(E.el_val(c2, n, k, l))
        DDs.append((Lks[-1] * Lll + P - C2v) % P)
        cellinfo.append((n, k, l))
        if verbose and ci % 100 == 0:
            print('  cell %d/%d %.0fs' % (ci, len(cells), time.time() - t0),
                  flush=True)
    return (np.array(rowsA, dtype=np.int64), np.array(rowsB, dtype=np.int64),
            np.array(rowsD, dtype=np.int64), tgt,
            np.array(Lks, dtype=np.int64), np.array(DDs, dtype=np.int64),
            names, cellinfo)

def assemble(rowsA, rowsB, rowsD, tgt, Lks, DDs, folded):
    if folded:
        A = (rowsA + Lks[:, None] * rowsB + DDs[:, None] * rowsD) % P
        b = np.array([(t[0] + int(Lks[i]) * t[1] + int(DDs[i]) * t[2]) % P
                      for i, t in enumerate(tgt)], dtype=np.int64)
        return A, b
    m, nc = rowsA.shape
    A = np.empty((3 * m, nc), dtype=np.int64)
    b = np.empty(3 * m, dtype=np.int64)
    A[0::3], A[1::3], A[2::3] = rowsA, rowsB, rowsD
    b[0::3] = [t[0] for t in tgt]
    b[1::3] = [t[1] for t in tgt]
    b[2::3] = [t[2] for t in tgt]
    return A, b

if __name__ == '__main__':
    cells = [(n, k, l) for n in range(1, NSOLVE + 1)
             for k in range(n + 1) for l in range(n + 1)]
    hcells = [(n, k, l) for n in (NHOLD,)
              for k in range(n + 1) for l in range(n + 1)]
    print('P=%d solve %d cells, holdout %d cells, folded=%s'
          % (P, len(cells), len(hcells), FOLDED), flush=True)
    blocks = build_all(cells)
    np.savez_compressed('sys2_%d_n%d.npz' % (P, NSOLVE),
                        A=blocks[0], B=blocks[1], D=blocks[2],
                        t=np.array(blocks[3]), Lk=blocks[4], DD=blocks[5])
    with open('sys2_%d_n%d_meta.pkl' % (P, NSOLVE), 'wb') as fh:
        pickle.dump({'names': blocks[6], 'cells': blocks[7]}, fh)
    hblocks = build_all(hcells, verbose=False)
    np.savez_compressed('sys2_%d_h%d.npz' % (P, NHOLD),
                        A=hblocks[0], B=hblocks[1], D=hblocks[2],
                        t=np.array(hblocks[3]), Lk=hblocks[4], DD=hblocks[5])
    for folded in (False, True):
        A, b = assemble(blocks[0], blocks[1], blocks[2], blocks[3],
                        blocks[4], blocks[5], folded)
        x, rk, piv, nbad = fastlin.solve(A, b, P)
        print('[folded=%s] system %s rank=%d nbad=%d'
              % (folded, A.shape, rk, nbad), flush=True)
        if nbad == 0:
            H, hb = assemble(hblocks[0], hblocks[1], hblocks[2], hblocks[3],
                             hblocks[4], hblocks[5], folded)
            resid = (H @ (x % P) - hb) % P
            nz = int(np.count_nonzero(resid))
            print('   HOLDOUT nonzero: %d of %d' % (nz, len(hb)), flush=True)
            supp = [i for i in range(A.shape[1]) if x[i] % P]
            print('   support:', len(supp))
            with open('live2_x_%d_f%d.pkl' % (P, int(folded)), 'wb') as fh:
                pickle.dump({'x': x, 'names': blocks[6]}, fh)
