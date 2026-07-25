"""T3 part 2: enlarged bases; test whether the chi-twisted sequences admit ANY
depth-1 harmonic-monomial decomposition, and whether adding chi-partial-sum letters repairs it."""
import sys, itertools
from fractions import Fraction as F
from math import comb, factorial
from sporadic import SEQS, gen_B

Q = (1 << 61) - 1
def inv(a): return pow(a % Q, Q-2, Q)
MAXA = 3000

_tab = {}
def tab(key):
    """key = ('H', r) or ('K', disc, r)"""
    if key in _tab: return _tab[key]
    t = [0]*(MAXA+1)
    if key[0] == 'H':
        r = key[1]
        for m in range(1, MAXA+1): t[m] = (t[m-1] + inv(pow(m, r, Q))) % Q
    else:
        _, D, r = key
        for m in range(1, MAXA+1):
            c = chi(D, m)
            t[m] = (t[m-1] + (c*inv(pow(m, r, Q)) if c else 0)) % Q
    _tab[key] = t; return t

_tabe = {}
def tabe(key):
    if key in _tabe: return _tabe[key]
    t = [F(0)]*(800)
    if key[0] == 'H':
        r = key[1]
        for m in range(1, 800): t[m] = t[m-1] + F(1, m**r)
    else:
        _, D, r = key
        for m in range(1, 800): t[m] = t[m-1] + F(chi(D, m), m**r)
    _tabe[key] = t; return t

def chi(D, m):
    if D == -3: return 0 if m % 3 == 0 else (1 if m % 3 == 1 else -1)
    if D == -4: return 0 if m % 2 == 0 else (1 if m % 4 == 1 else -1)
    if D == 5:  return 0 if m % 5 == 0 else (1 if m % 5 in (1,4) else -1)
    return 1

def rat_recon(a, N=10**8):
    r0, r1, s0, s1 = Q, a % Q, 0, 1
    while r1 > N:
        q = r0//r1; r0, r1 = r1, r0 - q*r1; s0, s1 = s1, s0 - q*s1
    if s1 == 0 or abs(s1) > N: return None
    return F(r1, s1) if s1 > 0 else F(-r1, -s1)

def solve_mod(M, rhs):
    rows = [r[:] + [rhs[i]] for i, r in enumerate(M)]
    nc = len(M[0]); piv = []; r = 0
    for c in range(nc):
        pr = next((i for i in range(r, len(rows)) if rows[i][c] % Q), None)
        if pr is None: continue
        rows[r], rows[pr] = rows[pr], rows[r]
        iv = inv(rows[r][c]); rows[r] = [x*iv % Q for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                f = rows[i][c]; rows[i] = [(rows[i][j] - f*rows[r][j]) % Q for j in range(nc+1)]
        piv.append(c); r += 1
        if r == len(rows): break
    for i in range(r, len(rows)):
        if rows[i][nc] % Q: return None, r, nc
    sol = [0]*nc
    for i, c in enumerate(piv): sol[c] = rows[i][nc]
    return sol, r, nc

def build(letters, w):
    """letters = list of (key, argname).  monomials of total weight w, factors <= w"""
    out = []
    byw = {}
    for key, a in letters:
        r = key[-1]
        byw.setdefault(r, []).append((key, a))
    if w == 2:
        for L in byw.get(2, []): out.append((L,))
        ones = byw.get(1, [])
        for x, y in itertools.combinations_with_replacement(ones, 2): out.append((x, y))
    else:
        for L in byw.get(3, []): out.append((L,))
        for L in byw.get(2, []):
            for M in byw.get(1, []): out.append((L, M))
        for x, y, z in itertools.combinations_with_replacement(byw.get(1, []), 3): out.append((x, y, z))
    return out

def fit(lab, S, argfn, argnames, w, discs=(), NEQ=110, HOLD=(70, 82), verbose=True):
    fam, par = {l: (f, p) for l, f, p, _, _ in SEQS}[lab]
    Bn = gen_B(fam, par, 320)
    letters = [(('H', r), a) for r in range(1, w+1) for a in argnames]
    for D in discs:
        letters += [(('K', D, r), a) for r in range(1, w+1) for a in argnames]
    mons = build(letters, w)
    def mval(mo, n, k, exact=False):
        v = F(1) if exact else 1
        for key, a in mo:
            x = argfn(a, n, k)
            if x < 0 or x > (799 if exact else MAXA): return F(0) if exact else 0
            v = v*(tabe(key)[x] if exact else tab(key)[x])
            if not exact: v %= Q
        return v
    M, rhs = [], []
    for n in range(1, NEQ+1):
        row = [0]*len(mons)
        for k in range(0, n+1):
            s = S(n, k)
            if s == 0: continue
            s %= Q
            for j, mo in enumerate(mons): row[j] = (row[j] + s*mval(mo, n, k)) % Q
        M.append(row); b = Bn[n]
        rhs.append(b.numerator % Q*inv(b.denominator % Q) % Q)
    sol, rank, nc = solve_mod(M, rhs)
    tag = f'{lab:6s} w={w} letters={len(letters)} basis={nc} eqs={NEQ} disc={discs}'
    if sol is None:
        print(f'{tag}: **INCONSISTENT** (rank {rank})'); return None
    co = [rat_recon(c) for c in sol]
    if any(c is None for c in co):
        print(f'{tag}: consistent mod Q (rank {rank}) but particular solution not rational -- retry'); return 'modonly'
    terms = [(co[j], mons[j]) for j in range(nc) if co[j] != 0]
    bad = []
    for n in range(HOLD[0], HOLD[1]+1):
        tot = F(0)
        for k in range(0, n+1):
            s = S(n, k)
            if s == 0: continue
            tot += s*sum(c*mval(mo, n, k, True) for c, mo in terms)
        if tot != Bn[n]: bad.append(n)
    print(f'{tag}: CONSISTENT rank={rank} nnz={len(terms)}  held-out {HOLD}: '
          f'{"ALL EXACT" if not bad else "FAIL "+str(bad)}')
    if verbose:
        for c, mo in sorted(terms, key=lambda t: str(t[1])):
            print('     ', c, '*', ' * '.join((f'H^({k[1]})' if k[0]=='H' else f'K[{k[1]}]^({k[2]})')+f'_[{a}]'
                                              for k, a in mo))
    return terms

AR = {'n': lambda n,k: n, 'k': lambda n,k: k, 'n-k': lambda n,k: n-k, 'n+k': lambda n,k: n+k,
      '2k': lambda n,k: 2*k, '2n-2k': lambda n,k: 2*(n-k), '2n': lambda n,k: 2*n,
      '2n-k': lambda n,k: 2*n-k, '2k-n': lambda n,k: 2*k-n, '3k': lambda n,k: 3*k,
      'n-3k': lambda n,k: n-3*k, '3n': lambda n,k: 3*n}
def argfn(a, n, k): return AR[a](n, k)

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if which in ('all', 'C'):
        S = lambda n,k: comb(n,k)**2*comb(2*k,k)
        print('--- C : enlarged plain-harmonic basis')
        fit('C', S, argfn, ['n','k','n-k','2k','n+k','2n-2k','2n','2n-k'], 2, verbose=False)
        print('--- C : plain + chi_{-3} letters')
        fit('C', S, argfn, ['n','k','n-k','2k'], 2, discs=(-3,))
    if which in ('all', 'E'):
        S = lambda n,k: comb(n,k)*comb(2*k,k)*comb(2*(n-k),n-k)
        print('--- E : enlarged plain-harmonic basis')
        fit('E', S, argfn, ['n','k','n-k','2k','2n-2k','n+k','2n','2n-k'], 2, verbose=False)
        print('--- E : plain + chi_{-4} letters')
        fit('E', S, argfn, ['n','k','n-k','2k','2n-2k'], 2, discs=(-4,))
    if which in ('all', 'delta'):
        S = lambda n,k: ((-1)**k*3**(n-3*k)*comb(n,3*k)*comb(n+k,n)*factorial(3*k)//factorial(k)**3
                         if 3*k <= n else 0)
        print('--- delta : plain-harmonic basis (alternating summand)')
        fit('delta', S, argfn, ['n','k','3k','n-3k','n+k'], 3, verbose=True)
