"""eps21.py -- weight 3:
 (1) saturation of ker(Phi) at larger NROWS + membership re-test
 (2) CONSTRUCTIVE span: is sym(Delta3) in the span of sym(proved generators)?
     Generators (all provable from Z5CF_BARNES sec 7 + Z5_ORDER0 (L5)):
       G1[phi2]  : L_l * phi2(k-side wt-2)                     [res-at-infinity F1]
       G2[phi1]  : (L_k L_l - C2) * phi1(k-side wt-1)          [Sum_l D_kl = 0]
       G3[rg,phi]: [(H2 rg-diff in l-arg) + L_l*(H1 rg-diff)] * phi1   [g_k(j)=0]
       G4a       : 2(H3_{n+l}-H3_{k+l}) + L_l(H2_{n+l}-H2_{k+l})       [g_k'(j)=0]
       G4b       : 2(H3_{n+k+l}-H3_{n+l}) + (L_k+L_l)(H2..) + (LkLl-C2)(H1..)
                                                               [q_k = g_k' on n<j<=n+k]
       G5[rg]    : L_k(H2 rg-diff) + (LkLl-C2)(H1 rg-diff)     [q_k(j)=0]
       G6        : 2(H3_{n+k+l}-H3_{k+l}) + (Lk+Ll)(H2..) + (LkLl-C2)(H1..)
                                                               [(L5) anti-diagonal residue]
     Every generator is CALIBRATED against Phi (must be in ker) before use.
"""
import sys
from math import comb
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import core
from eps20 import MON, MIDX, NM, SIG, DELTA3, NA

# letter index: [n, k, l, n+k, n+l, n-k, n-l, k+l, n+k+l]
LK = [F(0), F(3), F(0), F(-1), F(0), F(-2), F(0), F(1), F(-1)]
LL = [F(0), F(0), F(3), F(0), F(-1), F(0), F(-2), F(1), F(-1)]
KSIDE = [0, 1, 3, 5]     # n, k, n+k, n-k

def addB(vec, a, w1vec, coef=F(1)):
    """vec += coef * H2_a * (w1vec . H1)"""
    for b in range(NA):
        if w1vec[b]:
            vec[MIDX[('B', a, b)]] += coef * w1vec[b]

def addC(vec, w1, w2, coef=F(1)):
    """vec += coef * (w1.H1)*(w2.H1) ... as symmetric deg-2 -> C-type with a repeated?
       No: product of two weight-1 forms = sum over pairs -> C-type monomials need 3 H1s.
       This is deg-2 weight-2; NOT used alone."""
    raise RuntimeError

def prod_w1_w1_w1(vec, u, v, w, coef=F(1)):
    for a in range(NA):
        if u[a] == 0: continue
        for b in range(NA):
            if v[b] == 0: continue
            for c in range(NA):
                if w[c] == 0: continue
                t = tuple(sorted((a, b, c)))
                vec[MIDX[('C', t)]] += coef * u[a] * v[b] * w[c]

def prod_w2_w1(vec, a2coefs, w1, coef=F(1)):
    """a2coefs: dict arg->coef for H2; times weight-1 form w1"""
    for a, ca in a2coefs.items():
        if ca == 0: continue
        for b in range(NA):
            if w1[b]:
                vec[MIDX[('B', a, b)]] += coef * ca * w1[b]

def w3vec():
    return [F(0)] * NM

GENS = []
NAMES = []

# G1: L_l * phi2 ; phi2 = H2_x (x k-side)  OR  H1_x H1_y (k-side pair)
for x in KSIDE:
    v = w3vec()
    prod_w2_w1(v, {x: F(1)}, LL)
    GENS.append(v); NAMES.append('G1[H2_%d]' % x)
for i, x in enumerate(KSIDE):
    for y in KSIDE[i:]:
        v = w3vec()
        e1 = [F(0)]*NA; e1[x] = F(1)
        e2 = [F(0)]*NA; e2[y] = F(1)
        prod_w1_w1_w1(v, LL, e1, e2)
        GENS.append(v); NAMES.append('G1[H_%d H_%d]' % (x, y))

# C2 as H2-dict
C2D = {7: F(-1), 8: F(1)}

# G2: (L_k L_l - C2) * phi1
for x in KSIDE:
    v = w3vec()
    e1 = [F(0)]*NA; e1[x] = F(1)
    prod_w1_w1_w1(v, LK, LL, e1)
    prod_w2_w1(v, C2D, e1, F(-1))
    GENS.append(v); NAMES.append('G2[H_%d]' % x)

# G3: ranges (alpha,beta) in l-argument: pairs of args from {l(2), k+l(7), n+l(4), n+k+l(8)}
# (H2_beta - H2_alpha) + L_l (H_beta - H_alpha), times phi1
RANGES3 = [(2, 7), (2, 4), (2, 8), (7, 4), (7, 8), (4, 8)]   # (alpha_arg, beta_arg)
for (aa, bb) in RANGES3:
    for x in KSIDE:
        v = w3vec()
        e1 = [F(0)]*NA; e1[x] = F(1)
        prod_w2_w1(v, {bb: F(1), aa: F(-1)}, e1)
        d1 = [F(0)]*NA; d1[bb] = F(1); d1[aa] = F(-1)
        prod_w1_w1_w1(v, LL, d1, e1)
        GENS.append(v); NAMES.append('G3[(%d,%d),H_%d]' % (aa, bb, x))

# G4a: 2(H3_{n+l} - H3_{k+l}) + L_l (H2_{n+l} - H2_{k+l})
v = w3vec()
v[MIDX[('A', 4)]] += F(2); v[MIDX[('A', 7)]] += F(-2)
prod_w2_w1(v, {4: F(1), 7: F(-1)}, LL)
GENS.append(v); NAMES.append('G4a')

# G4b: 2(H3_{n+k+l} - H3_{n+l}) + (L_k+L_l)(H2_{n+k+l} - H2_{n+l})
#      + (L_kL_l - C2)(H_{n+k+l} - H_{n+l})
v = w3vec()
v[MIDX[('A', 8)]] += F(2); v[MIDX[('A', 4)]] += F(-2)
LKL = [LK[a] + LL[a] for a in range(NA)]
prod_w2_w1(v, {8: F(1), 4: F(-1)}, LKL)
d1 = [F(0)]*NA; d1[8] = F(1); d1[4] = F(-1)
prod_w1_w1_w1(v, LK, LL, d1)
prod_w2_w1(v, C2D, d1, F(-1))
GENS.append(v); NAMES.append('G4b')

# G5: ranges (0,k),(0,n),(k,n) in l-arg: args (l->k+l), (l->n+l), (k+l->n+l)
for (aa, bb) in [(2, 7), (2, 4), (7, 4)]:
    v = w3vec()
    prod_w2_w1(v, {bb: F(1), aa: F(-1)}, LK)
    d1 = [F(0)]*NA; d1[bb] = F(1); d1[aa] = F(-1)
    prod_w1_w1_w1(v, LK, LL, d1)
    prod_w2_w1(v, C2D, d1, F(-1))
    GENS.append(v); NAMES.append('G5[(%d,%d)]' % (aa, bb))

# G6: (L5) residue family, m-range [1,n]: args k+l -> n+k+l
v = w3vec()
v[MIDX[('A', 8)]] += F(2); v[MIDX[('A', 7)]] += F(-2)
prod_w2_w1(v, {8: F(1), 7: F(-1)}, LKL)
d1 = [F(0)]*NA; d1[8] = F(1); d1[7] = F(-1)
prod_w1_w1_w1(v, LK, LL, d1)
prod_w2_w1(v, C2D, d1, F(-1))
GENS.append(v); NAMES.append('G6')

print('constructive generators:', len(GENS))

# ---------------- Phi rows builder ----------------
def phi_rows(p, NROWS):
    HM = 3 * NROWS + 2
    Ht = [[0] * (HM + 1) for _ in range(4)]
    for m in range(1, HM + 1):
        im = pow(m, p - 2, p); acc = im
        Ht[1][m] = (Ht[1][m - 1] + acc) % p
        for r in (2, 3):
            acc = acc * im % p
            Ht[r][m] = (Ht[r][m - 1] + acc) % p
    rows = []
    for n in range(NROWS + 1):
        for k in range(n + 1):
            row = [0] * NM
            for l in range(n + 1):
                t = core.T(n, k, l) % p
                xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
                h1 = [Ht[1][x] for x in xs]; h2 = [Ht[2][x] for x in xs]
                h3 = [Ht[3][x] for x in xs]
                i = 0
                for a in range(NA):
                    row[i] = (row[i] + t * h3[a]) % p; i += 1
                for a in range(NA):
                    th2 = t * h2[a] % p
                    for b in range(NA):
                        row[i] = (row[i] + th2 * h1[b]) % p; i += 1
                for tt in cwr(range(NA), 3):
                    vv = t
                    for x in tt:
                        vv = vv * h1[x] % p
                    row[i] = (row[i] + vv) % p; i += 1
            rows.append(row)
    return rows

def rankof(vecs, p, ncols):
    Mx = [v[:] for v in vecs]
    mm = len(Mx); rr = 0
    for c in range(ncols):
        pr = next((i for i in range(rr, mm) if Mx[i][c] % p), None)
        if pr is None: continue
        Mx[rr], Mx[pr] = Mx[pr], Mx[rr]
        inv = pow(Mx[rr][c], p - 2, p)
        Mx[rr] = [v * inv % p for v in Mx[rr]]
        for i in range(mm):
            if i != rr and Mx[i][c]:
                f = Mx[i][c]
                Mx[i] = [(v - f * w) % p for v, w in zip(Mx[i], Mx[rr])]
        rr += 1
    return rr, Mx

if __name__ == '__main__':
    p = 2147483647
    fm = lambda fr: fr.numerator % p * pow(fr.denominator % p, p - 2, p) % p
    for NROWS in (26, 32):
        rows = phi_rows(p, NROWS)
        r, _ = rankof(rows, p, NM)
        print('NROWS=%d: rank(Phi) = %d' % (NROWS, r))
    rows = phi_rows(p, 32)

    # calibrate every generator: Phi . gen = 0 ?
    badgen = []
    for g, nm in zip(GENS, NAMES):
        gv = [fm(v) for v in g]
        ok = all(sum(rr_[i] * gv[i] for i in range(NM)) % p == 0 for rr_ in rows)
        if not ok: badgen.append(nm)
    print('generator calibration vs Phi(32):',
          'ALL IN KERNEL' if not badgen else 'FAILING: %s' % badgen)

    # constructive span test (symmetrised)
    i2 = pow(2, p - 2, p)
    symv = lambda v: [(v[i] + v[SIG[i]]) * i2 % p for i in range(NM)]
    Gs = [symv([fm(v) for v in g]) for g in GENS]
    d3s = symv([fm(v) for v in DELTA3])
    rG, _ = rankof(Gs, p, NM)
    rGd, _ = rankof(Gs + [d3s], p, NM)
    print('rank sym(constructive) = %d ; with sym(Delta3): %d -> %s'
          % (rG, rGd, 'IN CONSTRUCTIVE SPAN' if rGd == rG else 'NOT in constructive span'))
