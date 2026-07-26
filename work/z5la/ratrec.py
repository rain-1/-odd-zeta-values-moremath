"""univariate rational-function reconstruction over F_p, plus factor detection."""
import numpy as np

def null_min_deg(vals, xs, p, maxdeg):
    """find (num, den) coprime-ish with deg <= maxdeg s.t. num(x) = f(x)*den(x)
    at all sample points.  Increases the degree budget until a solution exists."""
    M = len(xs)
    for d in range(0, maxdeg + 1):
        nc = 2 * (d + 1)
        if M < nc: break
        A = np.zeros((M, nc), dtype=np.int64)
        for t, x in enumerate(xs):
            xp = 1
            for j in range(d + 1):
                A[t, j] = xp
                A[t, d + 1 + j] = (-vals[t] * xp) % p
                xp = xp * (x % p) % p
        ns = nullspace(A, p)
        if ns:
            v = ns[0]
            num = v[:d + 1]; den = v[d + 1:]
            if any(den): return trim(num), trim(den)
    return None

def nullspace(A, p):
    A = A.copy() % p
    rows, cols = A.shape
    piv = []
    r = 0
    for c in range(cols):
        if r >= rows: break
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0: continue
        i = r + int(nz[0])
        if i != r: A[[r, i]] = A[[i, r]]
        A[r] = A[r] * pow(int(A[r, c]), p - 2, p) % p
        col = A[:, c].copy(); col[r] = 0
        nzr = np.nonzero(col)[0]
        if nzr.size:
            A[nzr] = (A[nzr] - col[nzr, None] * A[r][None, :]) % p
        piv.append(c); r += 1
    free = [c for c in range(cols) if c not in piv]
    out = []
    for fc in free:
        v = np.zeros(cols, dtype=np.int64)
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-A[i, fc]) % p
        out.append(v)
    return out

def trim(c):
    c = list(int(x) for x in c)
    while len(c) > 1 and c[-1] == 0: c.pop()
    return c

def polyval(c, x, p):
    v = 0
    for a in reversed(c): v = (v * x + a) % p
    return v

def divide_out(c, root, p):
    """synthetic division by (x - root); returns (quotient, remainder)"""
    n = len(c) - 1
    q = [0] * n
    cur = c[n]
    for i in range(n - 1, -1, -1):
        q[i] = cur
        cur = (c[i] + cur * root) % p
    return q, cur % p

def factor_mult(den, roots, p):
    """for each named root, the multiplicity in den"""
    out = {}
    cur = list(den)
    for name, rt in roots:
        m = 0
        while len(cur) > 1 and polyval(cur, rt % p, p) == 0:
            cur, rem = divide_out(cur, rt % p, p)
            m += 1
        if m: out[name] = m
    return out, cur
