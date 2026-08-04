"""eps51_refine.py -- refined identification + ASD relations.

Fixes over eps51_dictionary: (i) eta classification requires a VERIFIED zero
tail (support <= 20, all exponents 20<m<=25 zero); (ii) generalized-eta
(periodic c_j) detection with verified repeats; (iii) refined ASD relations
for the weight-1 (R2) families: test A(p) =? b_p + e*chi(p), b_p*chi(p),
b_p + chi(p)*p-adjusted forms mod p.
"""
import sys
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import eps48_modular_nome as M
import eps51_dictionary as D

N = 26

def classify2(c):
    """c: dict j->Fraction exponents valid for j <= 25 (lead-1 series)."""
    upto = 25
    vals = [c[j] for j in range(1, upto + 1)]
    if any(v.denominator != 1 for v in vals):
        return ('nonintegral', None)
    iv = [int(v) for v in vals]
    # eta with verified tail
    for L in range(1, 21):
        e = {}
        ok = True
        for m in range(1, upto + 1):
            s = sum(e.get(d, 0) for d in range(1, m) if m % d == 0)
            e[m] = iv[m - 1] - s
            if m > L and e[m] != 0:
                ok = False
                break
        if ok:
            return ('eta', {m: v for m, v in e.items() if v})
    for L in range(1, 21):
        if upto - L >= 6 and all(iv[j] == iv[j + L] for j in range(upto - L)):
            return ('genEta mod %d' % L, iv[:L])
    return ('aperiodic', iv[:12])

def chiget(name):
    return {'x-3': D.chi_m3, 'x-4': D.chi_m4, 'x5': D.chi_5}.get(name)

if __name__ == '__main__':
    PR = [5, 7, 11, 13, 17, 19, 23]
    table = []
    for fam in D.FAMS:
        name, typ, par, w, chi, lim, sanity = fam
        A, Pj = D.build(fam)
        tq, Fq = M.nome(name, w, Pj, A)
        ct = D.product_exponents(tq, lead=1)
        cF = D.product_exponents(Fq, lead=0)
        clt = classify2(ct)
        clF = classify2({j: cF[j] for j in cF})
        # ASD relations
        cf = chiget(chi)
        rels = {}
        for p in PR:
            Ap = int(A[p]) % p
            bp = int(Fq[p]) % p
            cands = {
                'A=b': (Ap - bp) % p == 0,
            }
            if cf:
                x = cf(p)
                cands['A=b+chi'] = (Ap - bp - x) % p == 0
                cands['A=b-chi'] = (Ap - bp + x) % p == 0
                cands['A=chi*b'] = (Ap - x * bp) % p == 0
                cands['A=b+chi*p^0*2'] = (Ap - bp - 2 * x) % p == 0
            else:
                cands['A=b+1'] = (Ap - bp - 1) % p == 0
                cands['A=b-1'] = (Ap - bp + 1) % p == 0
                cands['A=b+2'] = (Ap - bp - 2) % p == 0
            rels[p] = [k for k, v in cands.items() if v]
        # uniform relation across primes?
        common = None
        sets = [set(rels[p]) for p in PR]
        inter = set.intersection(*sets) if sets else set()
        table.append((name, w, chi, lim, clt, clF, sorted(inter),
                      {p: rels[p] for p in PR}))
        print('%-6s w%d chi=%-4s t:%s' % (name, w, chi, clt))
        print('        F:%s' % (clF,))
        print('        ASD uniform relations:', sorted(inter) or 'NONE',
              '  per-prime:', {p: rels[p] for p in (5, 7, 11)}, flush=True)

    import pickle
    with open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/'
              'eps51_refined.pkl', 'wb') as fh:
        pickle.dump(table, fh)
