"""eps56_half_apery.py -- the half-Apery numbers: full data battery.

u(t) = sqrt(sum a_n t^n),  a_n = Apery zeta(3) numbers,
utilde_n = 4^n [t^n] u.

1. integrality of utilde to n<=200 + recurrence check
2. v2 pattern, sharp rescale exponent
3. Lucas-type congruences mod p = 3,5,7,11,13
4. q-side: u(t(q)) vs sqrt(F(q)); 2-adic behaviour of q-coefficients;
   theta/Eisenstein comparisons at discriminant -24
5. upstairs: 8^n [t^n] Q^{1/4} for the BZ zeta(5) row, same battery
"""

import sys
from fractions import Fraction as F
from math import comb

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
import core

N = 201

# ---------------- 1. the sequence ----------------
a = [sum(F(comb(n, k) ** 2 * comb(n + k, k) ** 2) for k in range(n + 1))
     for n in range(N)]

def sqrt_series(f, n):
    """sqrt of series f (f[0]=1), n terms, exact Fractions."""
    u = [F(1)]
    for m in range(1, n):
        s = f[m] - sum(u[i] * u[m - i] for i in range(1, m))
        u.append(s / 2)
    return u

u = sqrt_series(a, N)
ut = [u[n] * F(4) ** n for n in range(N)]
ok = all(x.denominator == 1 for x in ut)
print('utilde integral to n=%d: %s' % (N - 1, ok))
ut = [int(x) for x in ut]
print('utilde[0:8] =', ut[:8])

# recurrence check: n^2 ut_n = (136n^2-204n+78) ut_{n-1} - 4(2n-3)^2 ut_{n-2}
bad = 0
for n in range(2, N):
    lhs = n * n * ut[n]
    rhs = (136 * n * n - 204 * n + 78) * ut[n - 1] \
        - 4 * (2 * n - 3) ** 2 * ut[n - 2]
    if lhs != rhs:
        bad += 1
print('recurrence n^2 ut_n = (136n^2-204n+78)ut_{n-1} - 4(2n-3)^2 ut_{n-2}:',
      'PASS' if bad == 0 else 'FAIL %d' % bad)

# ---------------- 2. v2 pattern ----------------
def v2(x):
    if x == 0:
        return 999
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v

vs = [v2(x) for x in ut]
print('v2(utilde_n), n=0..40:', vs[:41])
# compare with candidate: v2 = v2(n)+1? or s2-related
cand1 = [0] + [v2(n) + 1 for n in range(1, N)]
print('v2 == v2(n)+1 (n>=1)?', vs[1:] == cand1[1:])
if vs[1:] != cand1[1:]:
    diffs = [(n, vs[n], cand1[n]) for n in range(1, N) if vs[n] != cand1[n]]
    print('  first mismatches:', diffs[:10])

# sharpness of the rescale: v2(u_n) = vs[n]-2n; sharp lambda = 2^c with
# c = max ceil(-v2(u_n)/n)
worst = max((2 * n - vs[n] + n - 1) // n for n in range(1, N))
print('sharp rescale exponent c* (u(2^c t) integral iff c>=c*):', worst)

# ---------------- 3. Lucas ----------------
for p in (3, 5, 7, 11, 13):
    bad = []
    for A_ in range(1, (N - 1) // p + 1):
        for r in range(p):
            n = A_ * p + r
            if n >= N:
                break
            if (ut[n] - ut[A_] * ut[r]) % p != 0:
                bad.append((A_, r))
    print('Lucas mod %d: %s (%d cells)' %
          (p, 'PASS' if not bad else 'FAIL %d e.g. %s' % (len(bad), bad[:4]),
           sum(1 for A_ in range(1, (N - 1) // p + 1)
               for r in range(p) if A_ * p + r < N)))

# ---------------- 4. q-side ----------------
NQ = 46
def eta_prod(d, nq):
    """prod(1-q^{d m}) as a list, no q-prefactor."""
    f = [F(0)] * nq
    f[0] = F(1)
    for m in range(1, nq // d + 1):
        # multiply by (1 - q^{d m})
        g = f[:]
        for i in range(nq - d * m):
            g[i + d * m] -= f[i]
        f = g
    return f

def mulser(f, g, nq):
    h = [F(0)] * nq
    for i in range(nq):
        if f[i] == 0:
            continue
        for j in range(nq - i):
            h[i + j] += f[i] * g[j]
    return h

def powser(f, k, nq):
    r = [F(0)] * nq
    r[0] = F(1)
    for _ in range(k):
        r = mulser(r, f, nq)
    return r

def invser(f, nq):
    g = [F(0)] * nq
    g[0] = 1 / f[0]
    for n in range(1, nq):
        g[n] = -sum(f[i] * g[n - i] for i in range(1, n + 1)) / f[0]
    return g

e1 = eta_prod(1, NQ); e2 = eta_prod(2, NQ)
e3 = eta_prod(3, NQ); e6 = eta_prod(6, NQ)
# t(q) = q * (e1 e6 / e2 e3)^12   (eta prefactors give the q)
num = mulser(powser(mulser(e1, e6, NQ), 12, NQ), [F(0), F(1)] + [F(0)] * (NQ - 2), NQ)
den = powser(mulser(e2, e3, NQ), 12, NQ)
tq = mulser(num, invser(den, NQ), NQ)
# F(q) = (e2 e3)^7/(e1 e6)^5, prefactor q^0
Fq = mulser(powser(mulser(e2, e3, NQ), 7, NQ),
            invser(powser(mulser(e1, e6, NQ), 5, NQ), NQ), NQ)
# compose u(t(q))
def compose(u_coeffs, tser, nq):
    out = [F(0)] * nq
    tp = [F(0)] * nq
    tp[0] = F(1)
    for n in range(len(u_coeffs)):
        if n > 0:
            tp = mulser(tp, tser, nq)
            if all(x == 0 for x in tp):
                break
        for i in range(nq):
            out[i] += u_coeffs[n] * tp[i]
    return out

uq_comp = compose(u[:NQ], tq, NQ)
uq_sqrt = sqrt_series(Fq, NQ)
print('u(t(q)) == sqrt(F(q)) to q^%d: %s' % (NQ - 1, uq_comp[:NQ] == uq_sqrt[:NQ]))
print('sqrt(F)(q) coefficients v2:', [(-v2(x.denominator) if x != 0 else None)
                                       for x in uq_sqrt[:25]])
print('sqrt(F)(q) first coeffs:', [str(x) for x in uq_sqrt[:10]])

# 2u - ? theta comparisons, disc -24: A = x^2+6y^2, B = 2x^2+3y^2
def theta(coefs_fn, nq):
    f = [0] * nq
    R = int(nq ** 0.5) + 3
    for x in range(-R, R + 1):
        for y in range(-R, R + 1):
            v = coefs_fn(x, y)
            if v < nq:
                f[v] += 1
    return f

TA = theta(lambda x, y: x * x + 6 * y * y, NQ)
TB = theta(lambda x, y: 2 * x * x + 3 * y * y, NQ)
print('theta A:', TA[:13])
print('theta B:', TB[:13])
half_sum = [F(TA[i] + TB[i], 2) for i in range(NQ)]
half_dif = [F(TA[i] - TB[i], 2) for i in range(NQ)]
# compare with 2*uq - const etc. -- try simple rational combos
import itertools
targets = {'sqrtF': uq_sqrt}
basis = {'(A+B)/2': half_sum, '(A-B)/2': half_dif}
for tn, tv in targets.items():
    for bn, bv in basis.items():
        # solve tv ?= alpha*bv + beta*other... quick: check proportionality of
        # tails and small linear combos
        pass
# direct: is 2*sqrtF - (A+B)/2 - c*(A-B)/2 = 0 for some c? solve from q^1..q^2
try:
    c1 = None
    # alpha*halfsum + beta*halfdif = sqrtF: solve from coeffs 0,1; check rest
    import fractions
    a0, b0, s0 = half_sum[0], half_dif[0], uq_sqrt[0]
    a1, b1, s1 = half_sum[1], half_dif[1], uq_sqrt[1]
    det = a0 * b1 - a1 * b0
    if det:
        al = (s0 * b1 - s1 * b0) / det
        be = (a0 * s1 - a1 * s0) / det
        okk = all(al * half_sum[i] + be * half_dif[i] == uq_sqrt[i]
                  for i in range(NQ))
        print('sqrtF = %s*(A+B)/2 + %s*(A-B)/2 ? %s' % (al, be, okk))
        if not okk:
            miss = [i for i in range(NQ)
                    if al * half_sum[i] + be * half_dif[i] != uq_sqrt[i]][:5]
            print('   first mismatch at q^', miss)
except Exception as e:
    print('theta solve error', e)

# ---------------- 5. upstairs ----------------
NU = 61
Qs = [core.Q(n) for n in range(NU)]
y4 = [Qs[n] * F(4) ** n for n in range(NU)]
r2 = sqrt_series(y4, NU)
print('BZ: sqrt(Q(4t)) integral to n=%d: %s'
      % (NU - 1, all(x.denominator == 1 for x in r2)))
y8 = [Qs[n] * F(8) ** n for n in range(NU)]
def root4(f, n):
    r = sqrt_series(sqrt_series(f, n), n)
    return r
r4 = root4(y8, NU)
print('BZ: Q(8t)^{1/4} integral to n=%d: %s'
      % (NU - 1, all(x.denominator == 1 for x in r4)))
w = [int(x) for x in r4] if all(x.denominator == 1 for x in r4) else None
if w:
    print('quarter-BZ sequence w[0:8]:', w[:8])
    print('v2(w_n) n=0..30:', [v2(x) for x in w[:31]])
    for p in (3, 5, 7):
        bad = []
        for A_ in range(1, (NU - 1) // p + 1):
            for r in range(p):
                n = A_ * p + r
                if n >= NU:
                    break
                if (w[n] - w[A_] * w[r]) % p != 0:
                    bad.append((A_, r))
        print('quarter-BZ Lucas mod %d: %s' %
              (p, 'PASS' if not bad else 'FAIL %d e.g. %s' % (len(bad), bad[:4])))
# sharpness upstairs
usq = sqrt_series(Qs, NU)
worst2 = max((0 - min(0, -v2(x.denominator)) + n - 1) // n if x != 0 else 0
             for n, x in enumerate(usq[1:], start=1))
vv = [v2(x.denominator) for x in usq[1:] if x != 0]
print('sqrt(Q) denominator v2 per n (first 20):', vv[:20])

# universal lemma sanity: random integer series f -> sqrt(f(4t)) integral
import random
random.seed(1)
f = [F(1)] + [F(random.randint(-9, 9)) for _ in range(40)]
f4 = [f[n] * F(4) ** n for n in range(41)]
rr = sqrt_series(f4, 41)
print('universal lemma sanity (random f): sqrt(f(4t)) integral:',
      all(x.denominator == 1 for x in rr))

# ---------------- PART 2: sharp structure ----------------
print('\n--- PART 2 ---')
def s2(n): return bin(n).count('1')
print('v2(ut_n) == s2(n), 1<=n<=200:',
      all(v2(ut[n]) == s2(n) for n in range(1, N)))

def kron(a_, p):
    a_ %= p
    if a_ == 0:
        return 'ram'
    return pow(a_, (p - 1) // 2, p) == 1

print('split-prime Lucas law (predict PASS iff (-6/p)=1 or p=3):')
for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
    bad = sum(1 for A_ in range(1, (N - 1) // p + 1) for r in range(p)
              if A_ * p + r < N and (ut[A_ * p + r] - ut[A_] * ut[r]) % p)
    print('  p=%2d split=%s  %s' % (p, kron(-6, p),
                                    'PASS' if bad == 0 else 'FAIL(%d)' % bad))

# half-BZ root battery
r2b = [int(x) for x in sqrt_series([Qs[n] * F(4) ** n for n in range(NU)], NU)]
print('half-BZ r2[0:6]:', r2b[:6])
print('v2(r2_n) == s2(n), n<=60:', all(v2(r2b[n]) == s2(n) for n in range(1, NU)))
for p in (3, 5, 7, 11, 13):
    bad = sum(1 for A_ in range(1, (NU - 1) // p + 1) for r in range(p)
              if A_ * p + r < NU and (r2b[A_ * p + r] - r2b[A_] * r2b[r]) % p)
    print('  half-BZ Lucas p=%d: %s' % (p, 'PASS' if bad == 0 else 'FAIL(%d)' % bad))

# genericity of v2=s2: random odd-a1 integer series
import random
random.seed(7)
gen_ok = 0
for trial in range(5):
    f = [F(1), F(2 * random.randint(0, 9) + 1)] + \
        [F(random.randint(-99, 99)) for _ in range(60)]
    f4 = [f[n] * F(4) ** n for n in range(62)]
    rr = sqrt_series(f4, 62)
    if all(x.denominator == 1 for x in rr) and \
       all(v2(int(rr[n])) == s2(n) for n in range(1, 62) if rr[n] != 0):
        gen_ok += 1
print('random odd-a1 series with v2==s2 profile: %d/5' % gen_ok)
