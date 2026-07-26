"""Strip the denominator down to the minimum that still admits a solution."""
import sys, json
from fractions import Fraction as Fr
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import wtools as W
import cert2, ordm, solve

K1, L1 = ordm.K1, ordm.L1
NK, NL, NKL = ordm.NK, ordm.NL, ordm.NKL
KL = [(j, 0, 1, 1) for j in range(0, 12)]
for _j in range(12):
    solve.NAMES[KL[_j]] = 'k+l+%d' % _j

def D(k1, l1, kl, nk, nl, nkl):
    out = []
    if k1: out.append((K1, k1))
    if l1: out.append((L1, l1))
    for j in range(1, kl + 1): out.append((KL[j], 1))
    for j in range(1, nk + 1): out.append((NK[j], 1))
    for j in range(1, nl + 1): out.append((NL[j], 1))
    for j in range(1, nkl + 1): out.append((NKL[j], 1))
    return out

CAND = {
 'J0': D(3,3,1,3,3,0),      # = H3
 'J1': D(3,3,0,3,3,0),
 'J2': D(2,2,1,3,3,0),
 'J3': D(3,3,1,2,2,0),
 'J4': D(3,3,1,0,0,0),
 'J5': D(1,1,1,3,3,0),
 'J6': D(0,0,1,3,3,0),
 'J7': D(3,3,1,3,3,0),
 'J8': D(2,2,0,3,3,0),
 'J9': D(3,3,1,1,1,0),
}
orig = cert2.dens2
def dens2(m=3):
    out = dict(orig(m)); out.update(CAND); return out
cert2.dens2 = dens2

p = W.P1
d = json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
w = W.to_p([Fr(c) for c in d['coeffs']], p)
n = int(sys.argv[1])
for nm in sorted(CAND):
    Dn = CAND[nm]
    dk0 = sum(mu*abs(f[2]) for f,mu in Dn)
    for slack in range(0, 17):
        r = cert2.letters_only(n, w, W.B, nm, slack, 1, p=p, verbose=False)
        if r['nfail'] == 0:
            a = r['ans']
            print('   %-3s %-62s dk0=%2d -> bidegree (%d,%d) nc=%d  [slack %d]'
                  % (nm, solve.dstr(Dn), dk0, a.par[0], a.par[1], a.nc, slack), flush=True)
            break
    else:
        print('   %-3s %-62s dk0=%2d -> NO SOLUTION up to slack 16' % (nm, solve.dstr(Dn), dk0), flush=True)
