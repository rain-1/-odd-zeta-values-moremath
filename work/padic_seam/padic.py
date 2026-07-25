"""p-adic toolbox: exact Z_p arithmetic, Teichmuller, Kubota-Leopoldt L_p, zeta_p.

SOURCE (local, fetched): llm/18-lai-sprang-zudilin-2025 sec.2, Definition 8 + preceding display:
  q_p = p (p odd), 4 (p=2).  omega = Teichmuller character mod q_p.  <x> = x/omega(x).
  p-adic Hurwitz zeta (Volkenborn):  zeta_p(s,x) = 1/(s-1) Int_{Z_p} <t+x>^{1-s} dt
  L_p(s,chi) = <M>^{1-s}/M * sum_{j=0,p!|j}^{M-1} chi(j) zeta_p(s, j/M),  q_p | M, f | M
  zeta_p(s) := L_p(s, omega^{1-s}),  s >= 2 integer.

DERIVED series (see PADIC_SEAM.md T2 for the derivation):
  Int_{Z_p} t^k dt = B_k  (B_1 = -1/2), so for |x|_p > 1
     zeta_p(s,x) = 1/(s-1) <x>^{1-s} sum_{k>=0} binom(1-s,k) B_k x^{-k},
  hence with M a multiple of q_p and f:
     L_p(s,chi) = 1/((s-1) M) sum_{p!|j, 0<j<M} chi(j) <j>^{1-s} sum_{k>=0} binom(1-s,k) B_k (M/j)^k
"""
from fractions import Fraction as Fr
from functools import lru_cache
import sympy

# ---------------- basic Z_p ----------------
def vp(x, p):
    if x == 0: return None
    if isinstance(x, int): num, den = x, 1
    else: num, den = x.numerator, x.denominator
    v = 0
    while num % p == 0: num //= p; v += 1
    while den % p == 0: den //= p; v -= 1
    return v

def frac_mod(x, p, prec):
    M = p**prec
    num, den = (x, 1) if isinstance(x, int) else (x.numerator, x.denominator)
    assert den % p != 0, "not p-integral: %s" % x
    return num % M * pow(den, -1, M) % M

def digits(r, p, prec):
    d = []
    for _ in range(prec):
        d.append(r % p); r //= p
    return d

def dstr(r, p, prec):
    """base-p digit string, least significant FIRST."""
    return " ".join(str(x) for x in digits(r % p**prec, p, prec))

def agree(x, y, p, cap):
    """number of leading p-adic digits on which x==y (both ints mod p^cap)."""
    d = (x - y) % p**cap
    if d == 0: return cap
    v = 0
    while d % p == 0: d //= p; v += 1
    return v

# ---------------- Teichmuller ----------------
@lru_cache(maxsize=None)
def teich_table(p, prec):
    M = p**prec
    out = [0]*p
    for a in range(1, p):
        x = a
        for _ in range(2*prec + 10):
            f = (pow(x, p, M) - x) % M
            d = (p*pow(x, p-1, M) - 1) % M
            x = (x - f*pow(d, -1, M)) % M
        assert pow(x, p-1, M) == 1 and (x - a) % p == 0
        out[a] = x
    return out

def omega(a, p, prec):
    """Teichmuller character value mod p^prec (as an element of Z/p^prec)."""
    if p == 2:
        assert a % 2 == 1
        return 1 if a % 4 == 1 else p**prec - 1
    return teich_table(p, prec)[a % p]

# ---------------- Bernoulli (B_1 = -1/2 convention) ----------------
@lru_cache(maxsize=None)
def bern(k):
    b = Fr(sympy.Rational(sympy.bernoulli(k)).p, sympy.Rational(sympy.bernoulli(k)).q)
    return -b if k == 1 else b

@lru_cache(maxsize=None)
def bern_poly_at(n, a, F):
    """B_n(a/F) exactly."""
    return sum(Fr(int(sympy.binomial(n, k))) * bern(k) * Fr(a, F)**(n-k) for k in range(n+1))

# ---------------- L_p via the derived series ----------------
def mulr(x, r, p, W):
    """x int mod p^W times Fraction r (must keep p-integrality): returns int mod p^W."""
    num, den = r.numerator, r.denominator
    v = 0
    while den % p == 0: den //= p; v += 1
    if v:
        assert x % p**v == 0, "not p-integral (short by p^%d)" % v
        x //= p**v; W -= v
    return (x * num % p**W) * pow(den, -1, p**W) % p**W

def Lp_shift(s, e, p, prec, SH=1, Mmul=1):
    """p^SH * L_p(s, omega^e)  mod p^prec, integer s != 1.  SH>=1 covers the only
       possible pole (v_p >= -1).  Returns int in [0,p^prec)."""
    qp = 4 if p == 2 else p
    ordw = 2 if p == 2 else p - 1
    M = qp * Mmul
    vM = vp(M, p)
    W = prec + vM + max(0, vp(s-1, p) or 0) + 4
    Mod = p**W
    e1 = 1 - s
    K = (W + 3)//vM + 3
    ee = e % ordw
    tot = 0
    for j in range(1, M):
        if j % p == 0: continue
        w = omega(j, p, W)
        chi = pow(w, ee, Mod)
        br = j * pow(w, -1, Mod) % Mod          # <j> = j/omega(j)
        brp = pow(br, e1, Mod)                  # <j>^{1-s}
        inner = Fr(0)
        for k in range(K+1):
            c = int(sympy.binomial(e1, k))
            if c == 0: continue
            inner += Fr(c) * bern(k) * Fr(M, j)**k
        tot = (tot + chi * brp % Mod * frac_mod(inner, p, W)) % Mod
    val = mulr(tot, Fr(p**SH, (s-1)*M), p, W)
    return val % p**prec

def zeta_p_sh(s, p, prec, SH=1):
    """p^SH * zeta_p(s),  zeta_p(s) := L_p(s, omega^{1-s}).  Integer s >= 2."""
    return Lp_shift(s, 1-s, p, prec, SH)

def zeta_p(s, p, prec):
    """zeta_p(s) mod p^prec, asserting v_p >= 0."""
    v = zeta_p_sh(s, p, prec+1, 1)
    assert v % p == 0, "zeta_p(%d) at p=%d has valuation -1" % (s, p)
    return (v//p) % p**prec

# ---------------- CROSS-CHECKS ----------------
def check_interpolation(p, prec, nmax=16, verbose=True):
    """L_p(1-n, omega^e) = -(1 - psi(p) p^{n-1}) B_{n,psi}/n,  psi = omega^{e-n},
       B_{n,psi} computed CLASSICALLY (independent code path):
         psi trivial : B_n, Euler factor (1-p^{n-1});
         psi != triv : B_{n,psi} = q^{n-1} sum_{a=1,p!|a}^{q-1} psi(a) B_n(a/q), psi(p)=0."""
    ordw = 2 if p == 2 else p - 1
    qp = 4 if p == 2 else p
    SH = 4
    W = prec + 3          # headroom; comparison is done at p^prec
    Mod = p**W
    bad = tot = 0
    for e in range(ordw):
        for n in range(2, nmax):
            lhs = Lp_shift(1-n, e, p, W, SH)
            pe = (e - n) % ordw
            if pe == 0:
                rhs = frac_mod(Fr(p**SH) * Fr(-1, n) * Fr(1 - p**(n-1)) * bern(n), p, W)
            else:
                acc = 0
                for a in range(1, qp):
                    if a % p == 0: continue
                    acc = (acc + pow(omega(a, p, W), pe, Mod) *
                           frac_mod(Fr(p**SH) * Fr(qp)**(n-1) * bern_poly_at(n, a, qp), p, W)) % Mod
                rhs = mulr(acc, Fr(-1, n), p, W)
            tot += 1
            if lhs % p**prec != rhs % p**prec:
                bad += 1
                if verbose: print("   MISMATCH p=%d e=%d n=%d: %d vs %d" % (p, e, n, lhs, rhs))
    return bad, tot

def check_M_independence(s, e, p, prec, SH=1):
    return [Lp_shift(s, e, p, prec, SH, Mmul=m) for m in (1, 2, 3, 4, 5)]

def zeta_p_via_kummer(s, p, N):
    """Independent route (LSZ, characterisation after Def. 8):
       zeta_p(s) = lim ζ(k), k -> s p-adically, k in Z_<0, k = s mod (p-1).
       zeta(1-n) = -B_n/n.  Choose n = 1-s mod lcm(p^N, p-1), n even, n>0."""
    ordw = 2 if p == 2 else p - 1
    Mm = (p**N) * ordw
    n = (1 - s) % Mm
    while n < 2 or n % 2:
        n += Mm
    return n, frac_mod(Fr(p) * Fr(-1, n) * bern(n), p, N)   # returns p*zeta(1-n)
