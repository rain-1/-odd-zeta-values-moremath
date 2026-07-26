"""The four non-tame families, their summands and their KNOWN harmonic decompositions.

The decompositions are LBW_GENERAL's (verbatim from work/lbw/t4_proofcheck.py, which
reproduces LBW's published two-layer figures exactly).  Each has been re-validated here
(see selfcheck.py) against B(n) on held-out n with exact rational arithmetic.
"""
from fractions import Fraction as F
from math import comb

# ------------------------------------------------------------------ supports
def ks_all(n):
    return range(0, n + 1)


def ks_half(n):
    return range((n + 1) // 2, n + 1)


ARG = {'n': lambda n, k: n, 'k': lambda n, k: k, 'n-k': lambda n, k: n - k,
       'n+k': lambda n, k: n + k, '2k': lambda n, k: 2 * k,
       '2n-2k': lambda n, k: 2 * (n - k), '2k-n': lambda n, k: 2 * k - n}


def S_alpha(n, k):
    return comb(n, k) ** 2 * comb(2 * k, k) * comb(2 * (n - k), n - k)


def S_eps(n, k):
    return comb(n, k) ** 2 * (comb(2 * k, n) ** 2 if 2 * k >= n else 0)


def S_s7(n, k):
    return comb(n, k) ** 2 * comb(n + k, k) * (comb(2 * k, n) if 2 * k >= n else 0)


def S_E(n, k):
    return comb(n, k) * comb(2 * k, k) * comb(2 * (n - k), n - k)


# binomial factor lists (top, bot) for exact v_p by Kummer/Legendre
def BIN_alpha(n, k):
    return [(n, k), (n, k), (2 * k, k), (2 * (n - k), n - k)]


def BIN_eps(n, k):
    return [(n, k), (n, k), (2 * k, n), (2 * k, n)]


def BIN_s7(n, k):
    return [(n, k), (n, k), (n + k, k), (2 * k, n)]


def BIN_E(n, k):
    return [(n, k), (2 * k, k), (2 * (n - k), n - k)]


# ------------------------------------------------------------------ weights
# monomial = list of (kind, r, argname);  term = (Fraction c, monomial)

W_alpha = [
    (F(1, 4),   [('H', 1, 'k'), ('H', 1, '2k'), ('H', 1, '2k')]),
    (F(-1, 2),  [('H', 1, 'k'), ('H', 1, '2k'), ('H', 1, '2n-2k')]),
    (F(1, 4),   [('H', 1, 'k'), ('H', 1, '2n-2k'), ('H', 1, '2n-2k')]),
    (F(-1),     [('H', 1, 'k'), ('H', 1, 'k'), ('H', 1, '2k')]),
    (F(1),      [('H', 1, 'k'), ('H', 1, 'k'), ('H', 1, '2n-2k')]),
    (F(1),      [('H', 1, 'k'), ('H', 1, 'k'), ('H', 1, 'k')]),
    (F(-1),     [('H', 1, 'k'), ('H', 1, 'k'), ('H', 1, 'n-k')]),
    (F(-1, 4),  [('H', 2, '2k'), ('H', 1, 'k')]),
    (F(-1, 4),  [('H', 2, '2k'), ('H', 1, 'n-k')]),
    (F(-5, 12), [('H', 2, 'k'), ('H', 1, '2k')]),
    (F(5, 12),  [('H', 2, 'k'), ('H', 1, '2n-2k')]),
    (F(13, 12), [('H', 2, 'k'), ('H', 1, 'k')]),
    (F(-7, 12), [('H', 2, 'k'), ('H', 1, 'n-k')]),
    (F(7, 24),  [('H', 3, 'k')]),
]

W_eps = [
    (F(-1, 4),  [('H', 2, '2k'), ('H', 1, '2k')]),
    (F(1, 4),   [('H', 2, '2k'), ('H', 1, '2k-n')]),
    (F(1, 8),   [('H', 2, '2k'), ('H', 1, 'k')]),
    (F(-1, 8),  [('H', 2, '2k'), ('H', 1, 'n-k')]),
    (F(1, 16),  [('H', 2, 'k'), ('H', 1, '2k')]),
    (F(-1, 16), [('H', 2, 'k'), ('H', 1, '2k-n')]),
    (F(-1, 32), [('H', 2, 'k'), ('H', 1, 'k')]),
    (F(1, 32),  [('H', 2, 'k'), ('H', 1, 'n-k')]),
    (F(1, 4),   [('H', 3, '2k')]),
    (F(-1, 32), [('H', 3, 'k')]),
]

W_s7 = [
    (F(3, 14),  [('H', 1, 'k'), ('H', 1, '2k')]),
    (F(-9, 28), [('H', 1, 'k'), ('H', 1, 'k')]),
    (F(3, 7),   [('H', 1, 'k'), ('H', 1, 'n-k')]),
    (F(-3, 14), [('H', 1, 'n-k'), ('H', 1, '2k')]),
    (F(-3, 28), [('H', 1, 'n-k'), ('H', 1, 'n-k')]),
    (F(5, 28),  [('H', 2, 'k')]),
    (F(1, 14),  [('H', 2, 'n')]),
    (F(-3, 28), [('H', 2, 'n-k')]),
]

W_E = [
    (F(-1, 2), [('H', 1, '2k'), ('K', 1, '2k')]),
    (F(1, 2),  [('H', 1, '2k'), ('K', 1, '2n-2k')]),
    (F(3, 4),  [('H', 1, 'k'), ('K', 1, '2k')]),
    (F(-3, 4), [('H', 1, 'k'), ('K', 1, '2n-2k')]),
    (F(1, 2),  [('K', 2, '2k')]),
]


class Family:
    def __init__(self, label, w, D, e, ks, S, BIN, W, seqlabel, maxarg):
        self.label, self.w, self.D, self.e = label, w, D, e
        self.ks, self.S, self.BIN, self.W = ks, S, BIN, W
        self.seqlabel = seqlabel
        self.maxarg = maxarg          # y -> max argument value as a function of n

    @property
    def wantK(self):
        return any(kind == 'K' for _, mo in self.W for kind, _, _ in mo)


FAMS = {
    'alpha': Family('alpha', 3, 1,  0, ks_all,  S_alpha, BIN_alpha, W_alpha, 'alpha',
                    lambda n: 2 * n),
    'eps':   Family('eps',   3, 1,  0, ks_half, S_eps,   BIN_eps,   W_eps,   'eps',
                    lambda n: 2 * n),
    's7':    Family('s7',    2, 1,  0, ks_half, S_s7,    BIN_s7,    W_s7,    's7',
                    lambda n: 2 * n),
    'E':     Family('E',     2, -4, 1, ks_all,  S_E,     BIN_E,     W_E,     'E',
                    lambda n: 2 * n),
}

ORDER = ['alpha', 'eps', 's7', 'E']


def chi_of(D, m):
    if D == 1:
        return 1
    if D == -4:
        return 0 if m % 2 == 0 else (1 if m % 4 == 1 else -1)
    raise ValueError(D)
