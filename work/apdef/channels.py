"""The three (a,c)-channels of the p^2 term, and the fact that the ac and c^2
channels are NOT rational identities -- they vanish only mod p, and only after the
borrow region s > r is included.  (See APERY_DEFECT sec.9, C2.)"""
from fractions import Fraction as F
from core import A, Hs


def channels(r):
    a2 = ac = cc = F(0)
    for s in range(r + 1):
        Ars = A(r, s); H = Hs
        u = H(r + s, 1) - H(r - s, 1)
        v = H(r + s, 1) + H(r - s, 1) - 2 * H(s, 1)
        a2 += Ars * (2 * u * u - (H(r + s, 2) - H(r - s, 2)))
        ac += Ars * (4 * u * v - 2 * (H(r + s, 2) + H(r - s, 2)))
        cc += Ars * (2 * v * v - (H(r + s, 2) - 2 * H(s, 2) + H(r - s, 2)))
    return a2, ac, cc


if __name__ == '__main__':
    print('%-4s %-26s %-22s %s' % ('r', 'a^2 channel', 'ac channel', 'c^2 channel'))
    for r in range(9):
        a2, ac, cc = channels(r)
        print('%-4d %-26s %-22s %s' % (r, a2, ac, cc))
    print('\nac == 0 for all r <= 30 :', all(channels(r)[1] == 0 for r in range(31)))
    print('cc == 0 for all r <= 30 :', all(channels(r)[2] == 0 for r in range(31)))
    print('=> not identities; the mod-p vanishing needs the borrow region.')
