import sympy as sp

h = sp.symbols('h')
N = 16
Cs = sp.symbols('C0:%d' % (N + 3))

def Cval(k):
    return Cs[k]

def Cprime(k):
    # C' = C shifted by 1: C'_j = C_{j+1}
    return Cs[k+1]

def S(nn, seq):
    return sum(sp.binomial(nn, k) * (-h) ** (nn - k) * seq(k) for k in range(nn + 1))

def rec_lhs(k, seq):
    return (k + 1) ** 2 * seq(k + 1) - h * (3 * k ** 2 + 3 * k + 1) * seq(k) + 3 * h ** 2 * k ** 2 * seq(k - 1)

def RHS(nn, seq):
    total = sum(sp.binomial(nn - 1, k) * (-h) ** (nn - 1 - k) * rec_lhs(k, seq) for k in range(1, nn))
    total += (-1)**nn * h**nn * seq(0) - (-1)**nn * h**(nn-1) * (seq(1) - 1)
    return sp.expand(total)

c = -h
for nn in range(3, 10):
    lhs = sp.expand(RHS(nn + 1, Cval))
    # candidate: c*RHS(n,C) + RHS(n,C') + (2n+1)*S(n,C) + 2h^3(n-1)*S(n-3,C) + (2n+1)*S(n,C') + 2h^3(n-1)*S(n-3,C')
    rhs_cand = c * RHS(nn, Cval) + RHS(nn, Cprime)
    rhs_cand += (2*nn+1)*S(nn, Cval) + 2*h**3*(nn-1)*S(nn-3, Cval) if nn>=3 else 0
    rhs_cand += (2*nn+1)*S(nn, Cprime) + 2*h**3*(nn-1)*S(nn-3, Cprime) if nn>=3 else 0
    rhs_cand = sp.expand(rhs_cand)
    diff = sp.expand(lhs - rhs_cand)
    print(nn+1, 'match:', diff == 0, ('' if diff==0 else diff))
