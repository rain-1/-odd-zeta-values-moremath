"""eps55_factory.py -- THE MODULAR FACTORY.

Reverse the companion construction: enumerate (hauptmodul-candidate t,
form-candidate F) pairs from eta-product/Eisenstein banks on genus-zero-ish
levels, set y0(t) := F(q(t)) = sum a_n t^n, hunt 3-term polynomial-coefficient
recurrences for a_n, and catalog the arithmetic.

Conventions (as in work/SPORADIC_MODULAR_DICTIONARY.md):
    P_e(q) = prod_m prod_{k>=1} (1-q^{mk})^{e_m};  t = q*P_e;  F = P_f, F(0)=1.
    Eta-modular cases have sum(m e_m)=24 (t, weight 0) and =0 with
    sum(e_m)=2w (F, weight w); the (-q)-twist t~(q)=-t(-q), F~(q)=F(-q) is
    swept as well (the family-B phenomenon).

Sweep mod p=4194301 at order QS (numpy kernels); every distinct hit is
re-derived EXACTLY (python ints / Fractions) at order QE, shape-matched
against Zagier/AZ/Cooper forms R2/R3, deduped by scaling+twist-invariant
fingerprints, compared against the known fifteen, and (for new pairs) the
second solution's denominator arithmetic profiled.  Controls first: the
factory must reproduce the known recurrences from the session's identified
(t,F) data before any sweep verdict counts.
"""

import sys, json, time, itertools
from fractions import Fraction as Fr
from math import lcm

import numpy as np

P = 4194301
QS = 30
QE = 46

# ---------------------------------------------------------------- exact ops
def mul_i(a, b, n):
    out = [0] * n
    for i, ai in enumerate(a[:n]):
        if ai:
            for j, bj in enumerate(b[:n - i]):
                if bj:
                    out[i + j] += ai * bj
    return out

def inv_i(a, n):
    assert a[0] == 1
    out = [1] + [0] * (n - 1)
    for k in range(1, n):
        s = 0
        for j in range(1, min(k, len(a) - 1) + 1):
            s += a[j] * out[k - j]
        out[k] = -s
    return out

def pow_i(a, e, n):
    if e < 0:
        return pow_i(inv_i(a, n), -e, n)
    out = [1] + [0] * (n - 1)
    b = list(a[:n]) + [0] * max(0, n - len(a))
    while e:
        if e & 1:
            out = mul_i(out, b, n)
        b = mul_i(b, b, n)
        e >>= 1
    return out

def compose_i(a, b, n):
    assert b[0] == 0
    out = [0] * n
    for c in reversed(a[:n]):
        out = mul_i(out, b, n)
        out[0] += c
    return out

def revert_i(T, n):
    """q(t) for T(q)=q+...; exact ints."""
    g = [0, 1] + [0] * (n - 2)
    Tp = [(i + 1) * T[i + 1] for i in range(len(T) - 1)]
    m = 2
    while m < n:
        m = min(2 * m, n)
        Tg = compose_i(T, g, m)
        r = list(Tg)
        r[1] -= 1
        Tpg = compose_i(Tp, g, m)
        corr = mul_i(r, inv_i(Tpg, m), m)
        g = [g[i] - (corr[i] if i < len(corr) else 0) for i in range(m)]
        g += [0] * (n - len(g))
    return g[:n]

# ---------------------------------------------------------------- mod-p ops
def mul_p(a, b, n):
    c = np.convolve(a[:n], b[:n])[:n] % P
    return c.astype(np.int64)

def inv_p(a, n):
    out = np.zeros(n, dtype=np.int64)
    i0 = pow(int(a[0]), P - 2, P)
    out[0] = i0
    for k in range(1, n):
        s = int((a[1:k + 1][::-1] * out[:k]).sum() % P) if k else 0
        out[k] = (-i0 * s) % P
    return out

def pow_p(a, e, n):
    if e < 0:
        return pow_p(inv_p(a, n), -e, n)
    out = np.zeros(n, dtype=np.int64)
    out[0] = 1
    b = np.array(list(a[:n]) + [0] * max(0, n - len(a)), dtype=np.int64)
    while e:
        if e & 1:
            out = mul_p(out, b, n)
        b = mul_p(b, b, n)
        e >>= 1
    return out

def compose_p(a, b, n):
    assert b[0] == 0
    out = np.zeros(n, dtype=np.int64)
    for c in a[:n][::-1]:
        out = mul_p(out, b, n)
        out[0] = (out[0] + int(c)) % P
    return out

def revert_p(T, n):
    g = np.zeros(n, dtype=np.int64)
    g[1] = 1
    Tp = np.array([(i + 1) * int(T[i + 1]) % P for i in range(len(T) - 1)],
                  dtype=np.int64)
    m = 2
    while m < n:
        m = min(2 * m, n)
        Tg = compose_p(T, g[:m], m)
        Tg[1] = (Tg[1] - 1) % P
        Tpg = compose_p(Tp, g[:m], m)
        corr = mul_p(Tg, inv_p(Tpg, m), m)
        g2 = (g[:m] - corr) % P
        g = np.concatenate([g2, np.zeros(n - m, dtype=np.int64)])
    return g

# ---------------------------------------------------------------- eta banks
_EF = {}
def euler_factor(m, n):
    out = [0] * n
    k = 0
    while True:
        g1 = k * (3 * k - 1) // 2
        g2 = k * (3 * k + 1) // 2
        s = (-1) ** k
        hit = False
        if m * g1 < n:
            out[m * g1] += s
            hit = True
        if k and m * g2 < n:
            out[m * g2] += s
            hit = True
        if k and not hit:
            break
        k += 1
    return out

def eprod_i(evec, n):
    out = [1] + [0] * (n - 1)
    for m, e in sorted(evec.items()):
        if e:
            key = (m, n)
            if key not in _EF:
                _EF[key] = euler_factor(m, n)
            out = mul_i(out, pow_i(_EF[key], e, n), n)
    return out

def eprod_p(evec, n):
    return np.array([x % P for x in eprod_i(evec, n)], dtype=np.int64)

def enum_evecs(divs, s0_target, s1_target, cap, sumabs_cap, count_cap):
    """sum e = s0_target, sum m*e = s1_target."""
    if len(divs) < 2:
        return []
    out = []
    free = divs[:-2]
    dA, dB = divs[-2], divs[-1]
    det = dB - dA
    for combo in itertools.product(range(-cap, cap + 1), repeat=len(free)):
        if sum(abs(x) for x in combo) > sumabs_cap:
            continue
        s0 = sum(combo)
        s1 = sum(m * e for m, e in zip(free, combo))
        num = (s1_target - s1) - dA * (s0_target - s0)
        if num % det:
            continue
        eB = num // det
        eA = (s0_target - s0) - eB
        if abs(eA) > cap or abs(eB) > cap:
            continue
        ev = {m: e for m, e in zip(free, combo) if e}
        if eA:
            ev[dA] = eA
        if eB:
            ev[dB] = eB
        if sum(abs(e) for e in ev.values()) > sumabs_cap:
            continue
        out.append(ev)
    out.sort(key=lambda ev: (sum(abs(e) for e in ev.values()),
                             max([abs(e) for e in ev.values()] or [0]),
                             sorted(ev.items())))
    # dedupe identical
    ded, seen = [], set()
    for ev in out:
        key = tuple(sorted(ev.items()))
        if key not in seen:
            seen.add(key)
            ded.append(ev)
    return ded[:count_cap]

def sigma1(n_):
    return sum(d for d in range(1, n_ + 1) if n_ % d == 0)

def eis_bank_fr(divs, n):
    """(name, weight, Fraction series) Eisenstein members."""
    E2s = {}
    for d in divs:
        e = [Fr(1)] + [Fr(0)] * (n - 1)
        for k in range(d, n, d):
            e[k] = Fr(-24 * sigma1(k // d))
        E2s[d] = e
    out = []
    for d1, d2 in itertools.combinations(divs, 2):
        den = d2 - d1
        ser = [Fr(d2 * E2s[d2][k] - d1 * E2s[d1][k], den) for k in range(n)]
        out.append(('E2[%d,%d]' % (d1, d2), 2, ser))
    chi3 = lambda x: 0 if x % 3 == 0 else (1 if x % 3 == 1 else -1)
    chi4 = lambda x: 0 if x % 2 == 0 else (1 if x % 4 == 1 else -1)
    for d in divs:
        for nm, chi, mult in (('E1chi3[%d]' % d, chi3, 6),
                              ('E1chi4[%d]' % d, chi4, 4)):
            e = [Fr(1)] + [Fr(0)] * (n - 1)
            for k in range(d, n, d):
                kk = k // d
                e[k] = Fr(mult * sum(chi(dd) for dd in range(1, kk + 1)
                                     if kk % dd == 0))
            out.append((nm, 1, e))
    return out

def fr_to_p(ser):
    return np.array([f.numerator % P * pow(f.denominator % P, P - 2, P) % P
                     for f in ser], dtype=np.int64)

# ---------------------------------------------------------------- fit + shapes
def fit_3term_p(a, maxdeg=4):
    unk = 3 * (maxdeg + 1)
    N = len(a)
    rows = []
    for n_ in range(N - 2):
        row = []
        for i in range(3):
            base = int(a[n_ + i])
            for j in range(maxdeg + 1):
                row.append(base * pow(n_, j, P) % P)
        rows.append(row)
    M = np.array(rows, dtype=np.int64)
    m, w = M.shape
    r = 0
    piv = []
    for c in range(w):
        nz = np.nonzero(M[r:, c] % P)[0]
        if not len(nz):
            continue
        pr = r + nz[0]
        if pr != r:
            M[[r, pr]] = M[[pr, r]]
        M[r] = M[r] * pow(int(M[r, c]), P - 2, P) % P
        col = M[:, c].copy()
        col[r] = 0
        nzr = np.nonzero(col)[0]
        if len(nzr):
            M[nzr] = (M[nzr] - col[nzr, None] * M[r][None, :]) % P
        piv.append(c)
        r += 1
        if r == m:
            break
    dim = w - r
    return dim

def fingerprint(a):
    a = [int(x) % P for x in a]
    if a[1] == 0:
        return ('z', tuple(a[2:12]))
    i1 = pow(a[1], P - 2, P)
    v = [a[k] * pow(i1, k, P) % P for k in range(2, 12)]
    vt = [(x if k % 2 == 0 else (P - x) % P) for k, x in enumerate(v, 2)]
    return min(tuple(v), tuple(vt))

R2 = {'A': (7, 2, -8), 'B': (9, 3, 27), 'C': (10, 3, 9), 'D': (11, 3, -1),
      'E': (12, 4, 32), 'F': (17, 6, 72)}
R3 = {'alpha': (10, 4, 64, 0), 'gamma': (17, 5, 1, 0),
      'delta': (7, 3, 81, 0), 'eps': (12, 4, 16, 0),
      'zeta': (9, 3, -27, 0), 'eta': (11, 5, 125, 0),
      's7': (13, 4, -27, 3), 's10': (6, 2, -64, 4),
      's18': (14, 6, 192, -12)}

def known_seq(name, N):
    u = [1]
    prev = 0
    if name in R2:
        a, b, c = R2[name]
        for n_ in range(N - 1):
            nxt = Fr((a * n_ * n_ + a * n_ + b) * u[-1]
                     - c * n_ * n_ * (u[-2] if n_ >= 1 else prev),
                     (n_ + 1) ** 2)
            u.append(int(nxt))
    else:
        a, b, c, d = R3[name]
        for n_ in range(N - 1):
            nxt = Fr((2 * n_ + 1) * (a * n_ * n_ + a * n_ + b) * u[-1]
                     - n_ * (c * n_ * n_ + d) * (u[-2] if n_ >= 1 else prev),
                     (n_ + 1) ** 3)
            u.append(int(nxt))
    return u

def shape_match_exact(a):
    """R2/R3 exact shape fit from integer a_n; returns (shape, params) or
    (None, None).  Rational parameters are rejected (recorded upstream)."""
    # R2: unknowns A,B,C from n=1,2 plus n=0 gives B=a1.
    B = a[1]
    # n=1: 4 a2 = (2A+B) a1 - C a0 ; n=2: 9 a3 = (6A+B) a2 - 4C a1
    # solve 2x2 in A, C
    M = [[2 * a[1], -1], [6 * a[2], -4 * a[1]]]
    r = [4 * a[2] - B * a[1], 9 * a[3] - B * a[2]]
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    if det:
        Anum = r[0] * M[1][1] - M[0][1] * r[1]
        Cnum = M[0][0] * r[1] - r[0] * M[1][0]
        if Anum % det == 0 and Cnum % det == 0:
            A_, C_ = Anum // det, Cnum // det
            if all((n_ + 1) ** 2 * a[n_ + 1]
                   == (A_ * n_ * n_ + A_ * n_ + B) * a[n_]
                   - C_ * n_ * n_ * a[n_ - 1]
                   for n_ in range(1, len(a) - 1)):
                return ('R2', (A_, B, C_))
    # R3: B=a1; unknowns A, C, D from n=1,2,3
    # (n+1)^3 a_{n+1} = (2n+1)(An^2+An+B)a_n - n(Cn^2+D)a_{n-1}
    rows, rhs = [], []
    for n_ in (1, 2, 3):
        rows.append([(2 * n_ + 1) * (n_ * n_ + n_) * a[n_],
                     -n_ ** 3 * a[n_ - 1], -n_ * a[n_ - 1]])
        rhs.append((n_ + 1) ** 3 * a[n_ + 1] - (2 * n_ + 1) * B * a[n_])
    import fractions
    # 3x3 exact solve
    Mx = [[Fr(x) for x in row] for row in rows]
    bx = [Fr(x) for x in rhs]
    for c in range(3):
        pr = next((t for t in range(c, 3) if Mx[t][c] != 0), None)
        if pr is None:
            return (None, None)
        Mx[c], Mx[pr] = Mx[pr], Mx[c]
        bx[c], bx[pr] = bx[pr], bx[c]
        pv = Mx[c][c]
        Mx[c] = [x / pv for x in Mx[c]]
        bx[c] = bx[c] / pv
        for t in range(3):
            if t != c and Mx[t][c] != 0:
                f = Mx[t][c]
                Mx[t] = [x - f * y for x, y in zip(Mx[t], Mx[c])]
                bx[t] = bx[t] - f * bx[c]
    A_, C_, D_ = bx
    if all(x.denominator == 1 for x in (A_, C_, D_)):
        A_, C_, D_ = int(A_), int(C_), int(D_)
        if all((n_ + 1) ** 3 * a[n_ + 1]
               == (2 * n_ + 1) * (A_ * n_ * n_ + A_ * n_ + B) * a[n_]
               - n_ * (C_ * n_ * n_ + D_) * a[n_ - 1]
               for n_ in range(1, len(a) - 1)):
            return ('R3', (A_, B, C_, D_))
    return (None, None)

def companion_profile(shape, prm, N=26):
    Bs = [Fr(0), Fr(1)]
    if shape == 'R2':
        A_, B_, C_ = prm
        for n_ in range(1, N):
            Bs.append(((A_ * n_ * n_ + A_ * n_ + B_) * Bs[-1]
                       - C_ * n_ * n_ * Bs[-2]) / Fr((n_ + 1) ** 2))
    else:
        A_, B_, C_, D_ = prm
        for n_ in range(1, N):
            Bs.append(((2 * n_ + 1) * (A_ * n_ * n_ + A_ * n_ + B_) * Bs[-1]
                       - n_ * (C_ * n_ * n_ + D_) * Bs[-2])
                      / Fr((n_ + 1) ** 3))
    for wtry in (1, 2, 3, 4):
        d_ = 1
        ok = True
        for n_ in range(1, N):
            d_ = lcm(d_, n_)
            if (Bs[n_] * d_ ** wtry).denominator != 1:
                ok = False
                break
        if ok:
            return wtry, [str(x) for x in Bs[:6]]
    return None, [str(x) for x in Bs[:6]]

# ---------------------------------------------------------------- twists
def twist_t(ser):
    """t~(q) = -t(-q): index k -> (-1)^{k+1}."""
    return [(-x if i % 2 == 0 else x) for i, x in enumerate(ser)]

def twist_f(ser):
    return [(x if i % 2 == 0 else -x) for i, x in enumerate(ser)]

# ---------------------------------------------------------------- levels
LEVELS = {
    2: [1, 2], 3: [1, 3], 4: [1, 2, 4], 5: [1, 5], 6: [1, 2, 3, 6],
    7: [1, 7], 8: [1, 2, 4, 8], 9: [1, 3, 9], 10: [1, 2, 5, 10],
    12: [1, 2, 3, 4, 6, 12], 13: [1, 13], 16: [1, 2, 4, 8, 16],
    18: [1, 2, 3, 6, 9, 18], 20: [1, 2, 4, 5, 10, 20], 25: [1, 5, 25],
}

CONTROLS = {
    'gamma':  ({1: 12, 6: 12, 2: -12, 3: -12}, {2: 7, 3: 7, 1: -5, 6: -5}),
    'A':      ({1: 3, 6: 9, 2: -3, 3: -9},     {2: 1, 3: 6, 1: -2, 6: -3}),
    'zeta':   ({1: 6, 9: 6, 3: -12},           {3: 10, 1: -3, 9: -3}),
    'delta':  ({1: 4, 4: 4, 6: 16, 2: -16, 3: -4, 12: -4},
               {2: 12, 3: 1, 12: 1, 1: -3, 4: -3, 6: -4}),
    'alpha':  ({1: 6, 3: 6, 4: 6, 12: 6, 2: -12, 6: -12},
               {2: 10, 6: 10, 1: -4, 3: -4, 4: -4, 12: -4}),
    'eps':    ({1: 8, 8: 8, 2: -8, 4: -8},     {2: 6, 4: 6, 1: -4, 8: -4}),
    'C':      ({1: 4, 6: 8, 2: -8, 3: -4},     {2: 6, 3: 1, 1: -3, 6: -2}),
    'E':      ({1: 4, 4: 2, 8: 4, 2: -10},     {2: 10, 1: -4, 4: -4}),
    'F':      ({1: 5, 3: 1, 4: 5, 6: 2, 12: 1, 2: -14},
               {2: 15, 3: 2, 12: 2, 1: -6, 4: -6, 6: -5}),
    'eta':    ({1: 6, 4: 6, 10: 18, 2: -18, 5: -6, 20: -6},
               {2: 15, 5: 1, 20: 1, 1: -5, 4: -5, 10: -3}),
}

def main():
    t0 = time.time()
    known_fp = {}
    for nm in list(R2) + list(R3):
        known_fp[fingerprint(known_seq(nm, 14))] = nm

    # ---------------- controls ----------------
    print('=== CONTROLS (exact, order %d) ===' % QE, flush=True)
    nfail = 0
    for nm, (te, fe) in CONTROLS.items():
        T = [0] + eprod_i(te, QE - 1)
        Fq = eprod_i(fe, QE)
        a = compose_i(Fq, revert_i(T, QE), QE)
        shp, prm = shape_match_exact(a)
        exp = R2.get(nm) or R3.get(nm)
        ok = prm is not None and tuple(prm) == tuple(exp)
        print('  %-7s -> %s %s %s' % (nm, shp, prm,
              'MATCH' if ok else '*** expected %s' % (exp,)), flush=True)
        nfail += 0 if ok else 1
    if nfail:
        print('CONTROLS FAILED (%d) -- aborting.' % nfail)
        sys.exit(1)
    print('all 10 controls MATCH (%.0fs)\n' % (time.time() - t0), flush=True)

    # ---------------- sweep ----------------
    print('=== SWEEP mod %d, order %d ===' % (P, QS), flush=True)
    seen = set()
    hits = []
    stats = {}
    for N, divs in sorted(LEVELS.items()):
        cap = 24 if len(divs) <= 3 else 8
        tc = enum_evecs(divs, 0, 24, cap, 26, 12)
        fb = []
        for w in (1, 2):
            for ev in enum_evecs(divs, 2 * w, 0, cap, 26, 24):
                fb.append(('eta%s' % (sorted(ev.items()),), w,
                           eprod_p(ev, QS), ('eta', ev)))
        for nm, w, ser in eis_bank_fr(divs, QS):
            fb.append((nm, w, fr_to_p(ser), ('eis', nm)))
        npairs = nhit = 0
        for te in tc:
            Tp_ = np.concatenate([[0], eprod_p(te, QS - 1)])
            for (fn, w, Fp_, fref) in fb:
                for tw in (1, -1):
                    npairs += 1
                    if tw == 1:
                        Ts, Fs = Tp_, Fp_
                    else:
                        Ts = np.array([int(x) if i % 2 else (-int(x)) % P
                                       for i, x in enumerate(Tp_)],
                                      dtype=np.int64)
                        Fs = np.array([int(x) if i % 2 == 0 else (-int(x)) % P
                                       for i, x in enumerate(Fp_)],
                                      dtype=np.int64)
                    q = revert_p(Ts, QS)
                    a = compose_p(Fs, q, QS)
                    dim = fit_3term_p(a)
                    if dim == 0:
                        continue
                    fp = fingerprint(a)
                    if fp in seen:
                        continue
                    seen.add(fp)
                    nhit += 1
                    hits.append({'level': N, 't': te, 'fname': fn,
                                 'fref': fref, 'w': w, 'twist': tw,
                                 'dim': dim, 'known': known_fp.get(fp)})
        stats[N] = (npairs, nhit)
        print('  level %-3d: %5d pairs, %3d new distinct hits  (%.0fs)'
              % (N, npairs, nhit, time.time() - t0), flush=True)

    # ---------------- exact classification ----------------
    print('\n=== CLASSIFY (exact, order %d) ===' % QE, flush=True)
    catalog = {'rediscovered': [], 'new3term': [], 'other': []}
    for h in hits:
        T = [0] + eprod_i(h['t'], QE - 1)
        kind, ref = h['fref']
        if kind == 'eta':
            Fq = [Fr(x) for x in eprod_i(ref, QE)]
        else:
            Fq = None
            for nm, w, ser in eis_bank_fr(LEVELS[h['level']], QE):
                if nm == ref:
                    Fq = ser
        if Fq is None:
            continue
        if h['twist'] == -1:
            T = twist_t(T)
            Fq = twist_f(Fq)
        Ti = [Fr(x) for x in T]
        # exact reversion/composition over Fractions
        # (reuse integer routines by scaling? just do Fractions -- few hits)
        def mul_f(a, b, n):
            out = [Fr(0)] * n
            for i, ai in enumerate(a[:n]):
                if ai:
                    for j, bj in enumerate(b[:n - i]):
                        if bj:
                            out[i + j] += ai * bj
            return out
        def inv_f(a, n):
            out = [Fr(0)] * n
            out[0] = 1 / a[0]
            for k in range(1, n):
                s = Fr(0)
                for j in range(1, min(k, len(a) - 1) + 1):
                    s += a[j] * out[k - j]
                out[k] = -out[0] * s
            return out
        def compose_f(a, b, n):
            out = [Fr(0)] * n
            for c in reversed(a[:n]):
                out = mul_f(out, b, n)
                out[0] += c
            return out
        def revert_f(Tser, n):
            g = [Fr(0), Fr(1)] + [Fr(0)] * (n - 2)
            Tp = [(i + 1) * Tser[i + 1] for i in range(len(Tser) - 1)]
            m = 2
            while m < n:
                m = min(2 * m, n)
                Tg = compose_f(Tser, g, m)
                Tg[1] -= 1
                corr = mul_f(Tg, inv_f(compose_f(Tp, g, m), m), m)
                g = [g[i] - (corr[i] if i < len(corr) else Fr(0))
                     for i in range(m)] + [Fr(0)] * (n - m)
            return g[:n]
        a = compose_f(Fq, revert_f(Ti, QE), QE)
        if any(x.denominator != 1 for x in a):
            catalog['other'].append({**h, 'note': 'non-integral a_n',
                                     'fref': str(h['fref'])})
            continue
        a = [int(x) for x in a]
        shp, prm = shape_match_exact(a)
        e = {**h, 'fref': str(h['fref']), 'shape': shp,
             'params': prm, 'a_start': a[:7]}
        if h['known']:
            catalog['rediscovered'].append(e)
        elif shp is not None:
            allknown = list(R2.values()) + list(R3.values())
            if tuple(prm) in [tuple(v) for v in allknown]:
                e['known'] = 'shape'
                catalog['rediscovered'].append(e)
            else:
                cw, bstart = companion_profile(shp, prm)
                e['companion_w'] = cw
                e['B_start'] = bstart
                catalog['new3term'].append(e)
        else:
            catalog['other'].append(e)

    print('rediscovered: %d' % len(catalog['rediscovered']))
    for e in catalog['rediscovered']:
        print('  known=%s level=%d twist=%d %s%s' % (e['known'], e['level'],
              e['twist'], e['shape'], e['params']))
    print('NEW 3-term integral pairs: %d' % len(catalog['new3term']))
    for e in catalog['new3term']:
        print('  NEW level=%d twist=%d %s%s a=%s comp_w=%s\n       t=%s f=%s'
              % (e['level'], e['twist'], e['shape'], e['params'],
                 e['a_start'], e['companion_w'], e['t'], e['fname']))
    print('other (degenerate/rational/no-3-term-shape): %d'
          % len(catalog['other']))
    out = {'stats': {str(k): v for k, v in stats.items()},
           'rediscovered': [{k: str(v) for k, v in e.items()}
                            for e in catalog['rediscovered']],
           'new3term': [{k: str(v) for k, v in e.items()}
                        for e in catalog['new3term']],
           'other': [{k: str(v) for k, v in e.items()}
                     for e in catalog['other']]}
    with open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/'
              'eps55_catalog.json', 'w') as fh:
        json.dump(out, fh, indent=1)
    print('\nsaved eps55_catalog.json  (%.0fs total)' % (time.time() - t0))

if __name__ == '__main__':
    main()
