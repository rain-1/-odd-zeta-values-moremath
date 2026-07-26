"""Full exact certificate for the counterexample cells (everything with Fractions)."""
import os
import sys
from fractions import Fraction as F
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'lbw'))

from sporadic import SEQS, gen_A, gen_B                       # noqa: E402
from decs import FAMS, ARG                                    # noqa: E402
from pad import vp_int, vp_fr, vp_binom, INF                  # noqa: E402
from selfcheck import wexact                                  # noqa: E402

PAR = {l: (f, p) for l, f, p, _, _ in SEQS}

CASES = [
    ('alpha', 5, 20, 5),
    ('alpha', 7, 35, 7),
    ('eps', 5, 15, 15),
    ('eps', 7, 28, 28),
    ('E', 5, 15, 15),
    ('E', 7, 28, 28),
    ('s7', 7, 15, 14),
]

for lab, p, n, k in CASES:
    fam = FAMS[lab]
    a, r = n // p, n % p
    b, s = k // p, k % p
    S = fam.S(n, k)
    vS = sum(vp_binom(t, bb, p) for t, bb in fam.BIN(n, k))
    assert vS == vp_int(S, p), (vS, vp_int(S, p))
    wv = wexact(fam, n, k)
    vw = vp_fr(wv, p)
    args = sorted({ag for _, mo in fam.W for _, _, ag in mo})
    wide = [(ag, ARG[ag](n, k), ARG[ag](n, k) // p) for ag in args]
    print('%s  p=%d   n = %d = %d*%d + %d ,  k = %d = %d*%d + %d' %
          (lab, p, n, a, p, r, k, b, p, s))
    print('   S(n,k) = %s   (v_p = %d, so p | S : VANISHING layer)' % (S, vS))
    print('   binomials %s  ->  valuations %s'
          % (fam.BIN(n, k), [vp_binom(t, bb, p) for t, bb in fam.BIN(n, k)]))
    for ag, x, fl in wide:
        print('      arg %-6s = %-5d   floor(x/p) = %-4d %s'
              % (ag, x, fl, '<-- WIDE: floor(x/p) >= p, letter has a pole' if fl >= p else ''))
    print('   w(n,k) = %s' % (str(wv)[:90] + ('...' if len(str(wv)) > 90 else '')))
    print('   v_p(w) = %d ,  v_p(p^w w) = %d ,  v_p(S) + v_p(p^w w) = %d   %s'
          % (vw, vw + fam.w, vS + vw + fam.w,
             '***  < 1 : SPORADIC_BARE inequality FAILS  ***'
             if vS + vw + fam.w < 1 else '(>= 1, holds)'))
    # aggregated layer in this cell
    V = F(0)
    for kk in fam.ks(n):
        bins = fam.BIN(n, kk)
        if any(bb < 0 or t < bb for t, bb in bins):
            continue
        if sum(vp_binom(t, bb, p) for t, bb in bins) > 0:
            V += fam.S(n, kk) * F(p) ** fam.w * wexact(fam, n, kk)
    print('   AGGREGATED vanishing layer  V(n) = sum_{p|S} S p^w w :  v_p(V) = %d  %s'
          % (vp_fr(V, p), '***  < 1 : the aggregated bound FAILS too  ***'
             if vp_fr(V, p) < 1 else '(>= 1)'))
    # Delta(a) and the identity
    Delta = F(0)
    for bb in fam.ks(a):
        bins = fam.BIN(a, bb)
        if any(x < 0 or t < x for t, x in bins):
            continue
        if sum(vp_binom(t, x, p) for t, x in bins) > 0:
            Delta += fam.S(a, bb) * wexact(fam, a, bb)
    f, par = PAR[fam.seqlabel]
    Aq = gen_A(f, par, p + 2)
    chi = 1 if fam.D == 1 else (1 if p % 4 == 1 else -1)
    pred = chi ** fam.e * Delta * Aq[r]
    print('   Delta(a=%d) = %s ,  chi(p)^e Delta(a) A(r) = %s' % (a, Delta, pred))
    print('   IDENTITY  v_p( V(n) - chi^e Delta(a) A(r) ) = %s   %s\n'
          % ('inf' if vp_fr(V - pred, p) >= INF else vp_fr(V - pred, p),
             '<-- >= 1 : the cancellation identity HOLDS'
             if vp_fr(V - pred, p) >= 1 else '<-- FAILS'))
