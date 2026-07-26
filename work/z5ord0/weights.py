"""The three target weight elements, built from work/z5barnes/universal.py.

W_B = I22 + L_k I12 + L_l I21 + (L_k L_l - C_2) I11 ,
  C_r = H^(r)_{n+k+l} - H^(r)_{k+l},   A_r(x) = H^(r)_{n+x} - H^(r)_x,
  B_r(x) = H^(r)_{n-x} - H^(r)_x,      L_k = -A_1(k) - C_1 - 2 B_1(k).

Targets
  T1  w = coeff_zeta3(W_B)                       (weight 2)
  T2  w = -coeff_zeta2(W_B)/4 - w3sym            (weight 3)
  T3  w = -coeff_1(W_B)/2 - w5sym                (weight 5)
and the calibration
  T0  w = L_k + L_l   (the PROVED zeta(4) identity, Z5CF_BARNES section 7).

Everything is a dict {monomial : Fraction} in the bare letter alphabet
h{r}_{arg}, arg in n,k,l,pk,pl,mk,ml,kl,pkl.
"""
from fractions import Fraction as Fr

import o0core as C
from o0core import el_add, el_mul, el_scale, el_sigma, lname


def one():
    return {(): Fr(1)}


def lt(r, a, c=1):
    return {(lname(r, a),): Fr(c)}


def A(r, x):
    """A_r(k) = H^(r)_{n+k} - H^(r)_k ; x in 'k','l'."""
    return el_add(lt(r, 'p' + x), lt(r, x), -1)


def Bl(r, x):
    return el_add(lt(r, 'm' + x), lt(r, x), -1)


def Cr(r):
    return el_add(lt(r, 'pkl'), lt(r, 'kl'), -1)


def Lk():
    return el_add(el_add(el_scale(A(1, 'k'), Fr(-1)), Cr(1), -1),
                  Bl(1, 'k'), -2)


def Ll():
    return el_sigma(Lk())


# ------------------------------------------------------------------- T0 ------

def w_cal():
    """L_k + L_l -- the PROVED unwanted-zeta(4) identity (adequacy control)."""
    return el_add(Lk(), Ll())


# ------------------------------------------------------------------- T1 ------
# section 7 of Z5CF_BARNES (verified independently in w_check.py):
#   [z3] I11 = 2
#   [z3] I12 = 2(H_k - H_{k+l})          [z3] I21 = 2(H_l - H_{k+l})
#   [z3] I22 = 2(H2_k + H2_l - 2 H2_{k+l})

def z3_I11():
    return {(): Fr(2)}


def z3_I12():
    return el_scale(el_add(lt(1, 'k'), lt(1, 'kl'), -1), Fr(2))


def z3_I21():
    return el_sigma(z3_I12())


def z3_I22():
    return el_scale(el_add(el_add(lt(2, 'k'), lt(2, 'l')), lt(2, 'kl'), -2),
                    Fr(2))


def w_t1():
    lk, ll = Lk(), Ll()
    out = z3_I22()
    out = el_add(out, el_mul(lk, z3_I12()))
    out = el_add(out, el_mul(ll, z3_I21()))
    mid = el_add(el_mul(lk, ll), Cr(2), -1)
    out = el_add(out, el_mul(mid, z3_I11()))
    return {m: c for m, c in out.items() if c != 0}


# ------------------------------------------------------------ compact w3/w5 --

def compact_w3sym():
    """w3sym of work/z5barnes/verify_global.py (already k<->l symmetric)."""
    a1k, a1l = A(1, 'k'), A(1, 'l')
    b1k, b1l = Bl(1, 'k'), Bl(1, 'l')
    alpha = el_add(a1k, a1l, -1)
    beta = el_add(b1k, b1l, -1)
    psi = el_add(el_scale(alpha, Fr(1, 2)), beta)
    w3 = el_scale(el_add(lt(3, 'pk'), lt(3, 'pl')), Fr(1, 2))
    w3 = el_add(w3, el_mul(psi, el_add(lt(2, 'pk'), lt(2, 'pl'), -1)),
                Fr(-1, 2))
    return w3


def compact_w5sym():
    a1k, a1l = A(1, 'k'), A(1, 'l')
    b1k, b1l = Bl(1, 'k'), Bl(1, 'l')
    alpha = el_add(a1k, a1l, -1)
    beta = el_add(b1k, b1l, -1)
    psi = el_add(el_scale(alpha, Fr(1, 2)), beta)
    cc = el_add(el_scale(el_add(A(2, 'k'), A(2, 'l')), Fr(1, 4)),
                el_mul(alpha, psi), Fr(-1, 2))
    w5 = el_scale(el_add(lt(5, 'pk'), lt(5, 'pl')), Fr(1, 2))
    w5 = el_add(w5, el_mul(el_add(alpha, beta, -1),
                           el_add(lt(4, 'pk'), lt(4, 'pl'), -1)), Fr(1, 4))
    w5 = el_add(w5, el_mul(cc, el_add(lt(3, 'pk'), lt(3, 'pl'))), Fr(1, 2))
    return w5
