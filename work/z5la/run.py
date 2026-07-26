"""Joint solve of the whole certificate system at one (n,p), plus an
independent residual check at fresh points."""
import numpy as np
import zla, solve, joint, fastlin
from solve import Ansatz, dval


def build_joint(pd, A, mord=3, free_d=False):
    return joint.build(pd, A, mord, free_d)


def check(pd, A, X, npt=25, seed=4242):
    """verify the module identity at fresh random points"""
    p, n, J = pd.p, pd.n, pd.J
    F = pd.F
    nc = A.nc
    rng = np.random.default_rng(seed)
    bad = 0; tested = 0
    guard = 0
    while tested < npt and guard < 5000:
        guard += 1
        k = int(rng.integers(2, p - 2)); l = int(rng.integers(2, p - 2))
        try:
            b = zla.el_to_vec(F, pd.B, zla.rhs_element(F, pd.w, n, k, l))
            gk = zla.gk_val(F, n, k, l); gl = zla.gl_val(F, n, k, l)
            Sk = zla.shift_matrix(F, pd.B, 'k', n, k, l)
            Sl = zla.shift_matrix(F, pd.B, 'l', n, k, l)
            xs = [X[j * nc:(j + 1) * nc] for j in range(J)]
            rv = [A.eval_r(x, n, k + 1, l, p) for x in xs]
            r0 = [A.eval_r(x, n, k, l, p) for x in xs]
            sv = [A.eval_s(x, n, k, l + 1, p) for x in xs]
            s0 = [A.eval_s(x, n, k, l, p) for x in xs]
        except ZeroDivisionError:
            continue
        tested += 1
        for i in range(J):
            acc = 0
            for j in range(J):
                acc = (acc + gk * Sk[j][i] % p * rv[j] + gl * Sl[j][i] % p * sv[j]) % p
            if (acc - r0[i] - s0[i] - b[i]) % p: bad += 1
    return tested, bad


def one(which, p, n, deg, npts, force=(1, 1), D=(), nb=64, verbose=True,
        docheck=True, seed=12345):
    A = Ansatz(list(D), list(D), deg, deg, deg, deg,
               force_k=force[0], force_l=force[1])
    pd = solve.PointData(which, p, n, npts=npts, seed=seed)
    M, rhs, ncols = joint.build(pd, A)
    X, rank, piv, nbad = fastlin.solve(M, rhs, p, nb=nb)
    out = dict(A=A, pd=pd, X=X, rank=rank, piv=piv, nbad=nbad, ncols=ncols,
               rows=M.shape[0])
    if docheck and nbad == 0:
        out['check'] = check(pd, A, X)
    if verbose:
        print('%s p=%d n=%-3d deg=%d nc=%d cols=%d rows=%d rank=%d nbad=%d %s'
              % (which, p, n, deg, A.nc, ncols, M.shape[0], rank, nbad,
                 out.get('check', '')))
    return out
