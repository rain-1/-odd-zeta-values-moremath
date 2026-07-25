"""T1: tower limits Lambda_a = lim_s p^{3s} b_{a p^s}/a_{a p^s}  (Apery zeta(3) pair),
plus the two *separate* limits  Atil_a = lim_s a_{a p^s}  and  Btil_a = lim_s p^{3s} b_{a p^s}
(the latter make sense because of the Beukers-Coster supercongruence a_{mp^s} = a_{mp^{s-1}}
mod p^{3s}; VERIFIED here, not assumed).

Method: integer recurrence  u_{n+1} = c_n u_n - n^6 u_{n-1}  mod p^K, one pass to N.
alpha_n = (n!)^3 a_n, beta_n = (n!)^3 b_n  =>  f(n) = beta_n/alpha_n and
a_n = alpha_n/(n!)^3 needs K > 3 v_p(N!).
"""
import sys, time, json, os
from core import vp_fact, agree, vp_int_mod

def towers(p, N, amax=12, target=40, verbose=True):
    K = target + 3*vp_fact(N, p) + 30
    M = p**K
    # indices we need
    want = {}
    for a in range(1, amax+1):
        if a % p == 0:
            continue
        s = 0
        n = a
        while n <= N:
            want.setdefault(n, []).append((a, s))
            s += 1
            n *= p
    idx = sorted(want)
    t0 = time.time()
    a0, a1 = 1 % M, 5 % M
    b0, b1 = 0 % M, 6 % M
    res = {}
    if 0 in want: res[0] = (a0, b0)
    if 1 in want: res[1] = (a1, b1)
    nxt = set(idx)
    for n in range(1, N):
        c = 34*n**3 + 51*n**2 + 27*n + 5
        n6 = n**6
        a0, a1 = a1, (c*a1 - n6*a0) % M
        b0, b1 = b1, (c*b1 - n6*b0) % M
        if n+1 in nxt:
            res[n+1] = (a1, b1)
    if verbose:
        print("  recurrence pass N=%d K=%d digits: %.1fs" % (N, K, time.time()-t0))
    # convert: f(n) = beta/alpha ; a_n = alpha/(n!)^3 ; b_n = beta/(n!)^3
    out = {}
    for a in range(1, amax+1):
        if a % p == 0:
            continue
        rows = []
        s = 0; n = a
        while n <= N:
            al, be = res[n]
            e = 3*vp_fact(n, p)              # v_p((n!)^3)
            # strip p^e from alpha and beta (they are divisible by at least p^e? not beta)
            prec = K - e                      # available digits after stripping
            # v_p(alpha_n) = e + v_p(a_n);  v_p(beta_n) >= e - 3*floor(log_p n)
            va = vp_int_mod(al, p, K) - e     # = v_p(a_n)
            vb = vp_int_mod(be, p, K) - e     # = v_p(b_n)
            # f(n) = beta/alpha  as p^(vb-va) * unit, known mod p^(prec - ...)
            au = (al // p**(e+va)) % p**(prec-va)
            bu = (be // p**(e+vb)) % p**(prec-vb)
            v = vb - va
            # unit part of f(n): bu/au  mod p^(prec - max(va,vb) ) -- be conservative
            pr = prec - max(va, vb, 0) - 2
            fu = bu % p**pr * pow(au % p**pr, -1, p**pr) % p**pr
            # L_s = p^{3s} f(n): valuation v+3s, unit fu
            rows.append(dict(s=s, n=n, va=va, vb=vb, vL=v+3*s, fu=fu, pr=pr,
                             au=au % p**pr, aprec=prec-va))
            s += 1; n *= p
        out[a] = rows
    return out, K

def report(p, out, K):
    print("p = %d" % p)
    for a, rows in sorted(out.items()):
        if len(rows) < 2:
            continue
        # agreement between successive L_s (same valuation expected)
        ag = []
        for i in range(1, len(rows)):
            r0, r1 = rows[i-1], rows[i]
            if r0["vL"] != r1["vL"]:
                ag.append("V%d/%d" % (r0["vL"], r1["vL"]))
            else:
                pr = min(r0["pr"], r1["pr"])
                ag.append(agree(r0["fu"], r1["fu"], p, pr))
        agA = []
        for i in range(1, len(rows)):
            r0, r1 = rows[i-1], rows[i]
            pr = min(r0["aprec"], r1["aprec"])
            agA.append(agree(r0["au"], r1["au"], p, pr))
        print("  a=%-3d smax=%d  v_p(Lambda)=%d  agree(L_s,L_{s-1})=%s   agree(a-tower)=%s"
              % (a, rows[-1]["s"], rows[-1]["vL"], ag, agA))

if __name__ == "__main__":
    p = int(sys.argv[1]); N = int(sys.argv[2])
    amax = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    out, K = towers(p, N, amax)
    report(p, out, K)
