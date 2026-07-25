"""Shared Kummer / pattern helpers for the (GAP-DESC) node (task P1i)."""

def car(x, y, p, eps=0):
    """number of carries in the base-p addition x+y+eps."""
    c = eps; n = 0
    while x or y or c:
        d = x % p + y % p + c
        c = 1 if d >= p else 0
        n += c
        x //= p; y //= p
    return n

def vpC(x, y, p):
    """v_p C(x+y, x) = carries in x+y."""
    return car(x, y, p)

def vT(n, k, l, p):
    """v_p T(n,k,l) by Kummer."""
    return (car(n, k, p) + 2 * car(k, n - k, p) + car(n, l, p)
            + 2 * car(l, n - l, p) + car(n, k + l, p))

def vp(x, p):
    if x == 0: return 10**9
    v = 0
    while x % p == 0:
        x //= p; v += 1
    return v

def pattern(n, k, l, p, M):
    """(alpha,gamma,kappa,theta) at level n with P = p^M (n < p^M)."""
    P = p ** M
    al = 1 if n + k >= P else 0
    ga = 1 if n + l >= P else 0
    eps = (k + l) // P
    ka = 1 if n + k + l >= (eps + 1) * P else 0
    th = eps + 1 if ka else 1
    return al, ga, ka, th

def Jcap(s):
    """depth cap J(pi) = 0 for the trivial pattern, else 1+min(s,2)."""
    return 0 if s == 0 else 1 + min(s, 2)

def logp(n, p):
    L = 0
    q = n
    while q >= p:
        q //= p; L += 1
    return L
