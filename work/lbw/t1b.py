import math, pickle
from fractions import Fraction as F
from sporadic import SEQS, gen_A, gen_B
import mpmath as mp

mp.mp.dps = 400
N = 600

D = [1]*(N+2)
for n in range(1, N+2): D[n] = D[n-1]*n//math.gcd(D[n-1], n)

def kron(a, n):
    import sympy
    res, m = 1, n
    while m % 2 == 0:
        m //= 2
        if a % 8 in (3, 5): res = -res
        elif a % 2 == 0: return 0
    if m == 1: return res
    return res*int(sympy.functions.combinatorial.numbers.jacobi_symbol(a, m))

def Lval(disc, s):
    m = abs(disc); tot = mp.mpf(0)
    for r in range(1, m+1):
        c = kron(disc, r) if math.gcd(disc, r) == 1 else 0
        if c: tot += c*mp.zeta(s, mp.mpf(r)/m)
    return tot/mp.mpf(m)**s

CONSTS = {'zeta(2)': mp.zeta(2), 'zeta(3)': mp.zeta(3), 'zeta(4)': mp.zeta(4)}
for d in (-3, -4, -7, -8, -11, -15, -20, -24, 5, 8, 12, 13, 24):
    for s in (2, 3):
        CONSTS[f'L_{{{d}}}({s})'] = Lval(d, s)
CONSTS['log(2)^2'] = mp.log(2)**2
CONSTS['pi^2*log(2)'] = mp.pi**2*mp.log(2)
CONSTS['log(2)^3'] = mp.log(2)**3

def tofl(q): return mp.mpf(q.numerator)/mp.mpf(q.denominator)

out = {}
for lab, fam, par, fn, note in SEQS:
    A = gen_A(fam, par, N); B = gen_B(fam, par, N)
    Q = [tofl(B[n])/tofl(A[n]) if A[n] != 0 else None for n in range(N+1)]
    # digits of agreement between Q(N) and Q(N-10)
    L = Q[N]
    try:
        agree = float(-mp.log10(abs(Q[N]-Q[N-10])/abs(Q[N])))
    except Exception:
        agree = 0.0
    if agree != agree or agree < 0: agree = 0.0
    agree = min(agree, mp.mp.dps-20)
    w = None
    for cand in range(0, 9):
        if all((B[n]*D[n]**cand).denominator == 1 for n in range(1, N+1)):
            w = cand; break
    # sharpness: is d_n^{w-1} B_n never integral for large n?
    sharp = None
    if w and w >= 1:
        bad = [n for n in range(2, N+1) if (B[n]*D[n]**(w-1)).denominator != 1]
        sharp = (len(bad), bad[:5])
    ids = []
    if agree > 12:
        tol = mp.mpf(10)**(-(agree*0.75))
        for name, c in CONSTS.items():
            r = mp.pslq([L, c], tol=tol, maxcoeff=10**6, maxsteps=50000)
            if r and r[0] != 0:
                q = F(-int(r[1]), int(r[0]))
                if max(abs(q.numerator), q.denominator) < 10**4:
                    ids.append((str(q), name, float(-mp.log10(abs(L - q.numerator*c/q.denominator)/abs(L)))))
    out[lab] = dict(w=w, sharp=sharp, agree=agree, L=mp.nstr(L, 30), ids=ids)
    print(f'{lab:7s} w={w} sharp_fail={sharp[0] if sharp else "-":>4} agree~{agree:7.1f}  L={mp.nstr(L,22)}')
    for q, name, d_ in ids: print(f'          == {q} * {name}   (matches to {d_:.0f} digits)')

pickle.dump(out, open('t1b.pkl', 'wb'))
