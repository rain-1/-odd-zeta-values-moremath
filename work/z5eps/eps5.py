"""eps5.py -- point pipeline on the full 9-letter deformation space.

L1 = a*X + b*Y + alpha.U   (a,b: sym null coords; alpha in Q^3 antisym, free)
L2 = g.h2sym + beta.w2     L3 = y.h3sym + gamma-antisym enters later, etc.

Stage solves (columns | unknowns):
 E2: [M2 | rows]                    (g6, s2,u2,v2)      RHS: -1/2 (S1^2 + A1^2)
 E3: [M3 | C_beta(alpha) | rows]    (y6, beta3, t3,s3,v3)
 E4: [M4 | C_gamma(alpha) | rows]   (z6, gamma3, u4,s4,v4)
 E5: [M5 | C_delta(alpha) | rows]   (w6, delta3, t5,u5,s5)
"""
import sys, pickle
from itertools import product as iproduct

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import core
from eps2 import rref_solve, ratrec, rr

BASE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/'


class Pipe:
    def __init__(self, p):
        d = pickle.load(open(BASE + 'eps4_tensors_%d.pkl' % p, 'rb'))
        self.p, self.NMAX, self.TN = d['p'], d['NMAX'], d['TN']
        self.nr = self.NMAX + 1
        lad = core.ladders()
        fm = lambda fr: fr.numerator % p * pow(fr.denominator % p, p - 2, p) % p
        self.Q = [fm(lad['Q'][n]) for n in range(self.nr)]
        self.Ph = [fm(lad['Ph'][n]) for n in range(self.nr)]
        self.P = [fm(lad['P'][n]) for n in range(self.nr)]
        self.inv = lambda x: pow(x, p - 2, p)

    # ---- contraction helpers ----
    def mom(self, vecs):
        """SigmaT prod_j (vecs[j].V)  -> n-vector"""
        p, TN = self.p, self.TN
        out = [0] * self.nr
        for idx in iproduct(range(5), repeat=len(vecs)):
            c = 1
            for j, i in enumerate(idx):
                c = c * vecs[j][i] % p
            if c == 0: continue
            key = ('V', tuple(sorted(idx)))
            tv = TN[key]
            for n in range(self.nr):
                out[n] = (out[n] + c * tv[n]) % p
        return out

    def momH(self, vecs, r, coef9):
        p, TN = self.p, self.TN
        out = [0] * self.nr
        for a in range(9):
            ca = coef9[a] % p
            if ca == 0: continue
            if not vecs:
                tv = TN[('VH', (), r, a)]
                for n in range(self.nr):
                    out[n] = (out[n] + ca * tv[n]) % p
                continue
            for idx in iproduct(range(5), repeat=len(vecs)):
                c = ca
                for j, i in enumerate(idx):
                    c = c * vecs[j][i] % p
                if c == 0: continue
                tv = TN[('VH', tuple(sorted(idx)), r, a)]
                for n in range(self.nr):
                    out[n] = (out[n] + c * tv[n]) % p
        return out

    def momHH(self, vecs, cA9, r2, cB9, r3=None):
        """r3 None: SigmaT (prod V)(cA.h2)(cB.h2);  else (cA.h2)(cB.h3), vecs=[]"""
        p, TN = self.p, self.TN
        out = [0] * self.nr
        for a in range(9):
            ca = cA9[a] % p
            if ca == 0: continue
            for b in range(9):
                cb = cB9[b] % p
                if cb == 0: continue
                cab = ca * cb % p
                if r3 is not None:
                    tv = TN[('VHH', (), 2, a, 3, b)]
                    for n in range(self.nr):
                        out[n] = (out[n] + cab * tv[n]) % p
                    continue
                aa, bb = min(a, b), max(a, b)
                if not vecs:
                    tv = TN[('VHH', (), 2, aa, 2, bb)]
                    for n in range(self.nr):
                        out[n] = (out[n] + cab * tv[n]) % p
                else:
                    for idx in iproduct(range(5), repeat=len(vecs)):
                        c = cab
                        for j, i in enumerate(idx):
                            c = c * vecs[j][i] % p
                        if c == 0: continue
                        tv = TN[('VHH', tuple(sorted(idx)), 2, aa, 2, bb)]
                        for n in range(self.nr):
                            out[n] = (out[n] + c * tv[n]) % p
        return out

    def stage_cols(self, r, alpha):
        """columns: M_r sym classes (6) + antisym-product columns (3) + rows (3)"""
        p = self.p
        cols = []
        for c in range(6):
            e9 = [0] * 9; e9[c] = 1
            cols.append(self.momH([], r, e9))
        a1c = [0, 0] + list(alpha)
        for j in range(3):
            e9 = [0] * 9; e9[6 + j] = 1
            cols.append(self.momH([a1c], r, e9))   # SigmaT A1 * w_r[j]
        return cols

    def solve(self, A_cols, rhs):
        p = self.p
        A = [[col[n] for col in A_cols] for n in range(self.nr)]
        return rref_solve(A, rhs, p)

    def run_point(self, a, b, alpha, verbose=True, rows_at=('E2', 'E3', 'E4', 'E5')):
        p = self.p
        i2, i6, i24, i120 = self.inv(2), self.inv(6), self.inv(24), self.inv(120)
        s1c = [a, b, 0, 0, 0]
        a1c = [0, 0] + list(alpha)
        R = {}
        rowscols = [[(-q) % p for q in self.Ph],
                    [(-q) % p for q in self.Q],
                    [(-q) % p for q in self.P]]

        # ---------------- E2 ----------------
        cols = []
        for c in range(6):
            e9 = [0] * 9; e9[c] = 1
            cols.append(self.momH([], 2, e9))
        cols += rowscols if 'E2' in rows_at else []
        t_s1s1 = self.mom([s1c, s1c]); t_a1a1 = self.mom([a1c, a1c])
        rhs = [(-i2 * (t_s1s1[n] + t_a1a1[n])) % p for n in range(self.nr)]
        ok, x, null, rk = self.solve(cols, rhs)
        if verbose: print('  E2: ok=%s rank=%d/%d null=%d' % (ok, rk, len(cols), len(null) if ok else -1))
        if not ok: R['fail'] = 'E2'; return R
        g = x[:6]; R['g'] = g; R['s2u2v2'] = x[6:9] if 'E2' in rows_at else (0, 0, 0)
        if verbose and 'E2' in rows_at:
            print('  E2: (u2,s2,v2)=(%s,%s,%s)  g=%s' %
                  (rr(x[6], p), rr(x[7], p), rr(x[8], p), [rr(v, p) for v in g]))
        g9 = list(g) + [0, 0, 0]

        # ---------------- E3 ----------------
        cols = self.stage_cols(3, alpha) + rowscols
        t_s1s2 = self.momH([s1c], 2, g9)
        t_s13 = self.mom([s1c] * 3)
        t_s1a12 = self.mom([s1c, a1c, a1c])
        rhs = [(-(t_s1s2[n] + i6 * t_s13[n] + i2 * t_s1a12[n])) % p
               for n in range(self.nr)]
        ok, x, null3, rk = self.solve(cols, rhs)
        if verbose: print('  E3: ok=%s rank=%d/12 null=%d' % (ok, rk, len(null3) if ok else -1))
        if not ok: R['fail'] = 'E3'; return R
        y, beta = x[:6], x[6:9]
        t3, s3, v3 = x[9], x[10], x[11]
        R.update(y=y, beta=beta, t3=t3, s3=s3, v3=v3, null3=len(null3))
        if verbose:
            print('  E3: t3=%s s3=%s v3=%s' % (rr(t3, p), rr(s3, p), rr(v3, p)))
            print('  E3: y=%s beta=%s' % ([rr(v, p) for v in y], [rr(v, p) for v in beta]))
            if null3:
                print('  E3 null dirs (y|beta|t3 s3 v3):')
                for v in null3: print('     ', [rr(u, p) for u in v])
        y9 = list(y) + [0, 0, 0]
        b9 = [0] * 6 + list(beta)

        # ---------------- E4 ----------------
        cols = self.stage_cols(4, alpha) + rowscols
        t_s1s3 = self.momH([s1c], 3, y9)
        t_s2s2 = self.momHH([], g9, 2, g9)
        t_a2a2 = self.momHH([], b9, 2, b9)
        t_s12s2 = self.momH([s1c, s1c], 2, g9)
        t_a12s2 = self.momH([a1c, a1c], 2, g9)
        t_s1a1a2 = self.momH([s1c, a1c], 2, b9)
        t_s14 = self.mom([s1c] * 4)
        t_s12a12 = self.mom([s1c, s1c, a1c, a1c])
        t_a14 = self.mom([a1c] * 4)
        rhs = [(-(t_s1s3[n] + i2 * (t_s2s2[n] + t_a2a2[n])
                  + i2 * (t_s12s2[n] + t_a12s2[n]) + t_s1a1a2[n]
                  + i24 * (t_s14[n] + 6 * t_s12a12[n] + t_a14[n]))) % p
               for n in range(self.nr)]
        ok, x, null4, rk = self.solve(cols, rhs)
        if verbose: print('  E4: ok=%s rank=%d/12 null=%d' % (ok, rk, len(null4) if ok else -1))
        if not ok: R['fail'] = 'E4'; return R
        z, gam = x[:6], x[6:9]
        u4, s4, v4 = x[9], x[10], x[11]
        R.update(z=z, gamma=gam, u4=u4, s4=s4, v4=v4, null4=len(null4))
        if verbose:
            print('  E4: u4=%s s4=%s v4=%s' % (rr(u4, p), rr(s4, p), rr(v4, p)))
        z9 = list(z) + [0, 0, 0]
        c9 = [0] * 6 + list(gam)

        # ---------------- E5 ----------------
        cols = self.stage_cols(5, alpha) + rowscols
        t_s1s4 = self.momH([s1c], 4, z9)
        t_s2s3 = self.momHH([], g9, 2, y9, 3)
        t_a2a3 = self.momHH([], b9, 2, c9, 3)
        t_s12s3 = self.momH([s1c, s1c], 3, y9)
        t_a12s3 = self.momH([a1c, a1c], 3, y9)
        t_s1a1a3 = self.momH([s1c, a1c], 3, c9)
        t_s1s2s2 = self.momHH([s1c], g9, 2, g9)
        t_s1a2a2 = self.momHH([s1c], b9, 2, b9)
        t_a1s2a2 = self.momHH([a1c], g9, 2, b9)
        t_s13s2 = self.momH([s1c] * 3, 2, g9)
        t_s1a12s2 = self.momH([s1c, a1c, a1c], 2, g9)
        t_s12a1a2 = self.momH([s1c, s1c, a1c], 2, b9)
        t_a13a2 = self.momH([a1c] * 3, 2, b9)
        t_s15 = self.mom([s1c] * 5)
        t_s13a12 = self.mom([s1c] * 3 + [a1c] * 2)
        t_s1a14 = self.mom([s1c] + [a1c] * 4)
        rhs = []
        for n in range(self.nr):
            v = (t_s1s4[n] + t_s2s3[n] + t_a2a3[n]
                 + i2 * (t_s12s3[n] + t_a12s3[n]) + t_s1a1a3[n]
                 + i2 * (t_s1s2s2[n] + t_s1a2a2[n]) + t_a1s2a2[n]
                 + i6 * (t_s13s2[n] + 3 * t_s1a12s2[n] + 3 * t_s12a1a2[n] + t_a13a2[n])
                 + i120 * (t_s15[n] + 10 * t_s13a12[n] + 5 * t_s1a14[n]))
            rhs.append((-v) % p)
        # E5 rows order: t5 (P), u5 (Ph), s5 (Q): reuse rowscols = (Ph,Q,P)
        ok, x, null5, rk = self.solve(cols, rhs)
        if verbose: print('  E5: ok=%s rank=%d/12 null=%d' % (ok, rk, len(null5) if ok else -1))
        if not ok: R['fail'] = 'E5'; return R
        w, dlt = x[:6], x[6:9]
        u5, s5, t5 = x[9], x[10], x[11]
        R.update(w=w, delta=dlt, t5=t5, u5=u5, s5=s5, null5=len(null5))
        if verbose:
            print('  E5: t5=%s u5=%s s5=%s' % (rr(t5, p), rr(u5, p), rr(s5, p)))
            print('  E5: w=%s delta=%s' % ([rr(v, p) for v in w], [rr(v, p) for v in dlt]))
        return R


if __name__ == '__main__':
    p = 2147483647
    pi = Pipe(p)
    print('== structural checks ==')
    # residual of SigmaT U_i U_j against [M2 | rows]
    cols = []
    for c in range(6):
        e9 = [0] * 9; e9[c] = 1
        cols.append(pi.momH([], 2, e9))
    cols += [[(-q) % p for q in pi.Ph], [(-q) % p for q in pi.Q],
             [(-q) % p for q in pi.P]]
    A = [[col[n] for col in cols] for n in range(pi.nr)]
    ok, x, null, rk = rref_solve(A, [0] * pi.nr, p)
    print('rank [M2|rows] =', rk, 'of 9')

    print()
    print('== point: pure Psi  (a,b)=(0,0), alpha=(-3,1,2) ==')
    pi.run_point(0, 0, (-3, 1, 2))
    print()
    print('== point: pure U1 ==')
    pi.run_point(0, 0, (1, 0, 0))
    print()
    print('== point: pure U2 ==')
    pi.run_point(0, 0, (0, 1, 0))
    print()
    print('== point: pure U3 ==')
    pi.run_point(0, 0, (0, 0, 1))
    print()
    print('== point: random alpha (17,5,-9) ==')
    pi.run_point(0, 0, (17, 5, -9))
    print()
    print('== point: mixed (a,b)=(1,1), alpha=(-3,1,2) ==')
    pi.run_point(1, 1, (-3, 1, 2))
