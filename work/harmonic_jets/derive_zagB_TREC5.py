import sympy as sp

h = sp.symbols('h')
N = 12
Cs = sp.symbols('C0:%d' % (N + 2))

def Cval(k):
    return Cs[k]

def S(nn):
    return sum(sp.binomial(nn, k) * (-h) ** (nn - k) * Cval(k) for k in range(nn + 1))

def rec_lhs(k):
    return (k + 1) ** 2 * Cval(k + 1) - h * (3 * k ** 2 + 3 * k + 1) * Cval(k) + 3 * h ** 2 * k ** 2 * Cval(k - 1)

def trec_defect(nn):
    return sp.expand(nn ** 2 * S(nn) + h ** 3 * (nn - 2) * (nn - 1) * S(nn - 3) - (-h) ** (nn - 1))

print("Testing conjectured certificate: defect(n) = sum_{k=1}^{n-1} C(n-1,k)(-h)^{n-1-k} rec_lhs(k) + h^n C0 - h^{n-1}(C1-1)")
for nn in range(3, 9):
    expr = trec_defect(nn)
    combo = sum(sp.binomial(nn - 1, k) * (-h) ** (nn - 1 - k) * rec_lhs(k) for k in range(1, nn))
    combo += h ** nn * Cval(0) - h ** (nn - 1) * (Cval(1) - 1)
    diff = sp.expand(expr - combo)
    print(nn, 'residual is zero:', diff == 0)

print()
for nn in [3,5,7]:
    expr = trec_defect(nn)
    combo = sum(sp.binomial(nn - 1, k) * (-h) ** (nn - 1 - k) * rec_lhs(k) for k in range(1, nn))
    combo += h ** nn * Cval(0) - h ** (nn - 1) * (Cval(1) - 1)
    diff = sp.expand(expr - combo)
    print(nn, 'diff=', diff)
    # try with a minus sign on whole combo
    diff2 = sp.expand(expr + combo - 2*(h**nn*Cval(0) - h**(nn-1)*(Cval(1)-1)))
    print(nn, 'diff with combo negated (keep boundary same)=', diff2)
