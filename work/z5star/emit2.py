"""JOB 4 -- write the certificate in the sparse-expanded-over-Z format the
reflective checker wants, and measure the integer coefficient heights."""
import os, sys, json, pickle, time
from fractions import Fraction as Fr
from math import gcd
import numpy as np
HERE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'
sys.path.insert(0, HERE)
import mindens, wtools as W, cert3, cert2
import bare, cert

B = W.B
maximal, letters, zero_j = cert2.blocks_of(B)
dc = json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
wQ = [Fr(c) for c in dc['coeffs']]
w = W.to_p(wQ, W.P1)
act = [j for j in letters
       if any(cert.divide(B[j], B[jj]) is not None and w[jj] for jj in range(len(B)))]
ansL = cert3.mk('M0', 8, 0, 0)
ans0 = cert3.mk('M0', 12, 0, 0)
nrL = len(ansL.mons_r); nr0 = len(ans0.mons_r)


def block_of(c):
    if c < len(act) * ansL.nc:
        b = c // ansL.nc; off = c % ansL.nc
        nm = '*'.join(B[act[b]])
        return (nm, 'rho' if off < nrL else 'sigma',
                ansL.mons_r[off] if off < nrL else ansL.mons_s[off - nrL])
    off = c - len(act) * ansL.nc
    return ('1', 'rho' if off < nr0 else 'sigma',
            ans0.mons_r[off] if off < nr0 else ans0.mons_s[off - nr0])


if __name__ == '__main__':
    sys.set_int_max_str_digits(2000000)
    d = pickle.load(open(os.path.join(HERE, 'lift_Q.pkl'), 'rb'))
    out, degs = d['out'], d['degs']
    blocks = {}
    unl = 0
    for c, vec in out.items():
        nm, part, (a, b) = block_of(c)
        key = (nm, part)
        tgt = blocks.setdefault(key, [])
        for e, q in enumerate(vec):
            if q is None:
                unl += 1
                continue
            if q != 0:
                tgt.append(((e, a, b), q))
    print('unliftable coefficients: %d %s'
          % (unl, '' if unl == 0 else '*** THE PRIME SET IS TOO SMALL; '
                                      'the emitted file is INCOMPLETE ***'), flush=True)
    payload = {}
    stats = []
    for key in sorted(blocks):
        terms = blocks[key]
        if not terms:
            continue
        # NOTE: a single integer scale for a whole block is NOT delivered -- the
        # lcm of ~5000 coefficient denominators runs to tens of thousands of
        # digits (measured), which is useless.  Per-(k,l)-column clearing below.
        dn_ = max(m[0] for m, _ in terms); dk = max(m[1] for m, _ in terms)
        dl = max(m[2] for m, _ in terms)
        nbits = max(abs(q.numerator).bit_length() for _, q in terms)
        dbits = max(q.denominator.bit_length() for _, q in terms)
        bits = 0; sbits = 0
        stats.append((key[0], key[1], dn_, dk, dl, len(terms), nbits, dbits, bits, sbits))
        # per-(k,l)-column clearing: one integer scale per (e_k,e_l) instead of
        # one huge scale for the whole block.  Measured to be far smaller.
        cols = {}
        for m, q in terms:
            cols.setdefault((m[1], m[2]), []).append((m[0], q))
        colout = []
        colbits = 0
        colsc = 0
        for (a, b), lst in sorted(cols.items()):
            dd = 1
            for _, q in lst:
                dd = dd * q.denominator // gcd(dd, q.denominator)
            iv = [(e, int(q * dd)) for e, q in lst]
            gg = 0
            for _, v in iv:
                gg = gcd(gg, abs(v))
            if gg > 1:
                iv = [(e, v // gg) for e, v in iv]
                dd = Fr(dd, gg)
            colbits = max(colbits, max(abs(v).bit_length() for _, v in iv))
            colsc = max(colsc, Fr(dd).numerator.bit_length())
            colout.append([[a, b], str(dd), [[e, v] for e, v in sorted(iv)]])
        payload['%s|%s' % key] = dict(
            col_coef_bits=colbits, col_scale_bits=colsc,
            Q_num_bits=nbits, Q_den_bits=dbits,
            columns=colout,
            terms_Q=[[list(m), str(q)] for m, q in sorted(terms)])
        stats[-1] = stats[-1] + (colbits, colsc)
    hdr = ('block', 'part', 'deg_n', 'deg_k', 'deg_l', 'monomials',
           'Qnum', 'Qden', 'Zcoef', 'Zscale', 'colcoef', 'colscale')
    print('%-14s %-6s %6s %5s %5s %10s %7s %7s %8s %8s %8s %9s' % hdr)
    T = 0; MX = [0]*6
    for st in stats:
        print('%-14s %-6s %6d %5d %5d %10d %7d %7d %8d %8d %8d %9d' % st)
        T += st[5]
        for i in range(6):
            MX[i] = max(MX[i], st[6+i])
    print('%-14s %-6s %6s %5s %5s %10d %7d %7d %8d %8d %8d %9d'
          % (('MAX/TOTAL', '', '', '', '', T) + tuple(MX)))
    doc = dict(
        what='order-3 WZ certificate for the P-hat row of Brown-Zudilin zeta(5), '
             'representative w* (Z5CF_REP 4.2), cofactors over Z[n,k,l], sparse',
        operator='L_BZ = cc0..cc3 of lean/ZetaLucas/BZClosedForm.lean',
        base='Phi_3 of LEAN_Z5_SCAFFOLD 5.2 ; T(n+i,k,l) = Phi_3 * P_i ; '
             'uses the T_shift_n3 direction',
        mixed_base='H^(r)_{n-k}, H^(r)_{n-l} are normalised at n+3 '
                   '(Lean atoms Harm r (n+3-k), Harm r (n+3-l))',
        identity='rho_j = Nr_j / ( dn(n) * D(n,k,l) * scale ), likewise sigma_j = Ns_j / (...)',
        D='(k+l+1)*(n+k+1)*(n+k+2)*(n+k+3)*(n+l+1)*(n+l+2)*(n+l+3)',
        dn='n*(n+1)^4*(n+2)^4*(n+3)^2*(n+4)^2*(n+5)^2*(n+6)^2*(n+7)^2',
        validity='n >= 1 (dn(0) = 0); the n = 0 instance of BZRec is kernel-checked '
                 'separately in BZClosedForm.lean 3.4 / BZStar.lean',
        monomial_key='[e_n, e_k, e_l]',
        maximal_blocks='the 29 maximal monomials of the closure carry rho_j = w_j * r_Q, '
                       'sigma_j = w_j * s_Q with r_Q, s_Q the already-certified Q-row '
                       'cofactors (work/z5cf/Qrow_phicert.m, lean/ZetaLucas/BZQRow.lean)',
        weight=dict(zip(['*'.join(m) if m else '1' for m in B],
                        [str(c) for c in wQ])),
        unliftable_coefficients=unl,
        WARNING=('COMPLETE' if unl == 0 else
                 'INCOMPLETE: %d coefficients could not be lifted to Q with the '
                 'prime set used; add primes to nsweep.PRIMES and re-run' % unl),
        blocks=payload)
    fn = os.path.join(HERE, 'CERT_wstar_sparse.json')
    json.dump(doc, open(fn, 'w'))
    print('written %s (%.1f MB)' % (fn, os.path.getsize(fn) / 1e6))
    # plain-text rendering
    with open(os.path.join(HERE, 'CERT_wstar_sparse.txt'), 'w') as f:
        for k in sorted(payload):
            f.write('### %s\n' % k)
            for (a, b), dd, iv in payload[k]['columns']:
                f.write('  k^%d l^%d  /  %s :\n' % (a, b, dd))
                for e, v in iv:
                    f.write('     n^%-3d %d\n' % (e, v))
    print('written CERT_wstar_sparse.txt')
