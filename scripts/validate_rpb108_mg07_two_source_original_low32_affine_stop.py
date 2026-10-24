#!/usr/bin/env python3
"""NF: TRUE ORIGINAL odd two-source [0,32] rigorous affine-frequency ray test.

For true physical f=a*sin(2*pi*(37/64)*x)+b*sinh(x/2), restricted
to [-11/10,11/10], quantify for the ORIGINAL real signed multiplier
  m=Re psi(1/4+i*pi*xi)-ln pi-2 sum_{n=2,3,4,5,7,8,9}
                                   Lambda(n)/sqrt(n)*cos(2*pi*xi*ln n)
the genuine original cap-only Ritz method test:
  Knegative(f) - THETA*Astar(f)>0, THETA=97/100.

On [0,32] use EXACT rational endpoint enclosures for m, including:
  * SI06 seven prime powers prime_interval at each rational endpoint;
  * quarter-digamma positive-term identity, finite 64 exact sums,
    integrable positive monotone tail, true Euler gamma bracket
        H_N-log(N+1)<gamma<H_N-log N (N=1024);
  * SI43A full signed m'' curvature (arch + seven-prime D2).
True m differs from endpoint-median AFFINE interpolant by at most
radius_of_endpoint_intervals + D*h^2/8 on EVERY REAL point.

In each sign-stable cell, w(m)=(kappa-m)_+-THETA*max(kappa,m)
is affine in the interpolant. For physical Fourier T(xi),
TRUE T(mid) and T'(mid) from SI42 F0,F1,pole_sin,pole_xcos are
rational interval-enclosed; |T''| is globally bounded by the
ORIGINAL physical second moment. Integrate affine-w times linear-T
squared analytically, paying every interpolation, endpoint, and
squared-source Fourier error by outward Fraction. Kink-ambiguous
cells use a rigorous constant weight lower, never a sign guess.

Reflect frequencies by factor 2; add full exact original 2|<f,s>|²
pole lower and deduct entire SM41 high Ao positive-form upper
above 32. An exact POSITIVE final scalar would obstruct ONLY
the original 470-source J-only Ritz/SM40-cap sufficient gate.
It does NOT imply original signed odd NEGATIVITY, and does not
test true SI29-augmented Ritz or establish 470D positive Loewner.
No floats appear in mathematical acceptance.
"""
from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
import json,argparse
from validate_rpb108_si06_negative_band import (
    PI,LN,B,prime_interval,log_rational_bounds)
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm40_endpoint_curvature_negative_cap import D2
from validate_rpb108_sm43_positive_affine_error import (
    arch_second_derivative_whole_real_upper)
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    F0,F1,pole_sin,pole_xcos,I,hyperbolic_interval)
from validate_rpb108_mg07_two_source_original_physical_pole_input import (
    CENTER,RAYS)
from validate_rpb108_mg07_two_source_stop_low_band_reduction import (
    exact_reduction)

ROOT=Path(__file__).resolve().parents[1]
THETA=F(97,100)
DEN=10**12
GAMMA_N=1024
ARCH_K=64
LO_LOG2=F(69,100)
HI_LOG2=F(347,500)

def below(x,d=DEN):
    q=F(x)*d
    return F(q.numerator//q.denominator,d)
def above(x,d=DEN):
    q=F(x)*d
    return F(-((-q.numerator)//q.denominator),d)
def outward(x,d=DEN):
    return below(x.l,d),above(x.h,d)
def maximum_abs(a,b):
    return max(abs(a),abs(b))

@lru_cache(maxsize=1)
def exact_arch_constant():
    assert LN[2][0]>LO_LOG2 and LN[2][1]<HI_LOG2
    harmonic=sum((F(1,k) for k in range(1,GAMMA_N+1)),F(0))
    # Classical elementary telescoping harmonic-integral gamma:
    # H_N-log(N+1) < gamma < H_N-log N.
    gam_lo=harmonic-log_rational_bounds(F(GAMMA_N+1))[1]
    gam_hi=harmonic-log_rational_bounds(F(GAMMA_N))[0]
    assert GAMMA_N==1024 and 0<gam_lo<gam_hi<F(1)
    # psi(1/4)-ln pi= -gamma-pi/2-3ln2-lnpi.
    c_lo=gam_lo+PI[0]/2+3*LN[2][0]+log_rational_bounds(PI[0])[0]
    c_hi=gam_hi+PI[1]/2+3*LN[2][1]+log_rational_bounds(PI[1])[1]
    assert c_lo<c_hi and c_hi-c_lo<F(1,900)
    return below(c_lo),above(c_hi)

@lru_cache(maxsize=16384)
def arch_at(q):
    """Original arch point interval at rational q>=0; all true terms."""
    assert isinstance(q,F) and q>=0
    c_lo,c_hi=exact_arch_constant()
    ylo=below(PI[0]*q,10**14)
    yhi=above(PI[1]*q,10**14)
    alpha=F(1,4)
    lo=F(0);hi=F(0)
    for k in range(ARCH_K):
        v=F(k)+alpha
        zlo=ylo*ylo/(v*(v*v+ylo*ylo))
        zhi=yhi*yhi/(v*(v*v+yhi*yhi))
        lo=below(lo+zlo)
        hi=above(hi+zhi)
    # decreasing positive integrand tail bracket:
    # integral_K^inf f <= sum_{k=K}^inf f(k) <= integral_{K-1}^inf f
    low_tail=log_rational_bounds(1+(ylo/(ARCH_K+alpha))**2)[0]/2
    up_tail=log_rational_bounds(1+(yhi/(ARCH_K-1+alpha))**2)[1]/2
    low=below(lo+low_tail-c_hi)
    high=above(hi+up_tail-c_lo)
    assert low<=high
    return low,high

@lru_cache(maxsize=16384)
def signed_m_at(q):
    a=arch_at(q)
    p=prime_interval(q)
    return below(a[0]+p[0]),above(a[1]+p[1])

def qbasis(mid,sh,ch):
    """TRUE original physical sine/pole Fourier packet + derivative ONCE."""
    u=(F0(CENTER-mid)-F0(CENTER+mid))/2
    # derivative of 1/2(F0(c-xi)-F0(c+xi)):
    du=I(PI[0],PI[1])*(F1(CENTER-mid)+F1(CENTER+mid))
    v=pole_sin(mid,sh,ch)
    dv=2*I(PI[0],PI[1])*pole_xcos(mid,sh,ch)
    return u,v,du,dv

def qinterval(basis,a,b):
    u,v,du,dv=basis
    return outward(a*u+b*v),outward(a*du+b*dv)

def cells(quick=False):
    # Focus where original source Fourier mass is substantial.
    # The two intervals are exactly disjoint and cover [0,32].
    # Quick mode is a VERIFICATION smoke test, never acceptance.
    grids=((F(0),F(1),F(1,256)),
           (F(1),F(32),F(1,64)))
    if quick:grids=((F(0),F(1),F(1,32)),
                    (F(1),F(32),F(1,8)))
    for left,right,h in grids:
        n=int((right-left)/h)
        assert left+n*h==right
        for j in range(n):
            l=left+j*h
            yield l,l+h

def regression_affine_signed_quadratic():
    """Independent exact polynomial moments and kink-monotonic checks."""
    # Integrate (2+3t)*(5-7t)^2 exactly on [-h/2,h/2].
    w0,w1,v,d,h=F(2),F(3),F(5),F(-7),F(3,4)
    analytic=h*w0*v*v+h**3/F(12)*(w0*d*d+2*w1*v*d)
    # Direct polynomial expansion: constant, t² and odd terms.
    independent=(w0*v*v*h+
                 (w0*d*d+2*w1*v*d)*h**3/12)
    assert analytic==independent
    for theta in (F(97,100),F(51,56)):
        k=F(1,1000)
        def weight(m):
            return max(F(0),k-m)-theta*max(k,m)
        lo=F(-1);mid=k;hi=F(1)
        assert weight(lo)>weight(mid)>weight(hi)
        assert weight(mid)==-theta*k
        assert weight(lo)==(1-theta)*k-lo
        assert weight(hi)==-theta*hi
    return True

def exact_scalar(quick=False):
    assert CENTER==F(37,64) and B==F(11,10)
    assert regression_affine_signed_quadratic()
    assert KAPPA==F(1,1000) and THETA==F(97,100)
    # True SI06 7-power signed multiplier at frequency 0 is
    # strongly negative, with no sample or new digamma assumption.
    zero=signed_m_at(F(0))
    assert F(-13)<zero[0]<=zero[1]<F(-12)
    assert F(600)<D2<F(900)
    cutoff=F(32)
    sh=hyperbolic_interval(B/2,"sinh")
    ch=hyperbolic_interval(B/2,"cosh")
    assert sh.l>0 and ch.h<F(6,5)
    # True physical Fourier second derivative bound from x² moments.
    second_factors={
      label:above(4*PI[1]*PI[1]*
          (F(a)*2*B**3/3+F(b)*2*B**3/3*sh.h))
      for a,b,label in RAYS
    }
    reduction=exact_reduction()
    out=[F(0)]*len(RAYS)
    total=0;stable=0;crossings=0
    worst_eps=F(0);max_source_error=F(0)
    for left,right in cells(quick):
        h=right-left;mid=(left+right)/2
        ma=signed_m_at(left); mb=signed_m_at(right)
        mal=(ma[0]+ma[1])/2;mbl=(mb[0]+mb[1])/2
        eps=above(max((ma[1]-ma[0])/2,(mb[1]-mb[0])/2)+
            (D2+arch_second_derivative_whole_real_upper(left))*h*h/8)
        assert eps>0
        worst_eps=max(worst_eps,eps)
        floor=min(mal,mbl)-eps
        ceil=max(mal,mbl)+eps
        negative=ceil<KAPPA
        positive=floor>KAPPA
        stable+=int(negative or positive)
        crossings+=int(not (negative or positive))
        intercept=(mal+mbl)/2
        slope=(mbl-mal)/h
        if negative:
            w0=(1-THETA)*KAPPA-intercept
            w1=-slope
        else:
            w0=-THETA*intercept
            w1=-THETA*slope
        w_hi_abs=abs(w0)+abs(w1)*h/2+eps
        # w(m) monotone decreasing for any original m:
        # below kappa: w=(1-theta)*kappa-m
        # above kappa: w=-theta*m.
        weight_floor=(1-THETA)*KAPPA-ceil if ceil<KAPPA else -THETA*ceil
        basis=qbasis(mid,sh,ch)
        for index,(a,b,label) in enumerate(RAYS):
            T,Tp=qinterval(basis,a,b)
            v=(T[0]+T[1])/2
            d=(Tp[0]+Tp[1])/2
            ev=(T[1]-T[0])/2
            ed=(Tp[1]-Tp[0])/2
            E=above(ev+ed*h/2+second_factors[label]*h*h/8)
            max_source_error=max(max_source_error,E)
            supT=abs(v)+abs(d)*h/2
            if negative or positive:
                # Entire true frequency integral, exactly integrated
                # affine signed weight against linear Fourier packet.
                baseline=h*w0*v*v+h**3/F(12)*(w0*d*d+2*w1*v*d)
                lin_mass=h*v*v+h**3/F(12)*d*d
                err=eps*lin_mass+w_hi_abs*h*E*(2*supT+E)
                contribution=baseline-err
            else:
                # Kink or uncertain sign: no differentiability assumed.
                lowT=max(F(0),abs(v)-abs(d)*h/2-E)
                highT=supT+E
                source_sq=lowT*lowT if weight_floor>=0 else highT*highT
                contribution=h*weight_floor*source_sq
            out[index]+=below(2*contribution,10**6)
        total+=1
    stop=[]
    for (a,b,label),r,v in zip(RAYS,reduction["rays"],out):
        assert r["ray"]==label
        const=F(r["certified_strict_low_band_difference_threshold"])
        reserve=v-const
        stop.append({
          "ray":label,"sine_coefficient":a,"pole_coefficient":b,
          "true_whole_original_signed_combination_LOW_lower":str(v),
          "exact_high_tail_minus_pole_threshold":str(const),
          "strict_full_original_Kminus_minus_97pct_Astar_lower":str(reserve),
          "strict_full_original_STOP_97percent_passed":reserve>0 and not quick,
          "display_lower":float(reserve)})
    accepted=[r["ray"] for r in stop
              if r["strict_full_original_STOP_97percent_passed"]]
    if not quick:
        assert total==256+31*64==2240
        # ONE exact physical ray suffices to reject this chosen
        # 470-source J-only Ritz/SM40-cap sufficient method.
        # Requiring both rays would silently impose a stronger and
        # irrelevant research acceptance condition.
        assert len(accepted)>=1, (
            "No strictly positive original signed ray certified; "
            "J-only Ritz method obstruction remains OPEN",stop)
        for ray in stop:
            if ray["strict_full_original_STOP_97percent_passed"]:
                assert F(ray["strict_full_original_Kminus_minus_97pct_Astar_lower"])>0
    return {
       "status":("SMOKE_TEST_NOT_CERTIFYING" if quick else
          "CONDITIONAL_EXACT_ORIGINAL_JONLY_RITZ_CAP_METHOD_STOP"),
       "original_exact_seven_prime_multiplier":True,
       "full_rational_digamma_positive_terms_and_tail":True,
       "quarter_gamma_harmonic_integral_bracket":True,
       "original_physical_Fourier_exact_T_and_Tprime_interval":True,
       "original_arch_and_prime_whole_REAL_second_curvature_paid":True,
       "all_real_kink_crossings_paid":True,
       "true_odd_pole_subtraction_and_high_LOG_tail_paid":True,
       "source_only_J470_Ritz_matched_SM40_cap_method_if_passed":
            "OBSTRUCTED_ONLY_ON_THIS_SUFFICIENT_METHOD",
       "true_SI29_augmented_484D_method":"NOT_TESTED",
       "entire_original_odd_operator_negative_witness":False,
       "full_original_signed_odd_positive":"OPEN",
       "even_CC27_Weil_RH":"OPEN",
       "low_band_cutoff":str(cutoff),
       "signed_frequency_factor_two":True,
       "rational_cells":total,
       "sign_stable_cells":stable,
       "kink_ambiguous_cells":crossings,
       "max_multiplier_affine_error":str(worst_eps),
       "max_physical_fourier_affine_error":str(max_source_error),
       "accepted_original_method_stopping_rays":accepted,
       "one_original_strict_rational_witness_suffices":True,
       "all_rays_accepted":len(accepted)==len(stop) and not quick,
       "rays":stop}
def main():
    a=argparse.ArgumentParser()
    a.add_argument("--quick",action="store_true")
    a.add_argument("--output",default="artifacts/mg07_two_source_original_low32_interval.json")
    q=a.parse_args()
    o=exact_scalar(q.quick)
    path=ROOT/q.output
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(o,indent=2)+"\n")
    print("Original true [0,32] Fraction cells",o["rational_cells"],
          "source-only Ritz stopping result",
          [(r["ray"],r["strict_full_original_STOP_97percent_passed"],
            r["display_lower"]) for r in o["rays"]],flush=True)
if __name__=="__main__":main()
