"""Full verification of a saved w5 representative.

  (V1) exact-Q ladder check      P_n = sum_{k,l} T(n,k,l) w5(n,k,l),  n = 1..NMAX
  (V2) depth sweep               d5(a,b,c) <= 1 + min(v_p T(a,b,c), 2),  all cells, p in PRIMES
  (V3) (GAP-5) cell-by-cell      v_p(Tcal(b,c) - (Q_n/Q_a) T(a,b,c)) >= 1 + d5(b,c)

Usage: python3 verify_depth.py FILE.json [V1max] [primes...]
"""
import json, sys
from fractions import Fraction as F
from math import comb
from core import P, Q, Hs, vp

FN = sys.argv[1]
V1MAX = int(sys.argv[2]) if len(sys.argv) > 2 else 30
PRIMES = [int(x) for x in sys.argv[3:]] or [5, 7, 11, 13, 17, 19]

d = json.load(open(FN))
terms = []
for lab, (num, den) in d.items():
    fg, rest = lab.split(']x'); f, g = fg[1:].split('|'); h, s = rest.split('x')
    sp = lambda x: [] if x == '1' else x.split('*')
    terms.append((F(num, den), sp(f), sp(g), sp(h), sp(s)))
print('%s: %d terms' % (FN, len(terms)), flush=True)


def w5(n, k, l):
    def L(nm, i):
        t, r = nm[0], int(nm[1])
        return (Hs(n + i, r) - Hs(i, r)) if t == 'A' else (Hs(n - i, r) - Hs(i, r))
    tot = F(0)
    for cf, f, g, h, s in terms:
        v = cf
        for nm in h:
            v *= Hs(n + k + l, int(nm[1])) - Hs(k + l, int(nm[1]))
        for nm in s:
            v *= Hs(n, int(nm[1]))
        pf = F(1)
        for nm in f: pf *= L(nm, k)
        for nm in g: pf *= L(nm, l)
        pb = F(1)
        for nm in f: pb *= L(nm, l)
        for nm in g: pb *= L(nm, k)
        tot += v * (pf if f == g else pf + pb)
    return tot


def Tl(a, b, c):
    return comb(a + b, a) * comb(a, b)**2 * comb(a + c, a) * comb(a, c)**2 * comb(a + b + c, a)


# -------------------------------------------------------------------- (V1)
print('--- (V1) exact ladder check ---', flush=True)
bad1 = 0
for n in range(1, V1MAX + 1):
    tot = F(0)
    for k in range(n + 1):
        tk = comb(n + k, n) * comb(n, k)**2
        for l in range(n + 1):
            T = tk * comb(n + l, n) * comb(n, l)**2 * comb(n + k + l, n)
            tot += T * w5(n, k, l)
    if tot != P(n):
        bad1 += 1
        print('  n=%d MISMATCH' % n, flush=True)
print('  (V1) n=1..%d : %d mismatches' % (V1MAX, bad1), flush=True)

# -------------------------------------------------------------------- (V2)
print('--- (V2) depth sweep  d5 <= 1+min(vT,2) ---', flush=True)
tot2 = 0
for p in PRIMES:
    bad = 0; mx = 0; slack = 99; ncell = 0
    for a in range(1, p):
        for b in range(a + 1):
            for c in range(a + 1):
                ncell += 1
                vT = vp(Tl(a, b, c), p)
                cap = 1 + min(vT, 2)
                W = w5(a, b, c) - Hs(a, 5)
                d5 = max(0, -vp(W, p)) if W else 0
                mx = max(mx, d5)
                slack = min(slack, cap - d5)
                if d5 > cap:
                    bad += 1
    tot2 += bad
    print('  p=%2d cells=%5d  max d5=%d  violations=%d  min slack=%d'
          % (p, ncell, mx, bad, slack), flush=True)
print('  (V2) total violations: %d' % tot2, flush=True)

# -------------------------------------------------------------------- (V3)
print('--- (V3) (GAP-5) cell-by-cell ---', flush=True)
from t2_lemFplus import fibre_table, Tlevel, vp_mod, CAP
tot3 = 0
for p in [q for q in PRIMES if q <= 13]:
    M = p**CAP
    ncell = 0; nbad = 0; worst = None
    for a in range(1, p):
        Qa = int(Q(a))
        if Qa % p == 0:
            continue
        Ta = {(b, c): Tlevel(a, b, c) for b in range(a + 1) for c in range(a + 1)}
        d5 = {}
        for b in range(a + 1):
            for c in range(a + 1):
                W = w5(a, b, c) - Hs(a, 5)
                d5[(b, c)] = max(0, -vp(W, p)) if W else 0
        for r in range(p):
            n = a * p + r
            if n > 360:
                continue
            tab = fibre_table(p, a, r, M)
            Qn = sum(tab.values()) % M
            Lam = Qn * pow(Qa % M, -1, M) % M
            for bc, val in tab.items():
                ncell += 1
                diff = (val - Lam * Ta[bc]) % M
                v = vp_mod(diff, p)
                if v < 1 + d5[bc]:
                    nbad += 1
                    sl = v - (1 + d5[bc])
                    if worst is None or sl < worst[0]:
                        worst = (sl, a, r, bc, d5[bc], v)
    tot3 += nbad
    print('  p=%2d cells=%5d  FAILING v_p(diff)>=1+d5: %d  worst=%s'
          % (p, ncell, nbad, worst), flush=True)
print('  (V3) total violations: %d' % tot3, flush=True)
print('VERDICT: V1=%d V2=%d V3=%d  ->  %s'
      % (bad1, tot2, tot3, 'ALL CLEAN' if bad1 + tot2 + tot3 == 0 else 'FAILURES'), flush=True)
