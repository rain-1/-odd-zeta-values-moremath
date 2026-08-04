"""eps57_heldout.py -- two referee-mandated finite checks.

PART A: held-out primes for the weight-1 twisted law.  The law
    A(p) = b_p - b*chi_N(p)  (mod p)   for families A, B, C, E, F
(and D's mod-5 rule A(p) - b_p = 2(p mod 5) - 5 mod p) was found on
p <= 23.  Here: p in {29, ..., 97}, genuinely held out.  b_p = [q^p] F
with F = y0(t(q)) computed directly from the recurrence via the Frobenius/
nome construction (no eta input), exact Fractions.

PART B: Veronese saturation for the curve-blindness theorem.  The coupling
lemma reduces the top-graded content of ANY polynomial curve atom to the
degree-5 Veronese image of its first-order direction u1 in Z^3.  Question:
do the directions of the eps41 box {-2..2}^3 already span Sym^5(Q^3)
(dim 21)?  If yes, the finite rank computations certify the top grade for
ALL first-order directions, hence all polynomial curves.  (Same for
Sym^2..Sym^4, used by the sub-top pinning grades.)
"""

from fractions import Fraction as F
from itertools import product as iproduct

# ---------------- Part A ----------------
R2 = {   # family: (a, b, c) with (n+1)^2 u_{n+1} = (a n^2+a n+b) u_n - c n^2 u_{n-1}
    'A': (7, 2, -8), 'B': (9, 3, 27), 'C': (10, 3, 9),
    'D': (11, 3, -1), 'E': (12, 4, 32), 'F': (17, 6, 72),
}
LAW = {  # family: (b-const, character)  chi3 = chi_{-3}, chi4 = chi_{-4}
    'A': (2, 3), 'B': (3, 3), 'C': (3, 3), 'E': (4, 4), 'F': (6, 3),
}

def chi(disc, p):
    if disc == 3:
        return 0 if p % 3 == 0 else (1 if p % 3 == 1 else -1)
    return 0 if p % 2 == 0 else (1 if p % 4 == 1 else -1)

N = 101   # series order (> 97)

def seq_A(a, b, c, N):
    u = [F(1), F(b)]
    for n in range(1, N):
        u.append((F(a * n * n + a * n + b) * u[n] - F(c * n * n) * u[n - 1])
                 / F((n + 1) ** 2))
    return u

def frobenius_g(a, b, c, y0, N):
    """g with L(y0 log t + g) = 0 for L = th^2 - t(a th^2+a th+b) + c t^2 (th+1)^2.
    L(y0 log t) = log t L(y0) + Lprime(y0) where Lprime = dL/dtheta:
    Lprime = 2 th - t(2a th + a) + c t^2 * 2(th+1).
    Solve L(g) = -Lprime(y0) order by order, g0 = 0."""
    rhs = [F(0)] * (N + 1)
    for n in range(N):
        # Lprime(y0) coefficient at t^n:
        v = F(2 * n) * y0[n]
        if n >= 1:
            v -= F(2 * a * (n - 1) + a) * y0[n - 1]
        if n >= 2:
            v += F(2 * c) * F(n - 1) * y0[n - 2]
        rhs[n] = -v
    g = [F(0)] * (N + 1)
    for n in range(1, N):
        # [t^n] L(g) = n^2 g_n - (a(n-1)^2+a(n-1)+b) g_{n-1} + c n^2? careful:
        # L(g)_n = n^2 g_n - (a(n-1)^2 + a(n-1) + b) g_{n-1} + c (n-1)^2 g_{n-2}
        acc = rhs[n]
        acc += F(a * (n - 1) ** 2 + a * (n - 1) + b) * g[n - 1]
        if n >= 2:
            acc -= F(c) * F((n - 1) ** 2) * g[n - 2]
        g[n] = acc / F(n * n)
    return g

def compose(series, inner, N):
    """series(t) with t -> inner(q), inner[0]=0, inner[1]=1; power method."""
    out = [F(0)] * N
    out[0] = series[0]
    tp = [F(0)] * N     # inner^k
    tp[0] = F(1)
    for k in range(1, N):
        # tp *= inner
        ntp = [F(0)] * N
        for i in range(N):
            if tp[i]:
                for j in range(1, N - i):
                    if inner[j]:
                        ntp[i + j] += tp[i] * inner[j]
        tp = ntp
        if k < len(series) and series[k]:
            for i in range(N):
                out[i] += series[k] * tp[i]
    return out

def revert(qs, N):
    """functional inverse of q(t) = t + ..., i.e. t(q); Newton on series."""
    tq = [F(0)] * N
    tq[1] = F(1)
    for order in range(2, N):
        cur = compose(qs, tq, order + 1)
        err = cur[order]
        tq[order] -= err
    return tq

def expseries(x, N):
    out = [F(0)] * N
    out[0] = F(1)
    term = [F(0)] * N
    term[0] = F(1)
    for k in range(1, N):
        nt = [F(0)] * N
        for i in range(N):
            if term[i]:
                for j in range(1, N - i):
                    if x[j]:
                        nt[i + j] += term[i] * x[j]
        term = [v / F(k) for v in nt]
        for i in range(N):
            out[i] += term[i]
        if all(v == 0 for v in term):
            break
    return out

def series_div(a, b, N):
    inv = [F(0)] * N
    inv[0] = F(1) / b[0]
    for n in range(1, N):
        inv[n] = -sum(b[k] * inv[n - k] for k in range(1, n + 1)) / b[0]
    out = [F(0)] * N
    for i in range(N):
        s = sum(a[k] * inv[i - k] for k in range(i + 1))
        out[i] = s
    return out

print('PART A: held-out primes 29..97 for the weight-1 law')
PRIMES = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
results = {}
for fam, (a, b, c) in R2.items():
    y0 = seq_A(a, b, c, N)
    g = frobenius_g(a, b, c, y0, N)
    goy = series_div(g, y0, N)
    qs_exp = expseries(goy, N)
    qs = [F(0)] * N
    for i in range(N - 1):
        qs[i + 1] = qs_exp[i]          # q = t * exp(g/y0)
    tq = revert(qs, N)
    Fq = compose(y0, tq, N)
    row = []
    for p in PRIMES:
        Ap = y0[p]
        bp = Fq[p]
        assert Ap.denominator == 1 and bp.denominator == 1
        Ap, bp = int(Ap), int(bp)
        if fam == 'D':
            lhs = (Ap - bp) % p
            rhs = (2 * (p % 5) - 5) % p
        else:
            bc, disc = LAW[fam]
            lhs = Ap % p
            rhs = (bp - bc * chi(disc, p)) % p
        row.append('OK' if lhs == rhs else 'FAIL(p=%d)' % p)
    results[fam] = row
    ok = all(x == 'OK' for x in row)
    print('  %-2s : %s' % (fam, 'ALL 16 HELD-OUT PRIMES PASS' if ok
                           else ' '.join(x for x in row if x != 'OK')))

# ---------------- Part B ----------------
print()
print('PART B: Veronese saturation of the direction box {-2..2}^3')
def sym_rank(deg, box):
    monos = [(i, j, deg - i - j) for i in range(deg + 1)
             for j in range(deg + 1 - i)]
    rows = []
    seen = set()
    for v in box:
        if v == (0, 0, 0):
            continue
        # projective dedupe
        from math import gcd
        g = gcd(gcd(abs(v[0]), abs(v[1])), abs(v[2]))
        vv = tuple(x // g for x in v) if g else v
        if vv in seen or tuple(-x for x in vv) in seen:
            continue
        seen.add(vv)
        rows.append([F(v[0] ** i * v[1] ** j * v[2] ** k)
                     for (i, j, k) in monos])
    # rank over Q
    m = len(monos)
    r = 0
    for col in range(m):
        piv = None
        for i in range(r, len(rows)):
            if rows[i][col] != 0:
                piv = i
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        pv = rows[r][col]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][col] != 0:
                f0 = rows[i][col]
                rows[i] = [x - f0 * y for x, y in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r, m

box = list(iproduct(range(-2, 3), repeat=3))
for deg in (2, 3, 4, 5):
    r, m = sym_rank(deg, box)
    print('  deg %d: rank %d of dim %d -> %s'
          % (deg, r, m, 'SATURATED' if r == m else 'NOT saturated'))
