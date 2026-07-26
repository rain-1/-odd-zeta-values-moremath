"""INSTRUMENT VALIDATION before any verdict is trusted.

(1) each decomposition reproduces B(n) exactly on held-out n  (exact Fractions);
(2) the scaled p-adic tables agree with exact Fractions;
(3) the p-adic evaluator of  p^w * w(n,k)  agrees with the exact Fraction evaluator
    in VALUATION, cell by cell, for p = 5 and p = 7 (all cells n = ap+r < p^2).
"""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lbw'))

from sporadic import SEQS, gen_A, gen_B                    # noqa: E402
from decs import FAMS, ORDER, ARG, chi_of                  # noqa: E402
import pad                                                 # noqa: E402
from pad import Tables, vp_int, vp_fr, verify_tables, INF  # noqa: E402

PAR = {l: (f, p) for l, f, p, _, _ in SEQS}

# ------------------------------------------------------------------ exact evaluator
_HT = {}


def Hex(r, y):
    t = _HT.setdefault(('H', r), [F(0)])
    while len(t) <= y:
        t.append(t[-1] + F(1, len(t) ** r))
    return t[y]


def Kex(r, y):
    t = _HT.setdefault(('K', r), [F(0)])
    while len(t) <= y:
        m = len(t)
        c = 0 if m % 2 == 0 else (1 if m % 4 == 1 else -1)
        t.append(t[-1] + F(c, m ** r))
    return t[y]


def wexact(fam, n, k):
    tot = F(0)
    for c, mo in fam.W:
        v = c
        for kind, r, a in mo:
            y = ARG[a](n, k)
            if y < 0:
                v = F(0)
                break
            v *= Hex(r, y) if kind == 'H' else Kex(r, y)
        tot += v
    return tot


# ------------------------------------------------------------------ (1)
def check_decompositions(NS=range(40, 50)):
    print('--- (1) decompositions reproduce B(n) exactly')
    ok = True
    for lab in ORDER:
        fam = FAMS[lab]
        f, par = PAR[fam.seqlabel]
        B = gen_B(f, par, max(NS) + 3)
        bad = []
        for n in NS:
            tot = F(0)
            for k in fam.ks(n):
                s = fam.S(n, k)
                if s:
                    tot += s * wexact(fam, n, k)
            if tot != B[n]:
                bad.append(n)
        print('    %-6s n=%d..%d : %s' % (lab, min(NS), max(NS),
                                          'ALL EXACT' if not bad else 'FAIL %s' % bad))
        ok &= not bad
    return ok


# ------------------------------------------------------------------ (2),(3)
def check_padic(p, T=30):
    fams = [FAMS[l] for l in ORDER]
    Y = 2 * (p * p - 1)
    tab = Tables(p, T, Y, rmax=3, want_K=True)
    bad = verify_tables(tab, p, list(range(0, Y + 1, max(1, Y // 40))) + [Y], 3, True)
    print('    tables p=%d: %s' % (p, 'OK' if not bad else 'MISMATCH %s' % bad[:4]))
    allok = not bad
    for fam in fams:
        SCW = 2 * fam.w
        SCC = max(0, max(vp_int(c.denominator, p) for c, _ in fam.W))
        M = p ** T
        cs = [(int((c * F(p) ** SCC).numerator)
               * pow(int((c * F(p) ** SCC).denominator) % M, -1, M)) % M for c, _ in fam.W]
        nbad = 0
        ncmp = 0
        for a in range(1, p):
            for r in range(p):
                n = a * p + r
                for k in fam.ks(n):
                    if fam.S(n, k) == 0:
                        continue
                    # p-adic
                    tot = 0
                    for j, (c, mo) in enumerate(fam.W):
                        v = cs[j]
                        for kind, rr, ag in mo:
                            y = ARG[ag](n, k)
                            v = v * tab.get(kind, rr, y) % M
                            if v == 0:
                                break
                        tot = (tot + v) % M
                    SC = SCW + SCC
                    vpad = vp_int(tot, p, cap=T) + fam.w - SC
                    # exact
                    ex = wexact(fam, n, k)
                    vex = INF if ex == 0 else vp_fr(ex, p) + fam.w
                    ncmp += 1
                    if vex >= T + fam.w - SC:
                        continue                     # both beyond precision: fine
                    if vpad != vex:
                        nbad += 1
                        if nbad < 4:
                            print('      MISMATCH %s p=%d n=%d k=%d padic=%d exact=%d'
                                  % (fam.label, p, n, k, vpad, vex))
        print('    %-6s p=%d: %d cells compared, %d valuation mismatches' %
              (fam.label, p, ncmp, nbad))
        allok &= (nbad == 0)
    return allok


if __name__ == '__main__':
    ok1 = check_decompositions()
    print('--- (2)(3) p-adic evaluator vs exact Fractions')
    ok2 = all(check_padic(p) for p in (5, 7))
    print('\nINSTRUMENT %s' % ('VALIDATED' if (ok1 and ok2) else 'FAILED'))
