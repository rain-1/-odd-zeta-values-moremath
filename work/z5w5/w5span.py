"""The BARE letter alphabet at WEIGHT 5:  H^(r)_x, r = 1..5, x one of the nine
arguments obtained by differentiating T's five binomials, and the weight-5
monomial span of degree <= 3 with its divisibility closure.

Conventions are EXACTLY z5rep/bare.py's (which is z5la/ordm.py's):
  * a "weight element" is a dict {monomial : constant}, monomial = sorted tuple
    of letter names;
  * a letter L carries a base offset delta_L and the SYMBOL L stands for
    L(n+delta_L,k,l);  delta_L = m for the letters whose argument carries -k or
    -l (the MIXED base of Z5CF_TELESCOPER 2.2).

Structure (measured, see _scope):
    9 symbols, weight 5, degree <= 3
        J = 1270 basis monomials
        981 MAXIMAL   (Theorem R, closed form)
        261 STANDALONE degree-2 blocks, every up-set of size exactly 10
         27 COUPLED   degree-1 blocks  (h1_*, h2_*, h3_*;  h4_* is standalone)
          1 COUPLED   () block
"""
import itertools
from fractions import Fraction as Fr

ARGS = {
    'n':   (1, 0, 0),
    'k':   (0, 1, 0),
    'l':   (0, 0, 1),
    'pk':  (1, 1, 0),      # n+k
    'pl':  (1, 0, 1),      # n+l
    'mk':  (1, -1, 0),     # n-k
    'ml':  (1, 0, -1),     # n-l
    'kl':  (0, 1, 1),      # k+l
    'pkl': (1, 1, 1),      # n+k+l
}
ARGORDER = ['n', 'k', 'l', 'pk', 'pl', 'mk', 'ml', 'kl', 'pkl']
SIX = ['k', 'l', 'pk', 'pl', 'mk', 'ml']
WMAX = 5


def lname(r, a):
    return 'h%d_%s' % (r, a)


LETTERS = {}
for _r in range(1, WMAX + 1):
    for _a in ARGORDER:
        LETTERS[lname(_r, _a)] = (_r, _a)
LWT = {nm: rv[0] for nm, rv in LETTERS.items()}


def delta(name, m):
    """mixed-base offset: m for the n-k / n-l family, 0 otherwise."""
    r, a = LETTERS[name]
    cn, ck, cl = ARGS[a]
    return m if (ck < 0 or cl < 0) else 0


def mono_wt(mon):
    return sum(LWT[L] for L in mon)


# ------------------------------------------------------------------ spans ----

def _partitions(W, maxparts, minv=1):
    if W == 0:
        yield ()
        return
    if maxparts == 0:
        return
    for v in range(minv, W + 1):
        for rest in _partitions(W - v, maxparts - 1, v):
            yield (v,) + rest


def tops(symbols=None, W=5, maxdeg=3):
    from collections import Counter
    syms = ARGORDER if symbols is None else list(symbols)
    out = []
    for pt in _partitions(W, maxdeg):
        cnt = Counter(pt)
        choices = []
        for r, c in sorted(cnt.items()):
            choices.append([tuple(sorted(x)) for x in
                            itertools.combinations_with_replacement(syms, c)])
        for combo in itertools.product(*choices):
            mon = []
            for (r, c), ss in zip(sorted(cnt.items()), combo):
                for s in ss:
                    mon.append(lname(r, s))
            out.append(tuple(sorted(mon)))
    return sorted(set(out))


def closure(T):
    seen = set()
    for m in T:
        for r in range(len(m) + 1):
            for sub in itertools.combinations(m, r):
                seen.add(tuple(sorted(sub)))
    return sorted(seen, key=lambda m: (-len(m), m))


def span_w5(symbols=None, W=5, maxdeg=3):
    T = tops(symbols, W, maxdeg)
    return closure(T), set(T)


def upset(B, mon, idx=None):
    """[(j, rest)] with  mon * rest = B[j]  as multisets."""
    out = []
    for j, m in enumerate(B):
        rest = list(m)
        ok = True
        for L in mon:
            if L in rest:
                rest.remove(L)
            else:
                ok = False
                break
        if ok:
            out.append((j, tuple(sorted(rest))))
    return out


def blocks(B):
    """(maximal, standalone, coupled, upsets) -- indices into B."""
    us = {j: upset(B, B[j]) for j in range(len(B))}
    maxi = set(j for j in range(len(B)) if len(us[j]) == 1)
    stand, coup = [], []
    for j in range(len(B)):
        if j in maxi:
            continue
        if all(jj in maxi for jj, _ in us[j] if jj != j):
            stand.append(j)
        else:
            coup.append(j)
    return sorted(maxi), stand, coup, us


# ------------------------------------------------------------------ sigma ----

SWAP = {'k': 'l', 'l': 'k', 'pk': 'pl', 'pl': 'pk', 'mk': 'ml', 'ml': 'mk',
        'n': 'n', 'kl': 'kl', 'pkl': 'pkl'}


def sigma_letter(L):
    r, a = LETTERS[L]
    return lname(r, SWAP[a])


def sigma_mono(m):
    return tuple(sorted(sigma_letter(L) for L in m))


def sigma_el(el):
    out = {}
    for m, c in el.items():
        mm = sigma_mono(m)
        out[mm] = out.get(mm, 0) + c
    return {m: c for m, c in out.items() if c != 0}


def sym_el(el):
    s = sigma_el(el)
    out = {m: Fr(c, 2) for m, c in el.items()}
    for m, c in s.items():
        out[m] = out.get(m, Fr(0)) + Fr(c, 2)
    return {m: c for m, c in out.items() if c != 0}


def anti_el(el):
    s = sigma_el(el)
    out = {m: Fr(c, 2) for m, c in el.items()}
    for m, c in s.items():
        out[m] = out.get(m, Fr(0)) - Fr(c, 2)
    return {m: c for m, c in out.items() if c != 0}


# ---------------------------------------------------------- element algebra --

def el_mul(a, b):
    out = {}
    for m1, v1 in a.items():
        for m2, v2 in b.items():
            m = tuple(sorted(m1 + m2))
            out[m] = out.get(m, Fr(0)) + Fr(v1) * Fr(v2)
    return {m: c for m, c in out.items() if c != 0}


def el_add(*els):
    out = {}
    for e in els:
        for m, c in e.items():
            out[m] = out.get(m, Fr(0)) + Fr(c)
    return {m: c for m, c in out.items() if c != 0}


def el_scale(a, c):
    return {m: Fr(v) * Fr(c) for m, v in a.items() if Fr(v) * Fr(c) != 0}


# --------------------------------------------------------- the two weights ---
# ZETA5_CLOSEDFORM 0:
#   A_r(x) = H^(r)_{n+x} - H^(r)_x ,  B_r(x) = H^(r)_{n-x} - H^(r)_x
#   alpha = A1(k)-A1(l),  beta = B1(k)-B1(l),  Psi = alpha/2 + beta
#   w3hat = H3_{n+k} - Psi H2_{n+k}
#   w5    = H5_{n+k} + (1/2)(alpha-beta) H4_{n+k}
#           + [ (1/4)(A2(k)+A2(l)) - (1/2) alpha Psi ] H3_{n+k}

def _alpha():
    return {('h1_pk',): Fr(1), ('h1_k',): Fr(-1),
            ('h1_pl',): Fr(-1), ('h1_l',): Fr(1)}


def _beta():
    return {('h1_mk',): Fr(1), ('h1_k',): Fr(-1),
            ('h1_ml',): Fr(-1), ('h1_l',): Fr(1)}


def w5_el():
    al = _alpha(); be = _beta()
    Psi = el_add(el_scale(al, Fr(1, 2)), be)
    amb = el_add(al, el_scale(be, -1))
    A2sum = {('h2_pk',): Fr(1), ('h2_k',): Fr(-1),
             ('h2_pl',): Fr(1), ('h2_l',): Fr(-1)}
    c3 = el_add(el_scale(A2sum, Fr(1, 4)), el_scale(el_mul(al, Psi), Fr(-1, 2)))
    w = el_add({('h5_pk',): Fr(1)},
               el_scale(el_mul(amb, {('h4_pk',): Fr(1)}), Fr(1, 2)),
               el_mul(c3, {('h3_pk',): Fr(1)}))
    return w


def w3hat_el():
    al = _alpha(); be = _beta()
    Psi = el_add(el_scale(al, Fr(1, 2)), be)
    return el_add({('h3_pk',): Fr(1)},
                  el_scale(el_mul(Psi, {('h2_pk',): Fr(1)}), -1))


def el_to_vec(B, el, p=None):
    idx = {m: j for j, m in enumerate(B)}
    v = [0] * len(B)
    for m, c in el.items():
        c = Fr(c)
        if m not in idx:
            raise KeyError('monomial %r outside the span' % (m,))
        if p is None:
            v[idx[m]] = c
        else:
            v[idx[m]] = c.numerator % p * pow(c.denominator % p, p - 2, p) % p
    return v


if __name__ == '__main__':
    from collections import Counter
    for syms, lab in ((ARGORDER, '9-symbol'), (SIX, '6-symbol')):
        B, T = span_w5(syms)
        maxi, stand, coup, us = blocks(B)
        print('%s  J=%d  tops=%d  maximal=%d  standalone=%d  coupled=%d'
              % (lab, len(B), len(T), len(maxi), len(stand), len(coup)))
        print('   standalone up-set sizes:', Counter(len(us[j]) for j in stand))
        print('   coupled:', [B[j] for j in coup][:5], '...')
        print('   degrees in B:', Counter(len(m) for m in B))
    B, T = span_w5()
    w5 = w5_el()
    print('w5 support %d, all in span: %s'
          % (len(w5), all(m in set(B) for m in w5)))
    print('w5 degrees:', Counter(len(m) for m in w5))
    print('w5 closure size:', len(closure(list(w5))))
    print('sigma-orbits of B:', len(set(frozenset([m, sigma_mono(m)]) for m in B)))
