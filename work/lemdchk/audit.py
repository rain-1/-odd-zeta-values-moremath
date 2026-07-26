"""T2/T3: the vanishing-layer valuation audit for alpha, eps, s7, E.

For every prime p, every cell n = ap+r < p^2 (1<=a<p, 0<=r<p) and every summation index
k with S(n,k) != 0 we compute, EXACTLY:

    vS  = v_p(S(n,k))                      (Legendre/Kummer, exact integers)
    vW  = v_p(p^w * w(n,k))                (fixed-precision p-adic, validated in selfcheck)

and report, on the VANISHING layer {p | S(n,k)}:

    T   termwise :  min over the layer of vS + vW          (SPORADIC_BARE's claim: >= 1)
    A   aggregate:  min over cells of v_p( sum_{p|S} S p^w w )   (weaker claim: >= 1)
    U   surviving:  min over cells of v_p( sum_{p!|S} S p^w w  -  chi(p)^e B(a) A(r) )
    X   total    :  min over cells of v_p( p^w B(n) - chi(p)^e B(a) A(r) )   (must be >= 1)
"""
import os
import sys
import time
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lbw'))

from sporadic import SEQS, gen_A, gen_B                       # noqa: E402
from decs import FAMS, ORDER, ARG                             # noqa: E402
from pad import Tables, vp_int, vp_fr, vp_binom, INF          # noqa: E402

PAR = {l: (f, p) for l, f, p, _, _ in SEQS}
T = 30


def chi_p(D, p):
    if D == 1:
        return 1
    if D == -4:
        return 1 if p % 4 == 1 else -1
    raise ValueError(D)


def run(lab, p, verbose=True):
    fam = FAMS[lab]
    w = fam.w
    M = p ** T
    Y = 2 * (p * p - 1)
    tab = Tables(p, T, Y, rmax=3, want_K=fam.wantK)

    SCW = 2 * w
    SCC = max(0, max(vp_int(c.denominator, p) for c, _ in fam.W))
    SC = SCW + SCC
    cs = []
    for c, _ in fam.W:
        cc = c * F(p) ** SCC
        assert cc.denominator % p != 0
        cs.append((cc.numerator % M) * pow(cc.denominator % M, -1, M) % M)

    f, par = PAR[fam.seqlabel]
    Aseq = gen_A(f, par, p + 2)
    Bsm = gen_B(f, par, p + 2)
    Bbig = gen_B(f, par, p * p + 2)
    chi = chi_p(fam.D, p) ** fam.e

    res = dict(term_min=INF, term_arg=None, term_viol=0, term_cells=0, nvan=0, nsurv=0,
               agg_min=INF, agg_arg=None, agg_viol=0,
               surv_min=INF, surv_viol=0, tot_min=INF, tot_viol=0,
               vW_min=INF, vW_arg=None, ncells=0)

    for a in range(1, p):
        for r in range(p):
            n = a * p + r
            Vacc = 0
            Uacc = 0
            cellmin = INF
            res['ncells'] += 1
            for k in fam.ks(n):
                bins = fam.BIN(n, k)
                if any(b < 0 or t < b for t, b in bins):
                    continue
                vS = sum(vp_binom(t, b, p) for t, b in bins)
                # scaled p-adic value of w(n,k)
                tot = 0
                for j, (_, mo) in enumerate(fam.W):
                    v = cs[j]
                    for kind, rr, ag in mo:
                        y = ARG[ag](n, k)
                        if y < 0:
                            v = 0
                            break
                        v = v * tab.get(kind, rr, y) % M
                        if v == 0:
                            break
                    tot = (tot + v) % M
                if vS == 0:
                    res['nsurv'] += 1
                    Uacc = (Uacc + fam.S(n, k) % M * tot) % M
                else:
                    res['nvan'] += 1
                    Vacc = (Vacc + fam.S(n, k) % M * tot) % M
                    vW = vp_int(tot, p, cap=T) + w - SC
                    tt = vS + vW
                    if tt < cellmin:
                        cellmin = tt
                    if tt < res['term_min']:
                        res['term_min'] = tt
                        res['term_arg'] = (n, a, r, k, k // p, k % p, vS, vW)
                    if vW < res['vW_min']:
                        res['vW_min'] = vW
                        res['vW_arg'] = (n, a, r, k, vS, vW)
                    if tt < 1:
                        res['term_viol'] += 1
            if cellmin < 1:
                res['term_cells'] += 1
            vV = vp_int(Vacc, p, cap=T) + w - SC
            if vV < res['agg_min']:
                res['agg_min'] = vV
                res['agg_arg'] = (n, a, r)
            if vV < 1:
                res['agg_viol'] += 1
            # surviving layer defect
            tgt = chi * Bsm[a] * Aseq[r]
            tgts = (tgt.numerator % M) * pow(tgt.denominator % M, -1, M) % M
            du = (Uacc - tgts * pow(p, SC - w, M)) % M
            vU = vp_int(du, p, cap=T) + w - SC
            if vU < res['surv_min']:
                res['surv_min'] = vU
            if vU < 1:
                res['surv_viol'] += 1
            # exact end-to-end control
            vX = vp_fr(F(p) ** w * Bbig[n] - tgt, p)
            if vX < res['tot_min']:
                res['tot_min'] = vX
            if vX < 1:
                res['tot_viol'] += 1
    return res


def fmt(v):
    return 'inf' if v >= INF else str(v)


if __name__ == '__main__':
    labs = sys.argv[1].split(',') if len(sys.argv) > 1 else ORDER
    primes = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 \
        else [5, 7, 11, 13, 17, 19, 23]
    print('%-6s %-4s | %-28s | %-22s | %-16s | %s' %
          ('fam', 'p', 'TERMWISE on vanishing layer', 'AGGREGATED layer', 'surviving',
           'total'))
    print('-' * 132)
    for lab in labs:
        for p in primes:
            t0 = time.time()
            R = run(lab, p)
            print('%-6s %-4d | min=%-4s viol=%-6d cells=%-4d | min=%-4s viol=%-4d | '
                  'min=%-4s viol=%-4d | min=%-3s viol=%d   [%d van, %d surv, %.0fs]'
                  % (lab, p, fmt(R['term_min']), R['term_viol'], R['term_cells'],
                     fmt(R['agg_min']), R['agg_viol'], fmt(R['surv_min']), R['surv_viol'],
                     fmt(R['tot_min']), R['tot_viol'], R['nvan'], R['nsurv'],
                     time.time() - t0), flush=True)
            if R['term_arg']:
                n, a, r, k, b, s, vS, vW = R['term_arg']
                print('        worst termwise cell: n=%d=%d*%d+%d, k=%d=%d*%d+%d, '
                      'v_p(S)=%d, v_p(p^w w)=%d, sum=%d   [2k=%d, 2k/p^2=%.2f]'
                      % (n, a, p, r, k, b, p, s, vS, vW, vS + vW, 2 * k, 2 * k / p ** 2),
                      flush=True)
            if R['agg_arg'] and R['agg_min'] < 1:
                print('        worst aggregate cell: n=%d=%d*%d+%d  v_p(V)=%s'
                      % (R['agg_arg'][0], R['agg_arg'][1], p, R['agg_arg'][2],
                         fmt(R['agg_min'])), flush=True)
        print('-' * 132, flush=True)
