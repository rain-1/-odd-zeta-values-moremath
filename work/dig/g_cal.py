"""g_cal.py -- archimedean calibration: how much does the smallness/budget ratio
degrade when we leave the totally symmetric point to buy group savings?

C_0 = -f_0(tau_0), C_1 = Re f_0(tau_1)   (Zudilin llm/04 Lemma 12)
tau_0 < tau_1 the real zeros of prod(tau-alpha_j) - prod(tau-beta_k).
"""
import numpy as np
from cmath import log as clog
def log(z):
    return clog(z)
from g_group import m_params, delta_limit, admissible

def f0(alpha, beta, tau):
    a = alpha; b = beta
    v = 0j
    for x in a: v += x*log(x-tau)
    v -= b[0]*log(tau-b[0]) if b[0] != 0 else 0j
    v -= b[1]*log(tau-b[1])
    v -= b[2]*log(b[2]-tau); v -= b[3]*log(b[3]-tau)
    v -= (a[0]-b[0])*log(a[0]-b[0]); v -= (a[1]-b[1])*log(a[1]-b[1])
    v += (b[2]-a[2])*log(b[2]-a[2]); v += (b[3]-a[3])*log(b[3]-a[3])
    return v.real

def taus(alpha, beta):
    pa = np.poly(alpha); pb = np.poly(beta)
    r = np.roots(pa - pb)
    r = sorted(float(x.real) for x in r if abs(x.imag) < 1e-9)
    return r

def report(alpha, beta, label):
    t = taus(alpha, beta)
    a = sorted(alpha); b = sorted(beta)
    cand = [x for x in t if b[1] < x < a[0]]
    hi = [x for x in t if x > a[3]]
    if not cand or not hi:
        print(f"  {label}: no admissible saddle ({t})"); return
    C0 = -f0(alpha, beta, cand[0]); C1 = f0(alpha, beta, hi[-1])
    m0,m1,m2,m3 = m_params(alpha,beta); bud = 2*m1+m2
    d,_,_ = delta_limit(alpha,beta)
    C2 = bud - d
    print(f"  {label}: alpha={alpha} beta={beta}")
    print(f"     tau0={cand[0]:.8f} C0={C0:.8f}  tau1={hi[-1]:.8f} C1={C1:.8f}")
    print(f"     budget={bud} delta={d:.6f} (ratio {d/bud:.6f})  C2={C2:.6f}")
    print(f"     C0/budget = {C0/bud:.6f};  margin/budget = {(C0-C2)/bud:.6f}")
    if C0 > C2: print(f"     mu <= {(C0+C1)/(C0-C2):.8f}")

if __name__ == "__main__":
    print("[cal] Apery/Ball symmetric point")
    report((1,1,1,1),(0,0,2,2),"symmetric")
    print("[cal] Rhin-Viola optimum  (anchor: C0=47.15472079, C1=48.46940964, mu=5.51389062)")
    report((18,17,16,19),(0,7,31,32),"RV")
    print("[cal] best-ratio point found by g_opt")
    report((4,7,8,11),(0,3,13,14),"best-delta-ratio")
    report((11,8,7,4),(0,3,13,14),"best (relabelled)")
    report((2,7,8,9),(0,1,12,13),"2nd")
