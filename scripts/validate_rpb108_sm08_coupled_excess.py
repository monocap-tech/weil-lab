#!/usr/bin/env python3
"""SM08 candidate: exact five-source supported odd inverse with a genuine
piece of the VARIABLE original negative-frequency multiplier.

This tests the full SM06 constant-weight J=[3.645,3.705] continuum jointly
with SM07's newly certified additional 3/5-weight J1=[3.645,3.655]
continuum. The positive signed reference remains the original C16.
Only a passing exact rational test plus both infinite-tail payments proves
this selected nonuniform two-level subband; it NEVER closes W-ODD-NEG.
"""
from fractions import Fraction as F
from validate_rpb108_sm06_first_negative_moment import (
    B, PI, KAPPA, FEATURES, N, POS_PANELS, NEG_PANELS, MOM_PANELS,
    NEG_CENTER, NEG_RADIUS, NEG_DELTA, signed_windows,
    composite_mean_terms, composite_moment_terms, simpson_error,
    moment_simpson_error, scale_int, add_int, sub_int
)
from validate_rpb108_si21_odd_jensen_four import outward, midpoint, solve_exact
from validate_rpb108_si25_first_moment_bessel import linear_interval, bilinear_interval
from validate_rpb108_si12_even_supported_inverse import sinh_bounds
from validate_rpb108_sm06_band_legendre_tail import validate as certify_broad_tail
from validate_rpb108_sm07_true_multiplier_excess_nogo import (
    CENTER as EX_CENTER, RADIUS as EX_RADIUS, EXTRA as EX_DELTA,
    certify_subband
)

THETA=F(993,1000)
# The initial 8-panel first-moment source replay failed ONLY because the
# interval norm-radius bound (0.12176) overwhelmed the finite LDL margin;
# use 16-panel moments to lower quadrature uncertainty by 16x.
MOMENT_PANELS=16
# Source columns: s, broad mean, broad first moment, narrow mean, narrow first moment.
SOURCE_DATA=(
    (NEG_CENTER,NEG_RADIUS,False,NEG_PANELS),
    (NEG_CENTER,NEG_RADIUS,True,MOMENT_PANELS),
    (EX_CENTER,EX_RADIUS,False,NEG_PANELS),
    (EX_CENTER,EX_RADIUS,True,MOMENT_PANELS),
)
WEIGHTS=(
    F(2),
    4*NEG_RADIUS*NEG_DELTA,
    4*NEG_RADIUS*NEG_DELTA/3,
    4*EX_RADIUS*EX_DELTA,
    4*EX_RADIUS*EX_DELTA/3
)
K=5

def make_sources():
    terms=[]
    taus=[]
    for c,r,moment,panels in SOURCE_DATA:
        terms.append(composite_moment_terms(c,r,panels)
                     if moment else composite_mean_terms(c,r,panels))
        taus.append(moment_simpson_error(r,panels)
                    if moment else simpson_error(r,panels))
    assert len(terms)==4 and all(t>0 for t in taus)
    return terms,taus

def supported_intervals():
    """Entrywise outward enclosures for true physical positive/source Grams."""
    source_terms,source_tau=make_sources()
    pos_terms=[composite_mean_terms(c,r,POS_PANELS)
               for c,r,delta,deg in FEATURES]
    pos_tau=[simpson_error(r,POS_PANELS) for c,r,delta,deg in FEATURES]
    gamma=[4*r*delta for c,r,delta,deg in FEATURES]
    assert len(pos_terms)==N==16 and len(gamma)==N
    assert WEIGHTS==(F(2),F(21,125),F(7,125),F(3,250),F(1,250))

    Q=[]
    for i in range(N):
        lo,hi=linear_interval(pos_terms[i])
        row=[outward((lo-F(3,4)*pos_tau[i],
                       hi+F(3,4)*pos_tau[i]),15)]
        for j in range(4):
            lo,hi=bilinear_interval(pos_terms[i],source_terms[j])
            err=4*B*(pos_tau[i]+source_tau[j])
            row.append(outward((lo-err,hi+err),15))
        Q.append(row)

    H=[[None]*N for _ in range(N)]
    for i in range(N):
        for j in range(i,N):
            lo,hi=bilinear_interval(pos_terms[i],pos_terms[j])
            err=4*B*(pos_tau[i]+pos_tau[j])
            H[i][j]=H[j][i]=outward((lo-err,hi+err),15)

    P=[[None]*K for _ in range(K)]
    slo,shi=sinh_bounds(B)
    P[0][0]=outward((slo-B,shi-B),15)
    for j in range(4):
        lo,hi=linear_interval(source_terms[j])
        P[0][j+1]=P[j+1][0]=outward(
            (lo-F(3,4)*source_tau[j],hi+F(3,4)*source_tau[j]),15)
    for i in range(4):
        for j in range(i,4):
            lo,hi=bilinear_interval(source_terms[i],source_terms[j])
            err=4*B*(source_tau[i]+source_tau[j])
            P[i+1][j+1]=P[j+1][i+1]=outward((lo-err,hi+err),15)

    M=[[(lo/KAPPA+(1/gamma[i] if i==j else 0),
          hi/KAPPA+(1/gamma[i] if i==j else 0))
         for j,(lo,hi) in enumerate(row)] for i,row in enumerate(H)]
    # Mathematically the exact M=Gamma^-1+G*G/kappa is SPD, even
    # if independent rational interval entry boxes are not a PSD matrix.
    print("SM08: enclosed original 16x16 positive and 16x5,5x5 physical Grams",
          flush=True)
    print("SM08: maximum signed Simpson source error:",
          float(max(source_tau)),flush=True)
    return Q,M,P

def inverse_loewner_majorant(Q,M,P):
    """Correct-sign variational/dual Woodbury upper, no square-root rounding."""
    Mmid=[[midpoint(a) for a in row] for row in M]
    Z=[]
    for col in range(K):
        z=solve_exact(Mmid,[midpoint(Q[i][col]) for i in range(N)])
        unit=10**12
        Z.append([F((a*unit).numerator//(a*unit).denominator,unit) for a in z])
    U=[[None]*K for _ in range(K)]
    for j in range(K):
        for k in range(j,K):
            corr=(F(0),F(0))
            for i in range(N):
                corr=add_int(corr,scale_int(Z[k][i],Q[i][j]))
                corr=add_int(corr,scale_int(Z[j][i],Q[i][k]))
            for i in range(N):
                for h in range(N):
                    corr=sub_int(corr,scale_int(Z[j][i]*Z[k][h],M[i][h]))
            U[j][k]=U[k][j]=outward(
                sub_int(scale_int(1/KAPPA,P[j][k]),
                        scale_int(1/KAPPA**2,corr)),12)
    return U

def strictly_positive_ldl(S):
    """Fraction-only congruent LDL test; true iff every exact pivot > 0."""
    n=len(S)
    diag=[]
    lower=[[F(0)]*n for _ in range(n)]
    for j in range(n):
        d=S[j][j]-sum(lower[j][k]**2*diag[k] for k in range(j))
        if d<=0:
            print("SM08: LDL nonpositive pivot",j,float(d),flush=True)
            return False
        diag.append(d)
        lower[j][j]=F(1)
        for i in range(j+1,n):
            lower[i][j]=(S[i][j]-
                sum(lower[i][k]*lower[j][k]*diag[k] for k in range(j)))/d
    print("SM08: exact positive LDL pivot lower selection:",
          [float(x) for x in diag],flush=True)
    return True

def certify_five_source(U):
    # Let Utrue be the symmetric EXPLICIT dual Loewner majorant produced
    # from exact physical Grams and the fixed rational Z. Each actual
    # Utrue_ij belongs to the following outward rational interval, and
    # V*A^-1 V <= Utrue. The entrywise error from the midpoint matrix
    # has spectral norm at most max absolute row sum of interval radii.
    # In particular no assertion is made that each true inverse entry
    # individually lies in U's scalar intervals.
    mid=[[midpoint(x) for x in row] for row in U]
    err=max(sum((hi-lo)/2 for lo,hi in row) for row in U)
    # diag(theta/w_i)-Utrue > 0 is EQUIVALENT to the normalized
    # BS upper D Utrue D < theta I, with D=diag(sqrt(w_i)).
    # This weighted congruence eliminates every irrational sqrt factor.
    # Gershgorin on DU D would lose the shared broad/narrow covariance.
    S=[[((THETA/WEIGHTS[i]-err) if i==j else F(0))-mid[i][j]
        for j in range(K)] for i in range(K)]
    assert all(S[i][j]==S[j][i] for i in range(K) for j in range(K))
    print("SM08: 5-source exact interval-norm error upper:",
          float(err),flush=True)
    print("SM08: source weights:",[float(w) for w in WEIGHTS],flush=True)
    passed=strictly_positive_ldl(S)
    if not passed:
        return False
    # Thus A - all five true rank-one source terms >= (1-theta)A.
    return True

def certify_tails():
    tail0=certify_broad_tail()
    # The second full continuum is an EXTRA constant delta=3/5 on
    # J1, nested inside the already paid first band. Parseval is
    # additive across spectral weights; no disjointness is required.
    # Independent exact Legendre degree>=2 error of the entire J1 band:
    tail1=(EX_DELTA*EX_RADIUS**5*(2*PI[1])**4*2*B**5)/25
    total=tail0+tail1
    budget=(1-THETA)*KAPPA
    assert tail1>0 and tail1<F(1,10**9)
    assert total<budget,("SM08 combined infinite tails exceed floor",
                         float(total),float(budget))
    print("SM08: broad, narrow and summed infinite-tail upper:",
          float(tail0),float(tail1),float(total),flush=True)
    return total

def validate():
    signed_windows()
    upper=certify_subband()
    # The full original m(xi)<-2 on J1 from SM07 implies
    # r=(kappa-m)_+ > 2.001 > delta+extra = 2.
    assert upper<-F(2)
    assert NEG_DELTA+EX_DELTA==F(2)
    assert (EX_CENTER-EX_RADIUS,EX_CENTER+EX_RADIUS)==(F(729,200),F(731,200))
    assert NEG_CENTER-NEG_RADIUS<=EX_CENTER-EX_RADIUS
    assert EX_CENTER+EX_RADIUS<=NEG_CENTER+NEG_RADIUS
    Q,M,P=supported_intervals()
    U=inverse_loewner_majorant(Q,M,P)
    assert certify_five_source(U),(
        "SM08 candidate 5-source BS at theta=.993 not certified; "
        "do NOT promote this partial variable band")
    tail=certify_tails()
    floor=(1-THETA)*KAPPA-tail
    print("SM08: rigorously derived selected nonuniform two-level original "
          "negative band residual L2 floor:",float(floor),flush=True)
    print("SM08 PASS (SCOPED): original odd A dominates pole + "
          "2*(7/5) integral_J hh* +2*(3/5) integral_J1 hh* "
          "on physical odd support; all other variable excess, "
          "other bands, and W-ODD-NEG OPEN",flush=True)

if __name__=="__main__":
    validate()
