#!/usr/bin/env python3
"""SM05: supported original odd A^-1 two-source upper, with pole cross terms.

This is an operator theorem for ONE *genuine continuous negative-frequency*
Jensen packet plus the odd pole, not the full negative-frequency K.
All acceptances are exact Fraction inequalities. Approximate rational
trial witnesses select bounds, they do not certify acceptance.
"""
from fractions import Fraction as F
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES as SI29
from validate_rpb108_si28_leverage_two_bands import certify_original_continuum
from validate_rpb108_si21_odd_jensen_four import (
    B, PI, KAPPA, outward, midpoint, solve_exact,
    certify_original_window
)
from validate_rpb108_si13_odd_fourier_reference import certify_window
from validate_rpb108_si25_first_moment_bessel import (
    linear_interval, bilinear_interval
)
from validate_rpb108_si12_even_supported_inverse import sinh_bounds
from validate_rpb108_sm03_negative_packet_reference_nogo import (
    C as NEG_CENTER, RADIUS as NEG_RADIUS, DELTA as NEG_DELTA,
    certify_negative_band
)

# Old sign-positive ORIGINAL features: drop surplus first moments and
# retain nine means from the original SI29 fourteen-feature reference.
KEEP=(0,1,2,3,4,5,9,10,13)
OLD=tuple(SI29[i] for i in KEEP)
NEW=(
    (F(19,5), F(19,1000), F(7,10), 0),  # 3.80
    (F(13,4), F(19,1000), F(11,5), 0), # 3.25
    (F(69,20),F(19,1000), F(27,10),0),# 3.45
    (F(83,20),F(19,1000), F(1,2),0),  # 4.15
    (F(77,20),F(19,1000), F(12,5),0), # 3.85
    (F(93,20),F(19,1000), F(1,2),0),  # 4.65
    (F(5),    F(19,1000), F(6,5),0),  # 5.00
)
FEATURES=OLD+NEW
N=16
POS_PANELS=4
NEG_PANELS=8
NEG_GAMMA=4*NEG_RADIUS*NEG_DELTA
SQRT_TWO_GAMMA_UP=F(3,5)   # sqrt(2*21/125) < 3/5

def composite_mean_terms(c,r,panels):
    """True odd sine frequency average, Simpson used for enclosure only."""
    assert panels%2==0 and panels>=2
    out=[]
    for k in range(panels+1):
        u=F(-1)+2*F(k,panels)
        coef=1 if k in (0,panels) else (4 if k%2 else 2)
        out.append((c+r*u,F(coef,3*panels)))
    assert sum((weight for _,weight in out),F(0))==1
    return tuple(out)

def simpson_error(radius,panels):
    beta=2*PI[1]*radius*B
    return beta**4/F(180)*(F(2,panels)**4)

def mul_int(x,y):
    z=[a*b for a in x for b in y]
    return min(z),max(z)

def scale_int(s,x):
    return (s*x[0],s*x[1]) if s>=0 else (s*x[1],s*x[0])

def add_int(x,y):
    return x[0]+y[0],x[1]+y[1]

def neg_int(x):
    return -x[1],-x[0]

def sub_int(x,y):
    return add_int(x,neg_int(y))

def abs_hi(x):
    return max(abs(x[0]),abs(x[1]))

def signed_windows():
    assert len(OLD)==9 and len(NEW)==7 and len(FEATURES)==N
    old_intervals=sorted(set((c-r,c+r) for c,r,_,d in OLD))
    all_intervals=sorted((c-r,c+r) for c,r,_,_ in FEATURES)
    assert len(old_intervals)==9 and len(all_intervals)==N
    assert all(all_intervals[i][1]<=all_intervals[i+1][0]
               for i in range(N-1))
    assert all(deg==0 for _,_,_,deg in FEATURES)

    # Four earlier SI21 true original signed windows.
    assert all(certify_original_window(c,d)>KAPPA+d
               for c,r,d,deg in OLD[:4])
    # Two SI23 disjoint outer means (0.25 and 0.35) both included in
    # [0.22,0.38], with strict inherited signed SI13 lower.
    assert certify_window()>KAPPA+F(1399,1000)
    # Remaining three original SI28/SI29 windows, and all seven NEW.
    for c,r,d,_ in OLD[6:]+NEW:
        assert certify_original_continuum(c,r,d)>KAPPA+d
    assert certify_negative_band()<-NEG_DELTA
    assert NEG_GAMMA==F(21,125)
    assert SQRT_TWO_GAMMA_UP**2>2*NEG_GAMMA

def intervals():
    tau=[simpson_error(r,POS_PANELS) for c,r,d,deg in FEATURES]
    gamma=[4*r*d for c,r,d,deg in FEATURES]
    terms=[composite_mean_terms(c,r,POS_PANELS)
           for c,r,d,deg in FEATURES]
    neg_terms=composite_mean_terms(NEG_CENTER,NEG_RADIUS,NEG_PANELS)
    neg_tau=simpson_error(NEG_RADIUS,NEG_PANELS)
    assert max(tau)<F(1,10**5) and neg_tau<F(1,10**6)
    assert all(t>0 for t in tau) and all(g>0 for g in gamma)

    # Q[i][j]=<true positive feature_i, source_j> (j=0:s,1:g_minus).
    # Physically supported, preserving all off-diagonal signs.
    Q=[]
    for i in range(N):
        a,b=linear_interval(terms[i])
        qs=outward((a-F(3,4)*tau[i],
                    b+F(3,4)*tau[i]),15)
        a,b=bilinear_interval(terms[i],neg_terms)
        err=4*B*(tau[i]+neg_tau)
        qg=outward((a-err,b+err),15)
        Q.append([qs,qg])
    print("SM05: complete 16x2 original physical supported source Gram enclosed",flush=True)

    H=[]
    for i in range(N):
        row=[]
        for j in range(i,N):
            a,b=bilinear_interval(terms[i],terms[j])
            err=4*B*(tau[i]+tau[j])
            row.append(outward((a-err,b+err),15))
        H.append(row)
    # Build correct symmetric physical Gram (no independent re-enclosure).
    H=[[H[i][j-i] if j>=i else H[j][i-j]
        for j in range(N)] for i in range(N)]
    assert all(H[i][j]==H[j][i]
               for i in range(N) for j in range(N))
    print("SM05: full 16x16 true physical supported positive-reference Gram enclosed",flush=True)

    slo,shi=sinh_bounds(B)
    p00=outward((slo-B,shi-B),15)
    a,b=linear_interval(neg_terms)
    p01=outward((a-F(3,4)*neg_tau,b+F(3,4)*neg_tau),15)
    a,b=bilinear_interval(neg_terms,neg_terms)
    p11=outward((a-8*B*neg_tau,b+8*B*neg_tau),15)
    P=[[p00,p01],[p01,p11]]
    M=[[(h[0]/KAPPA+(1/gamma[i] if i==j else 0),
         h[1]/KAPPA+(1/gamma[i] if i==j else 0))
        for j,h in enumerate(H[i])] for i in range(N)]
    # True M>0 because actual H=G*G PSD and Γ^-1 strictly positive.
    return Q,M,P,neg_tau,max(tau)

def loewner_upper(Q,M,P):
    # Midpoint rational exact solve is a WITNESS ONLY. Final bound includes
    # signed full H and Q intervals and correct positive residual remainder.
    Mmid=[[midpoint(x) for x in row] for row in M]
    Z=[]
    for col in (0,1):
        qcol=[midpoint(Q[i][col]) for i in range(N)]
        z=solve_exact(Mmid,qcol)
        # Rational witness rounded to limit final certificate arithmetic.
        unit=10**12
        z=[F((a*unit).numerator//(a*unit).denominator,unit) for a in z]
        Z.append(z)
    print("SM05: two 16-column rational inverse-response dual witnesses selected",flush=True)

    U=[[None]*2 for _ in range(2)]
    for j in range(2):
        for k in range(j,2):
            # P/κ - (Q*Z+Z*Q-Z*M*Z)/κ². This is an upper in Loewner,
            # not a lower: the true correction q*M^-1*q is >=
            # q*Z+Z*q-Z*M*Z by completion of squares.
            corr=(F(0),F(0))
            for i in range(N):
                corr=add_int(corr,scale_int(Z[k][i],Q[i][j]))
                corr=add_int(corr,scale_int(Z[j][i],Q[i][k]))
            for i in range(N):
                for h in range(N):
                    corr=sub_int(corr,scale_int(Z[j][i]*Z[k][h],M[i][h]))
            U[j][k]=outward(sub_int(scale_int(1/KAPPA,P[j][k]),
                                    scale_int(1/KAPPA**2,corr)),12)
            U[k][j]=U[j][k]
    return U

def validate():
    signed_windows()
    Q,M,P,neg_tau,maxtau=intervals()
    U=loewner_upper(Q,M,P)
    assert U[0][0][1]>0 and U[1][1][1]>0
    # B=(sqrt(2) s, sqrt(gamma) g_minus). Strict Gershgorin,
    # sqrt(2gamma)<0.6 rational envelope, all actual inverse cross
    # terms are contained in U[0][1].
    off=SQRT_TWO_GAMMA_UP*abs_hi(U[0][1])
    row0=2*U[0][0][1]+off
    row1=NEG_GAMMA*U[1][1][1]+off
    print("SM05: complete original physical inverse-response intervals:",
          [[(float(lo),float(hi)) for lo,hi in row] for row in U],flush=True)
    print("SM05: negative Jensen packet gamma:",float(NEG_GAMMA),flush=True)
    print("SM05: max true positive Simpson remainder:",float(maxtau),flush=True)
    print("SM05: negative packet Simpson remainder:",float(neg_tau),flush=True)
    print("SM05: pole/packet cross absolute UPPER:",float(abs_hi(U[0][1])),flush=True)
    print("SM05: weighted Birman-Schwinger row upper:",float(row0),float(row1),flush=True)
    assert row0<1 and row1<1, ("coupled original supported inverse gate FAILED",
                                float(row0),float(row1))
    print("SM05 PASS: A_o >= 2|s><s| + (21/125)|g_-><g_-| on the FULL physical odd carrier",flush=True)
    print("SM05 DOES NOT bound the residual K_freq - selected packet, W-ODD-NEG OPEN, RH OPEN.",flush=True)

if __name__=="__main__":
    validate()
