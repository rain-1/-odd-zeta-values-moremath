"""
High-precision Bloch-Vlasenko Frobenius constants kappa_{rho,n} at the conifold
closest to 0, for an operator L = sum_j z^j q_j(theta) with polynomial q_j.

METHOD (BV Lemma 24 + Golyshev-Zagier sec.9, recast as a Stokes-constant ratio).

  Frobenius:  Phi(s,z) = sum_n a_n(s) z^{n+s},  a_0 = 1,
              sum_{j=0}^{d} q_j(n+s-j) a_{n-j}(s) = 0   (n >= 1).
  BV Lemma 24 says  kappa(eps)/kappa_0 = c^eps * Lambda(eps),
              Lambda(eps) = lim_n a_n(rho+eps)/a_n(rho),   c = 1/lambda.

  Let A(x) = lambda^x x^alpha F(1/x), F(u)=sum_k c_k u^k, c_0=1, be THE formal
  (Birkhoff) solution of  sum_j q_j(x-j) A(x-j) = 0.  Because the deformation is
  literally  n -> n+eps,  the deformed sequence has the SAME formal solution
  evaluated at x = n+eps.  Hence with the Stokes constant
              S(eps) := lim_n a_n(rho+eps) / A(n+eps)
  one gets  Lambda(eps) = (S(eps)/S(0)) * lambda^eps  and therefore

              kappa(eps) = S(eps) / S(0).                       (*)

  (*) is what we compute: the log(c) and lambda^eps factors cancel exactly, and
  the convergence of a_n(eps)/A(n+eps) is beyond all orders in 1/n -- the error
  is O((lambda_2/lambda_1)^n) plus the truncation of the asymptotic series.

Everything below is generic in the q_j (integer coefficient lists, low->high).
"""
from mpmath import mp, mpf, matrix
from fractions import Fraction

# ---------------------------------------------------------------- eps-series
def smul(a, b, K):
    c = [mp.mpf(0)] * (K + 1)
    for i in range(K + 1):
        ai = a[i]
        if ai == 0:
            continue
        for j in range(K + 1 - i):
            bj = b[j]
            if bj != 0:
                c[i + j] += ai * bj
    return c

def sdiv(a, b, K):
    c = [mp.mpf(0)] * (K + 1)
    for i in range(K + 1):
        s = a[i]
        for j in range(1, i + 1):
            s -= b[j] * c[i - j]
        c[i] = s / b[0]
    return c

def sdiv_gen(a, b, K):
    """a/b allowing b (and a) to vanish to a common order v; the result is
    correct only to order K-v, the tail is returned as zeros."""
    vb = 0
    while vb <= K and b[vb] == 0:
        vb += 1
    if vb == 0:
        return sdiv(a, b, K)
    va = 0
    while va <= K and a[va] == 0:
        va += 1
    if va < vb:
        raise ValueError('pole of order %d' % (vb - va))
    aa = a[vb:] + [mp.mpf(0)] * vb
    bb = b[vb:] + [mp.mpf(0)] * vb
    c = sdiv(aa, bb, K - vb)
    return c + [mp.mpf(0)] * vb


def sscale(a, t, K):
    return [x * t for x in a]

def sexp_lin(g, K):
    """series of exp(g*eps)"""
    out = [mp.mpf(0)] * (K + 1)
    out[0] = mp.mpf(1)
    f = mp.mpf(1)
    p = mp.mpf(1)
    for i in range(1, K + 1):
        f *= i
        p *= g
        out[i] = p / f
    return out

def slog(a, K):
    """log of a series with a[0]=1"""
    x = list(a)
    x[0] = mp.mpf(0)
    acc = [mp.mpf(0)] * (K + 1)
    cur = list(x)
    for m in range(1, K + 1):
        s = mp.mpf(1) if m % 2 == 1 else mp.mpf(-1)
        for i in range(K + 1):
            acc[i] += s * cur[i] / m
        cur = smul(cur, x, K)
    return acc

def sexp(a, K):
    """exp of a series with a[0]=0"""
    acc = [mp.mpf(0)] * (K + 1)
    acc[0] = mp.mpf(1)
    cur = [mp.mpf(0)] * (K + 1)
    cur[0] = mp.mpf(1)
    f = mp.mpf(1)
    for m in range(1, K + 1):
        cur = smul(cur, a, K)
        f *= m
        for i in range(K + 1):
            acc[i] += cur[i] / f
    return acc

# ---------------------------------------------------------------- polynomials
def poly_shift_taylor(g, x0, K):
    """exact Taylor coefficients [q^{(i)}(x0)/i!] i=0..K, g = int/Fraction coeffs low->high."""
    p = [Fraction(x) for x in g]
    out = []
    for _ in range(K + 1):
        if not p:
            out.append(Fraction(0))
            continue
        n = len(p) - 1
        q = [Fraction(0)] * n
        acc = p[n]
        for k in range(n - 1, -1, -1):
            if k < n:
                q[k] = acc
            acc = p[k] + acc * x0
        out.append(acc)
        p = q
    return out

def poly_eval_int(g, x):
    acc = Fraction(0)
    for co in reversed(g):
        acc = acc * x + co
    return acc

# ------------------------------------------------ Birkhoff formal solution
def birkhoff(qs, lam, M):
    """
    qs: list of integer-coefficient polynomials q_0..q_d (low->high).
    lam: the characteristic root (mpf), i.e. a_n ~ const*lam^n*n^alpha.
    Returns (alpha, [c_0..c_M]) for A(x)=lam^x x^alpha sum c_k x^{-k}.

    Equation: sum_j q_j(x-j) A(x-j) = 0.  With u=1/x, Q_j(u):=u^D q_j(1/u - j),
      sum_j lam^{-j} Q_j(u) (1-ju)^{alpha-k} u^k c_k = 0.
    """
    d = len(qs) - 1
    D = max(len(g) - 1 for g in qs)
    # exact integer polys Q_j(u) = sum_i g_{j,i} u^{D-i} (1-j u)^i
    Qs = []
    for j, g in enumerate(qs):
        Q = [Fraction(0)] * (D + 1)
        for i, co in enumerate(g):
            if co == 0:
                continue
            # co * u^{D-i} * (1-j u)^i
            b = Fraction(1)
            for t in range(i + 1):
                # binom(i,t)*(-j)^t u^t
                if D - i + t <= D:
                    Q[D - i + t] += co * b * ((-j) ** t)
                b = b * Fraction(i - t, t + 1)
        Qs.append([mp.mpf(x.numerator) / mp.mpf(x.denominator) for x in Q])
    lp = [mp.mpf(1)]
    for j in range(1, d + 1):
        lp.append(lp[-1] / lam)
    # characteristic check
    chk = sum(lp[j] * Qs[j][0] for j in range(d + 1))
    beta = sum(lp[j] * Qs[j][1] for j in range(d + 1))
    gam = sum(lp[j] * Qs[j][0] * j for j in range(d + 1))
    alpha = beta / gam
    N = M + 2  # series length in u

    def binpow(base_j, e, N):
        """series of (1 - j u)^e up to u^{N-1}"""
        out = [mp.mpf(0)] * N
        out[0] = mp.mpf(1)
        co = mp.mpf(1)
        for i in range(1, N):
            co = co * (e - (i - 1)) / i
            out[i] = co * ((-base_j) ** i)
        return out

    def pmul(a, b, N):
        c = [mp.mpf(0)] * N
        for i in range(N):
            ai = a[i]
            if ai == 0:
                continue
            for k in range(N - i):
                bk = b[k]
                if bk != 0:
                    c[i + k] += ai * bk
        return c

    # P_j(u) = lam^{-j} Q_j(u) (1-ju)^alpha
    Ps = []
    for j in range(d + 1):
        qq = [Qs[j][i] if i <= D else mp.mpf(0) for i in range(N)]
        Ps.append([x * lp[j] for x in pmul(qq, binpow(j, alpha, N), N)])
    # H_k coefficients: H_k = sum_j P_j * (1-ju)^{-k}
    c = [mp.mpf(0)] * (M + 1)
    c[0] = mp.mpf(1)
    Hrows = []
    for k in range(0, M + 1):
        L = M + 2 - k
        if L <= 0:
            Hrows.append([])
            continue
        H = [mp.mpf(0)] * L
        for j in range(d + 1):
            if j == 0:
                for i in range(L):
                    H[i] += Ps[0][i]
            else:
                inv = binpow(j, -k, L)
                pj = Ps[j][:L]
                for i in range(L):
                    ai = pj[i]
                    if ai == 0:
                        continue
                    for t in range(L - i):
                        if inv[t] != 0:
                            H[i + t] += ai * inv[t]
        Hrows.append(H)
        if k >= 1:
            s = mp.mpf(0)
            for kk in range(k):
                idx = k + 1 - kk
                if idx < len(Hrows[kk]):
                    s += c[kk] * Hrows[kk][idx]
            c[k] = -s / (gam * k)
    return alpha, c, chk

# ------------------------------------------------ the main kappa computation
def kappa_series(qs, lam, rho, K, M, n_list, a0=None):
    """
    qs: q_0..q_d integer coeff lists; lam: dominant char root (mpf);
    rho: base exponent (usually 0); K: eps-truncation; M: asymptotic terms;
    n_list: sample points n to evaluate at (for convergence check).
    Returns dict n -> kappa series [kappa_0..kappa_K] (normalized kappa_0=1),
    plus (alpha, S0) with S0 = the Stokes constant lim a_n/A(n).
    """
    d = len(qs) - 1
    alpha, c, chk = birkhoff(qs, lam, M)
    nmax = max(n_list)
    # a_n(rho+eps) as eps-series
    a = [[mp.mpf(0)] * (K + 1) for _ in range(nmax + 1)]
    if a0 is None:
        a[0][0] = mp.mpf(1)
    else:
        for i, v in enumerate(a0):
            if i <= K:
                a[0][i] = mp.mpf(v)
    # cache Taylor coefficients of q_j at rho + n - j
    out = {}
    for n in range(1, nmax + 1):
        num = [mp.mpf(0)] * (K + 1)
        for j in range(1, d + 1):
            if n - j < 0:
                continue
            x0 = Fraction(rho) + n - j
            tc = poly_shift_taylor(qs[j], x0, K)
            tcm = [mp.mpf(t.numerator) / mp.mpf(t.denominator) for t in tc]
            pr = smul(tcm, a[n - j], K)
            for i in range(K + 1):
                num[i] -= pr[i]
        x0 = Fraction(rho) + n
        tc = poly_shift_taylor(qs[0], x0, K)
        den = [mp.mpf(t.numerator) / mp.mpf(t.denominator) for t in tc]
        a[n] = sdiv_gen(num, den, K)
        if n in n_list:
            out[n] = a[n]
    res = {}
    loglam = mp.log(lam)
    for n in n_list:
        an = out[n]
        # A(n+eps)/(lam^n n^alpha) = lam^eps (1+eps/n)^alpha F(1/(n+eps))
        f1 = sexp_lin(loglam, K)                       # lam^eps
        # (1+eps/n)^alpha
        g = [mp.mpf(0)] * (K + 1)
        g[1] = mp.mpf(1) / mp.mpf(n)
        lg = slog([mp.mpf(1)] + g[1:], K)
        # careful: build series 1 + eps/n then log then *alpha then exp
        base = [mp.mpf(0)] * (K + 1)
        base[0] = mp.mpf(1)
        base[1] = mp.mpf(1) / mp.mpf(n)
        f2 = sexp(sscale(slog(base, K), alpha, K), K)
        # u = 1/(n+eps) as eps-series
        inv = [mp.mpf(0)] * (K + 1)
        pw = mp.mpf(1) / mp.mpf(n)
        for i in range(K + 1):
            inv[i] = ((-1) ** i) * pw
            pw = pw / mp.mpf(n)
        # F(u)
        F = [mp.mpf(0)] * (K + 1)
        F[0] = c[0]
        up = [mp.mpf(0)] * (K + 1)
        up[0] = mp.mpf(1)
        for k in range(1, M + 1):
            up = smul(up, inv, K)
            if c[k] == 0:
                continue
            for i in range(K + 1):
                F[i] += c[k] * up[i]
        denom = smul(smul(f1, f2, K), F, K)
        T = sdiv(an, denom, K)
        v0 = 0
        while v0 <= K and T[v0] == 0:
            v0 += 1
        kap = sdiv(T[v0:] + [mp.mpf(0)] * v0, [T[v0]] + [mp.mpf(0)] * K, K)
        # Stokes constant  S(0) = lim a_n(rho)/A(n),  A(n)=lam^n n^alpha F(1/n)
        S0 = T[0] / (lam ** mp.mpf(n) * mp.mpf(n) ** alpha)
        res[n] = (kap, S0)
    return res, alpha, c, chk
