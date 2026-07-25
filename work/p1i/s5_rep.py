"""Phase 4: representative-independence.

(a) (DEPTH-gen) in the refined form  d5(n,k,l) <= 5L + 1 + min(s,2)  and the
    trivial-pattern form  d5 <= 5L  when s = 0,   for a GIVEN representative;
(b) the (GAP-DESC) cell inequality  v_p(T*E) >= -5(L-1)  for that representative.

Run:  python3 s5_rep.py <w5.json>
"""
import sys, collections
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1i')
from pad import Ctx, Level, load_w5
from kummer import car, logp

REP = sys.argv[1] if len(sys.argv) > 1 else \
    '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g/w5_exIII_allp.json'
TERMS = load_w5(REP)
print('representative:', REP, '(%d terms)' % len(TERMS))

# ---- (a) depth ------------------------------------------------------------
badA = badA0 = cells = 0
minslack = 99
for p, ns in ((5, list(range(1, 31))), (7, list(range(1, 30))),
              (11, list(range(1, 26))), (13, list(range(1, 20)))):
    ctx = Ctx(p, 40)
    for n in ns:
        L = logp(n, p); Pn = p ** (L + 1)
        lev = Level(ctx, n, TERMS)
        for k in range(n + 1):
            for l in range(k, n + 1):
                x = lev.v5(k, l)
                d5 = max(0, -x[0]) if x[1] else 0
                al = 1 if n + k >= Pn else 0
                ga = 1 if n + l >= Pn else 0
                eps = (k + l) // Pn
                ka = 1 if n + k + l >= (eps + 1) * Pn else 0
                s = al + ga + ka
                cap = 5 * L + 1 + min(s, 2)
                cells += 1
                if d5 > cap:
                    badA += 1
                    if badA < 4: print('  DEPTH violation p=%d n=%d k=%d l=%d d5=%d cap=%d'
                                       % (p, n, k, l, d5, cap))
                if s == 0 and d5 > 5 * L:
                    badA0 += 1
                    if badA0 < 4: print('  trivial-pattern violation p=%d n=%d k=%d l=%d d5=%d 5L=%d'
                                        % (p, n, k, l, d5, 5 * L))
                minslack = min(minslack, cap - d5)
print('(a) (DEPTH-gen): cells=%d violations=%d  trivial-pattern(J=0) violations=%d  min slack=%d'
      % (cells, badA, badA0, minslack))

# ---- (b) the descent inequality ------------------------------------------
import s3_exact
s3_exact.TERMS = TERMS
tot = totf = 0; gmin = 99
for p, n in [(5, 13), (5, 21), (5, 25), (5, 26), (5, 31), (5, 49),
             (7, 15), (7, 30), (7, 49), (7, 50), (7, 55),
             (11, 23), (11, 60), (11, 121), (11, 122),
             (13, 27), (13, 100), (13, 169)]:
    c, f, ms, h = s3_exact.run(p, n)
    tot += c; totf += f; gmin = min(gmin, ms)
print('(b) (GAP-DESC) off-regime cells=%d failures=%d min slack=%d' % (tot, totf, gmin))
