"""The BARE letter alphabet  H^(r)_x ,  x in the nine arguments of T, and the
weight-3 monomial span with its divisibility closure.

Conventions are EXACTLY zla/ordm's:
  * a "weight element" is a dict {monomial : constant}, monomial = sorted tuple
    of letter names;
  * a letter L carries a base offset delta_L, and the SYMBOL L stands for
    L(n+delta_L, k, l);  w(n+a,k,l) is expanded in those symbols by adding
    tot_L(a) = L(n+a) - L(n+delta_L)  to each symbol  (zla.w_shift_mixed).
  * delta_L = m  exactly for the letters whose argument carries -k or -l, which
    is what cancels Pm's double zeros prod_{j}(n+j-k)^2  (the MIXED base).
"""
import itertools

# argument name -> (c_n, c_k, c_l);  x = c_n*n + c_k*k + c_l*l
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
WMAX = 3


def lname(r, a):
    return 'h%d_%s' % (r, a)


LETTERS = {}                     # name -> (r, argname)
for _r in range(1, WMAX + 1):
    for _a in ARGORDER:
        LETTERS[lname(_r, _a)] = (_r, _a)

LWT = {nm: rv[0] for nm, rv in LETTERS.items()}


def delta(name, m):
    """mixed-base offset: m for the n-k / n-l family, 0 otherwise."""
    r, a = LETTERS[name]
    cn, ck, cl = ARGS[a]
    return m if (ck < 0 or cl < 0) else 0


# ------------------------------------------------------------------- spans --

def mono_wt(mon):
    return sum(LWT[L] for L in mon)


def span_w3(symbols=None, maxdeg=2):
    """all weight-3 monomials of degree <= maxdeg, plus the divisibility
    closure.  Returned ordered by (degree, name) -- descending degree first so
    that the cascade order is triangular."""
    syms = ARGORDER if symbols is None else list(symbols)
    tops = []
    if maxdeg >= 1:
        tops += [(lname(3, a),) for a in syms]
    if maxdeg >= 2:
        tops += [tuple(sorted((lname(1, a), lname(2, b)))) for a in syms for b in syms]
    if maxdeg >= 3:
        for c in itertools.combinations_with_replacement(syms, 3):
            tops.append(tuple(sorted(lname(1, a) for a in c)))
    seen = set()
    for m in tops:
        for r in range(len(m) + 1):
            for sub in itertools.combinations(m, r):
                seen.add(tuple(sorted(sub)))
    B = sorted(seen, key=lambda m: (-len(m), m))
    return B, set(tops)


def upset(B, mon):
    """{ j : mon divides B[j] } as multisets."""
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


# ------------------------------------------------------- the two weights ----

def w3hat_el():
    """what3 = H3_{n+k} - Psi * H2_{n+k},
       Psi = 1/2 H_{n+k} - 1/2 H_{n+l} + H_{n-k} - H_{n-l} - 3/2 H_k + 3/2 H_l"""
    from fractions import Fraction as Fr
    Psi = {('h1_pk',): Fr(1, 2), ('h1_pl',): Fr(-1, 2),
           ('h1_mk',): Fr(1), ('h1_ml',): Fr(-1),
           ('h1_k',): Fr(-3, 2), ('h1_l',): Fr(3, 2)}
    out = {('h3_pk',): Fr(1)}
    for m, c in Psi.items():
        mm = tuple(sorted(m + ('h2_pk',)))
        out[mm] = out.get(mm, Fr(0)) - c
    return {m: c for m, c in out.items() if c != 0}


def vtilde_el():
    """vt = H3_n + 2 A3(k) + 1/2 (A2(l)-A2(k)) * (A1(k) + 3 B1(k))
       A3(k) = h3_pk - h3_k ; A2(l)-A2(k) = h2_pl - h2_l - h2_pk + h2_k
       A1(k)+3B1(k) = h1_pk + 3 h1_mk - 4 h1_k"""
    from fractions import Fraction as Fr
    out = {('h3_n',): Fr(1), ('h3_pk',): Fr(2), ('h3_k',): Fr(-2)}
    X = {('h2_pl',): Fr(1), ('h2_l',): Fr(-1), ('h2_pk',): Fr(-1), ('h2_k',): Fr(1)}
    Y = {('h1_pk',): Fr(1), ('h1_mk',): Fr(3), ('h1_k',): Fr(-4)}
    for a, ca in X.items():
        for b, cb in Y.items():
            mm = tuple(sorted(a + b))
            out[mm] = out.get(mm, Fr(0)) + Fr(1, 2) * ca * cb
    return {m: c for m, c in out.items() if c != 0}


SWAP = {'k': 'l', 'l': 'k', 'pk': 'pl', 'pl': 'pk', 'mk': 'ml', 'ml': 'mk',
        'n': 'n', 'kl': 'kl', 'pkl': 'pkl'}


def sigma_letter(L):
    r, a = LETTERS[L]
    return lname(r, SWAP[a])


def sigma_el(el):
    out = {}
    for m, c in el.items():
        mm = tuple(sorted(sigma_letter(L) for L in m))
        out[mm] = out.get(mm, 0) + c
    return {m: c for m, c in out.items() if c != 0}


def sym_el(el):
    from fractions import Fraction as Fr
    s = sigma_el(el)
    out = {m: Fr(c, 2) for m, c in el.items()}
    for m, c in s.items():
        out[m] = out.get(m, Fr(0)) + Fr(c, 2)
    return {m: c for m, c in out.items() if c != 0}


def anti_el(el):
    from fractions import Fraction as Fr
    s = sigma_el(el)
    out = {m: Fr(c, 2) for m, c in el.items()}
    for m, c in s.items():
        out[m] = out.get(m, Fr(0)) - Fr(c, 2)
    return {m: c for m, c in out.items() if c != 0}


def testvecs():
    w = w3hat_el(); v = vtilde_el()
    return [('w3hat', w), ('w3hat_sym', sym_el(w)), ('w3hat_anti', anti_el(w)),
            ('vtilde', v), ('vtilde_sym', sym_el(v))]


def el_to_vec(B, el, p=None):
    idx = {m: j for j, m in enumerate(B)}
    from fractions import Fraction as Fr
    v = [0] * len(B)
    for m, c in el.items():
        c = Fr(c)
        if p is None:
            v[idx[m]] = c
        else:
            v[idx[m]] = c.numerator % p * pow(c.denominator % p, p - 2, p) % p
    return v


if __name__ == '__main__':
    for D in (2, 3):
        B, tops = span_w3(maxdeg=D)
        print('maxdeg %d : J = %d basis monomials, %d weight-3 tops'
              % (D, len(B), len(tops)))
        nonmax = [m for m in B if len(upset(B, m)) > 1]
        print('   blocks with a nontrivial up-set: %d' % len(nonmax))
        from collections import Counter
        print('   up-set sizes:', Counter(len(upset(B, m)) for m in nonmax))
    B, tops = span_w3(maxdeg=2)
    w = w3hat_el(); v = vtilde_el()
    print('w3hat  support %d, in span: %s' % (len(w), all(m in B for m in w)))
    print('vtilde support %d, in span: %s' % (len(v), all(m in B for m in v)))
    print('w3hat  =', sorted(w.items()))
    print('vtilde =', sorted(v.items()))
