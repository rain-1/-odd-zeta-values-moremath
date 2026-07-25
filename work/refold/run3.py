"""P1e-refold stage 3 driver: is <= SMAX distinct symbols reachable once the
coefficients are allowed to be POLYNOMIALS in (n,k,l) and the weight grading is
dropped?

For every closed symbol mask with <= SMAX symbols (equivalently every letter set
L with |symbols(L)| <= SMAX) test consistency of

    Phat_n = sum_{k,l} T(n,k,l) * sum_{mu, a+b+c<=dp} lambda_{mu,abc} n^a k^b l^c mu(n,k,l)

with mu ranging over letter monomials of degree <= Dm in L.

Also applies the p-ADIC POLE TEST first (a rigorous necessary condition, valid for
any p-integral coefficients):  v_p(Phat_n) = -1 is attained for every prime 5..59
(vp_phat.py), and
    v_p( sum T w ) >= min over reachable patterns pi of ( vT(pi) - D_L(pi) ),
    D_L(pi) = max pole weight of a monomial of L at pi
            = max over mu of  alpha*wA_k(mu) + gamma*wA_l(mu) + kappa*wC(mu),
reachable pi = (0,0,0;0) (0,0,1;1) (1,0,1;2) (0,1,1;2) (1,1,0;2) (1,1,1;3).
A letter set that cannot reach -1 is EXCLUDED outright.
"""
import sys, os, time, json
import numpy as np
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from w3full import LSYM, ALL_SYMBOLS, SYMIDX, rref_aug, Q1, Q2
from polyfit import PolySpec, pdesign

SMAX = int(os.environ.get('SMAX', 4))
DP = int(os.environ.get('DP', 2))
DM = int(os.environ.get('DM', 3))
NROW = int(os.environ.get('NROW', 0))       # 0 -> auto
q = int(os.environ.get('Q', Q1))
MODE = os.environ.get('MODE', 'S')          # S = whole summand, E = degree>=2 only

pc = lambda x: bin(int(x)).count('1')
letters = sorted(LSYM)
lmask = {lt: sum(1 << SYMIDX[s] for s in LSYM[lt]) for lt in letters}

# ------------------------------------------- enumerate letter sets, by symbol mask
seen = {}
frontier = {frozenset(): 0}
while frontier:
    nxt = {}
    for L, m in frontier.items():
        for lt in letters:
            if lt in L:
                continue
            mm = m | lmask[lt]
            if pc(mm) <= SMAX:
                LL = frozenset(L | {lt})
                if LL not in seen and LL not in nxt:
                    nxt[LL] = mm
    seen.update(frontier)
    frontier = nxt
seen.pop(frozenset(), None)
# keep only MAXIMAL letter sets for each symbol mask (a subset's columns are a subset)
bymask = {}
for L, m in seen.items():
    bymask.setdefault(m, set()).update(L)
cands = sorted(bymask.items(), key=lambda t: (pc(t[0]), sorted(t[1])))
print('SMAX=%d  DP=%d  DM=%d  MODE=%s  q=%d' % (SMAX, DP, DM, MODE, q), flush=True)
print('closed symbol masks with <= %d symbols: %d' % (SMAX, len(cands)), flush=True)

# -------------------------------------------------------------- p-adic pole test
PATTERNS = [(0, 0, 0, 0), (0, 0, 1, 1), (1, 0, 1, 2), (0, 1, 1, 2),
            (1, 1, 0, 2), (1, 1, 1, 3)]


def pole_ok(L, Dm):
    """can some monomial of degree <= Dm in L reach v_p = -1 ?"""
    wa_k = [int(x[1]) for x in L if x[0] == 'A' and x.endswith('(k)')]
    wa_l = [int(x[1]) for x in L if x[0] == 'A' and x.endswith('(l)')]
    wc = [int(x[1]) for x in L if x[0] == 'C']
    best = 99
    for (al, ga, ka, vT) in PATTERNS:
        pool = ([r for r in wa_k] if al else []) + ([r for r in wa_l] if ga else []) \
               + ([r for r in wc] if ka else [])
        if not pool:
            D = 0
        else:
            D = Dm * max(pool)          # <= Dm factors, best one repeated
        best = min(best, vT - D)
    return best <= -1


# NOTE: in MODE=E the FREE columns already include A3(k), A3(l), C3 with constant
# coefficients, which carry poles of weight 3, so the pole test is vacuous there.
live = ([(m, sorted(L)) for m, L in cands if pole_ok(sorted(L), DM)] if MODE == 'S'
        else [(m, sorted(L)) for m, L in cands])
print('survive the p-adic pole test: %d / %d' % (len(live), len(cands)), flush=True)

# ------------------------------------------------------------------------ fit
res = []
t00 = time.time()
for ii, (m, L) in enumerate(live):
    if MODE == 'S':
        spec = PolySpec(L, DP, DM, deg_min=0, deg_max=DM)
    else:
        # E-mode.  E(w) = sum_tau G_tau (tau.w - w).  For a term c*m with m a SINGLE
        # letter and c a CONSTANT, tau.(c m) - c m = c*(tau.m - m) is rational, so the
        # letter does not appear in E.  For a NON-constant coefficient,
        #   tau.(c m) - c m = (tau.c - c) m + (tau.c)(tau.m - m),
        # so the letter DOES appear.  Hence exactly two classes are free of charge:
        #   (i) the six weight-3 single letters with CONSTANT coefficient,
        #  (ii) the purely rational (letter-free) part, any polynomial coefficient.
        # Everything else is charged and must have its letters inside L.
        free = []
        for lt in ['A3', 'B3']:
            free.append(((lt,), (), (), (), 0, 0, 0))
            free.append(((), (lt,), (), (), 0, 0, 0))
        free.append(((), (), ('C3',), (), 0, 0, 0))
        free.append(((), (), (), ('N3',), 0, 0, 0))
        for a in range(DP + 1):                       # the pure rational part
            for bb in range(DP + 1 - a):
                for cc in range(DP + 1 - a - bb):
                    free.append(((), (), (), (), a, bb, cc))
        spec = PolySpec(L, DP, DM, deg_min=1, deg_max=DM, extra_free=free)
    nc = len(spec)
    # GUARD: the fit is meaningless unless there are many more equations than
    # unknowns -- a system with rank(M) = #rows is trivially "consistent".
    N = NROW if NROW else max(150, nc + max(150, nc // 2))
    M, b = pdesign(spec, N, q)
    r, piv, inc, A = rref_aug(M, b, q)
    excess = N - r
    ok = (not inc) and excess >= 100
    verdict = ('CONSISTENT' if not inc else 'incons') if excess >= 100 else 'UNDETERMINED'
    res.append((pc(m), L, nc, N, r, ok, verdict, excess))
    if ok:
        print('  *** CONSISTENT  symbols=%d  L=%s  cols=%d rows=%d rank=%d excess=%d'
              % (pc(m), L, nc, N, r, excess), flush=True)
    if ii % 25 == 0:
        print('    [%d/%d]  %s  cols=%d rows=%d rank=%d excess=%d  %s  (%.0f s)'
              % (ii, len(live), L, nc, N, r, excess, verdict,
                 time.time() - t00), flush=True)

good = [x for x in res if x[5]]
und = [x for x in res if x[6] == "UNDETERMINED"]
print("UNDETERMINED (too few excess equations): %d" % len(und), flush=True)
print('\nRESULT: %d / %d letter sets with <= %d symbols are CONSISTENT '
      '(poly coefficients deg <= %d, letter degree <= %d)'
      % (len(good), len(res), SMAX, DP, DM), flush=True)
for x in good:
    print('   ', x, flush=True)
json.dump([[x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]] for x in res],
          open(os.path.join(HERE, 'stage3_%s_S%d_D%d.json' % (MODE, SMAX, DP)), 'w'),
          indent=1)
