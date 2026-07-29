"""Direct one-shot certificate hunt for the Apery zeta(2) closed form.

Target: c_n := Sum_k S(n,k) w(n,k), S = C(n,k)^2 C(n+k,k),
        w = (1/5)[H2_n + H_k(2H_k - H_{n-k} - H_n)]
satisfies L c = 0, L u = (n+1)^2 u_{n+1} - (11n^2+11n+3) u_n - n^2 u_{n-1}.

One-shot: find Psi(n,k) = S(n,k) * sum_M psi_M(n,k) M(letters) with
LF(n,k) = Psi(n,k+1) - Psi(n,k) identically (interior), letters at (n,k):
h1=H_k h2=H_{n-k} h3=H_n h4=H_{n+k} s1=H2_k s2=H2_{n-k} s3=H2_n s4=H2_{n+k}.

Stage 1 (this file): assemble LF/S in the letter algebra at sample points,
GATE: reconstruct against direct values. Then mod-p solve for psi numerators.
"""
from fractions import Fraction as F
from math import comb
import itertools, sys

# ---------- letters & monomials ----------
H1 = {}; H2c = {}
def H(m):
    if m not in H1: H1[m] = sum(F(1,j) for j in range(1,m+1))
    return H1[m]
def H2(m):
    if m not in H2c: H2c[m] = sum(F(1,j*j) for j in range(1,m+1))
    return H2c[m]

LETTERS = ['h1','h2','h3','h4','s1','s2','s3','s4']
W = {'h1':1,'h2':1,'h3':1,'h4':1,'s1':2,'s2':2,'s3':2,'s4':2}
def letter_val(L,n,k):
    return {'h1':H(k),'h2':H(n-k),'h3':H(n),'h4':H(n+k),
            's1':H2(k),'s2':H2(n-k),'s3':H2(n),'s4':H2(n+k)}[L]

# monomial = tuple of letters sorted, weight<=2: (), (h,), (s,), (h,h)
MONOS = [()]
MONOS += [(l,) for l in LETTERS]
hs = ['h1','h2','h3','h4']
MONOS += [tuple(sorted((a,b))) for i,a in enumerate(hs) for b in hs[i:]]
MIDX = {m:i for i,m in enumerate(MONOS)}   # 1+8+10 = 19
def mono_val(m,n,k):
    v = F(1)
    for L in m: v *= letter_val(L,n,k)
    return v

# expression = dict mono -> Fraction
def emul(e1,e2):
    out={}
    for m1,c1 in e1.items():
        for m2,c2 in e2.items():
            m = tuple(sorted(m1+m2))
            assert sum(W[l] for l in m) <= 2, (m1,m2)
            out[m] = out.get(m,F(0)) + c1*c2
    return out
def eadd(*es):
    out={}
    for e in es:
        for m,c in e.items(): out[m]=out.get(m,F(0))+c
    return {m:c for m,c in out.items() if c!=0}
def escale(e,c): return {m:cc*c for m,cc in e.items()}

def shift_letter(L, n, k, dn, dk):
    """letter L at (n+dn, k+dk) as {(): rational, (L',): 1} in base letters at (n,k).
    Valid when all intermediate args stay >= the shift (interior cells)."""
    if L=='h1':  base='h1'; d = H(k+dk)-H(k)
    elif L=='h2': base='h2'; d = H(n+dn-k-dk)-H(n-k)
    elif L=='h3': base='h3'; d = H(n+dn)-H(n)
    elif L=='h4': base='h4'; d = H(n+dn+k+dk)-H(n+k)
    elif L=='s1': base='s1'; d = H2(k+dk)-H2(k)
    elif L=='s2': base='s2'; d = H2(n+dn-k-dk)-H2(n-k)
    elif L=='s3': base='s3'; d = H2(n+dn)-H2(n)
    elif L=='s4': base='s4'; d = H2(n+dn+k+dk)-H2(n+k)
    return {(): d, (base,): F(1)}

def shift_expr(e, n, k, dn, dk):
    out={}
    for m,c in e.items():
        term={(): c}
        for L in m:
            term = emul(term, shift_letter(L,n,k,dn,dk))
        out = eadd(out, term)
    return out

# ---------- the weight and summand ----------
def w_expr():
    # (1/5)[ s3 + h1*(2h1 - h2 - h3) ]
    h1={('h1',):F(1)}; e = eadd({('s3',):F(1)}, emul(h1, eadd(escale(h1,F(2)),
        {('h2',):F(-1)}, {('h3',):F(-1)})))
    return escale(e, F(1,5))
WEXPR = w_expr()

def S(n,k):
    if k<0 or k>n: return 0
    return comb(n,k)**2*comb(n+k,k)
def lam0(n): return 11*n*n+11*n+3

def w_val(n,k):
    return sum(c*mono_val(m,n,k) for m,c in WEXPR.items())

# sanity: c_n == B_n
def sanity():
    B=[F(0),F(1)]
    for n in range(1,30): B.append((lam0(n)*B[n]+n*n*B[n-1])/F((n+1)**2))
    ok = all(sum(S(n,k)*w_val(n,k) for k in range(n+1))==B[n] for n in range(30))
    print("sanity c_n == B_n (n<30):", ok)
    return ok

# ---------- LF/S in letter algebra at a point ----------
def LF_over_S(n,k):
    """(LF)(n,k)/S(n,k) as expression in base letters; interior 1<=k<=n-1 assumed."""
    rp = F((n+1)**2*S(n+1,k), S(n,k))        # c+ * S(n+1,k)/S(n,k)
    r0 = F(lam0(n))
    rm = F(n*n*S(n-1,k), S(n,k)) if k<=n-1 else F(0)
    wp = shift_expr(WEXPR, n, k, +1, 0)
    w0 = WEXPR
    wm = shift_expr(WEXPR, n, k, -1, 0)
    return eadd(escale(wp, rp), escale(w0, -r0), escale(wm, -rm))

def gate(npts=40, seed=3):
    import random
    random.seed(seed)
    pts=[]
    while len(pts)<npts:
        n=random.randint(4,20); k=random.randint(1,n-1); pts.append((n,k))
    bad=0
    for (n,k) in pts:
        e = LF_over_S(n,k)
        lhs = sum(c*mono_val(m,n,k) for m,c in e.items())*S(n,k)
        direct = (n+1)**2*S(n+1,k)*w_val(n+1,k) - lam0(n)*S(n,k)*w_val(n,k) \
                 - n*n*S(n-1,k)*w_val(n-1,k)
        if lhs != direct: bad+=1
    print("GATE LF letter-algebra vs direct:", "PASS" if bad==0 else f"FAIL {bad}/{npts}")
    return bad==0

if __name__=="__main__":
    ok = sanity() and gate()
    if not ok: sys.exit(1)
    # report which channels LF actually uses
    chans=set()
    for (n,k) in [(8,3),(11,5),(14,9)]:
        chans |= set(LF_over_S(n,k).keys())
    print("LF channels:", sorted(chans, key=lambda m:(len(m),m)))
