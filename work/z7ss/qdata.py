"""Exact q_n data for the totally-symmetric M_{0,10} zeta(7) cellular integral."""
import re, os

QFILE = "/home/ubuntu/fable-episode-2/zeta-math/worthiness/zeta7_lc_terms.txt"


def load_q():
    q = {}
    with open(QFILE) as f:
        for line in f:
            m = re.match(r"q_(\d+)\s*=\s*(-?\d+)", line.strip())
            if m:
                q[int(m.group(1))] = int(m.group(2))
    return [q[i] for i in range(len(q))]


Q = load_q()

if __name__ == "__main__":
    print(len(Q), "values")
    print(Q[:4])
    print("q_73 digits:", len(str(Q[73])))
