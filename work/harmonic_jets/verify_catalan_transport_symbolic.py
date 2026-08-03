#!/usr/bin/env python3
"""Symbolic chain-rule certificate for the Catalan binomial transport.

SymPy represents the test series by an arbitrary function V(z).  The script
substitutes B(w)=(1+c*z)V(z), w=z/(1+c*z), into the original ordinary-
generating-function differential operator and proves that the result is exactly
the transported operator printed in equation (transportrec) of the paper.
"""

import sympy as sp


z, c = sp.symbols("z c")
v = sp.Function("V")(z)
w = z/(1 + c*z)


def theta_z(expr):
    return sp.expand(z*sp.diff(expr, z))


def theta_w(expr):
    # dw/dz=(1+c*z)^(-2), hence w*d/dw=z*(1+c*z)*d/dz.
    return sp.expand(z*(1 + c*z)*sp.diff(expr, z))


b_of_w = (1 + c*z)*v
original = (
    theta_w(theta_w(b_of_w))
    - w*(12*theta_w(theta_w(b_of_w)) + 12*theta_w(b_of_w) + 4*b_of_w)
    + 32*w**2*(theta_w(theta_w(b_of_w)) + 2*theta_w(b_of_w) + b_of_w)
)

a = 4 - c
b = 32 - 24*c + 3*c**2
d = c*(4 - c)*(8 - c)
transported = (
    theta_z(theta_z(v))
    - a*z*(3*theta_z(theta_z(v)) + 3*theta_z(v) + v)
    + b*z**2*(theta_z(theta_z(v)) + 2*theta_z(v) + v)
    + d*z**3*(theta_z(theta_z(v)) + 3*theta_z(v) + 2*v)
)

assert sp.simplify(original - transported) == 0
x = sp.symbols("X")
characteristic = x**3 - 3*(4-c)*x**2 + b*x + d
assert sp.expand(characteristic - (x-(8-c))*(x-(4-c))*(x+c)) == 0

print("symbolic OGF transport identity: exact")
print("characteristic factorization: (X-(8-c))(X-(4-c))(X+c)")
