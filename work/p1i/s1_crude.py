"""Phase 1 (cheap, no w5): where does the CRUDE criterion for the descent term fail?

Crude criterion (from (DEPTH-gen) at BOTH levels):
    v_p(p^5 v5(n,k,l)) >= 5 - 5*L - J(pi_n)          [level n, M_n = L+1]
    v_p(   v5(a,b,c) ) >=   -5(L-1) - J(pi_a)        [level a, M_a = L]
  =>  v_p(E) >= -5(L-1) - max(J_n, J_a)
  =>  v_p(T(n,k,l) E) >= -5(L-1)   as soon as   vT_n >= max(J_n, J_a).       (CRUDE)

We scan every cell of every n in the given range, flag the OFF-REGIME cells
(s>r or t>r or e1+e2+e3+e4>0) where (CRUDE) fails, and classify them.
"""
import sys, collections
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1i')
from kummer import car, vT, pattern, Jcap, logp

def scan(p, nlo, nhi, verbose=False):
    stats = collections.Counter()
    fails = []
    for n in range(nlo, nhi + 1):
        L = logp(n, p)
        if L < 1: continue
        a, r = divmod(n, p)
        for k in range(n + 1):
            b, s = divmod(k, p)
            for l in range(n + 1):
                c, t = divmod(l, p)
                e1 = 1 if r + s >= p else 0
                e2 = 1 if r + t >= p else 0
                e3 = (r + s + t) // p
                e4 = 1 if s + t >= p else 0
                off = (s > r) or (t > r) or (e1 + e2 + e3 + e4 > 0)
                if not off:
                    stats['in'] += 1
                    continue
                stats['off'] += 1
                sn = sum(pattern(n, k, l, p, L + 1)[:3])
                sa = sum(pattern(a, b, c, p, L)[:3])
                need = max(Jcap(sn), Jcap(sa))
                v = vT(n, k, l, p)
                if v < need:
                    stats['crude_fail'] += 1
                    fails.append((n, k, l, a, b, c, r, s, t, e1, e2, e3, e4,
                                  sn, sa, v, need))
    return stats, fails

if __name__ == '__main__':
    for p, nlo, nhi in [(5, 5, 60), (7, 7, 60), (11, 11, 60), (13, 13, 60)]:
        stats, fails = scan(p, nlo, nhi)
        print('p=%2d n=%d..%d  in=%d off=%d  CRUDE failures=%d'
              % (p, nlo, nhi, stats['in'], stats['off'], stats['crude_fail']), flush=True)
        # classify the failures
        cl = collections.Counter()
        for f in fails:
            (n, k, l, a, b, c, r, s, t, e1, e2, e3, e4, sn, sa, v, need) = f
            cl[('e', e1, e2, e3, e4, 'sr', int(s > r), int(t > r), 'sn', sn, 'sa', sa,
                'vT', v, 'need', need)] += 1
        for key, cnt in sorted(cl.items(), key=lambda x: -x[1])[:12]:
            print('     %6d  %s' % (cnt, key))
        if fails:
            print('     example:', fails[0])
