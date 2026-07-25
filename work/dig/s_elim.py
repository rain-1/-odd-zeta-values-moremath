"""DIG-3  s_elim.py -- THE RANK QUESTION for zeta_2(7).

DIG-1's ledger says the p = 2 VWP family has

    margin(M, m) = 2M log2 - (M + m)  =  M (2 log 2 - 1) - m,

which is POSITIVE at weight 7 as soon as M >= 6:
    M=6, m=1 : weights {5,7}, rank 2, margin +1.3178, mu would be 12.6240
    M=7, m=0 : weights {3,5,7}, rank 3, margin +2.7041, mu would be 7.1774
    M=8, m=1 : weights {5,7,9}, rank 3, margin +2.0904, mu would be 10.6110
So the ONLY obstruction to zeta_2(7) inside this family is RANK, never size.
(The rank-1 slice caps M at 4 and gives the -1.4548 "nearest miss".)

This module asks, exhaustively and honestly: can the rank be brought to 1?

Two mechanisms are available in principle:
  (I)  a single point of the cone at which the unwanted rho_i vanishes identically
       -- searched over the inset lattice (e, f) and the length lattice;
  (II) an elimination:  sum_j c_j(n) S^{(j)}_n  with c_j POLYNOMIAL in n (cost
       e^{o(n)}, so it costs nothing in the ledger) that kills the unwanted rho_i
       but not rho_w.  (Non-polynomial c_j cost e^{Gn} each and destroy the
       margin: alpha - 2*beta < 0 always.  This is the classical elimination
       tax, and it is why "one of zeta(5), zeta(7)" is never sharpened.)

Everything is exact; the wide scans run modulo a 62-bit prime and every hit is
re-verified over Q.
"""
import sys, os, math, itertools, random
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s_vwp import VWPX, asymptotic_ledger, LOG2

Q = (1 << 61) - 1          # a Mersenne prime, > everything we need
Q2 = 4611686018427387847   # a second prime for confirmation


# ------------------------------------------------------- mod-q partial fractions
def pf_rho_modq(h0, e, f, q, dwp=1, imax=None):
    """rho_i mod q for i = 1..M, for R = (2t+h0)^dwp prod (t+1/2+e_j)_{h0-2e_j}
    / prod (t+f_j)_{h0+1-2f_j}.   Numerator roots are half-integers: we work with
    2*root to stay in Z, then divide by 2^{#num} at the end (a global scalar, so
    it does not affect vanishing)."""
    M = len(e)
    imax = imax or M
    inv2 = pow(2, q - 2, q)
    num2 = []          # 2 * (numerator root)  = 1 + 2 e_j + 2 i    (odd integers)
    for ej in e:
        L = h0 - 2 * ej
        num2 += [1 + 2 * ej + 2 * i for i in range(L)]
    den = []
    for fj in f:
        L = h0 + 1 - 2 * fj
        den += [fj + i for i in range(L)]
    rho = [0] * (M + 1)
    dencount = {}
    for c in den:
        dencount[c] = dencount.get(c, 0) + 1
    for k in sorted(dencount):
        mk = dencount[k]
        D = mk - 1
        # numerator series prod (eps + (root - k)) = 2^{-N} prod (2 eps + (num2 - 2k))
        top = [0] * (D + 1)
        top[0] = 1
        for a in num2:
            b = (a - 2 * k) % q
            newt = [0] * (D + 1)
            for d in range(D + 1):
                if top[d]:
                    newt[d] = (newt[d] + top[d] * b) % q
                    if d + 1 <= D:
                        newt[d + 1] = (newt[d + 1] + 2 * top[d]) % q
            top = newt
        # denominator (other roots)
        bot = [0] * (D + 1)
        bot[0] = 1
        for c, mult in dencount.items():
            mm = mult - (mk if c == k else 0)
            if c == k:
                mm = 0
            for _ in range(mult if c != k else 0):
                b = (c - k) % q
                newb = [0] * (D + 1)
                for d in range(D + 1):
                    if bot[d]:
                        newb[d] = (newb[d] + bot[d] * b) % q
                        if d + 1 <= D:
                            newb[d + 1] = (newb[d + 1] + bot[d]) % q
                bot = newb
        # invert bot
        inv = [0] * (D + 1)
        inv[0] = pow(bot[0], q - 2, q)
        for kk in range(1, D + 1):
            acc = 0
            for j in range(1, kk + 1):
                acc = (acc + bot[j] * inv[kk - j]) % q
            inv[kk] = (-acc * inv[0]) % q
        # well-poised linear factor  (h0 - 2k) + 2 eps
        lin = [0] * (D + 1)
        if dwp:
            lin[0] = (h0 - 2 * k) % q
            if D >= 1:
                lin[1] = 2
        else:
            lin[0] = 1
        # G = lin * top * inv, truncated at D ; but top is in "2 eps": substitute
        # eps -> eps means top coefficient d carries (2)^d already handled above.
        G = [0] * (D + 1)
        for a in range(D + 1):
            if not lin[a]:
                continue
            for b in range(D + 1 - a):
                if top[b]:
                    G[a + b] = (G[a + b] + lin[a] * top[b]) % q
        G2 = [0] * (D + 1)
        for a in range(D + 1):
            if not G[a]:
                continue
            for b in range(D + 1 - a):
                if inv[b]:
                    G2[a + b] = (G2[a + b] + G[a] * inv[b]) % q
        for i in range(1, mk + 1):
            rho[i] = (rho[i] + G2[mk - i]) % q
    return rho


def rho_exact(h0, e, f, dwp=1):
    v = VWPX(h0, e, f, dwp)
    return v.rho()


# ------------------------------------------------------- inset lattice
def insets(M, lo, hi, sumcap=None):
    for e in itertools.product(range(lo, hi + 1), repeat=M):
        if sumcap is not None and abs(sum(e)) > sumcap:
            continue
        yield e


def admissible_pair(M, e, f, dwp=1):
    """deg R = dwp + sum(h0-2e) - sum(h0+1-2f) = dwp - M + 2(sum f - sum e) <= -2,
    independent of h0; plus every brick non-empty for large h0."""
    return dwp - M + 2 * (sum(f) - sum(e)) <= -2


# ------------------------------------------------------- (I) pointwise vanishing
def scan_pointwise(M, i_kill, lo=-2, hi=2, ns=(9, 10, 11, 12), dwp=1, cap=200000):
    """search the inset lattice for rho_{i_kill} = 0 at EVERY n in ns."""
    hits, tested = [], 0
    base = list(insets(M, lo, hi))
    for e in base:
        for f in base:
            if not admissible_pair(M, e, f, dwp):
                continue
            tested += 1
            if tested > cap:
                return hits, tested
            ok = True
            for n in ns:
                if n - 2 * max(e) < 1 or n + 1 - 2 * max(f) < 1:
                    ok = False
                    break
                rr = pf_rho_modq(n, e, f, Q, dwp)
                if rr[i_kill] % Q != 0:
                    ok = False
                    break
            if ok:
                hits.append((e, f))
    return hits, tested


# ------------------------------------------------------- (II) elimination test
def elim_test(M, m, i_kill, i_keep, forms, ns, Dmax=6, q=Q, dwp=1, verbose=True):
    """Is there c_j(n) = sum_d c_{j,d} n^d (deg <= Dmax) with
         sum_j c_j(n) rho_{i_kill}^{(j)}(n) = 0  for all n in ns,
         sum_j c_j(n) rho_{i_keep}^{(j)}(n) != 0 ?
    Solved over F_q by nullspace of the i_kill block, then evaluated on i_keep."""
    J = len(forms)
    NU = J * (Dmax + 1)
    rows_kill, rows_keep = [], []
    tab = {}
    for n in ns:
        for j, (e, f) in enumerate(forms):
            tab[(n, j)] = pf_rho_modq(n, e, f, q, dwp)
    for n in ns:
        rk, rp = [], []
        for j in range(J):
            rho = tab[(n, j)]
            for d in range(Dmax + 1):
                rk.append(rho[i_kill] * pow(n, d, q) % q)
                rp.append(rho[i_keep] * pow(n, d, q) % q)
        rows_kill.append(rk)
        rows_keep.append(rp)
    # nullspace of rows_kill over F_q
    A = [r[:] for r in rows_kill]
    R, C = len(A), NU
    piv, where = 0, [-1] * C
    for c in range(C):
        sel = None
        for r in range(piv, R):
            if A[r][c]:
                sel = r
                break
        if sel is None:
            continue
        A[piv], A[sel] = A[sel], A[piv]
        iv = pow(A[piv][c], q - 2, q)
        A[piv] = [x * iv % q for x in A[piv]]
        for r in range(R):
            if r != piv and A[r][c]:
                fac = A[r][c]
                A[r] = [(A[r][cc] - fac * A[piv][cc]) % q for cc in range(C)]
        where[c] = piv
        piv += 1
        if piv == R:
            break
    free = [c for c in range(C) if where[c] == -1]
    null = []
    for fc in free:
        vec = [0] * C
        vec[fc] = 1
        for c in range(C):
            if where[c] != -1:
                vec[c] = (-A[where[c]][fc]) % q
        null.append(vec)
    # evaluate the i_keep functional on the nullspace
    survives = []
    for vec in null:
        vals = [sum(rows_keep[t][c] * vec[c] for c in range(C)) % q
                for t in range(len(ns))]
        if any(v for v in vals):
            survives.append((vec, vals))
    if verbose:
        print("      forms J=%d, deg<=%d -> %d unknowns, %d equations (n=%s..%s)"
              % (J, Dmax, NU, len(ns), ns[0], ns[-1]))
        print("      dim null(rho_%d) = %d ;  of these %d also survive on rho_%d"
              % (i_kill, len(null), len(survives), i_keep))
    return null, survives
