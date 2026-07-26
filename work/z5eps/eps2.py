"""eps2.py -- generalized mod-p cascade: L1 = a*D1 + b*V1 in the 2-dim null space N1.

Moments in the two per-cell scalars X = D1(cell), Y = V1(cell) are accumulated so
that every cascade equation becomes polynomial in (a,b) and linear in the higher
unknowns g (L2), y (L3), z (L4), w (L5), t3,s3, u4,s4,v4, t5,u5,s5.

Phase 1: E2-solvability condition = conic in (a^2, ab, b^2)  ->  candidate (a:b).
Phase 2: per-candidate linear cascade with null-space tracking.
"""
import sys
from math import comb
from itertools import product

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
import core

NMAX = 34
D1VEC = (0, -3, 1, 2, -2, 2)          # (d_k + d_l) log T
# V1 = [1, 1/2, -1, -1/2, 1, 0]; scale by 2 to clear denominators:
V1VEC = (2, 1, -2, -1, 2, 0)


def rref_solve(A, b, p):
    m = len(A); ncols = len(A[0]) if m else 0
    M = [row[:] + [bb % p] for row, bb in zip(A, b)]
    piv = []; r = 0
    for c in range(ncols):
        pr = next((i for i in range(r, m) if M[i][c] % p), None)
        if pr is None: continue
        M[r], M[pr] = M[pr], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [v * inv % p for v in M[r]]
        for i in range(m):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(v - f * w) % p for v, w in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == m: break
    for i in range(r, m):
        if M[i][ncols] % p:
            return False, None, None, r
    x = [0] * ncols
    for i, c in enumerate(piv): x[c] = M[i][ncols]
    null = []
    for fc in [c for c in range(ncols) if c not in piv]:
        v = [0] * ncols; v[fc] = 1
        for i, c in enumerate(piv): v[c] = (-M[i][fc]) % p
        null.append(v)
    return True, x, null, r


def ratrec(a, M, bound=None):
    a %= M
    if bound is None: bound = int((M // 2) ** 0.5)
    r0, r1, s0, s1 = M, a, 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1, s0, s1 = r1, r0 - q * r1, s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound: return None
    from math import gcd
    if gcd(r1, abs(s1)) != 1: return None
    num, den = (r1, s1) if s1 > 0 else (-r1, -s1)
    return (num, den)


def rr(a, M):
    v = ratrec(a, M)
    if v is None: return '?%d' % (a % M)
    return '%d/%d' % v if v[1] != 1 else '%d' % v[0]


def sweep(p, nmax):
    HM = 3 * nmax + 2
    H = [[0] * (HM + 1) for _ in range(6)]
    for m in range(1, HM + 1):
        im = pow(m, p - 2, p); acc = im
        H[1][m] = (H[1][m - 1] + acc) % p
        for r in range(2, 6):
            acc = acc * im % p
            H[r][m] = (H[r][m - 1] + acc) % p

    IJ5 = [(i, j) for s in range(6) for i in range(s + 1) for j in [s - i]]
    IJ3 = [(i, j) for s in range(4) for i in range(s + 1) for j in [s - i]]
    IJ2 = [(i, j) for s in range(3) for i in range(s + 1) for j in [s - i]]
    IJ1 = [(0, 0), (1, 0), (0, 1)]
    S = dict(Q=[], M1=[], P={}, R2={}, R3={}, R4={}, M5=[], Q22={}, Q23=[])
    for ij in IJ5: S['P'][ij] = []
    for ij in IJ3: S['R2'][ij] = []
    for ij in IJ2: S['R3'][ij] = []
    for ij in IJ1: S['R4'][ij] = []
    for ij in IJ1: S['Q22'][ij] = []

    for n in range(nmax + 1):
        q = 0
        M1 = [0] * 6
        P = {ij: 0 for ij in IJ5}
        R2 = {ij: [0] * 6 for ij in IJ3}
        R3 = {ij: [0] * 6 for ij in IJ2}
        R4 = {ij: [0] * 6 for ij in IJ1}
        M5 = [0] * 6
        Q22 = {ij: [[0] * 6 for _ in range(6)] for ij in IJ1}
        Q23 = [[0] * 6 for _ in range(6)]
        for k in range(n + 1):
            ck = comb(n + k, n) * comb(n, k) ** 2
            for l in range(n + 1):
                t = (ck * comb(n + l, n) * comb(n, l) ** 2
                     * comb(n + k + l, n)) % p
                args = [(n,), (k, l), (n + k, n + l), (n - k, n - l),
                        (k + l,), (n + k + l,)]
                h = [[0] * 6 for _ in range(6)]
                for ci, a in enumerate(args):
                    for r in range(1, 6):
                        h[r][ci] = sum(H[r][x] for x in a) % p
                X = sum(D1VEC[ci] * h[1][ci] for ci in range(6)) % p
                Y = sum(V1VEC[ci] * h[1][ci] for ci in range(6)) % p
                Xp = [1, X, X * X % p, pow(X, 3, p), pow(X, 4, p), pow(X, 5, p)]
                Yp = [1, Y, Y * Y % p, pow(Y, 3, p), pow(Y, 4, p), pow(Y, 5, p)]
                q = (q + t) % p
                for ci in range(6):
                    M1[ci] = (M1[ci] + t * h[1][ci]) % p
                    M5[ci] = (M5[ci] + t * h[5][ci]) % p
                for (i, j) in IJ5:
                    P[(i, j)] = (P[(i, j)] + t * Xp[i] % p * Yp[j]) % p
                for (i, j) in IJ3:
                    txy = t * Xp[i] % p * Yp[j] % p
                    row = R2[(i, j)]
                    for ci in range(6):
                        row[ci] = (row[ci] + txy * h[2][ci]) % p
                for (i, j) in IJ2:
                    txy = t * Xp[i] % p * Yp[j] % p
                    row = R3[(i, j)]
                    for ci in range(6):
                        row[ci] = (row[ci] + txy * h[3][ci]) % p
                for (i, j) in IJ1:
                    txy = t * Xp[i] % p * Yp[j] % p
                    row = R4[(i, j)]
                    for ci in range(6):
                        row[ci] = (row[ci] + txy * h[4][ci]) % p
                    m22 = Q22[(i, j)]
                    for ci in range(6):
                        v = txy * h[2][ci] % p
                        for cj in range(6):
                            m22[ci][cj] = (m22[ci][cj] + v * h[2][cj]) % p
                for ci in range(6):
                    v = t * h[2][ci] % p
                    for cj in range(6):
                        Q23[ci][cj] = (Q23[ci][cj] + v * h[3][cj]) % p
        S['Q'].append(q); S['M1'].append(M1); S['M5'].append(M5)
        for ij in IJ5: S['P'][ij].append(P[ij])
        for ij in IJ3: S['R2'][ij].append(R2[ij])
        for ij in IJ2: S['R3'][ij].append(R3[ij])
        for ij in IJ1: S['R4'][ij].append(R4[ij])
        for ij in IJ1: S['Q22'][ij].append(Q22[ij])
        S['Q23'].append(Q23)
    return S


def phase1(S, p, nmax):
    """E2 obstruction: for which (a:b) is  M2 g = -1/2 (a^2 G20 + 2ab G11 + b^2 G02)
    solvable?  Row-reduce [M2 | G20 G11 G02]; zero-M2 rows give the conic."""
    A = [S['R2'][(0, 0)][n][:] for n in range(nmax + 1)]
    aug = [[S['P'][(2, 0)][n], S['P'][(1, 1)][n], S['P'][(0, 2)][n]]
           for n in range(nmax + 1)]
    m = len(A)
    M = [A[i][:] + aug[i][:] for i in range(m)]
    r = 0
    for c in range(6):
        pr = next((i for i in range(r, m) if M[i][c] % p), None)
        if pr is None: continue
        M[r], M[pr] = M[pr], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [v * inv % p for v in M[r]]
        for i in range(m):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(v - f * w) % p for v, w in zip(M[i], M[r])]
        r += 1
    print('phase1: rank(M2) =', r)
    conds = []
    for i in range(r, m):
        row = M[i][6:]
        if any(v % p for v in row):
            conds.append(row)
    # rank of the condition system on (alpha, beta2, gamma) with
    # G-terms entering as alpha*G20 + beta2*G11 + gamma*G02, beta2 = 2ab
    ok, x, null, rc = rref_solve(conds, [0] * len(conds), p) if conds else (True, [0]*3, [[1,0,0],[0,1,0],[0,0,1]], 0)
    print('phase1: conic condition rank = %d, null dim = %d' % (rc, len(null)))
    return null, rc


def sqrt_mod(a, p):
    a %= p
    if a == 0: return 0
    if pow(a, (p - 1) // 2, p) != 1: return None
    if p % 4 == 3: return pow(a, (p + 1) // 4, p)
    return None


def candidates_ab(null, rc, p):
    """Solve for (a:b): alpha = a^2, beta2 = 2ab, gamma = b^2 subject to the
    linear conditions; Veronese: beta2^2 = 4 alpha gamma."""
    cands = []
    if rc == 0:
        return 'ALL'
    if rc >= 3:
        # only (a,b) = 0 satisfies -> L1 = 0 branch only
        return []
    if rc == 2:
        v = null[0]  # (alpha, beta2, gamma) up to scale
        al, b2, ga = v
        if (b2 * b2 - 4 * al * ga) % p != 0:
            return []
        # recover (a:b): if al != 0: a=1 ... scale so alpha = a^2
        if al % p:
            # b/a = b2/(2 al)
            ba = b2 * pow(2 * al % p, p - 2, p) % p
            cands.append((1, ba))
        elif ga % p:
            cands.append((0, 1))
        else:
            cands.append(None)
        return cands
    if rc == 1:
        # one condition c0*al + c1*b2 + c2*ga = 0 with al=a^2,b2=2ab,ga=b^2:
        # c0 a^2 + 2 c1 ab + c2 b^2 = 0 -> quadratic in a/b
        # find the single condition row: reconstruct from null space of dim 2:
        # cross product of the two null vectors
        u, v = null
        c = [(u[1] * v[2] - u[2] * v[1]) % p,
             (u[2] * v[0] - u[0] * v[2]) % p,
             (u[0] * v[1] - u[1] * v[0]) % p]
        c0, c1, c2 = c
        if c0 % p == 0:
            cands.append((0, 1))
            if c1 % p: cands.append((1, (-c2) * pow(2 * c1, p - 2, p) % p))
        else:
            disc = (c1 * c1 - c0 * c2) % p       # (2c1)^2 - 4 c0 c2 over 4
            s = sqrt_mod(disc, p)
            if s is not None:
                for sg in ({s, (-s) % p}):
                    a_over_b = (-c1 + sg) * pow(c0, p - 2, p) % p
                    cands.append((a_over_b, 1))
        return cands
    return []


def linear_cascade(S, p, nmax, a, b, verbose=True, allow_v4=True):
    lad = core.ladders()
    fm = lambda fr: fr.numerator % p * pow(fr.denominator % p, p - 2, p) % p
    Qs = [fm(lad['Q'][n]) for n in range(nmax + 1)]
    Phs = [fm(lad['Ph'][n]) for n in range(nmax + 1)]
    Ps = [fm(lad['P'][n]) for n in range(nmax + 1)]
    inv = lambda x: pow(x, p - 2, p)
    i2, i6, i24, i120 = inv(2), inv(6), inv(24), inv(120)
    P_, R2, R3, R4 = S['P'], S['R2'], S['R3'], S['R4']
    Q22, Q23, M5 = S['Q22'], S['Q23'], S['M5']
    out = {'a': a, 'b': b}

    def pab(i, j):  # a^i b^j
        return pow(a, i, p) * pow(b, j, p) % p

    # ---- E2 ----
    A = [R2[(0, 0)][n][:] for n in range(nmax + 1)]
    rhs = [(-i2 * (pab(2, 0) * P_[(2, 0)][n] + 2 * pab(1, 1) * P_[(1, 1)][n]
                   + pab(0, 2) * P_[(0, 2)][n])) % p for n in range(nmax + 1)]
    ok, g0, N2, r2 = rref_solve(A, rhs, p)
    if verbose: print('  E2: consistent=%s rank=%d nulldim=%d' % (ok, r2, len(N2) if ok else -1))
    if not ok: out['E2'] = 'FAIL'; return out
    dN2 = len(N2)

    # ---- E3: unknowns [lam(dN2), y(6), t3, s3] ----
    def L1L2vec(gv, n):    # sum_c g_c (a R2_10 + b R2_01)[c]
        return sum(gv[c] * (a * R2[(1, 0)][n][c] + b * R2[(0, 1)][n][c])
                   for c in range(6)) % p

    L1cube = lambda n: (pab(3, 0) * P_[(3, 0)][n] + 3 * pab(2, 1) * P_[(2, 1)][n]
                        + 3 * pab(1, 2) * P_[(1, 2)][n] + pab(0, 3) * P_[(0, 3)][n]) % p
    A, rhs = [], []
    for n in range(nmax + 1):
        row = [L1L2vec(N2[i], n) for i in range(dN2)]
        row += [S['R3'][(0, 0)][n][c] for c in range(6)]
        row += [(-Phs[n]) % p, (-Qs[n]) % p]
        A.append([v % p for v in row])
        rhs.append((-(L1L2vec(g0, n) + i6 * L1cube(n))) % p)
    ok, x3, N3, r3 = rref_solve(A, rhs, p)
    if verbose: print('  E3: consistent=%s rank=%d/%d nulldim=%d' % (ok, r3, dN2 + 8, len(N3) if ok else -1))
    if not ok: out['E3'] = 'FAIL'; return out
    lam, y0 = x3[:dN2], x3[dN2:dN2 + 6]
    t3, s3 = x3[dN2 + 6], x3[dN2 + 7]
    g = [(g0[c] + sum(lam[i] * N2[i][c] for i in range(dN2))) % p for c in range(6)]
    out.update(g=g, y=y0, t3=t3, s3=s3, N3dim=len(N3))
    if verbose:
        print('  E3: t3 = %s   s3 = %s' % (rr(t3, p), rr(s3, p)))
        print('  E3: g =', [rr(v, p) for v in g])
        print('  E3: y =', [rr(v, p) for v in y0])
        if N3:
            print('  E3: null dirs (lam|y|t3|s3):')
            for v in N3: print('      ', [rr(u, p) for u in v])

    # ---- E4: unknowns [z(6), u4, s4 (,v4)] ----
    ncol = 9 if allow_v4 else 8
    A, rhs = [], []
    for n in range(nmax + 1):
        row = [S['R4'][(0, 0)][n][c] for c in range(6)]
        row += [(-Phs[n]) % p, (-Qs[n]) % p] + ([(-Ps[n]) % p] if allow_v4 else [])
        A.append(row)
        cst = 0
        for c in range(6):
            cst += y0[c] * (a * R3[(1, 0)][n][c] + b * R3[(0, 1)][n][c])   # L1 L3
            cst += i2 * g[c] % p * (pab(2, 0) * R2[(2, 0)][n][c]
                                    + 2 * pab(1, 1) * R2[(1, 1)][n][c]
                                    + pab(0, 2) * R2[(0, 2)][n][c]) % p    # L1^2 L2 /2
        q22 = 0
        for c in range(6):
            for cc in range(6):
                q22 += g[c] * g[cc] % p * Q22[(0, 0)][n][c][cc]
        L1q = (pab(4, 0) * P_[(4, 0)][n] + 4 * pab(3, 1) * P_[(3, 1)][n]
               + 6 * pab(2, 2) * P_[(2, 2)][n] + 4 * pab(1, 3) * P_[(1, 3)][n]
               + pab(0, 4) * P_[(0, 4)][n]) % p
        cst = (cst + i2 * q22 + i24 * L1q) % p
        rhs.append((-cst) % p)
    ok, x4, N4, r4 = rref_solve(A, rhs, p)
    if verbose: print('  E4: consistent=%s rank=%d/%d nulldim=%d' % (ok, r4, ncol, len(N4) if ok else -1))
    if not ok: out['E4'] = 'FAIL'; return out
    z0 = x4[:6]; u4, s4 = x4[6], x4[7]; v4 = x4[8] if allow_v4 else 0
    out.update(z=z0, u4=u4, s4=s4, v4=v4)
    if verbose:
        print('  E4: u4 = %s  s4 = %s  v4 = %s' % (rr(u4, p), rr(s4, p), rr(v4, p)))
        print('  E4: z =', [rr(v, p) for v in z0])

    # ---- E5: unknowns [w(6), t5, u5, s5] ----
    A, rhs = [], []
    for n in range(nmax + 1):
        row = [M5[n][c] for c in range(6)]
        row += [(-Ps[n]) % p, (-Phs[n]) % p, (-Qs[n]) % p]
        A.append(row)
        cst = 0
        for c in range(6):
            cst += z0[c] * (a * R4[(1, 0)][n][c] + b * R4[(0, 1)][n][c])   # L1 L4
            cst += i2 * y0[c] % p * (pab(2, 0) * R3[(2, 0)][n][c]
                                     + 2 * pab(1, 1) * R3[(1, 1)][n][c]
                                     + pab(0, 2) * R3[(0, 2)][n][c]) % p   # L1^2 L3/2
            cst += i6 * g[c] % p * (pab(3, 0) * R2[(3, 0)][n][c]
                                    + 3 * pab(2, 1) * R2[(2, 1)][n][c]
                                    + 3 * pab(1, 2) * R2[(1, 2)][n][c]
                                    + pab(0, 3) * R2[(0, 3)][n][c]) % p    # L1^3 L2/6
        m23 = 0
        for c2 in range(6):
            for c3 in range(6):
                m23 += g[c2] * y0[c3] % p * Q23[n][c2][c3]                 # L2 L3
        m221 = 0
        for c in range(6):
            for cc in range(6):
                m221 += g[c] * g[cc] % p * (a * Q22[(1, 0)][n][c][cc]
                                            + b * Q22[(0, 1)][n][c][cc]) % p  # L1 L2^2
        L15 = sum(comb(5, i) * pab(i, 5 - i) % p * P_[(i, 5 - i)][n]
                  for i in range(6)) % p
        cst = (cst + m23 + i2 * m221 + i120 * L15) % p
        rhs.append((-cst) % p)
    ok, x5, N5, r5 = rref_solve(A, rhs, p)
    if verbose: print('  E5: consistent=%s rank=%d/9 nulldim=%d' % (ok, r5, len(N5) if ok else -1))
    if not ok: out['E5'] = 'FAIL'; return out
    w0 = x5[:6]; t5, u5, s5 = x5[6], x5[7], x5[8]
    out.update(w=w0, t5=t5, u5=u5, s5=s5)
    if verbose:
        print('  E5: t5 = %s  u5 = %s  s5 = %s' % (rr(t5, p), rr(u5, p), rr(s5, p)))
        print('  E5: w =', [rr(v, p) for v in w0])
    return out


if __name__ == '__main__':
    for p in (2147483647,):
        print('=' * 70); print('prime', p)
        S = sweep(p, NMAX)
        print('sweep done; Q_1 =', S['Q'][1])
        null, rc = phase1(S, p, NMAX)
        cands = candidates_ab(null, rc, p)
        print('phase1 candidates (a:b):', cands if cands != 'ALL' else 'ALL of P^1')
        todo = []
        if cands == 'ALL':
            # sample a few directions incl. the distinguished ones
            todo = [(1, 0), (0, 1), (1, 1), (2, 3)]
        else:
            todo = [c for c in cands if c]
        # always also test the L1 = 0 branch as control (expect E3 FAIL):
        print('-' * 50); print('branch L1 = 0 (control; expect E3 inconsistent)')
        linear_cascade(S, p, NMAX, 0, 0)
        for (a, b) in todo:
            print('-' * 50)
            print('branch (a, b) = (%s, %s)' % (rr(a, p), rr(b, p)))
            linear_cascade(S, p, NMAX, a, b)
