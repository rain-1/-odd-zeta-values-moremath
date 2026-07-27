"""check2.py -- null sanity for the new TX and EXTW families."""
import sys
sys.argv = ['check2.py']          # neutralise flag parsing in imports
import live2 as L2
from live2 import (tx_columns_spec, tx_col_val, extw_columns_spec,
                   extw_col_val, P, mq, hmod)
import evalq as E
import weights as W

lk, ll_, c2 = W.Lk(), W.Ll(), W.Cr(2)
txs = tx_columns_spec()
exs = extw_columns_spec()
print('TX columns:', len(txs), ' EXTW columns:', len(exs))
allbad = []
for n in (3, 4, 5):
    accT = [0] * len(txs)
    accE = [0] * len(exs)
    for k in range(n + 1):
        for l in range(n + 1):
            T = E.T(n, k, l) % P
            Lk = mq(E.el_val(lk, n, k, l))
            Ll = mq(E.el_val(ll_, n, k, l))
            C2 = mq(E.el_val(c2, n, k, l))
            DD = (Lk * Ll + P - C2) % P
            for i, (nm, spec) in enumerate(txs):
                a = tx_col_val(spec, n, k, l)
                accT[i] = (accT[i] + T * a) % P
            for i, (nm, spec) in enumerate(exs):
                a, b, d = extw_col_val(spec, n, k, l)
                accE[i] = (accE[i] + T * ((a + Lk * b + DD * d) % P)) % P
    bt = [txs[i][0] for i, v in enumerate(accT) if v % P]
    be = [exs[i][0] for i, v in enumerate(accE) if v % P]
    print('n=%d: TX bad %d/%d  EXTW bad %d/%d' % (n, len(bt), len(txs),
                                                  len(be), len(exs)))
    if bt: print('  TX bad:', bt[:8])
    if be: print('  EXTW bad:', be[:8])
    allbad += bt + be
print('NEWFAM NULLCHECK:', 'PASS' if not allbad else 'FAIL')
