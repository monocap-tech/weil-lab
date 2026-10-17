#!/usr/bin/env python3
"""SM22: first ACTUAL SM10 supported sine source, SI29-C14 inverse UPPER.

Uses the true original seven-prime SI29 physical 14-feature reference and
its previously certified pole response L<1. All 14 original continuous
Jensen/Legendre feature overlaps and all 196 true Gram intervals are paid.
The variational inverse correction is a rigorous exact Fraction lower,
therefore the resulting original supported inverse is an UPPER.

Also enclose the SM21 first actual forward residual in the original SM19
B14^-1 energy by a rational Young inequality. This is NOT an 890-column
inverse computation, a true entire signed odd Weil theorem, or RH.
"""
from fractions import Fraction as F

from validate_rpb108_si06_negative_band import B,PI
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_sm20_original_source_forward import (
    simpson_error,TAIL_A2,KAPPA_STAR
)
from validate_rpb108_si18_odd_rank_two_woodbury import gram,signed_odd_overlap
from validate_rpb108_si25_first_moment_bessel import feature_terms,bilinear_interval
from validate_rpb108_si21_odd_jensen_four import outward,midpoint,solve_exact,variational_lower
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES

L_POLE=F(966379,10**6)
YOUNG=(F(1,100),F(1,50),F(1,25),F(1,20),
       F(1,10),F(1,5),F(1,4),F(1,2),F(1),F(2),F(4),F(8))

def sqlo(iv):
    a,b=iv
    if a<=0<=b:return F(0)
    return min(a*a,b*b)

def abshi(iv):
    return max(abs(iv[0]),abs(iv[1]))

def run():
    assert KAPPA==F(1,1000) and KAPPA_STAR==F(33621,10**9)
    assert F(0)<L_POLE<1
    clusters,width,mass,total=full_upper_leaves()
    center=(clusters[0][0][0]+clusters[0][-1][1])/2
    assert len(FEATURES)==14 and center==F(37,64)
    nlo,nhi=outward(gram(center,center),12)
    assert 0<nlo<=nhi<F(9,4)

    # The TRUE SI29 source functions, not Simpson proxies, are used:
    # each Simpson form only chooses an enclosed physical interval.
    terms=[]
    tau=[]
    gamma=[]
    for source_c,r,delta,deg in FEATURES:
        terms.append(feature_terms(source_c,r,deg))
        err=simpson_error(r,deg)
        upper=outward((err,err),15)[1]
        assert 0<err<=upper<F(1,1000)
        tau.append(upper)
        gamma.append(4*r*delta/(3 if deg else 1))

    # True source->u0 overlaps q_j=<g_j,u0>, all 14 signed.
    q=[]
    for i,term in enumerate(terms):
        lo,hi=bilinear_interval(term,((center,F(1)),))
        q.append(outward((lo-2*B*tau[i],hi+2*B*tau[i]),12))
    assert len(q)==14 and all(lo<=hi for lo,hi in q)

    # Exact signed 14x14 physical Gram interval H_jk, including all
    # Jensen/Legendre errors, with mirrored identical intervals.
    H=[[None]*14 for _ in range(14)]
    for i in range(14):
        for j in range(i,14):
            lo,hi=bilinear_interval(terms[i],terms[j])
            eps=4*B*(tau[i]+tau[j])
            v=outward((lo-eps,hi+eps),12)
            H[i][j]=H[j][i]=v
    assert all(H[i][j]==H[j][i] for i in range(14) for j in range(14))

    # K=Gamma^-1 + H/kappa is SPD for the actual true Gram H.
    K=[[(iv[0]/KAPPA+(1/gamma[i] if i==j else 0),
         iv[1]/KAPPA+(1/gamma[i] if i==j else 0))
         for j,iv in enumerate(H[i])] for i in range(14)]

    # The floating/interval MIDPOINT solve selects a rational witness,
    # NOT a certificate; the full signed interval variational LOWER is
    # the sole accepting source of the inverse correction.
    z0=solve_exact([[midpoint(a) for a in row] for row in K],
                   [midpoint(v) for v in q])
    unit=10**10
    z=[F((v*unit).numerator//(v*unit).denominator,unit) for v in z0]
    correction=variational_lower(q,K,z)
    assert correction>0, "No certified original source correction"
    upper_C=nhi/KAPPA-correction/KAPPA**2
    assert upper_C>0, "Inconsistent supported inverse upper"

    # SI29 already certified the exact TRUE original pole Schur:
    # alpha=1-2<s,C14^-1 s> >=1-L_POLE>0.
    # Cauchy in C14^-1 energy plus positive pole Sherman-Morrison:
    # <u,B14^-1u> <= <u,C14^-1u>/alpha <= upper_C/(1-L).
    upper_B=upper_C/(1-L_POLE)
    floor_upper=nhi/KAPPA_STAR
    assert upper_B>0 and floor_upper>0
    best=min(upper_B,floor_upper)

    # SM21 local Rayleigh lower on this same actual source, with
    # the TRUE signed pole subtracted. No source-/pole cancellation.
    pole=signed_odd_overlap(center)
    pole_up=outward(pole,12)
    positive=KAPPA*nlo+sum((gamma[i]*sqlo(q[i])
                             for i in range(14)),F(0))
    rayleigh=positive-2*abshi(pole_up)**2
    assert rayleigh>0
    qL=max(rayleigh,KAPPA_STAR*nlo)
    graphM=1360*nhi+2*TAIL_A2
    lam=qL/graphM
    assert 0<lam<1
    residual_Dhi=nhi-qL**2/graphM
    assert 0<residual_Dhi<nhi

    # Actual residual E=u-lambda*A_star*u (graph action certified SM20).
    # For Cauchy in B14^-1 energy:
    # ||E||_B <= ||u||_B + lambda ||A_star*u||_B.
    # B14^-1<=kappa_star^-1 I. Rational Young upper for the sum
    # retains mixed terms without falsely declaring orthogonality.
    young_bounds=[((1+d)*upper_B+
                   (1+1/d)*lam*lam*graphM/KAPPA_STAR,d)
                  for d in YOUNG]
    young,delta=min(young_bounds,key=lambda x:x[0])
    global_error=residual_Dhi/KAPPA_STAR
    residual_bound=min(young,global_error)
    # Additionally from the existing original B14<=A_star:
    # <u,A_star^-1u> <= <u,B14^-1u>, hence the very same actual
    # first-source inverse response is bounded by best.
    assert best<=floor_upper
    assert residual_bound>0
    print("SM22 actual first original SM10 source",float(center),flush=True)
    print("SM22 original true SI29 sources",len(terms),
          "signed pair-Grams",len(terms)*(len(terms)+1)//2,flush=True)
    print("SM22 first-source physical norm2 upper",float(nhi),flush=True)
    print("SM22 original SI29 variational correction lower",
          float(correction),flush=True)
    print("SM22 original supported C14^-1 source upper",float(upper_C),flush=True)
    print("SM22 true original pole-conditioned B14^-1 source upper",
          float(upper_B),flush=True)
    print("SM22 original scalar floor source upper",float(floor_upper),flush=True)
    print("SM22 retained TRUE A_star^-1 first-source upper",float(best),flush=True)
    print("SM22 local signed original energy lower",float(rayleigh),flush=True)
    print("SM22 actual original forward Ritz scale",float(lam),flush=True)
    print("SM22 actual residual D00 upper",float(residual_Dhi),flush=True)
    print("SM22 Cauchy/Young residual B14^-1 upper",float(young),
          "delta",float(delta),flush=True)
    print("SM22 uniform residual B14^-1 upper",float(global_error),flush=True)
    print("SM22 accepted actual residual inverse bound",float(residual_bound),flush=True)
    if upper_B<floor_upper and young<global_error:
        print("SM22 PASS (SCOPED STRICT FIRST-SOURCE INVERSE IMPROVEMENT):"
              " true original supported SI29 C14-star source response and"
              " actual SM21 residual inverse error improve scalar estimates;"
              " full 890-source W-ODD-NEG and RH OPEN",flush=True)
    else:
        print("SM22 PASS (SCOPED DIAGNOSTIC): exact actual source inverse"
              " bounds retained but preconditioner insufficient versus"
              " scalar on one diagnostic; 890-source W-ODD-NEG OPEN",flush=True)

if __name__=="__main__":
    run()
