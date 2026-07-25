"""T1: full tower data for the Apery zeta(3) pair.
For p in {5,7,11,13} and a <= AMAX with p !| a, compute along n_s = a p^s:
    L_s   = p^{3s} b_{n_s}/a_{n_s}          -> Lambda_a
    At_s  = a_{n_s}                          -> Atil_a   (Beukers-Coster limit)
    Bt_s  = p^{3s} b_{n_s}                   -> Btil_a
all as exact p-adic numbers with honest precision.  Output: JSON.

Single pass of the integer recurrence alpha,beta mod p^K with
K = target + 3 v_p(N!) + slack, plus the running p-free factorial product.
"""
import sys, time, json, os
from core import vp_fact
from pnum import P

SCRATCH = "/tmp/claude-1000/-home-ubuntu-fable-episode-2-zeta-math-2/65d6d51f-5045-4f1b-98cc-77989fc30264/scratchpad"

def run(p, N, amax=12, target=45):
    K = target + 3*vp_fact(N, p) + 20
    K2 = target + 20                      # precision for the p-free factorial product
    M = p**K; M2 = p**K2
    want = {}
    for a in range(1, amax+1):
        if a % p == 0: continue
        n = a; s = 0
        while n <= N:
            want.setdefault(n, []).append((a, s)); s += 1; n *= p
    # also need p-free factorial blocks at floor(n/p^j) for j beyond the tower base
    extra = set()
    for a in range(1, amax+1):
        m = a
        while m:
            extra.add(m); m //= p
    need = set(want) | extra | {0}
    t0 = time.time()
    a0, a1 = 1 % M, 5 % M
    b0, b1 = 0 % M, 6 % M
    pf = 1                                 # prod_{m<=n, p!|m} m  mod p^K2
    res = {}; blk = {0: 1}
    if 1 in need: res[1] = (a1, b1)
    pf = 1  # after m=1
    if 1 in need: blk[1] = pf
    for n in range(1, N):
        c = 34*n**3 + 51*n**2 + 27*n + 5
        n6 = n**6
        a0, a1 = a1, (c*a1 - n6*a0) % M
        b0, b1 = b1, (c*b1 - n6*b0) % M
        m = n+1
        if m % p: pf = pf * m % M2
        if m in need:
            res[m] = (a1, b1); blk[m] = pf
    el = time.time()-t0
    # p-free part of n!
    def fu(n):
        r = 1
        while n:
            r = r * blk[n] % M2
            n //= p
        return r
    out = {}
    for a in range(1, amax+1):
        if a % p == 0: continue
        rows = []
        n = a; s = 0
        while n <= N:
            al, be = res[n]
            e = 3*vp_fact(n, p)
            # alpha_n = p^e * (n!_p-free)^3 * a_n ; beta_n likewise with b_n
            AL = P(p, 0, al, K); AL = AL.rescale(0)
            # careful: al is a residue mod p^K; its valuation is >= e
            AL = P(p, 0, al % M, K)
            BE = P(p, 0, be % M, K)
            f = BE / AL                                   # = b_n/a_n exactly (precision honest)
            L = f.rescale(3*s)
            f3 = pow(fu(n), 3, M2)
            an = P(p, AL.v - e, AL.u, min(AL.prec, K2)) / P(p, 0, f3, K2)
            bn = P(p, BE.v - e, BE.u, min(BE.prec, K2)) / P(p, 0, f3, K2)
            def trunc(x):
                pr = min(x.prec, target)
                return (x.v, x.u % p**pr if pr else 0, pr)
            rows.append(dict(s=s, n=n, L=trunc(L), At=trunc(an), Bt=trunc(bn.rescale(3*s))))
            s += 1; n *= p
        out[a] = rows
    return dict(p=p, N=N, K=K, K2=K2, target=target, elapsed=el, towers=out)

def summarize(d):
    p = d["p"]
    print("p=%d N=%d K=%d  (%.1fs)" % (p, d["N"], d["K"], d["elapsed"]))
    for a, rows in sorted(d["towers"].items(), key=lambda kv: int(kv[0])):
        if len(rows) < 2: continue
        agL, agA, agB = [], [], []
        for i in range(1, len(rows)):
            for key, acc in (("L", agL), ("At", agA), ("Bt", agB)):
                x = P(p, *rows[i-1][key]); y = P(p, *rows[i][key])
                acc.append(y.agree(x) - min(x.v, y.v))     # relative digits
        last = P(p, *rows[-1]["L"])
        print("  a=%-3s s<=%d v(L)=%-3d prec=%-3d relagree L:%s  a-tower:%s  b-tower:%s"
              % (a, rows[-1]["s"], last.v, last.prec, agL, agA, agB))

if __name__ == "__main__":
    p = int(sys.argv[1]); N = int(sys.argv[2])
    amax = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    d = run(p, N, amax)
    summarize(d)
    fn = os.path.join(SCRATCH, "lam%s_p%d.json" % (os.environ.get("LAMTAG",""), p))
    json.dump(d, open(fn, "w"))
    print("written", fn)
