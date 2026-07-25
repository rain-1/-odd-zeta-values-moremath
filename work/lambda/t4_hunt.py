"""T2/T3: the big hunt.  For each prime:
  (a) the harmonic split  Lambda_a = h_p(a) + C_p(a)   [h_p exact and cheap]
  (b) one-generator tests among the Lambda's / defects
  (c) algebraicity tests
  (d) zoo: LLL against zeta_p(3), zeta_p(5), log_p(2), log_p(3), Fermat/Wolstenholme
      quotients, B_{p-3}, the modular unit root.
All precisions are the CERTIFIED ones (3 digits per tower level).
"""
import sys, json, os
from fractions import Fraction as Fr
from pnum import P
from t2_ansatz import load, apery_rat
from t3_harm import h_p
from hunt import relation, scale, alg_test
import zoo

def main(p, verbose=True):
    dat, raw = load(p)
    a_, b_ = apery_rat(20)
    As = sorted(dat)
    print("=" * 78)
    print("p = %d" % p)
    K1 = dat[1]["L"].prec
    # ---------------------------------------------------------------- harmonic split
    print("\n[A] harmonic split  Lambda_a = h_p(a) + C_p(a),  h_p(a) = sum_{x in Z[1/p], 0<x<=a} x^-3")
    C = {}
    for a in As:
        L = dat[a]["L"]
        H = h_p(a, p, L.prec + max(0, -L.v) + 4)
        C[a] = (L - H).trunc(L.prec)
        print("   a=%-3d v(L)=%-3d v(h)=%-3d v(C)=%-4s prec(C)=%d" %
              (a, L.v, H.v, C[a].v if not C[a].is_zero() else "inf", C[a].prec))
    # is h_p(1) itself something?
    z3 = zoo.zeta_p_val(3, p, K1 + 4)
    z5 = zoo.zeta_p_val(5, p, K1 + 4)
    one = P.from_frac(p, 1, K1 + 4)
    H1 = h_p(1, p, K1 + 4)
    vals, K = scale([one, z3, H1]); relation(vals, p, K, ["1", "z3", "h_p(1)"], tag="(1, zeta_p(3), h_p(1))")
    vals, K = scale([one, H1]); relation(vals, p, K, ["1", "h_p(1)"], tag="h_p(1) rational?")
    alg_test(H1, 2, p, tag="h_p(1) algebraic deg 2?")
    # ---------------------------------------------------------------- one-generator
    print("\n[B] one-generator tests")
    fa = {a: P.from_frac(p, b_[a]/a_[a], dat[a]["L"].prec + 8) for a in As}
    delta = {a: (dat[a]["L"] - fa[a]) for a in As}
    small = [a for a in As if a <= 4]
    for i, a in enumerate(small):
        for b in small[i+1:]:
            x, y = delta[a], delta[b]
            vals, K = scale([x, y])
            relation(vals, p, K, ["d%d" % a, "d%d" % b], tag="delta_%d / delta_%d in Q?" % (a, b))
    for i, a in enumerate(small):
        for b in small[i+1:]:
            vals, K = scale([one.trunc(K1), dat[a]["L"], dat[b]["L"]])
            relation(vals, p, K, ["1", "L%d" % a, "L%d" % b],
                     tag="(1, Lambda_%d, Lambda_%d) span 2?" % (a, b))
    for i, a in enumerate(small):
        for b in small[i+1:]:
            x, y = C[a], C[b]
            if x.is_zero() or y.is_zero(): continue
            vals, K = scale([x, y])
            relation(vals, p, K, ["C%d" % a, "C%d" % b], tag="C_%d / C_%d in Q?" % (a, b))
    # ---------------------------------------------------------------- algebraicity
    print("\n[C] algebraicity of Lambda_1, Atil_1, C_1")
    for nm, x in (("Lambda_1", dat[1]["L"]), ("Atil_1", dat[1]["At"]),
                  ("Btil_1", dat[1]["Bt"]), ("C_1", C[1])):
        if x.is_zero(): continue
        for d in (2, 3):
            alg_test(x, d, p, tag="%s algebraic deg %d?" % (nm, d))
    # ---------------------------------------------------------------- the zoo
    print("\n[D] the zoo")
    KZ = K1
    # NOTE: the Fermat/Wolstenholme quotients and B_{p-3} are RATIONAL numbers, so an
    # LLL against (1, .) is vacuous; they enter only as mod-p congruence data (printed below).
    Z = {
        "1": one.trunc(KZ),
        "z3": z3.trunc(KZ), "z5": z5.trunc(KZ),
        "log2": zoo.iwasawa_log(2, p, KZ), "log3": zoo.iwasawa_log(3, p, KZ),
        "log5": zoo.iwasawa_log(5, p, KZ) if p != 5 else None,
    }
    u, ap = zoo.unit_root(p, KZ)
    if u is not None:
        Z["unitroot"] = u
    Z = {k: v for k, v in Z.items() if v is not None}
    print("   zoo members:", list(Z))
    targets = [("Lambda_1", dat[1]["L"]), ("Atil_1", dat[1]["At"]), ("C_1", C[1]),
               ("h_p(1)", H1.trunc(KZ))]
    print("   rational zoo (mod p only): q2=%s q3=%s w1=%s w2=%s B_{p-3}=%s" %
          (zoo.fermat_quot(2, p), zoo.fermat_quot(3, p), zoo.wolstenholme(p)[0],
           zoo.wolstenholme(p)[1], zoo.bern(p-3)))
    for nm, x in targets:
        if x.is_zero(): continue
        print("      %-9s leading digits: %s" % (nm, x.digits(min(x.prec, 8))))
        for zn in Z:
            if zn == "1": continue
            vals, K = scale([Z["1"], Z[zn], x])
            relation(vals, p, K, ["1", zn, nm], tag="(1, %s, %s)" % (zn, nm))
        if u is not None:
            vals, K = scale([Z["1"], u, x])
            relation(vals, p, K, ["1", "unitroot", nm], tag="(1, unitroot, %s)" % nm)
        vals, K = scale([Z["1"], Z["z3"], Z["log2"], x])
        relation(vals, p, K, ["1", "z3", "log2", nm], tag="(1, z3, log2, %s)" % nm)
    return dat, C, Z

if __name__ == "__main__":
    for p in [int(x) for x in sys.argv[1:]]:
        main(p)
