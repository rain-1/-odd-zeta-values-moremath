"""g_search2.py -- exhaustive cross-h0 search for transfer identities in the
LSZ-shape p-adic family (numerator bricks at theta, denominator bricks at Z).

    R(t) = (2t+h0) * prod_{j=1..M} (t+theta+e_j)_{h0-2e_j}
                   / prod_{j=1..M} (t+f_j)_{h0+1-2f_j}

M = w-1 (M=2 -> zeta_p(3);  M=4 -> zeta_p(5), the LSZ shape).

Two linear forms are related by a transfer identity iff they are exactly
proportional.  We test EVERY pair across a range of h0 -- this is the only
place a Rhin-Viola-type group could hide, because the group moves h0
(Zudilin's generator a_j changes h_0 = b_3+b_4-b_1-a_1).
"""

import itertools
import sys
from fractions import Fraction as F
from collections import defaultdict

from g_forms import VWP
from g_search import fact_str


def points(h0, M, theta):
    out = []
    for e in itertools.combinations_with_replacement(range(h0 // 2 + 1), M):
        if any(h0 - 2 * x < 0 for x in e):
            continue
        for f in itertools.combinations_with_replacement(range(h0 // 2 + 1), M):
            if any(h0 + 1 - 2 * x < 1 for x in f):
                continue
            v = VWP(h0, e, f, theta)
            # weight-w condition: rho_i = 0 for odd i < M-1.
            # M=2: no condition (deg = -1 + 2(sum f - sum e) <= -1 needed for
            #      convergence of the sum / integrability: deg <= -2 is safest
            #      but deg = -1 is what the symmetric point has).
            if M == 2:
                if v.deg > -1:
                    continue
            else:
                if v.deg > -2:
                    continue
            out.append((h0, e, f))
    return out


def evaluate(h0, e, f, M, theta):
    v = VWP(h0, e, f, theta)
    r = v.partial_fractions()
    rho = v.rho(r)
    zc = rho[M - 1]        # coefficient of zeta_p(M+1)
    if M == 2:
        zc = rho[1]
    return v.rho0(r), zc


def main():
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    hmax = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    theta = F(1, 2)
    data = {}
    for h0 in range(1, hmax + 1):
        for (a, e, f) in points(h0, M, theta):
            try:
                r0, rz = evaluate(a, e, f, M, theta)
            except AssertionError:
                continue
            if rz != 0:
                data[(a, e, f)] = (r0, rz)
    keys = sorted(data)
    print(f"M={M} (weight {M+1}), theta={theta}, h0<= {hmax}: "
          f"{len(keys)} points with non-zero zeta coefficient")

    hits = []
    for i in range(len(keys)):
        r0i, rzi = data[keys[i]]
        for j in range(i + 1, len(keys)):
            r0j, rzj = data[keys[j]]
            if r0i * rzj - r0j * rzi == 0:
                hits.append((keys[i], keys[j]))
    print(f"  exactly-proportional pairs found: {len(hits)}")
    shown = 0
    for a, b in hits:
        if a[0] == b[0] and sorted(a[1]) == sorted(b[1]) and sorted(a[2]) == sorted(b[2]):
            continue      # same point
        if shown < 20:
            ka = data[a][1] / data[b][1]
            print(f"    {a}  <->  {b}   kappa = {fact_str(ka)}")
            shown += 1
    # how many are genuine (different h0 or different multisets)?
    genuine = [(a, b) for a, b in hits
               if not (a[0] == b[0] and a[1] == b[1] and a[2] == b[2])]
    print(f"  genuine (distinct parameter) proportional pairs: {len(genuine)}")
    # cross-h0 only
    cross = [(a, b) for a, b in genuine if a[0] != b[0]]
    print(f"  of which CROSS-h0: {len(cross)}")


if __name__ == "__main__":
    main()
