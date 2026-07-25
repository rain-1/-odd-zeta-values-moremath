"""T2: numerical ledger for the middle-row descent  p^3 Phat_{ap+r} = Phat_a Q_r (mod p).

Objects (all exact Fractions):
  v(n,k,l) = w3hat(n,k,l) - H^(3)_n        (the "W-part" weight)
  What_n   = Phat_n - H3(n) Q_n = sum_{k,l} T(n,k,l) v(n,k,l)
  T_hi(a,b,c) = C(a+b,a)C(a,b)^2 C(a+c,a)C(a,c)^2 C(a+b+c,a)   ( = T(a,b,c) )
  T_lo(r,s,t) = C(r+s,r)C(r,s)^2 C(r+t,r)C(r,t)^2 C(r+s+t,r)   ( = T(r,s,t) )

Checks:
  (L1) termwise:  v_p( p^3 T(n,k,l) v(n,k,l) - T(n,k,l) v(a,b,c) ) >= 1   for all k,l
  (L2) termwise:  v_p( p^3 T(n,k,l) v(n,k,l) - T_hi(a,b,c)T_lo(r,s,t) v(a,b,c) ) >= 1
  (L3) summed:    v_p( sum_{b,c} v(a,b,c) [ Tcal(b,c) - Q_r T_hi(a,b,c) ] ) >= 1
                  where Tcal(b,c) = sum_{s,t} T(n,bp+s,cp+t)
"""
from core import T, Hs, w3hat, Q, Ph, vp
from fractions import Fraction as F
import sys

def v_weight(n, k, l):
    return w3hat(n, k, l) - Hs(n, 3)

def run(p, verbose=False):
    res = {'L1': [], 'L2': [], 'L3': [], 'L1min': 99, 'L2min': 99, 'L3min': 99}
    for a in range(1, p):
        va_int = vp(Ph(a), p) >= 0
        for r in range(p):
            n = a * p + r
            if n > 360:
                continue
            Qr = Q(r)
            # level-a data
            vA = {(b, c): v_weight(a, b, c) for b in range(a + 1) for c in range(a + 1)}
            Thi = {(b, c): T(a, b, c) for b in range(a + 1) for c in range(a + 1)}
            m1 = m2 = 99
            Tcal = {}
            for b in range(a + 1):
                for c in range(a + 1):
                    acc = 0
                    for s in range(p):
                        k = b * p + s
                        if k > n: continue
                        for t in range(p):
                            l = c * p + t
                            if l > n: continue
                            Tn = T(n, k, l)
                            acc += Tn
                            S1 = p**3 * Tn * v_weight(n, k, l)
                            S2a = Tn * vA[(b, c)]
                            Tlo = T(r, s, t) if (s <= r and t <= r) else 0
                            S2b = Thi[(b, c)] * Tlo * vA[(b, c)]
                            m1 = min(m1, vp(S1 - S2a, p))
                            m2 = min(m2, vp(S1 - S2b, p))
                    Tcal[(b, c)] = acc
            tot = sum(vA[(b, c)] * (Tcal[(b, c)] - Qr * Thi[(b, c)])
                      for b in range(a + 1) for c in range(a + 1))
            m3 = vp(tot, p)
            res['L1'].append((a, r, m1)); res['L2'].append((a, r, m2)); res['L3'].append((a, r, m3, va_int))
            res['L1min'] = min(res['L1min'], m1); res['L2min'] = min(res['L2min'], m2)
            res['L3min'] = min(res['L3min'], m3)
    return res

if __name__ == '__main__':
    for p in [int(x) for x in sys.argv[1:]] or [5, 7, 11]:
        r = run(p)
        bad1 = [x for x in r['L1'] if x[2] < 1]
        bad2 = [x for x in r['L2'] if x[2] < 1]
        bad3 = [x for x in r['L3'] if x[2] < 1]
        bad3g = [x for x in bad3 if x[3]]
        print('p=%d  L1min=%s (#fail %d)  L2min=%s (#fail %d)  L3min=%s (#fail %d, of which Phat_a integral: %d)'
              % (p, r['L1min'], len(bad1), r['L2min'], len(bad2), r['L3min'], len(bad3), len(bad3g)), flush=True)
        if bad1[:3]: print('   L1 fails:', bad1[:5])
        if bad2[:3]: print('   L2 fails:', bad2[:5])
        if bad3g[:3]: print('   L3 fails (Phat_a integral):', bad3g[:5])
