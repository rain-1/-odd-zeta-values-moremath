"""Probe of (F+):  Tcal(b,c) == (Q_n/Q_a) T(a,b,c)  mod p^{2 + v_p(T(a,b,c))}.

Tcal(b,c) = sum_{s,t=0}^{p-1} T(n, bp+s, cp+t),  n = ap+r.
Everything mod p^CAP, exactly.  Q_n is recomputed as sum_{b,c} Tcal(b,c) (self-contained),
and cross-checked against the exact ladder when n <= 360.
"""
import sys
from math import comb
from core import Q, Hs, w3hat, vp

CAP = 10


def vp_mod(x, p, cap=CAP):
    x %= p ** cap
    if x == 0:
        return cap
    v = 0
    while x % p == 0:
        x //= p
        v += 1
    return v


def v_weight(a, b, c):
    return w3hat(a, b, c) - Hs(a, 3)


def Tlevel(a, b, c):
    return (comb(a + b, a) * comb(a, b) ** 2 * comb(a + c, a) * comb(a, c) ** 2
            * comb(a + b + c, a))


def fibre_table(p, a, r, M):
    """Return dict (b,c) -> Tcal(b,c) mod M, for n = ap+r."""
    n = a * p + r
    c1 = [comb(n + i, n) % M for i in range(n + 1)]          # C(n+k,n)
    c2 = [comb(n, i) % M for i in range(n + 1)]              # C(n,k)
    c3 = [comb(n + j, n) % M for j in range(2 * n + 1)]      # C(n+k+l,n)
    tk = [c1[i] * c2[i] % M * c2[i] % M for i in range(n + 1)]
    out = {}
    for b in range(a + 1):
        lo_k, hi_k = b * p, min(n, b * p + p - 1)
        for c in range(a + 1):
            lo_l, hi_l = c * p, min(n, c * p + p - 1)
            acc = 0
            for k in range(lo_k, hi_k + 1):
                tkk = tk[k]
                if tkk == 0:
                    continue
                s = 0
                for l in range(lo_l, hi_l + 1):
                    s += tk[l] * c3[k + l] % M
                acc += tkk * (s % M)
            out[(b, c)] = acc % M
    return out


def run(p, verbose=False, nmax=None):
    M = p ** CAP
    stats = {}   # (d, vT) -> min slack_F, min slack_Fplus, count
    fails_F = fails_Fp = 0
    ncell = 0
    for a in range(1, p):
        Qa = int(Q(a))
        if Qa % p == 0:
            continue
        Ta = {(b, c): Tlevel(a, b, c) for b in range(a + 1) for c in range(a + 1)}
        dd = {bc: max(0, -vp(v_weight(a, bc[0], bc[1]), p)) for bc in Ta}
        vT = {bc: vp(Ta[bc], p) for bc in Ta}
        for r in range(p):
            n = a * p + r
            if nmax is not None and n > nmax:
                continue
            ncell += 1
            tab = fibre_table(p, a, r, M)
            Qn = sum(tab.values()) % M
            if n <= 360:
                assert (Qn - int(Q(n))) % M == 0, (p, a, r, 'Qn mismatch')
            Lam = Qn * pow(Qa % M, -1, M) % M
            for bc, val in tab.items():
                diff = (val - Lam * Ta[bc]) % M
                v = vp_mod(diff, p)
                sF = v - (1 + dd[bc])
                sFp = v - (2 + min(vT[bc], CAP))
                key = (dd[bc], min(vT[bc], 6))
                cur = stats.get(key)
                if cur is None:
                    stats[key] = [sF, sFp, 1]
                else:
                    cur[0] = min(cur[0], sF)
                    cur[1] = min(cur[1], sFp)
                    cur[2] += 1
                if sF < 0:
                    fails_F += 1
                    if verbose:
                        print('  F FAIL p=%d a=%d r=%d bc=%s d=%d vT=%d v=%d'
                              % (p, a, r, bc, dd[bc], vT[bc], v))
                if sFp < 0:
                    fails_Fp += 1
                    if verbose and fails_Fp < 15:
                        print('  F+ FAIL p=%d a=%d r=%d bc=%s d=%d vT=%d v=%d'
                              % (p, a, r, bc, dd[bc], vT[bc], v))
    return ncell, fails_F, fails_Fp, stats


if __name__ == '__main__':
    args = [int(x) for x in sys.argv[1:]] or [5, 7, 11]
    for p in args:
        ncell, fF, fFp, stats = run(p, verbose=True)
        print('p=%2d cells=%4d  F-failures=%d  F+failures=%d' % (p, ncell, fF, fFp), flush=True)
        print('   (d,vT) -> [min slack F, min slack F+, count]')
        for key in sorted(stats):
            print('     ', key, stats[key])
        print(flush=True)
