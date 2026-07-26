"""Emit the order-7 certificate in the LEAN_Z5_SCAFFOLD 5.5-5.6 shape.

What this file can emit EXACTLY today:

  * the operator          L_min = A . L_BZ ,  A = sum_{t=0}^{4} a_t(n) S_n^t
  * the base              Phi_7, P_i^(7), ghat_k^(7), ghat_l^(7)
  * the monomial basis    M_1 .. M_15
  * the SEVEN Theorem-R blocks  (j in supp(w3hat)) in PRE-FACTORED product form
        r_j = w_j * sum_{t=0}^{4} a_t(n) * rQ(n+t,k,l) * Q_t(n,k,l)
        s_j = w_j * sum_{t=0}^{4} a_t(n) * sQ(n+t,k,l) * Q_t(n,k,l)
        Q_t = prod_{j=1..t}(n+j)(n+k+j)(n+l+j)(n+k+l+j)
              * prod_{j=t+4..7}(n+j-k)^2 (n+j-l)^2                (a POLYNOMIAL)
    and the seven identities they satisfy, which are integer combinations of the
    already-certified Q-row Phi-identity at n, n+1, ..., n+4.
  * an exact-Q residual check of those seven identities.

The eight residual blocks are NOT emitted: they are pinned mod p only (see
work/Z5CF_LIFT.md).
"""
import json, os, pickle, sys
from fractions import Fraction as Fr
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
n, k, l = sp.symbols('n k l')


def Qt(t, m=7):
    """P_t^(m) / P_0^(3)(n+t)  --  a polynomial, product of linear forms."""
    v = sp.Integer(1)
    for j in range(1, t + 1):
        v *= (n + j) * (n + k + j) * (n + l + j) * (n + k + l + j)
    for j in range(t + 4, m + 1):
        v *= (n + j - k) ** 2 * (n + j - l) ** 2
    return v


def Pim(i, m=7):
    v = sp.Integer(1)
    for j in range(1, i + 1):
        v *= (n + j) * (n + k + j) * (n + l + j) * (n + k + l + j)
    a = sp.Integer(1); b = sp.Integer(1)
    for j in range(i + 1, m + 1):
        a *= (n + j - k); b *= (n + j - l)
    return v * a ** 2 * b ** 2


def apoly(Z, t):
    return sum(sp.Integer(c) * n ** i for i, c in enumerate(Z[t]))


def qrow_exact():
    sys.path.insert(0, HERE)
    import qrow
    return qrow.exact()          # (r_num, r_den, s_num, s_den)


def poly_json(e, vars=(n, k, l)):
    P = sp.Poly(sp.expand(e), *vars)
    return {'vars': [str(v) for v in vars],
            'terms': [[list(mo), str(co)] for mo, co in zip(P.monoms(), P.coeffs())]}


def build(Z):
    rn, rd, sn, sd = qrow_exact()
    out = {}
    out['operator'] = {
        'L_min': 'A . L_BZ,  order 7',
        'A': 'sum_{t=0}^{4} a_t(n) S_n^t',
        'a': [[str(c) for c in Z[t]] for t in range(5)],
        'L_BZ': {'c0': '(n+1)^5 (n+2) a0(n+1)', 'c1': '-2 (n+2) B8(n)',
                 'c2': '-2 B9(n)', 'c3': '2 (n+3)^5 (2n+5) a0(n)',
                 'a0': '41218 n^3 + 198849 n^2 + 320790 n + 173057'},
    }
    out['base'] = {
        'Phi_7': 'T(n+7,k,l) / prod_{j=1..7} (n+j)(n+k+j)(n+l+j)(n+k+l+j)',
        'T(n+i,k,l)': 'Phi_7 * P_i^(7)',
        'P_i^(7)': ('prod_{j=1..i}(n+j)(n+k+j)(n+l+j)(n+k+l+j) '
                    '* [prod_{j=i+1..7}(n+j-k)]^2 [prod_{j=i+1..7}(n+j-l)]^2'),
        'ghat_k': '(n+7-k)^2 (n+k+1)(n+k+l+1) / [(k+1)^3 (k+l+1)]',
        'ghat_l': '(n+7-l)^2 (n+l+1)(n+k+l+1) / [(l+1)^3 (k+l+1)]',
        'letters_base': ('H^(r)_{n+k}, H^(r)_{n+l}, H^(r)_k, H^(r)_l at base n; '
                         'H^(1)_{n-k}, H^(1)_{n-l} MIXED, i.e. based at n+7'),
        'shift_lemmas_used': ['T_shift_k', 'T_shift_l', 'T_shift_n', 'T_shift_n2',
                              'T_shift_n3', 'Phi (D1 at order 7)'],
    }
    out['monomials'] = ['*'.join(m) if m else '1' for m in MB]
    out['theoremR'] = {
        'Q_t': [str(sp.factor(Qt(t))) for t in range(5)],
        'rQ_num': poly_json(rn), 'rQ_den': poly_json(rd),
        'sQ_num': poly_json(sn), 'sQ_den': poly_json(sd),
        'formula': ('r_j = w_j sum_t a_t(n) rQ(n+t,k,l) Q_t(n,k,l),  '
                    's_j likewise;  j in supp(w3hat)'),
        'w': {('*'.join(m) if m else '1'): str(WT[m]) for m in WT},
    }
    return out


MB = None
WT = None


def _basis():
    global MB, WT
    sys.path.insert(0, HERE)
    import zla
    F = zla.FQ()
    w = zla.weight_element(F, 'w3')
    MB = zla.closure_basis(w)
    WT = dict(w)


def residual_check(Z, pts):
    """the SEVEN Theorem-R identities, exactly over Q, at integer (n,k,l)."""
    rn, rd, sn, sd = qrow_exact()
    gk = (n + 7 - k) ** 2 * (n + k + 1) * (n + k + l + 1) / ((k + 1) ** 3 * (k + l + 1))
    gl = (n + 7 - l) ** 2 * (n + l + 1) * (n + k + l + 1) / ((l + 1) ** 3 * (k + l + 1))
    A = [apoly(Z, t) for t in range(5)]
    sys.path.insert(0, HERE)
    import zla
    bad = 0; done = 0
    for (N, K, L) in pts:
        sub = {n: N, k: K, l: L}
        try:
            R = sum(A[t].subs(n, N) * (rn / rd).subs({n: N + t, k: K, l: L})
                    * Qt(t).subs(sub) for t in range(5))
            Rk = sum(A[t].subs(n, N) * (rn / rd).subs({n: N + t, k: K + 1, l: L})
                     * Qt(t).subs({n: N, k: K + 1, l: L}) for t in range(5))
            S = sum(A[t].subs(n, N) * (sn / sd).subs({n: N + t, k: K, l: L})
                    * Qt(t).subs(sub) for t in range(5))
            Sl = sum(A[t].subs(n, N) * (sn / sd).subs({n: N + t, k: K, l: L + 1})
                     * Qt(t).subs({n: N, k: K, l: L + 1}) for t in range(5))
            lhs = sp.nsimplify(gk.subs(sub) * Rk - R + gl.subs(sub) * Sl - S)
            rhs = 0
            for t in range(5):
                C = zla.cc(N + t)
                rhs += A[t].subs(n, N) * sum(C[u] * Pim(t + u).subs(sub) for u in range(4))
            if sp.simplify(lhs - rhs) != 0: bad += 1
            done += 1
        except ZeroDivisionError:
            continue
    return done, bad


def shift_table():
    import o_sym
    B, w, S = o_sym.matrices()
    out = {}
    for d in ('k', 'l'):
        ent = []
        for i in range(len(B)):
            for j in range(len(B)):
                if i != j and S[d][i, j] != 0:
                    ent.append(['M_%d' % (i + 1), 'M_%d' % (j + 1),
                                str(sp.factor(S[d][i, j]))])
        out['S_' + d] = ent
    return out


if __name__ == '__main__':
    _basis()
    fn = os.path.join(HERE, 'a_lift.pkl')
    Z = pickle.load(open(fn, 'rb'))['Z'] if os.path.exists(fn) else None
    d = build(Z if Z else [[0]] * 5)
    if Z is None:
        d['operator']['a'] = 'NOT YET LIFTED -- see work/Z5CF_LIFT.md 2.3'
    d['shift_table'] = shift_table()
    d['residual_blocks'] = ('NOT DELIVERED -- pinned mod p only; see '
                            'work/Z5CF_LIFT.md 4 for why they are not Lean-sized')
    json.dump(d, open(os.path.join(HERE, 'z5cf_order7_partial.json'), 'w'), indent=1)
    print('wrote z5cf_order7_partial.json')
    if Z is not None:
        pts = [(N, K, L) for N in range(0, 5) for K in range(0, 5) for L in range(0, 5)]
        done, bad = residual_check(Z, pts)
        print('Theorem-R identities checked exactly in Q at %d pole-free points: '
              '%d failures' % (done, bad))
