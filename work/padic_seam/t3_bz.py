"""T3: extend the exact BZ ladders by the certified order-3 recurrence, then p-adic towers."""
import sys, json, pickle
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.set_int_max_str_digits(3000000)
from fractions import Fraction as F
from core import ladders, c0, c1, c2, c3

def extend(NMAX):
    lad = {k: dict(v) for k, v in ladders().items()}
    for k in ('Q', 'P', 'Ph'):
        d = lad[k]
        n = max(d) - 2
        while n + 3 <= NMAX:
            d[n+3] = -(c0(n)*d[n] + c1(n)*d[n+1] + c2(n)*d[n+2]) / F(c3(n))
            n += 1
    return lad

if __name__ == "__main__":
    NMAX = int(sys.argv[1])
    lad = extend(NMAX)
    print("extended to", max(lad['Q']))
    import decimal
    decimal.getcontext().prec = 60
    def dec(x): return decimal.Decimal(x.numerator)/decimal.Decimal(x.denominator)
    for n in (300, NMAX):
        print("  n=%5d   P_n/Q_n = %s" % (n, dec(lad['P'][n]/lad['Q'][n])))
        print("            Ph_n/Q_n = %s" % dec(lad['Ph'][n]/lad['Q'][n]))
    pickle.dump({k: {n: (v.numerator, v.denominator) for n, v in d.items()}
                 for k, d in lad.items()}, open("bz_lad.pkl", "wb"))
    print("saved")
