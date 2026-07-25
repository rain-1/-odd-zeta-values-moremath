"""Exact p-adic linear algebra with honest precision tracking, on top of pnum.P.
Used to test ansaetze of the form   (sum_j y_j G_j(a)) * Lambda_a = sum_i x_i F_i(a).
"""
from pnum import P

def solve(rows, rhs, p):
    """Solve the square system rows . x = rhs over Q_p (rows: list of lists of P).
       Pivot on minimal valuation.  Returns (x, ok)."""
    n = len(rows)
    A = [list(r) for r in rows]
    b = list(rhs)
    piv = []
    for c in range(n):
        best, bv = None, None
        for r in range(c, n):
            if A[r][c].is_zero():
                continue
            if bv is None or A[r][c].v < bv:
                best, bv = r, A[r][c].v
        if best is None:
            return None, False
        A[c], A[best] = A[best], A[c]
        b[c], b[best] = b[best], b[c]
        inv = A[c][c].inv()
        A[c] = [x * inv for x in A[c]]
        b[c] = b[c] * inv
        for r in range(n):
            if r == c or A[r][c].is_zero():
                continue
            f = A[r][c]
            A[r] = [A[r][k] - f * A[c][k] for k in range(n)]
            b[r] = b[r] - f * b[c]
    return b, True

def test_ansatz(data, Fs, Gs, p, name="", solve_on=None, verbose=True):
    """data: list of (a, Lambda_a as P).  Fs, Gs: lists of functions a -> P (or Fraction).
       Model:  (sum_j y_j G_j(a)) * L_a  =  sum_i x_i F_i(a),   y_0 := 1  (normalisation).
       Unknowns: x_0..x_{k-1}, y_1..y_{m-1}.   #unknowns = k + m - 1.
       Solve on the first (k+m-1) values of a, verify on the rest."""
    k, m = len(Fs), len(Gs)
    nun = k + m - 1
    def coef_row(a, L):
        # unknown order: x_0..x_{k-1} (coefficient -F_i(a)), y_1..y_{m-1} (coefficient G_j(a)*L)
        row = [-mk(Fs[i](a), p, L.prec) for i in range(k)]
        row += [mk(Gs[j](a), p, L.prec) * L for j in range(1, m)]
        rhsv = -(mk(Gs[0](a), p, L.prec) * L)
        return row, rhsv
    if solve_on is None:
        solve_on = list(range(nun))
    idx = [i for i in solve_on]
    rest = [i for i in range(len(data)) if i not in idx]
    rows, rhs = [], []
    for i in idx:
        a, L = data[i]
        r, v = coef_row(a, L)
        rows.append(r); rhs.append(v)
    sol, ok = solve(rows, rhs, p)
    if not ok:
        if verbose: print("  %-28s SINGULAR" % name)
        return None
    worst = None
    details = []
    for i in rest:
        a, L = data[i]
        r, v = coef_row(a, L)
        res = -v
        for j in range(nun):
            res = res + r[j] * sol[j]
        # available absolute precision of this equation
        ap = min(min(x.v + x.prec for x in r if not x.is_zero()),
                 v.v + v.prec if not v.is_zero() else 10**9)
        got = ap if res.is_zero() else res.v
        # scale: compare to the size of the terms
        sc = min(x.v for x in r if not x.is_zero())
        details.append((a, got - sc, ap - sc))
        if worst is None or got - sc < worst:
            worst = got - sc
    if verbose:
        print("  %-28s solved on a=%s; residual digits (of avail) on rest: %s"
              % (name, [data[i][0] for i in idx],
                 " ".join("a=%s:%d/%d" % d for d in details)))
    return sol, details, worst

def mk(x, p, prec):
    if isinstance(x, P):
        return x
    return P.from_frac(p, x, prec + 4)
