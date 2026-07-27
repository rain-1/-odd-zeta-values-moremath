"""xyjets.py -- genuinely two-variable pole-raising jets.

For rho(x), sigma(y) monomials in the lattice blocks
  QX_r = sum_{k'=0}^n (x+k')^{-r},  RX1 = sum_{i=1}^n (x-i)^{-1}
(and mirrors in y), the function R(x,y) rho(x) sigma(y) is O(x^-2) in x for
each fixed y with poles only at the x-lattice (RX1's poles at x=i are killed
by R(i,y)=0), and vice versa.  Hence the sum of iterated residues over the
whole grid vanishes:

   0 = sum_{k,l} Res_{y=-l} Res_{x=-k} [ R rho sigma ]
     = sum_{k,l} A_kl * u_{rho,sigma}(n,k,l),

so u is a Sigma T-null weight (A_kl = T times an n-only factor).  u is the
[x^1 y^1] coefficient of E2(x,y) * rhoser(x) * sigmaser(y), where E2 is the
normalised local germ

   E2 = exp( sum_m alpha_m(k) x^m + beta_m(l) y^m + gamma_m(k+l) (x+y)^m ),

   alpha_m = -(1/m)(H^m_{n+k}-H^m_k) + 2(-1)^m/m (H^m_{n-k}+(-1)^m H^m_k),
   beta_m  = mirror (l),
   gamma_m = -(1/m)(H^m_{n+k+l}-H^m_{k+l}),

all bare forms in the eps22 letter model (args 0..8).  These functionals are
NOT per-fixed-variable null in the bare model (they fail the per-(n,k)
Phi-calibration), i.e. they are genuinely two-variable mechanisms.
"""
import sys
from fractions import Fraction as F
from math import comb

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')

from eps24 import f_add, f_scale, f_mul, ONE, L, f_weight

DX = 4   # max per-axis degree tracked (final extraction is [x^1 y^1] and
         # block orders are <= 3 per axis)
WMAX = 5  # total weight cap: only weight-5 forms survive to the extraction

# ---------------- 2-var series: dict[(dx,dy)] -> form -------------------
def s2_mul(s1, s2, dmax=DX):
    out = {}
    for (a1, b1), f1 in s1.items():
        for (a2, b2), f2 in s2.items():
            a, b = a1 + a2, b1 + b2
            if a > dmax or b > dmax:
                continue
            pr = f_mul(f1, f2)
            key = (a, b)
            out[key] = f_add(out[key], pr) if key in out else pr
    return {k: v for k, v in out.items() if v}

def s2_exp(ls, dmax=DX):
    """exp of a 2-var series with no constant term, truncated; positive
    keys only, so total degree = coefficient weight <= WMAX suffices."""
    E = {(0, 0): dict(ONE)}
    term = {(0, 0): dict(ONE)}
    for j in range(1, 2 * dmax + WMAX):
        term = s2_mul(term, ls, dmax)
        term = {k: f_scale(v, F(1, j)) for k, v in term.items()
                if k[0] + k[1] <= WMAX}
        if not term:
            break
        for k, v in term.items():
            E[k] = f_add(E[k], v) if k in E else dict(v)
    return E

# ---------------- germ jets (bare forms, eps22 arg indexing) -------------
# args: 0:n 1:k 2:l 3:n+k 4:n+l 5:n-k 6:n-l 7:k+l 8:n+k+l
def alpha_m(m, side):
    """side='x' uses (k, n+k, n-k); side='y' uses (l, n+l, n-l)."""
    a_k, a_pk, a_mk = (1, 3, 5) if side == 'x' else (2, 4, 6)
    # -(1/m)(H_{n+k}-H_k) - 2*(-1)^(m-1)/m * (H_{n-k} + (-1)^m H_k)
    f = f_scale(f_add(L(m, a_pk), L(m, a_k), F(-1)), F(-1, m))
    f = f_add(f, f_add(L(m, a_mk), L(m, a_k), F((-1) ** m)),
              F(-2 * (-1) ** (m - 1), m))
    return f

def gamma_m(m):
    return f_scale(f_add(L(m, 8), L(m, 7), F(-1)), F(-1, m))

def germ_log(wmax=WMAX, dmax=DX):
    ls = {}
    for m in range(1, wmax + 1):
        if m <= dmax:
            ls[(m, 0)] = f_add(ls.get((m, 0), {}), alpha_m(m, 'x'))
            ls[(0, m)] = f_add(ls.get((0, m), {}), alpha_m(m, 'y'))
        g = gamma_m(m)
        for i in range(0, m + 1):
            if i > dmax or m - i > dmax:
                continue
            key = (i, m - i)
            ls[key] = f_add(ls.get(key, {}), f_scale(g, F(comb(m, i))))
    return {k: v for k, v in ls.items() if v}

E2 = s2_exp(germ_log())

# ---------------- block series -------------------------------------------
def S3form(m, side):
    """sum_{k'!=k} (k'-k)^{-m} = H^m_{n-k} + (-1)^m H^m_k  (x-side)."""
    a_k, a_mk = (1, 5) if side == 'x' else (2, 6)
    return f_add(L(m, a_mk), L(m, a_k), F((-1) ** m))

def block_QX(r, side, dmax=DX):
    var = 0 if side == 'x' else 1
    s = {}
    key0 = (-r, 0) if side == 'x' else (0, -r)
    s[key0] = dict(ONE)
    for m in range(0, dmax + r + 1):
        c = F((-1) ** m * comb(m + r - 1, r - 1))
        key = (m, 0) if side == 'x' else (0, m)
        s[key] = f_add(s.get(key, {}), f_scale(S3form(m + r, side), c))
    return s

def block_RX1(side, dmax=DX):
    """sum_{i=1}^n 1/(x-i) at x=-k+x':  -sum_m x'^m (H^{m+1}_{n+k}-H^{m+1}_k)."""
    a_k, a_pk = (1, 3) if side == 'x' else (2, 4)
    s = {}
    for m in range(0, dmax + 2):
        f = f_scale(f_add(L(m + 1, a_pk), L(m + 1, a_k), F(-1)), F(-1))
        key = (m, 0) if side == 'x' else (0, m)
        s[key] = f
    return s

def xy_form(xmono, ymono):
    """[x^1 y^1] of E2 * prod(xblocks) * prod(yblocks)  -- the null weight."""
    s = E2
    for b in xmono:
        s = s2_mul(s, b)
    for b in ymono:
        s = s2_mul(s, b)
    return s.get((1, 1), {})

def menu():
    """(name, form) for wt(rho)+wt(sigma) = 3 (form weight 5)."""
    def xmonos(w, side):
        Q1 = block_QX(1, side); Q2 = block_QX(2, side)
        Q3 = block_QX(3, side); R1 = block_RX1(side)
        if w == 0:
            return [('1', [])]
        if w == 1:
            return [('Q1', [Q1]), ('R1', [R1])]
        if w == 2:
            return [('Q2', [Q2]), ('Q1Q1', [Q1, Q1]), ('R1Q1', [R1, Q1])]
        if w == 3:
            return [('Q3', [Q3]), ('Q1Q2', [Q1, Q2]), ('Q1Q1Q1', [Q1, Q1, Q1]),
                    ('R1Q2', [R1, Q2]), ('R1Q1Q1', [R1, Q1, Q1])]
    out = []
    for wx in range(0, 4):
        wy = 3 - wx
        for nx, bx in xmonos(wx, 'x'):
            for ny, by in xmonos(wy, 'y'):
                f = xy_form(bx, by)
                if f:
                    wchk = f_weight(f)
                    assert wchk == {5}, (nx, ny, wchk)
                    out.append(('XY[%s|%s]' % (nx, ny), f))
    return out

if __name__ == '__main__':
    M = menu()
    print('XY columns:', len(M))
    # exact nullcheck: sum_{k,l} T * u = 0
    from fractions import Fraction as Fr
    import core
    H = core.Hs
    def ev(f, n, k, l):
        xs = [n, k, l, n + k, n + l, n - k, n - l, k + l, n + k + l]
        tot = Fr(0)
        for mo, c in f.items():
            v = Fr(c)
            for (r, a) in mo:
                v *= H(xs[a], r)
            tot += v
        return tot
    for n in (2, 3, 4):
        bad = []
        for nm, f in M:
            s = sum(core.T(n, k, l) * ev(f, n, k, l)
                    for k in range(n + 1) for l in range(n + 1))
            if s != 0:
                bad.append((nm, s))
        print('n=%d: bad %d/%d' % (n, len(bad), len(M)),
              bad[:4] if bad else '')
