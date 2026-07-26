"""T3: the statements that could still carry the proof.

The Theorem-LB proof has TWO vanishing-layer-type requirements, not one:

 (V1)  sum_{k : p | S(n,k)}  S(n,k) p^w w(n,k)  ==  0  (mod p)          [top level]
 (V2)  Delta(a) := sum_{b : p | S(a,b)} S(a,b) w(a,b)  ==  0  (mod p)   [base level]

(V2) is hidden inside (H2): the surviving b-set is  B(a) = {b : p !| S(a,b)}, and the
product-region step only gives  sum_{b in B(a)} S(a,b) w(a,b) = B(a) - Delta(a).
For a tame weight Delta(a) = 0 mod p automatically (w(a,b) is p-integral and p | S(a,b));
for the four non-tame families w(a,b) has a pole of order <= w at 2b >= p, so it is not.

This script measures, exactly:
  * (V2) termwise and aggregated;
  * whether the surviving b-set equals {0..a} (the literal claim of (H2));
  * THE CANCELLATION IDENTITY   V(n)  ==  chi(p)^e * Delta(a) * A(r)   (mod p)
    and                          U(n)  ==  chi(p)^e * (B(a)-Delta(a)) * A(r)  (mod p).
"""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lbw'))

from sporadic import SEQS, gen_A, gen_B                       # noqa: E402
from decs import FAMS, ORDER, ARG                             # noqa: E402
from pad import Tables, vp_int, vp_fr, vp_binom, INF          # noqa: E402

PAR = {l: (f, p) for l, f, p, _, _ in SEQS}
T = 30


def chi_p(D, p):
    return 1 if D == 1 else (1 if p % 4 == 1 else -1)


def run(lab, p):
    fam = FAMS[lab]
    w = fam.w
    M = p ** T
    Y = 2 * (p * p - 1)
    tab = Tables(p, T, Y, rmax=3, want_K=fam.wantK)
    SCW, SCC = 2 * w, max(0, max(vp_int(c.denominator, p) for c, _ in fam.W))
    SC = SCW + SCC
    cs = []
    for c, _ in fam.W:
        cc = c * F(p) ** SCC
        cs.append((cc.numerator % M) * pow(cc.denominator % M, -1, M) % M)

    def wpad(n, k):
        """scaled p-adic w(n,k): integer  A  with  w(n,k) = A * p^(-SC)."""
        tot = 0
        for j, (_, mo) in enumerate(fam.W):
            v = cs[j]
            for kind, rr, ag in mo:
                y = ARG[ag](n, k)
                if y < 0:
                    v = 0
                    break
                v = v * tab.get(kind, rr, y) % M
                if v == 0:
                    break
            tot = (tot + v) % M
        return tot

    f, par = PAR[fam.seqlabel]
    Aseq = gen_A(f, par, p + 2)
    Bsm = gen_B(f, par, p + 2)
    chi = chi_p(fam.D, p) ** fam.e

    # ---------------- base level: Delta(a), B-set, (V2)
    Delta = {}          # a -> scaled p-adic integer for Delta(a)
    v2min, v2arg, v2viol = INF, None, 0
    dmin, dviol = INF, 0
    bset_not_full = []
    for a in range(1, p):
        acc = 0
        full = True
        for b in fam.ks(a):
            bins = fam.BIN(a, b)
            if any(bb < 0 or t < bb for t, bb in bins):
                continue
            vS = sum(vp_binom(t, bb, p) for t, bb in bins)
            if vS == 0:
                continue
            full = False
            A_ = wpad(a, b)
            acc = (acc + fam.S(a, b) % M * A_) % M
            vW = vp_int(A_, p, cap=T) - SC
            if vS + vW < v2min:
                v2min, v2arg = vS + vW, (a, b, vS, vW)
            if vS + vW < 1:
                v2viol += 1
        Delta[a] = acc
        vD = vp_int(acc, p, cap=T) - SC
        if vD < dmin:
            dmin = vD
        if vD < 1:
            dviol += 1
        if not full:
            bset_not_full.append(a)

    # ---------------- top level: V(n), U(n) and the cancellation identity
    idV = idU = 0
    nc = 0
    for a in range(1, p):
        for r in range(p):
            n = a * p + r
            Vacc = Uacc = 0
            for k in fam.ks(n):
                bins = fam.BIN(n, k)
                if any(bb < 0 or t < bb for t, bb in bins):
                    continue
                vS = sum(vp_binom(t, bb, p) for t, bb in bins)
                A_ = wpad(n, k)
                term = fam.S(n, k) % M * A_ % M
                if vS == 0:
                    Uacc = (Uacc + term) % M
                else:
                    Vacc = (Vacc + term) % M
            nc += 1
            Ar = Aseq[r]
            Ars = (Ar.numerator % M) * pow(Ar.denominator % M, -1, M) % M
            # predicted V = chi * Delta(a) * A(r);  both sides carry p^(-SC), V also p^w
            predV = chi * Delta[a] % M * Ars % M
            dv = (Vacc * pow(p, w, M) - predV) % M
            if vp_int(dv, p, cap=T) - SC < 1:
                idV += 1
            Ba = Bsm[a]
            Bas = (Ba.numerator % M) * pow(Ba.denominator % M, -1, M) % M
            predU = chi * ((Bas * pow(p, SC, M) - Delta[a]) % M) * Ars % M
            du = (Uacc * pow(p, w, M) - predU) % M
            if vp_int(du, p, cap=T) - SC < 1:
                idU += 1
    return dict(v2min=v2min, v2arg=v2arg, v2viol=v2viol, dmin=dmin, dviol=dviol,
                bsetnf=bset_not_full, idV=idV, idU=idU, nc=nc)


def fmt(v):
    return 'inf' if v >= INF else str(v)


if __name__ == '__main__':
    labs = sys.argv[1].split(',') if len(sys.argv) > 1 else ORDER
    primes = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 \
        else [5, 7, 11, 13, 17, 19, 23]
    for lab in labs:
        for p in primes:
            R = run(lab, p)
            print('%-6s p=%-3d | (V2) termwise min=%-4s viol=%-4d | Delta(a) min v_p=%-4s '
                  'a with Delta!=0 mod p: %-3d | B-set != {0..a} for a in %s | '
                  'cancellation V: %d/%d fail, U: %d/%d fail'
                  % (lab, p, fmt(R['v2min']), R['v2viol'], fmt(R['dmin']), R['dviol'],
                     R['bsetnf'][:6], R['idV'], R['nc'], R['idU'], R['nc']), flush=True)
            if R['v2arg']:
                a, b, vS, vW = R['v2arg']
                print('        worst (V2) term: a=%d b=%d  v_p(S(a,b))=%d v_p(w(a,b))=%d '
                      'sum=%d   [2b=%d, p=%d]' % (a, b, vS, vW, vS + vW, 2 * b, p),
                      flush=True)
        print('-' * 128, flush=True)
