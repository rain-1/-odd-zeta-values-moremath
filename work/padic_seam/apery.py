"""Exact Apery ζ(3) pair a_n, b_n and p-adic tower limits.  Exact arithmetic only."""
from fractions import Fraction as F
from math import comb
import sys, json

# ---------- generation ----------
def gen_recurrence(N):
    """Apery recurrence (n+1)^3 u_{n+1} = (34n^3+51n^2+27n+5) u_n - n^3 u_{n-1}."""
    a = [F(1), F(5)]
    b = [F(0), F(6)]
    for n in range(1, N):
        c = 34*n**3 + 51*n**2 + 27*n + 5
        d = F((n+1)**3)
        a.append((c*a[n] - n**3*a[n-1])/d)
        b.append((c*b[n] - n**3*b[n-1])/d)
    return a, b

def a_sum(n):
    return sum(comb(n,k)**2 * comb(n+k,k)**2 for k in range(n+1))

def b_sum(n):
    H3 = sum(F(1, m**3) for m in range(1, n+1))
    tot = F(0)
    inner = F(0)
    for k in range(n+1):
        if k >= 1:
            inner += F((-1)**(k-1), 2*k**3*comb(n,k)*comb(n+k,k))
        tot += comb(n,k)**2 * comb(n+k,k)**2 * (H3 + inner)
    return tot

# ---------- p-adic helpers ----------
def vp(x, p):
    """valuation of a Fraction"""
    if x == 0: return None
    num, den = x.numerator, x.denominator
    v = 0
    while num % p == 0: num//=p; v+=1
    while den % p == 0: den//=p; v-=1
    return v

def to_zp(x, p, prec):
    """x in Z_p (must be p-integral) -> residue mod p^prec, as int in [0,p^prec)"""
    M = p**prec
    num, den = x.numerator, x.denominator
    assert den % p != 0, "not p-integral"
    return (num % M) * pow(den, -1, M) % M

def digits(r, p, prec):
    d = []
    for _ in range(prec):
        d.append(r % p); r //= p
    return d

def teich(a, p, prec):
    """Teichmuller lift of a mod p^prec (a a p-unit)."""
    M = p**prec
    x = a % M
    for _ in range(prec*2+5):
        # Newton for x^(p-1)=1: x <- x - (x^p - x)/(p x^{p-1} - 1)
        f = (pow(x, p, M) - x) % M
        d = (p*pow(x, p-1, M) - 1) % M
        x = (x - f*pow(d, -1, M)) % M
    return x

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv)>1 else 400
    a, b = gen_recurrence(N)
    # verify against closed forms
    for n in range(0, 9):
        assert a[n] == a_sum(n), (n, a[n], a_sum(n))
        assert b[n] == b_sum(n), (n, b[n], b_sum(n))
    print("closed-form check n<=8: OK")
    print("a_0..a_5 =", [int(x) for x in a[:6]])
    print("b_1 =", b[1], " b_2 =", b[2], " b_3 =", b[3])
    # archimedean sanity: b_n/a_n -> zeta(3)
    import decimal
    decimal.getcontext().prec = 80
    r = decimal.Decimal(b[N-1].numerator)/decimal.Decimal(b[N-1].denominator)
    q = decimal.Decimal(a[N-1].numerator)/decimal.Decimal(a[N-1].denominator)
    print("b_n/a_n at n=%d ="%(N-1), (r/q))
    print("zeta(3)         = 1.2020569031595942853997381615114499907649862923404988817922715553418382057863130901864558736093352581")
    json.dump({"a":[[x.numerator,x.denominator] for x in a],
               "b":[[x.numerator,x.denominator] for x in b]},
              open("/tmp/claude-1000/-home-ubuntu-fable-episode-2-zeta-math-2/65d6d51f-5045-4f1b-98cc-77989fc30264/scratchpad/apery.json","w"))
    print("written")
