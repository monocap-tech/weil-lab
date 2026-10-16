#!/usr/bin/env python3
"""SI27 — original signed independent high-frequency window, nine-feature inverse.

Add SI14's ENTIRE original signed m(xi)>kappa+1 frequency window
[2.19,2.23] to SI25's eight true physical Jensen/Bessel functions.
Exact Jensen Loewner, full signed 9x9 physical supported Gram, original odd
pole source overlaps and correct-sign rational Woodbury dual upper bound.
All accepting inequalities exact Fraction; no sample-only m positivity.
Not a full Weil, even the one-pole <1, or complete Birman–Schwinger proof.
"""
from fractions import Fraction as F
from validate_rpb108_si25_first_moment_bessel import (
    FEATURES as BASE_FEATURES, feature_terms, linear_interval, bilinear_interval,
    square_lo,
)
from validate_rpb108_si21_odd_jensen_four import (
    B, PI, KAPPA, outward, midpoint, solve_exact, variational_lower,
    certify_original_window,
)
from validate_rpb108_si13_odd_fourier_reference import certify_window
from validate_rpb108_si14_odd_multiband_nogo import certify_positive_window
from validate_rpb108_si12_even_supported_inverse import sinh_bounds

NEW_CENTER=F(221,100)
NEW_RADIUS=F(1,50)
NEW_DELTA=F(1)
FEATURES=BASE_FEATURES+((NEW_CENTER,NEW_RADIUS,NEW_DELTA,0),)

def square_low(interval):
    lo,hi=interval
    return min(lo*lo,hi*hi) if lo*hi>0 else F(0)

def certify():
    assert len(BASE_FEATURES)==8 and len(FEATURES)==9
    assert FEATURES[-1] == (F(221,100),F(1,50),F(1),0)
    old_windows=sorted({(c-r,c+r) for c,r,d,deg in BASE_FEATURES})
    new_window=(NEW_CENTER-NEW_RADIUS,NEW_CENTER+NEW_RADIUS)
    assert new_window==(F(219,100),F(223,100))
    assert all(r<new_window[0] or new_window[1]<l for l,r in old_windows)
    assert len(old_windows)==6

    # Original SI14 certified SIGNED multiplier, not a point sample.
    high_min=certify_positive_window(*new_window)
    assert high_min>KAPPA+NEW_DELTA
    old_minima=[certify_original_window(c,d)
                for c,r,d,deg in BASE_FEATURES[:4]]
    assert all(m>KAPPA+d
               for m,(c,r,d,deg) in zip(old_minima,BASE_FEATURES[:4]))
    si13_min=certify_window()
    assert si13_min>KAPPA+F(1399,1000)

    # True frequency averages g0=E[h] on the NEW band yield
    # 2 int_J |h_xi><h_xi| dxi >= 4r |g0><g0|,
    # by Jensen variance, with NO negative Taylor floor penalty.
    # Previous eight vectors retain their exact true SI25 definitions.
    gamma=[4*r*d/(3 if deg else 1) for c,r,d,deg in FEATURES]
    assert gamma[-1]==F(2,25) and all(g>0 for g in gamma)

    tau=[]
    for c,r,d,deg in FEATURES:
        beta=2*PI[1]*r*B
        if deg==0:
            t=beta**4/F(180)  # true normalized 1-panel Simpson
        else:
            # True 3 E[u h] on the two original SI23 outer bands.
            t=3*(4*beta**3+beta**4)/F(180)*F(1,4)**4
        tau.append(t)
    assert max(tau)<F(11,10**6)
    assert F(0)<tau[-1]<F(3,10**6)

    # Interval-enclose *genuine* physical nine-feature source and Gram.
    # Degree-0 ||g||_infty<=1, degree-1 ||g||_infty<=3/2;
    # sup norms and physical support yield conservative remainders:
    # source <=3tau/4; Gram <=4B(tau_i+tau_j).
    terms=[]
    q=[]
    for i,(c,r,d,deg) in enumerate(FEATURES):
        t=feature_terms(c,r,deg)
        terms.append(t)
        lo,hi=linear_interval(t)
        q.append(outward((lo-F(3,4)*tau[i],hi+F(3,4)*tau[i]),12))
    assert q[0][0]>0 and q[1][1]<0 and q[2][0]>0
    assert q[3][1]<0 and q[4][0]>0 and q[5][0]>0
    assert q[8][0]>F(7,100)

    H=[]
    for i in range(9):
        row=[]
        for j in range(9):
            lo,hi=bilinear_interval(terms[i],terms[j])
            err=4*B*(tau[i]+tau[j])
            row.append(outward((lo-err,hi+err),12))
        H.append(row)
    assert all(H[i][j]==H[j][i] for i in range(9) for j in range(9))

    # A_o >= C9 =kappa I+G Gamma G* on the ORIGINAL physical odd H.
    # Full signed physical H=G*G, q=G*s.
    # M=Gamma^-1+H/kappa>0 and exact-rational variational witness:
    # 2<s,A_o^-1s> <= 2( ||s||²/kappa - q*M^-1q/kappa²),
    # q*M^-1q >=2 z*q-z*Mz for ANY rational z.
    M=[[(lo/KAPPA+(1/gamma[i] if i==j else 0),
         hi/KAPPA+(1/gamma[i] if i==j else 0))
        for j,(lo,hi) in enumerate(H[i])] for i in range(9)]
    z=solve_exact([[midpoint(span) for span in row] for row in M],
                  [midpoint(span) for span in q])
    correction=variational_lower(q,M,z)
    assert correction>0
    Slo0,Shi0=sinh_bounds(B)
    Slo,Shi=Slo0-B,Shi0-B
    norm_upper=F(235648,10**6)
    assert Shi<norm_upper
    response_upper=2*(norm_upper/KAPPA-correction/KAPPA**2)
    assert F(0)<response_upper<F(2), (
        "SI27 independent high band failed original signed <2 gate",
        float(response_upper)
    )
    assert response_upper<F(13,6)  # SI25 is strictly weaker

    # Another valid, but distinct, ONE-VECTOR test for this C9 reference.
    C9_on_s_low=KAPPA*Slo+sum(
        (g*square_low(qi) for g,qi in zip(gamma,q)),F(0))
    pole_hi=2*Shi**2
    surplus=C9_on_s_low-pole_hi
    assert surplus>F(47,1000)
    ratio=pole_hi/C9_on_s_low
    assert F(0)<ratio<F(7,10)

    print("SI27 PASS: independent signed 2.21 frequency window supports rank-nine physical inverse")
    print("NEW whole-band [2.19,2.23] original signed m strict min:",float(high_min))
    print("SI13 full band signed min:",float(si13_min))
    print("four original SI21 signed minima:",*(float(t) for t in old_minima))
    print("nine physical feature centers:",*(float(x[0]) for x in FEATURES))
    print("nine positive coefficients:",*(float(t) for t in gamma))
    print("new true averaged feature uniform Simpson remainder:",float(tau[-1]))
    print("full signed nine physical source overlaps:",[(float(a),float(b)) for a,b in q])
    print("FULL original physical 9x9 signed Gram:",
          [[(float(a),float(b)) for a,b in row] for row in H])
    print("rational variational inverse witness:",[float(v) for v in z])
    print("certified original supported odd inverse UPPER:",float(response_upper))
    print("original nine-reference s-only quadratic surplus LOWER:",float(surplus))
    print("s-only Rayleigh ratio UPPER, not BS norm:",float(ratio))
    print("NO inverse threshold <=1, complete signed BS, Stage I, F4, Lean, RH")
if __name__=="__main__":
    certify()
