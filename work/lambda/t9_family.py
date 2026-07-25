"""T4: cross-family and cross-weight.
The 15 sporadic Apery-like pairs (Malik-Straub / Zagier / Almkvist-Zudilin / Cooper),
table from work/LBW_GENERAL.md.  For each: tower limits Lambda_a = lim p^{ws}B(ap^s)/A(ap^s),
their existence, valuation stability, and the convergence RATE.

Prediction from the structure theorem: the rate is 3 digits per level for EVERY family and
EVERY weight, because it is the Kazandzidis p^3 of the binomial blocks C(ap^t,bp^t) out of
which every such tower limit is assembled; the weight w only fixes the normalising p^{ws}
(the pole order of the harmonic weight).
"""
import sys, time
from fractions import Fraction as Fr
from pnum import P
from core import gen_mod, vp_fact

# label, kind (order of (n+1)^k), params, weight w, chi, archimedean limit
FAM = [
    ("A_Franel",  2, (7, 2, -8),      2, "1",     "zeta(2)/4"),
    ("B_none",    2, (9, 3, 27),      2, "chi-3", "NONE (complex roots)"),
    ("C",         2, (10, 3, 9),      2, "chi-3", "L_{-3}(2)/2"),
    ("D_zeta2",   2, (11, 3, -1),     2, "1",     "zeta(2)/5"),
    ("E",         2, (12, 4, 32),     2, "chi-4", "G/2"),
    ("F",         2, (17, 6, 72),     2, "chi-3", "(5/8)L_{-3}(2)"),
    ("alpha_Domb",3, (10, 4, 64, 0),  3, "1",     "7zeta(3)/24"),
    ("gamma_Apery",3,(17, 5, 1, 0),   3, "1",     "zeta(3)/6"),
    ("delta_none",3, (7, 3, 81, 0),   3, "1",     "NONE (complex roots)"),
    ("epsilon",   3, (12, 4, 16, 0),  3, "1",     "7zeta(3)/32"),
    ("zeta_seq",  3, (9, 3, -27, 0),  3, "chi-3", "L_{-3}(3)/3"),
    ("eta_none",  3, (11, 5, 125, 0), 3, "chi5",  "NONE (complex roots)"),
    ("s7",        3, (13, 4, -27, 3), 2, "1",     "zeta(2)/7"),
    ("s10",       3, (6, 2, -64, 4),  2, "1",     "zeta(2)/5"),
    ("s18",       3, (14, 6, 192, -12),2,"chi-3", "L_{-3}(2)/2"),
]

def towers(p, N, kind, par, w, amax=3):
    K = 45 + kind*vp_fact(N, p) + 20
    M = p**K
    want = {}
    for a in range(1, amax+1):
        if a % p == 0: continue
        n = a
        while n <= N:
            want[n] = 1; n *= p
    res = gen_mod(kind, par, N, M, want.keys())
    out = {}
    for a in range(1, amax+1):
        if a % p == 0: continue
        rows = []
        n = a; s = 0
        while n <= N:
            A, B = res[n]
            PA = P(p, 0, A % M, K); PB = P(p, 0, B % M, K)
            if PA.is_zero(): rows.append(None); s += 1; n *= p; continue
            rows.append(((PB / PA).rescale(w*s)).trunc(40))
            s += 1; n *= p
        out[a] = rows
    return out

if __name__ == "__main__":
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
    print("p = %d, N = %d   (rate = digits gained per tower level)" % (p, N))
    print("%-14s %-2s %-6s %-22s %-16s %s" % ("family", "w", "chi", "arch. limit", "v_p(Lambda_a)", "rate a=1 / a=2"))
    for (lab, kind, par, w, chi, lim) in FAM:
        t0 = time.time()
        try:
            T = towers(p, N, kind, par, w)
        except Exception as e:
            print("%-14s ERROR %s" % (lab, e)); continue
        info = []
        vs = []
        for a in (1, 2):
            if a not in T: continue
            rows = [r for r in T[a] if r is not None]
            ag = [rows[i].agree(rows[i-1]) - min(rows[i].v, rows[i-1].v) for i in range(1, len(rows))]
            info.append(",".join(map(str, ag)))
            vs.append(rows[-1].v)
        print("%-14s %-2d %-6s %-22s %-16s %s   (%.0fs)" %
              (lab, w, chi, lim, str(vs), "  |  ".join(info), time.time()-t0))
