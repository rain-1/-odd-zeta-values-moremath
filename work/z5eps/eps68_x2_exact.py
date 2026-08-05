"""eps68_x2_exact.py -- X-2 STEP 1, exact pass.  The eps67 grid missed
AL fixed points at low Im(tau); here every Atkin-Lehner involution's
fixed points are enumerated exactly by matrices and only dt = 0 points
count as operator singularities (elliptic obstructions).  Cusp values
from eps67 machinery.  Each obstruction value is identified as an
algebraic number by PSLQ against 1, t, t^2.

W_Q on Gamma_0(N) (Q || N):  M = [[Qa, b],[Nc, -Qa]] with
det = -Q^2 a^2 - N b c = Q, i.e.  Q a^2 + (N/Q) b c = -1;
fixed points: N c tau^2 - 2 Q a tau - b = 0.

Verdict per level: order all obstructions after the AL fold by modulus;
X-2 cell iff the sub-threshold obstructions are all CUSP values and the
first elliptic barrier exceeds e^r, with a nonzero odd cusp space
(r = 3: S_4^-(Gamma_0(N)); r = 2: S_3(N, chi) real odd chi).
"""
import mpmath as mp
from eps67_x2_scan import (HAUPT, eta_red, hpt, dhpt, cusp_values,
                           critical_values, odd_dim)
mp.mp.dps = 50
E3, E2 = mp.e**3, mp.e**2


def al_fixed_values(N, Q, amax=8, cmax=80):
    """distinct t-values of W_Q fixed points, with dt flag."""
    out = []
    NQ = N // Q
    for a in range(-amax, amax + 1):
        for c in range(1, cmax + 1):
            num = -(Q * a * a + 1)
            if num % (NQ * c):
                continue
            b = num // (NQ * c)
            A_, B_, C_ = N * c, -2 * Q * a, -b
            disc = B_ * B_ - 4 * A_ * C_
            if disc >= 0:
                continue
            tau = (-B_ + mp.sqrt(disc)) / (2 * A_)
            try:
                t = hpt(N, tau)
                dt = abs(dhpt(N, tau))
            except Exception:
                continue
            if not mp.isfinite(t):
                continue
            if all(abs(t - v) > 1e-9 * (1 + abs(v)) for v, _ in out):
                out.append((t, dt < 1e-10))
    return out


def alg_id(t):
    """identify t as root of quadratic (or linear) with small coeffs."""
    if abs(t.imag) < 1e-20:
        x = t.real
        r = mp.pslq([mp.mpf(1), x], tol=mp.mpf(10) ** -30, maxcoeff=10**6)
        if r:
            from fractions import Fraction
            return str(Fraction(int(-r[0]), int(r[1])))
        r = mp.pslq([mp.mpf(1), x, x * x], tol=mp.mpf(10) ** -30,
                    maxcoeff=10**6)
        if r:
            return 'root(%d + %d t + %d t^2)' % (r[0], r[1], r[2])
    else:
        # complex: try quadratic with real coeffs
        re2 = 2 * t.real
        m2 = abs(t) ** 2
        r = mp.pslq([mp.mpf(1), re2, m2], tol=mp.mpf(10) ** -25,
                    maxcoeff=10**6)
        if r:
            return 'complex root, 2Re=%s |t|^2=%s' % (mp.nstr(re2, 8),
                                                      mp.nstr(m2, 8))
    return '?'


if __name__ == '__main__':
    import cypari2
    pari = cypari2.Pari()
    from sympy import divisors, gcd as sgcd
    print('X-2 exact scan: e^3=%.3f e^2=%.3f\n' % (float(E3), float(E2)))
    for N in sorted(HAUPT):
        try:
            tc = hpt(N, 1j / mp.sqrt(N))
            ells = []            # (t, 'W_Q') with dt=0 only
            nonc = []
            for Q in divisors(N):
                if Q == 1 or sgcd(Q, N // Q) != 1:
                    continue
                for (t, crit) in al_fixed_values(N, Q):
                    (ells if crit else nonc).append((t, 'W%d' % Q))
            # Newton criticals as safety net (Gamma-elliptic etc.)
            for v in critical_values(N, tbound=1e9):
                if all(abs(v - t) > 1e-8 * (1 + abs(t)) for t, _ in ells):
                    ells.append((v, 'newt'))
            cv = cusp_values(N)
            dS4 = int(pari.mfdim([N, 4], 1))
            dodd = odd_dim(pari, N, 4)
            d3 = pari.mfdim([N, 3, 0], 1)
            s3chi = [(x[1], int(x[2])) for x in d3
                     if int(x[2]) > 0 and int(x[0]) == 2]
            fold = min(ells, key=lambda p: abs(p[0] - tc))[0] if ells else tc
            obs = []
            for (t, lab) in ells:
                if abs(t - fold) > 1e-8 * (1 + abs(t)):
                    obs.append((abs(t), 'ELL[%s]' % lab, t))
            for (cu, v) in cv:
                if v is None or v == mp.inf or isinstance(v, tuple):
                    continue
                if abs(v) > 1e-9:
                    obs.append((abs(v), 'CUSP%s/%s' % cu, v))
            obs.sort(key=lambda x: float(x[0]))
            print('N=%d  fold=%s = %s   dimS4=%d S4odd=%d  S3(chi)=%s'
                  % (N, mp.nstr(fold, 8), alg_id(fold), dS4, dodd, s3chi))
            for (m, ty, v) in obs[:7]:
                print('    |t|=%-11.5f %-11s %-24s %s'
                      % (float(m), ty, mp.nstr(v, 8), alg_id(v)))
            ellm = [m for (m, ty, v) in obs if ty.startswith('ELL')]
            fe = min(ellm) if ellm else mp.inf
            cb = [m for (m, ty, v) in obs if not ty.startswith('ELL')
                  and m < fe]
            print('    first elliptic barrier %.4f: score3=%.3f score2=%.3f;'
                  ' cusp obstructions before it: %d'
                  % (float(fe), float(E3 / fe), float(E2 / fe), len(cb)))
            x2_r3 = fe > E3 * 0.99 and dodd > 0
            x2_r2 = fe > E2 and bool(s3chi)
            near3 = 1 < E3 / fe < 1.6 and dodd > 0
            print('    X-2 cell: r=3 %s%s  r=2 %s\n'
                  % ('YES' if x2_r3 else 'no',
                     ' (NEAR-MISS, score %0.2f)' % float(E3/fe) if near3
                     else '', 'YES' if x2_r2 else 'no'))
        except Exception as ex:
            print('N=%d ERROR %s\n' % (N, ex))
