#!/usr/bin/env python3
"""MG07 original signed-ray high-tail: use SI10 NEGATIVE SUPPORT mass.

For ORIGINAL signed m and Kminus=(kappa-m)_+, m_- <= Kminus.
SI10's true complete positive-frequency negative-cover intervals
[a,b] have Kminus <=h+kappa; outside them m>=kappa>0.
The exact full-two-signs SI10 weighted envelope mass is
 Mneg+kappa*W=1204033883/32000000 < 38.
For each TRUE physical original two-source f, two-IBP gives
 |T_f(xi)| <= beta_32/|xi| for EVERY |xi|>=32.
Hence on ALL real |xi|>=32, exactly
 ∫(-m)_+ |Tf|² <= (beta_32/32)^2 * M_SI10.
This is ~21x sharper than a uniform SI06 pointwise ceiling
 M0∫_{|xi|>=32}|Tf|² <= M0*2*beta²/32.

Every original nonnegative complement, original seven-prime band,
source endpoint and both frequency signs are paid. This is ONLY
a tail certificate; low32 original signed energy, signed universal
odd positivity, even, Weil and RH remain OPEN.
"""
from fractions import Fraction as F
import json
from pathlib import Path
from validate_rpb108_si06_negative_band import CONST_UP,TWOC
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_mg07_two_source_endpoint_log_tail import run

ROOT=Path(__file__).resolve().parents[1]
CUTOFF=F(32)
MASS_EXACT=F(1204033883,32000000)
UNIFORM_UP=CONST_UP+F(70751,10000)

def support_tail():
    clusters,width,mneg,mass=full_upper_leaves()
    assert len(clusters)==107
    assert sum(map(len,clusters))==973
    assert KAPPA==F(1,1000)
    assert width==F(973,32)
    assert mass==mneg+KAPPA*width==MASS_EXACT
    assert F(37)<mass<F(38)
    assert 0<TWOC<F(70751,10000)
    # Every actual original SI10 positive-frequency leaf I=[l,r]
    # bounds Kminus by its genuine h+kappa. Integrate the full
    # Fourier 1/xi² decay on I∩[32,∞), not a global cutoff max:
    # 2*∫_l^r (h+k)/xi² dxi = 2*(h+k)*(1/l-1/r).
    # Factor TWO is for both physical frequency signs ONLY here.
    weighted_reciprocal=F(0)
    high_band_mass=F(0)
    positive_half_high_leaves=0
    high_clusters=0
    for cluster in clusters:
        cluster_has_high=False
        for l,r,h in cluster:
            if r<=CUTOFF:continue
            start=max(l,CUTOFF)
            assert 0<start<r<=F(896)
            weight=h+KAPPA
            assert weight>=KAPPA
            portion=2*weight*(r-start)
            high_band_mass+=portion
            weighted_reciprocal+=2*weight*(1/start-1/r)
            positive_half_high_leaves+=1
            cluster_has_high=True
        high_clusters+=int(cluster_has_high)
    assert F(0)<high_band_mass<mass
    assert F(0)<weighted_reciprocal<high_band_mass/CUTOFF**2
    assert high_clusters>0 and positive_half_high_leaves>0
    actual=run()
    result=[]
    for ray in actual["rays"]:
        assert "32" in ray["all_frequency_cutoff_budgets"]
        beta=F(ray["all_frequency_cutoff_budgets"]["32"]["exact_upper_beta"])
        # BOTH frequency signs are already included in original
        # M=2*sum_leaf hwidth, so do NOT multiply by two again.
        previous_support_mass=mass*beta*beta/(CUTOFF*CUTOFF)
        supported=weighted_reciprocal*beta*beta
        uniform=UNIFORM_UP*2*beta*beta/CUTOFF
        assert 0<supported<previous_support_mass<uniform
        assert uniform/supported>F(20)
        # Weighted reciprocal 1/xi² is integrated on actual
        # original leaves and both frequency halves EXACTLY.
        assert supported<F(38)*beta*beta/F(1024)
        result.append({
          "ray":ray["purpose"],
          "original_sine_coefficient":ray["sine_coefficient"],
          "original_sinh_coefficient":ray["pole_coefficient"],
          "exact_beta_at_32":str(beta),
          "entire_true_original_signed_negative_high_tail_upper":str(supported),
          "previous_whole_SI10_mass_over_cutoff_squared_upper":str(previous_support_mass),
          "exact_leaf_reciprocal_improvement_factor":str(previous_support_mass/supported),
          "entire_true_original_signed_negative_high_tail_decimal":float(supported),
          "previous_uniform_SI06_high_tail_upper":str(uniform),
          "certified_improvement_factor":str(uniform/supported),
          "signed_low_0_32_exact_lower":"OPEN",
          "original_signed_ray_positive":"OPEN"})
    assert len(result)==2
    return {
      "status":"CONDITIONAL_EXACT_ORIGINAL_SI10_SUPPORTED_SIGNED_HIGH_TAIL",
      "original_frequencies_covered":"both signs, all real |xi|>=32",
      "original_negative_support_upper_frequency":896,
      "original_SI10_positive_half_clusters":107,
      "original_SI10_full_unresolved_leaves":973,
      "SI10_complete_original_two_signs_negative_cap_mass":str(mass),
      "SI10_true_two_signs_cap_mass_above_32":str(high_band_mass),
      "SI10_actual_half_frequency_negative_leaves_above_32":positive_half_high_leaves,
      "SI10_original_clusters_touching_high_band":high_clusters,
      "SI10_exact_frequency_weighted_reciprocal_integral":str(weighted_reciprocal),
      "reciprocal_leafwise_tail_rigorous":True,
      "mass_below_38":True,
      "SI06_uniform_tail_charge_replaced_by_true_support_mass":True,
      "reused_true_2_IBP_original_physical_source_bounds":True,
      "signed_original_odd_operator_universal_sign":"OPEN",
      "original_signed_even_CC27_Weil_RH":"OPEN",
      "rays":result}
if __name__=="__main__":
    m=json.loads((ROOT/"research/obligations.json").read_text())
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open"
    print(json.dumps(support_tail(),indent=2))
