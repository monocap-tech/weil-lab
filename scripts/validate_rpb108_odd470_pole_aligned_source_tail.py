#!/usr/bin/env python3
"""W-ODD-NEG: exact whole-470 source endpoint-alignment high tail.

The original odd 470-dimensional exceptional space contains s=sinh(x/2).
For each of its 469 polynomial sine/cosine generators f, set
  h=f-(f(B)/s(B))*s, B=11/10.
This replaces the finite trial BASIS, not the original source span, SM34
Schur, original Astar, or original Kminus. Every new h vanishes at both
physical endpoints, hence has O(|xi|^-2) Fourier decay after two correct
integrations by parts with derivative jumps and all interior f'' included.

Exactly rational pi/log upper and lower brackets plus the inherited SM41
a_o(xi)<=17+log|xi| produce a full 470-coefficient source-basis
high-frequency Loewner upper. This is NOT a residual certificate, a
coercivity bound in original J coordinates, or a signed odd theorem.
"""
from fractions import Fraction as F
import json

B=F(11,10)
PI_LO=F(333,106)
PI_UP=F(22,7)
LN2_UP=F(347,500)
COSH_UP=F(6,5)

def unaligned_envelope(c,k):
    assert isinstance(c,F) and c>0 and isinstance(k,int) and k>=0
    return F(1+(k>0),3)*B**k+2*c*B**(k+1)/(k+1)

def aligned_gamma(c,k):
    """|Fourier(f-(f(B)/s(B))*s)(xi)|<=gamma/xi^2, all xi!=0.

    f=x^k sin(2*pi*c*x) for even k; x^k cos(2*pi*c*x) for odd k.
    |alpha|<=2 B^(k-1) follows from s(B)=sinh(B/2)>=B/2.
    All rational bounds use upper pi except the denominator's lower pi.
    """
    assert isinstance(c,F) and c>0 and isinstance(k,int) and k>=0
    bk=B**k
    # Boundary derivative: 2|f'(B)|.
    boundary=4*PI_UP*c*bk
    if k:
        boundary+=2*k*B**(k-1)
    # Entire supported interior second derivative L1 norm.
    interior=8*PI_UP**2*c*c*B**(k+1)/(k+1)
    if k:
        interior+=8*PI_UP*c*bk
    if k>=2:
        interior+=2*k*B**(k-1)
    # s' boundary and s'' interior: 2cosh(B/2)-1.
    alpha_bound=2*B**(k-1)
    pole=alpha_bound*(2*COSH_UP-1)
    return (boundary+interior+pole)/(4*PI_LO**2)

def tail_weights(p):
    """Whole +/- frequency log²/xi² and log²/xi⁴ integrals."""
    assert isinstance(p,int) and p>=11
    cutoff=F(2**p)
    A=F(17)+p*LN2_UP
    return (2*(A*A+2*A+2)/cutoff,
            2*(A*A+F(2,3)*A+F(2,9))/(3*cutoff**3))

def records(geometry):
    return [(F(c),k,unaligned_envelope(F(c),k),
             aligned_gamma(F(c),k)) for c,k in geometry]

def bound_at(records_,p):
    oldweight,newweight=tail_weights(p)
    oldpolys=oldweight*sum((a*a for _,_,a,_ in records_),F())
    alignedpolys=newweight*sum((b*b for _,_,_,b in records_),F())
    y=B/2
    pole=F(2,3)*y/(1-y*y)
    polecharge=oldweight*pole*pole
    old=oldpolys+polecharge
    new=alignedpolys+polecharge
    return {
        "cutoff":2**p,"source_count":len(records_)+1,
        "endpoint_zero_original_source_directions":len(records_),
        "unchanged_nonzero_boundary_pole_directions":1,
        "unaligned_source_coefficient_tail_upper":str(old),
        "aligned_source_coefficient_tail_upper":str(new),
        "ratio_in_DISTINCT_coefficient_bases":str(old/new),
        "aligned_scalar_smaller":new<old,
        "aligned_scalar_float_for_diagnostic_only":float(new)
    }

def regression():
    data=records([(F(37,64),0),(F(37,64),1),(F(38938,100),0),
                  (F(3,4),5),(F(896),0)])
    assert len(data)==5
    assert unaligned_envelope(F(1),0)==F(1,3)+2*B
    assert unaligned_envelope(F(1),1)==F(2,3)*B+B**2
    first,second=tail_weights(24)
    assert all(second*gamma*gamma<first*a*a
               for _,_,a,gamma in data)
    result=bound_at(data,24)
    assert result["aligned_scalar_smaller"]
    return True

def original():
    from validate_rpb108_odd470_strong_domain_tail import source_envelopes
    original_sources,pole_envelope=source_envelopes()
    assert len(original_sources)==469 and pole_envelope>0
    data=records([(c,k) for c,k,_ in original_sources])
    assert all(c==c0 and k==k0 and a==a0 for
               (c,k,a,_),(c0,k0,a0) in zip(data,original_sources))
    out={
      "status":"EXACT_CONDITIONAL_ORIGINAL_470_POLE_ALIGNED_STRONG_TAIL_ONLY",
      "original_exceptional_source_dimension":470,
      "SI29_augmented_trial_dimension_upper":484,
      "original_source_space_UNCHANGED":True,
      "endpoint_alignment_coefficients_are_EXACT_real_not_rationalized":True,
      "whole_original_high_frequency_and_pole_paid":True,
      "original_SI10_cluster_geometry_replayed":True,
      "rational_regression":regression(),
      "cutoffs":{str(2**p):bound_at(data,p) for p in (11,12,13,16,20,24)},
      "original_Fourier_form_operator_identification_independently_audited":False,
      "original_470_source_AJ_CJ_DB_calculated":False,
      "signed_odd_even_Weil_CC27_RH":"OPEN"
    }
    # Only a coordinate-basis scalar upper; never promote as an
    # invariant original-J source Gram or Galerkin residual upper.
    assert all(z["source_count"]==470 for z in out["cutoffs"].values())
    return out

if __name__=="__main__":
    print(json.dumps(original(),indent=2))
