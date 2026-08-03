import sympy as sp

h = sp.symbols('h')
N = 14
Cs = sp.symbols('C0:%d' % (N + 2))

def Cval(k):
    return Cs[k]

def S(nn):
    return sum(sp.binomial(nn, k) * (-h) ** (nn - k) * Cval(k) for k in range(nn + 1))

def rec_lhs(k):
    return (k + 1) ** 2 * Cval(k + 1) - h * (3 * k ** 2 + 3 * k + 1) * Cval(k) + 3 * h ** 2 * k ** 2 * Cval(k - 1)

def trec_defect(nn):
    return sp.expand(nn ** 2 * S(nn) + h ** 3 * (nn - 2) * (nn - 1) * S(nn - 3) - (-h) ** (nn - 1))

print("Certificate: defect(n) = sum_k C(n-1,k)(-h)^{n-1-k} rec_lhs(k) + (-1)^n h^n C0 - (-1)^n h^{n-1}(C1-1)")
for nn in range(3, 11):
    expr = trec_defect(nn)
    combo = sum(sp.binomial(nn - 1, k) * (-h) ** (nn - 1 - k) * rec_lhs(k) for k in range(1, nn))
    combo += (-1)**nn * h ** nn * Cval(0) - (-1)**nn * h ** (nn - 1) * (Cval(1) - 1)
    diff = sp.expand(expr - combo)
    print(nn, 'residual zero:', diff == 0)
