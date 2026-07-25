"""T4: verify the two steps of the general proof, per sequence, exactly.
Step V (vanishing layer):  sum over k with p | S(n,k) of  S(n,k) p^w w(n,k)  ==  0 mod p
Step U (surviving layer):  sum over k with p!|S(n,k) of  S(n,k) p^w w(n,k)  ==  chi(p) B_a A_r mod p
Also: does the surviving region ever carry an argument >= p^2  (tameness)?
"""
from fractions import Fraction as F
from math import comb
from sporadic import SEQS, gen_A, gen_B

INF = 10**7
def vpi(x, p):
    if x == 0: return INF
    v = 0
    while x % p == 0: x //= p; v += 1
    return v
def vp(x, p):
    if x == 0: return INF
    return vpi(x.numerator, p) - vpi(x.denominator, p)

H = {}
def Hh(r, y):
    t = H.setdefault(r, [F(0)])
    while len(t) <= y: t.append(t[-1] + F(1, len(t)**r))
    return t[y]
K = {}
def Kk(D, r, y):
    t = K.setdefault((D, r), [F(0)])
    while len(t) <= y:
        m = len(t); c = 0 if m % 2 == 0 else (1 if m % 4 == 1 else -1)   # chi_{-4}
        t.append(t[-1] + F(c, m**r))
    return t[y]

AR = {'n': lambda n,k: n, 'k': lambda n,k: k, 'n-k': lambda n,k: n-k, 'n+k': lambda n,k: n+k,
      '2k': lambda n,k: 2*k, '2n-2k': lambda n,k: 2*(n-k), '2k-n': lambda n,k: 2*k-n}

# (label, w, chi-disc, summand, weight  [(coeff, [(kind,r,arg),...]), ...])
DEC = [
 ('gamma', 3, 1, lambda n,k: comb(n,k)**2*comb(n+k,n)**2,
   [(F(1,3), [('H',3,'n')]), (F(-1,6), [('H',3,'k')])]),
 ('A', 2, 1, lambda n,k: comb(n,k)**3,
   [(F(1,4), [('H',2,'k')]), (F(3,4), [('H',1,'k'),('H',1,'k')]), (F(-3,4), [('H',1,'k'),('H',1,'n-k')])]),
 ('D', 2, 1, lambda n,k: comb(n,k)**2*comb(n+k,n),
   [(F(1,5), [('H',2,'n')]), (F(2,5), [('H',1,'k'),('H',1,'k')]),
    (F(-1,5), [('H',1,'k'),('H',1,'n-k')]), (F(-1,5), [('H',1,'n'),('H',1,'k')])]),
 ('s10', 2, 1, lambda n,k: comb(n,k)**4,
   [(F(1,5), [('H',2,'k')]), (F(4,5), [('H',1,'k'),('H',1,'k')]), (F(-4,5), [('H',1,'k'),('H',1,'n-k')])]),
 ('s7', 2, 1, lambda n,k: comb(n,k)**2*comb(n+k,k)*comb(2*k,n),
   [(F(3,14),[('H',1,'k'),('H',1,'2k')]), (F(-9,28),[('H',1,'k'),('H',1,'k')]),
    (F(3,7),[('H',1,'k'),('H',1,'n-k')]), (F(-3,14),[('H',1,'n-k'),('H',1,'2k')]),
    (F(-3,28),[('H',1,'n-k'),('H',1,'n-k')]), (F(5,28),[('H',2,'k')]),
    (F(1,14),[('H',2,'n')]), (F(-3,28),[('H',2,'n-k')])]),
 ('eps', 3, 1, lambda n,k: comb(n,k)**2*comb(2*k,n)**2,
   [(F(-1,4),[('H',2,'2k'),('H',1,'2k')]), (F(1,4),[('H',2,'2k'),('H',1,'2k-n')]),
    (F(1,8),[('H',2,'2k'),('H',1,'k')]), (F(-1,8),[('H',2,'2k'),('H',1,'n-k')]),
    (F(1,16),[('H',2,'k'),('H',1,'2k')]), (F(-1,16),[('H',2,'k'),('H',1,'2k-n')]),
    (F(-1,32),[('H',2,'k'),('H',1,'k')]), (F(1,32),[('H',2,'k'),('H',1,'n-k')]),
    (F(1,4),[('H',3,'2k')]), (F(-1,32),[('H',3,'k')])]),
 ('alpha', 3, 1, lambda n,k: comb(n,k)**2*comb(2*k,k)*comb(2*(n-k),n-k),
   [(F(1,4),[('H',1,'k'),('H',1,'2k'),('H',1,'2k')]),
    (F(-1,2),[('H',1,'k'),('H',1,'2k'),('H',1,'2n-2k')]),
    (F(1,4),[('H',1,'k'),('H',1,'2n-2k'),('H',1,'2n-2k')]),
    (F(-1),[('H',1,'k'),('H',1,'k'),('H',1,'2k')]),
    (F(1),[('H',1,'k'),('H',1,'k'),('H',1,'2n-2k')]),
    (F(1),[('H',1,'k'),('H',1,'k'),('H',1,'k')]),
    (F(-1),[('H',1,'k'),('H',1,'k'),('H',1,'n-k')]),
    (F(-1,4),[('H',2,'2k'),('H',1,'k')]), (F(-1,4),[('H',2,'2k'),('H',1,'n-k')]),
    (F(-5,12),[('H',2,'k'),('H',1,'2k')]), (F(5,12),[('H',2,'k'),('H',1,'2n-2k')]),
    (F(13,12),[('H',2,'k'),('H',1,'k')]), (F(-7,12),[('H',2,'k'),('H',1,'n-k')]),
    (F(7,24),[('H',3,'k')])]),
 ('E', 2, -4, lambda n,k: comb(n,k)*comb(2*k,k)*comb(2*(n-k),n-k),
   [(F(-1,2),[('H',1,'2k'),('K',1,'2k')]), (F(1,2),[('H',1,'2k'),('K',1,'2n-2k')]),
    (F(3,4),[('H',1,'k'),('K',1,'2k')]), (F(-3,4),[('H',1,'k'),('K',1,'2n-2k')]),
    (F(1,2),[('K',2,'2k')])]),
]
def wval(dec, n, k, D):
    tot = F(0)
    for c, mo in dec:
        v = c
        for kind, r, a in mo:
            y = AR[a](n, k)
            if y < 0: v = F(0); break
            v *= Hh(r, y) if kind == 'H' else Kk(D, r, y)
        tot += v
    return tot
def chi(D, p):
    if D == 1: return 1
    if D == -4: return 1 if p % 4 == 1 else -1

PR = [5, 7, 11, 13]
for lab, w, D, S, dec in DEC:
    fam, par = {l: (f, pp) for l, f, pp, _, _ in SEQS}[lab]
    A = gen_A(fam, par, 400); B = gen_B(fam, par, 400)
    for p in PR:
        c = chi(D, p); pw = F(p)**w
        badV = badU = 0; maxarg = 0; tame = True
        for a in range(1, p):
            for r in range(p):
                n = a*p + r
                V = F(0); U = F(0)
                for k in range(0, n+1):
                    s = S(n, k)
                    if s == 0: continue
                    term = s*pw*wval(dec, n, k, D)
                    if vpi(s, p) >= 1: V += term
                    else:
                        U += term
                        for _, mo in dec:
                            for _, _, ag in mo:
                                y = AR[ag](n, k); maxarg = max(maxarg, y)
                                if y >= p*p: tame = False
                if vp(V, p) < 1: badV += 1
                if vp(U - c*B[a]*A[r], p) < 1: badU += 1
        print(f'{lab:6s} p={p:3d} chi={c:>2}  vanishing-layer fails={badV:>3}  '
              f'surviving-layer fails={badU:>3}  max surviving arg={maxarg} (p^2={p*p}) tame={tame}', flush=True)
    print(flush=True)
