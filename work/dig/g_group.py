"""g_group.py -- the Rhin-Viola / Zudilin group for the weight-3 family, exactly.

Realisation: Zudilin, "Arithmetic of linear forms involving odd zeta values"
(llm/04), Lemma 8.  The group  G = <a1,a2,a3,b,h>  acts by permutations of the
16 entries of the 4x4 matrix

    c_{jk} = |alpha_j - beta_k|   (j,k = 1..4)

built from integral directions (alpha, beta) with
    {beta_1,beta_2} < {alpha_1..alpha_4} < {beta_3,beta_4},
    alpha_1+..+alpha_4 = beta_1+..+beta_4.

Generators (all involutions):
    a_j (j=1,2,3) : swap rows j and 4
    b             : swap columns 3 and 4
    h             : (c11 c33)(c13 c31)(c22 c44)(c24 c42)
|G| = 1920 = |W(D_5)|.

Invariant (Zudilin Lemma 9):   H(c) / Pi(c)   with
    Pi(c) = c21! c31! c41! c12! c32! c42! c33! c44!
i.e. the transfer identity  H(c') = (Pi(c')/Pi(c)) H(c)  for every c' = g c.

Denominator saving:
    nu_p  = max_{g in G} ord_p( Pi(c n) / Pi(g c n) )
    Phi_n = prod_{sqrt(m0 n) < p <= m3 n} p^{nu_p}
    delta = lim log Phi_n / n
          = int_0^1 phi(x) dpsi(x) - int_0^{1/m3} phi(x) dx/x^2
    phi(x) = max_{g in G} sum_{i in F} ( floor(c_i x) - floor((g c)_i x) )

VALIDATION ANCHOR: at the Rhin-Viola optimum (alpha;beta) = (18,17,16,19;0,7,31,32)
Zudilin reports C_0 = 47.15472079, C_1 = 48.46940964, mu(zeta(3)) <= 5.51389062,
with C_2 = 2m1 + m2 - delta.  Solving gives delta = 20.1879...; we recompute it
here from scratch.
"""

from fractions import Fraction as F
from math import floor

import numpy as np
from scipy.special import digamma

# position index of c_{jk} (1-based j,k) inside a flat length-16 tuple
def pos(j, k):
    return 4 * (j - 1) + (k - 1)


def _swap_perm(pairs):
    p = list(range(16))
    for x, y in pairs:
        p[x], p[y] = p[y], p[x]
    return tuple(p)


GEN = {}
for j in (1, 2, 3):
    GEN[f"a{j}"] = _swap_perm([(pos(j, k), pos(4, k)) for k in (1, 2, 3, 4)])
GEN["b"] = _swap_perm([(pos(j, 3), pos(j, 4)) for j in (1, 2, 3, 4)])
GEN["h"] = _swap_perm([(pos(1, 1), pos(3, 3)), (pos(1, 3), pos(3, 1)),
                       (pos(2, 2), pos(4, 4)), (pos(2, 4), pos(4, 2))])

# the 8-element index set F carrying Pi(c)
F_IDX = [pos(2, 1), pos(3, 1), pos(4, 1), pos(1, 2),
         pos(3, 2), pos(4, 2), pos(3, 3), pos(4, 4)]


def compose(p, q):
    """(p after q): result[i] = p[q[i]]."""
    return tuple(p[q[i]] for i in range(16))


def generate_group():
    ident = tuple(range(16))
    seen = {ident}
    frontier = [ident]
    gens = list(GEN.values())
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = compose(g, x)
                if y not in seen:
                    seen.add(y)
                    nxt.append(y)
        frontier = nxt
    return sorted(seen)


GROUP = generate_group()


# ---------------------------------------------------------------- directions

def c_matrix(alpha, beta):
    """Flat 16-tuple c_{jk} = |alpha_j - beta_k|."""
    return tuple(abs(alpha[j] - beta[k]) for j in range(4) for k in range(4))


def admissible(alpha, beta):
    a = sorted(alpha)
    b = sorted(beta)
    return (sum(alpha) == sum(beta) and b[1] < a[0] and a[3] < b[2]
            and all(abs(x - y) > 0 for x in alpha for y in beta))


def m_params(alpha, beta):
    """m0, m1, m2, m3 of Zudilin Section 5."""
    a = sorted(alpha)
    b = sorted(beta)
    c = c_matrix(alpha, beta)
    m0 = max(c)
    m1 = b[3] - a[0]
    # m2 = max{a1-b1, a2-b2, b4*-a3, b4*-a4, b3*-a1*}  (labelled version)
    m2 = max(alpha[0] - beta[0], alpha[1] - beta[1],
             b[3] - alpha[2], b[3] - alpha[3], b[2] - a[0])
    m3 = min(m1, m2)
    return m0, m1, m2, m3


# ---------------------------------------------------------------- phi and delta

def orbit_F_multisets(c):
    """Distinct sorted 8-multisets {c_i : i in F} over the orbit."""
    out = set()
    for g in GROUP:
        gc = tuple(c[g[i]] for i in range(16))
        out.add(tuple(sorted(gc[i] for i in F_IDX)))
    return sorted(out)


def phi_data(c):
    """Return (base 8-multiset, list of orbit 8-multisets)."""
    base = tuple(sorted(c[i] for i in F_IDX))
    orb = orbit_F_multisets(c)
    # sanity: the sum over F is G-invariant (Zudilin's remark)
    s = sum(base)
    assert all(sum(o) == s for o in orb), "sum over F not G-invariant!"
    return base, orb


def delta_limit(alpha, beta, verbose=False):
    """delta = lim log Phi_n / n  for the direction (alpha, beta)."""
    c = c_matrix(alpha, beta)
    base, orb = phi_data(c)
    m0, m1, m2, m3 = m_params(alpha, beta)

    vals = sorted({v for v in base + tuple(x for o in orb for x in o) if v > 0})
    if not vals:
        return 0.0, 0.0, 0.0
    breaks = sorted({F(k, v) for v in vals for k in range(1, v + 1)})
    breaks = [b for b in breaks if b <= 1]
    if breaks[-1] != 1:
        breaks.append(F(1))
    prev = F(0)
    intervals = []          # (lo, hi, phi_value)
    for b in breaks:
        mid = (prev + b) / 2
        base_s = sum(floor(v * mid) for v in base)
        best = 0
        for o in orb:
            best = max(best, base_s - sum(floor(v * mid) for v in o))
        intervals.append((prev, b, best))
        prev = b

    # int_0^1 phi dpsi
    I1 = 0.0
    for lo, hi, ph in intervals:
        if ph == 0:
            continue
        I1 += ph * (digamma(float(hi)) - digamma(float(lo)))
    # int_0^{1/m3} phi dx/x^2  = sum phi * (1/lo - 1/hi)
    cut = F(1, m3)
    I2 = 0.0
    for lo, hi, ph in intervals:
        if ph == 0:
            continue
        a, bb = lo, min(hi, cut)
        if bb <= a:
            continue
        I2 += ph * (1.0 / float(a) - 1.0 / float(bb))
    if verbose:
        nz = [(str(lo), str(hi), ph) for lo, hi, ph in intervals if ph]
        print(f"    phi non-zero on {len(nz)} intervals, max phi = "
              f"{max(ph for _,_,ph in intervals)}")
    return I1 - I2, I1, I2


# ---------------------------------------------------------------- validation

def validate():
    print(f"[1] |G| = {len(GROUP)}   (expected 1920)")
    assert len(GROUP) == 1920

    print("[2] Rhin-Viola optimum (alpha;beta) = (18,17,16,19; 0,7,31,32)")
    alpha, beta = (18, 17, 16, 19), (0, 7, 31, 32)
    assert admissible(alpha, beta), "RV point not admissible?"
    m0, m1, m2, m3 = m_params(alpha, beta)
    d, I1, I2 = delta_limit(alpha, beta, verbose=True)
    budget = 2 * m1 + m2
    C0, C1 = 47.15472079, 48.46940964
    C2 = budget - d
    mu = (C0 + C1) / (C0 - C2)
    print(f"    m0={m0} m1={m1} m2={m2} m3={m3}  budget 2m1+m2 = {budget}")
    print(f"    int_0^1 phi dpsi = {I1:.8f},  int_0^(1/m3) = {I2:.8f}")
    print(f"    delta = {d:.8f}    (target 20.1879... from RV's mu)")
    print(f"    C2 = {C2:.8f}")
    print(f"    mu(zeta(3)) <= {mu:.8f}   (published 5.51389062)")
    print(f"    orbit size (distinct F-multisets) = {len(orbit_F_multisets(c_matrix(alpha,beta)))}")

    print("[3] totally symmetric (Apery/Ball) point (1,1,1,1; 0,0,2,2)")
    alpha, beta = (1, 1, 1, 1), (0, 0, 2, 2)
    c = c_matrix(alpha, beta)
    print(f"    c matrix entries = {set(c)}  -> orbit of F-multisets: "
          f"{len(orbit_F_multisets(c))}")
    m0, m1, m2, m3 = m_params(alpha, beta)
    d, I1, I2 = delta_limit(alpha, beta)
    print(f"    m1={m1} m2={m2} budget={2*m1+m2}  delta = {d:.8f}")
    print(f"    -> stabiliser is ALL of G; the group buys NOTHING at the "
          f"symmetric point.")
    return mu


if __name__ == "__main__":
    validate()
