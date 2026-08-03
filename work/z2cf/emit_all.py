"""Emit the four cell-certificate component identities in minimally-cleared
polynomial form, as a Lean file of `ring` lemmas in two free rationals x (base index)
and y (summation index)."""
import sympy as sp
import pickle
import functools

import os
SP = os.path.dirname(os.path.abspath(__file__)) + '/'
n, k = sp.symbols('n k')
x, y = sp.symbols('x y')
cert = {a: sp.cancel(sp.sympify(b))
        for a, b in pickle.load(open(SP + 'cert.pkl', 'rb')).items()}

rho = lambda N, K: K**2 + K*(1 + 6*N) - 4 - 15*N - 11*N**2
Pz = lambda t: 11*t**2 + 11*t + 3
Qz = lambda t: 625*t**4 + 7250*t**3 + 31245*t**2 + 59264*t + 41752
p = [sp.expand((n+1)*(n+2)*Qz(n)),
     sp.expand(6875*n**6 + 100375*n**5 + 597195*n**4 + 1849309*n**3
               + 3136850*n**2 + 2758284*n + 981880),
     sp.expand(-(n+3)*(n+4)*Qz(n-1))]
r = (n-k)**2*(n+k+1)/(k+1)**3


def sig(j):
    e = sp.Integer(1)
    for t in range(1, j+1):
        e *= (n+t)*(n+t+k)/(n+t-k)**2
    return e


Lc = [-(n+1)**2, -Pz(n+1), (n+2)**2]
m_ = []
for j in range(5):
    e = sp.Integer(0)
    for i in range(3):
        if 0 <= j-i <= 2:
            e += p[i]*Lc[j-i].subs(n, n+i)
    m_.append(sp.expand(e))

chi, gam, bet, alp = cert['chi'], cert['gamma'], cert['beta'], cert['alpha']
chip, gamp, betp = [e.subs(k, k+1) for e in (chi, gam, bet)]
Sig = sum(m_[j]*sig(j) for j in range(5))
s1 = lambda j: sum(sp.Integer(1)/(n+t-k) for t in range(1, j+1))
tt = lambda j: sum(sp.Integer(1)/(n+t) for t in range(1, j+1))
s2 = lambda j: sum(sp.Integer(1)/(n+t)**2 for t in range(1, j+1))
A1 = -sum(m_[j]*sig(j)*(s1(j)+tt(j)) for j in range(5))
A0 = sum(m_[j]*sig(j)*s2(j) for j in range(5))
u, v = 1/(k+1), 1/(n-k)

# each component: a list of signed rational terms whose sum is identically zero
COMPS = {
    'chi':   [r*chip, -chi, -Sig],
    'gamma': [r*gamp, -gam, -r*chip*u],
    'beta':  [r*betp, -bet, -A1, 4*r*chip*u, r*chip*v],
    'alpha': [r*alp.subs(k, k+1), -alp, -A0, 2*r*chip*u**2, r*chip*u*v,
              r*betp*u, -r*gamp*v],
}

DOC = {
    'chi': 'r(y)*X(y+1) - X(y) = Sigma(y)  --- the Zeilberger antidifference cofactor '
           'of the pre-operated row.',
    'gamma': 'r(y)*C(y+1) - C(y) = r(y)*X(y+1)/(y+1)  --- the H_(n-k) and H_n component '
             '(both give the same equation).',
    'beta': 'r(y)*B(y+1) - B(y) = A1(y) - 4 r(y) X(y+1)/(y+1) - r(y) X(y+1)/(x-y)  --- '
            'the H_k component.',
    'alpha': 'r(y)*A(y+1) - A(y) = A0(y) - 2 r X(y+1)/(y+1)^2 - r X(y+1)/((y+1)(x-y)) '
             '- r B(y+1)/(y+1) + r C(y+1)/(x-y)  --- the constant component.',
}


def clear(terms):
    terms = [sp.cancel(sp.together(t.subs({n: x, k: y}))) for t in terms]
    dens = [sp.fraction(t)[1] for t in terms]
    D = functools.reduce(sp.lcm, dens)
    polys = [sp.expand(sp.cancel(t*D)) for t in terms]
    polys = [q for q in polys if q != 0]
    g = functools.reduce(sp.gcd, polys)
    polys = [sp.expand(sp.cancel(q/g)) for q in polys]
    assert sp.expand(sum(polys)) == 0
    return polys, g


def L(e):
    return str(e).replace('**', '^')


out = ['''/-
# The four cell-certificate component identities for the minimal ζ(2) companion

Machine-generated from `work/z2cf/lean_certificate.py` (see `work/Z2_MINIMAL_LEAN.md`).

Each lemma is the **minimally-cleared** polynomial form of one letter-monomial component of
the cell identity `star_z2`, stated in two free rationals `x` (the base index `n`) and `y`
(the summation index `k`).  Minimal clearing matters: the naive `field_simp; ring` on the
rational form of even the smallest component exhausts several gigabytes without closing.

Writing `r(y) = (x−y)²(x+y+1)/(y+1)³ = S(x,y+1)/S(x,y)` and `X, C, B, A` for the certificate
cofactors `χ, γ, β, α`, the four components are the equations recorded in each docstring.
-/
import Mathlib

namespace ZetaLucas
''']

for tag in ('chi', 'gamma', 'beta', 'alpha'):
    polys, g = clear(COMPS[tag])
    tot = sum(len(sp.Poly(q, x, y).terms()) for q in polys)
    deg = max(sp.Poly(q, x, y).total_degree() for q in polys)
    print(tag, ': %d terms, %d monomials total, max degree %d' % (len(polys), tot, deg))
    body = ' + '.join('(%s)' % L(q) for q in polys)
    out.append('''
set_option maxRecDepth 1000000 in
set_option maxHeartbeats 4000000 in
/-- `%s`

Cleared by the common factor `%s`. -/
theorem z2cert_%s (x y : ℚ) :
    %s = 0 := by ring
''' % (DOC[tag], L(sp.factor(g)), tag, body))

out.append('\nend ZetaLucas\n')
src = ''.join(out)
open(SP + 'Z2Cert.lean', 'w').write(src)
print('written %d bytes' % len(src))
