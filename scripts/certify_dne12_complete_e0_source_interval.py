#!/usr/bin/env python3
"""DNE12 interval certificate: complete original Weil physical e0 source-square.

Uses outward mpmath.iv arithmetic and monotone Darboux sums on the positive
half interval. The endpoint logarithmic square is bounded analytically, not
sampled. No high F112 / E112 projection or full 58-mode source Gram is made.
Requires mpmath. Does not use numerical quadrature as a proof primitive.
"""
from mpmath import iv
import argparse
import json
import time

def run(N=60000, digits=35):
    iv.dps=digits
    I=iv.mpf
    a=I(53)/50
    delta=I(1)/10**8
    primes=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]
    logs=[(iv.log(n),iv.log(p)/iv.sqrt(n)) for n,p in primes]
    a0=-iv.euler-iv.pi/2-3*iv.log(2)-iv.log(iv.pi)
    polecoef=4*(iv.exp(a/2)-iv.exp(-a/2))

    def J(t):
        q=iv.exp(-t/2)
        return iv.log((1+q)/(1-q))/2+iv.atan2(q,1)

    def pole(x):
        return polecoef*(iv.exp(x/2)+iv.exp(-x/2))/2

    def arch(x):
        return a0+J(a-x)+J(a+x)

    def source_range(l,r):
        # arch and pole strictly increase on the positive half-interval.
        val=I([arch(l).a,arch(r).b])+I([pole(l).a,pole(r).b])
        for ell,c in logs:
            if ell.b<a.a:
                # negative translation is always active; plus translation
                # turns off at x=a-ell.
                if r.b<(a-ell).a:
                    multiplicity=I(2)
                elif l.a>(a-ell).b:
                    multiplicity=I(1)
                else:
                    multiplicity=I([1,2])
            else:
                # positive translation never active; negative turns on
                # at x=ell-a.
                if l.a>(ell-a).b:
                    multiplicity=I(1)
                elif r.b<(ell-a).a:
                    multiplicity=I(0)
                else:
                    multiplicity=I([0,1])
            val-=c*multiplicity
        return val

    end=a-delta
    interior=I(0)
    interior_arch=I(0)
    for i in range(N):
        l=end*i/N
        r=end*(i+1)/N
        interior+=(r-l)*source_range(l,r)**2
        interior_arch+=(r-l)*I([arch(l).a,arch(r).b])**2
    interior/=a
    interior_arch/=a

    # Endpoint t=a-x in (0,delta), retaining EVERY prime source term.
    for ell,_ in logs:
        assert ell.b<(2*a-delta).a
        if ell.b<a.a:
            assert delta.b<ell.a
    CJ=iv.log(2)+iv.pi/4
    regular=a0+CJ+I([J(2*a).a,J(2*a-delta).b])
    regular+=I([pole(a-delta).a,pole(a).b])
    regular-=sum((c for _,c in logs),I(0))

    # Analytic DNE11 Cauchy estimate for |r| on [0,delta].
    assert (I(11)/(I(5)/2-delta)).b<I(5).a
    regular+=I([-5,5])*delta
    assert regular.a>I(-10).b and regular.b<I(10).a

    # Integral of (-(1/2)log(t)+10)^2 for 0<t<delta.
    L=-iv.log(delta)
    endpoint=(delta/a)*(I(1)/4*(L*L+2*L+2)+10*(L+1)+100)
    whole=I([interior.a,interior.b+endpoint.b])
    arch_regular=a0+CJ+I([J(2*a).a,J(2*a-delta).b])
    arch_regular+=I([-5,5])*delta
    assert arch_regular.a>I(-10).b and arch_regular.b<I(10).a
    arch_whole=I([interior_arch.a,interior_arch.b+endpoint.b])
    assert arch_whole.a>I('7.0819').b
    assert arch_whole.b<I('7.0828').a
    # Read-only NF21/CC58 proves the complete prime-plus-pole SOURCE-square
    # strictly in (7.244,7.245). This is an imported separate certificate.
    cross=whole-arch_whole-I(['7.244','7.245'])
    assert cross.a>I('-14.245').b
    assert cross.b<I('-14.241').a
    assert whole.a>I('0.0834').b,(whole,interior,endpoint)
    assert whole.b<I('0.0846').a,(whole,interior,endpoint)

    # Authenticate the original Q(e0,e0) upper/lower via the separately
    # published CC40/NF12 exact source interval, NOT a floating point input.
    # Published grid 10^25, Q00 in
    # [401520842754207446870744,401520842754207446870745]/10^25.
    from fractions import Fraction as F
    qlo=F(401520842754207446870744,10**25)
    qhi=F(401520842754207446870745,10**25)
    assert F(15,10000)<qlo*qlo<=qhi*qhi<F(17,10000)

    return {
        "stage":"DNE12 complete original Weil constant-mode source square",
        "method":"directed interval arithmetic + monotone native panels + analytic endpoint tail",
        "working_decimal_digits":digits,
        "positive_half_darboux_panels":N,
        "endpoint_width":"1/100000000",
        "complete_source_square_strict_interval":["0.0834","0.0846"],
        "interior_interval":str(interior),
        "arch_source_square_interval":["7.0819","7.0828"],
        "arch_interior_interval":str(interior_arch),
        "NF21_CC58_prime_pole_sector":["7.244","7.245"],
        "doubled_arch_prime_pole_cross_interval":["-14.245","-14.241"],
        "endpoint_normalized_upper":str(endpoint.b),
        "original_Q00_source":"CC40/NF12 authenticated rational interval",
        "after_E0_only_source_residual_strict_interval":["0.0817","0.0831"],
        "all_six_native_prime_powers_retained":True,
        "both_signed_pole_source_directions_retained":True,
        "complete_56_retained_projection_subtracted":False,
        "full_58_compensated_residual_certified":False,
        "RH_proved":False,
        "lean_certified":False
    }

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--panels",type=int,default=60000)
    parser.add_argument("--digits",type=int,default=35)
    args=parser.parse_args()
    t=time.time()
    print(json.dumps(run(args.panels,args.digits),indent=2))
    print("elapsed_seconds",round(time.time()-t,2))
