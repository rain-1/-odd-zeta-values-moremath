"""Tiny exact LLL + p-adic integer-relation / rational-reconstruction helpers."""
from fractions import Fraction as Fr

def lll(B, delta=Fr(99, 100)):
    """B: list of integer row vectors. Exact LLL (Fraction Gram-Schmidt). Returns reduced basis."""
    B = [list(map(int, b)) for b in B]
    n = len(B)
    def gs(B):
        Bs, mu = [], [[Fr(0)]*n for _ in range(n)]
        for i in range(n):
            v = [Fr(x) for x in B[i]]
            for j in range(i):
                d = sum(x*x for x in Bs[j])
                mu[i][j] = (sum(Fr(B[i][k])*Bs[j][k] for k in range(len(v)))/d) if d else Fr(0)
                v = [v[k] - mu[i][j]*Bs[j][k] for k in range(len(v))]
            Bs.append(v)
        return Bs, mu
    Bs, mu = gs(B)
    k = 1
    guard = 0
    while k < n:
        guard += 1
        if guard > 20000: break
        for j in range(k-1, -1, -1):
            if abs(mu[k][j]) > Fr(1, 2):
                q = int(round(float(mu[k][j])))
                # exact rounding
                q = (mu[k][j].numerator*2 + mu[k][j].denominator)//(2*mu[k][j].denominator)
                B[k] = [B[k][t] - q*B[j][t] for t in range(len(B[k]))]
                Bs, mu = gs(B)
        nk = sum(x*x for x in Bs[k]); nk1 = sum(x*x for x in Bs[k-1])
        if nk >= (delta - mu[k][k-1]**2)*nk1:
            k += 1
        else:
            B[k], B[k-1] = B[k-1], B[k]
            Bs, mu = gs(B)
            k = max(k-1, 1)
    return B

def padic_relation(vals, p, K, weight=None):
    """Find small integer (c_0..c_{m-1}) with sum c_i vals[i] = 0 mod p^K.
       vals: ints mod p^K.  Returns sorted candidate relations (by L2 norm)."""
    m = len(vals)
    M = p**K
    C = weight if weight else M          # weight on the RESIDUE column: forces residue 0
    rows = []
    for i in range(m):
        rows.append([0]*i + [1] + [0]*(m-1-i) + [C*(vals[i] % M)])
    rows.append([0]*m + [C*M])
    R = lll(rows)
    out = []
    for r in R:
        c = r[:m]
        if all(x == 0 for x in c): continue
        chk = sum(c[i]*vals[i] for i in range(m)) % M
        if chk != 0: continue
        out.append((sum(x*x for x in c), c, chk))
    out.sort()
    return out

def rat_recon(x, p, K, bound=None):
    """rational reconstruction of x mod p^K: find n/d = x with |n|,|d| <= sqrt(p^K/2)."""
    M = p**K
    a0, a1 = M, x % M
    b0, b1 = 0, 1
    lim = int((M//2)**0.5)
    while a1 > lim:
        q = a0//a1
        a0, a1 = a1, a0 - q*a1
        b0, b1 = b1, b0 - q*b1
    if b1 == 0 or abs(b1) > lim: return None
    from math import gcd
    n, d = a1, b1
    if d < 0: n, d = -n, -d
    if gcd(abs(n), d) != 1: return None
    return Fr(n, d)
