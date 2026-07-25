"""T3: harmonic-monomial decomposition  B_n = sum_k S(n,k) * w(n,k),
w = Q-linear combination of weight-w harmonic monomials in H^{(r)} at a set of
arguments natural to the summand.  Solved exactly mod a 62-bit prime, then the
coefficients are rationally reconstructed and validated EXACTLY over Q on held-out n.
"""
import sys, itertools, math
from fractions import Fraction as F
from sporadic import SEQS, gen_A, gen_B

Q = (1 << 61) - 1          # Mersenne prime 2^61-1

def inv(a): return pow(a % Q, Q-2, Q)

# ---- harmonic numbers mod Q  ------------------------------------------------
MAXA = 4000
Hm = {}
def Htab(r):
    if r in Hm: return Hm[r]
    t = [0]*(MAXA+1)
    for m in range(1, MAXA+1):
        t[m] = (t[m-1] + inv(pow(m, r, Q))) % Q
    Hm[r] = t
    return t

# ---- exact harmonic numbers (Fractions) ------------------------------------
He = {}
def Hex(r):
    if r in He: return He[r]
    t = [F(0)]*(600)
    for m in range(1, 600): t[m] = t[m-1] + F(1, m**r)
    He[r] = t
    return t

# ---- summands ---------------------------------------------------------------
from math import comb
SUM = {
 'A':     (lambda n,k: comb(n,k)**3,                                  ['n','k','n-k']),
 'C':     (lambda n,k: comb(n,k)**2*comb(2*k,k),                      ['n','k','n-k','2k']),
 'D':     (lambda n,k: comb(n,k)**2*comb(n+k,n),                      ['n','k','n-k','n+k']),
 'E':     (lambda n,k: comb(n,k)*comb(2*k,k)*comb(2*(n-k),n-k),       ['n','k','n-k','2k','2n-2k']),
 'alpha': (lambda n,k: comb(n,k)**2*comb(2*k,k)*comb(2*(n-k),n-k),    ['n','k','n-k','2k','2n-2k']),
 'gamma': (lambda n,k: comb(n,k)**2*comb(n+k,n)**2,                   ['n','k','n-k','n+k']),
 'eps':   (lambda n,k: comb(n,k)**2*comb(2*k,n)**2,                   ['n','k','n-k','2k','2k-n']),
 's10':   (lambda n,k: comb(n,k)**4,                                  ['n','k','n-k']),
 's7':    (lambda n,k: comb(n,k)**2*comb(n+k,k)*comb(2*k,n),          ['n','k','n-k','n+k','2k','2k-n']),
}
def argval(name, n, k):
    return {'n':n,'k':k,'n-k':n-k,'n+k':n+k,'2k':2*k,'2n-2k':2*(n-k),'2k-n':2*k-n}[name]

W = {'A':2,'C':2,'D':2,'E':2,'alpha':3,'gamma':3,'eps':3,'s10':2,'s7':2}

def monomials(args, w):
    """list of monomials: each = tuple of (r, arg) factors, total sum r = w."""
    out = []
    if w == 2:
        for a in args: out.append(((2,a),))
        for a, b in itertools.combinations_with_replacement(args, 2): out.append(((1,a),(1,b)))
    elif w == 3:
        for a in args: out.append(((3,a),))
        for a in args:
            for b in args: out.append(((2,a),(1,b)))
        for a,b,c in itertools.combinations_with_replacement(args,3): out.append(((1,a),(1,b),(1,c)))
    return out

def mon_val_mod(mon, n, k):
    v = 1
    for r, a in mon:
        x = argval(a, n, k)
        if x < 0: return 0
        v = v*Htab(r)[x] % Q
    return v

def mon_val_exact(mon, n, k):
    v = F(1)
    for r, a in mon:
        x = argval(a, n, k)
        if x < 0: return F(0)
        v *= Hex(r)[x]
    return v

def rat_recon(a, N=10**7):
    """rational reconstruction of a mod Q"""
    r0, r1 = Q, a % Q
    s0, s1 = 0, 1
    while r1 > N:
        q = r0//r1
        r0, r1 = r1, r0 - q*r1
        s0, s1 = s1, s0 - q*s1
    if s1 == 0 or abs(s1) > N: return None
    return F(r1, s1) if s1 > 0 else F(-r1, -s1)

def solve_mod(M, rhs):
    """Gaussian elimination mod Q. M: list of rows (lists), rhs list. Returns (sol, rank, ncols)"""
    rows = [r[:] + [rhs[i]] for i, r in enumerate(M)]
    ncols = len(M[0]); piv = []
    r = 0
    for c in range(ncols):
        pr = None
        for i in range(r, len(rows)):
            if rows[i][c] % Q: pr = i; break
        if pr is None: continue
        rows[r], rows[pr] = rows[pr], rows[r]
        iv = inv(rows[r][c])
        rows[r] = [x*iv % Q for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                f = rows[i][c]
                rows[i] = [(rows[i][j] - f*rows[r][j]) % Q for j in range(ncols+1)]
        piv.append(c); r += 1
        if r == len(rows): break
    # consistency
    for i in range(r, len(rows)):
        if rows[i][ncols] % Q: return None, r, ncols
    sol = [0]*ncols
    for i, c in enumerate(piv): sol[c] = rows[i][ncols]
    return sol, r, ncols

def run(lab, NEQ=90, HOLD=(60,72)):
    fam, par = {l:(f,p) for l,f,p,_,_ in SEQS}[lab]
    Bn = gen_B(fam, par, 200)
    S, args = SUM[lab]; w = W[lab]
    mons = monomials(args, w)
    M, rhs = [], []
    for n in range(1, NEQ+1):
        row = [0]*len(mons)
        for k in range(0, n+1):
            s = S(n, k) % Q
            if s == 0: continue
            for j, mo in enumerate(mons):
                row[j] = (row[j] + s*mon_val_mod(mo, n, k)) % Q
        M.append(row)
        b = Bn[n]
        rhs.append(b.numerator % Q * inv(b.denominator % Q) % Q)
    sol, rank, nc = solve_mod(M, rhs)
    if sol is None:
        print(f'{lab:6s} w={w} basis={len(mons)} eqs={NEQ}: **INCONSISTENT** (rank {rank})')
        return None
    coeffs = []
    for j, c in enumerate(sol):
        q = rat_recon(c)
        coeffs.append(q)
    if any(c is None for c in coeffs):
        print(f'{lab:6s} w={w} basis={len(mons)}: solution found mod Q but NOT rationally reconstructible '
              f'(rank {rank}/{nc}) -> pick another basis vector')
        return None
    terms = [(coeffs[j], mons[j]) for j in range(len(mons)) if coeffs[j] != 0]
    # exact validation on held-out n
    bad = []
    for n in range(HOLD[0], HOLD[1]+1):
        tot = F(0)
        for k in range(0, n+1):
            s = S(n, k)
            if s == 0: continue
            wt = sum(c*mon_val_exact(mo, n, k) for c, mo in terms)
            tot += s*wt
        if tot != Bn[n]: bad.append(n)
    print(f'{lab:6s} w={w} basis={len(mons)} rank={rank} nnz={len(terms)}  '
          f'held-out n={HOLD[0]}..{HOLD[1]}: {"ALL EXACT" if not bad else "FAIL at "+str(bad)}')
    for c, mo in sorted(terms, key=lambda t: str(t[1])):
        print('        ', c, ' * ', ' * '.join(f'H^({r})_[{a}]' for r, a in mo))
    return terms

if __name__ == '__main__':
    for lab in (sys.argv[1:] or list(SUM)):
        run(lab)
        print(flush=True)
