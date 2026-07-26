"""T2 — the ORIGIN OF THE WEIGHT.  Gamma-ratio deformations of A(n,k).

A(n,k) = [ Gamma(n+k+1) / ( Gamma(k+1)^2 Gamma(n-k+1) ) ]^2  -- three Gamma letters
X = n+k (exponent 2), Y = k (exponent -4), Z = n-k (exponent -2).

A deformation is  A_eps = A * prod_L prod_i [ Gamma(L+1+m_{L,i} eps)/Gamma(L+1) ]^{c_{L,i}}
over ANY set of letters L (a letter not in A is legal: the ratio is 1 at eps=0).
With  e_j(L) := sum_i c_{L,i} m_{L,i}^j,

  log(A_eps/A) = sum_j L_j eps^j
  L_1 = sum_L e_1(L) ( H_L - gammaE )
  L_j = ((-1)^j / j) sum_L e_j(L) ( zeta(j) - H^(j)_L )     (j >= 2)

and  [eps^3] sum_k A_eps  =  sum_k A(n,k) ( L_3 + L_1 L_2 + L_1^3/6 ).

STEP 1  the letter obstruction
STEP 2  the single-shift-per-letter family: which are zeta-free?
STEP 3  the construction that works, verified exactly
STEP 4  can the zeta(3) impurity be removed?  (null-relation search)
"""
from fractions import Fraction as F
from core import av, bv, A, Hs, a_direct
from itertools import product

# ---------------------------------------------------------------- STEP 2
print('=' * 78)
print('STEP 2  single shift per letter:  A_eps uses (alpha,beta,gamma) on (X,Y,Z)')
print('        purity  e_j = 2 alpha^j - 4 beta^j - 2 gamma^j = 0  for j=1,2,3')
print('=' * 78)
print("""  e_1 = 0  =>  gamma = alpha - 2 beta
  e_2 = 0  =>  2 beta (2 alpha - 3 beta) = 0   =>  beta = 0  or  alpha = 3beta/2
  beta = 0 : gamma = alpha, e_3 = alpha^3 - alpha^3 = 0        OK  -> the n-SHIFT (1,0,1)
  alpha = 3beta/2 : gamma = -beta/2, e_3 = (3/2)beta^3 != 0    FAILS
  => the ONLY zeta-free single-shift deformation of A's own Gammas is n -> n+eps,
     and its  L_3 = (2/3)( H^(3)_{n+k} - H^(3)_{n-k} ).                    [PROVED]""")

# ---------------------------------------------------------------- STEP 1/4 data
NMAX = 15


def SX(n):
    return sum((A(n, k) * Hs(n + k, 3) for k in range(n + 1)), F(0))


def SY(n):
    return sum((A(n, k) * Hs(k, 3) for k in range(n + 1)), F(0))


def SZ(n):
    return sum((A(n, k) * Hs(n - k, 3) for k in range(n + 1)), F(0))


def SN(n):
    return F(av(n)) * Hs(n, 3)


def rank_Q(rows):
    """rank over Q of a list of rational row-vectors"""
    rows = [list(map(F, r)) for r in rows]
    m = len(rows); nc = len(rows[0]) if m else 0
    r = 0
    for c in range(nc):
        piv = next((i for i in range(r, m) if rows[i][c] != 0), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        pv = rows[r][c]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(m):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [rows[i][j] - f * rows[r][j] for j in range(nc)]
        r += 1
    return r


print('\n' + '=' * 78)
print('STEP 1/4  the weight-3 letter sums, and relations among them')
print('   S_X = sum_k A H^(3)_{n+k}   S_Y = sum_k A H^(3)_k')
print('   S_Z = sum_k A H^(3)_{n-k}   S_N = a_n H^(3)_n        b_n = 2 S_N - S_Y')
print('=' * 78)
cols = {'S_X': [], 'S_Y': [], 'S_Z': [], 'S_N': [], 'b': []}
for n in range(NMAX):
    cols['S_X'].append(SX(n)); cols['S_Y'].append(SY(n))
    cols['S_Z'].append(SZ(n)); cols['S_N'].append(SN(n))
    cols['b'].append(bv(n))
assert all(cols['b'][n] == 2 * cols['S_N'][n] - cols['S_Y'][n] for n in range(NMAX))
print('   b_n = 2 S_N - S_Y  verified exactly, n = 0..%d' % (NMAX - 1))

names = ['S_X', 'S_Y', 'S_Z', 'S_N']
M = [[cols[nm][n] for nm in names] for n in range(NMAX)]     # rows = n
print('   rank over Q of [S_X S_Y S_Z S_N] on n=0..%d : %d of 4'
      % (NMAX - 1, rank_Q(M)))
for sub in (['S_X', 'S_Y', 'S_Z'], ['S_X', 'S_Z', 'S_N'], ['S_X', 'S_Y', 'S_Z', 'S_N']):
    Ms = [[cols[nm][n] for nm in sub] for n in range(NMAX)]
    Mb = [[cols[nm][n] for nm in sub] + [cols['b'][n]] for n in range(NMAX)]
    print('   b in span%-28s : %s' % (sub, 'YES' if rank_Q(Ms) == rank_Q(Mb) else 'NO'))

# ---------------------------------------------------------------- STEP 3
print('\n' + '=' * 78)
print('STEP 3  the deformation that works, verified exactly')
print('=' * 78)
U = {1: 6, 2: -6, 3: 2}          # exponents on Gamma(n+1+j eps)
V = {1: -3, 2: 3, 3: -1}         # exponents on Gamma(k+1+j eps)


def e(coef, j):
    return sum(c * m ** j for m, c in coef.items())


for nm, coef in (('n-letter', U), ('k-letter', V)):
    print('  %s  e_1=%d  e_2=%d  e_3=%d' % (nm, e(coef, 1), e(coef, 2), e(coef, 3)))

print("""
  L_1 = e_1(n)(H_n - g) + e_1(k)(H_k - g)                  = 0   (both e_1 = 0)
  L_2 = (1/2)[ e_2(n)(z2 - H2_n) + e_2(k)(z2 - H2_k) ]     = 0   (both e_2 = 0)
  L_3 = (-1/3)[ e_3(n)(z3 - H3_n) + e_3(k)(z3 - H3_k) ]
      = (-1/3)[ 12 z3 - 12 H3_n - 6 z3 + 6 H3_k ] = 2(2 H3_n - H3_k) - 2 z3
  => [eps^3] sum_k A_eps = 2 ( b_n - zeta(3) a_n ),  and L_1 = L_2 = 0 identically,
     so the eps^3 Bell polynomial B_3 = L_3 + L_1 L_2 + L_1^3/6 collapses to L_3:
     the coefficient is PRIMITIVE.""")

# independent check: build the eps-series of the Gamma products from scratch
def logratio(m_int, mult, M):
    """coefficients (rational part, gamma coef, z2 coef, z3 coef) of
    log[Gamma(m+1+mult*eps)/Gamma(m+1)] up to eps^3"""
    out = []
    for j in range(1, M + 1):
        d = F(mult) ** j
        if j == 1:
            out.append({'1': d * Hs(m_int, 1), 'g': -d})
        else:
            s = F((-1) ** j, j) * d
            out.append({'1': -s * Hs(m_int, j), 'z%d' % j: s})
    return out


ok = True
for n in range(0, 13):
    for k in range(0, n + 1):
        L = [{} for _ in range(3)]
        for m, c in U.items():
            for j, term in enumerate(logratio(n, m, 3)):
                for key, val in term.items():
                    L[j][key] = L[j].get(key, F(0)) + c * val
        for m, c in V.items():
            for j, term in enumerate(logratio(k, m, 3)):
                for key, val in term.items():
                    L[j][key] = L[j].get(key, F(0)) + c * val
        L1 = {kk: vv for kk, vv in L[0].items() if vv != 0}
        L2 = {kk: vv for kk, vv in L[1].items() if vv != 0}
        L3 = {kk: vv for kk, vv in L[2].items() if vv != 0}
        want = {'1': 2 * (2 * Hs(n, 3) - Hs(k, 3)), 'z3': F(-2)}
        want = {kk: vv for kk, vv in want.items() if vv != 0}
        if L1 or L2 or L3 != want:
            ok = False
            print('  MISMATCH n=%d k=%d L1=%s L2=%s L3=%s' % (n, k, L1, L2, L3))
print('  L_1 = L_2 = 0 and L_3 = 2(2H3_n - H3_k) - 2 zeta(3) for every (n,k),'
      ' n <= 12 :  %s' % ('VERIFIED' if ok else 'FAILED'))
print('  => b_n - zeta(3) a_n = (1/2) [eps^3] sum_k A_eps(n,k)          [PROVED]')
print('  and b_n - zeta(3) a_n is exactly the Apery REMAINDER (-> 0 super-exponentially);')
print('  b_1/a_1 = 6/5 = 1.2 vs zeta(3) = 1.2020569...')
