#!/usr/bin/env python3
"""NF496 exact original J242-perpendicular residual lower, pole shear invariant.

This is a source-specific exact-Hilbert-space corollary of ACCEPTED
original NF404/NF456/NF478/NF479/NF495 source receipts. It does NOT
evaluate a new Weil source, prove any RH sign, or assert that all
alternative sources/certificate architectures fail.

Original same-source identities:
 E_cent = ||w-a*s||^2 = K+D7+D8,
 R_cent = ||P_J(w-a*s)||^2,
 Q_J(w-a*s)=Q_J w since original s in J242,
 ||Q_J w||^2 = E_cent - R_cent.

Original NF495 D8 raw exact-Fraction artifact is REQUIRED (not a
hand-transcribed decimal). Source immutable NF407/NF406 and all
accepted prior receipts SHA-checked. Conservative original
source-certified K and D7 decimal OUTWARD receipts are weakened rather
than used as point estimates. NF404 original exact 242D R_upper and
original exact complement gamma² budget are used AS RATIONALS.

Crucially any choice of a, ANY additive correction j in J242, or any
change of coordinates of the SAME selected subspace, leaves the
original Q_J w unchanged. For a different physical response w+h
one must change Q_J h by a quantitative minimum; the certificate
threshold itself must remain fixed for that conclusion to apply.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json,sys
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"

def load(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def finite_hilbert_controls():
    # Rational exact finite-dimensional logical countermodels:
    # selected J = span e1, authentic pole s=e1. Recenter or change
    # coordinates in J: Q_J(w-a*s) fixed regardless of a.
    n=0
    w=(F(3),F(5),F(0))
    def norm2(x):return sum((v*v for v in x),F(0))
    def Q(x):return (F(0),x[1],x[2])
    for a in [F(0),F(1),F(7,3),F(-200),F(10)**50]:
        centered=(w[0]-a,w[1],w[2])
        assert Q(centered)==Q(w)
        assert norm2(centered)==(w[0]-a)**2+norm2(Q(w))
        n+=1
    # A selected-source failure does NOT imply no other source can
    # meet a sufficient norm gate, even for the SAME J.
    passed=(F(3),F(0),F(0))
    assert norm2(Q(w))==25>1 and norm2(Q(passed))==0
    n+=1
    # One measured selected source can be consistent with a positive
    # quadratic Weil-model AND an indefinite one agreeing on the
    # actually measured 2D span. Global-sign inference invalid.
    def fpositive(x):return norm2(x)
    def findef(x):return x[0]**2+x[1]**2-x[2]**2
    assert fpositive(w)==findef(w)==34
    assert fpositive((F(0),F(0),F(1)))==1
    assert findef((F(0),F(0),F(1)))==-1
    n+=1
    # Orthogonal 2-ray split: Q²=d12+T with T>=0, never promote
    # d12 alone as the complete Q² or as a global form sign.
    x=(F(1),F(2),F(3))
    assert norm2(Q(x))==13==x[1]**2+x[2]**2
    n+=1
    return n

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--nf495-raw",required=True,
       help="Unmodified exact Fraction JSON artifact from accepted GitHub run #42866700605")
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    # Source and independently accepted original certificates, no new
    # numerical physical source/Weil operator computation.
    original,oss=load("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,sss=load("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    nf404,f404=load("notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
    nf456,f456=load("notes/data/provisional/NF456_original_J242_two_ray_residual_custody.json")
    nf478,f478=load("notes/data/provisional/NF478_original_complete_J7_signed_seven_panel_custody.json")
    nf479,f479=load("notes/data/provisional/NF479_original_full_J8_forced_positive_NF404_transfer_custody.json")
    nf495,f495=load(args.nf495_raw)
    assert oss==SRC and sss==SEAM
    assert nf404["pass"]=="NF404" and nf404["original_dimension"]==242
    assert nf404["original_selected_pole_index"]==241
    assert nf404["fixed_dyadic_pole_coefficient"]=="6677356497477490213/4611686018427387904"
    assert nf404["source_energy_cancellation_reduction"]
    assert nf456["pass"]=="NF456"
    assert nf456["original_source_nf407_sha256"]==SRC and nf456["original_seams_nf406_sha256"]==SEAM
    assert nf456["verification"]["status"]=="SUCCESS" and nf456["verification"]["run"]==41894746033
    assert nf478["pass"]=="NF478" and nf478["source_original_nf407_sha256"]==SRC and nf478["source_original_nf406_seams_sha256"]==SEAM
    assert nf478["independent_full_J7_exact_fraction_artifact"]["json_sha256"]=="91e007c65e8eccf84126073aac7b6a11c41d445284b2f616b6d05151340f1c1f"
    assert nf479["pass"]=="NF479"
    assert nf479["original_nf407_source_sha256"]==SRC and nf479["original_nf406_seams_sha256"]==SEAM
    assert nf479["focused_CI"]["conclusion"]=="SUCCESS" and nf479["focused_CI"]["run_id"]==42498316637
    assert "Efull=K+D7+D8" in nf479["authentic_physical_source_identity"]
    assert nf495["pass"]=="NF494"
    assert nf495["original_nf407_source_sha256"]==SRC and nf495["original_nf406_seams_sha256"]==SEAM
    assert nf495["original_full_J8_D8_signed_upper_numerically_integrated"]
    assert nf495["NF404_original_selected_source_scalar_decision"]=="NF404_SOURCE_SCALAR_CERTAIN_FAIL"
    assert nf495["W_ODD_NEG"]==nf495["RH"]=="OPEN"

    # These original 2 upstream "outward_approx" receipts are
    # themselves ACCEPTED and the strict *weakenings* below lie
    # comfortably outside their certified original outward intervals;
    # do NOT use the printed midpoints as exact actual integrals.
    original_Klo=F(nf479["original_exact_K_outward_approx"][0])
    original_D7lo=F(nf478["original_seven_panel_J7_signed_D_outward"][0])
    K_GUARD=F("1.3363e-21")
    D7_GUARD=F("-4.06954e-22")
    assert K_GUARD<original_Klo and D7_GUARD<original_D7lo
    assert F(nf479["original_exact_source_full_J7_outward_approx"][0])>D7_GUARD
    assert nf478["source_original_nf407_sha256"]==nf479["original_nf407_source_sha256"]

    # ALL original actual J8 (not NF479's earlier conditional lower)
    # comes directly from retained accepted 4096bit 400 H/U source,
    # independent NF495 full physical exact-Fraction artifact.
    D8lo,D8hi=map(F,nf495["original_true_full_J8_signed_D8_outward"])
    assert D8lo<D8hi and D8lo>F("3.2347e-22")
    assert nf495["original_true_full_J8_signed_D8_decimal"][0].startswith("3.23476513")
    assert nf495["original_true_full_J8_signed_D8_decimal"][1].startswith("3.23476513")
    D8_GUARD=F("3.2347e-22")

    # The original selected pole-centered projection R_a^2 is
    # evaluated by NF404 source-exact raw full 242D Gram; DO NOT
    # mix in the uncentered ~0.494 selected projection power.
    Rlo=F(nf404["original_selected_after_pole_shear_power_lower_exact"])
    Rhi=F(nf404["original_selected_after_pole_shear_power_upper_exact"])
    assert F("1.09e-21")<Rlo<=Rhi<F("1.10e-21")
    assert nf404["strict_new_selected_after_pole_shear_power_bracket"]=="109/10^23 < power < 11/10^22"
    R_GUARD=F("1.09501e-21")
    assert Rhi<R_GUARD

    gamma2=F(nf404["exact_source_original_full_complement_power_budget"])
    assert F(0)<gamma2<F("5.13e-26")
    assert gamma2<F("2.27e-13")**2

    # Same selected physical source and fixed NF404 centering:
    # exact original Ecent=K+D7+D8; strict lower by source-accepted
    # outward K/D7 and actual 400-H/400-U original D8.
    Ecent_lower=K_GUARD+D7_GUARD+D8_GUARD
    Q_lower=Ecent_lower-R_GUARD
    assert Ecent_lower==F("1.252816e-21")
    assert Q_lower==F("1.57806e-22")
    assert Q_lower>F("1.256e-11")**2
    assert Q_lower>3076*gamma2  # Q²/gamma² original source >3076

    # Original E=span(q512,q513) orthogonal to selected original J242.
    # NF456 accepted d12 upper, so residual after adding just two
    # genuinely exterior rays remains decisively too big.
    d12_upper=F(nf456["original_two_witness_power_upper_approx"])
    assert F(0)<d12_upper<F("1.85e-26")
    T_lower=Q_lower-F("1.85e-26")
    assert T_lower==F("1.577875e-22")
    necessary_T=F(nf456["necessary_for_NF404_T_at_most_approx"])
    assert necessary_T<F("3.32e-26")
    assert T_lower>4750*necessary_T

    # The source-specific *distance to the feasible residual ball*
    # is > ||Qw|| -gamma. Here use rational root-free strict bounds.
    Q_norm_lo=F("1.256e-11")
    gamma_hi=F("2.27e-13")
    correction_needed=Q_norm_lo-gamma_hi
    assert correction_needed==F("1.2333e-11")
    assert gamma_hi**2>gamma2 and Q_norm_lo**2<Q_lower
    # Thus if same J242 and same gamma, any physical replacement
    # with ||w_new-w_old|| <= 1.2333e-11 is INFEASIBLE under this
    # particular norm criterion. For pure pole recentering or j in
    # J242, Q change ==0 regardless of j's magnitude.

    # Logical scope exact adversarial finite-dimensional controls:
    # measured selected witness failure compatible with both globally
    # positive and indefinite quadratic forms and another feasible
    # source. Never upgrade to global Weil/RH theorem.
    toychecks=finite_hilbert_controls()
    assert toychecks==8
    receipt={
      "pass":"NF496",
      "standing":"SOURCE-EXACT original fixed-source 242D pole-center-invariant orthogonal residual lower; NF403/NF404 original residual sufficient gate DEFINITELY FAILS for original selected source, no global RH/Weil decision",
      "original_nf407_immutable_source_SHA256":SRC,
      "original_nf406_immutable_seam_SHA256":SEAM,
      "original_nf404_selected_pole_center_source_custody_SHA256":f404,
      "original_nf456_two_ray_residual_source_custody_SHA256":f456,
      "original_nf478_full_J7_source_custody_SHA256":f478,
      "original_nf479_source_K_and_J7_custody_SHA256":f479,
      "original_nf495_complete_J8_signed_raw_independent_SHA256":f495,
      "original_nf495_independent_github_run":42866700605,
      "original_nf495_independent_github_source_artifact":13786768945,
      "original_source_K_strict_conservative_lower":str(K_GUARD),
      "original_source_D7_strict_conservative_lower":str(D7_GUARD),
      "original_source_COMPLETE_D8_actual_exact_raw_lower":str(D8lo),
      "original_source_COMPLETE_D8_actual_exact_raw_upper":str(D8hi),
      "original_source_D8_strict_conservative_lower":str(D8_GUARD),
      "original_true_centered_Efull_STRICT_lower":str(Ecent_lower),
      "original_true_selected_centered_242D_R_STRICT_upper":str(R_GUARD),
      "original_selected_centered_242D_R_raw_upper_exact":str(Rhi),
      "original_J242_perpendicular_squared_norm_STRICT_lower":str(Q_lower),
      "original_J242_perpendicular_squared_norm_definition":"||Q_J w||^2=||w-a*s||^2-||P_J(w-a*s)||^2, s in original selected J242",
      "original_NF403_NF404_exact_gamma_squared_budget":str(gamma2),
      "original_J242_residual_exceeds_gamma_squared_by_factor_strictly":3076,
      "original_two_ray_source_d12_STRICT_upper_weakening":"1.85e-26",
      "original_two_ray_removed_infinite_residual_T_STRICT_lower":str(T_lower),
      "original_two_ray_removed_residual_exceeds_NF456_necessary_budget_by_factor_strictly":4750,
      "original_J242_perpendicular_norm_STRICT_lower":str(Q_norm_lo),
      "original_gamma_norm_STRICT_upper":str(gamma_hi),
      "original_new_physical_supported_response_L2_displacement_REQUIRED_if_fixed_J_and_gamma_strict_greater":str(correction_needed),
      "original_pole_shear_or_ANY_selected_subspace_additive_correction_can_fix_frozen_complement":False,
      "original_change_of_basis_within_same_J242_can_fix_frozen_complement":False,
      "source_FAMILY_with_changed_original_NF404_threshold_or_changed_J242_ROLLOUT":"OPEN NOT EXCLUDED",
      "exact_finite_dimensional_global_sign_nonimplication_controls":toychecks,
      "original_NF404_selected_sufficient_complement_gate":"CERTIFIED FAIL",
      "original_complete_NF495_selected_Ew_bulk_and_D8":"SOURCE ACCEPTED, unchanged",
      "W_ODD_NEG":"OPEN","even_whole_Weil_operator_domain":"OPEN","RH":"OPEN",
      "next_bold":"NF497: perform source-family vs projector redesign quantitative feasibility assessment; any genuinely new candidate needs >=1.2333e-11 physical supported response change to reach SAME gamma/J242 residual, or change J242 and/or gamma. This is not an RH result."
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(receipt,indent=2)+"\n")
    print("NF496 SOURCE EXACT original J242-perpendicular square >=",str(Q_lower),flush=True)
    print("NF496 source residual >3076 times original NF403 gamma squared",flush=True)
    print("NF496 source two-ray-removed infinite T lower",str(T_lower),">4750 times allowed NF456 bound",flush=True)
    print("NF496 any original physical replacement for SAME J and gamma needs L2 response displacement >",
          str(correction_needed),flush=True)
    print("NF496 pure selected basis / pole recenter / selected-subspace correction NO-GO exact",flush=True)
    print("NF496 fixed original NF404 complement certificate FAIL; W-ODD-NEG and RH OPEN",flush=True)
if __name__=="__main__":main()
