import sys, json, pickle
sys.set_int_max_str_digits(3000000)
from t1_towers import collect, fmod, tower_indices, branch_indices

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 125000
PRIMES = [5, 7, 11, 13]

jobs = []      # (label, p, [(s,n),...])
for p in PRIMES:
    for a in range(1, 13):
        t = tower_indices(p, NMAX, a)
        if len(t) >= 3: jobs.append(("tower a=%d" % a, p, t))
    # all-digits-(p-1) branch:  n_s = p^{s+1} - 1
    t = branch_indices(p, NMAX, p-1, [p-1]*40)
    if len(t) >= 3: jobs.append(("branch r=p-1 (n=p^{s+1}-1)", p, t))
    # a couple of mixed branches
    for rs, nm in [([1]*40, "branch r=1"), ([0,1,2,0,1,2,0,1,2,0,1,2], "branch r=012...")]:
        t = branch_indices(p, NMAX, 1, rs)
        if len(t) >= 3: jobs.append((nm, p, t))

want = set()
for _, p, t in jobs:
    for s, n in t: want.add(n)
print("indices needed: %d, max %d" % (len(want), max(want)), flush=True)
data = collect(NMAX+1, want)
print("recurrence done", flush=True)
pickle.dump({"NMAX": NMAX, "jobs": jobs,
             "data": {n: data[n] for n in want}},
            open("t1_data.pkl", "wb"))
print("saved")
