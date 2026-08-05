"""eps60b_phi_holdouts.py -- richer character bases for the five families
eps60 could not fit: D (level 5), zeta (level 9), s7/s10/s18 (Cooper).

Generic Eisenstein vectors: m -> sum_{d|m} f(m/d) g(d) d^{k-1}, f,g drawn
from integer-valued 'real character combos' (conjugate-pair sums), plus
constant term free.  Exact fit over Q to q^26.
"""
import sys, os, json
from fractions import Fraction as F_
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import eps48_modular_nome as M
N = 26
M.N = N
from eps60_phi_source import (phi_series, detect_rescale, rescale,
                              fit_series, qd, eta_pow, FAMS)

one = lambda d: 1
def psi1(d): return [0, 1, 0, 0, -1][d % 5]   # Re of odd char mod 5 (chi(2)=i)
def psi2(d): return [0, 0, 1, -1, 0][d % 5]   # Im
def chi_m3(d): return [0, 1, -1][d % 3]
def chi_m7(d): return [0, 1, 1, -1, 1, -1, -1][d % 7]  # Legendre mod 7, odd

def eis_pair(f, g, k, n=N):
    out = [F_(0)]*(n+1)
    for m in range(1, n+1):
        s = 0
        for d in range(1, m+1):
            if m % d == 0:
                s += f(m//d)*g(d)*d**(k-1)
        out[m] = F_(s)
    return out

def build_basis(pairs, k, divs, cusp=None):
    basis = [[F_(1)] + [F_(0)]*N]; names = ['1']
    for (fn, f, gn, g) in pairs:
        base = eis_pair(f, g, k)
        for d in divs:
            basis.append(qd(base, d))
            names.append('E%d[%s,%s](q^%d)' % (k, fn, gn, d))
    if cusp:
        for cn, (exps, lv) in cusp.items():
            fser = eta_pow(exps)
            if fser is None: continue
            for d in divs:
                basis.append(qd(fser, d)); names.append('%s(q^%d)' % (cn, d))
    return basis, names

JOBS = {
 'D':    dict(k=3, divs=[1,5],
              pairs=[('1',one,'p1',psi1), ('1',one,'p2',psi2),
                     ('p1',psi1,'1',one), ('p2',psi2,'1',one),
                     ('p1',psi1,'p1',psi1), ('p1',psi1,'p2',psi2),
                     ('p2',psi2,'p1',psi1), ('p2',psi2,'p2',psi2)]),
 'zeta': dict(k=4, divs=[1,3,9],
              pairs=[('1',one,'1',one), ('x3',chi_m3,'x3',chi_m3),
                     ('1',one,'x3',chi_m3), ('x3',chi_m3,'1',one)],
              cusp={'f9.4': ({3: 8}, 9)}),
 's7':   dict(k=3, divs=[1,7],
              pairs=[('1',one,'x7',chi_m7), ('x7',chi_m7,'1',one),
                     ('x7',chi_m7,'x7',chi_m7)]),
 's10':  dict(k=3, divs=[1,2,5,10],
              pairs=[('1',one,'p1',psi1), ('1',one,'p2',psi2),
                     ('p1',psi1,'1',one), ('p2',psi2,'1',one),
                     ('p1',psi1,'p2',psi2), ('p2',psi2,'p1',psi1)]),
 's18':  dict(k=3, divs=[1,2,3,6,9,18],
              pairs=[('1',one,'x3',chi_m3), ('x3',chi_m3,'1',one)]),
}

if __name__ == '__main__':
    out = {}
    for (name, tp, a, b, c, d, level, chi, lim) in FAMS:
        if name not in JOBS: continue
        job = JOBS[name]
        tq, Fq, Phi = phi_series(name, tp, a, b, c, d)
        mu = detect_rescale(tq)
        Ph = rescale(Phi, mu, shift=1)
        basis, names = build_basis(job['pairs'], job['k'], job['divs'],
                                   job.get('cusp'))
        x = fit_series(Ph, basis)
        if x is not None:
            nz = [(names[i], str(x[i])) for i in range(len(x)) if x[i]]
            print('%-5s: FIT wt %d:' % (name, job['k']), nz, flush=True)
            out[name] = nz
        else:
            print('%-5s: no fit (%d vectors, %d rows)'
                  % (name, len(basis), N+1), flush=True)
            out[name] = None
    with open(os.path.join(HERE, 'eps60b_results.json'), 'w') as fh:
        json.dump(out, fh, indent=1)
    print('saved')
