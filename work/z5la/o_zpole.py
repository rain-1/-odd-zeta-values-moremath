"""Exact pole structure of the () block's right-hand side AFTER the seven
standalone blocks have been solved -- i.e. of the object whose preimage the ()
ansatz must contain."""
import sys
import numpy as np
import zla, solve, fastlin, ratrec, ordm, o_scan, o_zero
from solve import Ansatz


def ratrec_at(vals, xs, p, d):
    """rational reconstruction with num,den degrees <= d (no search)."""
    M = len(xs); nc = 2 * (d + 1)
    if M < nc + 2: return None
    A = np.zeros((M, nc), dtype=np.int64)
    for t, x in enumerate(xs):
        xp = 1
        for j in range(d + 1):
            A[t, j] = xp
            A[t, d + 1 + j] = (-vals[t] * xp) % p
            xp = xp * (x % p) % p
    ns = ratrec.nullspace(A, p)
    if not ns: return None
    v = ns[0]
    return ratrec.trim(v[:d + 1]), ratrec.trim(v[d + 1:])


def zero_rhs(which, n, m, dname, slack, p, avec, pts):
    """the () block RHS at the given (k,l) points, using the fitted blocks."""
    D = o_scan.dens(m)[dname]
    dk0 = sum(mu * abs(f[2]) for f, mu in D); dl0 = sum(mu * abs(f[3]) for f, mu in D)
    ans = Ansatz(D, D, dk0 + slack, dl0 + slack, dk0 + slack, dl0 + slack,
                 force_k=0, force_l=0)
    na = m - 2
    nfit = int(1.35 * (ans.nc + na)) + 20
    pdf = ordm.PDm(which, p, n, m, nfit)
    Af = ordm.acols(pdf)
    stand = [j for j in pdf.free if len(pdf.B[j]) > 0]
    zj = [j for j in pdf.free if len(pdf.B[j]) == 0][0]
    Mf = o_scan.scal_mat(pdf, ans)
    rhsS = np.zeros((nfit, len(stand)), dtype=np.int64)
    avec = np.asarray(avec, dtype=np.int64) % p
    for u, j in enumerate(stand):
        rhsS[:, u] = [int(x) for x in
                      (-(Af[j * nfit:(j + 1) * nfit].astype(object) @ avec.astype(object))) % p]
    X, rank, piv, nbad = fastlin.solve(Mf, rhsS, p, nb=64)
    assert nbad == 0, nbad
    # now evaluate at the requested points
    pd = ordm.PDm(which, p, n, m, 0, pts=pts)
    A2 = ordm.acols(pd)
    N = pd.npts
    out = np.zeros(N, dtype=np.int64)
    for t, (k, l) in enumerate(pd.pts):
        acc = 0
        for tt in range(na):
            acc = (acc + int(avec[tt]) * int(A2[zj * N + t, tt])) % p
        acc = (-acc) % p
        gk = int(pd.gk[t]); gl = int(pd.gl[t])
        for u, j in enumerate(stand):
            ck = int(pd.Sk[t, zj, j]); cl = int(pd.Sl[t, zj, j])
            if ck: acc = (acc - gk * ck % p * ans.eval_r(X[:, u], n, k + 1, l, p)) % p
            if cl: acc = (acc - gl * cl % p * ans.eval_s(X[:, u], n, k, l + 1, p)) % p
        out[t] = acc
    return out, ans, X


if __name__ == '__main__':
    p = o_scan.P; n = 5; m = 7
    avec = [1, 1856591, 741434, 2946388, 1875359]
    NS = 340
    for direction in ('k', 'l'):
        if direction == 'k':
            xs = list(range(n + m + 4, n + m + 4 + NS)); lf = 37
            pts = [(x, lf) for x in xs]
            roots = ([('k+1', -1), ('k+2', -2), ('k+3', -3),
                      ('k+l+1', -(lf + 1)), ('k+l+2', -(lf + 2)), ('k+l+3', -(lf + 3)),
                      ('k+l+4', -(lf + 4))]
                     + [('n+k+%d' % j, -(n + j)) for j in range(0, m + 6)]
                     + [('n+%d-k' % j, n + j) for j in range(0, m + 6)]
                     + [('n+k+l+%d' % j, -(n + lf + j)) for j in range(0, m + 4)])
        else:
            xs = list(range(n + m + 4, n + m + 4 + NS)); kf = 41
            pts = [(kf, x) for x in xs]
            roots = ([('l+1', -1), ('l+2', -2), ('l+3', -3),
                      ('k+l+1', -(kf + 1)), ('k+l+2', -(kf + 2)), ('k+l+3', -(kf + 3)),
                      ('k+l+4', -(kf + 4))]
                     + [('n+l+%d' % j, -(n + j)) for j in range(0, m + 6)]
                     + [('n+%d-l' % j, n + j) for j in range(0, m + 6)]
                     + [('n+k+l+%d' % j, -(n + kf + j)) for j in range(0, m + 4)])
        vals, ans, X = zero_rhs('w3', n, m, 'E1', 18, p, avec, pts)
        for d in (60, 80, 100, 120, 150):
            r = ratrec_at([int(v) for v in vals], xs, p, d)
            if r is None: continue
            num, den = r
            fac, rest = ratrec.factor_mult(den, roots, p)
            ok = all(ratrec.polyval(num, x % p, p)
                     == vals[t] * ratrec.polyval(den, x % p, p) % p
                     for t, x in enumerate(xs))
            print('%s-direction  d<=%d : degnum=%d degden=%d  den=%s  unfactored-deg=%d  fits-all=%s'
                  % (direction, d, len(num) - 1, len(den) - 1,
                     '*'.join('%s%s' % (a, '^%d' % c if c > 1 else '')
                              for a, c in fac.items()), len(rest) - 1, ok), flush=True)
            break
