"""live3.py -- round 3 on T3: the folded system with the full tower algebra.

Additions over live2:
  TX2  value towers (R_k rho)(-j) = 0 and derivative towers (R_k rho)'(-j)=0
       (region B), rho = Q-block monomials, with BOTH j-weights phi_j AND
       k-side letter multipliers phi_k (weight fill to 5).  Per-cell XS tables
       make these cheap.
  EXTW2 g/gp/q towers with n-coupled weight arguments
       {j, l, jl, jml, n+j, n-j, n+l, n-l, n+j+l} + inverse powers at
       {j, jl, n+j}.
Primary system: FOLDED single density per cell,
    f = a + L_k b + (L_k L_l - C_2) d,
which is sufficient for  Sigma T [1]W_B = -2 Sigma T w5sym  and is the only
formulation in which the target's k-free nested B-content can cancel.
"""
import sys, time, pickle
import numpy as np
from fractions import Fraction as F

import live1 as L1
from live1 import (P, HT, INV, invz, mq, hmod, old_columns_spec, old_col_val,
                   sal_cell_block, fold, REGION_NAMES, SAL_WEIGHTS,
                   target_modp, old_jrng)
import fastlin
import weights as W
import evalq as E
import eps24
from eps24 import s_mul, ESER, BLOCKS

NSOLVE = int(sys.argv[sys.argv.index('-n') + 1]) if '-n' in sys.argv else 14
NHOLD = int(sys.argv[sys.argv.index('-H') + 1]) if '-H' in sys.argv else 15

# ------------------------------------------------------------------- TX2 -----
TX_RHOS = [((), 0), (('Q1',), 1), (('Q2',), 2), (('Q1', 'Q1'), 2),
           (('Q3',), 3), (('Q1', 'Q2'), 3), (('Q1', 'Q1', 'Q1'), 3)]

def tx_cs_forms(mono):
    s_ = ESER
    for nm in mono:
        s_ = s_mul(s_, BLOCKS[nm][0])
    qlat = sum(BLOCKS[nm][1] for nm in mono)
    return {s: s_.get(2 - s, {}) for s in range(1, 2 + qlat + 1)}, qlat

TX_CS = {mono: tx_cs_forms(mono)[0] for mono, _ in TX_RHOS}
TX_QL = {mono: q for mono, q in TX_RHOS}

def phi_menu(w):
    atoms = [(1, 'H'), (2, 'H'), (3, 'H'), (1, 'i'), (2, 'i'), (3, 'i')]
    out = []
    def rec(start, left, cur):
        if left == 0:
            out.append(tuple(cur)); return
        for ai in range(start, len(atoms)):
            r, t = atoms[ai]
            if r <= left:
                rec(ai, left - r, cur + [(r, t)])
    rec(0, w, [])
    return out

PHIJ = {w: phi_menu(w) for w in range(0, 4)}
ALLPHIJ = sorted(set(sum(PHIJ.values(), [])))
PHIJ_IDX = {p: i for i, p in enumerate(ALLPHIJ)}

# k-side letter monomials (args 0:n 1:k 3:n+k 5:n-k), exact weight w
def phik_menu(w):
    letters = [(r, a) for r in range(1, w + 1) for a in (0, 1, 3, 5)]
    out = []
    def rec(start, left, cur):
        if left == 0:
            out.append(tuple(cur)); return
        for ai in range(start, len(letters)):
            r, a = letters[ai]
            if r <= left:
                rec(ai, left - r, cur + [(r, a)])
    rec(0, w, [])
    return sorted(set(out))

PHIK = {w: phik_menu(w) for w in range(0, 4)}

TX_RANGES = ['A', 'B', 'C', 'AB', 'BC', 'ABC']
def tx_range(rname, n, kk):
    return {'A': (1, kk), 'B': (kk + 1, n), 'C': (n + 1, n + kk),
            'AB': (1, n), 'BC': (kk + 1, n + kk), 'ABC': (1, n + kk)}[rname]

def tx2_columns_spec():
    cols = []
    for mono, qlat in TX_RHOS:
        for rname in TX_RANGES:
            for wj in range(0, 4 - qlat):
                for pj in PHIJ[wj]:
                    wb = qlat + 2 + wj
                    for pk in PHIK[5 - wb]:
                        cols.append(('TX[%s|%s|%s]x%s'
                                     % ('.'.join(mono) or '1', rname, pj, pk),
                                     ('V', mono, rname, pj, pk)))
    # derivative towers, region B only
    for mono, qlat in TX_RHOS:
        for wj in range(0, 3 - qlat):
            for pj in PHIJ[wj]:
                wb = qlat + 3 + wj
                for pk in PHIK[5 - wb]:
                    cols.append(('TD[%s|%s]x%s' % ('.'.join(mono) or '1',
                                                   pj, pk),
                                 ('D', mono, 'B', pj, pk)))
    return cols

def phi_val(spec, j):
    v = 1
    for (r, t) in spec:
        v = v * (hmod(j, r) if t == 'H' else pow(int(INV[j]), r, P)) % P
    return v

def eval_form_modp(form, xs):
    tot = 0
    for m, c in form.items():
        v = c.numerator % P * pow(c.denominator % P, P - 2, P) % P
        for (r, a) in m:
            v = v * hmod(xs[a], r) % P
        tot = (tot + v) % P
    return tot

class TXCell:
    """per-cell XS tables and c_s values for both orientations."""
    def __init__(self, n, k, l):
        self.n, self.k, self.l = n, k, l
        self.data = {}
        for (kk, ll) in ((k, l), (l, k)):
            xs9 = [n, kk, ll, n + kk, n + ll, n - kk, n - ll, kk + ll,
                   n + kk + ll]
            csv = {}
            for mono, qlat in TX_RHOS:
                cs = TX_CS[mono]
                csv[mono] = {s: (eval_form_modp(cs[s], xs9) if cs.get(s)
                                 else 0) for s in cs}
            XS = {}
            for rname in TX_RANGES:
                lo, hi = tx_range(rname, n, kk)
                tab = np.zeros((len(ALLPHIJ), 7), dtype=np.int64)
                for j in range(lo, hi + 1):
                    ij = invz(j + ll)
                    pv = np.array([phi_val(p, j) for p in ALLPHIJ],
                                  dtype=np.int64)
                    cur = pv.copy()
                    for s in range(1, 7):
                        cur = cur * ij % P
                        tab[:, s] = (tab[:, s] + cur) % P
                XS[rname] = tab
            # k-side letter values
            kv = {}
            for w in range(1, 4):
                for mono2 in PHIK[w]:
                    v = 1
                    for (r, a) in mono2:
                        v = v * hmod(xs9[a], r) % P
                    kv[mono2] = v
            kv[()] = 1
            self.data[(kk, ll)] = (csv, XS, kv)

    def val(self, spec):
        typ, mono, rname, pj, pk = spec
        qlat = TX_QL[mono]
        i2 = (P + 1) // 2
        tot = 0
        for ori in ((self.k, self.l), (self.l, self.k)):
            csv, XS, kv = self.data[ori]
            tab = XS[rname]
            pji = PHIJ_IDX[pj]
            u = 0
            for s in range(1, 2 + qlat + 1):
                c = csv[mono].get(s, 0)
                if not c:
                    continue
                if typ == 'V':
                    u = (u + (-1) ** s * c * int(tab[pji, s])) % P
                else:
                    u = (u + s * (-1) ** s * c * int(tab[pji, s + 1])) % P
            tot = (tot + u * kv[pk]) % P
        return tot * i2 % P

# ------------------------------------------------------------------ EXTW2 ----
def ext2_wbasis(weight, kind):
    hargs = ['j', 'l', 'jl', 'nj', 'nmj', 'nl', 'nml', 'njl'] + (
        ['jml'] if kind == 'overlap' else [])
    iargs = ['j', 'jl', 'nj']
    atoms = []
    for r in range(1, weight + 1):
        for a in hargs:
            atoms.append((r, 'H', a))
        for a in iargs:
            atoms.append((r, 'i', a))
    out = []
    def rec(start, left, cur):
        if left == 0:
            out.append(tuple(cur)); return
        for ai in range(start, len(atoms)):
            r, t, a = atoms[ai]
            if r <= left:
                rec(ai, left - r, cur + [(r, t, a)])
    rec(0, weight, [])
    return [(str(sp), sp) for sp in out]

def ext2_weval(spec, n, l, j):
    v = 1
    for (r, t, a) in spec:
        x = {'j': j, 'l': l, 'jl': j + l, 'jml': j - l, 'nj': n + j,
             'nmj': n - j, 'nl': n + l, 'nml': n - l, 'njl': n + j + l}[a]
        if t == 'H':
            v = v * hmod(x, r) % P
        else:
            v = v * pow(invz(x), r, P) % P
    return v

def extw2_columns_spec():
    cols = []
    for kind in ('prefix', 'overlap', 'full'):
        for nm, spec in ext2_wbasis(3, kind):
            cols.append(('g2/%s/%s' % (kind, nm), ('g', kind, spec)))
    for nm, spec in ext2_wbasis(2, 'overlap'):
        cols.append(('gp2/overlap/%s' % nm, ('gp', 'overlap', spec)))
    for nm, spec in ext2_wbasis(2, 'qfull'):
        cols.append(('q2/full/%s' % nm, ('q', 'qfull', spec)))
    return cols

def extw2_col_val(spec, n, k, l):
    typ, kind, data = spec
    i2 = (P + 1) // 2
    if typ == 'g':
        a1 = b1 = 0
        for j in old_jrng(kind, n, l):
            fv = ext2_weval(data, n, l, j)
            ikj = invz(k + j)
            a1 = (a1 + fv * (ikj * ikj % P)) % P
            b1 = (b1 + fv * ikj) % P
        a2 = 0
        for j in old_jrng(kind, n, k):
            fv = ext2_weval(data, n, k, j)
            ilj = invz(l + j)
            a2 = (a2 + fv * (ilj * ilj % P)) % P
        return ((a1 + a2) * i2 % P, b1, 0)
    if typ == 'gp':
        a1 = b1 = 0
        for j in old_jrng('overlap', n, l):
            fv = ext2_weval(data, n, l, j)
            ikj = invz(k + j)
            ikj2 = ikj * ikj % P
            a1 = (a1 + fv * (ikj2 * ikj % P)) % P
            b1 = (b1 + fv * ikj2) % P
        a2 = 0
        for j in old_jrng('overlap', n, k):
            fv = ext2_weval(data, n, k, j)
            ilj = invz(l + j)
            a2 = (a2 + fv * (ilj * ilj % P * ilj % P)) % P
        return ((-(a1 + a2)) % P, (-b1) % P, 0)
    b = 0
    for j in range(1, n + 1):
        fv = ext2_weval(data, n, k, j)
        ilj = invz(l + j)
        b = (b + fv * (ilj * ilj % P)) % P
    d0 = 0
    for j in range(1, n + 1):
        d0 = (d0 + ext2_weval(data, n, l, j) * invz(k + j)) % P
    d1 = 0
    for j in range(1, n + 1):
        d1 = (d1 + ext2_weval(data, n, k, j) * invz(l + j)) % P
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
    txspec = tx2_columns_spec()
    extspec = extw2_columns_spec()

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
    print('columns: OLD %d SAL %d TX2 %d EXTW2 %d EPS %d = %d'
          % (len(oldspec), len(salnames), len(txspec), len(extspec),
             len(forms), len(names)), flush=True)
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
        txc = TXCell(n, k, l)
        for nm, spec in txspec:
            rowA.append(txc.val(spec)); rowB.append(0); rowD.append(0)
        for nm, spec in extspec:
            a, b, d = extw2_col_val(spec, n, k, l)
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
        Lkv = mq(E.el_val(lk, n, k, l))
        Llv = mq(E.el_val(ll_, n, k, l))
        C2v = mq(E.el_val(c2, n, k, l))
        Lks.append(Lkv); DDs.append((Lkv * Llv + P - C2v) % P)
        cellinfo.append((n, k, l))
        if verbose and ci % 100 == 0:
            print('  cell %d/%d %.0fs' % (ci, len(cells), time.time() - t0),
                  flush=True)
    return (np.array(rowsA, dtype=np.int64), np.array(rowsB, dtype=np.int64),
            np.array(rowsD, dtype=np.int64), tgt,
            np.array(Lks, dtype=np.int64), np.array(DDs, dtype=np.int64),
            names, cellinfo)

def assemble(blocks, folded):
    rowsA, rowsB, rowsD, tgt, Lks, DDs = blocks[:6]
    if folded:
        A = (rowsA + Lks[:, None] * rowsB % P + DDs[:, None] * rowsD % P) % P
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
    if '--null' in sys.argv:
        txs = tx2_columns_spec()
        exs = extw2_columns_spec()
        print('TX2 %d EXTW2 %d' % (len(txs), len(exs)))
        lk, ll_, c2 = W.Lk(), W.Ll(), W.Cr(2)
        bad = []
        for n in (3, 4):
            accT = [0] * len(txs); accE = [0] * len(exs)
            for k in range(n + 1):
                for l in range(n + 1):
                    T = E.T(n, k, l) % P
                    Lk = mq(E.el_val(lk, n, k, l))
                    Ll = mq(E.el_val(ll_, n, k, l))
                    C2 = mq(E.el_val(c2, n, k, l))
                    DD = (Lk * Ll + P - C2) % P
                    txc = TXCell(n, k, l)
                    for i, (nm, spec) in enumerate(txs):
                        accT[i] = (accT[i] + T * txc.val(spec)) % P
                    for i, (nm, spec) in enumerate(exs):
                        a, b, d = extw2_col_val(spec, n, k, l)
                        accE[i] = (accE[i] + T * ((a + Lk * b + DD * d) % P)) % P
            bt = [txs[i][0] for i, v in enumerate(accT) if v % P]
            be = [exs[i][0] for i, v in enumerate(accE) if v % P]
            print('n=%d TX2 bad %d/%d EXTW2 bad %d/%d' % (n, len(bt), len(txs),
                                                          len(be), len(exs)))
            if bt: print('  ', bt[:6])
            if be: print('  ', be[:6])
            bad += bt + be
        print('NULLCHECK3:', 'PASS' if not bad else 'FAIL')
        sys.exit(0)

    cells = [(n, k, l) for n in range(1, NSOLVE + 1)
             for k in range(n + 1) for l in range(n + 1)]
    hcells = [(n, k, l) for n in (NHOLD,)
              for k in range(n + 1) for l in range(n + 1)]
    print('P=%d solve %d cells, holdout %d cells' % (P, len(cells),
                                                     len(hcells)), flush=True)
    blocks = build_all(cells)
    hblocks = build_all(hcells, verbose=False)
    with open('live3_blocks_n%d.pkl' % NSOLVE, 'wb') as fh:
        pickle.dump({'names': blocks[6], 'cells': blocks[7]}, fh)
    np.savez_compressed('sys3_%d_n%d.npz' % (P, NSOLVE),
                        A=blocks[0], B=blocks[1], D=blocks[2],
                        t=np.array(blocks[3]), Lk=blocks[4], DD=blocks[5])
    np.savez_compressed('sys3_%d_h%d.npz' % (P, NHOLD),
                        A=hblocks[0], B=hblocks[1], D=hblocks[2],
                        t=np.array(hblocks[3]), Lk=hblocks[4], DD=hblocks[5])
    modes = (True,) if '--foldedonly' in sys.argv else (True, False)
    for folded in modes:
        A, b = assemble(blocks, folded)
        x, rk, piv, nbad = fastlin.solve(A, b, P)
        print('[folded=%s] system %s rank=%d nbad=%d (deprows=%d)'
              % (folded, A.shape, rk, nbad, A.shape[0] - rk), flush=True)
        if nbad == 0:
            H, hb = assemble(hblocks, folded)
            resid = (H @ (x % P) - hb) % P
            nz = int(np.count_nonzero(resid))
            print('   HOLDOUT nonzero: %d of %d' % (nz, len(hb)), flush=True)
            if nz == 0:
                supp = [i for i in range(A.shape[1]) if x[i] % P]
                print('   support:', len(supp))
                with open('live3_x_%d_f%d.pkl' % (P, int(folded)), 'wb') as fh:
                    pickle.dump({'x': x, 'names': blocks[6]}, fh)
