"""P1e-refold stage 8: build the PROVED-AFFINE optima explicitly over Q and verify
them exactly (sum_{k,l} T*w = Phat_n) for n = 0..40 with held-out levels.

Optima found by run6.py inside  w3hat + span(Lemma-Phi species + folding):
   E-optimum : degree>=2 letters {A1(k), A2(k), B1(k), A2(l)}   -> E = 7 symbols
   S-optimum : whole summand 10 symbols
"""
import sys, os, json
import numpy as np
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kernel_proved as KP
from w3full import FullBasis, LSYM, SYMIDX, ALL_SYMBOLS, Q1
from exact import rref_Q, sums
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import Ph, T                                            # noqa

B = KP.B
EIDX = KP.EIDX
NB = len(B)
pc = lambda x: bin(int(x)).count('1')
lmask = {lt: sum(1 << SYMIDX[s] for s in LSYM[lt]) for lt in sorted(LSYM)}
colsym = np.array([sum(1 << SYMIDX[s] for lt in B.letters(e) for s in LSYM[lt])
                   for e in B.els], dtype=np.int64)
coldeg = np.array([B.degree(e) for e in B.els])


def qvec(p):
    """letter polynomial -> exact rational coefficient vector"""
    v = [F(0)] * NB
    for m, c in p.items():
        f = tuple(sorted(x[:2] for x in m if x.endswith('(k)')))
        g = tuple(sorted(x[:2] for x in m if x.endswith('(l)')))
        cc = tuple(sorted(x for x in m if x[0] == 'C'))
        ss = tuple(sorted(x for x in m if x[0] == 'N'))
        v[EIDX[(KP.KIDX[f], KP.KIDX[g], KP.CIDX[cc], KP.NIDX[ss])]] += c
    return v


# exact generators: Lemma-Phi species + folding
gensQ = [qvec(g) for g in KP.gens]
for e in B.els:
    i, j, ci, ni = e
    if i == j:
        continue
    v = [F(0)] * NB
    v[EIDX[e]] = F(1)
    v[EIDX[(j, i, ci, ni)]] = F(-1)
    gensQ.append(v)
w3 = qvec(KP.W3HAT)
print('exact generators: %d ; ambient %d' % (len(gensQ), NB), flush=True)


def build(sel):
    """exact x supported on sel with x - w3 in span(gensQ)"""
    Z = [c for c in range(NB) if c not in set(sel)]
    rows = [[gensQ[a][c] for a in range(len(gensQ))] + [-w3[c]] for c in Z]
    r, piv, R, inc = rref_Q(rows)
    if inc:
        return None
    y = [F(0)] * len(gensQ)
    for i, c in enumerate(piv):
        y[c] = R[i][-1]
    x = [w3[c] + sum(y[a] * gensQ[a][c] for a in range(len(gensQ))) for c in range(NB)]
    assert all(x[c] == 0 for c in Z), 'support violated'
    return x


def mono_of(e):
    i, j, ci, ni = e
    return (tuple('%s(k)' % x for x in B.km[i][0])
            + tuple('%s(l)' % x for x in B.km[j][0])
            + tuple(B.cm[ci][0]) + tuple(B.nm[ni][0]))


def mkm(L):
    m = 0
    for x in L:
        m |= lmask[x]
    return m


CASES = {
    'wE (E=7, proved-affine)': np.unique(np.concatenate([
        np.nonzero(coldeg <= 1)[0],
        np.nonzero((coldeg >= 2) &
                   ((colsym & ~mkm(['A1(k)', 'A2(k)', 'B1(k)', 'A2(l)'])) == 0))[0]])),
    'wS (S=10, proved-affine)': np.nonzero(
        (colsym & ~mkm(['A1(k)', 'A2(k)', 'A3(k)', 'B1(k)', 'A2(l)', 'N3'])) == 0)[0],
}

OUT = {}
for tag, sel in CASES.items():
    print('\n=== %s : %d candidate columns ===' % (tag, len(sel)), flush=True)
    x = build(sel)
    if x is None:
        print('   NOT reachable exactly', flush=True)
        continue
    used = [(mono_of(B.els[c]), x[c]) for c in range(NB) if x[c] != 0]
    S = E = 0
    for mu, c in used:
        mm = 0
        for lt in mu:
            mm |= lmask[lt]
        S |= mm
        if len(mu) >= 2:
            E |= mm
    print('   %d monomials ; S = %d symbols ; E = %d symbols' % (len(used), pc(S), pc(E)),
          flush=True)
    for mu, c in used:
        print('      %-30s %s' % ('*'.join(mu), c), flush=True)
    sy = lambda m: ['H^(%d)_{%s}' % (r, a) for (a, r) in
                    (ALL_SYMBOLS[i] for i in range(len(ALL_SYMBOLS)) if m >> i & 1)]
    print('   S-symbols (%d): %s' % (pc(S), sy(S)), flush=True)
    print('   E-symbols (%d): %s' % (pc(E), sy(E)), flush=True)

    # ---- EXACT verification: sum_{k,l} T * w  ==  Phat_n ----
    monos = [mu for mu, c in used]
    coefs = [c for mu, c in used]
    NS = list(range(0, 31)) + [33, 36, 40]
    Sv = sums(monos, NS)
    bad = [n for n in NS if sum(coefs[i] * Sv[n][i] for i in range(len(monos))) != Ph(n)]
    print('   EXACT check  sum T*w == Phat  for n in %s : %s'
          % ('0..30,33,36,40', 'ALL PASS' if not bad else 'FAIL at %s' % bad), flush=True)
    OUT[tag] = {'monomials': [['*'.join(mu), str(c)] for mu, c in used],
                'S': pc(S), 'E': pc(E), 'S_symbols': sy(S), 'E_symbols': sy(E),
                'exact_verified_n': NS, 'proved_affine': True}

json.dump(OUT, open(os.path.join(HERE, 'wtilde3_proved.json'), 'w'), indent=1)
print('\nwrote wtilde3_proved.json', flush=True)
