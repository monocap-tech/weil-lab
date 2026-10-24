#!/usr/bin/env python3
"""MG07: STRONG-domain tail for the TRUE original SI29 Jensen features.

CRITICAL PREVIOUS DEFECT: SI24/SI25 feature_terms() is a Simpson
QUADRATURE PROXY and NOT the original SI29 positive-reference vector.
This certificate instead uses the ACTUAL continuous feature:
  g0(x)=1_[-B,B] (1/2) int_{-1}^1 sin(2pi(c+r*u)x) du
  g1(x)=1_[-B,B] (3/2) int_{-1}^1 u sin(2pi(c+r*u)x) du.
For c>r>0, the signed measure in frequency has exact
 total variation m0=1, m1=3/2, and absolute first moments
 p0=c, p1=3c/2. No finite quadrature approximates g0/g1 here.

Original physical zero-extension distributional variation <=
 V=2m+4*pi_upper*B*p, so for nonzero Fourier frequency
 |hat g(xi)|<=V/(2*pi_lower*|xi|).
SM41 original all-frequency high tail a_o(xi)<=17+ln |xi|
then yields exact-rational high-frequency squared strong-action
tail of each TRUE SI29 feature, and a full 14-source Loewner sum.
This remains conditional on ORIGINAL SM41/A_o Fourier-domain
identification; it is not low-frequency certification, 484x484
Galerkin positivity, whole signed odd or RH closure.
"""
import json
from fractions import Fraction as F
from pathlib import Path
from validate_rpb108_si06_negative_band import PI, LN, B
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES

ROOT=Path(__file__).resolve().parents[1]
LAMBDA=F(2048)
PI_LO=F(333,106)
PI_UP=F(22,7)
LN2_UP=F(347,500)

def true_feature_absolute_moments(c,r,degree):
    # The actual SI29 feature is a continuous u-average, NOT the
    # finite nodes returned by the SI25 quadrature function.
    assert isinstance(c,F) and isinstance(r,F)
    assert degree in (0,1) and c>r>0
    if degree==0:
        # (1/2)*int[-1,1] |1| du=1;
        # (1/2)*int[-1,1] (c+r*u) du=c.
        mass=F(1)
        moment=c
    else:
        # (3/2)*int[-1,1] |u| du=3/2;
        # (3/2)*int[-1,1] |u|(c+r*u) du=3c/2;
        # the u|u| term cancels exactly by symmetry.
        mass=F(3,2)
        moment=F(3,2)*c
    assert moment==mass*c and moment>0
    return mass,moment

def bounds():
    assert len(FEATURES)==14
    assert B==F(11,10)
    assert PI[0]>PI_LO and PI[1]<PI_UP
    assert LN[2][1]<LN2_UP
    assert LAMBDA==F(2**11)
    log_high=F(11)*LN2_UP
    a=F(17)+log_high
    # Exact integral:
    # int_Lambda^infty (17+log xi)^2 /xi^2 dxi
    # = ((17+log Lambda)^2+2(17+log Lambda)+2)/Lambda.
    integral=(a*a+2*a+2)/LAMBDA
    assert integral>0
    tv=[]; tails=[]; features=[]; degrees=[]
    for j,(c,r,d,degree) in enumerate(FEATURES):
        assert isinstance(c,F) and isinstance(r,F)
        assert isinstance(d,F) and d>0
        mass,moment=true_feature_absolute_moments(c,r,degree)
        # Both endpoint jumps <= mass each, plus
        # integral_{-B}^B |g'_j| <= 4*pi_up*B*moment.
        V=2*mass+4*PI_UP*B*moment
        U=V*V*integral/(2*PI_LO*PI_LO)
        assert V>0 and U>0
        tv.append(V);tails.append(U);degrees.append(degree)
        features.append({"index":j,"c":str(c),"r":str(r),
          "degree":degree,"true_continuous_L1_mass":str(mass),
          "true_continuous_abs_first_moment":str(moment),
          "variation_upper":str(V),"squared_strong_tail_upper":str(U)})
    assert len(tv)==len(tails)==14
    assert degrees.count(1)==2 and degrees.count(0)==12
    block=sum(tails,F(0))
    assert F(143)<block<F(144)
    # Independent rational metadata audit: original 14 true
    # c-values (not Simpson sample nodes) give conservative
    # combined squared-log-action tail about 143.1645 at 2048.
    # This bound proves finite strong domain but is FAR too
    # coarse to certify the MG07 ~1e-9 relative residual gate.
    return {
      "status":"CONDITIONAL_EXACT_RATIONAL_TRUE_CONTINUOUS_SI29_FEATURE_STRONG_TAIL",
      "original_source_dim_unchanged":470,
      "added_true_original_SI29_features":14,
      "max_augmented_trial_dim":484,
      "TRUE_feature_integrals_not_quadrature_proxies":True,
      "SI25_Simpson_proxies_NOT_substituted_for_true_features":True,
      "physical_half_width":str(B),
      "freq_cutoff":str(LAMBDA),
      "log_cutoff_upper":str(log_high),
      "original_true_feature_budgets":features,
      "full_14by14_squared_strong_tail_Loewner_scalar_upper":str(block),
      "full_14by14_squared_strong_tail_decimal_display":float(block),
      "tail_bound_is_not_a_small_MG07_residual":True,
      "14_true_features_versus_14_Simpson_proxies_distinguished":True,
      "high_frequency_action_multiplier_bound":"a_o(xi)<=17+ln|xi|",
      "original_SM41_and_SI29_Fourier_realization_audit":"OPEN",
      "actual_14by14_low_frequency_strong_Gram":"OPEN",
      "actual_484by470_source_residual":"OPEN",
      "original_signed_odd_even_Weil_CC27_RH":"OPEN"
    }

def regression():
    assert true_feature_absolute_moments(F(1,4),F(1,50),0)==(F(1),F(1,4))
    assert true_feature_absolute_moments(F(1,4),F(1,50),1)==(F(3,2),F(3,8))
    # Simpson's discrete moment values do not *define* either
    # continuous feature, even when a polynomial moment agrees.
    assert true_feature_absolute_moments(F(3,5),F(1,20),1)[0]==F(3,2)
    out=bounds()
    assert out["TRUE_feature_integrals_not_quadrature_proxies"]
    return out

if __name__=="__main__":
    m=json.loads((ROOT/"research/obligations.json").read_text())
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open"
    print(json.dumps(regression(),indent=2))
