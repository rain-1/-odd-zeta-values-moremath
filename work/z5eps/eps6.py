"""eps6.py -- corrected point pipeline (stage E_m: sym letters weight m,
antisym unknown A_{m-1} couples through A1*A_{m-1}, i.e. weight-(m-1) letters).

At the pure-antisymmetric point S1 = 0 the E3 stage is HOMOGENEOUS; its kernel
scale t is a genuine deformation parameter and flows into E4 (quadratically,
through A2 = t*beta_hat) and E5.  Handled explicitly.
"""
import sys, pickle

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import core
from eps2 import rref_solve, ratrec, rr
from eps5 import Pipe as Pipe0


class Pipe(Pipe0):
    def stage_cols2(self, r_sym, r_anti, alpha):
        cols = []
        for c in range(6):
            e9 = [0] * 9; e9[c] = 1
            cols.append(self.momH([], r_sym, e9))
        a1c = [0, 0] + list(alpha)
        for j in range(3):
            e9 = [0] * 9; e9[6 + j] = 1
            cols.append(self.momH([a1c], r_anti, e9))
        return cols

    def rowcols(self):
        p = self.p
        return [[(-q) % p for q in self.Ph], [(-q) % p for q in self.Q],
                [(-q) % p for q in self.P]]

    def E2(self, s1c, a1c, verbose=True):
        p = self.p; i2 = self.inv(2)
        cols = []
        for c in range(6):
            e9 = [0] * 9; e9[c] = 1
            cols.append(self.momH([], 2, e9))
        cols += self.rowcols()
        t1 = self.mom([s1c, s1c]); t2 = self.mom([a1c, a1c])
        rhs = [(-i2 * (t1[n] + t2[n])) % p for n in range(self.nr)]
        ok, x, null, rk = self.solve(cols, rhs)
        if verbose: print('  E2: ok=%s rank=%d/9 null=%d' % (ok, rk, len(null) if ok else -1))
        if not ok: return None
        if verbose:
            print('  E2: g=%s  (u2,s2,v2)=(%s,%s,%s)' %
                  ([rr(v, p) for v in x[:6]], rr(x[6], p), rr(x[7], p), rr(x[8], p)))
        return x

    def E3(self, s1c, a1c, g9, verbose=True):
        p = self.p; i2, i6 = self.inv(2), self.inv(6)
        alpha = a1c[2:]
        cols = self.stage_cols2(3, 2, alpha) + self.rowcols()
        t_s1s2 = self.momH([s1c], 2, g9)
        t_s13 = self.mom([s1c] * 3)
        t_s1a12 = self.mom([s1c, a1c, a1c])
        rhs = [(-(t_s1s2[n] + i6 * t_s13[n] + i2 * t_s1a12[n])) % p
               for n in range(self.nr)]
        ok, x, null, rk = self.solve(cols, rhs)
        if verbose:
            print('  E3: ok=%s rank=%d/12 null=%d' % (ok, rk, len(null) if ok else -1))
            if ok:
                print('  E3: x0: y=%s beta=%s (t3,s3,v3)=(%s,%s,%s)' %
                      ([rr(v, p) for v in x[:6]], [rr(v, p) for v in x[6:9]],
                       rr(x[9], p), rr(x[10], p), rr(x[11], p)))
                for v in null:
                    print('  E3 null: y=%s beta=%s (t3,s3,v3)=(%s,%s,%s)' %
                          ([rr(u, p) for u in v[:6]], [rr(u, p) for u in v[6:9]],
                           rr(v[9], p), rr(v[10], p), rr(v[11], p)))
        if not ok: return None, None
        return x, null

    def E4(self, s1c, a1c, g9, y9, b9, verbose=True, solveit=True):
        p = self.p
        i2, i24 = self.inv(2), self.inv(24)
        alpha = a1c[2:]
        cols = self.stage_cols2(4, 3, alpha) + self.rowcols()
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
        if not solveit:
            return cols, rhs
        ok, x, null, rk = self.solve(cols, rhs)
        if verbose:
            print('  E4: ok=%s rank=%d/12 null=%d' % (ok, rk, len(null) if ok else -1))
            if ok:
                print('  E4: z=%s gamma=%s (u4,s4,v4)=(%s,%s,%s)' %
                      ([rr(v, p) for v in x[:6]], [rr(v, p) for v in x[6:9]],
                       rr(x[9], p), rr(x[10], p), rr(x[11], p)))
                for v in null:
                    print('  E4 null:', [rr(u, p) for u in v])
        if not ok: return None, None
        return x, null

    def E5(self, s1c, a1c, g9, y9, b9, z9, c9, verbose=True, solveit=True):
        p = self.p
        i2, i6, i120 = self.inv(2), self.inv(6), self.inv(120)
        alpha = a1c[2:]
        cols = self.stage_cols2(5, 4, alpha) + self.rowcols()
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
        if not solveit:
            return cols, rhs
        ok, x, null, rk = self.solve(cols, rhs)
        if verbose:
            print('  E5: ok=%s rank=%d/12 null=%d' % (ok, rk, len(null) if ok else -1))
            if ok:
                print('  E5: w=%s delta=%s (u5,s5,t5)=(%s,%s,%s)' %
                      ([rr(v, p) for v in x[:6]], [rr(v, p) for v in x[6:9]],
                       rr(x[9], p), rr(x[10], p), rr(x[11], p)))
        if not ok: return None, None
        return x, null


def pure_psi_flow(p, alpha=(-3, 1, 2)):
    """S1 = 0 branch: E3 homogeneous with kernel scale t.
    E4's RHS = C0 + t^2 C2; E5's similar.  Reconstruct t-dependence by sampling."""
    pi = Pipe(p)
    s1c = [0] * 5
    a1c = [0, 0] + list(alpha)
    print('== pure-antisym point alpha =', alpha, ' p =', p, '==')
    x2 = pi.E2(s1c, a1c)
    if x2 is None: return
    g9 = list(x2[:6]) + [0, 0, 0]
    x3, null3 = pi.E3(s1c, a1c, g9)
    if x3 is None: return
    # solution family: x3 + t*null3[i].  At S1=0, expect x3 = 0.
    assert all(v == 0 for v in x3), 'expected homogeneous E3 at S1=0'
    if len(null3) != 1:
        print('  E3 kernel dim =', len(null3), '-- multi-parameter flow, inspect')
    for i, ker in enumerate(null3):
        print('  --- flowing kernel direction %d ---' % i)
        # E4 at t in {1, 2}: RHS(t) = C0 + t^2 C2 (only beta enters, quadratically)
        # solve for each t and check consistency & t-dependence of solutions
        for t in (1, 2, 3):
            y9 = [t * v % p for v in ker[:6]] + [0, 0, 0]
            b9 = [0] * 6 + [t * v % p for v in ker[6:9]]
            print('   E4 at t = %d: (t3 = %s)' % (t, rr(t * ker[9] % p, p)))
            x4, null4 = pi.E4(s1c, a1c, g9, y9, b9)
            if x4 is None:
                continue
            z9 = list(x4[:6]) + [0, 0, 0]
            c9 = [0] * 6 + list(x4[6:9])
            print('   E5 at t = %d:' % t)
            pi.E5(s1c, a1c, g9, y9, b9, z9, c9)


if __name__ == '__main__':
    for p in (2147483647,):
        pure_psi_flow(p)
