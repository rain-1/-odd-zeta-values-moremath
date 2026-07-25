"""THE SPLIT.  Apery's formula
    b_n = sum_k A(n,k) [ H_3(n) + sum_{m<=k} (-1)^{m-1} / (2 m^3 C(n,m) C(n+m,m)) ],
    A(n,k) = C(n,k)^2 C(n+k,k)^2.
Along n = a p^s the p^{3s}-scaled limit picks out (i) the harmonic part -> h_p(a) and
(ii) exactly the inner terms with m = j p^s (j = 1..a), everything else being suppressed
by p^{3(s - v_p(m))}.  For a = 1 only k = m = p^s survives and the term is
    A(n,n) / (2 p^{3s} C(2p^s,p^s)) = C(2p^s,p^s) / (2 p^{3s}).
PREDICTION:   Lambda_1 = h_p(1) + c_p / (2 Atil_1),   c_p := lim_s C(2p^s, p^s).
"""
import sys
from fractions import Fraction as Fr
from pnum import P

def cbin_tower(p, smax, K):
    """C(2p^s, p^s) mod p^K for s = 0..smax, exactly (p-free factorial units)."""
    M = p**K
    need = set()
    for s in range(smax+1):
        for k in range(s+1):
            need.add(p**k); need.add(2*p**k)
    top = max(need)
    u = {}
    acc = 1
    for j in range(1, top+1):
        if j % p:
            acc = acc * j % M
        if j in need:
            u[j] = acc
    u[1] = u.get(1, 1)
    out = {}
    for s in range(smax+1):
        num = 1; den = 1
        for k in range(s+1):
            num = num * u[2*p**k] % M
            den = den * pow(u[p**k], 2, M) % M
        # v_p((2p^s)!) - 2 v_p((p^s)!) = 0  (no carries adding p^s+p^s in base p, p odd)
        out[s] = P(p, 0, num * pow(den, -1, M) % M, K)
    return out

if __name__ == "__main__":
    from t2_ansatz import load
    from t3_harm import h_p
    for p in [int(x) for x in sys.argv[1:]]:
        dat, raw = load(p)
        L = dat[1]["L"]; At = dat[1]["At"]
        smax = dat[1]["s"]
        K = L.prec + 6
        cb = cbin_tower(p, smax, K)
        print("=" * 70)
        print("p =", p, " C(2p^s,p^s) tower:")
        for s in range(1, smax+1):
            print("   s=%d  agrees with s-1 to %d digits (expect >= %d, Kazandzidis)"
                  % (s, cb[s].agree(cb[s-1]), 3*s))
        c_p = cb[smax].trunc(3*(smax+1))
        H = h_p(1, p, L.prec + 4)
        pred = c_p / (At * 2)
        got = L - H
        print("   c_p        =", c_p)
        print("   h_p(1)     =", H.trunc(12))
        print("   Atil_1     =", At.trunc(12))
        print("   Lambda_1-h =", got.trunc(12))
        print("   c_p/(2At)  =", pred.trunc(12))
        d = got - pred
        print("   >>> PREDICTION Lambda_1 = h_p(1) + c_p/(2 Atil_1):  agree to %s digits"
              % ("ALL (%d)" % min(got.prec, pred.prec) if d.is_zero() else d.v))
