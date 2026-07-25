"""Phase 1b: the CRUDE criterion  (off-regime  =>  vT_n >= max(J(pi_n), J(pi_a)))
scanned hard: many primes, three/four digit levels, full cell sets.

Reports failures, and the joint distribution (s_n, s_a, vT_n) of the tight cells.
"""
import sys, collections
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1i')
from kummer import car, logp, Jcap

def scan_n(p, n, collect=None):
    """all cells of level n; returns (n_off, n_fail, examples)"""
    L = logp(n, p)
    if L < 1: return 0, 0, []
    a, r = divmod(n, p)
    Pn = p ** (L + 1); Pa = p ** L
    # per-index precomputation
    cn = [car(n, k, p) for k in range(n + 1)]          # v_p C(n+k,n)
    dk = [car(k, n - k, p) for k in range(n + 1)]      # v_p C(n,k)
    cj = [car(n, j, p) for j in range(2 * n + 1)]      # v_p C(n+j,n), j=k+l
    ca = [car(a, b, p) for b in range(a + 1)]
    da = [car(b, a - b, p) for b in range(a + 1)]
    cja = [car(a, j, p) for j in range(2 * a + 1)]
    alph = [1 if n + k >= Pn else 0 for k in range(n + 1)]
    alpha_a = [1 if a + b >= Pa else 0 for b in range(a + 1)]
    nfail = 0; noff = 0; ex = []
    for k in range(n + 1):
        b, s = divmod(k, p)
        e1 = 1 if r + s >= p else 0
        sgr = 1 if s > r else 0
        for l in range(n + 1):
            c, t = divmod(l, p)
            e2 = 1 if r + t >= p else 0
            e3 = (r + s + t) // p
            e4 = 1 if s + t >= p else 0
            if not (sgr or t > r or e1 or e2 or e3 or e4):
                continue
            noff += 1
            # level-n pattern
            eps = (k + l) // Pn
            kap = 1 if n + k + l >= (eps + 1) * Pn else 0
            sn = alph[k] + alph[l] + kap
            # level-a pattern
            epsa = (b + c) // Pa
            kapa = 1 if a + b + c >= (epsa + 1) * Pa else 0
            sa = alpha_a[b] + alpha_a[c] + kapa
            need = max(Jcap(sn), Jcap(sa))
            if need == 0:
                continue
            v = cn[k] + 2 * dk[k] + cn[l] + 2 * dk[l] + cj[k + l]
            if collect is not None:
                collect[(sn, sa, min(v, 6))] += 1
            if v < need:
                nfail += 1
                if len(ex) < 5:
                    va = ca[b] + 2 * da[b] + ca[c] + 2 * da[c] + cja[b + c]
                    ex.append(dict(p=p, n=n, k=k, l=l, a=a, b=b, c=c, r=r, s=s, t=t,
                                   e=(e1, e2, e3, e4), sn=sn, sa=sa, vTn=v, vTa=va,
                                   need=need))
    return noff, nfail, ex

JOBS = []
# level 1 (a < p): full ranges
for p in (5, 7, 11, 13):
    JOBS += [(p, n) for n in range(p, p * p)]
# level 2 : full for p=5,7 ; samples for 11,13,17,19,23,29,31
JOBS += [(5, n) for n in range(25, 125)]
JOBS += [(7, n) for n in range(49, 343, 3)]
for p in (11, 13, 17, 19, 23, 29, 31):
    P2 = p * p
    JOBS += [(p, n) for n in
             (P2, P2 + 1, P2 + p - 1, P2 + p, 2 * P2 // 3, P2 + P2 // 2,
              p * p * 2, p * (p + 1), p * p + p * p // 3, p ** 3 - 1, p ** 3 - p,
              p ** 3 - p - 1, (p ** 3) // 2, (p ** 3) // 2 + 1)
             if logp(n, p) == 2]
# level 3 : samples, small primes
JOBS += [(5, n) for n in (125, 126, 129, 130, 149, 249, 250, 311, 312, 373, 374,
                          499, 500, 561, 599, 620, 623, 624)]
JOBS += [(7, n) for n in (343, 344, 350, 400, 500, 685, 686, 900, 1000, 1200,
                          1715, 2400, 2401 - 1)]
JOBS += [(11, n) for n in (1331, 1332, 1340, 1500, 2000, 2661, 2662, 3000)]
JOBS += [(13, n) for n in (2197, 2198, 2210, 2500, 3000)]
# level 4 : a couple for p=5
JOBS += [(5, n) for n in (625, 626, 630, 700, 1249, 1250, 1560, 3000, 3124)]

if __name__ == '__main__':
    tot_off = 0; tot_fail = 0
    coll = collections.Counter()
    byp = collections.Counter()
    for p, n in JOBS:
        noff, nfail, ex = scan_n(p, n, coll)
        tot_off += noff; tot_fail += nfail
        byp[p] += noff
        if nfail:
            print('FAIL p=%d n=%d : %d failures' % (p, n, nfail))
            for e in ex: print('    ', e)
    print('jobs=%d   off-regime cells scanned=%d   CRUDE failures=%d'
          % (len(JOBS), tot_off, tot_fail))
    print('per prime:', dict(byp))
    print('\n(s_n, s_a, min(vT,6)) census over cells with need>0:')
    for key in sorted(coll):
        sn, sa, v = key
        print('   s_n=%d s_a=%d vT=%s  need=%d   count=%d'
              % (sn, sa, ('%d' % v) if v < 6 else '>=6', max(Jcap(sn), Jcap(sa)), coll[key]))
