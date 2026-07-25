"""P1e-refold stage 6: the PROVED sub-kernel, and whether the refolded weights are
reachable from w3hat inside it.

WHY THIS MATTERS.  Theorem B as consumed downstream is  Phat_n = sum T*w3hat, and
the downstream (Lemma G / Lemma F ledger / the d3 <= 1+min(vT,2) depth bound) reads
w3hat CELL BY CELL.  So certifying  Phat_n = sum T*w-tilde  for a different
representative does NOT deliver Theorem B unless  sum T*(w3hat - w-tilde) = 0 is
itself PROVED -- exactly the caveat PHASE2_CERTS section 1 raises for w5.

The proved supply of kernel elements is the "Lemma Phi species":
  (P0)  sum_k T*Phi = 0,                      Phi = A1(k) + 2 B1(k) + C1   [ENDGAME R1.2]
  (P1)  sum_k T*[Phi*A1(k) - A2(k)] = 0                                    [CANCEL 3]
  (P2)  sum_k T*[Phi*C1     - C2  ] = 0
  (P3)  sum_k T*[Phi*B1(k) - (1/2)(Phi^2 - A2(k) - C2)] = 0
each valid for EVERY fixed l, hence multipliable by any k-free factor; plus the
k<->l mirrors.  All four are PROVED (residue-sum arguments) and VERIFIED exactly.
"""
import sys, os
import numpy as np
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from w3full import FullBasis, rref_aug, LSYM, SYMIDX, ALL_SYMBOLS, Q1, Q2

B = FullBasis()
KIDX = {m: i for i, (m, w) in enumerate(B.km)}
CIDX = {m: i for i, (m, w) in enumerate(B.cm)}
NIDX = {m: i for i, (m, w) in enumerate(B.nm)}
EIDX = {e: i for i, e in enumerate(B.els)}


# ------------- letter polynomials as dict {sorted tuple of letter names: coeff} ----
def lp(*terms):
    out = {}
    for coef, mono in terms:
        key = tuple(sorted(mono))
        out[key] = out.get(key, F(0)) + F(coef)
    return {k: v for k, v in out.items() if v}


def mul(p, q):
    out = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            k = tuple(sorted(m1 + m2))
            out[k] = out.get(k, F(0)) + c1 * c2
    return {k: v for k, v in out.items() if v}


def add(*ps):
    out = {}
    for p in ps:
        for m, c in p.items():
            out[m] = out.get(m, F(0)) + c
    return {k: v for k, v in out.items() if v}


def smul(a, p):
    return {m: F(a) * c for m, c in p.items() if F(a) * c}


def mirror(p):
    def sw(lt):
        if lt.endswith('(k)'):
            return lt[:-3] + '(l)'
        if lt.endswith('(l)'):
            return lt[:-3] + '(k)'
        return lt
    return {tuple(sorted(sw(x) for x in m)): c for m, c in p.items()}


def tovec(p, q=Q1):
    """letter polynomial -> coefficient vector over the 98 folded basis columns"""
    v = np.zeros(len(B), dtype=np.int64)
    for m, c in p.items():
        f = tuple(sorted(x[:2] for x in m if x.endswith('(k)')))
        g = tuple(sorted(x[:2] for x in m if x.endswith('(l)')))
        cc = tuple(sorted(x for x in m if x[0] == 'C'))
        ss = tuple(sorted(x for x in m if x[0] == 'N'))
        e = (KIDX[f], KIDX[g], CIDX[cc], NIDX[ss])
        v[EIDX[e]] = (v[EIDX[e]] + c.numerator % q * pow(c.denominator % q, q - 2, q)) % q
    return v


A1k, B1k, C1 = ('A1(k)',), ('B1(k)',), ('C1',)
PHI = lp((1, A1k), (2, B1k), (1, C1))
P0 = PHI
P1 = add(mul(PHI, lp((1, A1k))), lp((-1, ('A2(k)',))))
P2 = add(mul(PHI, lp((1, C1))), lp((-1, ('C2',))))
P3 = add(mul(PHI, lp((1, B1k))),
         smul(F(-1, 2), add(mul(PHI, PHI), lp((-1, ('A2(k)',))), lp((-1, ('C2',))))))

# k-free multipliers of weight 2 and weight 1
W1 = [lp((1, ('A1(l)',))), lp((1, ('B1(l)',))), lp((1, ('N1',)))]
W2 = [lp((1, x)) for x in [('A2(l)',), ('B2(l)',), ('N2',), ('A1(l)', 'A1(l)'),
                           ('A1(l)', 'B1(l)'), ('A1(l)', 'N1'), ('B1(l)', 'B1(l)'),
                           ('B1(l)', 'N1'), ('N1', 'N1')]]

gens, names = [], []
for h in W2:
    gens.append(mul(P0, h)); names.append('P0 * %s' % (list(h)[0],))
for tag, P in (('P1', P1), ('P2', P2), ('P3', P3)):
    for lam in W1:
        gens.append(mul(P, lam)); names.append('%s * %s' % (tag, (list(lam)[0],)))
nk = len(gens)
for i in range(nk):                     # the k<->l mirrors
    gens.append(mirror(gens[i])); names.append('mirror(%s)' % names[i])

G = np.array([tovec(g) for g in gens], dtype=np.int64)
print('proved-kernel generators built: %d' % len(gens), flush=True)

# ---- sanity: every generator must be in ker V  (design matrix from run1) ----
z = np.load(os.path.join(HERE, 'DF_w3_240_%d.npz' % Q1))
M, b = z['M'], z['b']
resid = (M @ G.T) % Q1
bad = [names[i] for i in range(len(gens)) if (resid[:, i] != 0).any()]
print('generators with NONZERO value (must be none): %d  %s' % (len(bad), bad[:5]), flush=True)

rG, _, _, _ = rref_aug(G, np.zeros(len(gens), dtype=np.int64), Q1)
r0, _, _, A0 = rref_aug(M, b, Q1)
print('dim span(proved kernel) = %d ;  dim ker V = %d ;  ambient = %d'
      % (rG, len(B) - r0, len(B)), flush=True)

# --------------------------------------------------- membership of the targets
E = ()
W3HAT = lp((1, ('N3',)), (1, ('A3(k)',)), (1, ('A3(l)',)),
           (F(-1, 4), ('A2(k)', 'A1(k)')), (F(-1, 4), ('A2(l)', 'A1(l)')),
           (F(-3, 4), ('A2(k)', 'B1(k)')), (F(-3, 4), ('A2(l)', 'B1(l)')),
           (F(-3, 8), ('A2(k)', 'C1')), (F(-3, 8), ('A2(l)', 'C1')),
           (F(-1, 8), ('A2(k)', 'A1(l)')), (F(-1, 8), ('A2(l)', 'A1(k)')))
VFOLD = lp((1, ('N3',)), (2, ('A3(k)',)),
           (F(-1, 2), ('A2(k)', 'A1(k)')), (F(-3, 2), ('A2(k)', 'B1(k)')),
           (F(-3, 4), ('A2(k)', 'C1')), (F(-1, 4), ('A2(k)', 'A1(l)')))

import json
cand = json.load(open(os.path.join(HERE, 'wtilde3.json')))


def parse(entry):
    p = {}
    for lab, c in entry['monomials']:
        p[tuple(sorted(lab.split('*'))) if '*' in lab else (lab,)] = F(c)
    return {tuple(sorted(k)): v for k, v in p.items()}


def in_span(vec, G):
    r1, _, _, _ = rref_aug(G, np.zeros(len(G), dtype=np.int64), Q1)
    GG = np.concatenate([G, vec.reshape(1, -1)], axis=0)
    r2, _, _, _ = rref_aug(GG, np.zeros(len(GG), dtype=np.int64), Q1)
    return r1 == r2, r1, r2


for tag, target in [('v (folded w3hat)', VFOLD)] + \
                   [(k, parse(v)) for k, v in cand.items()]:
    d = add(W3HAT, smul(-1, target))
    v = tovec(d)
    ok, r1, r2 = in_span(v, G)
    val = (M @ v) % Q1
    print('w3hat - [%s] : in ker V = %s ; in PROVED span = %s  (rank %d -> %d)'
          % (tag, bool((val == 0).all()), ok, r1, r2), flush=True)

# ---------------------------------------------------------------------------
# The k<->l FOLDING moves are also PROVED (they are a rearrangement of a finite
# sum: T is k<->l symmetric, so  sum T*mu = sum T*mirror(mu)  for every monomial).
# PHASE2_CERTS 5.2 step 3 is exactly this, labelled [PROVED].
print('\n--- adding the PROVED folding (antisymmetric) moves ---', flush=True)
anti = []
for e in B.els:
    i, j, ci, ni = e
    if i == j:
        continue
    v = np.zeros(len(B), dtype=np.int64)
    v[EIDX[e]] = 1
    v[EIDX[(j, i, ci, ni)]] = Q1 - 1
    anti.append(v)
Ganti = np.array(anti, dtype=np.int64)
ra, _, _, _ = rref_aug(Ganti, np.zeros(len(anti), dtype=np.int64), Q1)
resid = (M @ Ganti.T) % Q1
print('folding moves: %d generators, span dim %d, all in ker V = %s'
      % (len(anti), ra, not bool((resid != 0).any())), flush=True)

GALL = np.concatenate([G, Ganti], axis=0)
rall, _, _, _ = rref_aug(GALL, np.zeros(len(GALL), dtype=np.int64), Q1)
print('dim span(PROVED kernel: Lemma-Phi species + folding) = %d   (ker V = %d)'
      % (rall, len(B) - r0), flush=True)

for tag, target in [('v (folded w3hat)', VFOLD)] + \
                   [(k, parse(v)) for k, v in cand.items()]:
    d = add(W3HAT, smul(-1, target))
    v = tovec(d)
    ok, r1, r2 = in_span(v, GALL)
    print('w3hat - [%-18s] : in PROVED span (Phi + folding) = %s  (rank %d -> %d)'
          % (tag, ok, r1, r2), flush=True)
