"""eps23.py -- constructive completion at weight 3: add the pole-raising jet
identities (residue lemma on R_k(z)*rho(z), rho with poles on the l-lattice).

Jet dictionary at z = l+w (all exact, weight-graded):
  R_k(z) = C(l) w^{-2} exp( G1 w - G2 w^2/2 + G3 w^3/3 - ... )
    G1 = -L_l ;  G2 = (H2_{n+l}-H2_l)+(H2_{n+k+l}-H2_{k+l})-2(H2_l+H2_{n-l})
    G3 = (H3_{n+l}-H3_l)+(H3_{n+k+l}-H3_{k+l})-2(H3_l-H3_{n-l})
  e1 = G1, e2 = G1^2/2 - G2/2, e3 = G1^3/6 - G1 G2/2 + G3/3
  rhoQ  = sum_j 1/(z-j)  : 1/w + T1 - T2 w + T3 w^2, T1 = H_l - H_{n-l},
          T2 = H2_l + H2_{n-l},  T3 = H3_l - H3_{n-l}
  rhoQ2 = sum_j 1/(z-j)^2: 1/w^2 + T2 - 2 T3 w
  rho_m = sum_{i=1}^m 1/(z+i): value r0(m), jets r1 = -(H2 diff), r2 = +(H3 diff)
          m in {k: (k+l,l)-diffs, n: (n+l,l), n+k: (n+k+l,l)}
  rho2_m = sum 1/(z+i)^2: value = H2diff, jet1 = -2 H3diff

Proved identities (all: sum over l of residues of a rational O(z^-2) function
whose off-lattice residues vanish by the P-factor):
  J1[phi]     : e2 + e1 T1 - T2                    (x phi weight-1 k-side)
  J2          : e3 + 2T1 e2 + (T1^2-2T2) e1 + 2T3 - 2T1 T2         [rhoQ^2]
  J3[m]       : (r2 + e1 r1 + e2 r0) + T1 (r1 + e1 r0) - T2 r0     [rhoQ rho_m]
  J4[m<=m']   : e1 r0 r0' + r0 r1' + r1 r0'                        [rho_m rho_m']
  J5[m]       : e1 h2 - 2 h3   (h2,h3 = H2,H3 range diffs)         [rho2_m]
  J6          : e3 + e1 T2 - 2 T3                                  [rhoQ2]
Every one is CALIBRATED against Phi(32) before use.
"""
import sys
from fractions import Fraction as F
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import core
from eps20 import MON, MIDX, NM, SIG, DELTA3, NA
from eps21 import (GENS, NAMES, phi_rows, rankof, prod_w1_w1_w1, prod_w2_w1,
                   w3vec, LK, LL, KSIDE)

# ---- weight-graded jet symbols as (const, w1vec, w2dict, w3dict, products) ----
# We represent each jet quantity as a formal polynomial in letters, using the
# generic expander: a "form" is a list of (coef, [(r,arg)...]) terms.
def form_scale(f, c): return [(cf * c, m) for (cf, m) in f]
def form_add(*fs):
    out = []
    for f in fs: out += f
    return out
def form_mul(f1, f2):
    return [(c1 * c2, m1 + m2) for (c1, m1) in f1 for (c2, m2) in f2]
def form_to_vec(f):
    v = [F(0)] * NM
    for (c, m) in f:
        key = None
        rs = sorted(r for (r, a) in m)
        if rs == [3]: key = ('A', m[0][1])
        elif rs == [1, 2]:
            a2 = [a for (r, a) in m if r == 2][0]
            a1 = [a for (r, a) in m if r == 1][0]
            key = ('B', a2, a1)
        elif rs == [1, 1, 1]:
            key = ('C', tuple(sorted(a for (r, a) in m)))
        else:
            raise ValueError('weight != 3: %s' % (m,))
        v[MIDX[key]] += c
    return v

W1 = lambda vec: [(vec[a], [(1, a)]) for a in range(NA) if vec[a]]
W2 = lambda d: [(c, [(2, a)]) for a, c in d.items() if c]
W3 = lambda d: [(c, [(3, a)]) for a, c in d.items() if c]
ONE = [(F(1), [])]

# args: [n,k,l,n+k,n+l,n-k,n-l,k+l,n+k+l] = 0..8
G1f = W1([-v for v in LL])
G2f = W2({4: F(1), 2: F(-1) - 2, 8: F(1), 7: F(-1), 6: F(-2)})
# careful: G2 = (H2_{n+l}-H2_l) + (H2_{n+k+l}-H2_{k+l}) - 2(H2_l + H2_{n-l})
G2f = W2({4: F(1), 8: F(1), 7: F(-1), 2: F(-3), 6: F(-2)})
G3f = W3({4: F(1), 8: F(1), 7: F(-1), 2: F(-3), 6: F(2)})
# G3 = (H3_{n+l}-H3_l)+(H3_{n+k+l}-H3_{k+l})-2(H3_l - H3_{n-l})
e1f = G1f
e2f = form_add(form_scale(form_mul(G1f, G1f), F(1, 2)), form_scale(G2f, F(-1, 2)))
e3f = form_add(form_scale(form_mul(form_mul(G1f, G1f), G1f), F(1, 6)),
               form_scale(form_mul(G1f, G2f), F(-1, 2)),
               form_scale(G3f, F(1, 3)))
T1f = W1([F(0), F(0), F(1), F(0), F(0), F(0), F(-1), F(0), F(0)])
T2f = W2({2: F(1), 6: F(1)})
T3f = W3({2: F(1), 6: F(-1)})
# rho_m data: m -> (upper-arg, lower-arg) for the H-differences
RHOM = {'k': (7, 2), 'n': (4, 2), 'nk': (8, 2)}
def r0f(m): u, lo = RHOM[m]; return W1([F(1) if a == u else (F(-1) if a == lo else F(0)) for a in range(NA)])
def r1f(m): u, lo = RHOM[m]; return W2({u: F(-1), lo: F(1)})
def r2f(m): u, lo = RHOM[m]; return W3({u: F(1), lo: F(-1)})

NEW, NEWNAMES = [], []
# J1[phi]: (e2 + e1 T1 - T2) * phi(k-side wt-1)
base = form_add(e2f, form_mul(e1f, T1f), form_scale(T2f, F(-1)))
for x in KSIDE:
    phi = W1([F(1) if a == x else F(0) for a in range(NA)])
    NEW.append(form_to_vec(form_mul(base, phi))); NEWNAMES.append('J1[H_%d]' % x)
# J2: e3 + 2 T1 e2 + (T1^2 - 2T2) e1 + 2T3 - 2 T1 T2
J2 = form_add(e3f, form_scale(form_mul(T1f, e2f), F(2)),
              form_mul(form_mul(T1f, T1f), e1f),
              form_scale(form_mul(T2f, e1f), F(-2)),
              form_scale(T3f, F(2)),
              form_scale(form_mul(T1f, T2f), F(-2)))
NEW.append(form_to_vec(J2)); NEWNAMES.append('J2')
# J3[m]: (r2 + e1 r1 + e2 r0) + T1 (r1 + e1 r0) - T2 r0
for m in RHOM:
    f = form_add(r2f(m), form_mul(e1f, r1f(m)), form_mul(e2f, r0f(m)),
                 form_mul(T1f, form_add(r1f(m), form_mul(e1f, r0f(m)))),
                 form_scale(form_mul(T2f, r0f(m)), F(-1)))
    NEW.append(form_to_vec(f)); NEWNAMES.append('J3[%s]' % m)
# J4[m<=m']: e1 r0 r0' + r0 r1' + r1 r0'
ms = list(RHOM)
for i in range(3):
    for j in range(i, 3):
        m1, m2 = ms[i], ms[j]
        f = form_add(form_mul(form_mul(e1f, r0f(m1)), r0f(m2)),
                     form_mul(r0f(m1), r1f(m2)),
                     form_mul(r1f(m1), r0f(m2)))
        NEW.append(form_to_vec(f)); NEWNAMES.append('J4[%s,%s]' % (m1, m2))
# J5[m]: e1 * (H2 diff) - 2 (H3 diff)   [rho2_m: value H2diff, jet -2 H3diff]
for m in RHOM:
    f = form_add(form_mul(e1f, form_scale(r1f(m), F(-1))),   # H2diff = -r1
                 form_scale(r2f(m), F(-2)))
    NEW.append(form_to_vec(f)); NEWNAMES.append('J5[%s]' % m)
# J6: e3 + e1 T2 - 2 T3
J6 = form_add(e3f, form_mul(e1f, T2f), form_scale(T3f, F(-2)))
NEW.append(form_to_vec(J6)); NEWNAMES.append('J6')

print('new jet generators:', len(NEW))

if __name__ == '__main__':
    p = 2147483647
    fm = lambda fr: fr.numerator % p * pow(fr.denominator % p, p - 2, p) % p
    rows = phi_rows(p, 32)
    badgen = []
    for g, nm in zip(NEW, NEWNAMES):
        gv = [fm(v) for v in g]
        ok = all(sum(rr_[i] * gv[i] for i in range(NM)) % p == 0 for rr_ in rows)
        if not ok: badgen.append(nm)
    print('jet-generator calibration:', 'ALL IN KERNEL' if not badgen else 'FAIL: %s' % badgen)

    i2 = pow(2, p - 2, p)
    symv = lambda v: [(v[i] + v[SIG[i]]) * i2 % p for i in range(NM)]
    Gs = [symv([fm(v) for v in g]) for g in GENS + NEW]
    d3s = symv([fm(v) for v in DELTA3])
    rG, _ = rankof(Gs, p, NM)
    rGd, _ = rankof(Gs + [d3s], p, NM)
    print('rank sym(constructive+jets) = %d ; with sym(Delta3): %d -> %s'
          % (rG, rGd, 'IN SPAN => Delta3 PROVED' if rGd == rG else 'still not in span'))
