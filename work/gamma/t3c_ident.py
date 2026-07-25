"""T3c: careful graded identification of kappa_j and lambda_j.

Bases are built from  zeta(2)^a * prod zeta(odd)  -- provably independent-looking
(no internal relations; checked by running PSLQ on the basis alone first).
MZV generators (zeta(3,5) at w=8, etc.) are added where the zeta-product basis is
known to be short of Zagier's dimension d_w.
"""
import sys, json, itertools
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma')
from mpmath import mp, mpf, nstr, pslq, zeta, pi, log, sqrt, polyroots
from frobkappa import kappa_series, slog
from bzop import QS
from fractions import Fraction

DPS = int(sys.argv[1]) if len(sys.argv) > 1 else 300
K = int(sys.argv[2]) if len(sys.argv) > 2 else 13
TOL = int(sys.argv[3]) if len(sys.argv) > 3 else 200
mp.dps = DPS

# ---------------- double/triple zeta by Euler-Maclaurin on the Hurwitz tail
def zeta_mult(ss, N=None):
    """zeta(s_1,...,s_k) = sum_{n_1>n_2>...>n_k>=1} prod n_i^{-s_i}, s_1>=2."""
    if N is None:
        N = int(mp.dps * 1.2) + 40
    k = len(ss)
    # nested tails: T_k(m) = sum_{n<m} n^{-s_k}  built up; use exact partial sums to N
    # then Euler-Maclaurin for the outermost variable.
    # inner_j(m) = sum_{m>n_{j+1}>...>n_k>=1} prod_{i>j} n_i^{-s_i}
    # Direct summation to N plus asymptotic tail for the outer sum.
    # inner values as functions of m computed incrementally.
    inner = [mp.mpf(0)] * (k + 1)   # inner[j] = partial value for level j
    # We iterate m from 1..N accumulating.
    vals = []
    acc = [mp.mpf(0)] * k  # acc[j] = sum over n_{j+1} ... for n_{j+1} < current m
    tot = mp.mpf(0)
    # Simpler: recursive definition with memo of prefix sums
    # A_k(m) = sum_{n=1}^{m} n^{-s_k}
    # A_j(m) = sum_{n=1}^{m} n^{-s_j} A_{j+1}(n-1)
    A = [mp.mpf(0)] * k
    for m in range(1, N + 1):
        newA = [mp.mpf(0)] * k
        # compute from innermost
        for j in range(k - 1, -1, -1):
            if j == k - 1:
                newA[j] = A[j] + mp.mpf(1) / mp.mpf(m) ** ss[j]
            else:
                newA[j] = A[j] + (A[j + 1]) / mp.mpf(m) ** ss[j]
        A = newA
    tot = A[0]
    # tail correction for the OUTER sum: sum_{m>N} m^{-s1} A_2(m-1)
    # A_2(m-1) -> zeta(s2,...,sk) - O(m^{1-s2}); use asymptotic expansion
    if k == 1:
        return mp.zeta(ss[0])
    zin = zeta_mult(ss[1:], N)
    # A_2(m-1) = zin - R(m),  R(m) = sum_{n>=m} n^{-s2} A_3(n-1) ~ zin3 * zeta(s2,m) - ...
    # keep two orders:
    tail = zin * (mp.zeta(ss[0]) - sum(mp.mpf(1) / mp.mpf(m) ** ss[0] for m in range(1, N + 1)))
    if k >= 2:
        zin3 = zeta_mult(ss[2:], N) if k >= 3 else mp.mpf(1)
        # R(m) ~ zin3 * zeta(s2, m); sum_{m>N} m^{-s1} zin3 zeta(s2,m)
        corr = mp.mpf(0)
        for m in range(N + 1, N + 1 + 6 * N):
            corr += zin3 * mp.zeta(ss[1], m) / mp.mpf(m) ** ss[0]
        tail -= corr
    return tot + tail

# ---------------- operators
rts = sorted(polyroots([4, -2368, -188, 1], maxsteps=400, extraprec=8 * mp.prec),
             key=lambda r: -abs(r))
lam3 = rts[0].real
q3 = [[0, 0, 0, 1], [-5, -27, -51, -34], [1, 3, 3, 1]]
q2 = [[0, 0, 1], [-3, -11, -11], [-1, -2, -1]]
OPS = {'BZ': (QS, lam3), 'A3': (q3, 17 + 12 * sqrt(2)), 'A2': (q2, (11 + 5 * sqrt(5)) / 2)}
res = {}
for name, (qs, lam) in OPS.items():
    r, al, c, ch = kappa_series(qs, lam, 0, K, 200, [600])
    kap = r[600][0]
    res[name] = {'kappa': kap, 'lambda': slog(kap, K), 'alpha': al, 'S0': r[600][1],
                 'logc': log(1 / lam)}

# ---------------- bases:  zeta(2)^a * prod_{odd} zeta(o)
z2 = zeta(2)
def zprod_basis(w):
    out = []
    def rec(rem, minodd, name, val):
        if rem % 2 == 0 and rem >= 0:
            out.append((name + ('z2^%d' % (rem // 2) if rem > 0 else ''),
                        val * z2 ** (rem // 2)))
        o = minodd
        while o <= rem:
            rec(rem - o, o, name + 'z%d.' % o, val * zeta(o))
            o += 2
    rec(w, 3, '', mp.mpf(1))
    # dedupe/keep
    return out

DIM = {2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 4, 9: 5, 10: 7, 11: 9, 12: 12, 13: 16}

def basis(w, with_extra=False):
    bs = zprod_basis(w)
    if with_extra:
        if w == 8:
            bs.append(('z(3,5)', zeta_mult([3, 5])))
        if w == 10:
            bs.append(('z(3,7)', zeta_mult([3, 7])))
            bs.append(('z2z(3,5)', z2 * zeta_mult([3, 5])))
        if w == 11:
            bs.append(('z3z(3,5)', zeta(3) * zeta_mult([3, 5])))
            bs.append(('z(3,5,3)', zeta_mult([3, 5, 3])))
    return bs

def ident(label, val, w, tol=TOL, maxc=10 ** 18):
    bs = basis(w)
    names = [b[0] for b in bs]
    # basis hygiene: internal relation check
    intern = pslq([b[1] for b in bs], tol=mpf(10) ** (-tol), maxcoeff=maxc, maxsteps=10 ** 6) \
        if len(bs) >= 2 else None
    tag = "" if intern is None else "  [!! basis has internal relation %s]" % intern
    r = pslq([val] + [b[1] for b in bs], tol=mpf(10) ** (-tol), maxcoeff=maxc, maxsteps=2 * 10 ** 6)
    if r is None or r[0] == 0:
        print("   %-12s w=%-2d : NONE  (dim_basis=%d, d_w=%s, tol 1e-%d, |c|<=%.0e)%s"
              % (label, w, len(bs), DIM.get(w), tol, maxc, tag))
        return None
    c0 = r[0]
    terms = " ".join("%+s*%s" % (Fraction(-r[i + 1], c0), names[i])
                     for i in range(len(names)) if r[i + 1] != 0)
    print("   %-12s w=%-2d = %s%s" % (label, w, terms, tag))
    return r

# --- validate the MZV routine on known reductions before using it
print("MZV routine validation:")
print("  stuffle z3z5 - z(3,5)-z(5,3)-z8 = %s"
      % nstr(zeta(3)*zeta(5) - zeta_mult([3,5]) - zeta_mult([5,3]) - zeta(8), 8))
print("  z(4,2) vs span{z6,z3^2}: %s"
      % pslq([zeta_mult([4,2]), zeta(6), zeta(3)**2], tol=mpf(10)**(-40), maxcoeff=10**8))
print("  z(6,2) vs span{z8,z3z5,z2z3^2}: %s"
      % pslq([zeta_mult([6,2]), zeta(8), zeta(3)*zeta(5), zeta(2)*zeta(3)**2],
             tol=mpf(10)**(-40), maxcoeff=10**8))
print("  z(5,2) vs span{z7,z2z5,z4z3}: %s"
      % pslq([zeta_mult([5,2]), zeta(7), zeta(2)*zeta(5), zeta(4)*zeta(3)],
             tol=mpf(10)**(-40), maxcoeff=10**8))

for kind in ['kappa', 'lambda']:
    print("\n=== %s_j (tol 1e-%d) ===" % (kind, TOL))
    for name in ['BZ', 'A3', 'A2']:
        print(" -- %s --" % name)
        for j in range(2, K + 1):
            ident("%s_%d" % (kind, j), res[name][kind][j], j)

json.dump({n: {'kappa': [mp.nstr(x, 210) for x in res[n]['kappa']],
               'lambda': [mp.nstr(x, 210) for x in res[n]['lambda']],
               'S0': mp.nstr(res[n]['S0'], 210),
               'logc': mp.nstr(res[n]['logc'], 210)} for n in res},
          open('/home/ubuntu/fable-episode-2/zeta-math-2/work/gamma/kappas.json', 'w'), indent=1)
print("\nsaved kappas.json")
