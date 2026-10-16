#!/usr/bin/env python3
"""SI24: exact rational rank-six supported Jensen inverse gate.

Keep SI21's four signed all-frequency positive windows and recover SI23's
two continuous-frequency outer intervals by exact Jensen/variance Loewner
rank-one minorants (not naive midpoint samples). Full original physically
supported 6x6 Gram and source overlaps, with all signs and rigorous Simpson
errors, feed a rational variational Woodbury certificate.

This is a valid upper bound for ONE original odd inverse scalar, not an
upper BS matrix norm, original inverse vector, Stage I, or RH.
"""
from fractions import Fraction as F

from validate_rpb108_si21_odd_jensen_four import (
    KAPPA, B, PI, CENTERS as BASE_CENTERS, RADIUS as BASE_RADIUS,
    DELTAS as BASE_DELTAS, certify_original_window,
    plus, scale, outward, midpoint, solve_exact, variational_lower,
)
from validate_rpb108_si13_odd_fourier_reference import certify_window
from validate_rpb108_si18_odd_rank_two_woodbury import (
    gram, signed_odd_overlap,
)
from validate_rpb108_si12_even_supported_inverse import sinh_bounds

OUTER_CENTERS = (F(1,4), F(7,20))  # .25, .35
OUTER_RADIUS = F(3,100)            # each width .06
OUTER_DELTA = F(1399,1000)
CENTERS = BASE_CENTERS + OUTER_CENTERS
RADII = (BASE_RADIUS,)*len(BASE_CENTERS) + (OUTER_RADIUS,)*2
DELTAS = BASE_DELTAS + (OUTER_DELTA,)*2

def simpson_terms(c, r):
    """Normalized Simpson quadrature only encloses the TRUE mean g_c,r."""
    return ((c-r, F(1,6)), (c, F(2,3)), (c+r, F(1,6)))

def ave_q(c, r):
    a=(F(0),F(0))
    for xi,wt in simpson_terms(c,r):
        a=plus(a,scale(wt,signed_odd_overlap(xi)))
    return a

def ave_h(c,r,d,t):
    a=(F(0),F(0))
    for xi,wi in simpson_terms(c,r):
        for z,wj in simpson_terms(d,t):
            a=plus(a,scale(wi*wj,gram(xi,z)))
    return a

def square_interval(span):
    lo,hi=span
    if lo<=0<=hi:
        return (F(0),max(lo*lo,hi*hi))
    return min(lo*lo,hi*hi),max(lo*lo,hi*hi)

def certify():
    assert len(CENTERS)==len(RADII)==len(DELTAS)==6
    assert CENTERS[:4]==BASE_CENTERS and RADII[:4]==(BASE_RADIUS,)*4
    # All six positive-frequency windows are pairwise disjoint up to
    # boundary points; thus their positive operator contributions can
    # be summed without double-counting the original multiplier.
    intervals=sorted((c-r,c+r) for c,r in zip(CENTERS,RADII))
    assert intervals == [
        (F(22,100),F(28,100)), (F(28,100),F(32,100)),
        (F(32,100),F(38,100)), (F(74,100),F(78,100)),
        (F(118,100),F(122,100)), (F(163,100),F(167,100))
    ]
    assert all(intervals[i][1]<=intervals[i+1][0]
               for i in range(5))

    minima=[certify_original_window(c,d)
            for c,d in zip(BASE_CENTERS,BASE_DELTAS)]
    assert len(minima)==4
    assert all(value>KAPPA+delta for value,delta in zip(minima,BASE_DELTAS))
    # Full signed original multiplier on [.22,.38] (entire, reflected)
    # is certified by SI13; its outer disjoint portions share this margin.
    si13_min=certify_window()
    assert si13_min>KAPPA+OUTER_DELTA

    # For J_j=[c_j-r_j,c_j+r_j] and true physical sine averages
    # g_j(x) = (2r_j)^-1 int_J sin(2*pi*xi*x) dxi,
    # Jensen variance proves EXACT operator Loewner
    #   A_o >= C6=kappa I+sum gamma_j |g_j><g_j|,
    #   gamma_j=4 r_j delta_j.
    # Each remainder T_J -4r |g><g| is PSD; no floor penalty.
    gammas=[4*r*d for r,d in zip(RADII,DELTAS)]
    assert all(g>0 for g in gammas)

    # Normalized Simpson uniform x in [-B,B]:
    # |g_j - (h_left+4h_mid+h_right)/6| <= tau_j.
    tau=[(4*PI[1]*r*B)**4/F(2880) for r in RADII]
    assert max(tau)<F(11,10**6)
    slo,shi=sinh_bounds(B)
    Slo,Shi=slo-B,shi-B
    S_up=F(235648,10**6)
    assert F(0)<Slo<Shi<S_up
    # ||s|| < 1/2, ||h|| <=sqrt(2B)<3/2. Hence
    # |<s,g_j>-<s,Simpson_j>| <=3/4*tau_j.
    # Every Gram entry error is <=2B*(tau_i+tau_j).
    qerr=[F(3,4)*t for t in tau]
    q=[]
    for i,(c,r) in enumerate(zip(CENTERS,RADII)):
        a,b=ave_q(c,r)
        q.append(outward((a-qerr[i],b+qerr[i]),12))
    assert q[0][0]>0 and q[1][1]<0 and q[2][0]>0 and q[3][1]<0
    assert q[4][0]>0 and q[5][0]>0

    H=[]
    for i,(c,r) in enumerate(zip(CENTERS,RADII)):
        row=[]
        for j,(d,t) in enumerate(zip(CENTERS,RADII)):
            a,b=ave_h(c,r,d,t)
            err=2*B*(tau[i]+tau[j])
            row.append(outward((a-err,b+err),12))
        H.append(row)
    for i in range(6):
        for j in range(6):
            assert H[i][j]==H[j][i],("interval Gram symmetry",i,j)

    # Correct-sign reference Woodbury:
    # M=Gamma^-1+H/kappa>0 since H is the TRUE physical Gram;
    # 2<s,A_o^-1s> <=2[||s||²/kappa-q^T M^-1 q/kappa²].
    M=[[(a/KAPPA+(1/gammas[i] if i==j else 0),
          b/KAPPA+(1/gammas[i] if i==j else 0))
        for j,(a,b) in enumerate(H[i])] for i in range(6)]
    Mmid=[[midpoint(t) for t in row] for row in M]
    qmid=[midpoint(t) for t in q]
    z=solve_exact(Mmid,qmid)
    # z midpoint solution merely chooses a rational test vector;
    # all accepting comparisons use outward ORIGINAL physical intervals.
    correction=variational_lower(q,M,z)
    assert correction>0
    upper=2*(S_up/KAPPA-correction/KAPPA**2)
    assert 0<upper<F(9,4),("six Jensen directions failed <2.25 gate",float(upper))
    assert upper<F(4)  # improves original SI21 strict upper

    # Independently check the original SI22 s-witness is removed even
    # by THIS FINITE six-Jensen minorant, not only SI23's continuum.
    C6_on_s_lo=KAPPA*Slo+sum((g*square_interval(qi)[0]
                             for g,qi in zip(gammas,q)),F(0))
    pole_hi=2*Shi*Shi
    s_surplus_lo=C6_on_s_lo-pole_hi
    assert s_surplus_lo>F(46,1000)
    s_rayleigh_hi=pole_hi/C6_on_s_lo
    assert 0<s_rayleigh_hi<F(71,100)

    print("SI24 PASS: exact-rational original signed rank-six Jensen supported inverse")
    print("six centers:",*(float(c) for c in CENTERS))
    print("six radii:",*(float(r) for r in RADII))
    print("four original all-frequency signed minima:",*(float(x) for x in minima))
    print("SI13 whole [.22,.38] signed minimum:",float(si13_min))
    print("six physical Simpson remainders:",*(float(x) for x in tau))
    print("full physical 6x6 Gram outward intervals:",
          [[(float(a),float(b)) for a,b in row] for row in H])
    print("six original signed source q intervals:",[(float(a),float(b)) for a,b in q])
    print("rational variational witness:",[float(x) for x in z])
    print("certified original supported odd inverse UPPER:",float(upper))
    print("C6 - negative pole on s strict quadratic LOWER:",float(s_surplus_lo))
    print("s-only Rayleigh quotient UPPER, NOT BS norm:",float(s_rayleigh_hi))
    print("NO rank-one pole threshold <=1; NO full K BS; NO Stage I/F4/Lean/RH")

if __name__=="__main__":
    certify()
