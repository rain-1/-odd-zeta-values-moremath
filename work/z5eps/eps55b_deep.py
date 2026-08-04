"""eps55b_deep.py -- factory pass 2: raised caps (sumabs<=60, 24 t-cands,
48 F-cands/weight) so the sweep reaches the region where the known large
eta-vectors live (gamma/alpha/delta/eta have sum|e| = 48..60).  Dedupe against
pass-1 hits and the fifteen; classify any genuinely new hit exactly."""

import time, json
import numpy as np
import eps55_factory as X

def main():
    t0 = time.time()
    known_fp = {}
    for nm in list(X.R2) + list(X.R3):
        known_fp[X.fingerprint(X.known_seq(nm, 14))] = nm
    seen = set(known_fp)
    # seed with pass-1 catalog fingerprints (recompute quickly from json)
    hits = []
    stats = {}
    for N, divs in sorted(X.LEVELS.items()):
        cap = 24 if len(divs) <= 3 else 10
        tc = X.enum_evecs(divs, 0, 24, cap, 60, 24)
        fb = []
        for w in (1, 2):
            for ev in X.enum_evecs(divs, 2 * w, 0, cap, 60, 48):
                fb.append(('eta%s' % (sorted(ev.items()),), w,
                           X.eprod_p(ev, X.QS), ('eta', ev)))
        for nm, w, ser in X.eis_bank_fr(divs, X.QS):
            fb.append((nm, w, X.fr_to_p(ser), ('eis', nm)))
        npairs = nhit = 0
        for te in tc:
            Tp_ = np.concatenate([[0], X.eprod_p(te, X.QS - 1)])
            for (fn, w, Fp_, fref) in fb:
                for tw in (1, -1):
                    npairs += 1
                    if tw == 1:
                        Ts, Fs = Tp_, Fp_
                    else:
                        Ts = np.array([int(x) if i % 2 else (-int(x)) % X.P
                                       for i, x in enumerate(Tp_)],
                                      dtype=np.int64)
                        Fs = np.array([int(x) if i % 2 == 0 else
                                       (-int(x)) % X.P
                                       for i, x in enumerate(Fp_)],
                                      dtype=np.int64)
                    q = X.revert_p(Ts, X.QS)
                    a = X.compose_p(Fs, q, X.QS)
                    dim = X.fit_3term_p(a)
                    if dim == 0:
                        continue
                    fp = X.fingerprint(a)
                    if fp in seen:
                        continue
                    seen.add(fp)
                    nhit += 1
                    hits.append({'level': N, 't': te, 'fname': fn,
                                 'fref': fref, 'w': w, 'twist': tw,
                                 'dim': dim, 'known': known_fp.get(fp)})
        stats[N] = (npairs, nhit)
        print('  level %-3d: %6d pairs, %3d distinct hits (%.0fs)'
              % (N, npairs, nhit, time.time() - t0), flush=True)

    print('\npass-2 distinct hits: %d -- classifying exactly' % len(hits),
          flush=True)
    results = []
    from fractions import Fraction as Fr
    for h in hits:
        T = [0] + X.eprod_i(h['t'], X.QE - 1)
        kind, ref = h['fref']
        if kind == 'eta':
            Fq = X.eprod_i(ref, X.QE)
        else:
            Fq = None
            for nm, w, ser in X.eis_bank_fr(X.LEVELS[h['level']], X.QE):
                if nm == ref:
                    if all(x.denominator == 1 for x in ser):
                        Fq = [int(x) for x in ser]
        if Fq is None:
            continue
        if h['twist'] == -1:
            T = X.twist_t(T)
            Fq = X.twist_f(Fq)
        a = X.compose_i(Fq, X.revert_i(T, X.QE), X.QE)
        shp, prm = X.shape_match_exact(a)
        results.append({**h, 'fref': str(h['fref']), 'shape': shp,
                        'params': prm, 'a_start': a[:7]})
        tag = 'KNOWN=%s' % h['known'] if h['known'] else (
            'shape %s%s' % (shp, prm) if shp else 'no-integer-shape')
        print('  level=%d twist=%d %s  a=%s' % (h['level'], h['twist'],
              tag, a[:6]), flush=True)
    with open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps/'
              'eps55b_pass2.json', 'w') as fh:
        json.dump({'stats': {str(k): v for k, v in stats.items()},
                   'hits': [{k: str(v) for k, v in e.items()}
                            for e in results]}, fh, indent=1)
    print('saved eps55b_pass2.json (%.0fs)' % (time.time() - t0))

if __name__ == '__main__':
    main()
