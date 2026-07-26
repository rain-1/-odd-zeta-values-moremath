"""T2, the exclusion.  Is there ANY letter set over which a zeta(3)-free
Gamma-ratio deformation realises b_n as its primitive eps^3 coefficient?

Need  e  with   sum_L e_L * S_L(n) = b_n  for all n   AND   sum_L e_L = 0,
where S_L(n) = sum_k A(n,k) H^(3)_{L(n,k)}.   (The zeta(3) coefficient of L_3 is
-(1/3) sum_L e_L, so zeta-freeness IS the condition sum_L e_L = 0.)

Letters swept: all L = alpha*n + beta*k + delta with small integer coefficients that
are >= 0 on 0 <= k <= n  (so H^(3)_L is defined).
"""
from fractions import Fraction as F
from core import av, bv, A, Hs

NMAX = 16
LETTERS = []
for al in range(0, 4):
    for be in range(-3, 4):
        for de in range(0, 3):
            if al == be == 0 and de == 0:
                continue
            ok = all(al * n + be * k + de >= 0
                     for n in range(NMAX) for k in range(n + 1))
            if ok:
                LETTERS.append((al, be, de))

print('letters swept: %d' % len(LETTERS))
print('  ', ', '.join('%dn%+dk%+d' % L for L in LETTERS[:12]), '...')


def Ssum(L, n):
    al, be, de = L
    return sum((A(n, k) * Hs(al * n + be * k + de, 3) for k in range(n + 1)), F(0))


COLS = [[Ssum(L, n) for n in range(NMAX)] for L in LETTERS]
BVEC = [bv(n) for n in range(NMAX)]


def solve(rows, rhs):
    """exact Q Gaussian elimination; returns (consistent, rank, particular sol)"""
    m = len(rows); nc = len(rows[0])
    Maug = [list(rows[i]) + [rhs[i]] for i in range(m)]
    piv_cols = []
    r = 0
    for c in range(nc):
        piv = next((i for i in range(r, m) if Maug[i][c] != 0), None)
        if piv is None:
            continue
        Maug[r], Maug[piv] = Maug[piv], Maug[r]
        pv = Maug[r][c]
        Maug[r] = [x / pv for x in Maug[r]]
        for i in range(m):
            if i != r and Maug[i][c] != 0:
                f = Maug[i][c]
                Maug[i] = [Maug[i][j] - f * Maug[r][j] for j in range(nc + 1)]
        piv_cols.append(c); r += 1
    bad = any(all(Maug[i][c] == 0 for c in range(nc)) and Maug[i][nc] != 0
              for i in range(m))
    sol = [F(0)] * nc
    if not bad:
        for row, c in zip(Maug[:r], piv_cols):
            sol[c] = row[nc]
    return (not bad), r, sol


nc = len(LETTERS)
# system rows: one per n  (sum_L e_L S_L(n) = b_n),  plus the zeta-free row
rows = [[COLS[j][n] for j in range(nc)] for n in range(NMAX)]
rhs = list(BVEC)
print('\n(1) without the zeta-free constraint:')
ok, rk, sol = solve(rows, rhs)
print('    consistent=%s  rank=%d  cols=%d  excess equations=%d'
      % (ok, rk, nc, NMAX - rk))
if ok:
    used = {'%dn%+dk%+d' % LETTERS[j]: sol[j] for j in range(nc) if sol[j] != 0}
    print('    a particular solution: %s   (sum of coefficients = %s)'
          % (used, sum(sol)))

print('\n(2) WITH the zeta-free constraint sum_L e_L = 0:')
rows2 = rows + [[F(1)] * nc]
rhs2 = rhs + [F(0)]
ok2, rk2, sol2 = solve(rows2, rhs2)
print('    consistent=%s  rank=%d  cols=%d  equations=%d  excess=%d'
      % (ok2, rk2, nc, len(rows2), len(rows2) - rk2))
if ok2:
    used = {'%dn%+dk%+d' % LETTERS[j]: sol2[j] for j in range(nc) if sol2[j] != 0}
    print('    SOLUTION FOUND: %s' % used)
else:
    print('    INCONSISTENT  =>  no zeta(3)-free Gamma-ratio deformation over this')
    print('    letter set has b_n as its primitive eps^3 coefficient.  [EXCLUDED]')

print('\n(3) sanity: the 4 canonical letters are Q-independent')
canon = [(1, 1, 0), (0, 1, 0), (1, -1, 0), (1, 0, 0)]
rowsc = [[Ssum(L, n) for L in canon] for n in range(NMAX)]
okc, rkc, _ = solve(rowsc, [F(0)] * NMAX)
print('    rank[S_X S_Y S_Z S_N] = %d of 4  on n=0..%d' % (rkc, NMAX - 1))
