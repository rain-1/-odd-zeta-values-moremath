"""Rational reconstruction in n of the joint (B-bot) certificate coefficients.

u is unique, so each Nu_t(n) is a well-defined element of Q(n).  Given values
mod p at many n, find (P_t, Q_t) with  Nu_t(n) Q_t(n) - P_t(n) = 0  for every
sampled n, minimising deg Q_t then deg P_t.  Rows must exceed columns by the
usual margin, and the fit is validated on n's HELD OUT of it.
"""
import pickle
import sys

import numpy as np

import bwz      # noqa: E402  (inserts work/z5star on sys.path)
import fastlin  # noqa: E402


def fit_one(vals, p, dp, dq, hold=6):
    """vals: {n: c mod p}.  Solve c(n)Q(n) = P(n), Q monic-normalised."""
    ns = sorted(vals)
    if len(ns) < dp + dq + 2 + hold:
        return None
    fit_ns, held = ns[:-hold], ns[-hold:]
    rows, rhs = [], []
    for n in fit_ns:
        c = vals[n] % p
        # unknowns: P_0..P_dp, Q_0..Q_{dq-1}   (Q_dq := 1)
        row = [(-pow(n % p, t, p)) % p for t in range(dp + 1)]
        row += [c * pow(n % p, t, p) % p for t in range(dq)]
        rows.append(row)
        rhs.append((-c * pow(n % p, dq, p)) % p)
    A = np.array(rows, dtype=np.int64) % p
    b = np.array(rhs, dtype=np.int64) % p
    if A.shape[0] < 1.3 * A.shape[1]:
        return None
    X, rk, piv, nbad = fastlin.solve(A, b, p)
    if nbad:
        return None
    P = [int(X[t]) % p for t in range(dp + 1)]
    Q = [int(X[dp + 1 + t]) % p for t in range(dq)] + [1]
    bad = 0
    for n in held:
        pv = sum(P[t] * pow(n % p, t, p) for t in range(dp + 1)) % p
        qv = sum(Q[t] * pow(n % p, t, p) for t in range(dq + 1)) % p
        if qv == 0 or (vals[n] * qv - pv) % p:
            bad += 1
    return (P, Q, bad, A.shape) if bad == 0 else None


def main(pkl=None, p=bwz.P1, dmax=14):
    pkl = pkl or ('bwz_lift_p%d.pkl' % p)
    data = pickle.load(open(pkl, 'rb'))
    print('reconstruction from %d values of n (%d..%d), p=%d'
          % (len(data), min(data), max(data), p))
    out = {}
    for t in range(13):
        vals = {n: v[t] for n, v in data.items()}
        if all(v == 0 for v in vals.values()):
            print('  Nu_%-2d : identically 0' % t)
            out[t] = ([0], [1])
            continue
        got = None
        for tot in range(0, 2 * dmax + 1):
            for dq in range(0, min(tot, dmax) + 1):
                dp = tot - dq
                if dp > dmax:
                    continue
                r = fit_one(vals, p, dp, dq)
                if r:
                    got = (dp, dq, r)
                    break
            if got:
                break
        if got:
            dp, dq, (P, Q, bad, shp) = got
            print('  Nu_%-2d : deg P = %-2d  deg Q = %-2d   rows=%d cols=%d  '
                  'held-out %d bad' % (t, dp, dq, shp[0], shp[1], bad))
            out[t] = (P, Q)
        else:
            print('  Nu_%-2d : NO rational fit with deg <= %d' % (t, dmax))
            out[t] = None
    pickle.dump(out, open('bwz_recon_p%d.pkl' % p, 'wb'))
    ok = all(v is not None for v in out.values())
    print('ALL COEFFICIENTS RECONSTRUCTED' if ok else
          'some coefficients need higher degree')
    return out


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
