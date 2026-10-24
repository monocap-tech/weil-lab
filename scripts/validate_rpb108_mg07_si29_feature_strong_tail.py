#!/usr/bin/env python3
"""Exact-rational SI29 14-feature original STRONG-domain Fourier tail.

The genuine original Jensen feature is a finite linear combination
  gj(x)=1_{[-B,B]} sum_k w_jk sin(2 pi nu_jk x)
with exact rational SI25/SI29 Simpson frequencies and coefficients.
Integration by parts on the TRUE odd supported zero extension gives
  |hat gj(xi)| <= TV_j/(2 pi |xi|),
  TV_j=2 sum |w| + 4 pi_up B sum |w| |nu|.
For |xi|>=Lambda original SM41 A_o multiplier obeys
  a_o(xi)<=17+ln|xi|,
yielding an ENTIRE real-frequency squared-strong-form tail
  <= TV_j^2/(2 pi_lo^2 Lambda)
    * ((17+ln Lambda)^2+2(17+ln Lambda)+2).
By Cauchy all fourteen source combinations are bounded by the sum
of these rational diagonal tail bounds as a scalar Loewner upper.
This does NOT certify the full low-frequency Gram, original signed
odd PSD, or independent SI29/SM41 Fourier identifications.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from validate_rpb108_si06_negative_band import PI, LN, B
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES
from validate_rpb108_si25_first_moment_bessel import feature_terms

ROOT=Path(__file__).resolve().parents[1]
LAMBDA=2048
PI_LOW=F(333,106)
PI_UP=F(22,7)
LN2_UP=F(347,500)

def bounds():
    assert len(FEATURES)==14
    assert B==F(11,10)
    assert PI[0]>PI_LOW and PI[1]<PI_UP
    assert LN[2][1]<LN2_UP
    assert LAMBDA==2**11
    log_high=11*LN2_UP
    a=F(17)+log_high
    integral=(a*a+2*a+2)/LAMBDA
    assert a>F(17) and integral>0
    tv=[];tails=[];nterms=0
    for c,r,d,degree in FEATURES:
        assert degree in (0,1) and c>r>0 and d>0
        terms=tuple(feature_terms(c,r,degree))
        assert terms
        assert all(isinstance(x,F) and isinstance(w,F) for x,w in terms)
        assert all(x>0 for x,w in terms)
        # Bounds full physical interval and endpoints; frequency
        # combinations need not be positive coefficients.
        mass=sum((abs(w) for x,w in terms),F(0))
        moment=sum((abs(w)*abs(x) for x,w in terms),F(0))
        V=2*mass+4*PI_UP*B*moment
        assert V>0
        tail=V*V*integral/(2*PI_LOW*PI_LOW)
        assert tail>0
        tv.append(V);tails.append(tail);nterms+=len(terms)
    block=sum(tails,F(0))
    assert nterms>=14 and block>0
    return {
      "status":"CONDITIONAL_EXACT_RATIONAL_ORIGINAL_SI29_14_FEATURE_STRONG_TAIL",
      "original_source_dim_unchanged":470,
      "added_true_SI29_features":14,
      "total_trial_dim_upper":484,
      "original_odd_physical_support_B":str(B),
      "exact_simpson_terms_used":nterms,
      "lambda":LAMBDA,
      "upper_log_Lambda":str(log_high),
      "exact_feature_variation_budgets":[str(v) for v in tv],
      "exact_individual_squared_strong_tail_uppers":[str(t) for t in tails],
      "complete_14by14_squared_strong_tail_Loewner_scalar_upper":str(block),
      "complete_14by14_squared_strong_tail_decimal":float(block),
      "all_feature_strong_domain_conditional_on_SM41":True,
      "original_low_frequency_feature_action_Gram":"OPEN",
      "full_470_source_augmented_residual":"OPEN",
      "original_signed_odd_even_Weil_CC27_RH":"OPEN"}
if __name__=="__main__":
    m=json.loads((ROOT/"research/obligations.json").read_text())
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open"
    print(json.dumps(bounds(),indent=2))
