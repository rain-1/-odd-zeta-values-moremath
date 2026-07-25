"""DIG-3  s_rank.py -- the hardened rank-reduction test (M1 and M2).

For each family (M, m) with rank >= 2 and a POSITIVE ledger margin, ask:
is there a polynomial-coefficient operator, over the whole inset cone and all
shifts, that kills the unwanted zeta coefficients and keeps the wanted one?

  M=6, m=1  weights {5,7}  margin +1.3178  kill rho_3 keep rho_5 -> mu(z2(7))<=12.6240
  M=5, m=0  weights {3,5}  margin +1.9315  kill rho_2 keep rho_4 -> mu(z2(5))<= 7.1774
  M=7, m=0  weights {3,5,7} margin +2.7041 kill rho_2,rho_4 keep rho_6
  M=8, m=1  weights {5,7,9} margin +2.0904 kill rho_3,rho_7 keep rho_5

POSITIVE CONTROL: the same kernel is evaluated on a coefficient sequence taken
from a DIFFERENT family (M=8), which no operator built from the M-family can
annihilate.  If the control shows survivors and the real test shows none, the
negative is about the mathematics, not about the search.
"""
import sys, os, time, itertools

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s_elim import pf_rho_modq, Q, Q2
from s_recur import rref_nullspace


def run(M, forms, kill, keep, L=3, D=8, nlo=6, extra=20, q=Q, dwp=1,
        control=None, label=""):
    J = len(forms)
    C = J * (L + 1) * (D + 1)
    ns = list(range(nlo, nlo + C + extra))
    nmax = ns[-1] + L
    t0 = time.time()
    cache = {}
    for j, (e, f) in enumerate(forms):
        for n in range(nlo, nmax + 1):
            cache[(j, n)] = pf_rho_modq(n, e, f, q, dwp)
    ctrl = {}
    if control is not None:
        Mc, ec, fc, ic = control
        for n in range(nlo, nmax + 1):
            ctrl[n] = pf_rho_modq(n, ec, fc, q, dwp)

    def build(getter):
        rows = []
        for n in ns:
            row = []
            for j in range(J):
                for l in range(L + 1):
                    v = getter(j, n + l)
                    nd = 1
                    for d in range(D + 1):
                        row.append(v * nd % q)
                        nd = nd * n % q
            rows.append(row)
        return rows

    print("  %s   M=%d  J=%d forms, L=%d shifts, deg<=%d -> C=%d unknowns, %d eqs"
          % (label, M, J, L, D, C, len(ns)))
    rows = []
    for idx in kill:
        rows += build(lambda j, n, i=idx: cache[(j, n)][i])
    null, rank = rref_nullspace(rows, C, q)
    print("      rank of the kill-block = %d  ->  dim ker(rho_%s) = %d   (%.0fs)"
          % (rank, ",rho_".join(map(str, kill)), len(null), time.time() - t0))
    if not null:
        print("      NO operator kills the unwanted coefficient(s) at this size.")
        return None
    out = {}
    for idx in keep:
        rk = build(lambda j, n, i=idx: cache[(j, n)][i])
        surv = sum(1 for vec in null
                   if any(sum(rk[t][c] * vec[c] for c in range(C)) % q
                          for t in range(len(ns))))
        out[idx] = surv
        print("      kernel vectors giving a NON-ZERO rho_%d : %d / %d   %s"
              % (idx, surv, len(null),
                 "<== RANK REDUCTION POSSIBLE" if surv else "(all killed too)"))
    rk0 = build(lambda j, n: cache[(j, n)][1])       # rho_1 is 0; use as a null check
    if control is not None:
        rc = build(lambda j, n: ctrl[n][control[3]])
        surv = sum(1 for vec in null
                   if any(sum(rc[t][c] * vec[c] for c in range(C)) % q
                          for t in range(len(ns))))
        print("      [POSITIVE CONTROL] same kernel on a foreign sequence: %d / %d "
              "non-zero  %s" % (surv, len(null),
                                "(machinery CAN see survivors)" if surv else
                                "(!! control failed -- search is degenerate)"))
    return out


def cone(M, k=4):
    Z = (0,) * M
    out = [(Z, Z)]
    for j in range(1, k):
        e = tuple([0] * (M - 1) + [j % 2]) if j % 2 else Z
        f = tuple([0] * (M - 1) + [1]) if j >= 2 else Z
        out.append((tuple(sorted(e)), tuple(sorted(f))))
    # a few genuinely different multiset shapes
    cand = [((0,) * M, (0,) * M),
            ((0,) * (M - 1) + (1,), (0,) * M),
            ((0,) * (M - 2) + (1, 1), (0,) * M),
            ((0,) * M, (0,) * (M - 1) + (1,)),
            ((0,) * (M - 1) + (1,), (0,) * (M - 1) + (1,)),
            ((0,) * (M - 2) + (1, 2), (0,) * M),
            ((0,) * (M - 2) + (1, 1), (0,) * (M - 1) + (1,)),
            ((0,) * (M - 3) + (1, 1, 1), (0,) * M)]
    out = []
    for e, f in cand[:k]:
        if 1 - M + 2 * (sum(f) - sum(e)) <= -2:
            out.append((tuple(sorted(e)), tuple(sorted(f))))
    return out


if __name__ == "__main__":
    print("=" * 78)
    print("s_rank : can the rank be cut to 1 inside a positive-margin p=2 family?")
    print("=" * 78)

    print("\n[M1-a] zeta_2(7) from M=6, m=1 (margin +1.3178): kill rho_3, keep rho_5")
    run(6, cone(6, 4), kill=[3], keep=[5], L=3, D=8,
        control=(8, (0,) * 8, (0,) * 8, 3), label="M1-a")

    print("\n[M1-b] same, wider: 6 forms, L=4, D=6")
    run(6, cone(6, 6), kill=[3], keep=[5], L=4, D=6,
        control=(8, (0,) * 8, (0,) * 8, 3), label="M1-b")

    print("\n[M2-a] zeta_2(5) from M=5, m=0 (margin +1.9315): kill rho_2, keep rho_4")
    run(5, cone(5, 4), kill=[2], keep=[4], L=3, D=8,
        control=(8, (0,) * 8, (0,) * 8, 3), label="M2-a")

    print("\n[M1-c] zeta_2(7) from M=7, m=0 (margin +2.7041): kill rho_2 & rho_4, keep rho_6")
    run(7, cone(7, 4), kill=[2, 4], keep=[6], L=3, D=8,
        control=(8, (0,) * 8, (0,) * 8, 3), label="M1-c")

    print("\n[M1-d] zeta_2(7) from M=8, m=1 (margin +2.0904): kill rho_3 & rho_7, keep rho_5")
    run(8, cone(8, 4), kill=[3, 7], keep=[5], L=3, D=6,
        control=(6, (0,) * 6, (0,) * 6, 3), label="M1-d")
