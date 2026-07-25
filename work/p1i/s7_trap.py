"""Phase 6: the TRAP.  The letter-wise ("mismatch pole compensated by carries") route
sketched in PHASE2_INDUCTION Sec.6.2 does NOT close cell-wise at weight 5.

For a cell with e1 = 1 and lambda := v_p(a+b+1) >= 1, the descent mismatch of the
single letter A_m(k) is  e1*(a+b+1)^{-m},  of valuation -m*lambda, while the Kummer
gain of the whole T is only  v_pC(n+k,n) - v_pC(a+b,a) = 1 + lambda.
At m = 5 the naive term  c_{A5(k)} * (a+b+1)^{-5}  therefore beats the gain by 4(1+lambda)-1.

We exhibit cells where the naive letter-wise bound is NEGATIVE while the true
v_p(T*E) is >= the target -- i.e. the pole is not in v5 at all: it is killed by the
(DEPTH) conditions at LEVEL n, which is exactly what the proof of P1i uses instead.
"""
import sys, json
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1i')
from pad import Ctx, Level, load_w5
from kummer import car, logp, vT, vp

W5 = '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/w5_allp.json'
d = json.load(open(W5))
print('coefficient of the pure A5(k) monomial [1|A5]x1x1 :', d.get('[1|A5]x1x1'))
print('coefficient of [A5|1]-type / other weight-5 single letters present:',
      {k: v for k, v in d.items() if k.count('*') == 0 and 'x1x1' in k})
TERMS = load_w5(W5)

print()
print('cells with e1=1 and p | a+b+1  (so the A_5(k) mismatch has valuation -5*lambda):')
print(' p   n   k   l  |  a  b  lam | vT_n | naive letterwise bound  | true v_p(T*E) | target')
for (p, n, k, l) in [(5, 19, 6, 0), (5, 19, 6, 6), (5, 19, 6, 19), (5, 24, 6, 3),
                     (7, 34, 20, 5), (7, 41, 27, 7), (11, 76, 43, 10),
                     (5, 99, 26, 30), (5, 124, 31, 40), (7, 244, 100, 50)]:
    if k > n or l > n: continue
    L = logp(n, p); a, r = divmod(n, p); b, s = divmod(k, p); c, t = divmod(l, p)
    if not (r + s >= p): continue
    lam = vp(a + b + 1, p)
    if lam < 1: continue
    v = vT(n, k, l, p)
    tgt = -5 * (L - 1)
    naive = v - 5 * lam                       # T * (coeff * (a+b+1)^{-5})
    ctx = Ctx(p, 48)
    lev_n = Level(ctx, n, TERMS); lev_a = Level(ctx, a, TERMS)
    x = lev_n.v5(k, l); x = (x[0] + 5, x[1], x[2])
    E = ctx.sub(x, lev_a.v5(b, c))
    print('%2d %4d %3d %3d  | %2d %2d %3d | %4d | %20d  | %13d | %6d %s'
          % (p, n, k, l, a, b, lam, v, naive, v + E[0], tgt,
             'NAIVE FAILS' if naive < tgt else ''))
