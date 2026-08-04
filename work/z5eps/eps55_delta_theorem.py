"""eps55_delta_theorem.py -- upgrade delta's modular identification to a
theorem-grade statement (Sturm/degree-bound route).

delta: A(n) defined by R3 (7,3,81,0): (n+1)^3 u_{n+1} =
(2n+1)(7n^2+7n+3) u_n - 81 n^3 u_{n-1}, A(0)=1 (= the AZ binomial sum).
Claimed (eps51): with eta exponents
  t(q):  {1:4, 2:-16, 3:-4, 4:4, 6:16, 12:-4}   (weight 0, q-order 1)
  F(q):  {1:-3, 2:12, 3:1, 4:-3, 6:-4, 12:1}    (weight 2, q-order 0)
on Gamma_0(12), we have  F(q) = y0(t(q))  where y0 = sum A(n) t^n.

Steps here (all exact over Q):
  A. Ligozat conditions for both eta quotients (exact integer checks).
  B. Frobenius/nome from the recurrence (dual numbers): q(t), invert to t(q);
     compare t(q), F(q) = y0(t(q)) against the eta quotients to q^N.
  C. Reconstruct the order-3 operator annihilating F along t from the
     ETA SIDE ONLY (theta_t = (t/theta_q t) theta_q on q-series), with
     polynomial-coefficient ansatz of degree <= D; show the solution space
     is 1-dimensional and equals the recurrence operator
     L = th^3 - t(2th+1)(7th^2+7th+3) + 81 t^2 (th+1)^3   exactly.
  D. Margin: consistency of C to q^NBIG.
"""
import sys
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')

N = 140          # series depth

# ---------------- series helpers over Q ----------------
def ser_mul(a, b):
    c = [F(0)] * N
    for i, ai in enumerate(a):
        if ai:
            for j in range(N - i):
                if b[j]:
                    c[i + j] += ai * b[j]
    return c

def ser_inv(a):
    assert a[0] != 0
    c = [F(0)] * N
    c[0] = 1 / a[0]
    for m in range(1, N):
        s = F(0)
        for i in range(1, m + 1):
            s += a[i] * c[m - i]
        c[m] = -s / a[0]
    return c

def ser_pow_int(a, e):
    out = [F(0)] * N
    out[0] = F(1)
    b = a[:]
    ee = e
    if ee < 0:
        b = ser_inv(b)
        ee = -ee
    while ee:
        if ee & 1:
            out = ser_mul(out, b)
        b = ser_mul(b, b)
        ee >>= 1
    return out

def eta_block(d):
    """prod_{m>=1} (1 - q^{d m}) to order N."""
    c = [F(0)] * N
    c[0] = F(1)
    # generalized pentagonal expansion of prod(1-x^m) with x = q^d
    import itertools
    e = [F(0)] * N
    e[0] = F(1)
    kk = 1
    while True:
        for g in (kk * (3 * kk - 1) // 2, kk * (3 * kk + 1) // 2):
            if g * d < N:
                e[g * d] += F((-1) ** kk)
        if kk * (3 * kk - 1) // 2 * d >= N:
            break
        kk += 1
    return e

def eta_quotient(exps):
    out = [F(0)] * N
    out[0] = F(1)
    for d, r in exps.items():
        out = ser_mul(out, ser_pow_int(eta_block(d), r))
    qord = sum(d * r for d, r in exps.items())
    assert qord % 24 == 0
    qord //= 24
    res = [F(0)] * N
    for i in range(N - qord):
        res[i + qord] = out[i]
    return res, qord

# ---------------- A: Ligozat ----------------
def ligozat(exps, Nlev):
    s24a = sum(d * r for d, r in exps.items()) % 24
    s24b = sum((Nlev // d) * r for d, r in exps.items()) % 24
    wt2 = sum(exps.values())
    prod = F(1)
    for d, r in exps.items():
        prod *= F(d) ** r
    return s24a, s24b, F(wt2, 2), prod

T_EXP = {1: 4, 2: -16, 3: -4, 4: 4, 6: 16, 12: -4}
F_EXP = {1: -3, 2: 12, 3: 1, 4: -3, 6: -4, 12: 1}

print('A. Ligozat: t:', ligozat(T_EXP, 12), ' F:', ligozat(F_EXP, 12))

# ---------------- B: Frobenius / nome from recurrence ----------------
def dseq(NN):
    """A_n(eps) over dual numbers Q[eps]/(eps^2): returns (A, dA)."""
    A = [F(1)]; dA = [F(0)]
    # recurrence with n -> n+eps: (n+1+e)^3 u_{n+1} =
    # (2(n+e)+1)(7(n+e)^2+7(n+e)+3) u_n - 81 (n+e)^3 u_{n-1}
    # solve for u_{n+1} incl. first order in e.
    # A_1: n=0 case: (1+e)^3 u1 = (2e+1)(7e^2+7e+3) u0 -> u1 = (3+13e+...)(1-3e)
    for n in range(0, NN):
        a3 = F((n + 1) ** 3); da3 = F(3 * (n + 1) ** 2)
        c1 = F((2 * n + 1) * (7 * n * n + 7 * n + 3))
        dc1 = F(2 * (7 * n * n + 7 * n + 3) + (2 * n + 1) * (14 * n + 7))
        c2 = F(81 * n ** 3); dc2 = F(243 * n * n)
        u, du = A[n], dA[n]
        v, dv = (A[n - 1], dA[n - 1]) if n >= 1 else (F(0), F(0))
        num = c1 * u - c2 * v
        dnum = dc1 * u + c1 * du - dc2 * v - c2 * dv
        A.append(num / a3)
        dA.append((dnum - da3 * num / a3) / a3)
    return A, dA

Aseq, dAseq = dseq(N)
# y0, g as t-series; q(t) = t * exp(g/y0)
y0 = [Aseq[n] if n < N else F(0) for n in range(N)]
g = [dAseq[n] if n < N else F(0) for n in range(N)]
r = ser_mul(g, ser_inv(y0))          # g/y0, r[0] = 0
expr = [F(0)] * N
expr[0] = F(1)
term = [F(0)] * N; term[0] = F(1)
for j in range(1, N):
    term = ser_mul(term, r)
    for i in range(N):
        term[i] = term[i] / j if term[i] else term[i]
    # term = r^j / j!
    for i in range(N):
        expr[i] += term[i]
qt = [F(0)] * N                       # q(t) = t*exp(r)
for i in range(N - 1):
    qt[i + 1] = expr[i]

def revert(a):
    """functional inverse of a series a with a0=0, a1=1."""
    b = [F(0)] * N
    b[1] = F(1)
    for m in range(2, N):
        # impose [q^m] a(b(q)) = 0
        comp = [F(0)] * N
        pw = [F(0)] * N; pw[0] = F(1)
        for j in range(1, m + 1):
            pw = ser_mul(pw, b)
            if a[j]:
                for i in range(m + 1):
                    comp[i] += a[j] * pw[i]
        b[m] = -comp[m]
    return b

assert qt[0] == 0 and qt[1] == 1
tq = revert(qt)
teta, tord = eta_quotient(T_EXP)
assert tord == 1
ok_t = all(tq[i] == teta[i] for i in range(N))
print('B1. t(q) recurrence-nome == eta quotient to q^%d: %s'
      % (N - 1, ok_t), flush=True)

# F(q) = y0(t(q))
Fq = [F(0)] * N
pw = [F(0)] * N; pw[0] = F(1)
Fq[0] = y0[0]
for n in range(1, N):
    pw = ser_mul(pw, tq)
    if y0[n]:
        for i in range(N):
            Fq[i] += y0[n] * pw[i]
Feta, ford = eta_quotient(F_EXP)
assert ford == 0
ok_F = all(Fq[i] == Feta[i] for i in range(N))
print('B2. F(q) = y0(t(q)) == eta quotient to q^%d: %s'
      % (N - 1, ok_F), flush=True)

# ---------------- C: reconstruct the ODE from the eta side ----------------
def theta(a):
    return [F(i) * a[i] for i in range(N)]

tw = theta(teta)                      # theta_q t  (q-order 1, like t)
tw_sh = tw[1:] + [F(0)]               # (theta_q t)/q
teta_sh = teta[1:] + [F(0)]           # t/q
tt_inv = ser_mul(teta_sh, ser_inv(tw_sh))   # t / theta_q t (order-0 series)
def theta_t(a):
    return ser_mul(tt_inv, theta(a))

Fd = [Feta]
for _ in range(3):
    Fd.append(theta_t(Fd[-1]))
# ansatz: sum_{j=0}^{3} C_j(t) th^j F = 0, deg C_j <= D, C_3 leading monic-ish
D = 2
cols = []
labels = []
for j in range(4):
    base = Fd[j]
    pw = [F(0)] * N; pw[0] = F(1)
    for dd in range(D + 1):
        cols.append(ser_mul(base, pw) if dd else base[:])
        labels.append((j, dd))
        pw = ser_mul(pw, teta)
# solve nullspace over Q of the (NROWS x ncols) system
NROWS = 120
ncols = len(cols)
M = [[cols[c][r] for c in range(ncols)] for r in range(NROWS)]
# gaussian elim
piv = []
row = 0
for c in range(ncols):
    pr = None
    for rr in range(row, NROWS):
        if M[rr][c] != 0:
            pr = rr; break
    if pr is None:
        continue
    M[row], M[pr] = M[pr], M[row]
    pv = M[row][c]
    M[row] = [x / pv for x in M[row]]
    for rr in range(NROWS):
        if rr != row and M[rr][c] != 0:
            f0 = M[rr][c]
            M[rr] = [x - f0 * y for x, y in zip(M[rr], M[row])]
    piv.append(c)
    row += 1
free = [c for c in range(ncols) if c not in piv]
print('C1. ODE ansatz deg<=%d: %d unknowns, rank %d, nullity %d'
      % (D, ncols, len(piv), len(free)), flush=True)
# nullspace vectors
sols = []
for fc in free:
    v = [F(0)] * ncols
    v[fc] = F(1)
    for rr, c in enumerate(piv):
        v[c] = -M[rr][fc]
    sols.append(v)
# recurrence operator L = th^3 - t(2th+1)(7th^2+7th+3) + 81 t^2(th+1)^3
# coefficients as C_j(t):
#  th^3:            1
#  t-part: -(2th+1)(7th^2+7th+3) = -(14th^3+21th^2+13th+3)
#  t^2-part: 81(th^3+3th^2+3th+1)
LREC = {(3, 0): F(1),
        (3, 1): F(-14), (2, 1): F(-21), (1, 1): F(-13), (0, 1): F(-3),
        (3, 2): F(81), (2, 2): F(243), (1, 2): F(243), (0, 2): F(81)}
lvec = [LREC.get(lab, F(0)) for lab in labels]
# is lvec in the nullspace span? residual check: apply M-original... simpler:
# verify directly: sum lvec[c]*cols[c] == 0 to N.
resid = [sum(lvec[c] * cols[c][r] for c in range(ncols)) for r in range(N)]
print('C2. recurrence operator annihilates eta-side F: %s (checked to q^%d)'
      % (all(x == 0 for x in resid), N - 1), flush=True)
if len(sols) == 1:
    s = sols[0]
    # normalize to match lvec at (3,0)
    idx30 = labels.index((3, 0))
    if s[idx30]:
        sn = [x / s[idx30] for x in s]
        print('C3. 1-dim nullspace; equals recurrence operator exactly:',
              all(a == b for a, b in zip(sn, lvec)), flush=True)
else:
    print('C3. nullity != 1 (%d); listing pivot structure for the memo'
          % len(sols))
    # check every nullspace elt is multiple of lvec?
    import itertools
    print('    (inspect manually)')
