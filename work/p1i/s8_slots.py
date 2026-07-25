"""Phase 7: the SLOT-WISE inequalities behind (DK2), checked one binomial at a time.

  V1 = v_pC(n+k,n) >= alpha + e1        V2 = v_pC(n+l,n) >= gamma + e2
  V3 = v_pC(n,k)   >= [s>r]             V4 = v_pC(n,l)   >= [t>r]
  V5 = v_pC(n+k+l,n) >= kappa + (e3-e4)

(the two carries in each addition sit in base-p positions 0 and L, distinct because L>=1).
Also checks the exact carry identities quoted in PHASE2_GAPDESC Sec.5 as a bonus:
  V1 = v_pC(a+b,a) + e1*(1+v_p(a+b+1)),   V3 = v_pC(a,b) + [s>r]*(1+v_p(a-b)).
"""
import sys, collections
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1i')
from kummer import car, logp, vp

cnt = collections.Counter()
JOBS = []
for p in (5, 7, 11, 13):
    JOBS += [(p, n) for n in range(p, min(p * p + 60, 200))]
JOBS += [(5, n) for n in (125, 130, 200, 300, 624, 625, 700)]
JOBS += [(7, n) for n in (343, 350, 400)]
JOBS += [(11, n) for n in (121, 200, 1331)]
JOBS += [(17, n) for n in (289, 300)]
JOBS += [(31, n) for n in (961, 1000)]

for p, n in JOBS:
    L = logp(n, p)
    if L < 1: continue
    a, r = divmod(n, p)
    Pn = p ** (L + 1); Pa = p ** L
    for k in range(n + 1):
        b, s = divmod(k, p)
        e1 = 1 if r + s >= p else 0
        sgr = 1 if s > r else 0
        V1 = car(n, k, p); V3 = car(k, n - k, p)
        al = 1 if n + k >= Pn else 0
        if V1 < al + e1: cnt['V1_FAIL'] += 1
        if V3 < sgr: cnt['V3_FAIL'] += 1
        if V1 != car(a, b, p) + e1 * (1 + vp(a + b + 1, p)): cnt['V1_IDENT_FAIL'] += 1
        if V3 != car(b, a - b, p) + sgr * (1 + (vp(a - b, p) if a != b else 0)):
            if not (sgr and a == b):        # b = a, s > r  =>  k > n, cell excluded
                cnt['V3_IDENT_FAIL'] += 1
        for l in range(n + 1):
            c, t = divmod(l, p)
            e2 = 1 if r + t >= p else 0
            e3 = (r + s + t) // p
            e4 = 1 if s + t >= p else 0
            eps = (k + l) // Pn
            kap = 1 if n + k + l >= (eps + 1) * Pn else 0
            V5 = car(n, k + l, p)
            if V5 < kap + (e3 - e4): cnt['V5_FAIL'] += 1
            cnt['cells'] += 1
print('cells =', cnt['cells'])
for key in ('V1_FAIL', 'V3_FAIL', 'V5_FAIL', 'V1_IDENT_FAIL', 'V3_IDENT_FAIL'):
    print('   %-16s %d   <-- must be 0' % (key, cnt.get(key, 0)))
