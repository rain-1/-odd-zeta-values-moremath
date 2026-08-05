"""eps62b_cusp_limit.py -- the Apery limit of the cuspidal companion
B^f (eps62), via the inhomogeneous recurrence

  m^3 B_m = (2m-1)(17(m-1)^2+17(m-1)+5) B_{m-1} - (m-1)^3 B_{m-2} + w_{m-1},

w = coefficients of (1-34t+t^2)^{-1/2}:  (n+1)w_{n+1} = 17(2n+1)w_n - n w_{n-1}.

xi_f = lim B^f_n / A_n  (error ~ alpha^{-2n}, alpha = (1+sqrt2)^4).
Then L(f,s) for f = 6.4.a.a = (eta1 eta2 eta3 eta6)^2 via the completed
L-function with eps = +1 (lambda_2 = lambda_3 = +1 from a_2=-2, a_3=-3),
and PSLQ.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
mp.mp.dps = 120

NTOP = 1500

def sequences():
    A = [mp.mpf(1), mp.mpf(5)]
    B = [mp.mpf(0), mp.mpf(1)]
    w = [mp.mpf(1), mp.mpf(17)]
    for n in range(1, NTOP+2):
        w.append((17*(2*n+1)*w[n] - n*w[n-1])/(n+1))
    for m in range(2, NTOP+1):
        c1 = (2*m-1)*(17*(m-1)**2 + 17*(m-1) + 5)
        c2 = (m-1)**3
        A.append((c1*A[m-1] - c2*A[m-2])/mp.mpf(m)**3)
        B.append((c1*B[m-1] - c2*B[m-2] + w[m-1])/mp.mpf(m)**3)
    return A, B

def eta_coeffs(n_top):
    """a_n of (eta1 eta2 eta3 eta6)^2 by exact convolution."""
    from fractions import Fraction as F_
    def etap(m, n):
        out = [0]*(n+1); out[0] = 1
        # (prod (1-q^{mk}))^1 via Euler: use recurrence by multiplication
        cur = [0]*(n+1); cur[0] = 1
        k = 1
        while m*k <= n:
            new = list(cur)
            for i in range(n+1-m*k):
                new[i+m*k] -= cur[i]
            cur = new; k += 1
        return cur
    def mul(a, b, n):
        out = [0]*(n+1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b[:n+1-i]):
                    if y:
                        out[i+j] += x*y
        return out
    n = n_top
    P1 = etap(1, n); P2 = etap(2, n); P3 = etap(3, n); P6 = etap(6, n)
    prod = mul(mul(P1, P1, n), mul(P2, P2, n), n)
    prod = mul(prod, mul(P3, P3, n), n)
    prod = mul(prod, mul(P6, P6, n), n)
    a = [0]*(n+2)
    for i in range(n+1):
        a[i+1] = prod[i]
    return a

def Lf(a, s, eps=1, NLEV=6):
    """L(f,s) via completed-L incomplete-gamma formula, weight 4."""
    A0 = mp.sqrt(NLEV)/(2*mp.pi)
    tot = mp.mpf(0)
    for n in range(1, len(a)):
        if a[n] == 0: continue
        x = mp.mpf(n)/A0
        tot += a[n]*(mp.gammainc(s, x)/mp.mpf(n)**s
                     + eps*mp.gammainc(4-s, x)*A0**(4-2*s)/mp.mpf(n)**(4-s))
        if x > 300: break
    return tot*A0**s/mp.gamma(s)/A0**s * 1  # Lambda(s)/ (A0^s Gamma(s)) = L
    # note: Lambda(s) = A0^s Gamma(s) L(f,s)

if __name__ == '__main__':
    A, B = sequences()
    xi = B[NTOP]/A[NTOP]
    xi2 = B[NTOP-1]/A[NTOP-1]
    print('xi_f  =', mp.nstr(xi, 100))
    print('|delta| =', mp.nstr(abs(xi-xi2), 5))
    a = eta_coeffs(400)
    # Lambda(s) = A0^s Gamma(s) L(s); formula returns sum = Lambda(s)
    A0 = mp.sqrt(6)/(2*mp.pi)
    def Lval(s):
        tot = mp.mpf(0)
        for n in range(1, len(a)):
            if a[n] == 0: continue
            x = mp.mpf(n)/A0
            if x > 350: break
            tot += a[n]*(mp.gammainc(s, x)/(A0**s*mp.mpf(n)**s)*A0**s
                         ) if False else 0
        # clean implementation below
        Lam = mp.mpf(0)
        for n in range(1, len(a)):
            if a[n] == 0: continue
            x = 2*mp.pi*n/mp.sqrt(6)
            if x > 350: break
            Lam += a[n]*(mp.gammainc(s, x)*(2*mp.pi*n/mp.sqrt(6))**-s
                         + mp.gammainc(4-s, x)*(2*mp.pi*n/mp.sqrt(6))**(s-4))
        # Lambda(s) = (sqrt6/2pi)^s Gamma(s) L(s) = sum a_n [...] with x=2pi n/sqrt6
        return Lam/mp.gamma(s)
    L1 = Lval(1); L2 = Lval(2); L3 = Lval(3)
    print('L(f,1) =', mp.nstr(L1, 40))
    print('L(f,2) =', mp.nstr(L2, 40))
    print('L(f,3) =', mp.nstr(L3, 40))
    print('check L(f,1) - 3L(f,3)/pi^2 =', mp.nstr(L1 - 3*L3/mp.pi**2, 8))
    pi = mp.pi
    basis = {'L3': L3, 'piL2': pi*L2, 'pi3': pi**3, 'z3': mp.zeta(3),
             'pi2': pi**2, '1': mp.mpf(1)}
    names = list(basis)
    vec = [xi] + [basis[k] for k in names]
    for mc in (10**4, 10**8):
        rel = mp.pslq(vec, tol=mp.mpf(10)**-80, maxcoeff=mc, maxsteps=500000)
        print('PSLQ maxcoeff %g:' % mc, rel, ['xi']+names)
        if rel: break
