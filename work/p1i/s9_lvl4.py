"""Phase 8: Lemma DK at digit level L = 4 (and a couple of L = 3 controls), fast."""
import sys, collections
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1i')
from s4_carry import scan_n

JOBS = [(5, 625), (5, 626), (5, 630), (5, 700), (5, 1249), (5, 1250), (5, 1560),
        (5, 3000), (5, 3124), (7, 2401), (7, 2402), (7, 3000), (11, 1331)]
cnt = collections.Counter()
for p, n in JOBS:
    scan_n(p, n, cnt)
    print('   done p=%d n=%d  (off so far %d)' % (p, n, cnt['off']), flush=True)
print('levels =', len(JOBS))
print('   in-regime cells   = %d' % cnt['in'])
print('   off-regime cells  = %d' % cnt['off'])
for key in ('B0_FAIL', 'B1_FAIL', 'B2_FAIL', 'K1_FAIL', 'K2_FAIL', 'K2b_FAIL', 'KC_FAIL'):
    print('   %-22s %d   <-- must be 0' % (key, cnt.get(key, 0)))
print('   in-regime control failures of the same criterion: %d' % cnt.get('in_KC_fails', 0))
print('   exceptional (e4=1, b+c=p^L-1) hits: %d' % cnt.get('K2_excep_harmless', 0))
print('   off-regime slack, 5 = >=5:', {i: cnt.get('slack_%d' % i, 0) for i in range(6)})
