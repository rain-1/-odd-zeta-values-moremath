"""Direct confirmation of the kernel verdict, without linear algebra:
perturb w_0 by each exact kernel basis vector and recompute Delta(a) mod p."""
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'lbw'))
sys.path.insert(0, os.path.join(HERE, '..', 'sporadic'))

from sporadic import SEQS, gen_B                               # noqa: E402
from decs import FAMS                                          # noqa: E402
from pad import vp_binom, vp_fr, INF                           # noqa: E402
import kernel as KK                                            # noqa: E402

PAR = {l: (f, p) for l, f, p, _, _ in SEQS}


def deltas(lab, p, co, mons):
    fam = FAMS[lab]
    out = {}
    for a in range(1, p):
        tot = F(0)
        for b in fam.ks(a):
            bins = fam.BIN(a, b)
            if any(bb < 0 or t < bb for t, bb in bins):
                continue
            if sum(vp_binom(t, bb, p) for t, bb in bins) == 0:
                continue
            tot += fam.S(a, b) * KK.w_from_coeffs(co, mons, a, b)
        out[a] = tot
    return out


if __name__ == '__main__':
    lab = sys.argv[1] if len(sys.argv) > 1 else 'alpha'
    p = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    ker, mons, st = KK.kernel_exact(lab)
    co0, _ = KK.w0_coeffs(lab, mons)
    fam = FAMS[lab]
    f, par = PAR[KK.SEQOF[lab]]
    Bn = gen_B(f, par, p + 2)
    d0 = deltas(lab, p, co0, mons)
    print('%s  p=%d   Delta(a) for LBW w_0 (exact rationals, v_p and residue):' % (lab, p))
    for a in sorted(d0):
        v = vp_fr(d0[a], p)
        res = 'n/a' if v < 0 else str((d0[a] * p ** 0).numerator % p
                                      * pow(d0[a].denominator % p, -1, p) % p
                                      if d0[a] != 0 else 0)
        print('    a=%d  Delta=%s   v_p=%s  Delta mod p = %s'
              % (a, str(d0[a])[:40], 'inf' if v >= INF else v, res))
    print('  perturbations w_0 + kappa_i  ->  Delta(a) mod p  (a with Delta_0 != 0 shown):')
    hot = [a for a in d0 if d0[a] != 0 and vp_fr(d0[a], p) < 1]
    if not hot:
        print('    (none: Delta(a) == 0 mod p for every a already)')
    for i, kv in enumerate(ker):
        co = [c + kv[j] for j, c in enumerate(co0)]
        d = deltas(lab, p, co, mons)
        chg = [(a, str((d[a] - d0[a]) != 0)) for a in hot]
        vals = []
        for a in hot:
            x = d[a]
            v = vp_fr(x, p)
            vals.append('a=%d:%s' % (a, 'ZERO mod p' if v >= 1 else
                                     ('pole' if v < 0 else
                                      str(x.numerator % p * pow(x.denominator % p, -1, p) % p))))
        moved = any(d[a] != d0[a] for a in hot)
        print('    kappa_%-2d moved Delta? %-5s  %s' % (i, moved, '  '.join(vals)))
