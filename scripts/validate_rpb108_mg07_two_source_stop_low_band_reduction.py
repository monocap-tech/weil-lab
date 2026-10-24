#!/usr/bin/env python3
"""Exact original two-ray method-stop reduction: low-frequency ONLY.

For original J-only MG07 Ritz, the cap-only necessary test is
  C_SM40(f) <= theta*Astar(f).
Since Kcap_SM40 >= Kminus and theta_SM40 < 97/100 (SM40 exact),
a rigorously certified
  Kminus_low(f) > (97/100)*(Ao_low(f)+T_Ao_high(f)-PolePayment(f))
would REFUTE ONLY the fixed J-only Ritz + SM40 sufficient method.

This script proves the full algebra and imports the actual exact
original physical pole and original high-log two-IBP tail certificates;
it does NOT invent the missing two LOW integral bounds. It outputs
the precise exact Fraction low-band required threshold:
 Kminus_low - 97/100*Ao_low > 97/100*(T_high - PolePayment_LO).
No unproven m-frequency quadrature is accepted as a certificate.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from validate_rpb108_mg07_two_source_endpoint_log_tail import run
THETA=F(97,100)
ROOT=Path(__file__).resolve().parents[1]

def exact_reduction():
    tail=run()
    p=tail["physical_norm_and_pole_rational_inputs"]
    assert len(tail["rays"])==len(p["rays"])==2
    rays=[]
    for t,physical in zip(tail["rays"],p["rays"]):
        assert t["purpose"]==physical["purpose"]
        assert t["sine_coefficient"]==physical["rational_sine_coefficient"]
        assert t["pole_coefficient"]==physical["rational_pole_coefficient"]
        hi=F(t["all_frequency_cutoff_budgets"]["2048"]["Ao_positive_form_tail_upper"])
        payment_lo=F(physical[
            "genuine_Astar_pole_subtraction_2overlap_squared_interval"][0])
        norm_lo=F(physical["complete_true_physical_norm_squared_interval"][0])
        assert payment_lo>hi>0
        assert hi/norm_lo<F(1,500000)
        rhs=THETA*(hi-payment_lo)
        if t["purpose"].startswith("direct"):
            assert F(-60000000)<rhs<F(-59000000)
        else:
            assert F(-3800000)<rhs<F(-3700000)
        rays.append({
          "ray":t["purpose"],
          "exact_b9_center":tail["sine_center"],
          "sine_coefficient":t["sine_coefficient"],
          "sinh_coefficient":t["pole_coefficient"],
          "rational_stop_comparison_theta":str(THETA),
          "certified_positive_high_tail_upper":str(hi),
          "certified_pole_payment_lower":str(payment_lo),
          "certified_strict_low_band_difference_threshold":str(rhs),
          "required_original_low_band_comparison":
            "Kminus_low_LO-(97/100)*Ao_low_HI > threshold",
          "Kminus_low_LO":"OPEN",
          "Ao_low_HI":"OPEN",
          "true_matched_SM40_cap_not_replaced_by_direct_samples":True,
          "physical_ray_original_method_stop_certified":False
        })
    return {
      "status":"CONDITIONAL_EXACT_TWO_SOURCE_LOW_BAND_ONLY_METHOD_STOP_REDUCTION",
      "original_470_exceptional_source_map_unchanged":True,
      "SM40_theta_exact_known_strictly_less_than_97_over_100":True,
      "theta_comparison_97_over_100_is_stronger_than_original_SM40_theta":True,
      "original_real_frequency_cutoff":2048,
      "a_o_high_frequency_operator_tail_proved_exact":True,
      "original_rank_one_odd_pole_payment_proved_exact":True,
      "all_low_frequency_integral_bounds":"OPEN",
      "specific_source_only_Ritz_SM40_method_stopped":False,
      "full_signed_odd_even_Weil_CC27_RH":"OPEN",
      "rays":rays
    }
if __name__=="__main__":
    ledger=json.loads((ROOT/"research/obligations.json").read_text())
    assert ledger["active_obligation"]=="W-ODD-NEG"
    assert ledger["objective"]["status"]=="open"
    print(json.dumps(exact_reduction(),indent=2))
