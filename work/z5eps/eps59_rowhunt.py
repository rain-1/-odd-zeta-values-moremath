"""eps59_rowhunt.py -- normal-form row hunt for the BZ zeta(5) 5-block.

(a) Exact coupled normal form of the block in the mirror coordinate:
    with a_j := ghat_j / F (j = 2,3,4), alpha := theta a2,
      Khat := 1 + theta(alpha)                      (= 1 + K(q))
      Mhat := 1 + theta( (2 theta a2 + theta^2 a3) / Khat )
      Bser := (2 theta a2 + theta^2 a3)/Khat + theta( (a2 + 2 theta a3
              + theta^2 a4) / Mhat )
      Rhat := 1 + theta( Bser / Mhat )
    and  N = theta o Rhat^{-1} o theta o Mhat^{-1} o theta o Khat^{-1}
             o theta o theta .
    N annihilates the rectified flag u_j = Yhat_j / F (verified on the
    log-vector representation).  Self-duality test: Rhat =?= Khat.
(b) Row hunt: phi_row := (row-generating-function composed with t(q)) / F;
    h_row := N(phi_row).  If the mirror form of the bridge is right, h_row
    is SIMPLE (low height / integral after small rescale).  Control: the
    same computation for Apery zeta(3) (order-3 block, N = theta o
    Khat^{-1} o theta o theta), where the proved Beukers form calibrates
    what "simple" looks like.
(c) Boundary defects: L9(row-gen) = polynomial of degree <= 2, computed
    exactly (the recurrence's N = 0,1,2 rows).
All arithmetic exact Fractions, series order NN = 32.
"""

import sys
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import core
import sympy as sp
import eps53_z5_deep as E
from eps48_modular_nome import smul, sinv, sexp, srevert, compose, A_seq_R3

NN = E.NN

# ---------------- series utilities ----------------
def theta(a):
    return [F(k) * a[k] for k in range(len(a))]

def sadd(a, b, c=F(1)):
    return [a[i] + c * b[i] for i in range(len(a))]

def sscale(a, c):
    return [c * v for v in a]

def hprof(a, upto=14):
    return [a[i].denominator for i in range(upto + 1)]

def maxheight(a, upto=14):
    return max(abs(a[i].numerator).bit_length() + a[i].denominator.bit_length()
               for i in range(upto + 1))

# ---------------- log-vector algebra (slot i = coeff of (log q)^i / i!) ----
def vec_theta(vec):
    out = []
    L = len(vec)
    for i in range(L):
        s = theta(vec[i])
        if i + 1 < L:
            s = sadd(s, vec[i + 1])
        out.append(s)
    return out

def vec_mul(series, vec):
    return [smul(series, s, NN) for s in vec]

# ---------------- BZ block normal form ----------------
fs = E.fs
y0 = fs[0]
tq = E.tq
Fq = E.Fq
rho = compose(smul(fs[1], sinv(fs[0], NN), NN), tq, NN)

def ghat(k):
    """ghat_k = sum_m f_{k-m} (-rho)^m / m!  (in q)."""
    from math import factorial
    out = [F(0)] * (NN + 1)
    rp = [F(0)] * (NN + 1)
    rp[0] = F(1)
    for m in range(0, k + 1):
        fq = compose(fs[k - m], tq, NN)
        term = smul(fq, rp, NN)
        out = sadd(out, sscale(term, F((-1) ** m, factorial(m))))
        rp = smul(rp, rho, NN)
    return out

gh = {j: ghat(j) for j in range(5)}
assert all(v == 0 for v in gh[1]), 'mirror normalization broken'
iF = sinv(Fq, NN)
a2 = smul(gh[2], iF, NN)
a3 = smul(gh[3], iF, NN)
a4 = smul(gh[4], iF, NN)

alpha = theta(a2)
Khat = sadd([F(1)] + [F(0)] * NN, theta(alpha))
iK = sinv(Khat, NN)
inner1 = sadd(sscale(theta(a2), F(2)), theta(theta(a3)))
Mhat = sadd([F(1)] + [F(0)] * NN, theta(smul(inner1, iK, NN)))
iM = sinv(Mhat, NN)
inner2 = sadd(sadd(a2, sscale(theta(a3), F(2))), theta(theta(a4)))
Bser = sadd(smul(inner1, iK, NN), theta(smul(inner2, iK, NN)))
Rhat = sadd([F(1)] + [F(0)] * NN, theta(smul(Bser, iM, NN)))
iR = sinv(Rhat, NN)

def Nop(vec):
    """N = theta Rhat^{-1} theta Mhat^{-1} theta Khat^{-1} theta theta,
    acting on log-vectors."""
    v = vec_theta(vec)
    v = vec_theta(v)
    v = vec_mul(iK, v)
    v = vec_theta(v)
    v = vec_mul(iM, v)
    v = vec_theta(v)
    v = vec_mul(iR, v)
    v = vec_theta(v)
    return v

# flag vectors u_j (rectified): u_j = sum_i (a_{j-i} as slot i), a_0 = 1,
# a_1 = 0
aa = {0: [F(1)] + [F(0)] * NN, 1: [F(0)] * (NN + 1), 2: a2, 3: a3, 4: a4}
print('== BZ 5-block normal form ==')
ok = True
for j in range(5):
    vec = [aa[j - i] if 0 <= j - i <= 4 else [F(0)] * (NN + 1)
           for i in range(5)]
    out = Nop(vec)
    z = all(all(x == 0 for x in s[:NN - 6]) for s in out)
    ok = ok and z
    print('  N(u_%d) = 0 (to order %d): %s' % (j, NN - 7, z))
print('  couplings: Khat_1..6:', [str(Khat[i]) for i in range(1, 7)])
print('             Mhat_1..6:', [str(Mhat[i]) for i in range(1, 7)])
print('             Rhat_1..6:', [str(Rhat[i]) for i in range(1, 7)])
print('  SELF-DUALITY Rhat == Khat:',
      all(Rhat[i] == Khat[i] for i in range(NN - 6)))
print('  Khat integral:', all(Khat[i].denominator == 1 for i in range(NN - 6)),
      ' Mhat integral:', all(Mhat[i].denominator == 1 for i in range(NN - 6)))

# ---------------- boundary defects ----------------
def defect(row):
    out = []
    for Nn in range(3):
        s = F(0)
        for j in range(4):
            m = Nn - j
            if m >= 0:
                s += F(int(E.PJ[j].eval(m))) * row[m]
        out.append(s)
    return out

Phs = [F(core.Ph(n)) for n in range(NN + 1)]
Ps = [F(core.P(n)) for n in range(NN + 1)]
print('\nboundary defects L9(gen) = d0 + d1 t + d2 t^2:')
print('  Phat:', [str(v) for v in defect(Phs)])
print('  P   :', [str(v) for v in defect(Ps)])

# ---------------- row hunt ----------------
def hunt(name, row):
    phi = smul(compose(row, tq, NN), iF, NN)
    vec = [phi] + [[F(0)] * (NN + 1)] * 4
    h = Nop(vec)[0]
    print(' %s: h = N(phi) coeffs 0..8:' % name,
          [str(h[i]) for i in range(9)])
    print('    denominators:', hprof(h))
    for lam in (1, 2, 3, 4, 6, 8, 12, 16, 24, 48, 96):
        if all((h[i] * lam).denominator == 1 for i in range(NN - 6)):
            print('    %d*h INTEGRAL to order %d' % (lam, NN - 7))
            return h
    print('    no integral rescale (height profile: max bits %d)'
          % maxheight(h))
    return h

print('\n== row hunt (BZ) ==')
hPh = hunt('Phat', Phs)
hP = hunt('P', Ps)

# ---------------- control: Apery zeta(3) ----------------
print('\n== control: Apery zeta(3) ==')
a_, b_, c_, d_ = 17, 5, 1, 0
A = A_seq_R3(a_, b_, c_, d_, NN + 2)[:NN + 1]
Bap = [F(0), F(6)]
for n in range(1, NN):
    Bap.append((F((2 * n + 1) * (a_ * n * n + a_ * n + b_)) * Bap[n]
                - F(n * (c_ * n * n + d_)) * Bap[n - 1]) / F((n + 1) ** 3))
th = sp.symbols('th')
Pjg = [sp.Poly(th**3, th),
       sp.Poly(-sp.expand((2 * th + 1) * (a_ * th**2 + a_ * th + b_)), th),
       sp.Poly(sp.expand((th + 1) * (c_ * (th + 1)**2 + d_)), th)]
# Frobenius tower for gamma
def gtower(y0g, kmax):
    Pd = [[sp.Poly(sp.diff(p.as_expr(), th, i), th) for p in Pjg]
          for i in range(4)]
    from math import factorial
    fsg = [list(y0g)]
    for k in range(1, kmax + 1):
        R = [F(0)] * (NN + 1)
        for i in range(1, k + 1):
            for j in range(3):
                for m in range(0, NN + 1 - j):
                    if fsg[k - i][m]:
                        R[m + j] -= F(int(Pd[i][j].eval(m)),
                                      factorial(i)) * fsg[k - i][m]
        f = [F(0)] * (NN + 1)
        for Nn in range(1, NN + 1):
            acc = R[Nn]
            for j in range(1, 3):
                if Nn - j >= 0:
                    acc -= F(int(Pjg[j].eval(Nn - j))) * f[Nn - j]
            f[Nn] = acc / F(int(Pjg[0].eval(Nn)))
        fsg.append(f)
    return fsg

fsg = gtower(A, 2)
gg1 = fsg[1]
qg = smul([F(0), F(1)] + [F(0)] * (NN - 1),
          sexp(smul(gg1, sinv(A, NN), NN), NN), NN)
tqg = srevert(qg, NN)
Fg = compose(A, tqg, NN)
rhog = compose(smul(gg1, sinv(A, NN), NN), tqg, NN)
gh2g = sadd(sadd(compose(fsg[2], tqg, NN),
                 sscale(smul(compose(fsg[1], tqg, NN), rhog, NN), F(-1))),
            sscale(smul(compose(fsg[0], tqg, NN),
                        smul(rhog, rhog, NN), NN), F(1, 2)))
a2g = smul(gh2g, sinv(Fg, NN), NN)
Kg = sadd([F(1)] + [F(0)] * NN, theta(theta(a2g)))
iKg = sinv(Kg, NN)
print('  Kg_1..6:', [str(Kg[i]) for i in range(1, 7)],
      ' integral:', all(Kg[i].denominator == 1 for i in range(NN - 6)))

def Nop3(vec):
    v = vec_theta(vec)
    v = vec_theta(v)
    v = vec_mul(iKg, v)
    v = vec_theta(v)
    return v

phig = smul(compose(Bap, tqg, NN), sinv(Fg, NN), NN)
hg = Nop3([phig] + [[F(0)] * (NN + 1)] * 2)[0]
print('  control h = N(B/A-rectified): coeffs 0..8:',
      [str(hg[i]) for i in range(9)])
print('    denominators:', hprof(hg))
for lam in (1, 2, 3, 6):
    if all((hg[i] * lam).denominator == 1 for i in range(NN - 6)):
        print('    %d*h INTEGRAL -- control shows the "simple" signature'
              % lam)
        break
