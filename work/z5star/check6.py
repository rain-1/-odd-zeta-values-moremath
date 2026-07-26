"""JOB 4, deliverable (3): the exact-Q residual spot check of the DELIVERED
sparse-Z certificate at small n,k,l, done from scratch.

Nothing here reuses the mod-p machinery: the shift matrices, the base cofactors
P_i, the operator coefficients and the Q-row cofactors are all rebuilt in exact Q
from their definitions, and the cofactors are read out of CERT_wstar_sparse.json.

Checked identity, for every monomial M_i of the 42-element closure:

  sum_j [ gk*(Sk)_{ij}*rho_j(n,k+1,l) + gl*(Sl)_{ij}*sigma_j(n,k,l+1) ]
        - rho_i(n,k,l) - sigma_i(n,k,l)   =   (E_w / Phi)_i (n,k,l)

  gk = (n+3-k)^2 (n+k+1)(n+k+l+1) / [ (k+1)^3 (k+l+1) ]        (l mirror for gl)

k = n+3 and l = n+3 are skipped: there gk (resp. gl) vanishes and the individual
(Sk) entries have removable poles, so a naive rational evaluation is 0/0.  That
is exactly the (P-int) point of Z5STAR_CERT 2.4 and it is a property of the
evaluation, not of the identity.
"""
import os, sys, json
from fractions import Fraction as Fr
HERE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'
sys.path.insert(0, HERE)
sys.path.insert(1, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import wtools as W
import bare, zla, qrow

M = 3
DN = [(0, 1), (-1, 4), (-2, 4), (-3, 2), (-4, 2), (-5, 2), (-6, 2), (-7, 2)]


def dn_val(n):
    v = 1
    for r, m in DN:
        v *= (n - r) ** m
    return v


def Dval(n, k, l):
    return ((k + l + 1) * (n + k + 1) * (n + k + 2) * (n + k + 3)
            * (n + l + 1) * (n + l + 2) * (n + l + 3))


def Pm(n, k, l, i):
    v = 1
    for j in range(1, i + 1):
        v *= (n + j) * (n + k + j) * (n + l + j) * (n + k + l + j)
    a = 1; b = 1
    for j in range(i + 1, M + 1):
        a *= (n + j - k); b *= (n + j - l)
    return v * a * a * b * b


def gk(n, k, l):
    return Fr((n + 3 - k) ** 2 * (n + k + 1) * (n + k + l + 1),
              (k + 1) ** 3 * (k + l + 1))


def gl(n, k, l):
    return Fr((n + 3 - l) ** 2 * (n + l + 1) * (n + k + l + 1),
              (l + 1) ** 3 * (k + l + 1))


def sym_arg(L, n, k, l):
    r, a = bare.LETTERS[L]
    cn, ck, cl = bare.ARGS[a]
    d = bare.delta(L, M)
    return r, cn * (n + d) + ck * k + cl * l, (cn, ck, cl), d


def inck(L, n, k, l):
    r, xb, (cn, ck, cl), d = sym_arg(L, n, k, l)
    if ck == 1:
        return Fr(1, (xb + 1) ** r)
    if ck == -1:
        return -Fr(1, xb ** r)
    return Fr(0)


def incl(L, n, k, l):
    r, xb, (cn, ck, cl), d = sym_arg(L, n, k, l)
    if cl == 1:
        return Fr(1, (xb + 1) ** r)
    if cl == -1:
        return -Fr(1, xb ** r)
    return Fr(0)


def incn(L, n, k, l, aa):
    """symbol(n+aa) - symbol(n+delta), exactly as work/z5rep/frw.PD._build"""
    r, a = bare.LETTERS[L]
    cn, ck, cl = bare.ARGS[a]
    d = bare.delta(L, M)
    if cn == 0:
        return Fr(0)
    tot = Fr(0)
    if aa > d:
        for ii in range(d, aa):
            tot += Fr(1, (cn * (n + ii) + ck * k + cl * l + 1) ** r)
    elif aa < d:
        for ii in range(aa, d):
            tot -= Fr(1, (cn * (n + ii) + ck * k + cl * l + 1) ** r)
    return tot


def divide(mi, mj):
    rest = list(mj)
    for L in mi:
        if L in rest:
            rest.remove(L)
        else:
            return None
    return tuple(sorted(rest))


_QC = None


def qcof(n, k, l):
    """r_Q, s_Q in exact Q from work/z5cf/Qrow_phicert.m's coefficient dicts"""
    global _QC
    if _QC is None:
        _QC = qrow._dd()

    def ev(key):
        s = 0
        for (i, j, m), c in _QC[key].items():
            s += c * n ** i * k ** j * l ** m
        return s
    return (Fr(ev('r_num'), ev('r_den')), Fr(ev('s_num'), ev('s_den')))


def load_cert():
    d = json.load(open(os.path.join(HERE, 'CERT_wstar_sparse.json')))
    blocks = {}
    for key, v in d['blocks'].items():
        nm, part = key.split('|')
        mon = () if nm == '1' else tuple(nm.split('*'))
        # columns: [[e_k,e_l], scale, [[e_n, c], ...]]  ->  rho = sum c/(scale) n^e k^a l^b
        terms = []
        for (a, b), dd, iv in v['columns']:
            dd = Fr(dd)
            for e, c in iv:
                terms.append(((e, a, b), Fr(c) / dd))
        blocks[(mon, part)] = (terms, Fr(1))
    wQ = {(() if kk == '1' else tuple(kk.split('*'))): Fr(vv)
          for kk, vv in d['weight'].items() if Fr(vv) != 0}
    return blocks, wQ


def cof(blocks, mon, part, n, k, l):
    t = blocks.get((mon, part))
    if t is None:
        return None
    terms, sc = t
    s = 0
    for (e, a, b), c in terms:
        s += c * n ** e * k ** a * l ** b
    return Fr(s) / (Fr(sc) * dn_val(n) * Dval(n, k, l))


if __name__ == '__main__':
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    blocks, wQ = load_cert()
    # the 42-element closure of supp(w*)
    clo = sorted({tuple(sorted(s)) for m in wQ
                  for r in range(len(m) + 1)
                  for s in __import__('itertools').combinations(m, r)},
                 key=lambda m: (-len(m), m))
    maximal = [m for m in clo if not any(divide(m, mm) not in (None, ())
                                         for mm in clo)]
    print('closure J = %d, maximal blocks = %d, ansatz blocks delivered = %d'
          % (len(clo), len(maximal), len({k[0] for k in blocks})))
    bad = 0
    cells = 0
    for n in range(1, NMAX + 1):
        for k in range(0, NMAX + 1):
            for l in range(0, NMAX + 1):
                if k == n + 3 or l == n + 3:
                    continue
                cells += 1
                RK = gk(n, k, l); RL = gl(n, k, l)
                for mi in clo:
                    acc = Fr(0)
                    for mj in clo:
                        rest = divide(mi, mj)
                        if rest is None:
                            continue
                        sk = Fr(1); sl = Fr(1)
                        for L in rest:
                            sk *= inck(L, n, k, l); sl *= incl(L, n, k, l)
                        if mj in maximal:
                            wj = wQ.get(mj, Fr(0))
                            if wj == 0:
                                continue
                            r1, _ = qcof(n, k + 1, l)
                            _, s1 = qcof(n, k, l + 1)
                            rj1 = wj * r1; sj1 = wj * s1
                        else:
                            rj1 = cof(blocks, mj, 'rho', n, k + 1, l)
                            sj1 = cof(blocks, mj, 'sigma', n, k, l + 1)
                            if rj1 is None:
                                rj1 = Fr(0)
                            if sj1 is None:
                                sj1 = Fr(0)
                        acc += RK * sk * rj1 + RL * sl * sj1
                    if mi in maximal:
                        wj = wQ.get(mi, Fr(0))
                        r0, s0 = qcof(n, k, l)
                        acc -= wj * r0 + wj * s0
                    else:
                        a = cof(blocks, mi, 'rho', n, k, l)
                        b = cof(blocks, mi, 'sigma', n, k, l)
                        acc -= (a or Fr(0)) + (b or Fr(0))
                    # right-hand side (E_w / Phi)_{mi}
                    rhs = Fr(0)
                    cc = zla.cc(n)
                    for mj in clo:
                        wj = wQ.get(mj, Fr(0))
                        if wj == 0:
                            continue
                        rest = divide(mi, mj)
                        if rest is None:
                            continue
                        for u in range(4):
                            pr = Fr(Pm(n, k, l, u))
                            for L in rest:
                                pr *= incn(L, n, k, l, u)
                            rhs += wj * Fr(cc[u]) * pr
                    if acc != rhs:
                        bad += 1
                        if bad <= 5:
                            print('   MISMATCH n=%d k=%d l=%d block %s : %s'
                                  % (n, k, l, '*'.join(mi) or '1', acc - rhs))
    print('exact-Q residual check: %d cells x %d components = %d identities, %d mismatches'
          % (cells, len(clo), cells * len(clo), bad))
