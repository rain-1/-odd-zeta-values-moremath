"""Filter hunt hits: keep only those whose ACTUAL nonzero support keeps every form in [0,n]."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hunt import hunt, show, value, ev, PAR
labs = sys.argv[1].split(',')
for lab in labs:
    hits = hunt(lab, verbose=False)
    seen = set()
    good = []
    for m, cand in hits:
        sg, e, pairs = cand
        forms = set()
        for (T, B) in pairs:
            forms.add(T); forms.add(B)
            forms.add(('d', T[1]-B[1], T[2]-B[2]))
        if e is not None:
            forms.add(('e', 1, -e[2]))
        ok = True
        for n in range(6, 25):
            for k in range(n + 1):
                if value(cand, n, k) == 0:
                    continue
                for f in forms:
                    x = ev(f, n, k)
                    if x < 0 or x > n:
                        ok = False; break
                if not ok: break
            if not ok: break
        s = show(cand)
        if ok and s not in seen:
            seen.add(s); good.append((m, s))
    print('=== %s : %d raw hits, %d GENUINELY TAME (distinct)' % (lab, len(hits), len(good)))
    for m, s in good:
        print('    m=%d  %s' % (m, s))
