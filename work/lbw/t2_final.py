"""DEFINITIVE T2 sweep: the chi-twisted master descent
      (LBw)  v_p( p^w B_n A_q - chi(p) B_q A_n ) >= w ,  q = floor(n/p)
   and the chi-twisted Lucas form
      (Luc)  p^w B_{ap+r} = chi(p) B_a A_r  (mod p)     for n=ap+r < p^2
Zero-failure standard, exact arithmetic.
"""
import math, pickle, sys
from fractions import Fraction as F
from sporadic import SEQS, gen_A, gen_B

W = {'A':2,'B':2,'C':2,'D':2,'E':2,'F':2,'alpha':3,'gamma':3,'delta':3,'eps':3,
     'zeta':3,'eta':3,'s7':2,'s10':2,'s18':2}
# discriminant of the quadratic character chi (1 = trivial)
DISC = {'A':1,'B':-3,'C':-3,'D':1,'E':-4,'F':-3,'alpha':1,'gamma':1,'delta':1,
        'eps':1,'zeta':-3,'eta':5,'s7':1,'s10':1,'s18':-3}
PRIMES = [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
N = 400
INF = 10**6
def vp_int(x, p):
    if x == 0: return INF
    v = 0
    while x % p == 0: x //= p; v += 1
    return v
def vp(x, p):
    if x == 0: return INF
    return vp_int(x.numerator, p) - vp_int(x.denominator, p)
def chi(D, p):
    if D == 1: return 1
    if D == -3: return 1 if p % 3 == 1 else (-1 if p % 3 == 2 else 0)
    if D == -4: return 1 if p % 4 == 1 else -1
    if D == 5:  return 1 if p % 5 in (1,4) else (-1 if p % 5 in (2,3) else 0)

summary = {}
for lab, fam, par, fn, note in SEQS:
    A = gen_A(fam, par, N); B = gen_B(fam, par, N); w = W[lab]; D = DISC[lab]
    tot_fail = 0; floors = {}; luc_fail = 0; ram = []
    for p in PRIMES:
        c = chi(D, p)
        if c == 0:
            ram.append(p); continue
        pw = F(p)**w
        fl = INF; nf = 0
        for n in range(1, N+1):
            q = n//p
            v = vp(pw*B[n]*A[q] - c*B[q]*A[n], p)
            if v < w: nf += 1
            fl = min(fl, v)
        # chi-twisted Lucas, single-digit n = a p + r < p^2
        lf = 0; lmin = INF
        for a in range(1, p):
            for r in range(p):
                n = a*p + r
                if n > N: continue
                v = vp(pw*B[n] - c*B[a]*A[r], p)
                lmin = min(lmin, v)
                if v < 1: lf += 1
        # integrality  v_p(B_n) >= -w*floor(log_p n)
        intfail = sum(1 for n in range(1, N+1)
                      if vp(B[n], p) < -w*int(math.log(n, p)+1e-9))
        floors[p] = (fl, nf, lmin, lf, c, intfail)
        tot_fail += nf; luc_fail += lf
    summary[lab] = dict(w=w, D=D, floors=floors, tot_fail=tot_fail, luc_fail=luc_fail, ram=ram)
    fls = sorted(set(f[0] for f in floors.values()))
    lms = sorted(set(f[2] for f in floors.values()))
    ints = sum(f[5] for f in floors.values())
    print(f'{lab:6s} w={w} disc={D:>3}  master floors={fls} fails={tot_fail} | '
          f'Lucas mins={lms} fails={luc_fail} | int-fails={ints} | ram p={ram}', flush=True)
pickle.dump(summary, open('t2final.pkl','wb'))
