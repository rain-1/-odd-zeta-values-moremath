"""eps60_density.py -- THE DENSITY QUESTION.

Do sporadic companions cancel denominators at a positive DENSITY of primes
(exponential lever on irrationality) or only at finitely many structural
primes (polynomial)?  Exact Fractions; recurrences validated against the
binomial sums before use; deficiency/valuation profiles for 2 <= p <= 200,
n <= 300; splitting-type classification of the cancelling primes.
"""
import sys, json
from fractions import Fraction as F
from math import comb, isqrt

NMAX = 300
PMAX = 200

def primes(lo, hi):
    out=[]
    for m in range(max(2,lo), hi+1):
        if all(m % d for d in range(2, isqrt(m)+1)):
            out.append(m)
    return out

def vp(x, p):
    if x == 0: return 10**9
    a, b = x.numerator, x.denominator
    v = 0
    while a % p == 0: a //= p; v += 1
    while b % p == 0: b //= p; v -= 1
    return v

# ---------------- families ----------------
# R2:  (n+1)^2 u_{n+1} = (a n^2 + a n + b) u_n - c n^2 u_{n-1}
# R3:  (n+1)^3 u_{n+1} = (2n+1)(a n^2 + a n + b) u_n - n (c n^2 + d) u_{n-1}
def rec_R2(a,b,c):
    def step(n, u0, u1):   # returns u_{n+1} from u_{n-1}=u0, u_n=u1
        return (F(a*n*n + a*n + b)*u1 - F(c*n*n)*u0) / F((n+1)**2)
    return step
def rec_R3(a,b,c,d):
    def step(n, u0, u1):
        return (F((2*n+1)*(a*n*n + a*n + b))*u1 - F(n*(c*n*n + d))*u0) / F((n+1)**3)
    return step

def sum_A(name, n):
    if name=='A':  return sum(comb(n,k)**3 for k in range(n+1))
    if name=='C':  return sum(comb(n,k)**2*comb(2*k,k) for k in range(n+1))
    if name=='D':  return sum(comb(n,k)**2*comb(n+k,k) for k in range(n+1))
    if name=='E':  return sum(comb(n,k)*comb(2*k,k)*comb(2*(n-k),n-k) for k in range(n+1))
    if name=='gamma': return sum(comb(n,k)**2*comb(n+k,k)**2 for k in range(n+1))
    if name=='zeta':
        return sum(comb(n,k)**2*comb(n,l)*comb(k,l)*comb(k+l,n)
                   for k in range(n+1) for l in range(n+1))
    raise KeyError(name)

FAMS = {
 'A':     dict(r=2, step=rec_R2(7,2,-8),   label='Franel (7,2,-8)'),
 'C':     dict(r=2, step=rec_R2(10,3,9),   label='C (10,3,9) chi-3'),
 'D':     dict(r=2, step=rec_R2(11,3,-1),  label='D (11,3,-1) level 5'),
 'E':     dict(r=2, step=rec_R2(12,4,32),  label='E (12,4,32) chi-4 / Catalan'),
 'gamma': dict(r=3, step=rec_R3(17,5,1,0), label='Apery zeta(3) (17,5,1,0)'),
 'zeta':  dict(r=3, step=rec_R3(9,3,-27,0),label='zeta (9,3,-27,0) chi-3'),
}

# ---------------- validation: recurrence == binomial sums ----------------
print('validation: A(n) from sums satisfies recurrence (n<=8):')
for nm, fam in FAMS.items():
    Avals=[F(sum_A(nm,n)) for n in range(10)]
    ok=all(fam['step'](n, Avals[n-1], Avals[n]) == Avals[n+1] for n in range(1,9))
    print('  %-6s %s' % (nm, 'PASS' if ok else 'FAIL'))
    assert ok, nm

# ---------------- companion sequences ----------------
print('computing B(n), n <= %d ...' % NMAX, flush=True)
B = {}
for nm, fam in FAMS.items():
    b=[F(0), F(1)]
    for n in range(1, NMAX):
        b.append(fam['step'](n, b[n-1], b[n]))
    B[nm]=b

PL = primes(2, PMAX)
DISCS = [-3, -4, -8, 8, 5, -20, 12, -24, 24, -7, 13, -11, 21, 28, -15]

def kronecker(D, p):
    # quadratic character chi_D(p) for odd p not dividing D
    if p == 2:
        return 0
    if D % p == 0: return 0
    return pow(D % p, (p-1)//2, p) == 1 and 1 or -1

# ---------------- valuation profiles ----------------
RES = {}
for nm, fam in FAMS.items():
    r = fam['r']
    prof = {}
    for p in PL:
        worst = 0            # max needed denominator exponent at p
        firstneg = None
        for n in range(1, NMAX+1):
            v = vp(B[nm][n], p)
            if v < 0:
                worst = max(worst, -v)
                if firstneg is None: firstneg = n
        prof[p] = dict(worst=worst, first=firstneg)
    canc = [p for p in PL if p >= 5 and prof[p]['worst'] == 0 and p <= NMAX]
    # (p <= NMAX so the window [p, NMAX] is nonempty and cancellation is a
    #  statement about at least one live digit)
    tested = [p for p in PL if 5 <= p <= NMAX]
    RES[nm] = dict(prof=prof, canc=canc, tested=len(tested))
    # character law search
    best = None
    for D in DISCS:
        for sign in (1,-1):
            okc = [p for p in tested if kronecker(D,p) == sign]
            if set(canc) == set(okc):
                best = (D, sign, 'exact')
                break
        if best: break
    dens = len(canc)/len(tested)
    print('%-6s r=%d  cancelling primes in [5,%d]: %d/%d (density %.3f)  %s' %
          (nm, r, PMAX, len(canc), len(tested), dens,
           ('LAW: chi_%d = %+d' % best[:2]) if best else ''))
    print('        cancelling:', canc if len(canc)<40 else canc[:40])
    RES[nm]['density']=dens
    RES[nm]['law']=best

# structural small primes (2,3) for the record
print('\nstructural primes (worst needed exponent at p=2,3):')
for nm in FAMS:
    print('  %-6s p=2: %d   p=3: %d' %
          (nm, RES[nm]['prof'][2]['worst'], RES[nm]['prof'][3]['worst']))

json.dump({nm: dict(canc=RES[nm]['canc'], density=RES[nm]['density'],
                    law=RES[nm]['law'],
                    struct={p: RES[nm]['prof'][p]['worst'] for p in (2,3,5,7,11,13)})
           for nm in FAMS},
          open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/eps60_results.json','w'),
          indent=1)
print('\nsaved eps60_results.json')
