"""eps67_x2_scan.py -- X-2 STEP 1 (Sol share 6a733a57): find rectified
families whose dominant fold is Atkin-Lehner fixed and whose NEXT
obstruction lies over a CUSP (not an elliptic point).

For each genus-zero-ish level with a standard integral eta hauptmodul t:
  * fold t_c = t(i/sqrt N) and AL-conjugate t_c' (Mobius fit, as eps65);
  * ALL critical values of t inside a modulus bound (Newton on dt/dtau
    from a seed grid over the fundamental strip) -- the elliptic
    obstruction set, where X-1's Fricke-forced branch argument applies;
  * ALL cusp values of t (numeric evaluation at a/c + i*eps via
    multiplier-tracked eta reduction) -- the CUSP obstruction set,
    where branch-killing is linear algebra in a weakly-holomorphic
    space of unbounded dimension (X-2's escape);
  * dim S_4^-(Gamma_0(N)) (Fricke-odd) exactly via PARI mfatkininit;
  * the verdict: order all obstructions after the fold by modulus and
    report the type sequence.  X-2 CANDIDATE iff the first elliptic
    obstruction has modulus > e^r (r = 3: 20.09; r = 2: 7.39) while any
    smaller obstructions are cusp values, and the odd cusp space is
    nonzero.

Also prints the r = 2 branch data: dim S_3(N, chi) for real odd
characters (PARI), the space the sixth-arc scanner never touched.
"""
import mpmath as mp
mp.mp.dps = 50

E3 = mp.e**3
E2 = mp.e**2

# ---- eta hauptmoduln: dict m -> exponent (q-power = sum m e_m / 24) ----
HAUPT = {
 5:  {1: 6, 5: -6},
 6:  {1: 12, 6: 12, 2: -12, 3: -12},
 8:  {1: 8, 8: 8, 2: -8, 4: -8},
 9:  {1: 3, 9: -3},
 10: {1: 6, 10: 6, 2: -6, 5: -6},
 12: {1: 4, 12: 4, 3: -4, 4: -4},
 14: {2: 3, 14: 3, 1: -3, 7: -3},   # (eta2 eta14/eta1 eta7)^3, q^1 at inf? sign
 15: {1: 3, 15: 3, 3: -3, 5: -3},
 18: {1: 3, 18: 3, 2: -3, 9: -3},
 20: {4: 2, 20: 2, 2: -2, 10: -2},
 21: {1: 2, 21: 2, 3: -2, 7: -2},
 24: {1: 1, 24: 1, 3: -1, 8: -1},
}

# ---- eta with multiplier-tracked reduction (valid near the real axis) ----
def eta_red(tau):
    """Dedekind eta via fundamental-domain reduction:
    eta(tau+1) = e^{i pi/12} eta(tau); eta(-1/tau) = sqrt(-i tau) eta(tau)."""
    C = mp.mpc(1)
    tau = mp.mpc(tau)
    for _ in range(4000):
        n = mp.nint(tau.real)
        if n != 0:
            tau -= n
            C *= mp.exp(1j * mp.pi * n / 12)
        if abs(tau) < 1:
            # eta(tau) = eta(-1/tau) / sqrt(-i tau)
            C /= mp.sqrt(-1j * tau)
            tau = -1 / tau
        else:
            break
    q = mp.exp(2j * mp.pi * tau)
    pr = mp.mpc(1)
    for n in range(1, 400):
        x = q ** n
        pr *= (1 - x)
        if abs(x) < mp.mpf(10) ** -46:
            break
    return C * q ** (mp.mpf(1) / 24) * pr


def hpt(N, tau):
    v = mp.mpc(1)
    for m, e in HAUPT[N].items():
        v *= eta_red(m * tau) ** e
    return v


def dhpt(N, tau, h=None):
    if h is None:
        h = mp.mpf(10) ** -20
    return (hpt(N, tau + h) - hpt(N, tau - h)) / (2 * h)


# ---- Mobius fit of t o W_N (as eps65) ----
def mobius_fit(N):
    ys = [mp.mpf('0.35'), mp.mpf('0.45'), mp.mpf('0.55'), mp.mpf('0.65')]
    rows = []
    for y in ys:
        tau = 1j * y
        x = hpt(N, tau)
        w = hpt(N, -1 / (N * tau))
        rows.append([x, mp.mpc(1), -w * x, -w])
    A3 = [[rows[i][j] for j in range(3)] for i in range(3)]
    b3 = [-rows[i][3] for i in range(3)]
    sol = mp.lu_solve(mp.matrix(A3), mp.matrix(b3))
    a, b, c = sol[0], sol[1], sol[2]
    d = mp.mpc(1)
    tau = 1j * ys[3]
    err = abs((a * hpt(N, tau) + b) / (c * hpt(N, tau) + d)
              - hpt(N, -1 / (N * tau)))
    return a, b, c, d, err


# ---- critical values: Newton on g(tau) = dt/dtau over a seed grid ----
def critical_values(N, tbound=1e5):
    vals = []
    seeds = []
    for xr in [k / mp.mpf(10) for k in range(-5, 6)]:
        for yi in [mp.mpf('0.06'), mp.mpf('0.09'), mp.mpf('0.13'),
                   mp.mpf('0.18'), mp.mpf('0.26'), mp.mpf('0.38'),
                   mp.mpf('0.55'), mp.mpf('0.8')]:
            seeds.append(mp.mpc(xr, yi))
    h = mp.mpf(10) ** -18
    for s in seeds:
        tau = s
        ok = True
        for _ in range(60):
            try:
                g = dhpt(N, tau)
                gp = (dhpt(N, tau + h) - dhpt(N, tau - h)) / (2 * h)
                if abs(gp) == 0:
                    ok = False; break
                step = g / gp
                tau = tau - step
                if tau.imag < mp.mpf('0.005') or abs(tau) > 60:
                    ok = False; break
                if abs(step) < mp.mpf(10) ** -30:
                    break
            except Exception:
                ok = False; break
        else:
            ok = False
        if not ok:
            continue
        try:
            tv = hpt(N, tau)
        except Exception:
            continue
        if not mp.isfinite(tv) or abs(tv) > tbound or abs(tv) < 1e-12:
            continue
        if all(abs(tv - v) > mp.mpf(10) ** -12 * (1 + abs(v)) for v in vals):
            vals.append(tv)
    return vals


# ---- cusp values ----
def cusps_gamma0(N):
    from sympy import divisors, gcd
    out = []
    for c in divisors(N):
        w = int(gcd(c, N // c))
        added = set()
        for a in range(1, c + w + 1):
            if mp.mpf(0) == 0 and (a % w if w > 1 else 0) in added:
                continue
            from math import gcd as g_
            if g_(a, c) != 1:
                continue
            added.add(a % w if w > 1 else 0)
            out.append((a, c))
            if len(added) == max(w, 1) * 0 + (w if w > 1 else 1):
                break
    return out


def cusp_values(N):
    vals = []
    for (a, c) in cusps_gamma0(N):
        if c == N:      # the infinity-type cusp for these hauptmoduls: t ~ q
            continue
        rec = []
        for eps in [mp.mpf(10) ** -5, mp.mpf(10) ** -6]:
            try:
                rec.append(hpt(N, mp.mpf(a) / c + 1j * eps))
            except Exception:
                rec.append(None)
        if rec[0] is None or rec[1] is None:
            vals.append(((a, c), None)); continue
        if abs(rec[1]) > 1e8 or abs(rec[1]) > 3 * abs(rec[0]) + 10:
            vals.append(((a, c), mp.inf))
        elif abs(rec[0] - rec[1]) < mp.mpf(10) ** -6 * (1 + abs(rec[1])):
            vals.append(((a, c), rec[1]))
        else:
            vals.append(((a, c), ('unstable', rec[0], rec[1])))
    return vals


def odd_dim(pari, N, k=4):
    mf = pari.mfinit([N, k], 1)
    if int(pari.mfdim([N, k], 1)) == 0:
        return 0
    ai = pari.mfatkininit(mf, N)
    ev = pari.mateigen(ai[1], 1)[0]
    return sum(1 for x in ev if int(x) == -1)


if __name__ == '__main__':
    import cypari2
    pari = cypari2.Pari()
    print('X-2 STEP-1 SCAN: obstruction geometry per level')
    print('thresholds: e^3 = %.2f (r=3), e^2 = %.2f (r=2)\n'
          % (float(E3), float(E2)))
    for N in sorted(HAUPT):
        try:
            a, b, c, d, err = mobius_fit(N)
            tc = hpt(N, 1j / mp.sqrt(N))
            crit = critical_values(N)
            cval = cusp_values(N)
            dS4 = int(pari.mfdim([N, 4], 1))
            dodd = odd_dim(pari, N, 4)
            # order obstructions beyond the fold
            fold = min(crit, key=lambda v: abs(v - tc)) if crit else tc
            obstructions = []
            for v in crit:
                if abs(v - fold) > 1e-10 * (1 + abs(v)):
                    obstructions.append((abs(v), 'ELL', v))
            for (cu, v) in cval:
                if v is None or v == mp.inf or isinstance(v, tuple):
                    continue
                if abs(v) > 1e-10:
                    obstructions.append((abs(v), 'CUSP %s/%s' % cu, v))
            obstructions.sort(key=lambda x: float(x[0]))
            print('N=%d  dimS4=%d  odd=%d  fold t_c=%s (|.|=%.4f)  fiterr=%.0e'
                  % (N, dS4, dodd, mp.nstr(fold, 6), float(abs(fold)),
                     float(err)))
            for (m, ty, v) in obstructions[:6]:
                mark = ''
                if ty == 'ELL':
                    mark = '  <-- ELLIPTIC BARRIER: score3=%.2f score2=%.2f' \
                        % (float(E3 / m), float(E2 / m))
                print('    |t|=%-12.5f %-12s t=%s%s'
                      % (float(m), ty, mp.nstr(v, 6), mark))
            unst = [(cu, v) for (cu, v) in cval
                    if isinstance(v, tuple) or v is None]
            if unst:
                print('    unstable cusp evals:', [(cu) for cu, v in unst])
            inf_c = [cu for (cu, v) in cval if v == mp.inf]
            print('    cusps at t=inf:', inf_c)
            # verdict
            ells = [m for (m, ty, v) in obstructions if ty == 'ELL']
            first_ell = min(ells) if ells else mp.inf
            cusps_before = [m for (m, ty, v) in obstructions
                            if not ty == 'ELL' and m < first_ell]
            v3 = first_ell > E3
            v2 = first_ell > E2
            print('    VERDICT: first elliptic barrier %.3f; cusp obstructions'
                  ' before it: %d;  X-2 cell (r=3): %s  (r=2): %s  odd>0: %s\n'
                  % (float(first_ell), len(cusps_before),
                     'YES' if v3 and dodd > 0 else 'no',
                     'YES' if v2 and dodd > 0 else 'no', dodd > 0))
        except Exception as ex:
            print('N=%d ERROR: %s\n' % (N, ex))

    print('\nr=2 branch: dim S_3(N, chi) for chi real odd (PARI wildcard):')
    for N in range(3, 26):
        dd = pari.mfdim([N, 3, 0], 1)
        nz = [x for x in dd if int(x[2]) > 0 and int(x[0]) == 2]
        if nz:
            print('  N=%d: %s' % (N, nz))
