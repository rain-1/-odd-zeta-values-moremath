"""Measure the exact pole structure, in k and in l, of the residual right-hand
side of every FREE block at order m (Theorem-R blocks fixed).  This is what the
ansatz denominator must contain."""
import sys
import numpy as np
import ordm, ratrec

p = 4194301


def measure(which, n, m, tt, nsamp=170):
    lfix = 37
    kfix = 41
    # --- k-direction ---
    ks = [k for k in range(n + m + 4, n + m + 4 + 400)][:nsamp]
    pts = [(k, lfix) for k in ks]
    pd = ordm.PDm(which, p, n, m, 0, pts=pts)
    A = ordm.acols(pd)
    J, N = pd.J, pd.npts
    kroots = ([('k+1', -1), ('k+2', -2), ('k+l+1', -(lfix + 1)), ('k+l+2', -(lfix + 2))]
              + [('n+k+%d' % j, -(n + j)) for j in range(0, m + 4)]
              + [('n+%d-k' % j, n + j) for j in range(0, m + 4)]
              + [('n+k+l+%d' % j, -(n + lfix + j)) for j in range(0, m + 4)])
    # --- l-direction ---
    lss = [l for l in range(n + m + 4, n + m + 4 + 400)][:nsamp]
    pts2 = [(kfix, l) for l in lss]
    pd2 = ordm.PDm(which, p, n, m, 0, pts=pts2)
    A2 = ordm.acols(pd2)
    lroots = ([('l+1', -1), ('l+2', -2), ('k+l+1', -(kfix + 1)), ('k+l+2', -(kfix + 2))]
              + [('n+l+%d' % j, -(n + j)) for j in range(0, m + 4)]
              + [('n+%d-l' % j, n + j) for j in range(0, m + 4)]
              + [('n+k+l+%d' % j, -(n + kfix + j)) for j in range(0, m + 4)])
    out = {}
    for i in range(J):
        if i in pd.supp: continue
        vk = [int(A[i * N + t, tt]) for t in range(N)]
        rk = ratrec.null_min_deg(vk, ks, p, 80)
        vl = [int(A2[i * pd2.npts + t, tt]) for t in range(pd2.npts)]
        rl = ratrec.null_min_deg(vl, lss, p, 80)
        rec = {}
        for lab, r, roots in (('k', rk, kroots), ('l', rl, lroots)):
            if r is None:
                rec[lab] = ('FAIL', None, None); continue
            num, den = r
            fac, rest = ratrec.factor_mult(den, roots, p)
            rec[lab] = (len(num) - 1, fac, len(rest) - 1)
        out[pd.B[i]] = rec
    return out


if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'w3'
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    for m in [int(x) for x in (sys.argv[3:] or ['4'])]:
        for tt in range(min(2, m - 2)):
            print('=== %s n=%d m=%d  a_%d column ===' % (which, n, m, tt), flush=True)
            out = measure(which, n, m, tt)
            for b, rec in out.items():
                for lab in ('k', 'l'):
                    dg, fac, restdeg = rec[lab]
                    print('  %-22s %s: degnum=%-3s den=%-70s residual-deg=%s'
                          % (str(b), lab, dg,
                             '*'.join('%s%s' % (a, '^%d' % c if c > 1 else '')
                                      for a, c in (fac or {}).items()), restdeg),
                          flush=True)
