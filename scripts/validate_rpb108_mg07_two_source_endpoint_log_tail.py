#!/usr/bin/env python3
"""Exact ORIGINAL rational 2-source Fourier tail with endpoint cancellation.

These are true SI10/SM35 original odd physical two-source rays:
 f=a sin(2pi*(37/64)x)+b sinh(x/2) on [-B,B], zero extended.
Use SI14 exact rational pi-phase sin/cos intervals and SI12
sinh/cosh Taylor intervals to certify ORIGINAL endpoint cancellation.

Two real physical integrations by parts:
 |fhat(xi)| <= |f(B)|/(pi |xi|)
      +(2|f'(B)| + ||f''||_L1)/(4pi² xi²)
 <= beta_Lambda/|xi| for all |xi|>=Lambda.
Here ||f''||_L1<=2B a(2pi_up c)²+b(cosh_hi(B/2)-1).
SM41 full ORIGINAL seven-prime digamma a_o(xi)<=17+ln|xi|
then gives exact outward high-frequency original Ao FORM and
squared STRONG action tail on the TRUE physical rays:
 form <= 2 beta²(18+ln Lambda)/Lambda
 strong <= 2 beta²((17+ln Lambda)²+2(17+ln Lambda)+2)/Lambda.

This is a piece of the ORIGINAL upper Ao energy; it does NOT
compute its low-frequency component or the full same-SM40 cap
energy lower, and therefore does not claim a method obstruction.
"""
from fractions import Fraction as F
import json
from pathlib import Path
from validate_rpb108_si06_negative_band import PI,LN,B
from validate_rpb108_si12_even_supported_inverse import sinh_bounds,cosh_bounds
from validate_rpb108_si14_odd_multiband_nogo import cos_sin_pi_multiple
from validate_rpb108_mg07_two_source_original_physical_pole_input import (
    CENTER,RAYS,evaluate as physical_anchor,mul,add,scl
)

ROOT=Path(__file__).resolve().parents[1]
PI_LO=F(333,106)
PI_UP=F(22,7)
LOG2_HI=F(347,500)

def abs_upper(x):
    return max(abs(x[0]),abs(x[1]))
def run():
    assert B==F(11,10) and CENTER==F(37,64)
    assert PI[0]>PI_LO and PI[1]<PI_UP
    assert LN[2][1]<LOG2_HI
    y=2*B*CENTER
    sinB,cosB=cos_sin_pi_multiple(y)
    sh=sinh_bounds(B/2)
    ch=cosh_bounds(B/2)
    k=(2*PI[0]*CENTER,2*PI[1]*CENTER)
    phys=physical_anchor()
    assert len(phys["rays"])==2
    rayinfo=[]
    for (a,b,label),anchor in zip(RAYS,phys["rays"]):
        assert anchor["purpose"]==label
        endpoint=add(scl(a,sinB),scl(b,sh))
        derivative=add(scl(a,mul(k,cosB)),scl(F(b,2),ch))
        endpoint_abs=abs_upper(endpoint)
        derivative_abs=abs_upper(derivative)
        # Integral |b sinh(x/2)/4|: exact b*(cosh(B/2)-1)
        second_l1=2*B*a*(2*PI_UP*CENTER)**2+b*(ch[1]-1)
        assert second_l1>0
        assert endpoint_abs<F(425) if label.startswith("direct") else endpoint_abs<F(97)
        assert derivative_abs<F(19200) if label.startswith("direct") else derivative_abs<F(4850)
        naive_u=F(a,2)+F(2*b,5)
        assert naive_u>endpoint_abs/PI_LO
        norm_lo=F(anchor["complete_true_physical_norm_squared_interval"][0])
        assert norm_lo>0
        budgets={}
        for power in (11,12,13,14):
            cutoff=F(2**power)
            assert cutoff>2*CENTER
            ln_hi=power*LOG2_HI
            A=17+ln_hi
            beta=endpoint_abs/PI_LO+(
                2*derivative_abs+second_l1)/(4*PI_LO**2*cutoff)
            assert beta>0
            form=2*beta**2*(A+1)/cutoff
            strong=2*beta**2*(A*A+2*A+2)/cutoff
            unaligned_form=2*naive_u**2*(A+1)/cutoff
            improvement=unaligned_form/form
            assert improvement>F(7000)
            relative_form=form/norm_lo
            relative_strong=strong/norm_lo
            if power==11:
                assert relative_form<F(1,500000)
                assert relative_strong<F(1,20000)
            if power==11:
                if label.startswith("direct"):
                    assert form<F(500) and strong<F(13000)
                else:
                    assert form<F(26) and strong<F(670)
            budgets[str(int(cutoff))]={
                "exact_upper_beta":str(beta),
                "Ao_positive_form_tail_upper":str(form),
                "Ao_squared_strong_tail_upper":str(strong),
                "naive_uncancelled_form_upper":str(unaligned_form),
                "rigorous_improvement_factor":str(improvement),
                "Ao_form_tail_over_true_L2_norm_upper":str(relative_form),
                "Ao_squared_strong_tail_over_true_L2_norm_upper":str(relative_strong),
                "display_form_tail_upper":float(form),
                "display_squared_strong_tail_upper":float(strong)
            }
        rayinfo.append({
            "purpose":label,"sine_coefficient":a,"pole_coefficient":b,
            "real_original_physical_endpoint_interval":[str(z) for z in endpoint],
            "real_original_physical_endpoint_absolute_upper":str(endpoint_abs),
            "real_original_physical_first_derivative_interval":[str(z) for z in derivative],
            "real_original_physical_first_derivative_absolute_upper":str(derivative_abs),
            "original_second_derivative_L1_upper":str(second_l1),
            "all_frequency_cutoff_budgets":budgets,
            "true_Ao_low_band_upper_computed":False,
            "matched_true_SM40_cap_lower_computed":False
        })
    return {
      "status":"CERTIFIED_CONDITIONAL_EXACT_ORIGINAL_TWO_SOURCE_Ao_LOG_HIGH_TAIL",
      "sine_center":str(CENTER),
      "two_original_rays_kept_separate":True,
      "genuine_SI14_phase_interval_and_SI12_pole_Taylor":True,
      "whole_original_SM41_high_log_multiplier_inherited":True,
      "two_physical_IBPs_both_endpoint_and_derivative_paid":True,
      "physical_norm_and_pole_rational_inputs":phys,
      "rays":rayinfo,
      "exact_original_low_frequency_positive_form":"OPEN",
      "exact_original_matched_SM40_cap_ray_lower":"OPEN",
      "original_signed_odd_even_CC27_Weil_RH":"OPEN"}
if __name__=="__main__":
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    assert manifest["active_obligation"]=="W-ODD-NEG"
    assert manifest["objective"]["status"]=="open"
    print(json.dumps(run(),indent=2))
