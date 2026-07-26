"""Does Theorem 4.1 (two-level digit law mod p^3) survive at p = 2 and p = 3?

We test, for every prime p and every 0 <= a,r < p, the three nested statements

  L0 (Lucas,   mod p  ):   a_{ap+r} == a_a a_r            ,  p^3 b_{ap+r} == b_a a_r
  L1 (1st ord, mod p^2):   a_{ap+r} == a_a u1 ,  u1 = a_r + 2p a U_r
  L2 (Thm 4.1, mod p^3):   a_{ap+r} == a_a u2 ,  u2 = u1 + p^2 a^2 X_p(r)

and report the exact floor  v_p(LHS - RHS)  in each case, so a failure is visible
as a valuation strictly below the claimed one.  Also isolates which of the two
proof ingredients that need p >= 5 actually breaks:

  (LA) Lemma A  : W(M) == ((p-1)!)^M mod p^3   [needs Wolstenholme, p >= 5]
  (LE) Lemma E  : sum_{w in F_p^x} w^-1 == sum w^-2 == 0 mod p   [w^-2 needs p >= 5]
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/apdef')
from fractions import Fraction as F
from math import factorial
from core import A, Hs, av, bv, vp
from gap_core import sigmas, Xi, Ur


def X(p, r):
    a2, _, _ = sigmas(r)
    return a2 + Xi(p, r)


def report(p):
    print(f"\n=== p = {p} " + "=" * 56)
    print(f"  U_r  = {[Ur(r) for r in range(p)]}")
    print(f"  X_p  = {[X(p, r) for r in range(p)]}   (Xi_p = {[Xi(p, r) for r in range(p)]})")
    print(f"  {'(a,r)':>7} {'n':>3} | {'row':>4} | {'v(L0)':>6} {'v(L1)':>6} {'v(L2)':>6}")
    worst = {0: 99, 1: 99, 2: 99}
    for a in range(1, p):                      # a = 0 is vacuous (n = r)
        for r in range(p):
            n = a * p + r
            u0 = F(A(r, r) * 0 + sum(A(r, s) for s in range(r + 1)))   # a_r
            u1 = u0 + 2 * p * a * Ur(r)
            u2 = u1 + p ** 2 * a ** 2 * X(p, r)
            for name, Ln, La in (("a", F(av(n)), F(av(a))),
                                 ("b", p ** 3 * bv(n), bv(a))):
                vs = [vp(Ln - La * u, p) for u in (u0, u1, u2)]
                for i, v in enumerate(vs):
                    worst[i] = min(worst[i], v)
                flag = "" if vs[0] >= 1 and vs[1] >= 2 and vs[2] >= 3 else "   <-- FAILS"
                print(f"  {str((a, r)):>7} {n:>3} | {name:>4} | "
                      f"{vs[0]:>6} {vs[1]:>6} {vs[2]:>6}{flag}")
    print(f"  worst-case valuations over all (a,r), both rows: "
          f"L0 {worst[0]} (need >=1), L1 {worst[1]} (need >=2), L2 {worst[2]} (need >=3)")
    return worst


def ingredients(p):
    """which p>=5 hypotheses hold at this p"""
    s1 = sum(F(1, w) for w in range(1, p)) % 1  # placeholder, computed mod p below
    inv1 = sum(pow(w, -1, p) for w in range(1, p)) % p
    inv2 = sum(pow(w * w % p, -1, p) for w in range(1, p)) % p
    # Lemma A at M = 1: W(1) = (p-1)! trivially; test M = 2
    W2 = 1
    for j in range(2):
        for i in range(1, p):
            W2 *= j * p + i
    LA = (W2 - factorial(p - 1) ** 2) % p ** 3 == 0
    print(f"  p={p}: sum w^-1 = {inv1} (need 0), sum w^-2 = {inv2} (need 0), "
          f"Lemma A at M=2: {'holds' if LA else 'FAILS'}")


if __name__ == "__main__":
    print("PROOF INGREDIENTS (the two places p >= 5 is used)")
    for p in (2, 3, 5, 7, 11):
        ingredients(p)
    for p in (2, 3, 5, 7):
        report(p)
