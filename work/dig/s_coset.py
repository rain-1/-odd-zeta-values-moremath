"""DIG-3  s_coset.py -- M3: THE ESCAPE HATCH, measured.

DIG-1 s5's only surviving p >= 5 route:  `alpha = min over cosets` is an
INEQUALITY.  The twisted sum could in principle be more p-adically small than
its worst summand, through systematic cancellation between cosets.  Nothing in
the literature does this and the ledger has no term for it.  Here it is tested
empirically, exactly.

Set-up.  R_n(t) = C^n (2t+n)^delta prod_c (t+theta'_c)_n / (t)_{n+1}^A .  The
partial fractions r_{i,k} do NOT depend on the integration shift, so one exact
computation gives every coset.  For each unit j mod p^r,

    S_n(j/p^r) = rho_0(j/p^r) + sum_i (-1)^m (i)_m rho_i J_{i+m}(j/p^r)

is computed exactly (J_u from the exact truncated Volkenborn/Bernoulli series).

THE TEST.  Put  mn := min_j v_p(S_n(j/p^r))  (the ledger's alpha, per n).  Then
  (1) plain and omega-twisted sums:  does any of the sums the THEORY actually
      needs beat mn by Omega(n)?
  (2) the sharp question: normalise u_n := (S_n(j))_j / p^{mn} in Z_p^phi, so
      some coordinate is a unit.  A fixed c in Z_p^phi gains Omega(n) for every
      n iff all the directions u_n lie in one hyperplane to depth Omega(n).
      Measured as  H(n) := max_c min over the tested n' <= n of v_p(c . u_{n'}),
      computed exactly by p-adic Gaussian elimination on the matrix of u_n.
      H bounded  <=>  NO systematic cancellation  <=>  the hatch is shut.
"""
import sys, os, math
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from family import Family, vp, bern_volkenborn
import sympy

_J = {}


def Ju(u, theta0, p, prec):
    key = (u, theta0, p, prec)
    if key in _J:
        return _J[key]
    tot = F(0)
    k = 0
    l = max(1, -vp(theta0, p))
    while True:
        term = F(int(sympy.binomial(-u, k))) * bern_volkenborn(k) * theta0 ** (-u - k)
        v = vp(term, p)
        if v is not None and v > prec:
            break
        tot += term
        k += 1
        if k > prec // l + 60:
            break
    _J[key] = tot
    return tot


def teich(a, p, prec):
    """Teichmuller omega(a) mod p^prec, as an integer."""
    x = a % p
    mod = p ** prec
    for _ in range(prec * 3 + 5):
        xn = pow(x, p, mod)
        if xn == x:
            break
        x = xn
    return x


def coset_run(p, r, shifts, A, m=0, delta=0, ns=(6, 9, 12, 15), label=""):
    D = p ** r
    units = [j for j in range(1, D) if j % p]
    vC = sum(max(0, -vp(F(s), p)) for s in shifts) + F(A, p - 1)
    print("\n  %s   p=%d r=%d A=%d m=%d delta=%d shifts=%s" %
          (label, p, r, A, m, delta, [str(F(s)) for s in shifts]))
    print("     v_p(C) = %s ;  cosets j/%d for j in %s" % (vC, D, units))
    hdr = "       n |" + "".join("  v_p S(%d/%d)" % (j, D) for j in units)
    print(hdr + " |   min  |  plain sum | best omega-twist | HYPERPLANE H(n)")
    Us = []
    for n in ns:
        base = Family(p=p, theta0=F(units[0], D), shifts=shifts, A=A, m=m, delta=delta)
        rr = base.partial_fractions(n)
        prec = int(4 * float(vC) * n) + 80
        Ss = []
        for j in units:
            fam = Family(p=p, theta0=F(j, D), shifts=shifts, A=A, m=m, delta=delta)
            rho0, Jc, rho = fam.form(n, rr)
            S = rho0
            for u, c in Jc.items():
                S += c * Ju(u, F(j, D), p, prec)
            Ss.append(S)
        vs = [vp(S, p) if S != 0 else None for S in Ss]
        good = [v for v in vs if v is not None]
        mn = min(good) if good else 0
        tot = sum(Ss)
        vtot = vp(tot, p) if tot != 0 else None
        # omega twists
        bestk, bestv = None, None
        for k in range(0, p - 1):
            acc = F(0)
            for j, S in zip(units, Ss):
                w = teich(j, p, 6)
                acc += F(pow(w, k, p ** 6)) * S
            v = vp(acc, p) if acc != 0 else 10 ** 9
            if bestv is None or v > bestv:
                bestv, bestk = v, k
        # hyperplane depth: p-adic elimination on the normalised directions
        U = [S / F(p) ** mn for S in Ss]
        Us.append([x for x in U])
        H = hyperplane_depth(Us, p, cap=int(6 * float(vC) * n) + 60)
        print("     %3d |" % n
              + "".join("%12s" % (v if v is not None else "0") for v in vs)
              + " | %5s  |  %8s  |   k=%d: %-7s |   %s"
              % (mn, vtot, bestk, bestv if bestv < 10 ** 9 else "inf", H))
    return Us


def hyperplane_depth(Us, p, cap=400):
    """max over primitive c in Z_p^d of  min_n v_p(c . u_n).

    U c = 0 mod p^k has a primitive solution iff k <= (largest elementary
    divisor exponent of U over Z_p).  So H = max_i d_i of the Smith normal form,
    and H = INF iff rank_{Q_p}(U) < d (the u_n really do lie in a hyperplane).
    Computed exactly by p-adic Smith reduction mod p^cap.
    """
    d = len(Us[0])
    N = len(Us)
    mod = p ** cap

    def toZp(x):
        num, den = x.numerator, x.denominator
        while den % p == 0:
            den //= p
            num_v = 0
            return None
        return (num % mod) * pow(den % mod, -1, mod) % mod

    M = []
    for u in Us:
        row = []
        for x in u:
            z = toZp(x)
            if z is None:
                return "n/a"
            row.append(z)
        M.append(row)

    def val(x):
        if x % mod == 0:
            return cap
        v = 0
        while x % p == 0:
            x //= p
            v += 1
        return v

    divs = []
    R = list(range(N))
    Cc = list(range(d))
    Mw = [r[:] for r in M]
    while R and Cc:
        best = None
        for i in R:
            for j in Cc:
                v = val(Mw[i][j])
                if best is None or v < best[0]:
                    best = (v, i, j)
        v0, i0, j0 = best
        if v0 >= cap:
            break
        divs.append(v0)
        unit = (Mw[i0][j0] // p ** v0) % mod
        iu = pow(unit, -1, mod)
        for i in R:
            if i == i0:
                continue
            a = Mw[i][j0]
            if a % mod == 0:
                continue
            fac = (a // p ** v0) * iu % mod
            for j in Cc:
                Mw[i][j] = (Mw[i][j] - fac * Mw[i0][j]) % mod
        R.remove(i0)
        Cc.remove(j0)
    if len(divs) < d:
        return "INF (rank %d < %d cosets: exact hyperplane)" % (len(divs), d)
    return "%d" % max(divs)


if __name__ == "__main__":
    print("=" * 78)
    print("M3 : coset cancellation at p >= 5 -- the ACTUAL valuations, not the bound")
    print("=" * 78)
    print("H(n) must be read against min*n: bounded H = no systematic cancellation.")
    coset_run(5, 1, [F(4, 5)] * 2, 2, 0, 0, ns=(6, 9, 12, 15, 18, 21, 24, 27),
              label="[c] p=5 A=2 m=0: the weight-3 rank-1 shape, bricks on 1/5")
    coset_run(5, 1, [F(4, 5)] * 4, 4, 0, 0, ns=(6, 9, 12, 15, 18, 21),
              label="[a] p=5 A=4: all 4 bricks aligned to the coset 1/5")
    coset_run(5, 1, [F(4, 5), F(3, 5), F(2, 5), F(1, 5)], 4, 0, 0,
              ns=(6, 9, 12, 15, 18, 21),
              label="[b] p=5 A=4: bricks spread over all 4 cosets (LLS shape)")
    coset_run(5, 1, [F(4, 5), F(4, 5), F(3, 5), F(3, 5)], 4, 0, 0,
              ns=(6, 9, 12, 15, 18, 21),
              label="[b2] p=5 A=4: 2+2 split over the two reflection classes")
    coset_run(5, 1, [F(4, 5)] * 4, 4, 1, 1, ns=(6, 9, 12, 15, 18, 21),
              label="[d] p=5 A=4 m=1 delta=1: well-poised")
    coset_run(5, 1, [F(4, 5)] * 3, 3, 0, 1, ns=(6, 9, 12, 15, 18, 21),
              label="[d2] p=5 A=3 delta=1")
    coset_run(7, 1, [F(6, 7)] * 3, 3, 0, 1, ns=(4, 6, 8, 10, 12, 14, 16, 18),
              label="[e] p=7 A=3 delta=1: bricks on 1/7")
    coset_run(7, 1, [F(6, 7), F(5, 7), F(4, 7)], 3, 0, 1,
              ns=(4, 6, 8, 10, 12, 14, 16, 18),
              label="[f] p=7 A=3: bricks spread over 3 cosets")
    coset_run(5, 2, [F(24, 25)] * 2, 2, 0, 0, ns=(6, 9, 12, 15, 18, 21, 24, 27, 30),
              label="[g] p=5 r=2 (20 cosets, depth-2 shift)")
