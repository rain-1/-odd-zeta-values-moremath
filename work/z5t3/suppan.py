"""suppan.py -- analyse the family composition of a folded+MT solution."""
import sys, pickle
import numpy as np
from collections import Counter

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5t3')

P = int(sys.argv[sys.argv.index('-p') + 1]) if '-p' in sys.argv else 4194301
NS = int(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith('-') else 25

x = np.load('mt26_x_%d_n%d.npy' % (P, NS))
meta = pickle.load(open('live3_blocks_n20.pkl', 'rb'))
base_names = meta['names']
import momtow as MT
spec = MT.mom_columns_spec()
names = base_names + [s[0] for s in spec]
assert len(names) == len(x), (len(names), len(x))
nz = [i for i in range(len(x)) if x[i] % P]
fam = Counter()
for i in nz:
    nm = names[i]
    fam[nm.split('/')[0].split('[')[0]] += 1
print('support size:', len(nz))
print('by family:', dict(fam.most_common()))
mtuse = [i for i in nz if i >= len(base_names)]
print('MT columns used:', len(mtuse), 'of', len(spec))
