#!/usr/bin/env python3
"""SM46: true original POSITIVE source-window stiffness with source-AFFINE Fourier cells.

SM45 actual original supported 25 odd source window bound has eps=176.527225
at mesh1/8. SM46 integrates the FIRST-ORDER variation of the original
zero-extended sine/xcos/sinh source Fourier transforms into a full 25x25
RATIONAL matrix, rather than paying |T'_j|*h/2 as a scalar error.

For every real original frequency cell [a,b], midpoint c:
  true T_j(xi) = v_j + d_j*(xi-c) + r_j(xi);
  |r_j| <= midpoint-source interval radius
          + midpoint-derivative interval radius*h/2
          + true original whole-cell T_j'' upper*h²/8.
SI06/SM42 exact rational F0/F1/F2/sinh-pole and new F3 intervals
certify original source first and second derivatives; exact third
spatial moment controls local T'' variation, intersected with SM45
whole-real global T'' majorants. All 25 genuine source cross included.

The original SM43A positive seven-prime/digamma scalar weight reference
is piecewise constant OR max(kappa,rational signed m affine). Its
moments J0,J1,J2 against (xi-c)^0,1,2 are computed EXACTLY, splitting
a rational kappa-crossing. Reference integral:
  P_aff=2Σcell [J0 vv* + J1(vd*+dv*)+J2 dd*].
Each Jk is independently rational rounded; all errors paid.

Certified full 25x25 source Fourier Gram error per cell by Cauchy:
  2 J0 ||r|| (||T||+||v+d(x-c)||)
  <=2 J0 sqrt(E2)*(sqrt(S2)+sqrt(V2))
plus all rounded reference moment contributions. All square-root
upper bounds computed by exact integer square roots.

On a cell choose the SMALLER of TWO independently certified errors:
  (a) SM45 unchanged MIDPOINT source proxy, OR
  (b) SM46 new rational SOURCE-AFFINE proxy and second-order remainder.
The mathematical choice is exact Fraction, not floating spectral sign.

This certificate is ONLY on original 16 selected frequency windows
(total measure 1029/64), not whole real positive LOW [0,4096],
not original all 470 k-source Astar inverse/strong resolvent,
not original complete Wodd O1/O2, Weil positivity or RH.
"""
import argparse
import json
from fractions import Fraction as F
from math import factorial,isqrt

from validate_rpb108_si06_negative_band import PI,B,prime_interval
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    F1,F2,I,sin_cos_period,omega,pole_xcos,hyperbolic_interval
)
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,source_window_support_envelopes,
    positive_cell_weight_interval,arch_upper_at,ceil_rat
)
from validate_rpb108_sm39_rational_left_arch_cap import arch_lower_at
from validate_rpb108_sm43_positive_affine_error import affine_cell_error
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    original_exact_physical_fourier_midpoint,
    original_physical_source_lipschitz,
    original_full_second_derivative_upper,
    quantize,sqrt_upper,partition
)

def original_F3(q):
    """Original exact F3(q)=int[-B,B] x^3 sin(2*pi*q*x)dx.

    =2[-B^3 cos(wB)/w +3B² sin(wB)/w²
        +6B cos(wB)/w³ -6 sin(wB)/w⁴].
    All terms exact SI06/SM42 rational interval; q=0 removable.
    """
    q=F(q)
    if not q:return I(0)
    sn,cs=sin_cos_period(B*q)
    w=omega(q)
    return 2*(-B**3*cs/w+3*B*B*sn/(w*w)
               +6*B*cs/(w*w*w)-6*sn/(w*w*w*w))

def original_midpoint_derivative_intervals(xi,centers,sources,hyp):
    sh,ch=hyp
    pii=I(PI[0],PI[1])
    intervals=[];second=[]
    for kind,j,k in sources:
        if kind=="pole":
            one=2*pii*pole_xcos(xi,sh,ch)
            two=None
        elif k==0:
            c=centers[j]
            one=pii*(F1(c-xi)+F1(c+xi))
            two=2*pii*pii*(F2(c+xi)-F2(c-xi))
        elif k==1:
            c=centers[j]
            one=pii*(F2(xi+c)+F2(xi-c))
            two=-2*pii*pii*(original_F3(xi+c)+original_F3(xi-c))
        else:raise AssertionError("k>1 ORIGINAL not verified")
        intervals.append(one)
        second.append(two)
    assert len(intervals)==len(second)==25
    return intervals,second

def original_third_spatial_moment(sources):
    """Whole original REAL |T'''(xi)| for a supported source.

    |T'''| <= (2*pi_up)^3 int_-B^B |x|^3 |g_j(x)|dx.
    g=sin or sinh: |g|<=1, integral=B^4/2.
    g=x*cos: |g|<=|x|, integral=2B^5/5.
    """
    c=8*PI[1]**3
    return [c*(2*B**5/5 if typ!="pole" and k==1 else B**4/2)
            for typ,j,k in sources]

def polynomial_moment(alpha,beta,start,finish,n):
    """∫[start,finish] (t-1/2)^n * (alpha+beta*t) dt, n=0,1,2."""
    from math import comb
    out=F(0)
    for k in range(n+1):
        coeff=F(comb(n,k))*(-F(1,2))**(n-k)
        out+=coeff*(alpha*(finish**(k+1)-start**(k+1))/F(k+1)+
                    beta*(finish**(k+2)-start**(k+2))/F(k+2))
    return out

def positive_reference_moments(a,b,meta):
    """Exact J0,J1,J2 of actual original SM43A positive reference."""
    h=b-a
    if meta["reference_choice"]=="original_constant_cell":
        lo,hi,_=positive_cell_weight_interval(a,b)
        v=(lo+hi)/2
        J0=h*v;J1=F(0);J2=h**3*v/12
        return J0,J1,J2
    mla=arch_lower_at(a)+prime_interval(a)[0]
    mua=arch_upper_at(a)+prime_interval(a)[1]
    mlb=arch_lower_at(b)+prime_interval(b)[0]
    mub=arch_upper_at(b)+prime_interval(b)[1]
    va=(mla+mua)/2;vb=(mlb+mub)/2
    pieces=[]
    if va>=KAPPA and vb>=KAPPA:pieces=[(F(0),F(1),va,vb-va)]
    elif va<=KAPPA and vb<=KAPPA:pieces=[(F(0),F(1),KAPPA,F(0))]
    else:
        t=(KAPPA-va)/(vb-va)
        assert 0<t<1
        if va<KAPPA:
            pieces=[(F(0),t,KAPPA,F(0)),(t,F(1),va,vb-va)]
        else:
            pieces=[(F(0),t,va,vb-va),(t,F(1),KAPPA,F(0))]
    vals=[h**(n+1)*sum((polynomial_moment(alpha,beta,l,r,n)
                   for l,r,alpha,beta in pieces),F(0))
          for n in range(3)]
    assert vals[0]>0 and vals[2]>=0
    assert abs(vals[1])<=h*vals[0]/2
    assert vals[2]<=h*h*vals[0]/4
    return vals

def add_outer_symmetric(m,v,w,coef):
    """Exact rational whole original symmetric v wᵀ + w vᵀ cross."""
    if not coef:return
    n=len(v)
    for i in range(n):
        for j in range(i,n):
            m[i][j]+=coef*(v[i]*w[j]+w[i]*v[j])

def add_outer(m,v,coef):
    if not coef:return
    n=len(v)
    for i in range(n):
        for j in range(i,n):
            m[i][j]+=coef*v[i]*v[j]

def one_mesh(step,centers,sources,windows):
    assert step in (F(1,4),F(1,8))
    n=len(sources);assert n==25
    lows=original_physical_source_lipschitz(sources)
    second_global=original_full_second_derivative_upper(sources)
    third=original_third_spatial_moment(sources)
    sh=hyperbolic_interval(B/2,"sinh")
    ch=hyperbolic_interval(B/2,"cosh")
    rational_matrix=[[F(0) for _ in range(n)] for _ in range(n)]
    old_fourier=F(0);new_fourier=F(0)
    weight_error=F(0)
    chosen={"SM45_midpoint":0,"SM46_source_affine":0}
    improved_sources=0
    ncell=0
    max_drad=F(0)
    for a,b in partition(windows,step):
        ncell+=1;h=b-a;xi=(a+b)/2
        werror,meta=affine_cell_error(a,b,centers,sources)
        weight_error+=werror
        J0,J1,J2=positive_reference_moments(a,b,meta)
        p=original_exact_physical_fourier_midpoint(xi,centers,sources,(sh,ch))
        v=[x for x,rad in p]
        vr=[rad for x,rad in p]
        derivatives,second=original_midpoint_derivative_intervals(
            xi,centers,sources,(sh,ch))
        d=[quantize(q.mid()) for q in derivatives]
        dr=[ceil_rat(max(abs(qq.l-x),abs(qq.h-x)),10**9)
            for qq,x in zip(derivatives,d)]
        max_drad=max(max_drad,max(dr))
        K=[]
        for q,glob,t in zip(second,second_global,third):
            k=glob
            if q is not None:
                k=min(k,max(abs(q.l),abs(q.h))+t*h/2)
            assert k>=0 and k<=glob
            K.append(k)
        # Every REAL ξ in [a,b], bound both old T-v and new
        # original true affine-T errors with exact rational data.
        old_err=[rad+min(l*h/2,
                 max(abs(q.l),abs(q.h))*h/2+g*h*h/8)
                 for rad,l,q,g in zip(vr,lows,derivatives,second_global)]
        aff_err=[rad+rd*h/2+k*h*h/8
                 for rad,rd,k in zip(vr,dr,K)]
        improved_sources+=sum(ae<oe for ae,oe in zip(aff_err,old_err))
        cap=source_window_support_envelopes(a,b,centers,sources)
        s2=sum((q*q for q in cap),F(0))
        o2=sum((q*q for q in old_err),F(0))
        v2=sum((q*q for q in v),F(0))
        # SM45 full source Fourier error (same original matrix),
        # exactly reproduced, with original quantized J0.
        J0q=quantize(J0)
        oldeps=2*J0*(2*sqrt_upper(o2*s2)+o2)+2*abs(J0-J0q)*v2
        assert oldeps>=0
        old_fourier+=oldeps

        a2=sum((q*q for q in aff_err),F(0))
        tmax2=sum((abs(x)+abs(y)*h/2)**2 for x,y in zip(v,d))
        # The original true T is bounded by cap, while the
        # source-linear reference V=v+d*(ξ-mid) by tmax2.
        # Rank-one operator difference <= ||T-V||(||T||+||V||).
        bound=2*J0*sqrt_upper(a2)*(sqrt_upper(s2)+sqrt_upper(tmax2))
        moms=[J0,J1,J2]
        mq=[quantize(m) for m in moms]
        d2=sum((q*q for q in d),F(0))
        # Exact rational moment rounding Loewner:
        # 2*|δJ0| ||v||² +4*|δJ1| ||v||||d||
        # +2*|δJ2| ||d||².
        rounding=2*abs(J0-mq[0])*v2+4*abs(J1-mq[1])*sqrt_upper(v2*d2)+2*abs(J2-mq[2])*d2
        affineeps=bound+rounding
        assert affineeps>=0
        if affineeps<oldeps:
            chosen["SM46_source_affine"]+=1
            new_fourier+=affineeps
            add_outer(rational_matrix,v,2*mq[0])
            add_outer_symmetric(rational_matrix,v,d,2*mq[1])
            add_outer(rational_matrix,d,2*mq[2])
        else:
            chosen["SM45_midpoint"]+=1
            new_fourier+=oldeps
            add_outer(rational_matrix,v,2*J0q)
    for i in range(n):
        for j in range(i):
            rational_matrix[i][j]=rational_matrix[j][i]
    assert ncell>0 and chosen["SM46_source_affine"]>0
    assert new_fourier<old_fourier
    assert all(rational_matrix[i][j]==rational_matrix[j][i]
               for i in range(n) for j in range(n))
    eps=weight_error+new_fourier
    assert eps>0
    # The chosen rational matrix is a sum of positive-weight
    # original Fourier Gram integrals of rational affine source
    # functions (or constants), hence PSD; signs of its entries
    # or raw eigenvalues do not replace that proof.
    return {
       "max_cell_width":str(step),
       "original_supported_source_dimension":n,
       "original_true_frequency_cell_count":ncell,
       "same_source_centered_window_measure":str(sum((b-a for a,b in windows),F(0))),
       "source_reference_choices":chosen,
       "source_components_with_strict_affine_error_improvement":improved_sources,
       "max_original_midpoint_source_derivative_interval_radius_float":float(max_drad),
       "unchanged_original_weight_Loewner_error_exact_outward":str(ceil_rat(weight_error,10**9)),
       "SM45_original_midpoint_Fourier_cell_error_exact_outward":str(ceil_rat(old_fourier,10**9)),
       "SM46_new_source_affine_Fourier_cell_error_exact_outward":str(ceil_rat(new_fourier,10**9)),
       "SM46_complete_original_selected_source_window_Loewner_error_exact_outward":str(ceil_rat(eps,10**9)),
       "SM45_Fourier_error_float":float(old_fourier),
       "SM46_Fourier_error_float":float(new_fourier),
       "SM46_total_error_float":float(eps),
       "SM46_Fourier_error_ratio_to_SM45_float":float(new_fourier/old_fourier),
       "exact_complete_rational_original_25x25_source_matrix":
         [[str(z) for z in row] for row in rational_matrix],
       "entire_true_positive_low_0_to_4096_certified":False,
       "complete_original_odd_O1_O2_certified":False,
       "all_470_original_Astar_inverse_certified":False
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm46_original_source_affine_physical_fourier.json")
    args=p.parse_args()
    data=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in data["obligations"] if o["id"]=="W-ODD-NEG")
    assert data["active_obligation"]=="W-ODD-NEG"
    assert data["objective"]["status"]=="open" and odd["status"]=="open"
    assert data["governance"]["no_automatic_promotion"] is True
    assert "SM46" in data["evidence"] and "SM46" in odd["evidence"]
    assert "sm46_original_source_affine_physical_Fourier" in data["governance"]
    centers,sources,windows=original_source_centered_windows()
    outputs=[]
    for step in (F(1,4),F(1,8)):
        result=one_mesh(step,centers,sources,windows)
        print("SM46 exact original 25-source AFFINE Fourier",
              json.dumps({k:v for k,v in result.items()
                  if k!="exact_complete_rational_original_25x25_source_matrix"},
                  sort_keys=True),flush=True)
        outputs.append(result)
    coarse,fine=outputs
    assert coarse["original_true_frequency_cell_count"]==65
    assert fine["original_true_frequency_cell_count"]==129
    assert fine["same_source_centered_window_measure"]==coarse["same_source_centered_window_measure"]=="1029/64"
    assert fine["SM46_Fourier_error_float"]<coarse["SM46_Fourier_error_float"]
    assert fine["SM46_total_error_float"]<coarse["SM46_total_error_float"]
    # Meaningful exact-rational >=5% reduction vs SM45
    assert F(fine["SM46_new_source_affine_Fourier_cell_error_exact_outward"]) < F(95,100)*F(
        fine["SM45_original_midpoint_Fourier_cell_error_exact_outward"]),(
            "The original full 25x25 source-affine method did not achieve a meaningful >=5% certified error reduction")
    output={
       "status":"CERTIFIED_SCOPED_TRUE_ORIGINAL_AFFINE_PHYSICAL_FOURIER_FULL_25x25_SOURCE_WINDOW",
       "canonical_original_W_ODD_NEG":"OPEN",
       "source_scope":"same 25 genuine original supported odd SI10 physical sources, selected source-centered windows only",
       "true_original_seven_prime_digamma_positive_weight":"identical to SM43A/SM45, original entire-real kink-safe certified interpolation fee",
       "mathematical_operator_statement":"-eps I25 <= A_original_positive_source_windows - P_SM46_rational25x25 <= eps I25",
       "coarse_mesh":{k:v for k,v in coarse.items()
           if k!="exact_complete_rational_original_25x25_source_matrix"},
       "fine_mesh":fine,
       "whole_original_positive_low_0_to_4096_certified":False,
       "full_original_Astar_inverse_strong_residual_certified":False,
       "full_original_odd_Wodd_O1_O2_certified":False,
       "even_E1_E4_Weil_CC27_RH_certified":False,
       "remaining":[
           "high-frequency original positive low [0,4096] outside selected source windows",
           "local matrix/source preconditioned Loewner error if still too large for 25-source source norm",
           "all 470 original polynomial-source physical Fourier transforms and high positive digamma tail",
           "full true original Astar inverse strong residual and all 470 odd Wodd O1/O2 or corrected Schur",
           "independent exact original Fourier/closed domain audit and original even/whole Weil/RH"
       ]
    }
    dest=ROOT/args.output
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(output,indent=2)+"\n")
    print("SM46 SCOPED: actual original 25x25 RATIONAL source-affine"
          " Fourier cell stiffness on SAME true selected windows,"
          " exact source full-coupled Loewner source variation"
          " paid and strict meaningful improvement vs SM45."
          " Whole positive low [0,4096], full 470 Astar inverse,"
          " Wodd/even/Weil/CC27/RH remain OPEN.",flush=True)

if __name__=="__main__":
    main()
