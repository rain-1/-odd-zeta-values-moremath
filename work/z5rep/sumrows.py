"""STEP 2a -- the kernel K = { w : sum_{k,l} T(n,k,l) w(n,k,l) = 0 for all n }
over the bare weight-3 span, and the affine set of REPRESENTATIVES  what3 + K.

All arithmetic mod a large prime; the design matrix rows are n = 0..N.
"""
import sys, time
import numpy as np
import bare

P = 4194301


def hvals(r, xmax, p):
    """H^(r)_x mod p for x = 0..xmax"""
    out = np.zeros(xmax + 1, dtype=np.int64)
    s = 0
    for x in range(1, xmax + 1):
        s = (s + pow(pow(x, r, p), p - 2, p)) % p
        out[x] = s
    return out


def design(B, N, p=P):
    """A[n, j] = sum_{k,l=0}^{n} T(n,k,l) * B[j](n,k,l)  mod p"""
    J = len(B)
    xmax = 3 * N + 3
    Hs = {r: hvals(r, xmax, p) for r in (1, 2, 3)}
    # factorials
    fmax = 4 * N + 4
    fact = np.ones(fmax + 1, dtype=np.int64)
    for i in range(1, fmax + 1):
        fact[i] = fact[i - 1] * i % p
    inv = np.ones(fmax + 1, dtype=np.int64)
    inv[fmax] = pow(int(fact[fmax]), p - 2, p)
    for i in range(fmax, 0, -1):
        inv[i - 1] = inv[i] * i % p

    def C(a, b):
        if b < 0 or b > a:
            return 0
        return int(fact[a]) * int(inv[b]) % p * int(inv[a - b]) % p

    A = np.zeros((N + 1, J), dtype=np.int64)
    letters = sorted({L for m in B for L in m})
    lidx = {L: i for i, L in enumerate(letters)}
    monidx = [[lidx[L] for L in m] for m in B]
    fa = fact.astype(np.int64); iv = inv.astype(np.int64)
    for n in range(N + 1):
        kk = np.arange(n + 1)
        K2, L2 = np.meshgrid(kk, kk, indexing='ij')
        # T(n,k,l) = C(n+k,n) C(n,k)^2 C(n+l,n) C(n,l)^2 C(n+k+l,n)
        Cnk = fa[n + kk] * iv[n] % p * iv[kk] % p               # C(n+k,n)
        Cn_k = fa[n] * iv[kk] % p * iv[n - kk] % p              # C(n,k)
        rowk = Cnk * Cn_k % p * Cn_k % p
        Ckl = fa[n + K2 + L2] * iv[n] % p * iv[K2 + L2] % p     # C(n+k+l,n)
        Tg = rowk[:, None] * rowk[None, :] % p * Ckl % p
        Lv = []
        for L in letters:
            r, a = bare.LETTERS[L]
            cn, ck, cl = bare.ARGS[a]
            X = cn * n + ck * K2 + cl * L2
            Lv.append(Hs[r][X])
        TL = [Tg * v % p for v in Lv]
        acc = np.zeros(J, dtype=np.int64)
        for j, ids in enumerate(monidx):
            if len(ids) == 0:
                v = Tg
            elif len(ids) == 1:
                v = TL[ids[0]]
            else:
                v = TL[ids[0]] * Lv[ids[1]] % p
            acc[j] = int(v.sum() % p)
        A[n] = acc
    return A


def phat_row(N, p=P):
    """Phat_n mod p, from the exact ladder for n <= 22 and by the L_BZ
    recurrence beyond (Phat is the unique solution with those initial values)."""
    import pickle, sys as _s
    _s.path.insert(0, '../z5la')
    import zla
    from fractions import Fraction as Fr
    d = pickle.load(open('../z5la/ladder_w3.pkl', 'rb'))
    Ph = d['Phat']
    out = []
    for x in Ph[:min(len(Ph), N + 1)]:
        x = Fr(x)
        out.append(x.numerator % p * pow(x.denominator % p, p - 2, p) % p)
    n = len(out) - 1
    while len(out) <= N:
        m = len(out) - 3
        c = [ci % p for ci in zla.cc(m)]
        v = (-(c[0] * out[m] + c[1] * out[m + 1] + c[2] * out[m + 2])) % p
        out.append(v * pow(c[3], p - 2, p) % p)
    return np.array(out[:N + 1], dtype=np.int64)


def nullsp(A, p):
    import ratrec
    return ratrec.nullspace(A, p)


if __name__ == '__main__':
    sys.path.insert(0, '../z5la')
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    D = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    p = int(sys.argv[3]) if len(sys.argv) > 3 else P
    B, tops = bare.span_w3(maxdeg=D)
    t0 = time.time()
    A = design(B, N, p)
    print('design %d x %d built in %.0fs (p=%d)' % (A.shape[0], A.shape[1],
                                                    time.time() - t0, p))
    import solve
    _, piv, _ = solve.rref(A.copy(), p)
    rk = len(piv)
    print('rank of the sum-map  = %d   ->  dim K = %d  (excess rows %d)'
          % (rk, len(B) - rk, N + 1 - rk))
    b = phat_row(N, p)
    Aug = np.concatenate([A, (-b).reshape(-1, 1) % p], axis=1)
    _, piv2, _ = solve.rref(Aug.copy(), p)
    print('rank of [A | Phat]   = %d   ->  Phat IS%s in the image'
          % (len(piv2), '' if len(piv2) == rk else ' NOT'))
    # confirm what3 and vtilde are solutions
    for nm, el in (('w3hat', bare.w3hat_el()), ('vtilde', bare.vtilde_el())):
        w = np.array(bare.el_to_vec(B, el, p), dtype=np.int64)
        r = (A.astype(object) @ w.astype(object) - b) % p
        print('   sum T*%-7s - Phat : %d nonzero of %d rows'
              % (nm, int(np.count_nonzero(r)), N + 1))
    ns = nullsp(A, p)
    np.save('K_d%d_p%d.npy' % (D, p), np.array(ns, dtype=np.int64))
    np.save('A_d%d_p%d.npy' % (D, p), A)
    np.save('b_d%d_p%d.npy' % (D, p), b)
    print('K basis saved: %d vectors, dim %d' % (len(ns), len(B)))
