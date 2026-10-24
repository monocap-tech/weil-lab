#!/usr/bin/env python3
"""MG07 SI29-augmented Ritz: exact per-ray Young-parameter feasibility.

For genuine original nonnegative n=Z*Kcap Z, d=(Hinf/
(kappa_star*kappa))*R*R, and g=Z*Astar Z>0, the augmented
MG07 sufficient Loewner gate needs for ONE t>0
 (1+t)n + (1+1/t)d <=theta*g.
The infimum over t>0 is (sqrt(n)+sqrt(d))**2.
A rational ray with (sqrt(n)+sqrt(d))**2>theta*g rules
out EVERY global t for this SPECIFIC augmented trial and cap,
NOT signed odd positivity or a different approximation.
No original ray inputs are constructed by this small validator.
"""
from fractions import Fraction as F
import json
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm17_compact_spectral_gate import KAPPA_STAR
from validate_rpb108_mg07_global_negative_sup import exact_bound

THETA_OLD=F(51,56)
THETA_PAID_SAFE=F(14937022508400793,16000000000000000)

def classify_strict_ray(n,d,g,theta):
    assert all(isinstance(x,F) for x in (n,d,g,theta))
    assert n>=0 and d>=0 and g>0 and 0<theta<=1
    delta=theta*g-n-d
    # Strict positive reserve exists for this ray with finite t>0
    # iff theta*g > (sqrt(n)+sqrt(d))^2.
    possible=delta>0 and delta*delta>4*n*d
    # Non-strict Young feasibility: a zero component can make the
    # infimum unattainable except when both vanish.
    weak=(delta>0 and delta*delta>=4*n*d) or (
        delta==0 and n>0 and d>0 and delta*delta==4*n*d)
    return dict(strict=possible,weak=weak,delta=delta,
                discriminant=delta*delta-4*n*d)

def exact_tests():
    assert classify_strict_ray(F(1,4),F(1,9),F(1),F(1))["strict"]
    q=classify_strict_ray(F(1,4),F(1,4),F(1),F(1))
    assert not q["strict"] and q["weak"]
    q=classify_strict_ray(F(3,4),F(1,4),F(1),F(1))
    assert not q["strict"] and not q["weak"]
    assert classify_strict_ray(F(0),F(1,2),F(1),F(1))["strict"]
    assert not classify_strict_ray(F(0),F(1),F(1),F(1))["weak"]
    assert classify_strict_ray(F(0),F(0),F(1),F(1))["strict"]
    sup=exact_bound()
    H=F(sup["original_negative_norm_upper"])
    k=KAPPA;ks=KAPPA_STAR
    assert H==F(871887,70000)
    assert k==F(1,1000) and ks==F(33621,10**9)
    coeff=H/(ks*k)
    # For all t>0, the residual-only portion already requires
    #   D/G0 < theta * ks*k/H
    # (strict version, ignoring the nonzero negative cap charge).
    necessary_old=THETA_OLD/coeff
    necessary_paid=THETA_PAID_SAFE/coeff
    assert necessary_old<F(1,10**8)
    assert necessary_paid<F(1,10**8)
    assert necessary_old<necessary_paid<1/coeff
    return {
      "status":"EXACT_YOUNG_PARAMETER_RAY_FAIL_FAST_ALGEBRA_ONLY",
      "original_source_dim":470,"augmented_trial_dim_upper":484,
      "original_Hinfty":str(H),
      "reference_residual_coefficient_H_over_kappastar_kappa":str(coeff),
      "coefficient_float_display":float(coeff),
      "theta_original_51_over_56":str(THETA_OLD),
      "theta_safe_kappa_paid":str(THETA_PAID_SAFE),
      "necessary_D_over_G0_limit_at_old_theta":str(necessary_old),
      "necessary_D_over_G0_limit_at_safe_theta":str(necessary_paid),
      "necessary_D_over_G0_limit_safe_decimal":float(necessary_paid),
      "scalar_exact_adversarial_regressions":True,
      "entire_original_470_ray_n_d_g_computed":False,
      "global_single_t_Loewner_test":"OPEN",
      "odd_even_Weil_CC27_RH":"OPEN"}
if __name__=="__main__":
    print(json.dumps(exact_tests(),indent=2))
