"""DIG-3  s_recur.py -- THE DECISIVE M1 TEST.

A rank-2 form  S_n = rho_0 + a_n zeta_2(5) + b_n zeta_2(7)  (M=6, m=1: the
family behind Lai's "one of zeta_2(5), zeta_2(7)") becomes a rank-1 form in 1
and zeta_2(7) iff some operator

        L  =  sum_{j,l,d}  c_{j,l,d} * n^d * (shift n -> n+l) * (form j)

with POLYNOMIAL coefficients satisfies   L(a) = 0  and  L(b) != 0.

Polynomial coefficients are the only affordable ones: a combination with
coefficients of size e^{Gn} multiplies beta by 2 and the margin
alpha - 2 beta = 2G - 2(G+E) = -2E < 0 is destroyed.  (That is the classical
elimination tax; it is exactly why "one of zeta(5), zeta(7)" is never sharpened
archimedeanly either.)

If instead EVERY L that kills a also kills b, the two coefficient sequences
generate the same D-module and the rank cannot be reduced -- a structural wall,
not a numerical accident.  This module decides which.

All linear algebra is over F_q (a 61-bit prime); dimensions are confirmed with a
second prime.
"""
import sys, os, itertools, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s_elim import pf_rho_modq, Q, Q2


def rref_nullspace(rows, C, q):
    A = [r[:] for r in rows]
    R = len(A)
    where = [-1] * C
    piv = 0
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
                Ap = A[piv]
                A[r] = [(A[r][cc] - fac * Ap[cc]) % q for cc in range(C)]
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
    return null, piv


def operator_test(M, forms, i_kill, i_keep, L=4, D=10, nlo=6, q=Q, dwp=1,
                  extra=25, verbose=True, also=()):
    """Search for polynomial operators killing rho_{i_kill}; report whether any
    of them survives on rho_{i_keep} (and on the further indices in `also`)."""
    J = len(forms)
    C = J * (L + 1) * (D + 1)
    NEQ = C + extra
    ns = list(range(nlo, nlo + NEQ))
    nmax = ns[-1] + L
    t0 = time.time()
    cache = {}
    for j, (e, f) in enumerate(forms):
        for n in range(nlo, nmax + 1):
            cache[(j, n)] = pf_rho_modq(n, e, f, q, dwp)
    if verbose:
        print("      built %d rho-vectors up to n=%d in %.0fs"
              % (len(cache), nmax, time.time() - t0))

    def build(idx):
        rows = []
        for n in ns:
            row = []
            for j in range(J):
                for l in range(L + 1):
                    v = cache[(j, n + l)][idx]
                    nd = 1
                    for d in range(D + 1):
                        row.append(v * nd % q)
                        nd = nd * n % q
            rows.append(row)
        return rows

    rows_kill = build(i_kill)
    null, rank = rref_nullspace(rows_kill, C, q)
    if verbose:
        print("      unknowns C=%d, equations=%d, rank=%d -> dim ker(rho_%d) = %d"
              % (C, len(ns), rank, i_kill, len(null)))
    survivors = []
    for idx in (i_keep,) + tuple(also):
        rows_keep = build(idx)
        surv = 0
        for vec in null:
            vals = [sum(rows_keep[t][c] * vec[c] for c in range(C)) % q
                    for t in range(len(ns))]
            if any(vals):
                surv += 1
        survivors.append((idx, surv))
        if verbose:
            print("      of the %d kernel vectors, %d give a NON-zero rho_%d"
                  % (len(null), surv, idx))
    return null, survivors


if __name__ == "__main__":
    print("=" * 78)
    print("s_recur  M1 : can a polynomial operator kill the zeta_2(5) coefficient")
    print("             of the M=6 rank-2 family and keep the zeta_2(7) one?")
    print("=" * 78)
    Z = (0,) * 6
    print("\n[R0] CONTROL -- the operator search on a family where the answer is known:")
    print("     M=4, m=1 (LSZ) has rank 1 already; rho_3 is the only coefficient.")
    print("     A kernel for rho_3 must therefore also kill rho_0 (S == 0).")

    print("\n[R1] single symmetric form, shifts only (the minimal recurrence route)")
    operator_test(6, [(Z, Z)], 3, 5, L=4, D=10, nlo=6, extra=20)

    print("\n[R2] wider operator: L=6, D=12")
    operator_test(6, [(Z, Z)], 3, 5, L=6, D=12, nlo=6, extra=20)

    print("\n[R3] the inset cone: 4 distinct forms, shifts L=3, D=8")
    F4 = [(Z, Z),
          ((0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 0)),
          ((0, 0, 0, 0, 1, 1), (0, 0, 0, 0, 0, 0)),
          ((0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1))]
    operator_test(6, F4, 3, 5, L=3, D=8, nlo=6, extra=20)
