#!/usr/bin/env python3
"""MG07 NF: original 960-cell low12 source-only Ritz/SM40 method STOP.

This is a SHORTER complete-original proof attempt than low32:
  256 exact cells width 1/256 on [0,1]
  704 exact cells width 1/64 on [1,12]
  Entire original Ao positive form tail |xi|>12 paid via the
  TRUE physical sine/sinh endpoint-cancelled two-IBP/log envelope.

The original signed seven-prime/digamma m endpoints and TRUE odd
physical Fourier intervals are imported from the low32 verifier.
The only required full-real multiplier curvature is the robust
global rational 2300, because inherited SM40 D2<900 and
SM43A whole-real quarter-digamma bound LOWARCH<1400.
No adaptive-cell gap, sign shortcut, sampling, SI29 quadrature
or unrealized 484D Galerkin term appears. Strict exact Fraction
positive lower on ONE source ray rejects ONLY the chosen J470
source-only Ritz+SM40 cap SUFFICIENT method. No original odd
negative direction or RH inference.
"""
from fractions import Fraction as F
import json
from pathlib import Path
from validate_rpb108_si06_negative_band import (
    B,PI,log_rational_bounds)
from validate_rpb108_sm43_positive_affine_error import LOWARCH
from validate_rpb108_mg07_two_source_original_physical_pole_input import (
    CENTER,RAYS,evaluate as physical_anchor,add,scl,mul)
from validate_rpb108_mg07_two_source_endpoint_log_tail import (
    PI_LO,PI_UP,abs_upper)
from validate_rpb108_si12_even_supported_inverse import (
    sinh_bounds,cosh_bounds)
from validate_rpb108_si14_odd_multiband_nogo import cos_sin_pi_multiple
from validate_rpb108_si10_complement_positivity import protected_inner_cover
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_sm40_sharp_odd_complement_threshold import new_threshold
from validate_rpb108_mg07_two_source_original_low32_affine_stop import (
    D2,KAPPA,THETA,below,above,signed_m_at,
    qbasis,qinterval,hyperbolic_interval,
    cell_affine_exact_lower,cell_kink_lower,
    kink_affine_branch_lower,kink_piecewise_exact_lower,
    regression_affine_signed_quadratic,
    regression_cell_integral_adversarial,
    regression_true_odd_Fourier_zero,
    exact_arch_constant)

ROOT=Path(__file__).resolve().parents[1]
CUT=F(12)
GLOBAL_D2=F(2300)

def high_positive_tail12():
    assert B==F(11,10) and CENTER==F(37,64)
    assert PI[0]>PI_LO and PI[1]<PI_UP
    assert F(600)<D2<F(900)
    assert F(1100)<LOWARCH<F(1400)
    assert D2+LOWARCH<GLOBAL_D2
    sh=sinh_bounds(B/2)
    ch=cosh_bounds(B/2)
    sn,cs=cos_sin_pi_multiple(2*B*CENTER)
    omega=(2*PI[0]*CENTER,2*PI[1]*CENTER)
    ln12hi=log_rational_bounds(CUT)[1]
    tails=[]
    for a,b,label in RAYS:
        endpoint=add(scl(a,sn),scl(b,sh))
        derivative=add(scl(a,mul(omega,cs)),scl(F(b,2),ch))
        # Fractions inherited from 85+-term trig/pi series can have
        # thousands of decimal digits. Round UP before persisting;
        # exact outward bounds are preserved, unlike str(huge_fraction).
        ep=above(abs_upper(endpoint),10**12)
        der=above(abs_upper(derivative),10**12)
        if label.startswith("direct"):
            assert ep<F(425) and der<F(19200)
        else:
            assert ep<F(97) and der<F(4850)
        second=2*B*a*(2*PI_UP*CENTER)**2+b*(ch[1]-1)
        beta=above(ep/PI_LO+(2*der+second)/(4*PI_LO**2*CUT),10**12)
        tail=above(2*beta**2*(18+ln12hi)/CUT,10**12)
        assert beta>0 and tail>0
        if label.startswith("direct"):assert tail<F(3200000)
        else:assert tail<F(200000)
        tails.append({
            "ray":label,
            "true_physical_endpoint_upper":str(ep),
            "true_physical_endpoint_derivative_upper":str(der),
            "original_two_IBP_beta_cut12":str(beta),
            "complete_original_Ao_log_tail_beyond12_upper":str(tail)})
    return tails

def exact_original_J_membership():
    """Fail closed unless both supported rays really belong to SM35's J470.

    The first SM35 cluster contributes its degree-zero odd physical sine;
    the true sinh pole is the final original J column. Do not infer
    membership merely from the numerical scout's source labels.
    """
    clusters,_,_,_,_=protected_inner_cover()
    assert len(clusters)==107
    source_dim=1+sum(taylor_order(r-l,9)[0] for l,r,_ in clusters)
    assert source_dim==470
    l0,r0,_=clusters[0]
    assert (l0+r0)/2==CENTER==F(37,64)
    assert taylor_order(r0-l0,9)[0]>=1
    assert len(RAYS)==2
    assert all(a>0 and b>0 for a,b,_ in RAYS)
    return {
      "original_SM35_J_source_dim":source_dim,
      "original_first_cluster_interval":[str(l0),str(r0)],
      "original_first_degree_zero_sine_center":str((l0+r0)/2),
      "original_true_sinh_pole_in_J":True,
      "both_rays_exact_original_J_membership":True}

def verify():
    membership=exact_original_J_membership()
    # The strict method-stop implication needs the actual ORIGINAL
    # same-SM40 complement threshold, not a presumed decimal value.
    sm40=new_threshold()
    assert sm40["original_source_dim"]==470
    assert sm40["original_SM40_cap_columns"]==890
    assert sm40["original_signed_real_subcells"]==3892
    threshold=F(sm40["new_sharp_sufficient_source_threshold"])
    assert F(51,56)<threshold<THETA==F(97,100)
    assert regression_affine_signed_quadratic()
    assert regression_cell_integral_adversarial()
    assert regression_true_odd_Fourier_zero()
    assert 0<exact_arch_constant()[1]-exact_arch_constant()[0]<F(1,1000000)
    assert D2+LOWARCH<GLOBAL_D2 and THETA==F(97,100)
    tails=high_positive_tail12()
    phys=physical_anchor()
    sh=hyperbolic_interval(B/2,"sinh")
    ch=hyperbolic_interval(B/2,"cosh")
    second=[
       above(4*PI[1]**2*(F(a)*2*B**3/3+F(b)*2*B**3/3*sh.h))
       for a,b,_ in RAYS
    ]
    low=[F(0)]*len(RAYS)
    regions=((F(0),F(1),F(1,256)),
             (F(1),CUT,F(1,64)))
    contributions=[[F(0)]*len(RAYS) for _ in range(4)]
    intervals=((F(0),F(1)),(F(1),F(4)),
               (F(4),F(8)),(F(8),CUT))
    cells=0;kinks=0
    for start,end,h in regions:
        assert start<end and h>0
        n=int((end-start)/h)
        assert start+n*h==end
        for j in range(n):
            l=start+j*h;r=l+h;mid=(l+r)/2
            a=signed_m_at(l);b=signed_m_at(r)
            u=(a[0]+a[1])/2
            v=(b[0]+b[1])/2
            m0=(u+v)/2
            m1=(v-u)/h
            # FULL original real signed m: global curvature is
            # larger than BOTH certified original component bounds.
            eps=above(max((a[1]-a[0])/2,(b[1]-b[0])/2)
                      +GLOBAL_D2*h*h/8)
            lower_m=min(u,v)-eps
            upper_m=max(u,v)+eps
            below_kappa=upper_m<KAPPA
            above_kappa=lower_m>KAPPA
            kinks+=int(not (below_kappa or above_kappa))
            basis=qbasis(mid,sh,ch)
            region=next(i for i,(x,y) in enumerate(intervals)
                        if x<=l and r<=y)
            for i,(alpha,beta,label) in enumerate(RAYS):
                T,Tp=qinterval(basis,alpha,beta)
                amp=(T[0]+T[1])/2
                deriv=(Tp[0]+Tp[1])/2
                E=above((T[1]-T[0])/2+
                         (Tp[1]-Tp[0])*h/4+second[i]*h*h/8)
                if below_kappa:
                    w0=(1-THETA)*KAPPA-m0;w1=-m1
                    contribution=cell_affine_exact_lower(
                        w0,w1,amp,deriv,h,eps,E)
                elif above_kappa:
                    w0=-THETA*m0;w1=-THETA*m1
                    contribution=cell_affine_exact_lower(
                        w0,w1,amp,deriv,h,eps,E)
                else:
                    floor_w=((1-THETA)*KAPPA-upper_m
                             if upper_m<KAPPA else -THETA*upper_m)
                    contribution=max(
                       cell_kink_lower(floor_w,amp,deriv,E,h),
                       kink_affine_branch_lower(
                           m0,m1,amp,deriv,h,eps,E),
                       kink_piecewise_exact_lower(
                           m0,m1,amp,deriv,h,eps,E))
                certified=below(2*contribution,10**6)
                contributions[region][i]+=certified
                low[i]+=certified
            cells+=1
    assert cells==256+11*64==960
    assert all(sum(reg[i] for reg in contributions)==low[i]
               for i in range(len(RAYS)))
    out=[]
    for i,(a,b,label) in enumerate(RAYS):
        assert phys["rays"][i]["purpose"]==label==tails[i]["ray"]
        pole_lo=F(phys["rays"][i][
           "genuine_Astar_pole_subtraction_2overlap_squared_interval"][0])
        high_hi=F(tails[i][
           "complete_original_Ao_log_tail_beyond12_upper"])
        lower=low[i]+THETA*(pole_lo-high_hi)
        out.append({
          "ray":label,
          "low_0_12_signed_method_lower":str(low[i]),
          "genuine_original_pole_payment_lower":str(pole_lo),
          "entire_original_Ao_high12_upper":str(high_hi),
          "complete_original_Kminus_minus_97pct_Astar_lower":str(lower),
          "certified_source_only_method_stop":lower>0,
          "display_complete_lower":float(lower)})
    accepted=[r["ray"] for r in out if r[
        "certified_source_only_method_stop"]]
    return {
      "status":("CONDITIONAL_EXACT_ORIGINAL_LOW12_SOURCE_ONLY_METHOD_STOP"
          if accepted else "ORIGINAL_LOW12_INCONCLUSIVE"),
      "original_physical_J_membership":membership,
      "same_original_SM40_threshold_exact":str(threshold),
      "method_test_threshold_exact":str(THETA),
      "same_original_SM40_threshold_strictly_below_method_test":threshold<THETA,
      "true_original_signed_prime_powers_all_seven":True,
      "true_original_quarter_digamma_endpoint_interval":True,
      "physical_sine_sinh_pole_source_genuine":True,
      "global_multiplier_curvature_upper":str(GLOBAL_D2),
      "true_all_real_gamma_and_convex_tail_paid":True,
      "complete_original_high12_two_IBP_log_tail_paid":True,
      "exact_rational_cells":cells,
      "kink_cells":kinks,
      "strict_positive_original_method_stop_rays":accepted,
      "original_960_cell_region_lowers":[
        {"region":str(l)+".."+str(r),
         "ray_lowers":{RAYS[i][2]:str(contributions[j][i])
                    for i in range(len(RAYS))}}
        for j,(l,r) in enumerate(intervals)],
      "rays":out,
      "original_true_signed_odd_operator":"OPEN",
      "original_SI29_augmented_trial":"OPEN",
      "even_CC27_Weil_RH":"OPEN"}

def main():
    result=verify()
    location=ROOT/"artifacts/mg07_true_original_low12_960cell.json"
    location.parent.mkdir(parents=True,exist_ok=True)
    location.write_text(json.dumps(result,indent=2)+"\n")
    print("Original exact low12 960-cell method-stop:",
        [(x["ray"],x["display_complete_lower"]) for x in
           result["rays"]],flush=True)
    # Save exact artifact even if certification fails.
    assert result["strict_positive_original_method_stop_rays"],(
       "No exact original low12 one-ray method stop; see artifact")

if __name__=="__main__":
    main()
