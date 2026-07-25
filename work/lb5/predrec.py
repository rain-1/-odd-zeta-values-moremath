"""SUPERSEDED -- see PHASE2_CERTS.md section 8.5.  Kept for the machinery only.

This script sums e_m*T over k,l <= n, which is NOT the sequence the rank-1
telescopers annihilate: for m in {c0, beta} the summand has a pole at k = n, and
for every m the cells k or l in {n+1,n+2,n+3} contribute a finite non-zero amount
(pole order <= 2 against T's double zero).  A valid modular prediction needs the
box [0,K]^2, K >= n+3, with the cell values regularised at n = n0 + eps, i.e.
truncated Laurent arithmetic mod p.  The polynomial-evaluation and nullspace
machinery below is correct and reusable for that.

Original header:
Independent modular prediction of the rank-1 telescoper orders.

For each letter coefficient e_m of  E(v)/T = c0 + alpha A1(k) + ... + eps A1(l),
compute   S_m(n) = sum_{k,l=0}^{n} e_m(n,k,l) T(n,k,l)   mod p   for n = 0..N,
then search for a recurrence  sum_{j<=r} p_j(n) S(n+j) = 0,  deg p_j <= d.

The minimal (r,d) found is the order/degree the rank-1 CreativeTelescoping of
certU.wl must return -- an independent check on the RISC computation, and an
early estimate of ord(LCLM) <= sum_m ord(M_m) for the order budget of PHASE2_CERTS
section 9.5.

Usage:  python3 predrec.py [NMAX] [labels...]
"""
import sys, numpy as np

P = 33554393
DIR = '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/'


def load_coefs(path):
    """label -> {'num': dense array [dk][dl][dn], 'den': ...}"""
    blocks = {}
    cur = None
    rows = []
    with open(path) as f:
        for line in f:
            if line.startswith('#'):
                if cur is not None:
                    blocks[cur] = rows
                _, lab, tag, _ = line.split()
                cur = (lab, tag)
                rows = []
            else:
                a, b, c, v = line.split()
                rows.append((int(a), int(b), int(c), int(v)))
    if cur is not None:
        blocks[cur] = rows
    out = {}
    for (lab, tag), rows in blocks.items():
        Dn = max(r[0] for r in rows)
        Dk = max(r[1] for r in rows)
        Dl = max(r[2] for r in rows)
        A = np.zeros((Dk + 1, Dl + 1, Dn + 1), dtype=np.int64)
        for dn, dk, dl, v in rows:
            A[dk, dl, dn] = v % P
        out.setdefault(lab, {})[tag] = A
    return out


def modpow_arr(a, e, p=P):
    """vectorised modular exponentiation"""
    r = np.ones_like(a)
    b = a % p
    while e:
        if e & 1:
            r = (r * b) % p
        b = (b * b) % p
        e >>= 1
    return r


def eval_grid(A, n, Kg, Lg):
    """A[dk][dl][dn] -> value on the (n+1)x(n+1) grid, mod P."""
    Dk, Dl, Dn = A.shape[0] - 1, A.shape[1] - 1, A.shape[2] - 1
    npow = np.empty(Dn + 1, dtype=np.int64)
    npow[0] = 1
    for i in range(1, Dn + 1):
        npow[i] = (npow[i - 1] * n) % P
    # C[dk][dl] = sum_dn A[dk,dl,dn] n^dn
    C = (A.reshape(-1, Dn + 1) @ npow) % P
    C = C.reshape(Dk + 1, Dl + 1)
    # B[dk][l] = sum_dl C[dk,dl] l^dl   (Horner in l, 1-D)
    B = np.zeros((Dk + 1, n + 1), dtype=np.int64)
    lv = Lg.reshape(-1)
    for dk in range(Dk + 1):
        acc = np.zeros(n + 1, dtype=np.int64)
        for dl in range(Dl, -1, -1):
            acc = (acc * lv + C[dk, dl]) % P
        B[dk] = acc
    # val[k][l] = sum_dk B[dk][l] k^dk    (Horner in k, 2-D)
    val = np.zeros((n + 1, n + 1), dtype=np.int64)
    kv = Kg
    for dk in range(Dk, -1, -1):
        val = (val * kv + B[dk][None, :]) % P
    return val


def make_T(NMAX):
    f = [1] * (4 * NMAX + 5)
    for i in range(1, len(f)):
        f[i] = f[i - 1] * i % P
    fi = [1] * len(f)
    fi[-1] = pow(f[-1], P - 2, P)
    for i in range(len(f) - 1, 0, -1):
        fi[i - 1] = fi[i] * i % P
    fa = np.array(f, dtype=np.int64)
    fia = np.array(fi, dtype=np.int64)

    def T(n):
        k = np.arange(n + 1, dtype=np.int64).reshape(-1, 1)
        l = np.arange(n + 1, dtype=np.int64).reshape(1, -1)
        c = lambda a, b: fa[a] * fia[b] % P * fia[a - b] % P
        t = c(n + k, n) * (c(n, k) ** 2 % P) % P
        t = t * c(n + l, n) % P * (c(n, l) ** 2 % P) % P
        t = t * c(n + k + l, n) % P
        return t
    return T


def nullspace_mod(M, p=P):
    """row-reduce M (rows=equations, cols=unknowns) mod p, return nullity."""
    M = M % p
    rows, cols = M.shape
    r = 0
    piv = []
    for c in range(cols):
        pr = None
        for i in range(r, rows):
            if M[i, c] % p:
                pr = i
                break
        if pr is None:
            continue
        M[[r, pr]] = M[[pr, r]]
        inv = pow(int(M[r, c]), p - 2, p)
        M[r] = M[r] * inv % p
        col = M[:, c].copy()
        col[r] = 0
        M = (M - np.outer(col, M[r])) % p
        piv.append(c)
        r += 1
        if r == rows:
            break
    return cols - r


def main():
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    want = sys.argv[2:] or ['alpha', 'beta', 'gamma', 'delta', 'eps', 'c0']
    co = load_coefs(DIR + 'Ecoef.txt')
    Tf = make_T(NMAX)
    for lab in want:
        num, den = co[lab]['num'], co[lab]['den']
        S = []
        badden = 0
        for n in range(NMAX + 1):
            Kg = np.arange(n + 1, dtype=np.int64).reshape(-1, 1)
            Lg = np.arange(n + 1, dtype=np.int64).reshape(1, -1)
            u = eval_grid(num, n, Kg, Lg)
            v = eval_grid(den, n, Kg, Lg)
            badden += int(np.count_nonzero(v == 0))
            vi = modpow_arr(np.where(v == 0, 1, v), P - 2)
            e = u * vi % P
            S.append(int((e * Tf(n) % P).sum() % P))
        S = np.array(S, dtype=np.int64)
        print('%-6s computed n=0..%d  (den==0 cells: %d)  S[0..4]=%s'
              % (lab, NMAX, badden, S[:5].tolist()), flush=True)
        found = None
        for r in range(1, 13):
            for d in range(0, 41):
                unk = (r + 1) * (d + 1)
                neq = NMAX + 1 - r
                if neq < unk + 8:
                    continue
                rowsl = []
                for n in range(neq):
                    row = []
                    npw = 1
                    pw = [1] * (d + 1)
                    for i in range(1, d + 1):
                        pw[i] = pw[i - 1] * n % P
                    for j in range(r + 1):
                        for i in range(d + 1):
                            row.append(pw[i] * int(S[n + j]) % P)
                    rowsl.append(row)
                M = np.array(rowsl, dtype=np.int64)
                nul = nullspace_mod(M)
                if nul > 0:
                    found = (r, d, nul)
                    break
            if found:
                break
        print('   -> minimal recurrence %s' % (str(found) if found
              else 'NONE with r<=12, d<=40 in range'), flush=True)


if __name__ == '__main__':
    main()
