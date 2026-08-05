"""eps64_kz32.py -- Project C execution: is the Koutschan-Zudilin z=1/2
(conductor-32 CM) exterior-square recurrence modularly rectifiable?

Recurrence (KZ 2022, arXiv:2111.08796, transcribed from the fetched paper;
z symbolic then z=1/2), acting on A_n (and B_n):
  c1(n) A_{n+1} + c0(n) A_n + cm1(n) A_{n-1} + cm2(n) A_{n-2} = 0,
  c1  =  4(n+1)(n+2)^2(2n+1)^2(2n+3)^2 z^8 p0(n) p0(n-1)
  c0  = -4(n+1)^2(2n+1)^2 z^4 p0(n-1) Q1(n)
  cm1 = -n(2n-1)^2(1-z) z^2 p0(n+1) Q2(n)
  cm2 = -4(n-1)n^2(2n-3)^2(2n-1)^2(1-z)^2 p0(n) p0(n+1)
  p0  = 16(27z-32)n^4 + 48(13z-14)n^3 + 8(18z-11)n^2 - 4(19z-24)n - (7z+6)
Initial data at z=1/2: A: 26, 146, 171368/25; B: 0, 2494/9, 2743456/225.
"""
import sys, os
from fractions import Fraction as F_
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import eps48_modular_nome as M
N = M.N
from eps48_modular_nome import smul, sinv, sexp, srevert, compose, gseries
import sympy as sp

nv, zv = sp.symbols('n z')
p0 = 16*(27*zv-32)*nv**4 + 48*(13*zv-14)*nv**3 + 8*(18*zv-11)*nv**2 \
     - 4*(19*zv-24)*nv - (7*zv+6)
Q1 = (64*(3*zv**2-20*zv+16)*(27*zv-32)*nv**7
      + 64*(3*zv**2-20*zv+16)*(147*zv-170)*nv**6
      + 16*(3369*zv**3-26678*zv**2+44012*zv-20576)*nv**5
      + 16*(2457*zv**3-20918*zv**2+34376*zv-15896)*nv**4
      + 4*(843*zv**3-16808*zv**2+29432*zv-13736)*nv**3
      - 4*(1445*zv**3-6794*zv**2+9600*zv-4144)*nv**2
      - (741*zv**3-6922*zv**2+10772*zv-4728)*nv
      + zv**2*(131*zv-66))
Q2 = (256*(3*zv+8)*(27*zv-32)*nv**8 - 256*(3*zv+8)*(15*zv-22)*nv**7
      - 64*(651*zv**2+661*zv-1744)*nv**6 + 192*(59*zv**2-186)*nv**5
      + 16*(1503*zv**2+697*zv-3610)*nv**4 - 16*(79*zv**2-290*zv+116)*nv**3
      - 4*(569*zv**2-381*zv-580)*nv**2 + 4*(11*zv**2-44*zv+18)*nv
      + 3*(4*zv+3)*(7*zv-10))
c1  = 4*(nv+1)*(nv+2)**2*(2*nv+1)**2*(2*nv+3)**2*zv**8 \
      * p0*p0.subs(nv, nv-1)
c0  = -4*(nv+1)**2*(2*nv+1)**2*zv**4*p0.subs(nv, nv-1)*Q1
cm1 = -nv*(2*nv-1)**2*(1-zv)*zv**2*p0.subs(nv, nv+1)*Q2
cm2 = -4*(nv-1)*nv**2*(2*nv-3)**2*(2*nv-1)**2*(1-zv)**2*p0*p0.subs(nv, nv+1)

Z = F_(1, 2)
def ev(expr, n):
    v = expr.subs({zv: sp.Rational(1, 2), nv: n})
    v = sp.nsimplify(v)
    r = sp.Rational(v)
    return F_(int(r.p), int(r.q))

def seqs(x0, x1, x2, top):
    A = [x0, x1, x2]
    for n in range(2, top):
        s = ev(c0, n)*A[n] + ev(cm1, n)*A[n-1] + ev(cm2, n)*A[n-2]
        A.append(-s/ev(c1, n))
    return A

if __name__ == '__main__':
    A = seqs(F_(26), F_(146), F_(171368, 25), N+2)
    B = seqs(F_(0), F_(2494, 9), F_(2743456, 225), N+2)
    print('A[3..5]:', [str(x) for x in A[3:6]])
    # agent cross-check: A3 = 2033916/5, A4 = 18919290512/675
    assert A[3] == F_(2033916, 5) and A[4] == F_(18919290512, 675), 'MISMATCH'
    assert B[3] == F_(380414354, 525), 'B MISMATCH'
    print('cross-check vs agent table: PASS')
    # operator Pj(theta): P0 = c1(th-1), P1 = c0(th), P2 = cm1(th+1), P3 = cm2(th+2)
    th = sp.symbols('th')
    sub = {zv: sp.Rational(1, 2)}
    Pjs = [sp.expand(c1.subs(sub).subs(nv, th-1)),
           sp.expand(c0.subs(sub).subs(nv, th)),
           sp.expand(cm1.subs(sub).subs(nv, th+1)),
           sp.expand(cm2.subs(sub).subs(nv, th+2))]
    # verify L(y_A) = 0 (+ boundary), get defect for B
    Pl = [sp.Poly(pp, th) for pp in Pjs]
    def applyL(y):
        out = [F_(0)]*(N+1)
        for j in range(4):
            for m in range(0, N+1-j):
                cc = sp.Rational(Pl[j].eval(m))
                out[m+j] += F_(int(cc.p), int(cc.q))*y[m]
        return out
    rA = applyL(A[:N+1]); rB = applyL(B[:N+1])
    print('L(y_A) head:', [str(x) for x in rA[:5]], 'tail0:', all(x == 0 for x in rA[5:]))
    print('L(y_B) head:', [str(x) for x in rB[:5]], 'tail0:', all(x == 0 for x in rB[5:]))
    # indicial polynomial P0(theta): factor
    print('indicial factor:', sp.factor(Pjs[0]))
    # normalize y0 = A/26 and attempt canonical nome
    y0 = [x/F_(26) for x in A[:N+1]]
    g = gseries(Pjs, y0)
    qser = smul([F_(0), F_(1)] + [F_(0)]*(N-1), sexp(smul(g, sinv(y0))))
    tq = srevert(qser)
    print('t(q) 1..6:', [str(tq[i]) for i in range(1, 7)])
    print('t(q) denominators 1..10:', [tq[i].denominator for i in range(1, 11)])
    from eps60_phi_source import detect_rescale
    mu = detect_rescale(tq)
    print('detect_rescale mu =', mu)
    if mu is None:
        found = []
        for a_ in range(-10, 11):
            for b_ in range(-4, 5):
                for cc_ in range(-3, 4):
                    m_ = F_(2)**a_ * F_(3)**b_ * F_(5)**cc_
                    for s_ in (1, -1):
                        mm = s_*m_
                        if all((tq[n]*mm**(1-n)).denominator == 1
                               for n in range(2, N+1)):
                            found.append(mm)
        print('exhaustive mu scan (2^a 3^b 5^c, |a|<=10,|b|<=4,|c|<=3):',
              found if found else 'NONE')
