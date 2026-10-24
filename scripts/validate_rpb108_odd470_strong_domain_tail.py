#!/usr/bin/env python3
"""Scope: ORIGINAL odd 470 physical-source strong DOMAIN/Tail lemma only.

Under the inherited SM41 multiplier |a_o(xi)| <= 17+log|xi| for |xi|>=1
and the original supported Fourier form realization, all 469 SI10/SM35
odd polynomial sine/cosine generators and the original sinh pole lie
in Dom(A_o) and Dom(Astar). No signed-odd, original Weil-form transfer
or RH assertion is made. The scalar 470D tail upper is deliberately
coarse and cannot settle the MG07 residual/negative-cap gate.
"""
import json
from fractions import Fraction as Q
from pathlib import Path
from validate_rpb108_si10_complement_positivity import B, protected_inner_cover
from validate_rpb108_si08_multiband_rank import taylor_order

ROOT=Path(__file__).resolve().parents[1]
F=Q
LOG_MULTIPLIER_CONSTANT=17
# Two-frequency-side integral: 2 integral_1^infty (17+log t)^2 / t^2 dt.
# The exact moments integral_1^infty (log t)^j/t^2 dt = j!, j=0,1,2.
TWO_SIDED_TAIL=2*(17**2+2*17+2)
assert TWO_SIDED_TAIL==650

def poly_fourier_envelope(c,k):
    """For |xi|>=1, |hat f_{c,k}(xi)|<=C_{c,k}/|xi|.

    f_{c,k} is x^k sin(2*pi*c*x) for even k and x^k cos(2*pi*c*x)
    for odd k, on [-B,B], zero outside.  The endpoint jump term is
    <= 2 B^k. For k>0, integral |(x^k)'| = 2 B^k.
    The oscillatory derivative contributes
       (2*pi*c) integral |x|^k dx =4*pi*c*B^(k+1)/(k+1).
    Divide total variation plus endpoints by 2*pi*|xi|,
    and use pi>3. All resulting constants are exact rationals.
    """
    assert c>0 and isinstance(k,int) and k>=0
    return (F(1+(k>0),3)*B**k + 2*c*B**(k+1)/(k+1))

def pole_fourier_envelope():
    """s(x)=sinh(x/2) on [-B,B], zero outside.

    Let y=B/2<1. sinh(y)<=sum_(j>=0) y^(2j+1)
    = y/(1-y*y); both boundary and integral derivative total
    are 2*sinh(y), so C_pole<=2*sinh(y)/pi<=(2/3)*y/(1-y*y).
    """
    y=B/2
    assert 0<y<1
    return F(2,3)*y/(1-y*y)

def source_envelopes():
    clusters,width,mass,n_unresolved,n_protected=protected_inner_cover()
    assert len(clusters)==107 and n_unresolved==973 and n_protected==9261
    assert B==F(11,10)
    desc=[]
    prev=F(0)
    for a,b,w in clusters:
        c=(a+b)/2
        assert prev<c<F(896) and w>=0
        prev=c
        order,_=taylor_order(b-a,9)
        for k in range(order):
            desc.append((c,k,poly_fourier_envelope(c,k)))
    assert len(desc)==469
    assert sum(k%2==0 for c,k,e in desc)==260
    assert sum(k%2==1 for c,k,e in desc)==209
    pole=pole_fourier_envelope()
    assert pole>0 and pole<F(1)
    return desc,pole

def verify():
    desc,pole=source_envelopes()
    constants=[e for c,k,e in desc]+[pole]
    # Cauchy-Schwarz in coefficient space: for every z in R^470,
    # |hat(Jz)(xi)| <= sum_j |z_j| C_j / |xi|
    #                <= sqrt(sum_j C_j^2) ||z||_2 / |xi|.
    # Consequently S_{o,|xi|>=1} <= 650 sum_j C_j^2 I_470.
    tail_scalar=F(TWO_SIDED_TAIL)*sum((u*u for u in constants),F(0))
    assert tail_scalar>0
    assert all(x.denominator>0 for x in constants)
    assert len(constants)==470
    assert poly_fourier_envelope(F(1),0)==F(1,3)+2*B
    assert poly_fourier_envelope(F(1),1)==F(2,3)*B+B**2
    # No numerical quadrature, truncated high-frequency test, or
    # implicit cancellation of the original odd pole occurs here.
    record={
      "scope":"DOMAIN_AND_COARSE_ALL_470_STRONG_HIGH_TAIL_ONLY",
      "basis_dim":470,
      "polynomial_sources":469,
      "sine_sources":260,
      "cosine_sources":209,
      "odd_pole_sources":1,
      "negative_leaves_geometry_checked":973,
      "original_supported_aperture_B":str(B),
      "SM41_high_frequency_multiplier_assumption":"0<a_o(xi)<=17+ln|xi| for |xi|>=1",
      "two_sided_weight_integral":str(TWO_SIDED_TAIL),
      "all470_squared_coefficient_tail_upper":str(tail_scalar),
      "original_form_realization_independently_audited":False,
      "actual_470_G0_N0cap_DB_certified":False,
      "W_ODD_NEG_even_Weil_CC27_RH":"OPEN"
    }
    print("Odd 470-domain analytic tail check PASS (scope only).")
    print(json.dumps(record,indent=2))
    return record

if __name__=="__main__":
    verify()
