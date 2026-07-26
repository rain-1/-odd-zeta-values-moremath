"""T2 SOLVED — b_n as a PRIMITIVE third-order coefficient of one deformed family.

Let  Pi_j(t) := prod_{i=1}^{t} (1 + j*eps/i)  =  Gamma(t+1+j eps) / ( t! Gamma(1+j eps) )
(the Gamma(1+j eps)-normalised = Pochhammer form; NO zeta values appear in its log).

    A_eps(n,k) := A(n,k) * prod_{j=1}^{3} Pi_j(n)^{u_j} Pi_j(k)^{v_j}
    u = (6, -6, 2)      v = (-3, 3, -1)

log( A_eps / A ) = sum_{m>=1} eps^m L_m ,
    L_m = ((-1)^{m-1}/m) [ e_m(u) H^(m)_n + e_m(v) H^(m)_k ] ,   e_m(c) = sum_j c_j j^m
    e_1(u)=e_2(u)=0, e_3(u)=12 ;  e_1(v)=e_2(v)=0, e_3(v)=-6
 => L_1 = L_2 = 0  identically, so the eps^3 Bell polynomial
    B_3 = L_3 + L_1 L_2 + L_1^3/6  =  L_3  =  2 ( 2 H^(3)_n - H^(3)_k ) .

    ==>  b_n  =  (1/2) [eps^3] sum_k A_eps(n,k)          PRIMITIVE, zeta-free.

Minimality: two shift-points cannot give e_1 = e_2 = 0 non-degenerately; with shifts
(1,2,3) the exponents are forced up to scale by the inverse Vandermonde,
(E/2, -E/2, E/6).
"""
from fractions import Fraction as F
from core import av, bv, A, Hs

M = 4
U = {1: 6, 2: -6, 3: 2}
V = {1: -3, 2: 3, 3: -1}


def smul(x, y):
    z = [F(0)] * (M + 1)
    for i, xi in enumerate(x):
        if xi == 0:
            continue
        for j in range(min(len(y), M + 1 - i)):
            if y[j]:
                z[i + j] += xi * y[j]
    return z


def Pi(t, j):
    """prod_{i<=t}(1 + j eps/i) as a truncated series"""
    out = [F(1)] + [F(0)] * M
    for i in range(1, t + 1):
        f = [F(1), F(j, i)] + [F(0)] * (M - 1)
        out = smul(out, f)
    return out


def Piinv(t, j):
    """its reciprocal:  prod_{i<=t} sum_m (-j eps/i)^m"""
    out = [F(1)] + [F(0)] * M
    for i in range(1, t + 1):
        f = [F((-j) ** m, i ** m) for m in range(M + 1)]
        out = smul(out, f)
    return out


def factor(t, coefs):
    out = [F(1)] + [F(0)] * M
    for j, c in coefs.items():
        base = Pi(t, j) if c > 0 else Piinv(t, j)
        for _ in range(abs(c)):
            out = smul(out, base)
    return out


print('=' * 78)
print('moments of the exponent vectors')
for nm, c in (('u', U), ('v', V)):
    print('  e_1(%s)=%d  e_2(%s)=%d  e_3(%s)=%d'
          % (nm, sum(k * m for m, k in c.items()),
             nm, sum(k * m ** 2 for m, k in c.items()),
             nm, sum(k * m ** 3 for m, k in c.items())))

print('\n' + '=' * 78)
print('EXACT VERIFICATION:  [eps^m] sum_k A_eps(n,k)  for m = 0,1,2,3')
print('  expect  (a_n, 0, 0, 2 b_n)')
print('=' * 78)
print('%-4s %-8s %-8s %-8s %-28s %s' % ('n', 'm=0', 'm=1', 'm=2', '[eps^3]/2', 'b_n  match'))
allok = True
for n in range(0, 21):
    tot = [F(0)] * (M + 1)
    for k in range(n + 1):
        s = smul(factor(n, U), factor(k, V))
        ak = A(n, k)
        for i in range(M + 1):
            if s[i]:
                tot[i] += ak * s[i]
    half = tot[3] / 2
    ok = (tot[0] == av(n)) and tot[1] == 0 and tot[2] == 0 and half == bv(n)
    allok = allok and ok
    if n <= 8 or not ok or n == 20:
        print('%-4d %-8s %-8s %-8s %-28s %s'
              % (n, 'a_n' if tot[0] == av(n) else 'BAD', tot[1], tot[2],
                 str(half)[:26], 'OK' if half == bv(n) else 'MISMATCH'))
print('\n  all of n = 0..20 :  %s' % ('VERIFIED' if allok else 'FAILED'))
print("""
  [eps^1] = [eps^2] = 0 termwise (L_1 = L_2 = 0 in the summand), so no weight-1 or
  weight-2 term has to be cancelled by the summation -- the coefficient is primitive
  by construction, not by conspiracy.""")

print('=' * 78)
print('the two degenerate one-parameter members, for contrast')
print('=' * 78)
print("""  n-shift  (alpha,beta,gamma)=(1,0,1):  L_1 = 2(H_{n+k}-H_{n-k}),
      [eps^1] sum = 2 U_n  != 0                     -- drives the p-adic scalar law (T1)
  k-shift  (1,1,-1):                    L_1 = 2(H_{n+k}-2H_k+H_{n-k}),
      [eps^1] sum = 2 V_n  =  0  BY THE IDENTITY    -- the same identity as T1 sec.3.2""")
