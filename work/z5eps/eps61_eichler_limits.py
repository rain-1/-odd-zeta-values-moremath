"""eps61_eichler_limits.py -- Apery limits as Eichler values of the
identified sources Phi (eps60/eps60b), Sol flagship step 4.

For each identified family: c(m) is an explicit divisor sum, so
    xi = (theta_q^{-r} Phi)(q_c) = sum_{m>=1} c(m) m^{-r} q_c^m,
with q_c the nome of the dominant singularity t_c of P(t) (root of minimal
modulus), q_c solved from the exact 26-term series t(q) by Newton (|q_c|
small => series error ~ |q_c|^26, tracked).

Check xi against the known Apery limit for the nine limit families; for the
three 'no-limit' families (B, delta, eta: complex conjugate singularities)
compute the complex Eichler value and attempt PSLQ recognition of Re/Im.
"""
import sys, os
from fractions import Fraction as F_
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import eps48_modular_nome as M
M.N = 26
from eps60_phi_source import phi_series, detect_rescale, rescale, FAMS
import mpmath as mp
mp.mp.dps = 40

def chi_m3(d): return [0, 1, -1][d % 3]
def chi_m4(d): return [0, 1, 0, -1][d % 4]
def chi_5(d):  return [0, 1, -1, -1, 1][d % 5]
def psi1(d): return [0, 1, 0, 0, -1][d % 5]
def psi2(d): return [0, 0, 1, -1, 0][d % 5]

def S(chi, k, mode):
    """divisor-sum function of one embedding."""
    def f(m):
        if m <= 0 or m != int(m): return 0
        m = int(m)
        return sum((chi(d) if mode == 1 else chi(m//d)) * d**k
                   for d in range(1, m+1) if m % d == 0)
    return f

def sig3(m):
    if m <= 0 or m != int(m): return 0
    m = int(m)
    return sum(d**3 for d in range(1, m+1) if m % d == 0)

def prod33(m):
    if m <= 0 or m != int(m): return 0
    m = int(m)
    return sum(chi_m3(d)*chi_m3(m//d)*d**3 for d in range(1, m+1) if m % d == 0)

S1_3m1 = S(chi_m3, 2, 1)
S1_3m2 = S(chi_m3, 2, 2)
S1_4m2 = S(chi_m4, 2, 2)
T5m2   = S(chi_5, 3, 2)
Sp1    = S(psi1, 2, 1)
Sp2    = S(psi2, 2, 1)

# family -> (r, c(m), P-poly coeffs (1, pa, pc), known limit or None)
def combo(f, terms):
    return lambda m: sum(co*f(m/dd) for dd, co in terms)

CFG = {
 'A':     (2, combo(S1_3m1, [(1,1),(2,-1)]),        (7, -8),   'z2/4'),
 'B':     (2, combo(S1_3m2, [(1,1),(2,-6),(4,-8)]), (9, 27),   None),
 'C':     (2, combo(S1_3m2, [(1,1),(2,-8)]),        (10, 9),   'L32/2'),
 'D':     (2, lambda m: Sp1(m)-2*Sp2(m),            (11, -1),  'z2/5'),
 'E':     (2, combo(S1_4m2, [(1,1),(2,-8)]),        (12, 32),  'G/2'),
 'Ff':    (2, combo(S1_3m2, [(1,1),(2,-7),(4,-8)]), (17, 72),  '5L32/8'),
 'alpha': (3, combo(sig3, [(1,1),(2,-17),(3,-9),(4,16),(6,153),(12,-144)]),
           (20, 64), '7z3/24'),
 'gamma': (3, combo(sig3, [(1,1),(2,-28),(3,63),(6,-36)]), (34, 1), 'z3/6'),
 'delta': (3, combo(sig3, [(1,1),(2,-14),(3,-1),(4,16),(6,14),(12,-16)]),
           (14, 81), None),
 'eps':   (3, combo(sig3, [(1,1),(2,-21),(4,84),(8,-64)]), (24, 16), '7z3/32'),
 'zeta':  (3, prod33,                                (18, -27), 'L33/3'),
 'eta':   (3, combo(T5m2, [(1,1),(2,-14),(4,-16)]),  (22, 125), None),
}

CONST = {
 'z2/4': mp.pi**2/24, 'z2/5': mp.pi**2/30,
 'L32/2': None, '5L32/8': None, 'G/2': mp.catalan/2,
 '7z3/24': 7*mp.zeta(3)/24, 'z3/6': mp.zeta(3)/6, '7z3/32': 7*mp.zeta(3)/32,
 'L33/3': None,
}
def Lchi(chi, s, per):
    return mp.nsum(lambda n: chi(int(n))/mp.mpf(n)**s, [1, mp.inf])
L32 = Lchi(chi_m3, 2, 3); L33 = Lchi(chi_m3, 3, 3)
L53 = Lchi(chi_5, 3, 5)
CONST['L32/2'] = L32/2; CONST['5L32/8'] = 5*L32/8; CONST['L33/3'] = L33/3

def tq_poly(name):
    """exact series t(q) as float-coefficient polynomial (mu-rescaled)."""
    for fam in FAMS:
        if fam[0] == name:
            (nm, tp, a, b, c, d, level, chi, lim) = fam
            tq, Fq, Phi = phi_series(nm, tp, a, b, c, d)
            mu = detect_rescale(tq)
            th_ = rescale(tq, mu, shift=1)
            return [mp.mpf(x.numerator)/mp.mpf(x.denominator) for x in th_], tp
    raise KeyError(name)

def solve_q(tser, tc):
    """Newton solve t(q)=tc from q0=tc (complex ok)."""
    def t_of(q):
        return sum(tser[n]*q**n for n in range(len(tser)))
    def td_of(q):
        return sum(n*tser[n]*q**(n-1) for n in range(1, len(tser)))
    q = mp.mpmathify(tc)
    for _ in range(80):
        q = q - (t_of(q)-tc)/td_of(q)
    return q

def eichler(cfun, r, qc, M=3000):
    return mp.fsum(cfun(m)*qc**m/mp.mpf(m)**r for m in range(1, M+1))

def eichler_d(cfun, r, qc, M=3000):
    """d/dq theta^{-r}Phi = sum c(m) m^{1-r} q^{m-1}."""
    return mp.fsum(cfun(m)*mp.mpf(m)**(1-r)*qc**(m-1) for m in range(1, M+1))

def F_series(name):
    for fam in FAMS:
        if fam[0] == name:
            (nm, tp, a, b, c, d, level, chi, lim) = fam
            tq, Fq, Phi = phi_series(nm, tp, a, b, c, d)
            mu = detect_rescale(tq)
            Fh = rescale(Fq, mu, shift=0)
            return [mp.mpf(x.numerator)/mp.mpf(x.denominator) for x in Fh]
    raise KeyError(name)

if __name__ == '__main__':
    for name, (r, cf, (pa, pc), lim) in CFG.items():
        # roots of 1 - pa t + pc t^2
        disc = mp.mpc(pa*pa - 4*pc)
        r1 = (pa + mp.sqrt(disc))/(2*pc)
        r2 = (pa - mp.sqrt(disc))/(2*pc)
        tc = r1 if abs(r1) < abs(r2) else r2
        if abs(mp.im(tc)) < 1e-30:
            tc = mp.re(tc)
        tser, tp = tq_poly(name)
        qc = solve_q(tser, tc)
        err = abs(qc)**26
        Fs = F_series(name)
        Fv = sum(Fs[n]*qc**n for n in range(len(Fs)))
        Fd = sum(n*Fs[n]*qc**(n-1) for n in range(1, len(Fs)))
        # connection coefficient at the fold t'(q_c)=0:
        # xi = y_B'(q_c)/y_0'(q_c) = Theta(q_c) + F Theta'/F'
        xi = eichler(cf, r, qc) + Fv*eichler_d(cf, r, qc)/Fd
        line = '%-6s r=%d  t_c=%s  q_c=%s  |q_c|^26=%.1e' % (
            name, r, mp.nstr(tc, 8), mp.nstr(qc, 8), err)
        print(line, flush=True)
        if lim:
            tgt = CONST[lim]
            print('        xi = %s   known %s = %s   diff %.2e'
                  % (mp.nstr(xi, 25), lim, mp.nstr(tgt, 25), abs(xi-tgt)),
                  flush=True)
        else:
            print('        xi = %s' % mp.nstr(xi, 30), flush=True)
            # PSLQ recognition of Re, Im
            pi = mp.pi
            if r == 2:
                basis = {'G': mp.catalan, 'L32': L32, 'pi2': pi**2,
                         'pi2/sqrt3': pi**2/mp.sqrt(3),
                         'pi*log3': pi*mp.log(3), 'log^2': mp.log(3)**2}
            else:
                basis = {'z3': mp.zeta(3), 'L33': L33, 'L53': L53,
                         'pi3': pi**3, 'pi3/sqrt3': pi**3/mp.sqrt(3),
                         'pi3/sqrt5': pi**3/mp.sqrt(5),
                         'pi*L32': pi*L32, 'pi2log': pi**2*mp.log(2)}
            for part, val in (('Re', mp.re(xi)), ('Im', mp.im(xi))):
                names = list(basis)
                vec = [val] + [basis[k] for k in names]
                rel = mp.pslq(vec, tol=mp.mpf(10)**-25, maxcoeff=10**8)
                if rel:
                    print('        %s PSLQ: %s . %s' % (part, rel,
                          ['xi']+names), flush=True)
                else:
                    print('        %s PSLQ: none (basis %s)' % (part, names),
                          flush=True)
