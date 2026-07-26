import sys, pickle
from math import comb
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import core
from eps5 import Pipe

p = 2147483647
pi = Pipe(p)
NCH = 8

# brute force per cell
HM = 3*NCH+2
H = [[0]*(HM+1) for _ in range(6)]
for m in range(1, HM+1):
    im = pow(m, p-2, p); acc = im
    H[1][m] = (H[1][m-1]+acc) % p
    for r in range(2,6):
        acc = acc*im % p
        H[r][m] = (H[r][m-1]+acc) % p

for n in range(NCH+1):
    colbf = 0        # SigmaT * 2Psi * (H2_{n+k}-H2_{n+l})
    w3sum = 0        # SigmaT * w3sym
    m3c2 = 0         # SigmaT * (H3_{n+k}+H3_{n+l})
    for k in range(n+1):
        for l in range(n+1):
            t = (comb(n+k,n)*comb(n,k)**2*comb(n+l,n)*comb(n,l)**2*comb(n+k+l,n)) % p
            U1 = (H[1][k]-H[1][l]) % p
            U2 = (H[1][n+k]-H[1][n+l]) % p
            U3 = (H[1][n-k]-H[1][n-l]) % p
            twoPsi = (-3*U1 + U2 + 2*U3) % p
            W2 = (H[2][n+k]-H[2][n+l]) % p
            colbf = (colbf + t*twoPsi%p*W2) % p
            m3c2 = (m3c2 + t*((H[3][n+k]+H[3][n+l])%p)) % p
            i2 = pow(2, p-2, p); i4 = pow(4, p-2, p)
            w3s = (i2*(H[3][n+k]+H[3][n+l]) - i2*twoPsi%p*i2%p*W2) % p
            w3sum = (w3sum + t*w3s) % p
    # tensor route
    e9 = [0]*9; e9[7] = 1     # w2 pair n+k is index 6+1 = 7
    coltn = pi.momH([[0,0,-3,1,2]], 2, e9)[n]
    m3tn = pi.momH([], 3, [0,0,1,0,0,0,0,0,0])[n]
    ph = pi.Ph[n]
    i2 = pow(2, p-2, p); i4 = pow(4, p-2, p)
    lin = (i2*m3c2 - i4*colbf - ph) % p
    print('n=%d  colbf==coltn: %s   m3 ok: %s   w3sum==Ph: %s   kernel lin comb == 0: %s'
          % (n, colbf==coltn, m3c2==m3tn, w3sum==ph, lin==0))
