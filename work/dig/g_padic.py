"""g_padic.py -- does the Rhin-Viola transfer identity survive the p-adic
(theta-shifted) very-well-poised family?

The p-adic Volkenborn construction needs the poles of R at shifts theta with
|theta|_p >= q_p.  For the very-well-poised 7F6

    Rtilde(h;t) = (h_0+2t) (t+1)_{h_0-1} prod_{j=1}^{5} 1/(t+h_j)_{1+h_0-2h_j}

the bricks are rational functions of t iff  2h_j - h_0 - 1 in Z.  With
h_0 in Z this forces h_j in (1/2)Z -- so the ONLY very-well-poised p-adic shift
is theta = 1/2, i.e. p = 2.  (Recorded as a structural finding.)

Here we test whether the group still acts when the h_j are half-integers, i.e.
whether the transfer identity is a property of the *lattice* or only of the
integer points.

TEST: the linear forms at h and at g h must be PROPORTIONAL as vectors
      V(h) = ( rho_{c,i} for every pole-residue class c and every order i ,
               rational part B ) .
This is exact rational arithmetic.
"""

from fractions import Fraction as F
from collections import defaultdict

from g_verify import partial_fractions, h_from_ab, orbit_ab


def R_data_half(h):
    """Rtilde for h_0 in Z, h_j in (1/2)Z."""
    h0 = int(h[0])
    num = [F(1 + i) for i in range(h0 - 1)]
    den = []
    for hj in h[1:]:
        L = 1 + h0 - 2 * hj
        assert L == int(L) and L >= 1, f"bad brick length {L}"
        den += [F(hj) + i for i in range(int(L))]
    return num, den, (h0, 2)


def valid_half(h):
    h0 = h[0]
    if h0 != int(h0):
        return False
    if h0 < 2:
        return False
    for hj in h[1:]:
        if 2 * hj != int(2 * hj):
            return False
        if hj < F(1, 2):
            return False
        L = 1 + h0 - 2 * hj
        if L < 1:
            return False
    if 1 + 2 * h0 - sum(h[1:]) < 0:
        return False
    return True


def form_vector(h):
    """(rho_{class,i}, rational part) exactly, as a canonical tuple."""
    num, den, lin = R_data_half(h)
    r = partial_fractions(num, den, lin)
    rho = defaultdict(F)
    B = F(0)
    for (i, k), v in r.items():
        cls = F(k) - int(k)          # residue class of the pole in Q/Z
        rho[(cls, i)] += v
        # sum_{t>=0} 1/(t+k)^i = zeta(i, k) ; split off the tail so that the
        # 'value' part only depends on cls:  zeta(i,cls_0) - sum_{l} ...
        k0 = cls if cls != 0 else F(1)
        m = int((F(k) - k0))
        Hk = sum(F(1) / (k0 + l) ** i for l in range(m))
        B -= v * Hk
    return dict(rho), B


def proportional(v, w):
    """Exact proportionality of two rational vectors (either may be scaled)."""
    if len(v) != len(w):
        return False
    piv = None
    for a, b in zip(v, w):
        if a != 0 or b != 0:
            piv = (a, b)
            break
    if piv is None:
        return True
    for a, b in zip(v, w):
        if piv[0] * b != piv[1] * a:
            return False
    return True


def test(alpha, beta, n=1, half_shift=(3, 4)):
    """Base point from (alpha,beta), then subtract 1/2 from the h_j listed in
    half_shift (making them half-integers) -- the p=2 p-adic family."""
    a = tuple(alpha[j] * n + 1 for j in range(4))
    b = (beta[0] * n + 1, beta[1] * n + 1, beta[2] * n + 2, beta[3] * n + 2)
    sh = 1 - b[0]
    a = tuple(F(x + sh) for x in a)
    b = tuple(F(x + sh) for x in b)
    # push the half-integrality into b_3, b_4 -> h_4, h_5 become half-integers
    b = (b[0], b[1], b[2] - F(1, 2), b[3] - F(1, 2))
    ab0 = (a, b)
    orb = orbit_ab(ab0)
    h0 = h_from_ab(*ab0)
    print(f"   base h = {h0}  (classes mod 1: "
          f"{[str(F(x)-int(x)) for x in h0[1:]]})")
    if not valid_half(h0):
        print("   base point invalid")
        return
    rho0, B0 = form_vector(h0)
    ok = bad = skipped = 0
    for ab in orb:
        h = h_from_ab(*ab)
        if not valid_half(h):
            skipped += 1
            continue
        rho1, B1 = form_vector(h)
        keys = sorted(set(rho0) | set(rho1))
        v0 = tuple(rho0.get(k, F(0)) for k in keys) + (B0,)
        v = tuple(rho1.get(k, F(0)) for k in keys) + (B1,)
        if proportional(v0, v):
            ok += 1
        else:
            bad += 1
            if bad <= 2:
                print(f"     FAIL at h={h}")
    print(f"   orbit {len(orb)};  comparable {ok+bad} (skipped {skipped});  "
          f"proportional {ok},  NOT proportional {bad}")
    return ok, bad, skipped


if __name__ == "__main__":
    print("[P] half-integer (p=2) very-well-poised family, transfer identity")
    for (al, be) in [((2, 2, 3, 3), (0, 1, 4, 5)),
                     ((3, 4, 4, 5), (0, 2, 7, 7)),
                     ((4, 7, 8, 11), (0, 3, 13, 14))]:
        print(f"  alpha={al} beta={be}:")
        test(al, be, n=1)
