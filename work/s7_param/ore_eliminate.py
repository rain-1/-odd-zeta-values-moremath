#!/usr/bin/env python3
"""Ore-algebra audit for the polarized one-parameter proof of the s7 formula.

Development input is the three machine-readable Maxima logs in /tmp.  The
script factors the Taylor operators and constructs a finite-dimensional
first-order system for A, U, U_2, V_2, D_2.  A scalar recurrence for
J=(D_2-U_2-V_2)/2 can then be extracted by a cyclic-vector calculation.
"""

from pathlib import Path
import re
import sympy as sp

n = sp.symbols("n")


def load_tag(path: str, tag: str):
    text = Path(path).read_text()
    m = re.search(rf"(?m)^{re.escape(tag)} (.*)$", text)
    if not m:
        raise RuntimeError(f"missing {tag} in {path}")
    return sp.sympify(m.group(1).replace("^", "**"), locals={"n": n})


for path, tag in [
    ("/tmp/s7-extract-u.log", "U_CHECK"),
    ("/tmp/s7-extract-v.log", "V_CHECK"),
    ("/tmp/s7-extract-diag.log", "D_CHECK"),
]:
    check = load_tag(path, tag)
    assert check == 0, (tag, check)


def sh(x, j):
    return sp.cancel(x.subs(n, n + j))


def op_mul(a, b):
    out = [sp.S.Zero] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * sh(bj, i)
    return [sp.cancel(x) for x in out]


def op_sub(a, b):
    r = max(len(a), len(b))
    aa = a + [sp.S.Zero] * (r - len(a))
    bb = b + [sp.S.Zero] * (r - len(b))
    return [sp.cancel(x - y) for x, y in zip(aa, bb)]


def right_divide(a, b):
    rem = list(a)
    q = [sp.S.Zero] * (len(a) - len(b) + 1)
    for j in range(len(q) - 1, -1, -1):
        q[j] = sp.cancel(rem[j + len(b) - 1] / sh(b[-1], j))
        mon = [sp.S.Zero] * j + [q[j]]
        rem = op_sub(rem, op_mul(mon, b))[: len(rem)]
    return q, [sp.factor(sp.cancel(x)) for x in rem]


L = [
    -3 * (n + 1) * (3 * n + 2) * (3 * n + 4),
    -(2 * n + 3) * (13 * n**2 + 39 * n + 30),
    (n + 2) ** 3,
]

U0 = load_tag("/tmp/s7-extract-u.log", "U_C0")
U1 = load_tag("/tmp/s7-extract-u.log", "U_C1")
U2 = load_tag("/tmp/s7-extract-u.log", "U_C2")
D0 = load_tag("/tmp/s7-extract-diag.log", "D_C0")
D1 = load_tag("/tmp/s7-extract-diag.log", "D_C1")
D2 = load_tag("/tmp/s7-extract-diag.log", "D_C2")

for name, op in [("U0", U0), ("D0", D0)]:
    q, rem = right_divide(op, L)
    assert all(x == 0 for x in rem), (name, rem)
    print(name, "= Q L; remainder:", rem)
    print(name, "Q:", [sp.factor(x) for x in q])

if Path("/tmp/s7-extract-v.log").exists() and "V_C2 " in Path("/tmp/s7-extract-v.log").read_text():
    V0 = load_tag("/tmp/s7-extract-v.log", "V_C0")
    V1 = load_tag("/tmp/s7-extract-v.log", "V_C1")
    V2 = load_tag("/tmp/s7-extract-v.log", "V_C2")
    for name, op in [("V0", V0), ("V1", V1)]:
        q, rem = right_divide(op, L)
        assert all(x == 0 for x in rem), (name, rem)
        print(name, "= Q L; remainder:", rem)
        print(name, "Q:", [sp.factor(x) for x in q])
else:
    print("V data not ready; stopping after U/D factor audit")
    raise SystemExit(0)


# State at n: A[0:2], U[0:2], UU[0:2], VV[0:4], DD[0:3].
N = 13


def e(i):
    r = sp.zeros(1, N)
    r[0, i] = 1
    return r


def clean_row(r):
    return r.applyfunc(sp.cancel)


Ar = [e(0), e(1)]
for m in range(3):
    top = -(sh(L[0], m) * Ar[m] + sh(L[1], m) * Ar[m + 1]) / sh(L[2], m)
    Ar.append(clean_row(top))

Ur = [e(2), e(3)]
for m in range(2):
    forcing = sp.zeros(1, N)
    for i, ci in enumerate(U1):
        forcing += sh(ci, m) * Ar[m + i]
    top = -(sh(U0[0], m) * Ur[m] + sh(U0[1], m) * Ur[m + 1] + forcing) / sh(U0[2], m)
    Ur.append(clean_row(top))

UUr = [e(4), e(5)]
forcing = sp.zeros(1, N)
for i, ci in enumerate(U1):
    forcing += 2 * ci * Ur[i]
for i, ci in enumerate(U2):
    forcing += ci * Ar[i]
UUtop = clean_row(-(U0[0] * UUr[0] + U0[1] * UUr[1] + forcing) / U0[2])

VVr = [e(6), e(7), e(8), e(9)]
forcing = sp.zeros(1, N)
for i, ci in enumerate(V2):
    forcing += ci * Ar[i]
VVtop = clean_row(-(sum((V0[i] * VVr[i] for i in range(4)), sp.zeros(1, N)) + forcing) / V0[4])

DDr = [e(10), e(11), e(12)]
forcing = sp.zeros(1, N)
for i, ci in enumerate(D1):
    forcing += 2 * ci * Ur[i]
for i, ci in enumerate(D2):
    forcing += ci * Ar[i]
DDtop = clean_row(-(sum((D0[i] * DDr[i] for i in range(3)), sp.zeros(1, N)) + forcing) / D0[3])

T = sp.zeros(N, N)
rows = [Ar[1], Ar[2], Ur[1], Ur[2], UUr[1], UUtop,
        VVr[1], VVr[2], VVr[3], VVtop,
        DDr[1], DDr[2], DDtop]
for i, row in enumerate(rows):
    T[i, :] = row

print("transition matrix built")

jrow = (DDr[0] - UUr[0] - VVr[0]) / 2
krylov = [jrow]
for degree in range(1, N + 2):
    prev = krylov[-1].subs(n, n + 1) * T
    krylov.append(clean_row(prev))
    print("krylov row", degree, "built")
    M = sp.Matrix.vstack(*krylov)
    ns = M.T.nullspace()
    if ns:
        coeff = [sp.factor(sp.cancel(x)) for x in ns[0]]
        print("J recurrence order", degree)
        print("JOP", coeff)
        q, rem = right_divide(coeff, L)
        assert all(x == 0 for x in rem), rem
        print("JOP right remainder by L", rem)
        print("JOP quotient", [sp.factor(x) for x in q])
        print("ALL CELL, FACTORIZATION, AND ORE ASSERTIONS PASSED")
        break
else:
    raise RuntimeError("no cyclic-vector recurrence found")
