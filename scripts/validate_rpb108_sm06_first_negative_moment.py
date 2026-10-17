#!/usr/bin/env python3
"""SM06: supported original odd A^-1 three-source upper, with full pole/packet cross terms.

This is a coupled operator certificate for the pole, the true negative-band
Jensen mean, and its orthogonal first Legendre frequency moment.
It is NOT positivity after subtraction of the full negative-frequency K.
All acceptances are exact Fraction inequalities. Approximate rational
trial witnesses select bounds, they do not certify acceptance.
"""
from fractions import Fraction as F
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES as SI29
from validate_rpb108_si21_odd_jensen_four import (
    B, PI, KAPPA, outward, midpoint, solve_exact
)
from validate_rpb108_si13_odd_fourier_reference import arch_lower
from validate_rpb108_si06_negative_band import prime_interval
from validate_rpb108_si25_first_moment_bessel import (
    linear_interval, bilinear_interval
)
from validate_rpb108_si12_even_supported_inverse import sinh_bounds
from validate_rpb108_sm06_band_legendre_tail import validate as certify_constant_band_tail
from validate_rpb108_sm03_negative_packet_reference_nogo import (
    C as NEG_CENTER, RADIUS as NEG_RADIUS, DELTA as NEG_DELTA
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
MOM_GAMMA=NEG_GAMMA/F(3)
MOM_PANELS=16
# Rational upper bounds for sqrt(weight_i*weight_j), used only in
# Gershgorin absolute row sums, not approximating the true source.
CROSS_01=F(29,50)    # sqrt(2*21/125)<0.58
CROSS_02=F(67,200)   # sqrt(2*7/125)<0.335
CROSS_12=F(97,1000) # sqrt((21/125)*(7/125))<0.097

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

def composite_moment_terms(c,r,panels):
    """Quadrature for true g1=3 E[u sin(2*pi*(c+r*u)*x)].

    These *signed* Simpson nodes are enclosures only. The operator
    Bessel/Legendre identity is exact before quadrature.
    """
    assert panels%2==0 and panels>=2
    out=[]
    for k in range(panels+1):
        u=F(-1)+2*F(k,panels)
        coef=1 if k in (0,panels) else (4 if k%2 else 2)
        out.append((c+r*u,F(coef*u,panels)))
    assert sum((wt for _,wt in out),F(0))==0
    return tuple(out)

def moment_simpson_error(radius,panels):
    beta=2*PI[1]*radius*B
    # The derivative of 3u*sin(2*pi*(c+ru)*x) has
    # fourth absolute bound 3*(4 beta^3+beta^4).
    return 3*(4*beta**3+beta**4)/F(180)*(F(2,panels)**4)

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

    # OLD true mean windows inherit the exact whole-interval original
    # seven-prime signed certifications in SI21/23/28/29, replayed in
    # their independent historical validators. This test explicitly pins
    # their names, widths and disjointness without rerunning 900 cells.
    assert len(OLD)==9
    assert OLD[0][0]==F(3,10) and OLD[4][0]==F(1,4)
    assert OLD[6][0]==F(21,10) and OLD[7][0]==F(58,25)
    assert OLD[8][0]==F(17,5)

    # NEW: check the *entire* original signed multiplier continuously
    # with rational 16-cell arch-lower + signed prime derivative bounds.
    # The old SI28 routine used 128 cells; margins here are broad enough
    # that 16 cells also certify strict positivity on every real point.
    cells=16
    for c,r,d,_ in NEW:
        for i in range(cells):
            lo=c-r+2*r*i/cells
            hi=c-r+2*r*(i+1)/cells
            mid=(lo+hi)/2
            certified=arch_lower(lo)+prime_interval(mid)[0]-F(69,2)*(hi-lo)
            assert certified>KAPPA+d,(c,i,float(certified),float(KAPPA+d))
    # SM03's full ORIGINAL signed negative band was already certified
    # with 128 independent subcells and remains a required prior.
    assert (NEG_CENTER,NEG_RADIUS,NEG_DELTA)==(F(147,40),F(3,100),F(7,5))
    assert NEG_GAMMA==F(21,125)
    assert MOM_GAMMA==F(7,125)
    assert CROSS_01**2>2*NEG_GAMMA
    assert CROSS_02**2>2*MOM_GAMMA
    assert CROSS_12**2>NEG_GAMMA*MOM_GAMMA

def intervals():
    tau=[simpson_error(r,POS_PANELS) for c,r,d,deg in FEATURES]
    gamma=[4*r*d for c,r,d,deg in FEATURES]
    terms=[composite_mean_terms(c,r,POS_PANELS)
           for c,r,d,deg in FEATURES]
    neg_terms=composite_mean_terms(NEG_CENTER,NEG_RADIUS,NEG_PANELS)
    neg_tau=simpson_error(NEG_RADIUS,NEG_PANELS)
    moment_terms=composite_moment_terms(NEG_CENTER,NEG_RADIUS,MOM_PANELS)
    moment_tau=moment_simpson_error(NEG_RADIUS,MOM_PANELS)
    assert max(tau)<F(1,10**5) and neg_tau<F(1,10**6)
    assert 0<moment_tau<F(1,10**6)
    assert all(t>0 for t in tau) and all(g>0 for g in gamma)

    # Q[i][j]=<true positive feature_i, source_j>.
    # j=0:s, j=1:odd negative Jensen mean, j=2:odd first moment.
    # Physically supported, preserving all off-diagonal signs.
    Q=[]
    for i in range(N):
        a,b=linear_interval(terms[i])
        qs=outward((a-F(3,4)*tau[i],
                    b+F(3,4)*tau[i]),15)
        a,b=bilinear_interval(terms[i],neg_terms)
        err=4*B*(tau[i]+neg_tau)
        qg=outward((a-err,b+err),15)
        a,b=bilinear_interval(terms[i],moment_terms)
        # Degree-one moment has pointwise amplitude ≤3/2. The
        # conservative physical perturbation 4B*(tau_i+moment_tau)
        # covers the true original support and quadrature errors.
        err=4*B*(tau[i]+moment_tau)
        qm=outward((a-err,b+err),15)
        Q.append([qs,qg,qm])
    print("SM06: complete 16x3 original physical supported source Gram enclosed",flush=True)

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
    print("SM06: full 16x16 true physical supported positive-reference Gram enclosed",flush=True)

    slo,shi=sinh_bounds(B)
    p00=outward((slo-B,shi-B),15)
    a,b=linear_interval(neg_terms)
    p01=outward((a-F(3,4)*neg_tau,b+F(3,4)*neg_tau),15)
    a,b=bilinear_interval(neg_terms,neg_terms)
    p11=outward((a-8*B*neg_tau,b+8*B*neg_tau),15)
    a,b=linear_interval(moment_terms)
    p02=outward((a-F(3,4)*moment_tau,b+F(3,4)*moment_tau),15)
    a,b=bilinear_interval(neg_terms,moment_terms)
    p12=outward((a-4*B*(neg_tau+moment_tau),
                 b+4*B*(neg_tau+moment_tau)),15)
    a,b=bilinear_interval(moment_terms,moment_terms)
    p22=outward((a-8*B*moment_tau,b+8*B*moment_tau),15)
    P=[[p00,p01,p02],[p01,p11,p12],[p02,p12,p22]]
    M=[[(h[0]/KAPPA+(1/gamma[i] if i==j else 0),
         h[1]/KAPPA+(1/gamma[i] if i==j else 0))
        for j,h in enumerate(H[i])] for i in range(N)]
    # True M>0 because actual H=G*G PSD and Γ^-1 strictly positive.
    return Q,M,P,neg_tau,moment_tau,max(tau)

def loewner_upper(Q,M,P):
    # Midpoint rational exact solve is a WITNESS ONLY. Final bound includes
    # signed full H and Q intervals and correct positive residual remainder.
    Mmid=[[midpoint(x) for x in row] for row in M]
    Z=[]
    for col in range(3):
        qcol=[midpoint(Q[i][col]) for i in range(N)]
        z=solve_exact(Mmid,qcol)
        # Rational witness rounded to limit final certificate arithmetic.
        unit=10**12
        z=[F((a*unit).numerator//(a*unit).denominator,unit) for a in z]
        Z.append(z)
    print("SM06: three 16-column rational inverse-response dual witnesses selected",flush=True)

    U=[[None]*3 for _ in range(3)]
    for j in range(3):
        for k in range(j,3):
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
    Q,M,P,neg_tau,moment_tau,maxtau=intervals()
    U=loewner_upper(Q,M,P)
    assert all(U[i][i][1]>0 for i in range(3))
    # The exact operator being tested is
    # A_o -2|s><s| -γ0|g0><g0| -γ1|g1><g1|.
    # U encloses the entries of an explicit LOEWNER MAJORANT for the
    # true inverse-response matrix; it does NOT generally enclose each
    # actual off-diagonal scalar entry. Gershgorin is applied to that
    # majorant and transported to the true BS matrix by Loewner order.
    off01=CROSS_01*abs_hi(U[0][1])
    off02=CROSS_02*abs_hi(U[0][2])
    off12=CROSS_12*abs_hi(U[1][2])
    row0=2*U[0][0][1]+off01+off02
    row1=NEG_GAMMA*U[1][1][1]+off01+off12
    row2=MOM_GAMMA*U[2][2][1]+off02+off12
    print("SM06: physical inverse-response intervals:",
          [[(float(lo),float(hi)) for lo,hi in row] for row in U],flush=True)
    print("SM06: original negative means/first-moment Bessel weights:",
          float(NEG_GAMMA),float(MOM_GAMMA),flush=True)
    print("SM06: positive/mean/moment Simpson uniform errors:",
          float(maxtau),float(neg_tau),float(moment_tau),flush=True)
    print("SM06: 3x3 weighted Birman-Schwinger Gershgorin ROW upper:",
          float(row0),float(row1),float(row2),flush=True)
    theta=max(row0,row1,row2)
    assert theta<F(993,1000), (
        "SM06 full constant-weight negative BAND margin not certified",
        float(row0),float(row1),float(row2))
    tail_eps=certify_constant_band_tail()
    # Since BS_max <= theta, the original positive support obeys
    # A_o-2ss* - gamma0*g0*g0* - gamma1*g1*g1*
    #    >= (1-theta)*A_o >= (1-theta)*kappa*I.
    # The exact complete delta-weighted higher Legendre continuum is
    # <=tail_eps*I, so this positive floor pays the WHOLE remainder.
    remaining_floor=(1-theta)*KAPPA-tail_eps
    assert remaining_floor>0
    print("SM06: after original full constant-weight negative BAND residual, certified L2 floor LOWER:",
          float(remaining_floor),flush=True)
    print("SM06 PASS: A_o dominates original odd pole + entire uniform delta=7/5 negative-frequency band",flush=True)
    print("SM06 leaves actual variable (kappa-m)-delta excess on band, other signed bands and entire W-ODD-NEG open",flush=True)

if __name__=="__main__":
    validate()
