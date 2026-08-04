"""eps40_gate.py -- GATE A/B for the epsilon-analytic bridge route.

GATE A: realize the family-1 deformation as an honest meromorphic gamma
product: for each of the 9 letters L find INTEGER shift multiplicities
c_{L,j}, j = 1..J, with

    sum_j c_{L,j} j^m  =  etilde_m(L) := 2^m e_m(L),   m = 1..5,

so that with delta = eps/2

    T_eps(n,k,l) = T * prod_L prod_j [ Gamma(x_L+1+j*delta) /
                                       (Gamma(x_L+1) Gamma(1+j*delta)) ]^{c_{L,j}}

reproduces T * exp(sum_m eps^m L_m) exactly.  Control: the finite double sum's
eps^3/eps^5 coefficients must reproduce  -t*(Q zeta3 - Phat)  and
-t5*(Q zeta5 - P)  (un-normalized variant: DROP the Gamma(1+j delta)
normalizers and the zeta content appears through C(eps)).

GATE B: continuation cells (k>n or l>n) are finite for eps != 0 through the
gamma realization; measure the eps-order of the tail sum.  Tail order >= 6
means the finite sum IS the analytic object through eps^5.

Numerics: mpmath, high precision, Richardson-style extraction of Taylor
coefficients from a small-eps stencil.
"""

import sys, json
from fractions import Fraction as F

import mpmath as mp
import sympy as sp

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import core

mp.mp.dps = 60

# ---------------- letter tables (family 1, t = 1; from eps22) ----------------
Ll = [F(0), F(0), F(3), F(0), F(-1), F(0), F(-2), F(1), F(-1)]
L1 = [2 * v for v in Ll]
L2 = [F(-4), F(-8), F(10), F(-17, 4), F(-7, 4), F(0), F(8), F(2), F(-2)]
L3 = [F(0), F(0), F(24), F(0), F(-5, 3), F(0), F(-64, 3), F(8, 3), F(-8, 3)]
L4 = [F(0), F(-68), F(68), F(31, 32), F(-31, 32), F(-64), F(64), F(4), F(-4)]
L5 = [F(0), F(528, 5), F(528, 5), F(37, 40), F(37, 40), F(-512, 5),
      F(-512, 5), F(32, 5), F(-32, 5)]
COEF = [L1, L2, L3, L4, L5]
NA = 9
ARGNM = ['n', 'k', 'l', 'n+k', 'n+l', 'n-k', 'n-l', 'k+l', 'n+k+l']

# e_m(L) = (-1)^(m-1) * m * coeff_m(L);  etilde_m = 2^m e_m  (delta = eps/2)
ETILDE = {}
for a in range(NA):
    v = []
    for m in range(1, 6):
        e = F((-1) ** (m - 1) * m) * COEF[m - 1][a]
        et = F(2) ** m * e
        v.append(et)
    ETILDE[a] = v

print('etilde integrality check:')
allint = True
for a in range(NA):
    ints = [x.denominator == 1 for x in ETILDE[a]]
    if not all(ints):
        allint = False
    print('  %-6s' % ARGNM[a], [str(x) for x in ETILDE[a]],
          'OK' if all(ints) else 'NON-INTEGER')
if not allint:
    sys.exit('scaled e-table not integral -- change delta scaling')

# ---------------- integer shift solve: sum_j c_j j^m = etilde_m ----------------
J = 10
M = sp.Matrix(5, J, lambda m, j: (j + 1) ** (m + 1))
SHIFTS = {}
for a in range(NA):
    target = sp.Matrix([int(x) for x in ETILDE[a]])
    # particular rational solution using j=1..5 Vandermonde block
    V = M[:, :5]
    cpart = V.solve(target)
    # kernel of M over Q, then clear denominators using integer kernel moves
    ker = M.nullspace()
    # integer solve via Smith normal form of M
    from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
    # Solve M c = target over Z: use sympy diophantine-style via HNF of M^T
    # Simple approach: HNF H = M * U (column ops, U unimodular);
    # solve H y = target (H lower-triangular-ish), c = U y.
    Mt = sp.Matrix(M)
    # sympy hermite_normal_form works on integer matrices, returns HNF of rows;
    # use transpose trick
    H = hermite_normal_form(Mt.T).T          # H = column-style HNF, H = M*U'
    # find U with M*U = H by solving (requires care); fallback: brute search
    sol = None
    # brute: adjust cpart by rational kernel combos with small denominators
    dens = sp.ilcm(*[sp.denom(x) for x in cpart]) if cpart else 1
    if dens == 1:
        sol = list(cpart) + [0] * (J - 5)
    else:
        # search small integer combos of nullspace to clear denominators
        import itertools
        kb = [sp.Matrix(list(k)) for k in ker]
        rng = range(-6, 7)
        base = sp.Matrix(list(cpart) + [0] * (J - 5))
        found = False
        for combo in itertools.product(rng, repeat=len(kb)):
            cand = base + sum((c * k for c, k in zip(combo, kb)),
                              sp.zeros(J, 1))
            if all(sp.denom(x) == 1 for x in cand):
                sol = list(cand)
                found = True
                break
        if not found:
            sys.exit('no small integer shift solution for letter ' + ARGNM[a])
    # verify
    chk = M * sp.Matrix(sol)
    assert list(chk) == [int(x) for x in ETILDE[a]], (ARGNM[a], sol)
    SHIFTS[a] = [int(x) for x in sol]
    print('  shifts %-6s' % ARGNM[a], SHIFTS[a])

# ---------------- deformed cell via gamma products ----------------
def cell(n, k, l, eps):
    """T_eps(n,k,l), normalized variant (with Gamma(1+j delta) divisors)."""
    d = eps / mp.mpf(2)
    xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
    val = mp.mpf(core.T(n, k, l)) if min(n - k, n - l) >= 0 else None
    # continuation: build T itself from gammas too
    logv = mp.mpf(0)
    # log T from gammas (continuation-safe): use loggamma of positive args
    # T = G(n+k+1)G(n+l+1)G(n+k+l+1)G(n+1)/[G(k+1)^3 G(l+1)^3
    #      G(n-k+1)^2 G(n-l+1)^2 G(k+l+1)]
    num = [n + k, n + l, n + k + l, n]
    den3 = [k, l]
    den2 = [n - k, n - l]
    den1 = [k + l]
    def lg(x, shift=0):
        return mp.loggamma(x + 1 + shift) if x + 1 + shift > 0 else \
            mp.log(abs(mp.gamma(x + 1 + shift)))
    # for continuation cells n-k+1 <= 0: gamma pole -> handled by shifts below;
    # compute the WHOLE product cellwise with shifts folded in per letter
    tot = mp.mpf(1)
    POW = {0: 1, 1: -3, 2: -3, 3: 1, 4: 1, 5: -2, 6: -2, 7: -1, 8: 1}
    for a in range(NA):
        x = xs[a]
        p = POW[a]
        # base letter power p, then multiply the shift realization
        cshifts = SHIFTS[a]
        stot = sum(cshifts)
        # prod_j [G(x+1+jd)/G(x+1)]^{c_j} * G(x+1)^p
        #  = G(x+1)^{p-stot_..} etc; combine to avoid 0/0 at continuation:
        acc = mp.mpf(1)
        base_pow = p
        for j, c in enumerate(cshifts, start=1):
            if c == 0:
                continue
            acc *= (mp.gamma(x + 1 + j * d) / mp.gamma(1 + j * d)) ** c
            base_pow -= c
        acc *= mp.gamma(x + 1) ** base_pow
        tot *= acc
    return tot

def cell_ctrl(n, k, l, eps):
    """control: T * exp(sum eps^m L_m) for in-range cells."""
    xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
    H = core.Hs
    s = mp.mpf(0)
    for m in range(1, 6):
        lm = sum(mp.mpf(str(COEF[m - 1][a].numerator))
                 / mp.mpf(str(COEF[m - 1][a].denominator))
                 * mp.mpf(str(H(xs[a], m).numerator))
                 / mp.mpf(str(H(xs[a], m).denominator))
                 for a in range(NA))
        s += eps ** m * lm
    return core.T(n, k, l) * mp.e ** s

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    eps = mp.mpf('0.001')

    # ---- realization check on a few cells ----
    print('\nGATE A0: gamma realization == exp(series) on cells (rel err):')
    worst = 0
    for (k, l) in [(0, 0), (1, 0), (n, n), (1, n)]:
        c1 = cell(n, k, l, eps)
        c2 = cell_ctrl(n, k, l, eps)
        rel = abs(c1 - c2) / abs(c2)
        worst = max(worst, rel)
        print('  cell(%d,%d): rel diff %.3e' % (k, l, rel))
    print('  worst:', mp.nstr(worst, 3),
          '(should be ~eps^6 ~ 1e-18 level, NOT eps^1)')

    # ---- GATE B: tail cells ----
    print('\nGATE B: continuation-cell magnitudes (k>n), eps=%s:' % eps)
    for (k, l) in [(n + 1, 0), (n + 1, n), (n + 2, 1), (n + 1, n + 1)]:
        v = cell(n, k, l, eps)
        print('  cell(%d,%d) = %s' % (k, l, mp.nstr(v, 5)))
    print('scaling in eps (cell(n+1,0)):')
    for e2 in ['0.001', '0.0005', '0.00025']:
        v = cell(n, n + 1, 0, mp.mpf(e2))
        print('  eps=%s  -> %s' % (e2, mp.nstr(v, 6)))
