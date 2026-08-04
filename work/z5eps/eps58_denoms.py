"""eps58_denoms.py -- DENOMINATOR HARVEST from the Eichler companion formula.

For each of the fifteen sporadic pairs:
  (1) exact B(n), n <= NMAX, denominators D(n), v_p profiles p <= 13,
      test of the bound  v_p(D(n)) <= r * v_p(d_n)  (d_n = lcm(1..n),
      r = operator order);
  (2) self-contained verification of the conditional inputs at stated
      series orders: t(q), F(q), sigma(q), A(q) = t*sigma^r/(P(t)F) all in
      Z[[q]]; q(t) in Z[[t]]; and the Eichler formula
      B(n) = [t^n] F * theta_q^{-r}(A) against the recurrence;
  (3) sharpness gaps  r*v_p(d_n) - v_p(D(n)) at n = NMAX.

Recurrences (papers_out/sporadics table):
  R2 (rows 1-6):  (n+1)^2 u_{n+1} = (a n^2 + a n + b) u_n - c n^2 u_{n-1}
  R3 (rows 7-15): (n+1)^3 u_{n+1} = (2n+1)(a n^2 + a n + b) u_n
                                    - n (c n^2 + d) u_{n-1}
Operators:
  R2: L = th^2 - t(a th^2 + a th + b) + c t^2 (th+1)^2,   P(t)=1-at+ct^2, r=2
  R3: L = th^3 - t(2th+1)(a th^2+a th+b) + t^2 (th+1)(c(th+1)^2+d),
      P(t)=1-2at+ct^2, r=3
Second solution: B(0)=0, B(1)=1;  L(y_B) = t exactly (n=0 instance).
"""

import sys, json
from fractions import Fraction as F
from math import gcd

NMAX = 120       # exact B(n) range
QORD = 48        # series order for nome/formula verification
PRIMES = [2, 3, 5, 7, 11, 13]

FAMS = {
    # name: (shape, a, b, c, d)
    'A_franel': ('R2', 7, 2, -8, 0),
    'B':        ('R2', 9, 3, 27, 0),
    'C':        ('R2', 10, 3, 9, 0),
    'D':        ('R2', 11, 3, -1, 0),
    'E':        ('R2', 12, 4, 32, 0),
    'F':        ('R2', 17, 6, 72, 0),
    'alpha':    ('R3', 10, 4, 64, 0),
    'gamma':    ('R3', 17, 5, 1, 0),
    'delta':    ('R3', 7, 3, 81, 0),
    'epsilon':  ('R3', 12, 4, 16, 0),
    'zeta':     ('R3', 9, 3, -27, 0),
    'eta':      ('R3', 11, 5, 125, 0),
    's7':       ('R3', 13, 4, -27, 3),
    's10':      ('R3', 6, 2, -64, 4),
    's18':      ('R3', 14, 6, 192, -12),
}
# NOTE: rows 13-15 (Cooper) use the R3 *shape* although their modular weight
# is 2; the operator order (hence r and the theta-power) is 3.


def vp(x, p):
    if x == 0:
        return 10 ** 9
    x = F(x)
    a, b = x.numerator, x.denominator
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v


def dn_vp(n, p):
    """v_p(lcm(1..n)) = floor(log_p n)."""
    v = 0
    q = p
    while q <= n:
        v += 1
        q *= p
    return v


def seqs(shape, a, b, c, d, N, eps_deriv=False):
    """A(n) (and dA/deps if eps_deriv) for n <= N; also B(n)."""
    A = [F(1)]
    dA = [F(0)]
    for n in range(0, N):
        if shape == 'R2':
            num = (F(a * n * n + a * n + b) * A[n]
                   - (F(c * n * n) * A[n - 1] if n >= 1 else 0))
            den = F((n + 1) ** 2)
            if eps_deriv:
                # d/de of ((n+1+e)^2 A_{n+1}) = d/de(rhs)
                dnum = (F(a * (2 * n) + a) * A[n] + F(a * n * n + a * n + b) * dA[n]
                        - ((F(c * 2 * n) * A[n - 1] + F(c * n * n) * dA[n - 1])
                           if n >= 1 else 0))
                Anew = num / den
                dAnew = (dnum - F(2 * (n + 1)) * Anew) / den
        else:
            num = (F((2 * n + 1) * (a * n * n + a * n + b)) * A[n]
                   - (F(n * (c * n * n + d)) * A[n - 1] if n >= 1 else 0))
            den = F((n + 1) ** 3)
            if eps_deriv:
                p1 = (2 * n + 1) * (a * n * n + a * n + b)
                dp1 = 2 * (a * n * n + a * n + b) + (2 * n + 1) * (2 * a * n + a)
                p2 = n * (c * n * n + d)
                dp2 = (c * n * n + d) + n * (2 * c * n)
                dnum = (F(dp1) * A[n] + F(p1) * dA[n]
                        - ((F(dp2) * A[n - 1] + F(p2) * dA[n - 1])
                           if n >= 1 else 0))
                Anew = num / den
                dAnew = (dnum - F(3 * (n + 1) ** 2) * Anew) / den
        A.append(num / den)
        if eps_deriv:
            dA.append(dAnew)
    return (A, dA) if eps_deriv else A


def bseq(shape, a, b, c, d, N):
    B = [F(0), F(1)]
    for n in range(1, N):
        if shape == 'R2':
            nxt = (F(a * n * n + a * n + b) * B[n] - F(c * n * n) * B[n - 1]) \
                / F((n + 1) ** 2)
        else:
            nxt = (F((2 * n + 1) * (a * n * n + a * n + b)) * B[n]
                   - F(n * (c * n * n + d)) * B[n - 1]) / F((n + 1) ** 3)
        B.append(nxt)
    return B


# ---------- series helpers (dense lists of Fractions, index = power) ----------
def smul(x, y, N):
    out = [F(0)] * (N + 1)
    for i, xi in enumerate(x):
        if xi == 0 or i > N:
            continue
        for j, yj in enumerate(y):
            if i + j > N:
                break
            if yj:
                out[i + j] += xi * yj
    return out


def sinv(x, N):
    """1/x for x[0] != 0."""
    out = [F(0)] * (N + 1)
    out[0] = 1 / x[0]
    for n in range(1, N + 1):
        s = F(0)
        for k in range(1, n + 1):
            if k < len(x) and x[k]:
                s += x[k] * out[n - k]
        out[n] = -s / x[0]
    return out


def sexp(x, N):
    """exp(x) for x[0] = 0."""
    out = [F(0)] * (N + 1)
    out[0] = F(1)
    # out' = x' * out  =>  n*out_n = sum_{k=1..n} k*x_k*out_{n-k}
    for n in range(1, N + 1):
        s = F(0)
        for k in range(1, n + 1):
            if k < len(x) and x[k]:
                s += F(k) * x[k] * out[n - k]
        out[n] = s / n
    return out


def scomp(x, y, N):
    """x(y(t)) with y[0] = 0."""
    out = [F(0)] * (N + 1)
    ypow = [F(0)] * (N + 1)
    ypow[0] = F(1)
    for i, xi in enumerate(x):
        if i > N:
            break
        if xi:
            for j in range(N + 1):
                out[j] += xi * ypow[j]
        ypow = smul(ypow, y, N)
    return out


def srevert(y, N):
    """compositional inverse of y = t + O(t^2)."""
    assert y[0] == 0 and y[1] == 1
    inv = [F(0), F(1)]
    for n in range(2, N + 1):
        cur = scomp(y, inv + [F(0)] * (N + 1 - len(inv)), n)
        inv.append(-cur[n])
    return inv + [F(0)] * (N + 1 - len(inv))


def theta_inv(x, N, r):
    out = [F(0)] * (N + 1)
    for m in range(1, N + 1):
        if m < len(x) and x[m]:
            out[m] = x[m] / F(m ** r)
    return out


def is_int_series(x, upto):
    bad = [m for m in range(min(upto, len(x) - 1) + 1)
           if x[m].denominator != 1]
    return (not bad), bad[:4]


def run_family(name, spec):
    shape, a, b, c, d = spec
    r = 2 if shape == 'R2' else 3
    # ---------- exact B and denominators ----------
    B = bseq(shape, a, b, c, d, NMAX)
    Dprof = {}
    excess = {}
    gap120 = {}
    for p in PRIMES:
        vmax = -99
        firstbad = None
        for n in range(NMAX + 1):
            e = vp(B[n], p)
            exc = -e - r * dn_vp(n, p)   # v_p(denominator) = -min(e,0)
            dden = max(0, -e)
            exc = dden - r * dn_vp(n, p)
            if exc > vmax:
                vmax = exc
                firstbad = n
        excess[p] = (vmax, firstbad)
        gap120[p] = r * dn_vp(NMAX, p) - max(0, -vp(B[NMAX], p))
    # ---------- nome + formula verification ----------
    (A_, dA_) = seqs(shape, a, b, c, d, QORD + 2, eps_deriv=True)
    y0 = A_[:QORD + 1]
    g = dA_[:QORD + 1]
    ratio = smul(g, sinv(y0, QORD), QORD)      # g/y0, constant term 0
    ratio[0] = F(0)
    q_of_t = smul([F(0), F(1)] + [F(0)] * (QORD - 1), sexp(ratio, QORD), QORD)
    t_of_q = srevert(q_of_t, QORD)
    ok_q, badq = is_int_series(q_of_t, QORD)
    ok_t, badt = is_int_series(t_of_q, QORD)
    Fq = scomp(y0, t_of_q, QORD)
    ok_F, badF = is_int_series(Fq, QORD)
    # sigma = theta_q t / t
    th_t = [F(m) * t_of_q[m] for m in range(QORD + 1)]
    sigma = smul(th_t, sinv(t_of_q[1:] + [F(0)], QORD), QORD)  # t/q shifted
    # careful: t/q = series with const t_of_q[1]=1: build properly
    t_over_q = t_of_q[1:] + [F(0)]
    sigma = smul([F(m) * t_of_q[m] for m in range(1, QORD + 1)] + [F(0)],
                 sinv(t_over_q, QORD), QORD)
    # theta_q t = sum m t_m q^m ; (theta_q t)/t = (sum m t_m q^{m-1})/(t/q)
    ok_s, bads = is_int_series(sigma, QORD)
    # P(t) as series in q
    if shape == 'R2':
        Pt = [F(1), F(-a), F(c)]
    else:
        Pt = [F(1), F(-2 * a), F(c)]
    P_q = scomp(Pt, t_of_q, QORD)
    Aq = smul(smul(t_of_q, [x for x in sigma], QORD),
              sinv(smul(P_q, Fq, QORD), QORD), QORD)
    for _ in range(r - 1):
        Aq = smul(Aq, sigma, QORD)
    ok_A, badA = is_int_series(Aq, QORD)
    yB_q = smul(Fq, theta_inv(Aq, QORD, r), QORD)
    yB_t = scomp(yB_q, q_of_t, QORD)
    nver = min(QORD, 40)
    ok_formula = all(yB_t[n] == B[n] for n in range(nver + 1))
    return {
        'family': name, 'shape': shape, 'r': r,
        'excess': {p: excess[p] for p in PRIMES},
        'bound_holds': all(excess[p][0] <= 0 for p in PRIMES),
        'gap_at_%d' % NMAX: gap120,
        'q_int': (ok_q, badq), 't_int': (ok_t, badt),
        'F_int': (ok_F, badF), 'sigma_int': (ok_s, bads),
        'A_int': (ok_A, badA),
        'formula_matches_to': nver if ok_formula else
            min(n for n in range(nver + 1) if yB_t[n] != B[n]) - 1,
        'D_at_16': str(F(B[16]).denominator) if len(B) > 16 else '',
    }


if __name__ == '__main__':
    results = []
    for name, spec in FAMS.items():
        res = run_family(name, spec)
        results.append(res)
        print('%-9s r=%d bound d_n^r holds: %-5s  formula matches n<=%s  '
              't,F,sig,A int: %s%s%s%s  (q int: %s)'
              % (res['family'], res['r'], res['bound_holds'],
                 res['formula_matches_to'],
                 'T' if res['t_int'][0] else 'F',
                 'T' if res['F_int'][0] else 'F',
                 'T' if res['sigma_int'][0] else 'F',
                 'T' if res['A_int'][0] else 'F',
                 'T' if res['q_int'][0] else 'F'), flush=True)
        print('   excess (v_p(D)-r*v_p(d_n), max over n<=%d): %s'
              % (NMAX, {p: res['excess'][p] for p in PRIMES}))
        print('   sharpness gap at n=%d: %s' % (NMAX, res['gap_at_120']))
    with open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/'
              'eps58_results.json', 'w') as fh:
        json.dump([{k: str(v) for k, v in r.items()} for r in results],
                  fh, indent=1)
    print('saved eps58_results.json')
