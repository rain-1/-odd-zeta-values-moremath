"""T2b: the DEFECTS.  delta_a = Lambda_a - f(a),  eps_a = Atil_a - a_a,  eta_a = Btil_a - b_a.
All have v_p >= 3 (the supercongruence).  One-generator test: is delta_a/delta_1 rational?
(equivalently Lambda_a = f(a) + kappa * g(a) with g in Q).  Exact throughout."""
import sys, json, os
from fractions import Fraction as Fr
from core import apery_exact
from pnum import P
from t2_ansatz import load, apery_rat

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "padic_seam"))
from lll import rat_recon

def show(p, name, vals, ref):
    """vals: dict a -> P.  Report v_p, and rational reconstruction of vals[a]/vals[ref]."""
    print("  %s :" % name)
    r0 = vals[ref]
    for a in sorted(vals):
        x = vals[a]
        if x.is_zero():
            print("     a=%-3d  ZERO to precision %d" % (a, x.prec)); continue
        q = x / r0
        pr = q.prec
        # rational reconstruction of the unit part times p^v
        rr = rat_recon(q.u, p, pr)
        ok = ""
        if rr is not None:
            cand = Fr(p)**q.v * rr
            # certify: recompute
            h = max(abs(rr.numerator), rr.denominator)
            ok = "  == %s  (height %.1e, floor %.1e)" % (cand, float(h), float(p)**(pr/2.0))
            if h > float(p)**(pr/2.0)/4:
                ok += " [NOISE]"
        print("     a=%-3d  v=%-3d prec=%-3d  ratio v=%-3d%s" % (a, x.v, x.prec, q.v, ok))

def main(p):
    dat, raw = load(p)
    a_, b_ = apery_rat(20)
    As = sorted(dat)
    print("=" * 78); print("p =", p)
    delta, eps, eta = {}, {}, {}
    for a in As:
        L, At, Bt = dat[a]["L"], dat[a]["At"], dat[a]["Bt"]
        fa = P.from_frac(p, b_[a]/a_[a], L.prec + 10)
        delta[a] = L - fa
        eps[a] = At - P.from_frac(p, a_[a], At.prec + 10)
        eta[a] = Bt - P.from_frac(p, b_[a], Bt.prec + 10)
    ref = As[0]
    show(p, "delta_a = Lambda_a - f(a),  ratio to a=%d" % ref, delta, ref)
    show(p, "eps_a   = Atil_a  - a_a  ,  ratio to a=%d" % ref, eps, ref)
    show(p, "eta_a   = Btil_a  - b_a  ,  ratio to a=%d" % ref, eta, ref)
    return delta, eps, eta

if __name__ == "__main__":
    for p in [int(x) for x in sys.argv[1:]]:
        main(p)
