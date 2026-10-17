#!/usr/bin/env python3
"""SM20: first ACTUAL SM10 supported odd source forward-residual enclosures.

A deliberately conservative analytic bound on the actual ORIGINAL a=max(m,kappa)
controls A_* h graph norm, including the full unbounded Fourier exterior.
For Y=lambda*h, certify D00=<E,E>, all 14 SI29 overlaps G*E, and
t=<s,E>. This is only column zero, with loose conservative intervals.
Neither 890-column inverse nor W-ODD-NEG is proved.
"""
from fractions import Fraction as F

from validate_rpb108_si06_negative_band import (
    B, PI, TWOC, log_rational_bounds
)
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_si18_odd_rank_two_woodbury import gram, signed_odd_overlap
from validate_rpb108_si12_even_supported_inverse import sinh_bounds
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES
from validate_rpb108_si25_first_moment_bessel import (
    feature_terms, bilinear_interval
)

KAPPA_STAR=F(33621,10**9)
FREQ_CUTOFF=F(2048)
# On |xi|>=2048 and center <=896, each |hat(h_c)(xi)| <= 2/(3|xi|).
# On this exterior, 0<=a(xi)<=19+ln|xi|, and ln 2048<8.
# Reflected integral of a^2 |hat(h_c)|^2:
TAIL_A2=F(785,2304)


def simpson_error(radius,degree):
    beta=2*PI[1]*radius*B
    if degree==0:
        return beta**4/F(180)
    assert degree==1
    return 3*(4*beta**3+beta**4)/F(180)*F(1,4)**4


def run():
    assert TWOC<F(70751,10000)
    assert F(3)<PI[0]<PI[1]<4
    assert log_rational_bounds(F(2049))[1] < 8
    assert log_rational_bounds(F(2048))[1] < 8
    slo,shi=sinh_bounds(B)
    assert F(0)<shi-B<1

    # ACTUAL SM10 first cluster/first source, not a separately invented sine.
    clusters,width,mass,total=full_upper_leaves()
    assert len(clusters)==107 and len(FEATURES)==14
    cluster=clusters[0]
    c=(cluster[0][0]+cluster[-1][1])/2
    assert F(0)<c<F(896) and FREQ_CUTOFF>2*c
    # U_{0,0}(x)=sin(2*pi*c*x) on original [-B,B].
    nlo,nhi=gram(c,c)
    assert 0<nlo<=nhi<F(9,4)

    # ANALYTIC multiplier bound: original arch sum with
    # f(t)=y^2/[t(t^2+y^2)], N=max(1,ceil(y)), decreasing-integral tail.
    # sum f(n+1/4) < 7+log(1+pi|xi|); original subtraction constant>0;
    # prime absolute bound TWOC<8, log4<2. Hence
    # a(xi)=max(original m(xi),kappa) < 18+log(1+|xi|).
    # In |xi|<=2048 a<26; exterior <=19+log|xi|.
    # Therefore ||A_o h||^2 <=676||h||^2+785/2304.
    # Pole norm ||2s<s,h>||^2 <4||h||^2 and (v-w)^2<=2v^2+2w^2:
    # ||A_*h||^2 < 1360||h||^2+2*TAIL_A2.
    m_upper=1360*nhi+2*TAIL_A2
    assert F(0)<m_upper<10000
    N=1
    while F(N*N)<=m_upper:
        N+=1
    assert F(N*N)>m_upper

    # Nonzero *actual* original forward graph trial Y=lambda*U0.
    lam=KAPPA_STAR*nlo/m_upper
    delta=KAPPA_STAR*KAPPA_STAR*nlo*nlo/m_upper
    assert F(0)<lam<1 and delta>0
    # E0=U0-lambda*A_*U0. SI29's proven pole-conditioned coercivity:
    # D00<=nhi-2lam*kappa_star*nlo+lam^2*m_upper=nhi-delta.
    dhi=nhi-delta
    # Triangle/cross lower: |<h,A_*h>| <=||h||*||A_*h||<2N.
    dlo=max(F(0),nlo-4*lam*N)
    assert 0<dlo<=dhi<nhi

    # First true physical odd pole overlap, not point sampling.
    q=signed_odd_overlap(c)
    t=(q[0]-lam*N,q[1]+lam*N)

    # All 14 SI29 *actual* true continuous physical sources.
    # SI29's Simpson error is uniform in x. Original source norm <=3.
    # |<G_i,A_*h>| <= ||G_i|| ||A_*h|| <3N.
    F_intervals=[]
    for j,(center,radius,delta_j,degree) in enumerate(FEATURES):
        terms=feature_terms(center,radius,degree)
        initial=bilinear_interval(terms,((c,F(1)),))
        tau=simpson_error(radius,degree)
        assert tau>0
        quadrature=2*B*tau
        actual=(initial[0]-quadrature,initial[1]+quadrature)
        f=(actual[0]-3*lam*N,actual[1]+3*lam*N)
        assert f[0]<=f[1]
        F_intervals.append(f)
    assert len(F_intervals)==14

    print("SM20 actual SM10 source cluster count",len(clusters),flush=True)
    print("SM20 first original signed odd Taylor source center",str(c),float(c),flush=True)
    print("SM20 true physical source norm2",float(nlo),float(nhi),flush=True)
    print("SM20 entire original a^2 graph tail upper",float(TAIL_A2),flush=True)
    print("SM20 all-frequency true original A_star source norm2 upper",float(m_upper),flush=True)
    print("SM20 actual nonzero physical Ritz scale",float(lam),flush=True)
    print("SM20 certified residual D00 interval",float(dlo),float(dhi),flush=True)
    print("SM20 strict improvement against original norm upper",float(delta),flush=True)
    print("SM20 original pole <s,E0> interval",float(t[0]),float(t[1]),flush=True)
    for j,(lo,hi) in enumerate(F_intervals):
        print("SM20 true SI29 source residual F",j,float(lo),float(hi),flush=True)
    print("SM20 PASS (SCOPED ACTUAL SOURCE COLUMN): graph-domain and D00,F[14],t")
    print("SM20 889 other original columns, all mixed residuals, W-ODD-NEG and RH OPEN")

if __name__=="__main__":
    run()
