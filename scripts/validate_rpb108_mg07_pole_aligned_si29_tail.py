#!/usr/bin/env python3
"""MG07 original SI29 14 TRUE feature pole-aligned strong-action tail.

The TRUE SI29 Jensen means/moments G are NOT Simpson proxies.
The original 470-source J contains genuine pole s(x)=sinh(x/2).
For each true odd SI29 feature g_j, put
  h_j(x)=g_j(x)-alpha_j*s(x), alpha_j=g_j(B)/s(B).
These are SAME trial span(J,G), but vanish at +/-B and their
zero-extended Fourier transforms decay O(xi^-2), not O(xi^-1).

The proof uses exact rational upper bounds only:
 |alpha_j| <= 2*b_j/B (since sinh(B/2)>=B/2),
 b_j <= min(1, pi_up*dist(2cB,Z)) for true Jensen means,
 b_j <= 2*pi_up*r*B for genuine odd first moments,
 |g_j'(B)|<=2*pi_up*p_j,
 int[-B,B]|g_j''| <=8B*pi_up^2*q_j,
 p_j=m_j*c, q_j=m_j*(c+r)^2, m_j=1 or 3/2.
 Pole correction adds <=|alpha_j|(2cosh(B/2)-1) to
  2|h_j'(B)|+int|h_j''|; cosh(B/2)<6/5 by a geometric
 rational majorant.
 Two true physical IBPs give |hat h_j(xi)|<=gamma_j/xi^2.
 Original SM41 high-frequency a_o(xi)<=17+ln|xi| yields
 2 gamma_j^2/(3L^3)*[A^2+(2/3)A+2/9], A=17+ln L.
 Full 14x14 Loewner upper=sum_j U_j, exact rational.

Important: this is a NEW POLE-ALIGNED BASIS of the SAME
SI29-augmented trial span, not a new positive-reference operator
or a bound on the unmodified g_j. No actual 484-by-470 source
residual or signed odd positivity is asserted.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from validate_rpb108_si06_negative_band import PI,LN,B
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES
from validate_rpb108_mg07_si29_feature_strong_tail import (
    true_feature_absolute_moments, PI_LO, PI_UP, LN2_UP, bounds
)

ROOT=Path(__file__).resolve().parents[1]
COSH_UP=F(6,5)

def absolute_boundary_bound(c,r,degree):
    assert degree in (0,1) and c>r>0
    if degree==1:
        # Integral odd-u cancellation is EXACT in the real
        # continuous first moment, not a Simpson numerical effect.
        return 2*PI_UP*r*B
    # g0(B)=sin(2pi c B)*sinc(2pi r B)
    # |sin(pi y)|<=pi_up*dist(y,Z), |sinc|<=1.
    y=2*c*B
    n=(y+F(1,2)).numerator//(y+F(1,2)).denominator
    assert abs(y-n)<=F(1,2)
    return min(F(1),PI_UP*abs(y-n))

def exact_aligned_tails():
    assert len(FEATURES)==14
    assert B==F(11,10) and PI[0]>PI_LO and PI[1]<PI_UP
    assert LN[2][1]<LN2_UP
    assert COSH_UP>1/(1-(B/2)**2/2)
    assert COSH_UP==F(6,5)
    # True original added trial directions are h_j=g_j-alpha_j*s,
    # where s belongs to original 470D source synthesis.
    # Consequently span(J,g_1..g_14)=span(J,h_1..h_14).
    dirs=[]
    for j,(c,r,d,degree) in enumerate(FEATURES):
        mass,p=true_feature_absolute_moments(c,r,degree)
        b=absolute_boundary_bound(c,r,degree)
        assert b>=0
        alpha_bound=2*b/B
        q=mass*(c+r)**2
        d_g=4*PI_UP*p+8*B*PI_UP**2*q
        d_pole=alpha_bound*(2*COSH_UP-1)
        gamma=(d_g+d_pole)/(4*PI_LO**2)
        assert gamma>0
        dirs.append((gamma,j,c,r,degree,b,alpha_bound))
    totals={}
    for log2cut in (11,12,13,14):
        L=F(2**log2cut)
        A=F(17)+log2cut*LN2_UP
        integral=(A*A+F(2,3)*A+F(2,9))/(3*L**3)
        value=sum((2*gamma*gamma*integral
                   for gamma,*_ in dirs),F(0))
        assert value>0
        totals[str(int(L))]=value
    assert totals["2048"]<F(3,40000) # <0.000075
    assert totals["8192"]<F(7,5000000) # <0.0000014
    assert totals["16384"]<F(1,5000000) # <0.0000002
    old=F(bounds()["full_14by14_squared_strong_tail_Loewner_scalar_upper"])
    phase_old=F(bounds()["phase_refined_two_IBP_14_feature_tail_upper"])
    assert F(143)<old<F(144)
    assert F(3,5)<phase_old<F(31,50)
    assert old/totals["2048"]>F(1900000)
    assert phase_old/totals["2048"]>F(8000)
    return {
      "status":"CONDITIONAL_EXACT_ORIGINAL_POLE_ALIGNED_SI29_14D_LOG_STRONG_TAIL",
      "true_original_J_source_dim":470,
      "true_original_SI29_augmented_trial_dim_at_most":484,
      "all_genuine_14_continuous_Jensen_features":True,
      "pole_source_s_is_in_original_J":True,
      "new_basis_hj_equals_gj_minus_endpoint_pole_multiple":True,
      "same_original_trial_span_exact":True,
      "endpoints_of_every_new_trial_feature_zero_exactly":True,
      "original_pole_coefficient_transcendental_not_approximated":True,
      "cosh_upper":str(COSH_UP),
      "cutoff_tail_upper_exact":{k:str(v) for k,v in totals.items()},
      "cutoff_tail_upper_decimal_display":{k:float(v) for k,v in totals.items()},
      "prior_true_feature_variation_14D_tail_at_2048":str(old),
      "prior_true_feature_phase_IBP_14D_tail_at_2048":str(phase_old),
      "improvement_over_initial_true_feature_variation":str(old/totals["2048"]),
      "improvement_over_phase_IBP":str(phase_old/totals["2048"]),
      "14_original_feature_boundary_and_pole_coeff_uppers":[{
          "index":j,"center":str(c),"radius":str(r),
          "degree":degree,"endpoint_bound":str(b),
          "abs_alpha_j_upper":str(alpha),
          "two_IBP_gamma_j":str(gamma)
        } for gamma,j,c,r,degree,b,alpha in dirs],
      "actual_original_484_by_470_low_strong_Gram":"OPEN",
      "true_original_470_source_G_N_Ritz_residual":"OPEN",
      "SI29_SM41_physical_form_domain_review":"OPEN",
      "signed_odd_even_Weil_CC27_RH":"OPEN"
    }

if __name__=="__main__":
    m=json.loads((ROOT/"research/obligations.json").read_text())
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open"
    print(json.dumps(exact_aligned_tails(),indent=2))
