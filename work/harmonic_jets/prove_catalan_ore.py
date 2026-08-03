#!/usr/bin/env python3
"""Exact Ore-algebra reduction for the Catalan harmonic companion.

Run with the PassageMath/ore_algebra environment installed at
    /home/ubuntu/.local/opt/harmonic-ore/bin/python

The optional analytic Cython extensions of ore_algebra are not used.
"""

import sage.all__sagemath_combinat  # initializes the modular Sage namespace

from fractions import Fraction as F
from hashlib import sha256
from math import comb

from sage.rings.finite_rings.finite_field_constructor import GF
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
from sage.rings.rational_field import QQ

from ore_algebra import OreAlgebra
from ore_algebra.guessing import guess_raw


def scalar_operators():
    rn = PolynomialRing(QQ, "n")
    n = rn.gen()
    an = OreAlgebra(rn, "Sn")
    sn = an.gen()

    # c_k=C(2k,k), a_k=c_k(3H_k/4-H_2k/2),
    # d_k=c_k K_2k^(1), e_k=c_k(K_2k^(2)/2+A_k K_2k^(1)).
    rc = (n + 1) * sn - 2 * (2 * n + 1)
    ra = (4 * (n + 1) * (2 * n + 1) ** 2
          - 2 * (4 * n**3 + 12 * n**2 + 10 * n + 1) * sn
          + n * (n + 2) ** 2 * sn**2)
    rd = (-4 * (2 * n + 1) ** 2 - 4 * (n + 1) * sn
          + (n + 1) * (n + 2) * sn**2)

    p0 = (16 * (2*n + 1)**3 * (2*n + 3)
          * (8*n**5 + 84*n**4 + 336*n**3 + 628*n**2 + 522*n + 129))
    p1 = (32 * (2*n + 3)
          * (16*n**7 + 184*n**6 + 832*n**5 + 1824*n**4
             + 1782*n**3 + 48*n**2 - 1215*n - 660))
    p2 = (-8 * (32*n**9 + 528*n**8 + 3704*n**7 + 14356*n**6
                + 33332*n**5 + 46676*n**4 + 36898*n**3
                + 12653*n**2 - 1179*n - 1431))
    p3 = (-8 * (n + 3)**2
          * (8*n**6 + 72*n**5 + 228*n**4 + 270*n**3
             - 44*n**2 - 347*n - 211))
    p4 = ((n + 3)**2 * (n + 4)**2
          * (8*n**5 + 44*n**4 + 80*n**3 + 44*n**2 - 22*n - 25))
    re = p0 + p1*sn + p2*sn**2 + p3*sn**3 + p4*sn**4
    return rn, n, an, sn, rc, ra, rd, re


def exact_data(count):
    h = h2 = d = q = F()
    c, a, ds, e = [], [], [], []
    for k in range(count + 2):
        ck = comb(2*k, k)
        ak = F(3, 4)*h - F(1, 2)*h2
        c.append(F(ck))
        a.append(ck*ak)
        ds.append(ck*d)
        e.append(ck*(F(1, 2)*q + ak*d))
        h += F(1, k + 1)
        h2 += F(1, 2*k + 1) + F(1, 2*k + 2)
        d += F((-1)**k, 2*k + 1)
        q += F((-1)**k, (2*k + 1)**2)

    def conv(u, v, j):
        return sum((comb(j, k)*u[k]*v[j-k] for k in range(j + 1)), F())

    b1 = [conv(e, c, j) for j in range(count + 2)]
    b2 = [conv(a, ds, j) for j in range(count + 2)]

    def residual(b, j):
        prev = b[j - 1] if j else F()
        return ((j + 1)**2*b[j + 1] - (12*j*j + 12*j + 4)*b[j]
                + 32*j*j*prev)

    y1 = [residual(b1, j) for j in range(count + 1)]
    y2 = [residual(b2, j) for j in range(count + 1)]
    return c, a, ds, e, b1, b2, y1, y2


def build_residual_operators():
    rn, n, an, sn, rc, ra, rd, re = scalar_operators()
    rx = PolynomialRing(QQ, "x")
    x = rx.gen()
    ax = OreAlgebra(rx, "Dx")
    dx = ax.gen()

    # Multiplication by 1/k! changes ordinary coefficient series into EGFs.
    rfac = (n + 1)*sn - 1
    dc = rc.symmetric_product(rfac).to_D(ax)
    da = ra.symmetric_product(rfac).to_D(ax)
    dd = rd.symmetric_product(rfac).to_D(ax)
    de = re.symmetric_product(rfac).to_D(ax)

    # g1=E*C and g2=A*D are the two EGF convolution pieces.
    p1 = de.symmetric_product(dc)
    p2 = da.symmetric_product(dd)
    theta = x*dx
    lapery = ((theta + 1)*(theta + 1)*dx
              - (12*theta**2 + 12*theta + 4) + 32*x*(theta + 1))
    hy1 = p1.annihilator_of_associate(lapery)
    hy2 = p2.annihilator_of_associate(lapery)
    return rn, n, an, sn, rx, x, ax, dx, hy1, hy2


def empirical_factor(ax, values):
    """Return the search operator; later exact divisions make the guess harmless."""
    from math import factorial

    series = [QQ(v.numerator)/(QQ(v.denominator)*factorial(i))
              for i, v in enumerate(values)]
    basis = guess_raw(series, ax, order=11, degree=17,
                      ensure=80, cut=None)
    assert len(basis) == 1
    return basis[0].normalize(), series


def polynomial_forward_profile(op):
    """Data for forward propagation of coefficients of a formal power series.

    If ``op=sum p_j(x)D^j``, the coefficient of x^n involves indices
    n+j-i for each monomial x^i D^j.  This returns the largest shift r,
    the first n at which its complete coefficient is present, and that
    coefficient as a polynomial in n.
    """
    op = op.numerator()
    terms = []
    for j, polynomial in enumerate(op.coefficients(sparse=False)):
        if not polynomial:
            continue
        for i, coefficient in enumerate(polynomial):
            if coefficient:
                terms.append((j - i, j, i, coefficient))

    forward_shift = max(term[0] for term in terms)
    leading_terms = [term for term in terms if term[0] == forward_shift]
    start = max(term[2] for term in leading_terms)
    z = PolynomialRing(QQ, "z").gen()
    leading = z.parent().zero()
    for _, j, i, coefficient in leading_terms:
        falling = z.parent().one()
        for h in range(1, j + 1):
            falling *= z - i + h
        leading += coefficient*falling
    assert leading
    assert all(root < 0 for root, _ in leading.roots(QQ))
    return forward_shift, start, leading


def apply_to_series(op, series, count):
    """Exact first ``count`` coefficients of op(sum series[n]*x^n)."""
    op = op.numerator()
    answer = []
    for n in range(count):
        value = QQ.zero()
        for j, polynomial in enumerate(op.coefficients(sparse=False)):
            if not polynomial:
                continue
            for i, coefficient in enumerate(polynomial):
                index = n - i + j
                if not coefficient or n < i or not (0 <= index < len(series)):
                    continue
                falling = QQ.one()
                for h in range(1, j + 1):
                    falling *= n - i + h
                value += coefficient*falling*series[index]
        answer.append(value)
    return answer


def main():
    data = exact_data(360)
    y1, y2 = data[-2], data[-1]
    assert y1[0] == 1 and y2[0] == 0
    print("exact coefficient data constructed through n=360")

    rn, n, an, sn, rx, x, ax, dx, hy1, hy2 = build_residual_operators()
    print("generic residual operator orders:", hy1.order(), hy2.order())
    q1, series1 = empirical_factor(ax, y1)
    q2, series2 = empirical_factor(ax, y2)
    assert q1 == q2 and q1.order() == 11 and q1[0].is_zero()
    print("identical search operators: order 11, degree 17, Q[1]=0")

    # Clear rational-function denominators.  Q is used only to locate C; all
    # subsequent claims are certified by exact divisions and propagation.
    h1 = ax(hy1.numerator())
    h2 = ax(hy2.numerator())
    qpoly = ax(q1.numerator())
    print("lifting common factor over Q ...", flush=True)
    c = h1.gcrd(qpoly, prs="essential").normalize()
    assert c.order() == 10
    cpoly = ax(c.numerator())
    assert cpoly.order() == 10 and cpoly.degree() == 29
    assert cpoly[0].is_zero()  # constants are C-solutions

    qquot, qrem = qpoly.quo_rem(cpoly)
    assert qrem.is_zero() and qquot.order() == 1
    cofactors = []
    for h in (h1, h2):
        quotient, remainder = h.quo_rem(cpoly)
        assert remainder.is_zero()
        cofactors.append(ax(quotient.numerator()))
    assert [cofactor.order() for cofactor in cofactors] == [34, 19]
    print("exact right divisions: H1=A1*C, H2=A2*C, Q=B*C")

    # If f_i is the distinguished residual EGF and g_i=C f_i, exact closure
    # gives A_i g_i=0.  Each cofactor recurrence has forward shift four and a
    # leading polynomial with only negative rational roots.  The following
    # exact zero coefficients therefore force g_i=0 by induction.
    for index, (cofactor, series) in enumerate(zip(cofactors,
                                                   (series1, series2)), 1):
        shift, start, leading = polynomial_forward_profile(cofactor)
        assert shift == 4
        needed = start + shift
        image = apply_to_series(cpoly, series, needed)
        assert all(value == 0 for value in image)
        print(f"C*f{index}=0: {needed} initial zeros; "
              f"forward start {start}; lead degree {leading.degree()}")

    # C also has forward shift four, kills constants, and is nonsingular for
    # every nonnegative forward index.  The two residuals agree with a
    # difference of one through the necessary initial segment, hence forever.
    shift, start, leading = polynomial_forward_profile(cpoly)
    assert shift == 4
    needed = start + shift
    delta = [series1[i] - series2[i] - (1 if i == 0 else 0)
             for i in range(needed)]
    assert all(value == 0 for value in delta)
    fingerprint = sha256(str(cpoly).encode()).hexdigest()
    print(f"C*(f1-f2-1)=0: {needed} matching initial coefficients")
    print("C forward leading factor:", leading.factor())
    print("C SHA-256:", fingerprint)
    print("SUCCESS: L(E*C-A*D)=1 identically; Catalan formula is proved")


if __name__ == "__main__":
    main()
