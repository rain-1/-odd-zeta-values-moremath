"""live1.py -- THE COMBINED LAURENT+JETS SHOT AT T3 (rational/weight-5 bridge).

Target, in canonical (a,b,d) density components against (A_kl, B_kl, D_kl):
    a = r22(k,l) + 2*w5sym(n,k,l),   b = 2*r12(k,l),   d = r11(k,l).
A solution x with  target = sum_i x_i * column_i  cellwise, with all columns
proved-null functionals, proves  Sigma T [1]W_B = -2 Sigma T w5sym  and hence
(with the subtraction anchor)  P_n = Sigma T w5.

Columns:
  OLD  g/g'/q zero facts + R/Rx lattice facts     (search_t3zeros.columns)
  SAL  Laurent/Vertical band coefficients of R(x,m-x)=0, R(x,j)=0
  EPS  eps24+eps25 pole-raising jet forms as A-only null densities.

All evaluation is mod p (fast reimplementation, cross-checked in --check mode
against the exact Fraction implementations).  Discovery only; a hit must be
reconstructed exactly and each column family carries its own residue proof.
"""
import sys, time, pickle
import numpy as np
from fractions import Fraction as F

ROOT = '/home/ubuntu/fable-episode-2/zeta-math-2/work'
for d in ('z5ord0', 'z5la', 'z5barnes', 'z5eps', 'lb5'):
    sys.path.insert(0, ROOT + '/' + d)

import fastlin
import t_euler as TE
import weights as W
import evalq as E

P = int(sys.argv[sys.argv.index('-p') + 1]) if '-p' in sys.argv else 4194301
NSOLVE = int(sys.argv[sys.argv.index('-n') + 1]) if '-n' in sys.argv else 9
NHOLD = ((int(sys.argv[sys.argv.index('-H') + 1]),) if '-H' in sys.argv
         else (NSOLVE + 1,))
CHECK = '--check' in sys.argv

# ---------------------------------------------------------------- mod-p tables
MMAX = 400
HT = np.zeros((6, MMAX + 1), dtype=np.int64)     # HT[r][m] = H^(r)_m mod P
INV = np.zeros(MMAX + 1, dtype=np.int64)
for m in range(1, MMAX + 1):
    INV[m] = pow(m, P - 2, P)
    acc = INV[m]
    HT[1][m] = (HT[1][m - 1] + acc) % P
    for r in range(2, 6):
        acc = acc * INV[m] % P
        HT[r][m] = (HT[r][m - 1] + acc) % P

_invc = {}
def invz(x):
    """inverse mod P of a (possibly negative) nonzero int"""
    v = _invc.get(x)
    if v is None:
        v = pow(x % P, P - 2, P)
        _invc[x] = v
    return v

def mq(fr):
    fr = F(fr)
    return fr.numerator % P * pow(fr.denominator % P, P - 2, P) % P

def hmod(x, r=1):
    return int(HT[r][max(x, 0)])

# ---------------------------------------------------------------- SAL regions
def region_points(name, n):
    pts = []
    if name == 'all':
        pts = [(t, m) for t in range(n + 1) for m in range(1, n + 1)]
    elif name == 'tle':
        pts = [(t, m) for t in range(n + 1) for m in range(1, n + 1) if t <= m]
    elif name == 'tlt':
        pts = [(t, m) for t in range(n + 1) for m in range(1, n + 1) if t < m]
    elif name == 'tge':
        pts = [(t, m) for t in range(n + 1) for m in range(1, n + 1) if t >= m]
    elif name == 'tgt':
        pts = [(t, m) for t in range(n + 1) for m in range(1, n + 1) if t > m]
    elif name == 'sumle':
        pts = [(t, m) for t in range(n + 1) for m in range(1, n + 1) if t + m <= n]
    elif name == 'sumlt':
        pts = [(t, m) for t in range(n + 1) for m in range(1, n + 1) if t + m < n]
    elif name == 'sumge':
        pts = [(t, m) for t in range(n + 1) for m in range(1, n + 1) if t + m >= n]
    elif name == 'sumgt':
        pts = [(t, m) for t in range(n + 1) for m in range(1, n + 1) if t + m > n]
    elif name.startswith('sumle') or name.startswith('sumeq') or \
            name.startswith('tle_sumle') or name.startswith('tge_sumle'):
        c = int(name[name.rfind('e') + 1:]) if False else None
    if pts or name in ('all', 'tle', 'tlt', 'tge', 'tgt',
                       'sumle', 'sumlt', 'sumge', 'sumgt'):
        return pts
    # parametrised families
    if name[:5] == 'sumle' and ('+' in name or '-' in name[5:]):
        c = int(name[5:])
        return [(t, m) for t in range(n + 1) for m in range(1, n + 1)
                if t + m <= n + c]
    if name[:5] == 'sumeq':
        c = int(name[5:])
        return [(t, m) for t in range(n + 1) for m in range(1, n + 1)
                if t + m == n + c]
    if name[:9] == 'tle_sumle':
        c = int(name[9:])
        return [(t, m) for t in range(n + 1) for m in range(1, n + 1)
                if t <= m and t + m <= n + c]
    if name[:9] == 'tge_sumle':
        c = int(name[9:])
        return [(t, m) for t in range(n + 1) for m in range(1, n + 1)
                if t >= m and t + m <= n + c]
    raise KeyError(name)

REGION_NAMES = ['all', 'tle', 'tlt', 'tge', 'tgt',
                'sumle', 'sumlt', 'sumge', 'sumgt']
for _c in range(-4, 5):
    REGION_NAMES += ['sumle%+d' % _c, 'sumeq%+d' % _c,
                     'tle_sumle%+d' % _c, 'tge_sumle%+d' % _c]

# SAL weight list, order replicated exactly (16 entries incl. inv_m duplicate)
def sal_weight_vec(name, n, T_, M_):
    """values mod P on region points (int64 arrays T_, M_)."""
    if name == 'one':
        return np.ones(len(T_), dtype=np.int64)
    if name.startswith('H_'):
        arg = name[2:]
        x = {'t': T_, 'm': M_, 'tm': T_ + M_, 'n': np.full(len(T_), n),
             'nt': n + T_, 'nm': n + M_, 'nmt': n - T_, 'nmm': n - M_,
             'ntm': n + T_ + M_}[arg]
        return HT[1][np.maximum(x, 0)]
    if name.startswith('inv_'):
        arg = name[4:]
        x = {'m': M_, 'tm': T_ + M_, 'n': np.full(len(T_), n),
             'nm': n + M_, 'ntm': n + T_ + M_}[arg]
        return INV[x]
    raise KeyError(name)

SAL_WEIGHTS = (['one', 'H_t', 'H_m', 'H_tm', 'H_n', 'inv_m', 'inv_tm']
               + ['H_nt', 'H_nm', 'H_nmt', 'H_nmm', 'H_ntm']
               + ['inv_n', 'inv_m', 'inv_nm', 'inv_ntm'])
NW = len(SAL_WEIGHTS)

def sal_cell_block(n, k, l):
    """returns dict (regionname) -> (16x16 arrays) of weighted sums.

    For each region: rows = weights, cols = the 8 coef types x 2 orientations:
      [A0,B0,C0,D0,A1,B1,C1,D1] for orientation (k,l) then (l,k)  -> 16 cols
    Laurent semantics (with special row t==kk), plus 8 more columns for
    Vertical semantics -> total 24 cols per orientation? no: vertical shares
    the same (t,m)->(t,j) point set; returns second 16-col array.
    """
    out = {}
    for rg in REGION_NAMES:
        pts = region_points(rg, n)
        if not pts:
            out[rg] = (np.zeros((NW, 16), dtype=np.int64),
                       np.zeros((NW, 16), dtype=np.int64))
            continue
        T_ = np.array([p[0] for p in pts], dtype=np.int64)
        M_ = np.array([p[1] for p in pts], dtype=np.int64)
        L = len(pts)
        wmat = np.empty((NW, L), dtype=np.int64)
        for i, wn in enumerate(SAL_WEIGHTS):
            wmat[i] = sal_weight_vec(wn, n, T_, M_)
        coefL = np.zeros((L, 16), dtype=np.int64)
        coefV = np.zeros((L, 16), dtype=np.int64)
        for oi, (kk, ll) in enumerate(((k, l), (l, k))):
            base = 8 * oi
            e = M_ + T_ + ll                      # >= 1 always
            ie = INV[e]
            ie2 = ie * ie % P
            ie3 = ie2 * ie % P
            ie4 = ie2 * ie2 % P
            ie5 = ie4 * ie % P
            q = kk - T_
            spec = (q == 0)
            gen = ~spec
            iq = np.zeros(L, dtype=np.int64)
            iq[gen] = np.array([invz(int(v)) for v in q[gen]], dtype=np.int64)
            iq2 = iq * iq % P
            iq3 = iq2 * iq % P
            # Laurent order 0
            coefL[gen, base + 0] = iq2[gen] * ie2[gen] % P            # A
            coefL[gen, base + 1] = iq[gen] * ie2[gen] % P             # B
            coefL[gen, base + 2] = iq2[gen] * ie[gen] % P             # C
            coefL[gen, base + 3] = iq[gen] * ie[gen] % P              # D
            coefL[spec, base + 0] = 3 * ie4[spec] % P
            coefL[spec, base + 1] = 2 * ie3[spec] % P
            coefL[spec, base + 2] = ie3[spec]
            coefL[spec, base + 3] = ie2[spec]
            # Laurent order 1:  -a/q^{a+1}e^b + b/q^a e^{b+1}
            coefL[gen, base + 4] = ((-2 * iq3[gen] % P) * ie2[gen]
                                    + 2 * iq2[gen] * ie3[gen]) % P    # A
            coefL[gen, base + 5] = ((-iq2[gen] % P) * ie2[gen]
                                    + 2 * iq[gen] * ie3[gen]) % P     # B
            coefL[gen, base + 6] = ((-2 * iq3[gen] % P) * ie[gen]
                                    + iq2[gen] * ie2[gen]) % P        # C
            coefL[gen, base + 7] = ((-iq2[gen] % P) * ie[gen]
                                    + iq[gen] * ie2[gen]) % P         # D
            coefL[spec, base + 4] = 4 * ie5[spec] % P
            coefL[spec, base + 5] = 3 * ie4[spec] % P
            coefL[spec, base + 6] = ie4[spec]
            coefL[spec, base + 7] = ie3[spec]
            # Vertical: e = j + ll, skip t==kk entirely
            ev = M_ + ll
            iev = INV[ev]
            iev2 = iev * iev % P
            coefV[gen, base + 0] = iq2[gen] * iev2[gen] % P
            coefV[gen, base + 1] = iq[gen] * iev2[gen] % P
            coefV[gen, base + 2] = iq2[gen] * iev[gen] % P
            coefV[gen, base + 3] = iq[gen] * iev[gen] % P
            coefV[gen, base + 4] = (-2 * iq3[gen] % P) * iev2[gen] % P
            coefV[gen, base + 5] = (-iq2[gen] % P) * iev2[gen] % P
            coefV[gen, base + 6] = (-2 * iq3[gen] % P) * iev[gen] % P
            coefV[gen, base + 7] = (-iq2[gen] % P) * iev[gen] % P
        out[rg] = ((wmat @ (coefL % P)) % P, (wmat @ (coefV % P)) % P)
    return out

def fold(vals, wi, o0, kind):
    """vals: (NW x 16); build (a,b,d) canonical components for weight wi.
    kind 0 -> order 0, kind 1 -> order 1.
    columns [A,B,C,D] at base 0 (orient kl) and 8 (orient lk), +4 if order 1"""
    off = 4 * kind
    A1 = int(vals[wi, off + 0]); A2 = int(vals[wi, 8 + off + 0])
    B1 = int(vals[wi, off + 1]); C2 = int(vals[wi, 8 + off + 2])
    D1 = int(vals[wi, off + 3]); D2 = int(vals[wi, 8 + off + 3])
    i2 = (P + 1) // 2
    return ((A1 + A2) * i2 % P, (B1 + C2) % P, (D1 + D2) * i2 % P)

# ------------------------------------------------------------- OLD columns ---
def old_wbasis(weight, kind):
    aa = ['j', 'l', 'jl'] + (['jml'] if kind == 'overlap' else [])
    out = []
    for a in aa:
        out.append(('H%d_%s' % (weight, a), [(weight, a)]))
    if weight >= 2:
        for a in aa:
            for b in aa:
                out.append(('H1_%s*H%d_%s' % (a, weight - 1, b),
                            [(1, a), (weight - 1, b)]))
    if weight == 3:
        for ia, a in enumerate(aa):
            for ib in range(ia, len(aa)):
                b = aa[ib]
                for ic in range(ib, len(aa)):
                    c = aa[ic]
                    out.append(('H1_%s*H1_%s*H1_%s' % (a, b, c),
                                [(1, a), (1, b), (1, c)]))
    seen = set()
    return [(nm, sp) for nm, sp in out if not (nm in seen or seen.add(nm))]

def old_weval(spec, n, l, j):
    v = 1
    for (r, a) in spec:
        x = {'j': j, 'l': l, 'jl': j + l, 'jml': j - l}[a]
        v = v * hmod(x, r) % P
    return v

def old_jrng(kind, n, l):
    if kind == 'prefix':
        return range(1, l + 1)
    if kind == 'overlap':
        return range(l + 1, n + 1)
    if kind == 'full':
        return range(1, n + l + 1)
    if kind == 'qfull':
        return range(1, n + 1)
    raise KeyError(kind)

def old_columns_spec():
    cols = []
    for kind in ('prefix', 'overlap', 'full'):
        for nm, spec in old_wbasis(3, kind):
            cols.append(('g/%s/%s' % (kind, nm), ('g', kind, spec)))
    for nm, spec in old_wbasis(2, 'overlap'):
        cols.append(('gp/overlap/%s' % nm, ('gp', 'overlap', spec)))
    for nm, spec in old_wbasis(2, 'qfull'):
        cols.append(('q/full/%s' % nm, ('q', 'qfull', spec)))
    regions = ['square', 'lower', 'strict', 'diag']
    f1s = ['H1_i', 'H1_j', 'H1_ij', 'H1_n', 'inv_i', 'inv_j', 'inv_ij']
    for rg in regions:
        for nm in f1s:
            cols.append(('R/%s/%s' % (rg, nm), ('R', rg, nm)))
        cols.append(('Rx/%s' % rg, ('Rx', rg, 'one')))
    return cols

def old_rpoints(rg, n):
    if rg == 'square':
        return [(i, j) for i in range(1, n + 1) for j in range(1, n + 1)]
    if rg == 'lower':
        return [(i, j) for i in range(1, n + 1) for j in range(i, n + 1)]
    if rg == 'strict':
        return [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]
    if rg == 'diag':
        return [(i, i) for i in range(1, n + 1)]
    raise KeyError(rg)

def old_f1(nm, n, i, j):
    if nm == 'H1_i':
        return hmod(i)
    if nm == 'H1_j':
        return hmod(j)
    if nm == 'H1_ij':
        return hmod(i + j)
    if nm == 'H1_n':
        return hmod(n)
    if nm == 'inv_i':
        return int(INV[i])
    if nm == 'inv_j':
        return int(INV[j])
    if nm == 'inv_ij':
        return int(INV[i + j])
    if nm == 'one':
        return 1
    raise KeyError(nm)

def old_col_val(spec, n, k, l):
    i2 = (P + 1) // 2
    typ, kind, data = spec
    if typ == 'g':
        a1 = b1 = 0
        for j in old_jrng(kind, n, l):
            fv = old_weval(data, n, l, j)
            ikj = invz(k + j)
            a1 = (a1 + fv * (ikj * ikj % P)) % P
            b1 = (b1 + fv * ikj) % P
        a2 = 0
        for j in old_jrng(kind, n, k):
            fv = old_weval(data, n, k, j)
            ilj = invz(l + j)
            a2 = (a2 + fv * (ilj * ilj % P)) % P
        return ((a1 + a2) * i2 % P, b1, 0)
    if typ == 'gp':
        a1 = b1 = 0
        for j in old_jrng('overlap', n, l):
            fv = old_weval(data, n, l, j)
            ikj = invz(k + j)
            ikj2 = ikj * ikj % P
            a1 = (a1 + fv * (ikj2 * ikj % P)) % P
            b1 = (b1 + fv * ikj2) % P
        a2 = 0
        for j in old_jrng('overlap', n, k):
            fv = old_weval(data, n, k, j)
            ilj = invz(l + j)
            a2 = (a2 + fv * (ilj * ilj % P * ilj % P)) % P
        return ((-(a1 + a2)) % P, (-b1) % P, 0)
    if typ == 'q':
        b = 0
        for j in old_jrng('qfull', n, k):
            fv = old_weval(data, n, k, j)
            ilj = invz(l + j)
            b = (b + fv * (ilj * ilj % P)) % P
        d0 = 0
        for j in old_jrng('qfull', n, l):
            d0 = (d0 + old_weval(data, n, l, j) * invz(k + j)) % P
        d1 = 0
        for j in old_jrng('qfull', n, k):
            d1 = (d1 + old_weval(data, n, k, j) * invz(l + j)) % P
        return (0, b, (d0 + d1) * i2 % P)
    # R / Rx
    def raw(kk, ll):
        aa = bb = cc = dd = 0
        for (i, j) in old_rpoints(kind, n):
            z = old_f1(data, n, i, j)
            iki = invz(kk + i)
            ilj = invz(ll + j)
            iki2 = iki * iki % P
            ilj2 = ilj * ilj % P
            if typ == 'R':
                aa = (aa + z * (iki2 * ilj2 % P)) % P
                bb = (bb + z * (iki * ilj2 % P)) % P
                cc = (cc + z * (iki2 * ilj % P)) % P
                dd = (dd + z * (iki * ilj % P)) % P
            else:
                iki3 = iki2 * iki % P
                aa = (aa - 2 * z * (iki3 * ilj2 % P)) % P
                bb = (bb - z * (iki2 * ilj2 % P)) % P
                cc = (cc - 2 * z * (iki3 * ilj % P)) % P
                dd = (dd - z * (iki2 * ilj % P)) % P
        return aa % P, bb % P, cc % P, dd % P
    aa, bb, cc, dd = raw(k, l)
    aa2, bb2, cc2, dd2 = raw(l, k)
    return ((aa + aa2) * i2 % P, (bb + cc2) % P, (dd + dd2) * i2 % P)

# ---------------------------------------------------------------- target -----
W5S = W.compact_w5sym()
def target_modp(n, k, l):
    a = mq(TE.r22_fit(k, l)) + 2 * mq(E.el_val(W5S, n, k, l))
    b = 2 * mq(TE.r12_fit(k, l))
    d = mq(TE.r11_fit(k, l))
    return a % P, b % P, d % P

# ---------------------------------------------------------------- main -------
def build_system(cells, eps=True, verbose=True):
    t0 = time.time()
    oldspec = old_columns_spec()
    salnames = []
    for rg in REGION_NAMES:
        for wn in SAL_WEIGHTS:
            salnames.append(('Laurent0/%s/%s' % (rg, wn), rg, wn, 0, 'L'))
    for rg in REGION_NAMES:
        salnames.append(('Laurent1/%s' % rg, rg, 'one', 1, 'L'))
    for rg in REGION_NAMES:
        for wn in SAL_WEIGHTS:
            salnames.append(('Vertical0/%s/%s' % (rg, wn), rg, wn, 0, 'V'))
    for rg in REGION_NAMES:
        salnames.append(('Vertical1/%s' % rg, rg, 'one', 1, 'V'))
    wi_of = {wn: i for i, wn in enumerate(SAL_WEIGHTS)}
    # NB duplicate 'inv_m' -> same index twice; harmless duplicate column.

    names = [nm for nm, _ in oldspec] + [s[0] for s in salnames]

    eps_block = None
    if eps:
        import eps24, eps25
        from eps22 import MON, MIDX, NM, SIG
        forms = eps24.GEN_FORMS + eps25.NEWF
        enames = eps24.GEN_NAMES + eps25.NEWN
        Gv = np.zeros((len(forms), NM), dtype=np.int64)
        for i, f in enumerate(forms):
            Gv[i] = eps24.form_to_vec_modp(f, P)
        i2 = (P + 1) // 2
        SymG = (Gv + Gv[:, SIG]) * i2 % P
        names += ['EPS/' + nm for nm in enames]
        # monomial values per cell
        def monvals(n, k, l):
            xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
            lv = {}
            for r in range(1, 6):
                for a in range(9):
                    lv[(r, a)] = hmod(xs[a], r)
            out = np.empty(NM, dtype=np.int64)
            for i, m in enumerate(MON):
                v = 1
                for la in m:
                    v = v * lv[la] % P
                out[i] = v
            return out
        eps_block = (SymG, monvals)
        if verbose:
            print('eps forms:', len(forms), flush=True)

    rows, rhs, rowinfo = [], [], []
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
        if eps_block is not None:
            SymG, monvals = eps_block
            mv = monvals(n, k, l)
            av = SymG @ mv % P
            rowA.extend(int(v) for v in av)
            rowB.extend([0] * len(av))
            rowD.extend([0] * len(av))
        ta, tb, td = target_modp(n, k, l)
        rows.append(rowA); rhs.append(ta); rowinfo.append((n, k, l, 'a'))
        rows.append(rowB); rhs.append(tb); rowinfo.append((n, k, l, 'b'))
        rows.append(rowD); rhs.append(td); rowinfo.append((n, k, l, 'd'))
        if verbose and ci % 50 == 0:
            print('  cells %d/%d  %.0fs' % (ci, len(cells), time.time() - t0),
                  flush=True)
    return (np.array(rows, dtype=np.int64), np.array(rhs, dtype=np.int64),
            names, rowinfo)

def crosscheck():
    """compare fast mod-p columns against the exact Fraction implementations"""
    import random
    import os
    cwd = os.getcwd()
    os.chdir(ROOT + '/z5barnes')
    sys.path.insert(0, ROOT + '/z5barnes')
    import search_t3zeros as OLDX
    import search_antidiag_laurent as SALX
    os.chdir(cwd)
    random.seed(7)
    cells = [(n, random.randint(0, n), random.randint(0, n))
             for n in (2, 3, 4, 5) for _ in range(2)]
    # OLD columns
    oc_exact = OLDX.columns()
    oc_fast = old_columns_spec()
    assert len(oc_exact) == len(oc_fast), (len(oc_exact), len(oc_fast))
    idxs = random.sample(range(len(oc_fast)), 12)
    bad = 0
    for i in idxs:
        nm_f = oc_fast[i][0]
        nm_e = oc_exact[i][0]
        assert nm_f == nm_e, (nm_f, nm_e)
        for (n, k, l) in cells[:4]:
            ex = oc_exact[i][1](n, k, l)
            fa = old_col_val(oc_fast[i][1], n, k, l)
            exm = tuple(mq(v) for v in ex)
            if exm != tuple(int(v) % P for v in fa):
                print('OLD MISMATCH', nm_f, (n, k, l), exm, fa)
                bad += 1
    print('OLD crosscheck: %s' % ('PASS' if bad == 0 else 'FAIL %d' % bad))
    # SAL columns
    sal_exact = ([('Laurent0/%s/%s' % (rg, nm), SALX.column(rg, wt))
                  for rg in SALX.REGIONS for nm, wt in SALX.WEIGHTS]
                 + [('Laurent1/%s' % rg,
                     SALX.column(rg, lambda n, t, m: F(1), 1))
                    for rg in SALX.REGIONS]
                 + [('Vertical0/%s/%s' % (rg, nm),
                     SALX.column_vertical(rg, wt))
                    for rg in SALX.REGIONS for nm, wt in SALX.WEIGHTS]
                 + [('Vertical1/%s' % rg,
                     SALX.column_vertical(rg, lambda n, t, j: F(1), 1))
                    for rg in SALX.REGIONS])
    # my ordering
    mine = []
    for rg in REGION_NAMES:
        for wn in SAL_WEIGHTS:
            mine.append(('Laurent0/%s/%s' % (rg, wn), rg, wn, 0, 'L'))
    for rg in REGION_NAMES:
        mine.append(('Laurent1/%s' % rg, rg, 'one', 1, 'L'))
    for rg in REGION_NAMES:
        for wn in SAL_WEIGHTS:
            mine.append(('Vertical0/%s/%s' % (rg, wn), rg, wn, 0, 'V'))
    for rg in REGION_NAMES:
        mine.append(('Vertical1/%s' % rg, rg, 'one', 1, 'V'))
    assert len(sal_exact) == len(mine), (len(sal_exact), len(mine))
    wi_of = {wn: i for i, wn in enumerate(SAL_WEIGHTS)}
    idxs = random.sample(range(len(mine)), 16)
    bad = 0
    for i in idxs:
        nm_e = sal_exact[i][0]
        nm_f, rg, wn, order, kindLV = mine[i]
        # names may differ (weight naming); rely on position
        for (n, k, l) in cells[:3]:
            ex = sal_exact[i][1](n, k, l)
            blocks = sal_cell_block(n, k, l)
            vals = blocks[rg][0 if kindLV == 'L' else 1]
            fa = fold(vals, wi_of[wn], 0, order)
            exm = tuple(mq(v) for v in ex)
            if exm != tuple(int(v) % P for v in fa):
                print('SAL MISMATCH', nm_e, nm_f, (n, k, l), exm, fa)
                bad += 1
    print('SAL crosscheck: %s' % ('PASS' if bad == 0 else 'FAIL %d' % bad))

def nullcheck(nvals=(3, 4, 5), neps=40):
    """Sigma_{k,l} T [a + L_k b + (L_kL_l-C2) d] must be 0 for every column
    (they are null functionals) and for the TARGET (T3 is true numerically)."""
    import eps24, eps25
    from eps22 import MON, SIG, NM
    lk, ll, c2 = W.Lk(), W.Ll(), W.Cr(2)
    oldspec = old_columns_spec()
    salnames = []
    for rg in REGION_NAMES:
        for wn in SAL_WEIGHTS:
            salnames.append((rg, wn, 0, 'L'))
    for rg in REGION_NAMES:
        salnames.append((rg, 'one', 1, 'L'))
    for rg in REGION_NAMES:
        for wn in SAL_WEIGHTS:
            salnames.append((rg, wn, 0, 'V'))
    for rg in REGION_NAMES:
        salnames.append((rg, 'one', 1, 'V'))
    wi_of = {wn: i for i, wn in enumerate(SAL_WEIGHTS)}
    forms = eps24.GEN_FORMS + eps25.NEWF
    import random
    random.seed(11)
    esel = random.sample(range(len(forms)), neps)
    Gsel = np.zeros((neps, NM), dtype=np.int64)
    for ii, fi in enumerate(esel):
        Gsel[ii] = eps24.form_to_vec_modp(forms[fi], P)
    i2 = (P + 1) // 2
    GselS = (Gsel + Gsel[:, SIG]) * i2 % P
    bad = set()
    tgt_bad = 0
    for n in nvals:
        accO = [0] * len(oldspec)
        accS = [0] * len(salnames)
        accE = [0] * neps
        accT = 0
        for k in range(n + 1):
            for l in range(n + 1):
                T = E.T(n, k, l) % P
                Lk = mq(E.el_val(lk, n, k, l))
                LL = mq(E.el_val(ll, n, k, l))
                C2 = mq(E.el_val(c2, n, k, l))
                DD = (Lk * LL + P - C2) % P
                blocks = sal_cell_block(n, k, l)
                for i, (nm, spec) in enumerate(oldspec):
                    a, b, d = old_col_val(spec, n, k, l)
                    accO[i] = (accO[i] + T * ((a + Lk * b + DD * d) % P)) % P
                for i, (rg, wn, order, kd) in enumerate(salnames):
                    vals = blocks[rg][0 if kd == 'L' else 1]
                    a, b, d = fold(vals, wi_of[wn], 0, order)
                    accS[i] = (accS[i] + T * ((a + Lk * b + DD * d) % P)) % P
                # eps
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
                ev = GselS @ mv % P
                for i in range(neps):
                    accE[i] = (accE[i] + T * int(ev[i])) % P
                ta, tb, td = target_modp(n, k, l)
                accT = (accT + T * ((ta + Lk * tb + DD * td) % P)) % P
        bo = [i for i, v in enumerate(accO) if v % P]
        bs = [i for i, v in enumerate(accS) if v % P]
        be = [i for i, v in enumerate(accE) if v % P]
        print('n=%d: OLD bad %d/%d, SAL bad %d/%d, EPS bad %d/%d, target %s'
              % (n, len(bo), len(accO), len(bs), len(accS), len(be), neps,
                 'ZERO' if accT % P == 0 else 'NONZERO(%d)' % accT), flush=True)
        if bs:
            print('   SAL bad first10:', [salnames[i] for i in bs[:10]])
        if bo:
            print('   OLD bad first10:', [oldspec[i][0] for i in bo[:10]])
        bad.update(bs)
        tgt_bad += (accT % P != 0)
    print('NULLCHECK:', 'PASS' if not bad and tgt_bad == 0 else 'FAIL')

if __name__ == '__main__':
    if '--null' in sys.argv:
        nullcheck()
        sys.exit(0)
    if CHECK:
        crosscheck()
        sys.exit(0)
    cells = [(n, k, l) for n in range(1, NSOLVE + 1)
             for k in range(n + 1) for l in range(n + 1)]
    hcells = [(n, k, l) for n in NHOLD
              for k in range(n + 1) for l in range(n + 1)]
    print('P =', P, 'solve cells:', len(cells), 'holdout cells:', len(hcells),
          flush=True)
    A, b, names, ri = build_system(cells)
    np.savez_compressed('sys_%d_n%d.npz' % (P, NSOLVE), A=A, b=b)
    with open('sys_%d_n%d_names.pkl' % (P, NSOLVE), 'wb') as fh:
        pickle.dump({'names': names, 'rowinfo': ri}, fh)
    print('system:', A.shape, flush=True)
    t0 = time.time()
    x, rk, piv, nbad = fastlin.solve(A, b, P)
    print('rank=%d nbad=%d (%.0fs)' % (rk, nbad, time.time() - t0), flush=True)
    if nbad == 0:
        H, hb, _, hri = build_system(hcells, verbose=False)
        resid = (H @ (x % P) - hb) % P
        nz = int(np.count_nonzero(resid))
        print('HOLDOUT rows nonzero: %d of %d' % (nz, len(hb)), flush=True)
        supp = [(names[i], int(x[i])) for i in range(len(names)) if x[i] % P]
        print('support size:', len(supp))
        with open('live1_x_%d.pkl' % P, 'wb') as fh:
            pickle.dump({'x': x, 'names': names, 'nbad': nbad,
                         'holdout_nz': nz}, fh)
        for nm, v in supp[:60]:
            print('   %-44s %d' % (nm, v))
    else:
        # which rows are bad?  refit with rank info: report distribution
        print('INCONSISTENT: %d bad rows' % nbad)
