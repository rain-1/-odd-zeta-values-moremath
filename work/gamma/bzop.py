"""The Brown-Zudilin order-9 operator: exact q_j(theta) integer coefficient lists.

Recurrence (BZ, n>=2):  A(n)u_{n+1} + B(n)u_n + C(n)u_{n-1} + D(n)u_{n-2} = 0.
Operator  L = A(th-1) + z B(th) + z^2 C(th+1) + z^3 D(th+2)  (order 9, degree 3).
"""
import sympy as sp

n = sp.Symbol('n')
A = 2*(2*n+1)*(41218*n**3 - 48459*n**2 + 20010*n - 2871)*(n+1)**5
B = -(97604224*n**9 + 178061760*n**8 + 72005308*n**7 - 48634688*n**6
      - 39076836*n**5 + 2622730*n**4 + 7581006*n**3 + 920112*n**2
      - 543402*n - 120582)
C = -2*n*(3874492*n**8 - 2617900*n**7 - 3144314*n**6 + 2947148*n**5
          + 647130*n**4 - 1182926*n**3 + 115771*n**2 + 170716*n - 44541)
D = n*(41218*n**3 + 75195*n**2 + 46746*n + 9898)*(n-1)**5

def coeffs(expr):
    p = sp.Poly(sp.expand(expr), n)
    d = p.degree()
    cs = [int(p.coeff_monomial(n**i)) for i in range(d+1)]
    return cs

q0 = coeffs(A.subs(n, n-1))
q1 = coeffs(B)
q2 = coeffs(C.subs(n, n+1))
q3 = coeffs(D.subs(n, n+2))
QS = [q0, q1, q2, q3]

# characteristic polynomial in lambda:  sum_j lead(q_j) lam^{-j} = 0
CHARPOLY = [1, -188, -2368, 4]   # low->high : 4L^3 - 2368L^2 - 188L + 1

if __name__ == '__main__':
    for i, q in enumerate(QS):
        print("q_%d deg=%d lead=%d  q(0)=%d" % (i, len(q)-1, q[-1], q[0]))
    print("indicial I(s)=q_0(s) factored:", sp.factor(sp.Poly(q0[::-1], sp.Symbol('s')).as_expr()))
    # check leading coefficients give the characteristic polynomial
    L = sp.Symbol('L')
    ch = sp.expand(sum(QS[j][-1]*L**(3-j) for j in range(4))/41218)
    print("char poly:", sp.factor(ch), " (expect 4L^3-2368L^2-188L+1)")
