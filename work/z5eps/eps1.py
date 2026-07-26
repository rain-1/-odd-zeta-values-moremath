"""eps1.py -- mod-p search for a one-parameter Gamma-deformation of the BZ summand.

Space searched (the exact analogue of APERY_DEFECT sec 7.1, per-letter Pochhammer):
  T_eps = T * prod_L exp( sum_m eps^m ((-1)^(m-1)/m) e_m(L) H^(m)_L ),
with L over the nine bare letters of T and k<->l symmetry imposed:
  classes  0:n   1:{k,l}   2:{n+k,n+l}   3:{n-k,n-l}   4:{k+l}   5:{n+k+l}
Unknowns: e_m(class) in Q for m = 1..5  (30 rationals; e_1 pinned first).

Necessary + sufficient cascade on S(eps) = sum_{k,l} T_eps:
  [eps^1]S = 0            (E1)  -> e_1 in null space N1 of the 6 weight-1 sums
  [eps^2]S = 0            (E2)
  [eps^3]S = t3*Phat + s3*Q     (E3)
  [eps^4]S = u4*Phat + s4*Q + v4*P   (E4, span membership)
  [eps^5]S = t5*P + u5*Phat + s5*Q   (E5), t5 != 0 wanted.

All linear algebra over F_p at two 31-bit primes; solutions CRT-combined and
rational-reconstructed.  Exact-Q verification is eps2.py's job.
"""
import sys, json
from math import comb

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
import core

PRIMES = (2147483647, 2147483629)
NMAX = 34          # rows n = 0..NMAX per order


# ---------------- F_p linear algebra ----------------
def rref_solve(A, b, p):
    """Solve A x = b over F_p.  Returns (consistent, x_particular, null_basis, rank)."""
    m = len(A)
    ncols = len(A[0]) if m else 0
    M = [row[:] + [bb % p] for row, bb in zip(A, b)]
    piv_cols = []
    r = 0
    for c in range(ncols):
        pr = None
        for i in range(r, m):
            if M[i][c] % p:
                pr = i
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [(v * inv) % p for v in M[r]]
        for i in range(m):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(v - f * w) % p for v, w in zip(M[i], M[r])]
        piv_cols.append(c)
        r += 1
        if r == m:
            break
    # consistency
    for i in range(r, m):
        if M[i][ncols] % p:
            return False, None, None, r
    x = [0] * ncols
    for i, c in enumerate(piv_cols):
        x[c] = M[i][ncols]
    null = []
    free = [c for c in range(ncols) if c not in piv_cols]
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, c in enumerate(piv_cols):
            v[c] = (-M[i][fc]) % p
        null.append(v)
    return True, x, null, r


# ---------------- the sweep ----------------
def sweep(p, nmax):
    """Accumulate all per-n sums needed by the cascade, mod p."""
    HM = 3 * nmax + 2
    H = [[0] * (HM + 1) for _ in range(6)]      # H[r][m], r=1..5
    for m in range(1, HM + 1):
        im = pow(m, p - 2, p)
        acc = im
        H[1][m] = (H[1][m - 1] + acc) % p
        for r in range(2, 6):
            acc = acc * im % p
            H[r][m] = (H[r][m - 1] + acc) % p

    d1 = None   # filled by caller after N1 known; here use candidate then verify
    D1VEC = (0, -3, 1, 2, -2, 2)   # (d/dk + d/dl) log T, class basis

    Z6 = lambda: [0] * 6
    S = dict(
        Q=[], M1=[], M2=[], M3=[], M4=[], M5=[],
        G2=[], G3=[], G4=[], G5=[],
        C21=[], C31=[], C41=[], C211=[], C311=[], C2111=[],
        C22=[], C23=[], C221=[],
    )
    for n in range(nmax + 1):
        q = 0
        M = [Z6() for _ in range(6)]            # M[r] r=1..5
        G2 = G3 = G4 = G5 = 0
        C21, C31, C41 = Z6(), Z6(), Z6()
        C211, C311, C2111 = Z6(), Z6(), Z6()
        C22 = [[0] * 6 for _ in range(6)]
        C23 = [[0] * 6 for _ in range(6)]
        C221 = [[0] * 6 for _ in range(6)]
        for k in range(n + 1):
            ck = comb(n + k, n) * comb(n, k) ** 2
            for l in range(n + 1):
                t = (ck * comb(n + l, n) * comb(n, l) ** 2
                     * comb(n + k + l, n)) % p
                args = (n, (k, l), (n + k, n + l), (n - k, n - l),
                        (k + l,), (n + k + l,))
                h = [[0] * 6 for _ in range(6)]   # h[r][class]
                for ci, a in enumerate(args):
                    if isinstance(a, tuple):
                        for r in range(1, 6):
                            s = 0
                            for aa in a:
                                s += H[r][aa]
                            h[r][ci] = s % p
                    else:
                        for r in range(1, 6):
                            h[r][ci] = H[r][a]
                d1v = 0
                for ci in range(6):
                    d1v += D1VEC[ci] * h[1][ci]
                d1v %= p
                q = (q + t) % p
                td = t * d1v % p
                td2 = td * d1v % p
                td3 = td2 * d1v % p
                td4 = td3 * d1v % p
                G2 = (G2 + td2) % p
                G3 = (G3 + td3) % p
                G4 = (G4 + td4) % p
                G5 = (G5 + td4 * d1v) % p
                for ci in range(6):
                    h2c, h3c = h[2][ci], h[3][ci]
                    for r in range(1, 6):
                        M[r][ci] = (M[r][ci] + t * h[r][ci]) % p
                    C21[ci] = (C21[ci] + td * h2c) % p
                    C31[ci] = (C31[ci] + td * h3c) % p
                    C41[ci] = (C41[ci] + td * h[4][ci]) % p
                    C211[ci] = (C211[ci] + td2 * h2c) % p
                    C311[ci] = (C311[ci] + td2 * h3c) % p
                    C2111[ci] = (C2111[ci] + td3 * h2c) % p
                    th2 = t * h2c % p
                    tdh2 = td * h2c % p
                    for cj in range(6):
                        C22[ci][cj] = (C22[ci][cj] + th2 * h[2][cj]) % p
                        C23[ci][cj] = (C23[ci][cj] + th2 * h[3][cj]) % p
                        C221[ci][cj] = (C221[ci][cj] + tdh2 * h[2][cj]) % p
        S['Q'].append(q)
        for r in range(1, 6):
            S['M%d' % r].append(M[r])
        S['G2'].append(G2); S['G3'].append(G3)
        S['G4'].append(G4); S['G5'].append(G5)
        S['C21'].append(C21); S['C31'].append(C31); S['C41'].append(C41)
        S['C211'].append(C211); S['C311'].append(C311); S['C2111'].append(C2111)
        S['C22'].append(C22); S['C23'].append(C23); S['C221'].append(C221)
    return S


def frac_mod(fr, p):
    return fr.numerator % p * pow(fr.denominator % p, p - 2, p) % p


def cascade(p, nmax, S, verbose=True):
    lad = core.ladders()
    Qs = [frac_mod(lad['Q'][n], p) for n in range(nmax + 1)]
    Phs = [frac_mod(lad['Ph'][n], p) for n in range(nmax + 1)]
    Ps = [frac_mod(lad['P'][n], p) for n in range(nmax + 1)]
    assert S['Q'] == Qs, 'sweep Q mismatch vs ladder'
    inv2 = pow(2, p - 2, p)
    inv6 = pow(6, p - 2, p)
    inv24 = pow(24, p - 2, p)
    inv120 = pow(120, p - 2, p)
    out = {}

    # ---- E1: null space of M1 ----
    A = [S['M1'][n] for n in range(nmax + 1)]
    ok, x, null, r = rref_solve(A, [0] * len(A), p)
    if verbose:
        print('E1: rank(M1) = %d of 6, null dim = %d' % (r, len(null)))
        for v in null:
            print('    null vec:', v)
    out['N1'] = null
    # check candidate D1VEC is in the null space (it should BE the null space)
    D1VEC = [0, -3, 1, 2, -2, 2]
    resid = [sum(D1VEC[c] * S['M1'][n][c] for c in range(6)) % p
             for n in range(nmax + 1)]
    d1_null = all(v == 0 for v in resid)
    print('E1: candidate (d_k+d_l)logT vector [0,-3,1,2,-2,2] is null:', d1_null)
    if not d1_null or len(null) != 1:
        print('E1 STRUCTURE UNEXPECTED -- stopping for inspection')
        return out

    # ---- E2: M2 . g = -1/2 G2 ----
    A = [S['M2'][n] for n in range(nmax + 1)]
    b = [(-inv2 * S['G2'][n]) % p for n in range(nmax + 1)]
    ok, g0, N2, r2 = rref_solve(A, b, p)
    print('E2: rank(M2) = %d of 6, consistent = %s, null dim = %d, excess eq = %d'
          % (r2, ok, len(N2) if ok else -1, (nmax + 1) - r2))
    if not ok:
        # measure the deficiency: how far is -G2/2 from the span?
        out['E2'] = 'INCONSISTENT'
        return out
    print('E2: g0 =', g0)
    out['g0'], out['N2'] = g0, N2

    # ---- E3: unknowns [lam(dim N2), y(6), t3, s3] ----
    dN2 = len(N2)
    nunk3 = dN2 + 8
    A, b = [], []
    for n in range(nmax + 1):
        row = [0] * nunk3
        for i in range(dN2):
            row[i] = sum(N2[i][c] * S['C21'][n][c] for c in range(6)) % p
        for c in range(6):
            row[dN2 + c] = S['M3'][n][c]
        row[dN2 + 6] = (-Phs[n]) % p
        row[dN2 + 7] = (-Qs[n]) % p
        A.append(row)
        cst = (sum(g0[c] * S['C21'][n][c] for c in range(6)) + inv6 * S['G3'][n]) % p
        b.append((-cst) % p)
    ok, x3, N3, r3 = rref_solve(A, b, p)
    print('E3: rank = %d of %d, consistent = %s, null dim = %d, excess eq = %d'
          % (r3, nunk3, ok, len(N3) if ok else -1, (nmax + 1) - r3))
    if not ok:
        out['E3'] = 'INCONSISTENT'
        return out
    lam = x3[:dN2]
    y0 = x3[dN2:dN2 + 6]
    t3, s3 = x3[dN2 + 6], x3[dN2 + 7]
    print('E3: t3 = %d  s3 = %d   (mod p; t3 as fraction ~ %s)' % (t3, s3, ratrec(t3, p)))
    print('E3: y0 =', y0)
    print('E3: lam =', lam)
    if N3:
        print('E3: null basis:')
        for v in N3:
            print('    ', v)
    # fold lam back into g
    g = [(g0[c] + sum(lam[i] * N2[i][c] for i in range(dN2))) % p for c in range(6)]
    out['g'], out['y0'], out['t3'], out['s3'], out['N3'] = g, y0, t3, s3, N3
    # NOTE: if N3 has null directions touching lam, g is not unique; report and
    # continue with this representative, flag for E4/E5 caveat.
    lam_free = any(any(v[i] % p for i in range(dN2)) for v in N3)
    y_free = any(any(v[dN2 + c] % p for c in range(6)) for v in N3)
    print('E3: null moves g:', lam_free, '  null moves y:', y_free)

    # ---- E4: unknowns [z(6), u4, s4, v4]  (freeze g, y at representative) ----
    nunk4 = 9
    A, b = [], []
    for n in range(nmax + 1):
        row = [0] * nunk4
        for c in range(6):
            row[c] = S['M4'][n][c]
        row[6] = (-Phs[n]) % p
        row[7] = (-Qs[n]) % p
        row[8] = (-Ps[n]) % p
        A.append(row)
        cst = 0
        for c in range(6):
            cst += y0[c] * S['C31'][n][c]
            cst += inv2 * g[c] % p * S['C211'][n][c]
        gc22 = 0
        for c in range(6):
            for cc in range(6):
                gc22 += g[c] * g[cc] % p * S['C22'][n][c][cc]
        cst = (cst + inv2 * gc22 + inv24 * S['G4'][n]) % p
        b.append((-cst) % p)
    ok, x4, N4, r4 = rref_solve(A, b, p)
    print('E4: rank = %d of %d, consistent = %s, null dim = %d, excess eq = %d'
          % (r4, nunk4, ok, len(N4) if ok else -1, (nmax + 1) - r4))
    if ok:
        z0 = x4[:6]
        u4, s4, v4 = x4[6], x4[7], x4[8]
        print('E4: z0 =', z0)
        print('E4: u4 = %d s4 = %d v4 = %d  (u4 ~ %s, v4 ~ %s)'
              % (u4, s4, v4, ratrec(u4, p), ratrec(v4, p)))
        out['z0'], out['u4s4v4'] = z0, (u4, s4, v4)
    else:
        out['E4'] = 'INCONSISTENT'
        z0 = None

    # ---- E5: unknowns [w(6), t5, u5, s5] ----
    if z0 is None:
        return out
    nunk5 = 9
    A, b = [], []
    for n in range(nmax + 1):
        row = [0] * nunk5
        for c in range(6):
            row[c] = S['M5'][n][c]
        row[6] = (-Ps[n]) % p
        row[7] = (-Phs[n]) % p
        row[8] = (-Qs[n]) % p
        A.append(row)
        cst = 0
        for c in range(6):
            cst += z0[c] * S['C41'][n][c]                     # L1 L4
            cst += inv2 * y0[c] % p * S['C311'][n][c]         # L1^2 L3 / 2
            cst += inv6 * g[c] % p * S['C2111'][n][c]         # L1^3 L2 / 6
        m23 = 0
        for c2 in range(6):
            for c3 in range(6):
                m23 += g[c2] * y0[c3] % p * S['C23'][n][c2][c3]   # L2 L3
        m221 = 0
        for c in range(6):
            for cc in range(6):
                m221 += g[c] * g[cc] % p * S['C221'][n][c][cc]    # L1 L2^2
        cst = (cst + m23 + inv2 * m221 + inv120 * S['G5'][n]) % p
        b.append((-cst) % p)
    ok, x5, N5, r5 = rref_solve(A, b, p)
    print('E5: rank = %d of %d, consistent = %s, null dim = %d, excess eq = %d'
          % (r5, nunk5, ok, len(N5) if ok else -1, (nmax + 1) - r5))
    if ok:
        w0 = x5[:6]
        t5, u5, s5 = x5[6], x5[7], x5[8]
        print('E5: w0 =', w0)
        print('E5: t5 = %d u5 = %d s5 = %d  (t5 ~ %s, u5 ~ %s)'
              % (t5, u5, s5, ratrec(t5, p), ratrec(u5, p)))
        out['w0'], out['t5u5s5'] = w0, (t5, u5, s5)
    else:
        out['E5'] = 'INCONSISTENT'
    return out


def ratrec(a, M, bound=None):
    """Rational reconstruction of a mod M; returns 'num/den' or None."""
    a %= M
    if bound is None:
        bound = int((M // 2) ** 0.5)
    r0, r1 = M, a
    s0, s1 = 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if abs(s1) > bound or s1 == 0:
        return None
    from math import gcd
    if gcd(r1, abs(s1)) != 1:
        return None
    num, den = (r1, s1) if s1 > 0 else (-r1, -s1)
    return '%d/%d' % (num, den) if den != 1 else '%d' % num


if __name__ == '__main__':
    results = {}
    for p in PRIMES:
        print('=' * 70)
        print('prime p =', p)
        S = sweep(p, NMAX)
        print('sweep done, Q_1 =', S['Q'][1], '(expect 21)')
        results[p] = cascade(p, NMAX, S)
    json.dump({str(p): {k: v for k, v in r.items() if k != 'S'}
               for p, r in results.items()},
              open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/eps1_out.json', 'w'),
              default=str)
    print('saved eps1_out.json')
