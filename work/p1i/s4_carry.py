"""Phase 3: the two purely combinatorial lemmas that carry (GAP-DESC).

For an OFF-REGIME cell (s>r or t>r or e1+e2+e3+e4>0) at level n, with
   B := e1 + e2 + 2[s>r] + 2[t>r] + (e3-e4)        ("bottom carries")
we verify, exhaustively:

 (B0)  0 <= e3-e4 <= 1                       (always)
 (B1)  B >= 1                                (off-regime)
 (B2)  e4 = 1  ==>  B >= 2
 (K1)  vT_n >= s_n + B
 (K2)  s_n >= s_a - [e4=1 and b+c = p^L - 1]     (hence s_n + B >= s_a + 1)
 (KC)  vT_n >= max(J(pi_n), J(pi_a))         (the criterion (GAP-DESC) consumes)

and, as a control, that (KC) FAILS somewhere in-regime (so off-regime is essential).
"""
import sys, collections
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1i')
from kummer import car, logp, Jcap


def scan_n(p, n, cnt):
    L = logp(n, p)
    if L < 1: return
    a, r = divmod(n, p)
    Pn = p ** (L + 1); Pa = p ** L
    cn = [car(n, k, p) for k in range(n + 1)]
    dk = [car(k, n - k, p) for k in range(n + 1)]
    cj = [car(n, j, p) for j in range(2 * n + 1)]
    alph = [1 if n + k >= Pn else 0 for k in range(n + 1)]
    al_a = [1 if a + b >= Pa else 0 for b in range(a + 1)]
    for k in range(n + 1):
        b, s = divmod(k, p)
        e1 = 1 if r + s >= p else 0
        sgr = 1 if s > r else 0
        for l in range(n + 1):
            c, t = divmod(l, p)
            e2 = 1 if r + t >= p else 0
            e3 = (r + s + t) // p
            e4 = 1 if s + t >= p else 0
            tgr = 1 if t > r else 0
            off = sgr or tgr or e1 or e2 or e3 or e4
            zeta = e3 - e4
            if not (0 <= zeta <= 1): cnt['B0_FAIL'] += 1
            eps = (k + l) // Pn
            kap = 1 if n + k + l >= (eps + 1) * Pn else 0
            sn = alph[k] + alph[l] + kap
            epsa = (b + c) // Pa
            kapa = 1 if a + b + c >= (epsa + 1) * Pa else 0
            sa = al_a[b] + al_a[c] + kapa
            v = cn[k] + 2 * dk[k] + cn[l] + 2 * dk[l] + cj[k + l]
            need = max(Jcap(sn), Jcap(sa))
            B = e1 + e2 + 2 * sgr + 2 * tgr + zeta
            if not off:
                cnt['in'] += 1
                if v < need: cnt['in_KC_fails'] += 1
                if B != 0: cnt['in_B_nonzero'] += 1
                if sn != sa: cnt['in_sn_ne_sa'] += 1
                continue
            cnt['off'] += 1
            if B < 1: cnt['B1_FAIL'] += 1
            if e4 and B < 2: cnt['B2_FAIL'] += 1
            if v < sn + B: cnt['K1_FAIL'] += 1
            excep = 1 if (e4 and b + c == Pa - 1) else 0
            if sn < sa - excep: cnt['K2_FAIL'] += 1
            if excep and sn >= sa: cnt['K2_excep_harmless'] += 1
            if sn + B < sa + 1: cnt['K2b_FAIL'] += 1
            if v < need: cnt['KC_FAIL'] += 1
            cnt['slack_%d' % min(v - need, 5)] += 1


JOBS = []
for p in (5, 7, 11, 13):
    JOBS += [(p, n) for n in range(p, min(p * p, 200))]
JOBS += [(5, n) for n in range(25, 130)]
JOBS += [(7, n) for n in range(49, 360, 2)]
JOBS += [(11, n) for n in range(121, 400, 3)]
JOBS += [(13, n) for n in range(169, 400, 3)]
for p in (17, 19, 23, 29, 31):
    JOBS += [(p, n) for n in range(p * p, min(p ** 3, p * p + 200), 7)]
JOBS += [(5, n) for n in (125, 126, 130, 200, 300, 400, 500, 624, 625, 626, 700, 1000)]
JOBS += [(7, n) for n in (343, 344, 400, 700, 1000, 2400, 2401, 2402)]
JOBS += [(11, n) for n in (1331, 1332, 1500, 2000)]
JOBS += [(13, n) for n in (2197, 2198, 2500)]

if __name__ == '__main__':
    cnt = collections.Counter()
    for p, n in JOBS:
        scan_n(p, n, cnt)
    print('jobs = %d' % len(JOBS))
    print('   in-regime cells   = %d' % cnt['in'])
    print('   off-regime cells  = %d' % cnt['off'])
    for key in ('B0_FAIL', 'B1_FAIL', 'B2_FAIL', 'K1_FAIL', 'K2_FAIL', 'K2b_FAIL',
                'KC_FAIL'):
        print('   %-22s %d   <-- must be 0' % (key, cnt.get(key, 0)))
    for key in ('in_KC_fails', 'in_B_nonzero', 'in_sn_ne_sa', 'K2_excep_harmless'):
        print('   %-22s %d' % (key, cnt.get(key, 0)))
    print('   off-regime slack of (KC), 5 = >=5:',
          {i: cnt.get('slack_%d' % i, 0) for i in range(6)})
