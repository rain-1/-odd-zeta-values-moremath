"""Hunt for TAME binomial-sum representations A(n) = sum_k S(n,k).

"Tame" means: every Gamma-argument of S (every binomial top, bottom and top-bottom,
and every exponential exponent) is a linear form x(n,k) with 0 <= x <= n on the
support.  If the support is k in [0, n/m], the tame forms are exactly
      { j*k : 1<=j<=m }  u  { n - j*k : 0<=j<=m },
and the tame binomial pairs (T,B) (needing T, B, T-B all tame) are exactly
      (j k, i k) i<j ;  (n - i k, j k) with i+j<=m ;  (n - i k, n - j k) with i<j.

At n=1 the support of any m>=2 template is k=0 alone and every binomial is 1,
so  A(1) = base^{e(1,0)} -- which pins the exponential almost completely.
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math import comb
from core import SEQS, gen_A

PAR = {l: (f, p) for l, f, p, _, _ in SEQS}


def tame_forms(m):
    out = [('k', 0, j) for j in range(1, m + 1)]          # j*k
    out += [('n', 1, -j) for j in range(0, m + 1)]        # n - j*k
    return out                                            # (tag, cn, ck): cn*n + ck*k


def ev(f, n, k):
    return f[1] * n + f[2] * k


def tame_pairs(m):
    P = []
    for j in range(1, m + 1):
        for i in range(0, j):
            if i == 0:
                continue
            P.append((('k', 0, j), ('k', 0, i)))
    for i in range(0, m + 1):
        for j in range(1, m + 1):
            if i + j <= m:
                P.append((('n', 1, -i), ('k', 0, j)))
    for i in range(0, m + 1):
        for j in range(i + 1, m + 1):
            P.append((('n', 1, -i), ('n', 1, -j)))
    return P


def perfect_bases(b):
    """(base, c) with base**c == b, c>=1."""
    out = []
    for base in range(2, abs(b) + 1):
        v, c = base, 1
        while v <= abs(b):
            if v == abs(b):
                out.append((base, c))
            v *= base
            c += 1
    return out


def candidates(m, b, maxfac=5):
    P = tame_pairs(m)
    exps = [None]
    for (base, c) in perfect_bases(b):
        for j in range(0, m + 1):
            exps.append((base, c, j))          # base ** (c*(n - j*k))
    for sg in (1, -1):
        for ne in range(1, maxfac + 1):
            for ms in itertools.combinations_with_replacement(range(len(P)), ne):
                for e in exps:
                    yield (sg, e, tuple(P[i] for i in ms))


def value(cand, n, k):
    sg, e, pairs = cand
    v = (-1) ** k if sg < 0 else 1
    if e is not None:
        base, c, j = e
        ex = c * (n - j * k)
        if ex < 0:
            return 0
        v *= base ** ex
    for (T, B) in pairs:
        t, bb = ev(T, n, k), ev(B, n, k)
        if bb < 0 or t < bb or t < 0:
            return 0
        v *= comb(t, bb)
        if v == 0:
            return 0
    return v


def total(cand, n):
    return sum(value(cand, n, k) for k in range(n + 1))


def hunt(lab, ms=(2, 3, 4, 5), maxfac=5, NCHK=13, NDEEP=26, verbose=True):
    fam, par = PAR[lab]
    An = gen_A(fam, par, NDEEP + 2)
    b = par[1]
    hits = []
    for m in ms:
        mf = maxfac if m <= 3 else min(maxfac, 4)
        cnt = 0
        for cand in candidates(m, b, mf):
            cnt += 1
            if total(cand, 1) != An[1]:
                continue
            if total(cand, 2) != An[2] or total(cand, 3) != An[3]:
                continue
            if any(total(cand, n) != An[n] for n in range(4, NCHK)):
                continue
            if any(total(cand, n) != An[n] for n in range(NCHK, NDEEP)):
                continue
            hits.append((m, cand))
        if verbose:
            print('   %s m=%d: %d templates scanned' % (lab, m, cnt), flush=True)
    return hits


def show(cand):
    sg, e, pairs = cand
    s = '(-1)^k ' if sg < 0 else ''
    if e is not None:
        base, c, j = e
        s += '%d^(%s(n-%dk)) ' % (base, '' if c == 1 else str(c), j)
    from collections import Counter
    cc = Counter(pairs)
    for (T, B), ex in sorted(cc.items(), key=str):
        nm = lambda f: ('%dk' % f[2] if f[1] == 0 else ('n' if f[2] == 0 else 'n-%dk' % (-f[2])))
        s += 'C(%s,%s)%s ' % (nm(T), nm(B), '' if ex == 1 else '^%d' % ex)
    return s.strip()


if __name__ == '__main__':
    labs = sys.argv[1].split(',') if len(sys.argv) > 1 else \
        ['E', 'alpha', 'eps', 's7', 'C', 'B', 'F', 'delta', 'zeta', 'eta', 's18', 'A', 'D', 'gamma', 's10']
    mf = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    for lab in labs:
        print('==== %s (b=%d, A(1)=%d)' % (lab, PAR[lab][1][1], gen_A(*PAR[lab], 3)[1]), flush=True)
        h = hunt(lab, maxfac=mf)
        if not h:
            print('   NO tame representation found', flush=True)
        for m, c in h:
            print('   m=%d  %s' % (m, show(c)), flush=True)
