"""eps61b_complex_limits.py -- high-precision complex Eichler limits for the
three no-limit families B, delta, eta (complex conjugate singularities;
fields Q(sqrt-3), Q(sqrt-2), Q(i)), with PSLQ recognition.
Series order N=60, dps=80.
"""
import sys, os
from fractions import Fraction as F_
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import eps48_modular_nome as M
NN = 60
M.N = NN
import importlib
import eps60_phi_source as E60
importlib.reload(E60)
E60.N = NN
import mpmath as mp
mp.mp.dps = 80

def chi_m3(d): return [0, 1, -1][d % 3]
def chi_m4(d): return [0, 1, 0, -1][d % 4]
def chi_5(d):  return [0, 1, -1, -1, 1][d % 5]
def chi_m8(d): return [0, 1, 0, 1, 0, -1, 0, -1][d % 8]

def S(chi, k, mode):
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

S1_3m2 = S(chi_m3, 2, 2)
T5m2   = S(chi_5, 3, 2)
def combo(f, terms):
    return lambda m: sum(co*f(m/dd) for dd, co in terms)

FAMDATA = {
 'B':     (2, 9, 3, 27, 0, combo(S1_3m2, [(1,1),(2,-6),(4,-8)]), (9, 27)),
 'delta': (3, 7, 3, 81, 0,
           combo(sig3, [(1,1),(2,-14),(3,-1),(4,16),(6,14),(12,-16)]),
           (14, 81)),
 'eta':   (3, 11, 5, 125, 0, combo(T5m2, [(1,1),(2,-14),(4,-16)]), (22, 125)),
}

def mpf_of(x): return mp.mpf(x.numerator)/mp.mpf(x.denominator)

def run(name):
    r, a, b, c, d, cf, (pa, pc) = FAMDATA[name]
    tq, Fq, Phi = E60.phi_series(name, r, a, b, c, d)
    mu = E60.detect_rescale(tq)
    ts = [mpf_of(x) for x in E60.rescale(tq, mu, shift=1)]
    Fs = [mpf_of(x) for x in E60.rescale(Fq, mu, shift=0)]
    disc = mp.mpc(pa*pa - 4*pc)
    tc = (pa - mp.sqrt(disc))/(2*pc)
    # Newton for q_c
    q = mp.mpmathify(tc)
    for _ in range(200):
        tv = sum(ts[n]*q**n for n in range(len(ts)))
        td = sum(n*ts[n]*q**(n-1) for n in range(1, len(ts)))
        q = q - (tv-tc)/td
    qc = q
    serr = abs(qc)**NN
    Mtop = 4000
    Th  = mp.fsum(cf(m)*qc**m/mp.mpf(m)**r for m in range(1, Mtop))
    Thd = mp.fsum(cf(m)*mp.mpf(m)**(1-r)*qc**(m-1) for m in range(1, Mtop))
    Fv = sum(Fs[n]*qc**n for n in range(len(Fs)))
    Fd = sum(n*Fs[n]*qc**(n-1) for n in range(1, len(Fs)))
    xi = Th + Fv*Thd/Fd
    print('%s: q_c=%s  |q_c|^N=%.1e' % (name, mp.nstr(qc, 12), serr))
    print('  xi = %s' % mp.nstr(xi, 45), flush=True)
    return xi, serr

def Lchi(chi, s, per):
    return mp.nsum(lambda n: chi(int(n))/mp.mpf(n)**s, [1, mp.inf])

if __name__ == '__main__':
    pi = mp.pi
    L32 = Lchi(chi_m3, 2, 3); L33 = Lchi(chi_m3, 3, 3)
    L43 = Lchi(chi_m4, 3, 4); L53 = Lchi(chi_5, 3, 5)
    L83 = Lchi(chi_m8, 3, 8)
    bases = {
     'B': {'1': mp.mpf(1), 'L32': L32, 'pi2': pi**2, 'pi2/s3': pi**2/mp.sqrt(3),
           'pilog3': pi*mp.log(3), 'log2_3': mp.log(3)**2, 'G': mp.catalan},
     'delta': {'1': mp.mpf(1), 'z3': mp.zeta(3), 'pi3/s2': pi**3/mp.sqrt(2),
               'L83': L83, 'pi3': pi**3, 'pi2log2': pi**2*mp.log(2),
               'pilog2_2': pi*mp.log(2)**2},
     'eta': {'1': mp.mpf(1), 'z3': mp.zeta(3), 'L43': L43, 'L53': L53,
             'pi3': pi**3, 'pi3/s5': pi**3/mp.sqrt(5),
             'pi2log': pi**2*mp.log((1+mp.sqrt(5))/2)},
    }
    for name in FAMDATA:
        xi, serr = run(name)
        tol = max(serr*100, mp.mpf(10)**-60)
        basis = bases[name]
        for part, val in (('Re', mp.re(xi)), ('Im', mp.im(xi))):
            names = list(basis)
            vec = [val] + [basis[k] for k in names]
            rel = mp.pslq(vec, tol=tol, maxcoeff=10**7, maxsteps=100000)
            print('  %s PSLQ (tol %.0e): %s   %s'
                  % (part, float(tol), rel, ['xi']+names), flush=True)
