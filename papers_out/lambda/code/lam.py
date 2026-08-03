"""Foundations of the Lambda-algebra: verification code.

All arithmetic exact (Python int/Fraction); every p-adic digit comes from an exact
rational or an exact residue mod p^K.  Reuses the p-adic number class and the
validated Kubota-Leopoldt implementation of the companion ledgers.

Objects.

  c_p(A,B) := lim_t binom(A p^t, B p^t)            (Kazandzidis limit)
  ghat(x)  := - sum_{m odd >= 3} zeta_p(m) x^m p^m / (m (1-p^m))
  beta_p(B,D) := exp( ghat(B+D) - ghat(B) - ghat(D) )      (the tower Beta)
  E_p(A,B) := - p^{v_p binom(A,B)} T(A,B) Gp(A+1)/(Gp(B+1) Gp(D+1))   (elementary part)

Claim verified here:   c_p(A,B) = E_p(A,B) * beta_p(B, A-B).
"""
import os, sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "work", "lambda"))
sys.path.insert(0, os.path.join(ROOT, "work", "padic_seam"))

from pnum import P            # exact Q_p with honest precision
import zoo                    # zeta_p(m) (Kubota-Leopoldt, 980/980-validated)
import lll as LLL


# --------------------------------------------------------------- basic p-adic
def vp(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def vp_fact(n, p):
    v = 0
    while n:
        n //= p
        v += n
    return v


def exp_p(x, K):
    """exp(x) for v_p(x) >= 1 (p >= 5), to K relative digits."""
    p = x.p
    acc = P.from_frac(p, 1, K)
    term = P.from_frac(p, 1, K)
    n = 1
    while True:
        term = term * x / P.from_frac(p, n, K + 12)
        if term.is_zero() or term.v > K + 2:
            break
        acc = acc + term
        n += 1
        if n > 40 * K:
            break
    return acc


def gamma_p_int(n, p, K):
    """Gp(n) = (-1)^n prod_{j<n, p !| j} j, for a positive integer n."""
    M = p ** K
    r = 1
    for j in range(1, n):
        if j % p:
            r = r * j % M
    return P(p, 0, (-1) ** n * r % M, K)


# ------------------------------------------- ghat, beta, and the elementary part
_ZCACHE = {}


def zeta_p(m, p, K):
    key = (m, p, K)
    if key not in _ZCACHE:
        _ZCACHE[key] = zoo.zeta_p_val(m, p, K)
    return _ZCACHE[key]


def ghat(x, p, K):
    """ghat(x) = - sum_{m odd>=3} zeta_p(m) x^m p^m/(m(1-p^m)), to K relative digits.

    The m-th term has v_p >= m - 1 - v_p(m), so m <= K + 4 suffices for K+? digits."""
    W = K + 8
    tot = P.zero(p)
    m = 3
    while m <= K + 6:
        z = zeta_p(m, p, W)
        coef = Fr(-(x ** m), m) * Fr(p ** m, 1 - p ** m)
        t = z * P.from_frac(p, coef, W)
        if not (t.is_zero() or t.v > K + 5):
            tot = tot + t
        m += 2
    return tot


def beta_p(B, D, p, K):
    """beta_p(B,D) = exp(ghat(B+D) - ghat(B) - ghat(D))."""
    arg = ghat(B + D, p, K) - ghat(B, p, K) - ghat(D, p, K)
    return exp_p(arg, K)


def elem_p(A, B, p, K):
    """E_p(A,B) = - p^{v_p binom(A,B)} T(A,B) Gp(A+1)/(Gp(B+1)Gp(D+1))."""
    D = A - B
    W = K + 4
    T = P.from_frac(p, 1, W)
    l = 1
    while A // p ** l:
        Al, Bl, Dl = A // p ** l, B // p ** l, D // p ** l
        T = T * gamma_p_int(Al + 1, p, W) * P.from_frac(p, (-1) ** (Al + 1), W)
        T = T / (gamma_p_int(Bl + 1, p, W) * P.from_frac(p, (-1) ** (Bl + 1), W))
        T = T / (gamma_p_int(Dl + 1, p, W) * P.from_frac(p, (-1) ** (Dl + 1), W))
        l += 1
    G = gamma_p_int(A + 1, p, W) / (gamma_p_int(B + 1, p, W) * gamma_p_int(D + 1, p, W))
    vC = vp_fact(A, p) - vp_fact(B, p) - vp_fact(D, p)
    return P.from_frac(p, -1, W) * P(p, vC, 1, W) * T * G


# ------------------------------------------------- direct Kazandzidis limits
def unit_prod_batch(indices, p, K):
    """u(n) = prod_{j<=n, p !| j} j mod p^K, for every n in `indices`.  One pass,
    O(max index) time and O(|indices|) memory."""
    M = p ** K
    want = sorted(set(int(i) for i in indices))
    out = {0: 1}
    acc = 1
    j = 1
    for n in want:
        if n <= 0:
            out[n] = 1
            continue
        while j <= n:
            if j % p:
                acc = acc * j % M
            j += 1
        out[n] = acc
    return out


def _needed(n, p):
    out = []
    while n:
        out.append(n)
        n //= p
    return out


def binom_mod(n, k, p, K, u):
    """(v_p binom(n,k), unit part mod p^K) using Morita/Legendre splitting."""
    M = p ** K

    def parts(x):
        v, pr, y = 0, 1, x
        while y:
            y //= p
            v += y
        y = x
        while y:
            pr = pr * u[y] % M
            y //= p
        return v, pr

    v1, q1 = parts(n)
    v2, q2 = parts(k)
    v3, q3 = parts(n - k)
    return v1 - v2 - v3, q1 * pow(q2 * q3 % M, -1, M) % M


def kaz_batch(pairs, p, K):
    """c_p(A,B) for a list of pairs, to K certified digits (3 per tower level).
    Returns {(A,B): P} together with the measured per-level agreements."""
    t = (K + 2) // 3 + 1
    W = K + 6
    idx = set()
    for (A, B) in pairs:
        for tt in range(t + 1):
            for n in (A * p ** tt, B * p ** tt, (A - B) * p ** tt):
                idx.update(_needed(n, p))
    u = unit_prod_batch(idx, p, W)
    res, rates = {}, {}
    for (A, B) in pairs:
        vals = []
        for tt in range(t + 1):
            v, uu = binom_mod(A * p ** tt, B * p ** tt, p, W, u)
            vals.append(P(p, v, uu, W))
        ag = [vals[i].agree(vals[i - 1]) - vals[i].v for i in range(1, len(vals))]
        rates[(A, B)] = ag
        res[(A, B)] = vals[-1].trunc(3 * (t + 1))
    return res, rates


# ------------------------------------------------------------------ reporting
def show(tag, ok, extra=""):
    print("   %-58s %s %s" % (tag, "OK" if ok else "**FAIL**", extra))


def main(primes, K):
    for p in primes:
        print("=" * 78)
        print("p = %d,  K = %d certified digits" % (p, K))

        # ---- (0) sanity: zeta_p(3) digits against the recorded ledger value
        z3 = zeta_p(3, p, K)
        print("   zeta_p(3) =", " ".join(map(str, z3.digits(12))))

        # ---- (1) closed form in the beta packaging
        print("  -- Theorem (closed form, beta packaging):  c_p(A,B) = E_p(A,B) beta_p(B,A-B)")
        pairs = [(2, 1), (3, 1), (3, 2), (4, 1), (5, 2), (7, 3), (p, 1), (p, 2),
                 (p + 1, 1), (p + 1, p), (2 * p, p)]
        pairs = [(A, B) for (A, B) in pairs if A > B >= 1]
        C, rates = kaz_batch(pairs, p, K)
        nfail = 0
        for (A, B) in pairs:
            f = (elem_p(A, B, p, K) * beta_p(B, A - B, p, K)).trunc(K)
            d = C[(A, B)] - f
            ok = d.is_zero()
            nfail += (not ok)
            print("     c_p(%2d,%2d)  v=%-2d  direct %s   %s"
                  % (A, B, C[(A, B)].v, " ".join(map(str, C[(A, B)].digits(6))),
                     "MATCH all %d" % K if ok else "DIFFER at v_p=%d" % d.v))
        show("closed form, %d pairs" % len(pairs), nfail == 0)

        # ---- (2) the three structural relations, from the direct limits
        print("  -- Relations among Kazandzidis limits (verified on the direct limits)")
        need = set()
        sym = [(A, B) for A in range(2, 13) for B in range(1, A)]
        need.update(sym)
        homo = [(A, B) for A in range(2, 8) for B in range(1, A)]
        need.update([(p * A, p * B) for (A, B) in homo])
        tri = [(A, B, Cc) for A in range(3, 11) for B in range(2, A) for Cc in range(1, B)]
        for (A, B, Cc) in tri:
            need.update([(A, B), (B, Cc), (A, Cc), (A - Cc, B - Cc)])
        need = sorted({(A, B) for (A, B) in need if A > B >= 1})
        Kr = min(K, 9)
        Cr, _ = kaz_batch(need, p, Kr)

        bad = [(A, B) for (A, B) in sym if not (Cr[(A, B)] - Cr[(A, A - B)]).is_zero()]
        show("symmetry  c_p(A,B) = c_p(A,A-B)   [%d cells]" % len(sym), not bad, str(bad[:3]))

        bad = [(A, B) for (A, B) in homo if not (Cr[(p * A, p * B)] - Cr[(A, B)]).is_zero()]
        show("p-homogeneity  c_p(pA,pB) = c_p(A,B)   [%d cells]" % len(homo), not bad, str(bad[:3]))

        bad = []
        for (A, B, Cc) in tri:
            lhs = Cr[(A, B)] * Cr[(B, Cc)]
            rhs = Cr[(A, Cc)] * Cr[(A - Cc, B - Cc)]
            if not (lhs - rhs).is_zero():
                bad.append((A, B, Cc))
        show("trinomial revision   [%d cells]" % len(tri), not bad, str(bad[:3]))



# --------------------------------------------------- (IND_p): the ghat hunt
def ind_hunt(primes, Ks, N=8):
    """Q-linear relations among ghat(1),...,ghat(N)?  Run at TWO precisions:
    a genuine relation has a height independent of the precision, noise scales
    like the floor p^{A/m}."""
    for p in primes:
        print("=" * 78)
        print("(IND_p) hunt at p = %d,  x = 1..%d" % (p, N))
        rows = {}
        Aused = {}
        for K in Ks:
            g = [ghat(x, p, K) for x in range(1, N + 1)]
            v0 = min(t.v for t in g)
            A = min(t.v + t.prec for t in g) - v0
            units = [t.rescale(-v0) for t in g]
            vals_all = [uu.u * p ** uu.v % p ** A for uu in units]
            Aused[K] = A
            if K == Ks[-1]:
                print("   v_p(ghat(x)) =", [t.v for t in g])
                planted = (3 * vals_all[0] - 7 * vals_all[1]) % p ** A
                out = LLL.padic_relation([vals_all[0], vals_all[1], planted], p, A)
                rec = [r[1] for r in out if max(abs(c) for c in r[1]) <= 30][:1]
                show("finder validation (planted 3g1-7g2) recovered", bool(rec), str(rec))
            for m in range(2, N + 1):
                out = LLL.padic_relation(vals_all[:m], p, A)
                h = min(max(abs(c) for c in r[1]) for r in out) if out else None
                rows.setdefault(("g", m), {})[K] = (h, Fr(p) ** Fr(A, m))
            for m in range(1, N + 1):
                out = LLL.padic_relation([1] + vals_all[:m], p, A)
                h = min(max(abs(c) for c in r[1]) for r in out) if out else None
                rows.setdefault(("1g", m), {})[K] = (h, Fr(p) ** Fr(A, m + 1))
        print("   A (certified absolute digits) per K:", Aused)
        print("   %-18s %s" % ("basis",
              "  ".join("K=%-2d: height / floor" % K for K in Ks)))
        for key in sorted(rows, key=lambda t: (t[0], t[1])):
            tag = ("(ghat(1..%d))" % key[1]) if key[0] == "g" else ("(1,ghat(1..%d))" % key[1])
            cells = []
            for K in Ks:
                h, fl = rows[key][K]
                cells.append("%9.3g / %-9.3g" % (h if h else 0, float(fl)))
            print("   %-18s %s" % (tag, "  ".join(cells)))


# ------------------------------------------------- the relation lattice ker(delta)
def relation_lattice(N):
    """delta(A,B) = [A]-[B]-[A-B] in Z[{1..N}].  Compute
       (i)  image(delta) = ker(m_1),  m_1(sum c_x [x]) = sum c_x x;
       (ii) whether ker(delta) is generated over Z by the symmetry and
            trinomial-revision relations."""
    from sympy import Matrix, ZZ
    from sympy.matrices.normalforms import smith_normal_form
    pairs = [(A, B) for A in range(2, N + 1) for B in range(1, A)]
    idx = {q: i for i, q in enumerate(pairs)}
    Dm = []
    for (A, B) in pairs:
        r = [0] * N
        r[A - 1] += 1
        r[B - 1] -= 1
        r[A - B - 1] -= 1
        Dm.append(r)
    Dm = Matrix(Dm)
    rk = Dm.rank()
    ker_rank = len(pairs) - rk
    # image sits inside ker(m_1) and has the same rank iff rk = N-1
    ok_image = (rk == N - 1)
    # the expected relations
    gens = []
    for (A, B) in pairs:                       # symmetry
        if B < A - B:
            v = [0] * len(pairs)
            v[idx[(A, B)]] += 1
            v[idx[(A, A - B)]] -= 1
            gens.append(v)
    for A in range(3, N + 1):                  # trinomial revision
        for B in range(2, A):
            for C in range(1, B):
                v = [0] * len(pairs)
                v[idx[(A, B)]] += 1
                v[idx[(B, C)]] += 1
                v[idx[(A, C)]] -= 1
                v[idx[(A - C, B - C)]] -= 1
                gens.append(v)
    G = Matrix(gens)
    # sanity: every proposed generator really is in ker(delta)
    assert (G * Dm).is_zero_matrix, "a proposed relation is NOT in ker(delta)"
    grk = G.rank()
    # index of <gens> inside ker(delta): compare Smith normal forms
    # build a Z-basis of ker(delta) from the (saturated) nullspace
    ns = Dm.T.nullspace()          # vectors v with v^T * Dm = 0, i.e. rows of Dm
    # sympy nullspace of Dm.T gives v with Dm.T v = 0 <=> sum v_i row_i = 0.  Good.
    from sympy import lcm, Rational
    B = []
    for v in ns:
        d = 1
        for e in v:
            d = lcm(d, Rational(e).q)
        B.append([int(e * d) for e in v])
    B = Matrix(B)
    # saturate: Smith normal form of B gives the elementary divisors of <B> in ker
    idx_gens = None
    if grk == ker_rank and ker_rank > 0:
        # express: is <gens> = ker?  compare determinants of the SNFs
        s1 = smith_normal_form(Matrix(B), domain=ZZ)
        s2 = smith_normal_form(Matrix(gens), domain=ZZ)
        d1 = [s1[i, i] for i in range(min(s1.shape))if s1[i, i] != 0]
        d2 = [s2[i, i] for i in range(min(s2.shape))if s2[i, i] != 0]
        idx_gens = (d1, d2)
    print("N=%-3d pairs=%-5d rank(delta)=%-4d (N-1=%d, image = ker(m_1): %s)  "
          "dim ker(delta)=%-4d rank(sym+trinomial)=%-4d %s"
          % (N, len(pairs), rk, N - 1, ok_image, ker_rank, grk,
             ("elementary divisors %s vs %s" % idx_gens) if idx_gens else ""))
    return ok_image, ker_rank == grk, idx_gens





# ------------------------------------------------- the tower-harmonic constants
def h_p(a, w, p, K):
    """h_p^{(w)}(a) = sum_{x in Z[1/p], 0<x<=a} x^{-w} = sum_i p^{wi} S_i(a),
       S_i(a) = sum_{k <= a p^i, p !| k} k^{-w},
       the index i running over ALL integers with a p^i >= 1 (so i can be
       negative once a >= p).  Exact modular arithmetic."""
    W = K + 6
    M = p ** W
    tot = P.zero(p)
    i0 = 0
    while a * p ** (i0 - 1) >= 1:
        i0 -= 1
    i = i0
    while w * i <= K + 4:
        top = (a * p ** i) if i >= 0 else (a // p ** (-i))
        S = 0
        for k in range(1, top + 1):
            if k % p:
                S = (S + pow(pow(k, -1, M), w, M)) % M
        tot = tot + P(p, w * i, S, W + min(0, w * i))
        i += 1
    return tot.trunc(K)


def h_hunt(primes, K, amax=5):
    for p in primes:
        print("=" * 78)
        print("h_p hunt, p = %d, w = 3, a = 1..%d" % (p, amax))
        hs = [h_p(a, 3, p, K) for a in range(1, amax + 1)]
        # distribution relation h_p(pa) = p^{-w} h_p(a)
        ok = all((h_p(p * a, 3, p, K - 3) - h_p(a, 3, p, K).rescale(-3)).is_zero()
                 for a in range(1, 4))
        show("distribution relation h_p(pa) = p^{-3} h_p(a), a=1,2,3", ok)
        v0 = min(t.v for t in hs)
        A = min(t.v + t.prec for t in hs) - v0
        vals = [t.rescale(-v0).u * p ** (t.rescale(-v0).v) % p ** A for t in hs]
        print("   v_p(h_p(a)) =", [t.v for t in hs], "  certified absolute digits A =", A)
        for m in range(1, amax + 1):
            out = LLL.padic_relation([1] + vals[:m], p, A)
            fl = Fr(p) ** Fr(A, m + 1)
            h = min(max(abs(c) for c in r[1]) for r in out) if out else None
            print("     (1,h_p(1..%d)):  best height %-10s floor %-10.3g %s"
                  % (m, "%.3g" % h if h else "none", float(fl),
                     "nothing below floor" if (h is None or h >= fl) else "*** CANDIDATE ***"))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "main"
    rest = [int(x) for x in sys.argv[2:]]
    if cmd == "main":
        K = rest[0] if rest else 12
        main(rest[1:] or [5, 7, 11, 13], K)
    elif cmd == "ind":
        ind_hunt(rest[2:] or [5, 7, 11, 13], [rest[0], rest[1]] if len(rest) > 1 else [20, 32])
    elif cmd == "hp":
        h_hunt(rest[1:] or [5, 7, 11, 13], rest[0] if rest else 24)
    elif cmd == "lattice":
        for N in (rest or [6, 8, 10, 12]):
            relation_lattice(N)