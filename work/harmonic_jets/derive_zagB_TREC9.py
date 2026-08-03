import sympy as sp

h = sp.symbols('h')
N = 16
Cs = sp.symbols('C0:%d' % (N + 3))

def Cval(k): return Cs[k]
def Cprime(k): return Cs[k+1]

def S(nn, seq):
    if nn < 0:
        return 0
    return sum(sp.binomial(nn, k) * (-h) ** (nn - k) * seq(k) for k in range(nn + 1))

def rec_lhs(k, seq):
    return (k + 1) ** 2 * seq(k + 1) - h * (3 * k ** 2 + 3 * k + 1) * seq(k) + 3 * h ** 2 * k ** 2 * seq(k - 1)

def RHS(nn, seq):
    total = sum(sp.binomial(nn - 1, k) * (-h) ** (nn - 1 - k) * rec_lhs(k, seq) for k in range(1, nn))
    total += (-1)**nn * h**nn * seq(0) - (-1)**nn * h**(nn-1) * (seq(1) - 1)
    return sp.expand(total)

c = -h
for nn in range(3, 9):
    target = sp.expand(RHS(nn + 1, Cval) - c * RHS(nn, Cval) - RHS(nn, Cprime))
    deg = 2
    names = ['a','b','d','e','p','q']
    syms = {}
    combo = 0
    for nm, seqval in [('a', S(nn, Cval)), ('b', S(nn-3, Cval)), ('d', S(nn, Cprime)),
                        ('e', S(nn-3, Cprime)), ('p', Cval(0)), ('q', Cval(1)-1)]:
        poly = 0
        for dd in range(deg+1):
            u = sp.Symbol(f'{nm}_{dd}')
            syms[(nm,dd)] = u
            poly += u*h**dd
        combo += poly*seqval
    diff = sp.expand(target - combo)
    polydiff = sp.Poly(diff, h, *Cs)
    eqs = [co for _, co in polydiff.terms()]
    unknowns = list(syms.values())
    sol = sp.linsolve(eqs, unknowns)
    print(nn+1, 'solved:', sol != sp.EmptySet)
    if sol != sp.EmptySet:
        assign = dict(zip(unknowns, list(sol)[0]))
        for nm in names:
            val = sp.expand(sum(assign.get(syms[(nm,dd)],0)*h**dd for dd in range(deg+1)))
            if val != 0:
                print('  ', nm, '=', sp.factor(val))
