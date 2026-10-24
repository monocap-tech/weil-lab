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
    PI,LN,B,prime_interval,log_rational_bounds,CONST_UP,TWOC)
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
from validate_rpb108_mg07_original_signed_supported_tail import (
    support_tail)

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

def cell_affine_exact_lower(w0,w1,v,d,h,eps,E):
    """True all-real signed-cell lower, not a sampled quadrature."""
    assert h>0 and eps>=0 and E>=0
    baseline=h*w0*v*v+h**3/F(12)*(w0*d*d+2*w1*v*d)
    lin_mass=h*v*v+h**3/F(12)*d*d
    supT=abs(v)+abs(d)*h/2
    w_abs=abs(w0)+abs(w1)*h/2+eps
    error=eps*lin_mass+w_abs*h*E*(2*supT+E)
    return baseline-error

def kink_affine_branch_lower(intercept,slope,v,d,h,eps,E):
    """Certified real-cell lower for convex signed κ-kink, no sign split.

    wθ(m) = max{(1-θ)κ-m, -θ m} pointwise for all REAL m.
    Both affine branches are individually GLOBAL lower bounds.
    Integrate each against nonnegative TRUE |T|² using the
    original complete multiplier/source error; take MAX of those
    independently valid rational lowers.
    """
    minus=cell_affine_exact_lower(
        (1-THETA)*KAPPA-intercept,-slope,v,d,h,eps,E)
    plus=cell_affine_exact_lower(
        -THETA*intercept,-THETA*slope,v,d,h,eps,E)
    return max(minus,plus)

def affine_weight_square_antiderivative(t,w0,w1,v,d):
    """Exact rational polynomial primitive, true physical no quadrature."""
    return (w0*v*v*t
        +(2*w0*v*d+w1*v*v)*t*t/2
        +(w0*d*d+2*w1*v*d)*t**3/3
        +w1*d*d*t**4/4)

def kink_piecewise_exact_lower(intercept,slope,v,d,h,eps,E):
    """Integrate convex κ kink EXACTLY for affine signed multiplier.

    For original m_*(t)=intercept+slope*t, wθ(m_*(t))
    is piecewise affine with exact rational transition time
    t*=(κ-intercept)/slope. The integral of wθ(m_*) *
    (v+d*t)^2 is a rational quartic primitive on at most two
    pieces. Actual m and physical Fourier are controlled by the
    SAME global errors eps and E as sign-stable cells.
    """
    assert h>0 and eps>=0 and E>=0
    lo=-h/2;hi=h/2
    knots=[lo,hi]
    if slope!=0:
        crossing=(KAPPA-intercept)/slope
        if lo<crossing<hi:knots=[lo,crossing,hi]
    integral=F(0)
    for a,b in zip(knots,knots[1:]):
        middle=intercept+slope*(a+b)/2
        if middle<KAPPA:
            w0=(1-THETA)*KAPPA-intercept
            w1=-slope
        else:
            w0=-THETA*intercept
            w1=-THETA*slope
        integral+=(affine_weight_square_antiderivative(
                    b,w0,w1,v,d)
                  -affine_weight_square_antiderivative(
                    a,w0,w1,v,d))
    mass=h*v*v+h**3/F(12)*d*d
    supT=abs(v)+abs(d)*h/2
    minus0=(1-THETA)*KAPPA-intercept
    plus0=-THETA*intercept
    supW=max(abs(minus0)+abs(slope)*h/2,
             abs(plus0)+THETA*abs(slope)*h/2)+eps
    error=eps*mass+supW*h*E*(2*supT+E)
    return integral-error

def cell_kink_lower(weight_floor,v,d,E,h):
    """Safe even across any m=kappa crossing inside the REAL cell."""
    assert h>0 and E>=0
    lowT=max(F(0),abs(v)-abs(d)*h/2-E)
    highT=abs(v)+abs(d)*h/2+E
    return h*weight_floor*(lowT*lowT if weight_floor>=0
                            else highT*highT)

def polynomial_product(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j]+=a*b
    return out

def symmetric_polynomial_integral(p,h):
    return sum((p[j]*h**(j+1)/(2**j*(j+1))
                for j in range(0,len(p),2)),F(0))

def regression_cell_integral_adversarial():
    """Compare certified lower with INDEPENDENT exact sextic integral."""
    h=F(1,4)
    k=KAPPA
    for intercept,slope,v,d,curve,quad in (
        (F(-2),F(1,3),F(4),F(-5),F(1,4),F(3,7)),
        (F(3),F(-1,4),F(-5),F(7),F(-1,8),F(-2,5)),
        (F(-3),F(-1,7),F(2),F(1,3),F(1,11),F(-1,2)),
        (F(5),F(1,6),F(1,2),F(-3),F(-1,7),F(1,5)),
    ):
        # m(t)=intercept+slope*t+curve*(t*t-h*h/4).
        # |m-m_affine|<=|curve|*h*h/4 on the WHOLE cell.
        eps=abs(curve)*h*h/4
        E=abs(quad)*h*h/4
        assert intercept-abs(slope)*h/2-eps>k or (
             intercept+abs(slope)*h/2+eps<k)
        negative=intercept<k
        # EXACT piecewise w(m) branch; no interval approximation.
        w_const=((1-THETA)*k-intercept if negative
                 else -THETA*intercept)
        fac=F(-1) if negative else -THETA
        wpoly=[w_const-fac*curve*h*h/4,fac*slope,fac*curve]
        tpoly=[v-quad*h*h/4,d,quad]
        actual=symmetric_polynomial_integral(
            polynomial_product(wpoly,polynomial_product(tpoly,tpoly)),h)
        w0=w_const
        w1=fac*slope
        lower=cell_affine_exact_lower(w0,w1,v,d,h,eps,E)
        assert lower<=actual, (lower,actual)
    # wθ(m) is EXACTLY the maximum of two linear branches.
    # Their integrals therefore give two globally valid LOWER
    # certificates on ANY crossing cell; this is independent of
    # declaring m above/below the κ crossing.
    for m in (F(-13),F(-2),F(-1,100),KAPPA,F(1,50),F(1)):
        minus=(1-THETA)*KAPPA-m
        plus=-THETA*m
        actual=max(F(0),KAPPA-m)-THETA*max(KAPPA,m)
        assert actual==max(minus,plus)
    # In crossing cells, the new affine minorant must stay below
    # an independently integrated EXACT polynomial with a real
    # κ crossing; split its two halves by analytic antiderivatives.
    hcross=F(1,4)
    s_cross=F(1,50)
    amp=F(2)
    true_int=amp*amp*(
        -THETA*KAPPA*hcross + (1-THETA)*s_cross*hcross*hcross/8)
    affine_lower=kink_affine_branch_lower(
        KAPPA,s_cross,amp,F(0),hcross,F(0),F(0))
    assert affine_lower<=true_int
    piecewise=kink_piecewise_exact_lower(
        KAPPA,s_cross,amp,F(0),hcross,F(0),F(0))
    assert piecewise==true_int and piecewise>affine_lower
    assert kink_piecewise_exact_lower(
        KAPPA,-s_cross,amp,F(0),hcross,F(0),F(0))==true_int
    # Non-centered crossing, nonlinear linear-Fourier square.
    # Independent primitive integrates exact branch polynomials.
    hm=F(1,3)
    mm=KAPPA+F(1,300)
    sm=F(1,20)
    vv=F(3,2);dd=F(-2,3)
    cross=(KAPPA-mm)/sm
    assert -hm/2<cross<hm/2
    wminus=((1-THETA)*KAPPA-mm,-sm)
    wplus=(-THETA*mm,-THETA*sm)
    independent=(
      affine_weight_square_antiderivative(
          cross,*wminus,vv,dd)
      -affine_weight_square_antiderivative(
          -hm/2,*wminus,vv,dd)
      +affine_weight_square_antiderivative(
          hm/2,*wplus,vv,dd)
      -affine_weight_square_antiderivative(
          cross,*wplus,vv,dd))
    assert kink_piecewise_exact_lower(
        mm,sm,vv,dd,hm,F(0),F(0))==independent
    # GENUINE kink inside the cell; lower must not use a smooth
    # branch across m=kappa. Exact integral on both halves with
    # a constant true physical Fourier packet.
    slope=F(1,50);v=F(2)
    left=(1-THETA)*k-(k-slope*h/2)
    right=-THETA*(k+slope*h/2)
    floor=right
    # integrated w for left/right half, where m=k+slope*t.
    actual=v*v*(-THETA*k*h+(1-THETA)*slope*h*h/8)
    lower=cell_kink_lower(floor,v,F(0),F(0),h)
    assert left>right and lower<=actual
    # Explicit positive lower-cell weight: use MINIMUM source
    # square, never the upper source square.
    assert cell_kink_lower(F(1),F(3),F(1),F(1,4),h)>=0
    return True

def regression_true_odd_Fourier_zero():
    """Independent physical-moment normalization at the origin.

    For any zero-extended REAL odd source, the genuine sine
    transform T(0)=0 and T'(0)=2*pi*int x*f(x)dx.
    Explicit sine and sinh physical moments must overlap the
    SI42 true Fourier derivative intervals, not a sampled FFT.
    """
    sh=hyperbolic_interval(B/2,"sinh")
    ch=hyperbolic_interval(B/2,"cosh")
    u,v,du,dv=qbasis(F(0),sh,ch)
    assert u.l<=0<=u.h and v.l<=0<=v.h
    # Direct original sine first moment (SI42 F1 primitive).
    du_original=2*I(PI[0],PI[1])*F1(CENTER)
    # Direct analytic hyperbolic identity:
    # int_{-B}^B x*sinh(x/2) dx =
    #       4 B cosh(B/2) - 8 sinh(B/2).
    pole_moment=4*B*ch-8*sh
    dv_original=2*I(PI[0],PI[1])*pole_moment
    assert du.l>0 and dv.l>0
    assert du.l<=du_original.h and du_original.l<=du.h
    assert dv.l<=dv_original.h and dv_original.l<=dv.h
    return True

def regression_affine_signed_quadratic():
    """Independent exact polynomial moments and kink-monotonic checks."""
    # Integrate (2+3t)*(5-7t)^2 exactly on [-h/2,h/2].
    w0,w1,v,d,h=F(2),F(3),F(5),F(-7),F(3,4)
    analytic=h*w0*v*v+h**3/F(12)*(w0*d*d+2*w1*v*d)
    # Direct polynomial expansion: constant, t² and odd terms.
    independent=(w0*v*v*h+
                 (w0*d*d+2*w1*v*d)*h**3/12)
    assert analytic==independent
    # Canonical pointwise ORIGINAL signed decomposition, including
    # κ exactly at the kink; the direct signed diagnostic is not a
    # substitute source or an assumed Kminus/Astar commutator.
    for m in (F(-13),F(-1),F(0),KAPPA,F(1,2),F(9)):
        assert max(KAPPA,m)-max(F(0),KAPPA-m)==m
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
    assert regression_cell_integral_adversarial()
    assert regression_true_odd_Fourier_zero()
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
    supported=support_tail()
    assert len(supported["rays"])==len(RAYS)==2
    out=[F(0)]*len(RAYS)
    signed_true_low=[F(0)]*len(RAYS)
    total=0;stable=0;crossings=0
    worst_eps=F(0);max_source_error=F(0)
    # Preserve exact five-region diagnostics even if strict method
    # STOP does not pass. Nothing below is a sampled sign estimate.
    band_ranges=((F(0),F(1)),(F(1),F(4)),(F(4),F(8)),
                 (F(8),F(16)),(F(16),F(32)))
    band_sums=[[F(0)]*len(RAYS) for _ in band_ranges]
    true_signed_band_sums=[[F(0)]*len(RAYS) for _ in band_ranges]
    assert CONST_UP==F(4707,875)
    assert 0<TWOC<F(70751,10000)
    # Entire signed Fourier multiplier m(ξ) on ALL real
    # frequencies: SI06 positive digamma series and seven
    # original prime powers give m >= -M0 pointwise.
    M0=CONST_UP+F(70751,10000)
    assert M0>0
    for left,right in cells(quick):
        band_index=next(i for i,(lo,hi) in enumerate(band_ranges)
                        if lo<=left and right<=hi)
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
                contribution=cell_affine_exact_lower(
                    w0,w1,v,d,h,eps,E)
            else:
                # Kink or uncertain sign: no differentiability assumed.
                constant_kink=cell_kink_lower(
                    weight_floor,v,d,E,h)
                convex_kink=kink_affine_branch_lower(
                    intercept,slope,v,d,h,eps,E)
                exact_kink=kink_piecewise_exact_lower(
                    intercept,slope,v,d,h,eps,E)
                # All three individually paid whole-real original
                # enclosures; take the strongest without guessing
                # the unknown actual crossing location.
                contribution=max(constant_kink,convex_kink,
                                 exact_kink)
            certified_cell=below(2*contribution,10**6)
            out[index]+=certified_cell
            band_sums[band_index][index]+=certified_cell
            # Independent smooth SIGNED-WEIL scalar lower:
            # Astar - Kminus = m(D) - 2ss*, exactly,
            # with no kink in the original multiplier m.
            # The same all-real affine m and true physical
            # T bounds apply, but use w0=m_mid and w1=slope.
            true_cell=below(2*cell_affine_exact_lower(
                intercept,slope,v,d,h,eps,E),10**6)
            signed_true_low[index]+=true_cell
            true_signed_band_sums[band_index][index]+=true_cell
        total+=1
    assert all(sum(band_sums[k][i] for k in range(len(band_ranges)))==out[i]
               for i in range(len(RAYS)))
    assert all(sum(true_signed_band_sums[k][i]
                   for k in range(len(band_ranges)))==signed_true_low[i]
               for i in range(len(RAYS)))
    stop=[]
    for index,((a,b,label),r,v) in enumerate(zip(
            RAYS,reduction["rays"],out)):
        assert r["ray"]==label
        const=F(r["certified_strict_low_band_difference_threshold"])
        reserve=v-const
        beta=F(r["original_odd_Fourier_beta_at_32"])
        pole_hi=F(r["certified_pole_payment_upper"])
        # Fourier tail: ∫_{|ξ|>32}|T_f(ξ)|² <= 2 beta²/32,
        # m(ξ)>=-(CONST_UP+TWOC) for every original real ξ.
        previous_uniform_signed_high_negative_budget=M0*2*beta*beta/F(32)
        assert supported["rays"][index]["ray"]==label
        signed_high_negative_budget=F(supported["rays"][index][
            "entire_true_original_signed_negative_high_tail_upper"])
        assert signed_high_negative_budget>0
        assert previous_uniform_signed_high_negative_budget/signed_high_negative_budget>20
        signed_energy_lower=(
            signed_true_low[index]-signed_high_negative_budget-pole_hi)
        signed_ray_positive=signed_energy_lower>0 and not quick
        stop.append({
          "true_original_signed_odd_energy_lower":str(signed_energy_lower),
          "true_original_signed_odd_ray_positive_if_strict":
              signed_ray_positive,
          "true_original_signed_low_0_32_lower":
              str(signed_true_low[index]),
          "all_real_original_signed_high_tail_negative_budget":
              str(signed_high_negative_budget),
          "previous_SI06_uniform_signed_high_tail_negative_budget":
              str(previous_uniform_signed_high_negative_budget),
          "SI10_support_mass_tail_improvement_factor":
              str(previous_uniform_signed_high_negative_budget/
                  signed_high_negative_budget),
          "true_original_sinh_pole_subtraction_upper":str(pole_hi),
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
        # ONE exact physical ray suffices; DO NOT assert until
        # AFTER saving exact rational diagnostics as a CI artifact.
        for ray in stop:
            if ray["strict_full_original_STOP_97percent_passed"]:
                assert F(ray["strict_full_original_Kminus_minus_97pct_Astar_lower"])>0
    return {
       "status":("SMOKE_TEST_NOT_CERTIFYING" if quick else
          ("CONDITIONAL_EXACT_ORIGINAL_JONLY_RITZ_CAP_METHOD_STOP"
           if accepted else "EXACT_ORIGINAL_LOW32_INCONCLUSIVE_NO_STOP")),
       "original_exact_seven_prime_multiplier":True,
       "full_rational_digamma_positive_terms_and_tail":True,
       "quarter_gamma_harmonic_integral_bracket":True,
       "original_physical_Fourier_exact_T_and_Tprime_interval":True,
       "independent_origin_sine_pole_physical_moment_identity":True,
       "original_arch_and_prime_whole_REAL_second_curvature_paid":True,
       "all_real_kink_crossings_paid":True,
       "independent_sextic_polynomial_cell_lower_regression":True,
       "exact_straddling_kappa_kink_adversarial_regression":True,
       "original_kappa_kink_is_exact_maximum_two_affine_branches":True,
       "crossing_cells_use_stronger_certified_convex_branch_lower":True,
       "crossing_cells_use_exact_piecewise_rational_kappa_intersection":True,
       "crossing_piecewise_independent_polynomial_regression":True,
       "true_odd_pole_subtraction_and_high_LOG_tail_paid":True,
       "source_only_J470_Ritz_matched_SM40_cap_method_if_passed":
            ("OBSTRUCTED_ONLY_ON_THIS_SUFFICIENT_METHOD"
             if accepted else "OPEN_NOT_CERTIFIED"),
       "true_SI29_augmented_484D_method":"NOT_TESTED",
       "independent_true_original_signed_ray_positive_count":sum(
          int(r["true_original_signed_odd_ray_positive_if_strict"])
          for r in stop),
       "true_original_signed_smooth_multiplier_identity":
          "Astar-Kminus = m(D)-2ss*",
       "true_original_signed_high_frequency_lower_from_SI06":True,
       "true_original_signed_high_frequency_support_from_SI10":True,
       "SI10_negative_high_tail_mass_exact":supported[
           "SI10_complete_original_two_signs_negative_cap_mass"],
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
       "true_original_signed_odd_low32_lower_by_frequency_region":[
         {"region":str(lo)+".."+str(hi),
          "ray_signed_lower_contributions":{
             RAYS[i][2]:str(true_signed_band_sums[k][i])
             for i in range(len(RAYS))}}
         for k,(lo,hi) in enumerate(band_ranges)
       ],
       "exact_original_certified_low32_lower_by_frequency_region":[
         {"region":str(lo)+".."+str(hi),
          "ray_lower_contributions":{RAYS[i][2]:str(band_sums[k][i])
                                   for i in range(len(RAYS))}}
         for k,(lo,hi) in enumerate(band_ranges)
       ],
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
    # Exact artifact is now preserved on failure/inconclusive.
    # This assertion is NEVER waived for a full certificate run.
    if not q.quick:
        assert o["accepted_original_method_stopping_rays"], (
            "Exact low32 method-stop FAILED: no certified strict "
            "positive ray. See retained artifact "+str(path))
if __name__=="__main__":main()
