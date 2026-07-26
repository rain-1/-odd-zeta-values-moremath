"""T3b/T4: (H1), (H2) as literally stated, and the LOCAL form of the cancellation.

For n = ap+r, k = bp+s:
  H1   p | S(n,k)  or  S(n,k) == S(a,b) S(r,s)  (mod p)
  H2   surviving set = Bset x Sigma_r  (product region?)  with Bset = {0..a}?  and
       sum_{s in Sigma_r} S(r,s) == A(r) (mod p)
  LOC  for each digit b, with  V_b(n) := sum_{s : p | S(n,bp+s)} S(n,bp+s) p^w w(n,bp+s),
           V_b(n)  ==  chi(p)^e * S(a,b) w(a,b) * A(r)   (mod p)     if p | S(a,b)
           V_b(n)  ==  0                                  (mod p)     if p !| S(a,b)
       (the second line is the honest content of "the vanishing layer dies"; the first is
        the exact defect that the surviving layer is missing.)
"""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lbw'))

from sporadic import SEQS, gen_A, gen_B                       # noqa: E402
from decs import FAMS, ORDER, ARG                             # noqa: E402
from pad import Tables, vp_int, vp_binom, INF                 # noqa: E402

PAR = {l: (f, p) for l, f, p, _, _ in SEQS}
T = 30


def chi_p(D, p):
    return 1 if D == 1 else (1 if p % 4 == 1 else -1)


def run(lab, p):
    fam = FAMS[lab]
    w, M = fam.w, p ** T
    tab = Tables(p, T, 2 * (p * p - 1), rmax=3, want_K=fam.wantK)
    SCW, SCC = 2 * w, max(0, max(vp_int(c.denominator, p) for c, _ in fam.W))
    SC = SCW + SCC
    cs = []
    for c, _ in fam.W:
        cc = c * F(p) ** SCC
        cs.append((cc.numerator % M) * pow(cc.denominator % M, -1, M) % M)

    def wpad(n, k):
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
        return tot

    def vS(n, k):
        bins = fam.BIN(n, k)
        if any(bb < 0 or t < bb for t, bb in bins):
            return None
        return sum(vp_binom(t, bb, p) for t, bb in bins)

    f, par = PAR[fam.seqlabel]
    Aseq = gen_A(f, par, p + 2)
    chi = chi_p(fam.D, p) ** fam.e

    # base level
    Sab, wab, van_b = {}, {}, {}
    for a in range(1, p):
        for b in fam.ks(a):
            v = vS(a, b)
            if v is None:
                continue
            Sab[(a, b)] = fam.S(a, b) % M
            wab[(a, b)] = wpad(a, b)
            van_b.setdefault(a, set())
            if v > 0:
                van_b[a].add(b)
    surv_r = {}
    for r in range(p):
        surv_r[r] = set(b for b in fam.ks(r) if vS(r, b) == 0)

    h1bad = h2prod = h2full = h2sig = 0
    locbad_zero = locbad_def = 0
    nb_zero = nb_def = 0
    for a in range(1, p):
        for r in range(p):
            n = a * p + r
            surv = set()
            Vb = {}
            for k in fam.ks(n):
                v = vS(n, k)
                if v is None:
                    continue
                b, s = k // p, k % p
                if v == 0:
                    surv.add((b, s))
                    # (H1): S(n,k) == S(a,b) S(r,s) mod p
                    lhs = fam.S(n, k) % p
                    rhs = (fam.S(a, b) if (a, b) in Sab else 0) * \
                          (fam.S(r, s) if s in [x for x in fam.ks(r)] else 0) % p
                    if lhs != rhs % p:
                        h1bad += 1
                else:
                    Vb[b] = (Vb.get(b, 0) + fam.S(n, k) % M * wpad(n, k)) % M
            # (H2) product region?
            bs = set(b for b, _ in surv)
            ss = set(s for _, s in surv)
            if surv and surv != set((b, s) for b in bs for s in ss):
                h2prod += 1
            if bs and bs != set(b for b in fam.ks(a) if vS(a, b) == 0):
                h2full += 1
            if sum(fam.S(r, s) for s in ss) % p != Aseq[r].numerator % p * \
                    pow(Aseq[r].denominator % p, -1, p) % p:
                h2sig += 1
            # (LOC)
            Ar = Aseq[r]
            Ars = (Ar.numerator % M) * pow(Ar.denominator % M, -1, M) % M
            for b, val in Vb.items():
                lhs = val * pow(p, w, M) % M                # scale SC
                if (a, b) in Sab and b in van_b.get(a, set()):
                    pred = chi * Sab[(a, b)] % M * wab[(a, b)] % M * Ars % M
                    nb_def += 1
                    if vp_int((lhs - pred) % M, p, cap=T) - SC < 1:
                        locbad_def += 1
                else:
                    nb_zero += 1
                    if vp_int(lhs, p, cap=T) - SC < 1:
                        locbad_zero += 1
    return dict(h1bad=h1bad, h2prod=h2prod, h2full=h2full, h2sig=h2sig,
                locbad_zero=locbad_zero, nb_zero=nb_zero,
                locbad_def=locbad_def, nb_def=nb_def)


if __name__ == '__main__':
    labs = sys.argv[1].split(',') if len(sys.argv) > 1 else ORDER
    primes = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 \
        else [5, 7, 11, 13]
    for lab in labs:
        for p in primes:
            R = run(lab, p)
            print('%-6s p=%-3d | (H1) fails=%-4d | (H2) non-product cells=%-4d  '
                  'b-set != {0..a} cells=%-4d  Sigma_r sum fails=%-3d | '
                  'LOCAL: p!|S(a,b) digits %d/%d fail;  p|S(a,b) digits %d/%d fail'
                  % (lab, p, R['h1bad'], R['h2prod'], R['h2full'], R['h2sig'],
                     R['locbad_zero'], R['nb_zero'], R['locbad_def'], R['nb_def']),
                  flush=True)
        print('-' * 128, flush=True)
