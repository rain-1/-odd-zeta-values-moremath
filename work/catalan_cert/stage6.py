"""
Stage 6: symbolic completion with the fitted order-4 pre-operator, per parity.

p_i(n) are the fitted rational functions (fit_mod.py) cleared to polynomials by
multiplying the whole identity by the common denominator; p4 := that
denominator.  For each parity e=+1 (n even) / e=-1 (n odd), solve the five
remaining sectors symbolically and save the complete certificate.
"""
import sympy as sp
import pickle, os, sys

SP = os.path.dirname(os.path.abspath(__file__)) + '/'
src = open(SP + 'certificate.py').read()
exec(src.split("# ---------------------------------------------------------------- graded solve")[0])

st2 = pickle.load(open(SP + 'stage2_state.pkl', 'rb'))
ps, ORDER, certs2, = st2['ps'], st2['ORDER'], st2['certs']
combined = st2['combined']
assert ORDER == 4

Deven = (n + 3)*(n + 5)*(63*n**11 + 1068*n**10 + 7693*n**9 + 30420*n**8 + 69985*n**7
         + 85082*n**6 + 13016*n**5 - 125310*n**4 - 203061*n**3 - 152056*n**2
         - 56262*n - 7776)
PEVEN = [
 512*n**2*(n + 1)*(n + 2)**2*(n + 4)*(99*n**7 + 1596*n**6 + 10514*n**5 + 36326*n**4
    + 70194*n**3 + 74656*n**2 + 39628*n + 7824),
 64*(n + 2)*(n + 4)*(27*n**11 + 495*n**10 + 4008*n**9 + 19097*n**8 + 59049*n**7
    + 116550*n**6 + 112506*n**5 - 74640*n**4 - 383818*n**3 - 496676*n**2
    - 294212*n - 67200),
 -16*(n + 4)*(261*n**12 + 5502*n**11 + 50519*n**10 + 264388*n**9 + 864280*n**8
    + 1807654*n**7 + 2337854*n**6 + 1575586*n**5 + 972*n**4 - 844270*n**3
    - 554756*n**2 - 93908*n + 15744),
 -4*(n + 1)*(n + 3)*(n + 4)*(27*n**10 + 441*n**9 + 3108*n**8 + 11846*n**7 + 23201*n**6
    + 5418*n**5 - 87276*n**4 - 222233*n**3 - 261368*n**2 - 152766*n - 34272),
 Deven]

Dodd = (n + 2)*(n + 3)**2*(n + 4)**3*(n + 5)*(99*n**7 + 903*n**6 + 3017*n**5
        + 4231*n**4 + 1575*n**3 - 1249*n**2 - 719*n - 33)
PODD = [
 512*n*(n + 1)*(n + 3)*(63*n**11 + 1761*n**10 + 21838*n**9 + 158112*n**8
    + 739243*n**7 + 2326335*n**6 + 4964273*n**5 + 7009263*n**4 + 6065261*n**3
    + 2543209*n**2 - 81360*n - 337138),
 64*(n + 3)*(135*n**13 + 4338*n**12 + 62061*n**11 + 521037*n**10 + 2847129*n**9
    + 10605791*n**8 + 27376458*n**7 + 48621995*n**6 + 57278802*n**5
    + 40431978*n**4 + 11205595*n**3 - 5451298*n**2 - 5362192*n - 1341405),
 -16*(n + 2)*(n + 3)*(225*n**12 + 6279*n**11 + 77179*n**10 + 547668*n**9
    + 2465639*n**8 + 7260379*n**7 + 13788817*n**6 + 15625380*n**5 + 7852026*n**4
    - 2122290*n**3 - 3751963*n**2 - 533077*n + 302610),
 -4*(n + 2)*(n + 4)*(135*n**12 + 3933*n**11 + 50442*n**10 + 373449*n**9
    + 1757175*n**8 + 5441500*n**7 + 11053256*n**6 + 14039439*n**5 + 9552990*n**4
    + 1163579*n**3 - 2685200*n**2 - 1519929*n - 252345),
 Dodd]

def delta_of(cm, m):
    return eadd(escale(shift_element({m: cm}), r), {m: -cm})

results = {}
for EPS, PV in ((1, PEVEN), (-1, PODD)):
    # sanity: fitted ratios times cleared denominator are polynomials
    for i, p in enumerate(PV):
        assert sp.fraction(sp.cancel(sp.together(p)))[1] == 1, ('nonpoly', EPS, i)
    # residual with p substituted
    residual = {}
    for m, c in combined.items():
        cc = c
        for i in range(5):
            cc = cc.subs(ps[i], PV[i])
        residual[m] = sp.cancel(sp.together(cc.subs(e, EPS)))
    residual = {m: c for m, c in residual.items() if c != 0}
    cert = {}
    while residual:
        m = max(residual, key=lambda mm: (weight(mm), mm))
        g = residual.pop(m)
        diag = -1 if m[0] else 1
        phi = solve_first_order(diag, g, maxdeg_extra=10)
        assert phi is not None, ('OBSTRUCTION', EPS, m)
        cert[m] = phi
        contrib = delta_of(phi, m)
        chk = sp.cancel(contrib.pop(m) - g)
        assert chk == 0, ('diag mismatch', EPS, m)
        for mm, cc in contrib.items():
            residual[mm] = sp.cancel(residual.get(mm, 0) - cc.subs(e, EPS))
            if residual[mm] == 0:
                residual.pop(mm)
        print('parity %+d: solved sector %s' % (EPS, (m,)))
        sys.stdout.flush()
    # total certificate: weight-2 part sum_i PV[i]*certs2[i] + lower sectors
    tot = dict(cert)
    for i in range(5):
        for m, c in certs2[i].items():
            tot[m] = sp.cancel(tot.get(m, 0) + PV[i] * c.subs(e, EPS))
    results[EPS] = {'PV': PV, 'cert': tot}
    print('parity %+d COMPLETE (%d cofactors)' % (EPS, len(tot)))

pickle.dump(results, open(SP + 'final_certificate.pkl', 'wb'))
print('saved final_certificate.pkl')
