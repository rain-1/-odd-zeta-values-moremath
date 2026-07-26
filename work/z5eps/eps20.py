"""eps20.py -- Does Delta3 = B3 - w3sym reduce to ONE-VARIABLE (per-fixed-k) sums?

Test:  sym(Delta3) in sym(U),   U := { weight u :  sum_l T(n,k,l) u(n,k,l) = 0
                                       for every fixed (n,k) }.
This is exactly the necessary-and-sufficient shape for a decomposition
   Delta3 = u + u' + antisym,   u in U, u' in sigma(U),
i.e. for the cellwise defect to be provable by one-variable residue facts
(whatever the deformation used), since any one-variable identity kills the
inner sum at fixed outer variable.

Monomial space: all weight-3 monomials of degree <= 3 in the 27 letters
H^(r)_x, r=1..3, x in {n,k,l,n+k,n+l,n-k,n-l,k+l,n+k+l}:  9 + 81 + 165 = 255.

U is computed as ker(Phi) with Phi rows = per-(n,k) sums over l, n <= NROWS.
ker from finite rows OVERESTIMATES U, so a NO here is a clean NO.
A YES needs saturation + out-of-sample verification (done separately).
"""
import sys
from math import comb
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
import core

ARGS = ['n', 'k', 'l', 'n+k', 'n+l', 'n-k', 'n-l', 'k+l', 'n+k+l']
PERM = [0, 2, 1, 4, 3, 6, 5, 7, 8]          # k <-> l on args
NA = 9

# ---------------- monomial basis ----------------
# type A: ('A', a)            = H3_a
# type B: ('B', a, b)         = H2_a * H1_b     (all 81 ordered pairs)
# type C: ('C', (a<=b<=c))    = H1_a H1_b H1_c  (165 multisets)
MON = [('A', a) for a in range(NA)]
MON += [('B', a, b) for a in range(NA) for b in range(NA)]
MON += [('C', t) for t in cwr(range(NA), 3)]
MIDX = {m: i for i, m in enumerate(MON)}
NM = len(MON)
assert NM == 255

def mon_sigma(m):
    if m[0] == 'A':
        return ('A', PERM[m[1]])
    if m[0] == 'B':
        return ('B', PERM[m[1]], PERM[m[2]])
    return ('C', tuple(sorted(PERM[x] for x in m[1])))

SIG = [MIDX[mon_sigma(m)] for m in MON]

# ---------------- Delta3 expansion (exact Q) ----------------
# family-1 (t=1) data
Ll = [F(0), F(0), F(3), F(0), F(-1), F(0), F(-2), F(1), F(-1)]  # -d/dl log T
L1 = [2 * v for v in Ll]
L2 = [F(-4), F(-8), F(10), F(-17, 4), F(-7, 4), F(0), F(8), F(2), F(-2)]
L3 = [F(0), F(0), F(24), F(0), F(-5, 3), F(0), F(-64, 3), F(8, 3), F(-8, 3)]
PSI = [F(0), F(-3, 2), F(3, 2), F(1, 2), F(-1, 2), F(1), F(-1), F(0), F(0)]

vec = [F(0)] * NM
# L3 -> type A
for a in range(NA):
    if L3[a]: vec[MIDX[('A', a)]] += L3[a]
# L1*L2 -> type B  (H2_a from L2, H1_b from L1)
for a in range(NA):
    if L2[a] == 0: continue
    for b in range(NA):
        if L1[b] == 0: continue
        vec[MIDX[('B', a, b)]] += L2[a] * L1[b]
# L1^3/6 -> type C
c1 = L1
for t in cwr(range(NA), 3):
    # multinomial coefficient for multiset t
    from collections import Counter
    cnt = Counter(t)
    coef = F(6)
    for v in cnt.values():
        for j in range(1, v + 1):
            coef /= j
    prod = coef
    for x in t:
        prod *= c1[x]
    if prod:
        vec[MIDX[('C', t)]] += prod / 6
# minus w3sym
vec[MIDX[('A', 3)]] -= F(1, 2)
vec[MIDX[('A', 4)]] -= F(1, 2)
for b in range(NA):
    if PSI[b] == 0: continue
    vec[MIDX[('B', 3, b)]] -= -F(1, 2) * PSI[b]   # w3sym has -(1/2)Psi*H2_{n+k}
    vec[MIDX[('B', 4, b)]] -= F(1, 2) * PSI[b]    # and +(1/2)Psi*H2_{n+l}
DELTA3 = vec

# ---------------- exact sanity: expansion == Bell cellwise, and null sum ----------------
H = core.Hs
def letters_at(n, k, l):
    xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
    return xs

def mon_val(m, xs):
    if m[0] == 'A':
        return H(xs[m[1]], 3)
    if m[0] == 'B':
        return H(xs[m[1]], 2) * H(xs[m[2]], 1)
    p = F(1)
    for x in m[1]:
        p *= H(xs[x], 1)
    return p

def eval_vec(v, n, k, l):
    xs = letters_at(n, k, l)
    s = F(0)
    for i, c in enumerate(v):
        if c:
            s += c * mon_val(MON[i], xs)
    return s

def B3_direct(n, k, l):
    xs = letters_at(n, k, l)
    l1 = sum(L1[a] * H(xs[a], 1) for a in range(NA))
    l2 = sum(L2[a] * H(xs[a], 2) for a in range(NA))
    l3 = sum(L3[a] * H(xs[a], 3) for a in range(NA))
    return l3 + l1 * l2 + l1 ** 3 / 6

def w3sym_direct(n, k, l):
    xs = letters_at(n, k, l)
    psi = sum(PSI[a] * H(xs[a], 1) for a in range(NA))
    return (F(1, 2) * (H(n + k, 3) + H(n + l, 3))
            - psi / 2 * (H(n + k, 2) - H(n + l, 2)))

bad = 0
for n in range(0, 7):
    for k in range(n + 1):
        for l in range(n + 1):
            d1 = eval_vec(DELTA3, n, k, l)
            d2 = B3_direct(n, k, l) - w3sym_direct(n, k, l)
            if d1 != d2: bad += 1
print('expansion == direct Bell defect, cells n<=6:', 'PASS' if bad == 0 else 'FAIL %d' % bad)
s = [sum(core.T(n, k, l) * eval_vec(DELTA3, n, k, l)
         for k in range(n + 1) for l in range(n + 1)) for n in range(7)]
print('double sum T*Delta3 = 0, n<=6:', 'PASS' if all(v == 0 for v in s) else 'FAIL')

# ---------------- Phi matrix and kernel, mod p ----------------
def run(p, NROWS):
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
                h1 = [Ht[1][x] for x in xs]
                h2 = [Ht[2][x] for x in xs]
                h3 = [Ht[3][x] for x in xs]
                i = 0
                for a in range(NA):
                    row[i] = (row[i] + t * h3[a]) % p; i += 1
                for a in range(NA):
                    th2 = t * h2[a] % p
                    for b in range(NA):
                        row[i] = (row[i] + th2 * h1[b]) % p; i += 1
                for tt in cwr(range(NA), 3):
                    v = t
                    for x in tt:
                        v = v * h1[x] % p
                    row[i] = (row[i] + v) % p; i += 1
            rows.append(row)
    print('Phi: %d rows x %d cols' % (len(rows), NM))

    # rref -> rank + null basis
    M = [r[:] for r in rows]
    m_ = len(M); piv = []; r_ = 0
    for c in range(NM):
        pr = next((i for i in range(r_, m_) if M[i][c] % p), None)
        if pr is None: continue
        M[r_], M[pr] = M[pr], M[r_]
        inv = pow(M[r_][c], p - 2, p)
        M[r_] = [v * inv % p for v in M[r_]]
        for i in range(m_):
            if i != r_ and M[i][c]:
                f = M[i][c]
                M[i] = [(v - f * w) % p for v, w in zip(M[i], M[r_])]
        piv.append(c); r_ += 1
    rank = r_
    null = []
    pivset = set(piv)
    for fc in range(NM):
        if fc in pivset: continue
        v = [0] * NM; v[fc] = 1
        for i, c in enumerate(piv):
            v[c] = (-M[i][fc]) % p
        null.append(v)
    print('rank(Phi) = %d, dim ker = %d' % (rank, len(null)))

    # calibration: Ll * H2_n  should be in ker(Phi)
    cal = [0] * NM
    fm = lambda fr: fr.numerator % p * pow(fr.denominator % p, p - 2, p) % p
    for b in range(NA):
        if Ll[b]:
            cal[MIDX[('B', 0, b)]] = fm(Ll[b])
    resid = max(sum(rr[i] * cal[i] for i in range(NM)) % p for rr in rows)
    print('calibration Ll*H2_n in ker(Phi):', 'PASS' if resid == 0 else 'FAIL')

    # symmetrise null basis and Delta3; membership test
    d3 = [fm(v) for v in DELTA3]
    i2 = pow(2, p - 2, p)
    d3s = [(d3[i] + d3[SIG[i]]) * i2 % p for i in range(NM)]
    A = []
    for v in null:
        A.append([(v[i] + v[SIG[i]]) * i2 % p for i in range(NM)])
    # rank of [A] vs [A | d3s]  (rows = vectors)
    def rankof(vecs):
        Mx = [v[:] for v in vecs]
        mm = len(Mx); rr_ = 0
        for c in range(NM):
            pr = next((i for i in range(rr_, mm) if Mx[i][c] % p), None)
            if pr is None: continue
            Mx[rr_], Mx[pr] = Mx[pr], Mx[rr_]
            inv = pow(Mx[rr_][c], p - 2, p)
            Mx[rr_] = [v * inv % p for v in Mx[rr_]]
            for i in range(mm):
                if i != rr_ and Mx[i][c]:
                    f = Mx[i][c]
                    Mx[i] = [(v - f * w) % p for v, w in zip(Mx[i], Mx[rr_])]
            rr_ += 1
        return rr_, Mx
    rA, _ = rankof(A)
    rAd, _ = rankof(A + [d3s])
    print('rank sym(kerPhi) = %d ; with sym(Delta3): %d  -> %s'
          % (rA, rAd, 'MEMBER (YES)' if rAd == rA else 'NOT MEMBER (NO)'))
    return rank, rA, rAd

if __name__ == '__main__':
    for p in (2147483647, 2147483629):
        print('=' * 60, 'p =', p)
        run(p, 26)
