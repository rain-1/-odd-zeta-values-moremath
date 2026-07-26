"""The desingularised order-4 left multiple  L-tilde  of L_BZ (PHASE2_NUCLEUS 3.3)
expressed in the A.L_BZ family:   A = a_0 + a_1 S_n ,  (a_0,a_1) ~ (-lambda(n+1), 1).

  lambda(nu) = (392627556035671426586 nu^2 + 1282015597875460006266 nu
                + 1052781309790247665282) / D ,   D = 3641620092914355321

Verified here against work/p1h/desing_coeffs.json coefficient by coefficient.
"""
import sys, json
from fractions import Fraction as Fr
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import zla

LD = 3641620092914355321
LC = (392627556035671426586, 1282015597875460006266, 1052781309790247665282)


def lam(nu):
    return Fr(LC[0] * nu * nu + LC[1] * nu + LC[2], LD)


def avec(n, p):
    """(a_0, a_1) mod p, normalised a_1 = 1"""
    x = -lam(n + 1)
    return [x.numerator % p * pow(x.denominator % p, p - 2, p) % p, 1 % p]


def dcoeffs(nu):
    """L-tilde's d_i(nu), i = 0..4, from the recorded json (sympy srepr)"""
    import sympy as sp
    d = json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/p1h/desing_coeffs.json'))
    v = sp.Symbol('nu')
    return [sp.sympify(x).subs(v, nu) for x in d]


def check(nu):
    """L-tilde row  ==  const * (a_0 row(nu-1) + a_1 row(nu)) ?"""
    n = nu - 1
    a0 = -lam(nu); a1 = Fr(1)
    c_n = [Fr(x) for x in zla.cc(n)]        # acts on Y_n .. Y_{n+3}
    c_n1 = [Fr(x) for x in zla.cc(n + 1)]   # acts on Y_{n+1} .. Y_{n+4}
    row = [Fr(0)] * 5
    for u in range(4):
        row[u] += a0 * c_n[u]
        row[u + 1] += a1 * c_n1[u]
    d = [Fr(int(x)) for x in dcoeffs(nu)]
    rat = None
    ok = True
    for i in range(5):
        if row[i] == 0 and d[i] == 0:
            continue
        if row[i] == 0 or d[i] == 0:
            ok = False
            break
        q = d[i] / row[i]
        if rat is None:
            rat = q
        elif q != rat:
            ok = False
    return ok, rat


if __name__ == '__main__':
    for nu in (3, 5, 8, 11):
        ok, rat = check(nu)
        print('nu=%2d : L-tilde == const * (a_0 L_BZ|_{nu-1} + a_1 L_BZ|_nu)  -> %s'
              % (nu, 'YES' if ok else 'NO'))
    p = 4194301
    for n in (5, 9):
        print('n=%d  avec mod %d = %s' % (n, p, avec(n, p)))
