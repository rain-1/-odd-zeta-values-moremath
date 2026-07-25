"""T2: the one-generator question.
Load tower data, cap every limit at its CERTIFIED precision (3 digits per level,
Lambda_a = L_s mod p^{v+3(s+1)}), and test ansaetze.
"""
import sys, json, os
from fractions import Fraction as Fr
from core import apery_exact
from pnum import P
from plin import test_ansatz, mk

SCRATCH = "/tmp/claude-1000/-home-ubuntu-fable-episode-2-zeta-math-2/65d6d51f-5045-4f1b-98cc-77989fc30264/scratchpad"

def load(p, cap_extra=0):
    d = json.load(open(os.path.join(SCRATCH, "lam_p%d.json" % p)))
    out = {}
    for a, rows in d["towers"].items():
        a = int(a)
        r = rows[-1]
        s = r["s"]
        cert = 3*(s+1) + cap_extra          # certified RELATIVE digits
        def cut(key):
            v, u, pr = r[key]
            pr = min(pr, cert)
            return P(p, v, u % p**pr, pr)
        out[a] = dict(s=s, L=cut("L"), At=cut("At"), Bt=cut("Bt"))
    return out, d

def apery_rat(amax=20):
    A, B = apery_exact(amax+2)
    import math
    a = [Fr(A[n], math.factorial(n)**3) for n in range(amax+2)]
    b = [Fr(B[n], math.factorial(n)**3) for n in range(amax+2)]
    return a, b

def main(p):
    dat, raw = load(p)
    a_, b_ = apery_rat(20)
    As = sorted(dat)
    print("=" * 78)
    print("p = %d   towers a = %s   certified rel. digits = %s"
          % (p, As, [3*(dat[a]["s"]+1) for a in As]))
    for a in As:
        L = dat[a]["L"]
        print("   a=%-3d  v(L)=%-3d  L = [%s]   f(a)=%s" %
              (a, L.v, " ".join(map(str, L.digits(min(L.prec, 12)))), b_[a]/a_[a]))

    D = [(a, dat[a]["L"]) for a in As]
    DA = [(a, dat[a]["At"]) for a in As]
    DB = [(a, dat[a]["Bt"]) for a in As]
    one = lambda a: Fr(1)
    aa = lambda a: a_[a]
    bb = lambda a: b_[a]
    ff = lambda a: b_[a]/a_[a]
    aa1 = lambda a: a_[a+1]
    bb1 = lambda a: b_[a+1]
    idn = lambda a: Fr(a)

    print(" -- ansatz tests on Lambda_a (residual digits / available; want ~available) --")
    test_ansatz(D, [bb, aa], [one], p, "(i)   L = a*b_a + b*a_a")
    test_ansatz(D, [ff, one], [one], p, "(i')  L = a*f(a) + b")
    test_ansatz(D, [one], [one], p, "(0)   L = const")
    test_ansatz(D, [ff], [one], p, "(0')  L = a*f(a)")
    test_ansatz(D, [bb, aa], [bb, aa], p, "(ii)  Moebius in (a_a,b_a)")
    test_ansatz(D, [bb, aa, one], [bb, aa, one], p, "(ii+) Moebius in (a_a,b_a,1)")
    test_ansatz(D, [ff, one, idn], [one], p, "(ii*) L = a f(a)+b+c*a")
    test_ansatz(D, [bb, aa, bb1, aa1], [bb, aa, bb1, aa1], p, "(iii) Moebius in state vector")
    print(" -- ansatz tests on Atil_a --")
    test_ansatz(DA, [aa, bb], [one], p, "At = a*a_a + b*b_a")
    test_ansatz(DA, [aa], [one], p, "At = a*a_a")
    test_ansatz(DA, [aa, bb, one], [one], p, "At = a*a_a + b*b_a + c")
    test_ansatz(DA, [aa, aa1], [one], p, "At = a*a_a + b*a_{a+1}")
    print(" -- ansatz tests on Btil_a --")
    test_ansatz(DB, [aa, bb], [one], p, "Bt = a*a_a + b*b_a")
    test_ansatz(DB, [bb], [one], p, "Bt = a*b_a")
    test_ansatz(DB, [aa, bb, one], [one], p, "Bt = a*a_a + b*b_a + c")

if __name__ == "__main__":
    for p in [int(x) for x in sys.argv[1:]]:
        main(p)
