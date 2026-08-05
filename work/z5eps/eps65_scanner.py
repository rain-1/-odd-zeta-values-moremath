"""eps65_scanner.py -- the modular irrationality scanner (Sol's project,
River's directive): for each genus-zero-ish level with an integral eta
hauptmodul, compute the Atkin-Lehner fold data and the Apery race score.

Mechanism (D1 ledger 9): an odd source vanishing at the W_N-fixed fold
gives error ~ |t_c'|^{-n} relative... precisely |A_n xi - B_n| ~ |t_c'|^{-n}
in the t-scale where A_n integral; denominators d_n^r ~ e^{rn}.
RACE WON iff e^r < |t_c'|  (r = 3 for weight-2 F / weight-4 sources,
r = 2 for weight-1 F / weight-3 sources).

t o W_N is a Mobius involution of the hauptmodul; its fixed values are
the two AL-elliptic singular values t_c (= t(i/sqrt N)) and t_c'.
We fit the Mobius map numerically from samples and extract both.

Cusp dims: dim S_k(Gamma_0(N)) by the classical formula.
"""
import mpmath as mp
mp.mp.dps = 50

# ---- eta hauptmoduln: dict m -> exponent; q-power auto = sum m e_m/24 ----
HAUPT = {
 2:  {1: 24, 2: -24},          # (eta1/eta2)^24 : t = q^{-1}(...)? handle inversions
 3:  {1: 12, 3: -12},
 4:  {1: 8, 4: -8},
 5:  {1: 6, 5: -6},
 6:  {1: 12, 6: 12, 2: -12, 3: -12},   # Apery's (eta1 eta6/eta2 eta3)^12
 7:  {1: 4, 7: -4},
 8:  {1: 8, 8: 8, 2: -8, 4: -8},
 9:  {1: 3, 9: -3},
 10: {1: 6, 10: 6, 2: -6, 5: -6},
 12: {1: 4, 12: 4, 3: -4, 4: -4},
 13: {1: 2, 13: -2},
 16: {2: 4, 16: 4, 4: -4, 8: -4},
 18: {1: 3, 18: 3, 2: -3, 9: -3},
 25: {1: 1, 25: -1},
}

def eta(tau, terms=400):
    q = mp.exp(2j*mp.pi*tau)
    pr = mp.mpc(1)
    for n in range(1, terms):
        x = q**n
        pr *= (1 - x)
        if abs(x) < mp.mpf(10)**-45: break
    return q**(mp.mpf(1)/24) * pr

def hpt(N, tau):
    v = mp.mpc(1)
    for m, e in HAUPT[N].items():
        v *= eta(m*tau)**e
    return v

def sgnpow(N):
    """q-power of hauptmodul = sum m e_m / 24 (should be +-1 or so)."""
    return sum(m*e for m, e in HAUPT[N].items())/24

def mobius_fit(N):
    """fit t(W tau) = (a t + b)/(c t + d) from samples."""
    ys = [mp.mpf('0.35'), mp.mpf('0.45'), mp.mpf('0.55'), mp.mpf('0.65')]
    rows = []
    for y in ys:
        tau = 1j*y
        x = hpt(N, tau)
        w = hpt(N, -1/(N*tau))
        # w(c x + d) = a x + b -> a x + b - w c x - w d = 0
        rows.append([x, mp.mpc(1), -w*x, -w])
    # nullspace via 3x3 solve with d = 1 (or c = 1 fallback)
    import itertools
    A3 = [[rows[i][j] for j in range(3)] for i in range(3)]
    b3 = [-rows[i][3] for i in range(3)]
    try:
        sol = mp.lu_solve(mp.matrix(A3), mp.matrix(b3))
        a, b, c = sol[0], sol[1], sol[2]
        d = mp.mpc(1)
    except Exception:
        return None
    # verify on 4th sample
    x, w = None, None
    tau = 1j*ys[3]
    x = hpt(N, tau); w = hpt(N, -1/(N*tau))
    err = abs((a*x+b)/(c*x+d) - w)
    return (a, b, c, d, err)

def fixed_points(a, b, c, d):
    # (a x + b)/(c x + d) = x -> c x^2 + (d - a) x - b = 0
    disc = mp.sqrt((d-a)**2 + 4*b*c)
    x1 = ((a-d) + disc)/(2*c)
    x2 = ((a-d) - disc)/(2*c)
    return x1, x2

# ---- dim S_k(Gamma_0(N)), k even >= 4 ----
def dims(N, k=4):
    from sympy import primefactors, isprime
    def mu(N):
        m = N
        for p in primefactors(N):
            m = m*(p+1)//p
        return m
    def e2(N):
        if N % 4 == 0: return 0
        r = 1
        for p in primefactors(N):
            r *= (1 + pow(-1, (p-1)//2) if p % 2 else 1) if p != 2 else 1
        # standard: prod (1 + (-1/p))
        r = 1
        for p in primefactors(N):
            if p == 2: continue
            r *= 1 + (1 if p % 4 == 1 else -1)
        return r
    def e3(N):
        if N % 9 == 0: return 0
        r = 1
        for p in primefactors(N):
            if p == 3: continue
            r *= 1 + (1 if p % 3 == 1 else -1)
        return r
    def einf(N):
        from sympy import divisors, totient, gcd
        return sum(totient(gcd(dd, N//dd)) for dd in divisors(N))
    m = mu(N); E2 = e2(N); E3 = e3(N); Ei = einf(N)
    g = 1 + mp.mpf(m)/12 - E2/mp.mpf(4) - E3/mp.mpf(3) - Ei/mp.mpf(2)
    g = int(mp.nint(g))
    dS = (k-1)*(g-1) + (k//4)*E2 + (k//3)*E3 + (k//2 - 1)*Ei
    return g, int(dS), m, E2, E3, Ei

if __name__ == '__main__':
    e3v = mp.e**3; e2v = mp.e**2
    print('N   g  dimS4  t_c            |t_c|     |t_c_prime|   e^3/|tcp|  e^2/|tcp|')
    results = []
    for N in sorted(HAUPT):
        try:
            fit = mobius_fit(N)
            if fit is None:
                print('%2d  fit failed' % N); continue
            a, b, c, d, err = fit
            tc_direct = hpt(N, 1j/mp.sqrt(N))
            if abs(c) < mp.mpf(10)**-20:
                print('%2d  involution affine (t_c at infinity?)' % N)
                continue
            x1, x2 = fixed_points(a, b, c, d)
            # identify which is t(i/sqrt N)
            if abs(x1 - tc_direct) < abs(x2 - tc_direct):
                tc, tcp = x1, x2
            else:
                tc, tcp = x2, x1
            g, dS4, mu_, E2_, E3_, Ei_ = dims(N, 4)
            s3 = e3v/abs(tcp); s2 = e2v/abs(tcp)
            flag = ''
            if abs(tc) < abs(tcp):
                if s3 < 1: flag += ' ***WIN r=3***'
                if s2 < 1: flag += ' **win r=2**'
            else:
                flag = ' [fold not dominant]'
            print('%2d  %d   %2d   %-14s %.6f  %.6f   %8.3f  %8.3f%s  (miderr %.0e)'
                  % (N, g, dS4, mp.nstr(tc, 6), abs(tc), abs(tcp),
                     float(s3), float(s2), flag, float(err)))
            results.append((N, dS4, float(abs(tc)), float(abs(tcp)),
                            float(s3), float(s2)))
        except Exception as ex:
            print('%2d  ERROR %s' % (N, ex))
