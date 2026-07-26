"""The bare-alphabet fitter.

probe(lab, argnames, w=None, discs=(), maxdeg=None, N=..., chi_hom=None)
  -> dict with rank / excess / consistent / (exact terms, held-out verdict)

Verdicts are refused unless excess >= GUARD (default 40) excess equations.
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import numpy as np

import core
from core import (PRIMES, Tab, ETab, monomials, mname, rref, consistency, crt,
                  ratrecon, bmod, SEQS, gen_B)
from fams import FAMS, Fac

PAR = {l: (f, p) for l, f, p, _, _ in SEQS}
PAR['E2'] = PAR['E']          # second representation, same recurrence/second solution
GUARD = 40
_BC = {}


def Bseq_of(lab, N):
    if (lab, N) not in _BC:
        fam, par = PAR[lab]
        _BC[(lab, N)] = gen_B(fam, par, N + 4)
    return _BC[(lab, N)]


def keys_of(w, discs, rmin=1):
    ks = [('H', r) for r in range(rmin, w + 1)]
    for Dd in discs:
        ks += [('K', Dd, r) for r in range(rmin, w + 1)]
    return ks


def design_of(F, mons, N, q, argnames):
    M = F.maxtop * N + 8
    fac = Fac(M, q)
    keys = sorted({L[0] for m in mons for L in m})
    tab = Tab(M, q, keys)
    rows = np.zeros((N, len(mons)), dtype=np.int64)
    for n in range(1, N + 1):
        S = F.Smod(n, fac)
        if S.size == 0:
            continue
        ix = F.idx(n)
        cache = {}
        for j, m in enumerate(mons):
            v = S
            for L in m:
                if L not in cache:
                    cache[L] = tab.vals(L[0], ix[L[1]])
                v = v * cache[L] % q
            rows[n - 1, j] = int(v.sum() % q)
    return rows


def rhs_of(lab, N, q):
    Bn = Bseq_of(lab, N)
    return np.array([bmod(Bn[n], q) for n in range(1, N + 1)], dtype=np.int64)


def probe(lab, argnames, w=None, discs=(), maxdeg=None, N=110, chi_hom=None,
          guard=GUARD, verbose=True, extract=True, holdout=None, prim=4,
          mons=None, tag='', q=None):
    F = FAMS[lab]
    w = F.w if w is None else w
    if mons is None:
        mons = monomials(keys_of(w, discs), argnames, w, maxdeg, chi_hom)
    q = q or PRIMES[0]
    A = design_of(F, mons, N, q, argnames)
    b = rhs_of(lab, N, q)
    nz = int(np.sum((np.any(A != 0, axis=1)) | (b != 0)))
    r = consistency(A, b, q)
    r['excess'] = nz - r['rank']
    r['mons'] = mons
    r['label'] = '%s%s w=%d args=%s deg<=%s disc=%s hom=%s' % (
        lab, ('/' + tag if tag else ''), w, ','.join(argnames), maxdeg, discs, chi_hom)
    head = '%-58s cols=%-4d rank=%-4d excess=%-4d' % (r['label'], len(mons), r['rank'], r['excess'])
    if r['excess'] < guard:
        r['verdict'] = 'REFUSED (excess %d < %d)' % (r['excess'], guard)
        if verbose:
            print(head, r['verdict'], flush=True)
        return r
    if not r['consistent']:
        r['verdict'] = 'INCONSISTENT'
        if verbose:
            print(head, 'INCONSISTENT', flush=True)
        return r
    r['verdict'] = 'CONSISTENT'
    if verbose:
        print(head, 'CONSISTENT', flush=True)
    if extract:
        ex = extract_exact(lab, mons, N, r['pivots'], prim=prim, holdout=holdout,
                           verbose=verbose)
        r.update(ex)
    return r


def solve_support(F, lab, mons, sup, N, q):
    """solve A[:,sup] x = b mod q ; returns (x or None, rank, excess)."""
    sm = [mons[j] for j in sup]
    A = design_of(F, sm, N, q, None)
    b = rhs_of(lab, N, q)
    nz = int(np.sum((np.any(A != 0, axis=1)) | (b != 0)))
    r = consistency(A, b, q)
    return (r['sol'] if r['consistent'] else None), r['rank'], nz - r['rank']


def extract_exact(lab, mons, N, sup, prim=4, holdout=None, verbose=True, NE=None):
    """CRT + rational reconstruction on the prescribed support, then EXACT held-out check."""
    F = FAMS[lab]
    sols, ms = [], []
    for q in PRIMES[:prim]:
        x, rk, exc = solve_support(F, lab, mons, sup, N, q)
        if x is None:
            if verbose:
                print('      extract: inconsistent on support at q=%d' % q)
            return dict(terms=None, heldout='EXTRACT-FAIL')
        sols.append([int(v) for v in x])
        ms.append(q)
    co = []
    for i in range(len(sup)):
        a, M = crt([s[i] for s in sols], ms)
        f = ratrecon(a, M)
        if f is None:
            if verbose:
                print('      extract: rational reconstruction failed at slot %d' % i)
            return dict(terms=None, heldout='RECON-FAIL')
        co.append(f)
    terms = [(co[i], mons[sup[i]]) for i in range(len(sup)) if co[i] != 0]
    ns = holdout if holdout is not None else list(range(N + 1, N + 9))
    NE = NE or (F.maxtop * max(ns) + 8)
    keys = sorted({L[0] for _, m in terms for L in m})
    et = ETab(NE, keys)
    Bn = Bseq_of(lab, max(ns) + 2)
    bad = core.exact_check(F, terms, Bn, ns, et)
    if verbose:
        print('      terms=%d  held-out n=%s: %s' % (
            len(terms), '%d..%d' % (min(ns), max(ns)),
            'ALL EXACT' if not bad else 'FAIL at %s' % bad))
        for c, m in terms:
            print('        %+s * %s' % (c, mname(m)))
    return dict(terms=terms, heldout=('OK' if not bad else 'FAIL %s' % bad),
                denoms=sorted({c.denominator for c, _ in terms}))


def minimize(lab, mons, N, sup, tries=6, seed=0, verbose=True, guard=GUARD):
    """greedy locally-minimal support (drop columns while the system stays consistent)."""
    F = FAMS[lab]
    q = PRIMES[0]
    best = list(sup)
    rnd = random.Random(seed)
    for t in range(tries):
        cur = list(best) if t == 0 else rnd.sample(list(best), len(best))
        order = list(cur)
        rnd.shuffle(order)
        keep = list(cur)
        for j in order:
            trial = [x for x in keep if x != j]
            if not trial:
                continue
            x, rk, exc = solve_support(F, lab, mons, trial, N, q)
            if x is not None and exc >= guard:
                keep = trial
        if len(keep) < len(best):
            best = keep
        if verbose:
            print('      minimize pass %d -> %d cols' % (t, len(keep)), flush=True)
    return sorted(best)
