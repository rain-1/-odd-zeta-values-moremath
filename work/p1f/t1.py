"""T1: sanity + the (V2)/(V3) test at L = 0 (the (BASE) level)."""
import sys
from fractions import Fraction as F
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1f')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1d')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from kgrade import v5_upoly, pattern
from w5eval import v5, Tl
from core import vp

PR = [int(x) for x in (sys.argv[1:] or ['5', '7', '11', '13'])]
for p in PR:
    bad_rec = 0
    bad_int = 0
    bad_cap = 0
    ncell = 0
    for a in range(1, p):
        S = [F(0)] * 6
        for b in range(a + 1):
            for c in range(a + 1):
                ncell += 1
                K, L, M = v5_upoly(a, b, c, p)
                assert L == 0 and M == 1
                # (a) reconstruction
                val = sum(K[j] * F(1, p) ** j for j in range(6))
                if val != v5(a, b, c):
                    bad_rec += 1
                # (b) integrality of each K_j
                for j in range(6):
                    if K[j] and vp(K[j], p) < 0:
                        bad_int += 1
                # (c) the depth cap
                al, ga, ka, th = pattern(a, b, c, p, 1)
                s = al + ga + ka
                J = 0 if s == 0 else 1 + min(s, 2)
                for j in range(J + 1, 6):
                    if K[j]:
                        bad_cap += 1
                        print('  CAP VIOL p=%d a=%d b=%d c=%d j=%d J=%d' % (p, a, b, c, j, J))
                Tv = Tl(a, b, c)
                for j in range(6):
                    S[j] += Tv * K[j]
        vs = [vp(S[j], p) if S[j] else None for j in range(6)]
        # target:  v_p(S_j) >= j
        tgt = [('OK' if (S[j] == 0 or vp(S[j], p) >= j) else 'FAIL') for j in range(6)]
        print('p=%2d a=%2d  v_p(S_j)=%s   need j  -> %s' % (p, a, vs, tgt))
    print('p=%2d cells=%d  rec-bad=%d  nonintegral-K=%d  cap-viol=%d' %
          (p, ncell, bad_rec, bad_int, bad_cap), flush=True)
