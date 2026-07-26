"""p = 2, 3: which layers of the Theorem-4.1 proof survive, and which don't.

Layers, from the bottom up:

  LA  Lemma A      W(M) == ((p-1)!)^M  (mod p^3)                [needs Wolstenholme]
  S1  the four regional formulas for A(ap+r,cp+s) mod p^3       [needs LA]
  P21 Proposition 2.1 (the assembly)                            [needs S1]
  R1  Sigma_ac + 2 Sigma_c^2 = 0 over Q                         [p-free]
  R2  Sigma_c^2 + Xi_p == 0 (mod p)                             [needs Lemma E, p>=5]
  N   {(a m1(a), m2(a)) : 1<=a<p} spans F_p^2                   [makes R1,R2 necessary]
  T41 the theorem itself

Each is checked at p = 2,3 and, as a control, at p = 5,7.
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/apdef')
from fractions import Fraction as F
from math import factorial
from core import A, Hs, av, bv, vp
from gap_core import sigmas, Xi, Delta, Cfun, moments, Ur

PRIMES = (2, 3, 5, 7)


def modp(x, p):
    """Fraction -> F_p (assumes p-integral)"""
    num, den = x.numerator % p, x.denominator % p
    return num * pow(den, -1, p) % p


def Wblock(M, p):
    w = 1
    for j in range(M):
        for i in range(1, p):
            w *= j * p + i
    return w


def X(p, r):
    return sigmas(r)[0] + Xi(p, r)


def ar(r):
    return sum(A(r, s) for s in range(r + 1))


print("LAYER-BY-LAYER, p = 2,3 vs the p>=5 control\n")
print(f"{'p':>3} {'LA':>10} {'LemE1':>7} {'LemE2':>7} {'S1':>8} {'P2.1':>8} "
      f"{'R1':>5} {'R2':>8} {'span N':>8} {'T4.1':>8}")

for p in PRIMES:
    # --- LA: Lemma A at M = 2,3
    LA = all((Wblock(M, p) - factorial(p - 1) ** M) % p ** 3 == 0 for M in (2, 3))

    # --- Lemma E's two power sums
    E1 = sum(pow(w, -1, p) for w in range(1, p)) % p == 0
    E2 = sum(pow(w * w % p, -1, p) for w in range(1, p)) % p == 0

    # --- S1: regional formulas, cell by cell, mod p^3
    s1bad = 0
    for a in range(p):
        for c in range(a + 1):
            for r in range(p):
                for s in range(r + 1):
                    lhs = F(A(a * p + r, c * p + s))
                    u = Hs(r + s, 1) - Hs(r - s, 1)
                    v = Hs(r + s, 1) + Hs(r - s, 1) - 2 * Hs(s, 1)
                    if r + s < p:
                        L1 = a * u + c * v
                        L2 = ((a + c) ** 2 * Hs(r + s, 2) - 2 * c ** 2 * Hs(s, 2)
                              - (a - c) ** 2 * Hs(r - s, 2))
                        rhs = A(a, c) * A(r, s) * (1 + 2 * p * L1 + p ** 2 * (2 * L1 ** 2 - L2))
                    else:
                        rhs = p ** 2 * A(a, c) * (1 + a + c) ** 2 * F(A(r, s), p ** 2)
                    if vp(lhs - rhs, p) < 3:
                        s1bad += 1
                    # borrow cells s = r+m
                for m in range(1, p - r):
                    s = r + m
                    if s >= p:
                        break
                    lhs = F(A(a * p + r, c * p + s))
                    rhs = p ** 2 * (a - c) ** 2 * A(a, c) * Cfun(r, m)
                    if vp(lhs - rhs, p) < 3:
                        s1bad += 1

    # --- P2.1: the assembly, both weights
    p21bad = 0
    for a in range(1, p):
        for wname in ("a", "b"):
            om = (lambda c: F(1)) if wname == "a" else (
                lambda c: 2 * Hs(a, 3) - Hs(c, 3))
            m0 = sum((om(c) * A(a, c) for c in range(a + 1)), F(0))
            m1 = sum((c * om(c) * A(a, c) for c in range(a + 1)), F(0))
            m2 = sum((c * c * om(c) * A(a, c) for c in range(a + 1)), F(0))
            for r in range(p):
                T = sum((om(c) * A(a * p + r, c * p + s)
                         for c in range(a + 1) for s in range(p)), F(0))
                lhs = (T - m0 * (ar(r) + 2 * p * a * Ur(r))) / p ** 2
                s_a2, s_ac, s_cc = sigmas(r)
                rhs = (a * a * m0 * s_a2 + a * m1 * s_ac + m2 * s_cc
                       + (a * a * m0 - 2 * a * m1 + m2) * Xi(p, r))
                if vp(lhs - rhs, p) < 1:
                    p21bad += 1

    # --- R1 over Q, r < p
    R1 = all(sigmas(r)[1] + 2 * sigmas(r)[2] == 0 for r in range(p))

    # --- R2 mod p, r < p
    r2bad = [r for r in range(p) if modp(sigmas(r)[2] + Xi(p, r), p) != 0]

    # --- N: span of {(a m1, m2)} in F_p^2, weight omega = 1
    vecs = []
    for a in range(1, p):
        m0, m1, m2 = moments(a)
        vecs.append((a * m1 % p, m2 % p))
    rank = 0
    basis = []
    for v in vecs:
        w = v
        for b in basis:
            if b[0]:
                f = w[0] * pow(b[0], -1, p) % p
                w = ((w[0] - f * b[0]) % p, (w[1] - f * b[1]) % p)
        if w != (0, 0):
            basis.append(w if w[0] else (w[1], 0) and w)
            basis.sort(key=lambda t: t[0] == 0)
            rank = len({tuple(b) for b in basis if b != (0, 0)})
    # simple rank over F_p
    def rk(vs):
        mat = [list(v) for v in vs]
        rr = 0
        for col in range(2):
            piv = next((i for i in range(rr, len(mat)) if mat[i][col] % p), None)
            if piv is None:
                continue
            mat[rr], mat[piv] = mat[piv], mat[rr]
            inv = pow(mat[rr][col], -1, p)
            mat[rr] = [x * inv % p for x in mat[rr]]
            for i in range(len(mat)):
                if i != rr and mat[i][col] % p:
                    f = mat[i][col]
                    mat[i] = [(mat[i][j] - f * mat[rr][j]) % p for j in range(2)]
            rr += 1
        return rr
    rank = rk(vecs)

    # --- T4.1 itself
    t41bad = 0
    for a in range(1, p):
        for r in range(p):
            n = a * p + r
            u = ar(r) + 2 * p * a * Ur(r) + p ** 2 * a * a * X(p, r)
            if vp(F(av(n)) - av(a) * u, p) < 3:
                t41bad += 1
            if vp(p ** 3 * bv(n) - bv(a) * u, p) < 3:
                t41bad += 1

    fmt = lambda ok: "holds" if ok else "FAILS"
    print(f"{p:>3} {fmt(LA):>10} {fmt(E1):>7} {fmt(E2):>7} "
          f"{('0 bad' if not s1bad else str(s1bad)+' bad'):>8} "
          f"{('0 bad' if not p21bad else str(p21bad)+' bad'):>8} "
          f"{fmt(R1):>5} "
          f"{('holds' if not r2bad else 'FAILS r='+','.join(map(str,r2bad))):>8} "
          f"{'rank '+str(rank):>8} "
          f"{('0 bad' if not t41bad else str(t41bad)+' bad'):>8}")

print("\nDetail at p = 2,3:")
for p in (2, 3):
    print(f"  p={p}: Sigma_c^2(r) = {[sigmas(r)[2] for r in range(p)]},  "
          f"Xi_p(r) = {[Xi(p,r) for r in range(p)]}")
    print(f"        Sigma_c^2+Xi mod p = {[modp(sigmas(r)[2]+Xi(p,r), p) for r in range(p)]}"
          f"   (R2 wants all 0)")
    print(f"        (-2a m1 + m2) mod p, omega=1, a=1..p-1 = "
          f"{[( -2*a*moments(a)[1] + moments(a)[2]) % p for a in range(1,p)]}")
