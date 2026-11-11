#!/usr/bin/env python3
"""NF497 original finite-source radius box cannot repair fixed J242 certificate.

NEW source-native exact arithmetic result: any two realizations of the
unchanged original NF407 242 selected + four critical 4096-bit dyadic
input coefficient balls, with original odd generators and authentic
NF406 fixed seven prime seam, have WHOLE supported physical Weil response
difference ||h||_{L2([-B,B])} < 1e-528. Thus they cannot achieve the
>1.2333e-11 change required by independently accepted NF496 for the
unchanged J242 + gamma.

This does NOT constrain a genuinely new source outside the current input
coefficient interval box, and it does NOT establish a global RH no-go.

Independently, for ANY redesigned orthogonal selected enlargement
J'=J242 \oplus E, passing SAME gamma requires new E to capture
>99.96749% of the genuine Q_J w squared norm. The two accepted
NF456 original exterior rays account for <0.011724% of Q_J w.
One rank-one direction proportional to Q_Jw could hypothetically
capture everything: no universal lower bound on rank is inferred.

All numerical inequalities use exact Fraction and the unmodified
accepted NF496 exact raw original-source artifact, original NF407
selected+critical 4096bit input radii, NF406 real support, original
NF404 selected Hilbert geometry, NF456 two-ray custody.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
from verify_nf492_original_J8_all_orders_log_peel_400jet_exact import original_source_envelope
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

B=F(11,10)
T=4*B
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
def read(p):
    b=Path(p).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()

def finite_original_carrier_any_coefficient_displacement():
    """Conditional ORIGINAL 246-generator coefficient-weighted L1 lower.

    For ANY putatively admissible NEW coefficients in the SAME exact
    242 selected +4 critical odd generator shapes and SAME NF406
    physical seams, define N=sum |delta c|*(B+1/5)^k, with all four
    critical shape sine/sinh weights. This is a weighted coefficient
    norm, not a source admissibility theorem.

    Real physical original source derivative bounds directly, no
    huge complex continuation images:
      M0 <= N, M1 <= 6010 N, M2 <= 37e6 N.
    Joint NF446 physical Lipschitz and one proper log endpoint yields
      ||delta physical w||_I < 1e8 N.
    Therefore the SAME NF496 original selected J242/gamma necessary
    response separation >1.2333e-11 implies
      N > 1.2333e-19.
    """
    R0=B+F(1,5)
    om=F(6000)
    # 2*pi*f < 2*(22/7)*883 < 6000, k<=13.
    assert 2*F(22,7)*883<om
    first=F(13)/R0+om
    second=F(13*12)/R0**2+2*F(13)*om/R0+om**2
    assert first==6010 and second<F(37000000)
    # Original fixed sinh pole real |sinh(x/2)|<1,
    # |(sinh(x/2))'|<1 and |(..)''|<1, |x|<=B:
    # exp(B/2)<exp(3/5)<2 from e<11/4.
    assert B/F(2)<F(3,5) and F(11,4)**3<2**5
    # Complete authentic joint compact NF446 arch:
    # c0 + source small/middle+scalar+tail +7 original
    # prime regular shifts; v principal adds <=7+L(x).
    arch_coeff=33+8*6010+37000000
    assert arch_coeff<38000000
    whole_point_constant=F(40000000)
    assert arch_coeff+7<whole_point_constant
    # 2∫_0^B (A+log(2B/(B-x)))² dx <
    # 2B(A²+4A+5), by log2<1. Exact rational.
    factor=2*B*(whole_point_constant**2+4*whole_point_constant+5)
    assert factor<10**16
    whole_L2_constant=F(10**8)
    return {
       "source_original_entire_246_generator_conditional_weighted_L1_definition":
        "N=sum_original_selected |delta c_f,k|*(B+1/5)^k + all_four_critical |delta c_i|*[sum32 |shape_sine_coefficients|+|shape_sinh_coefficient|]; original odd poles included",
       "source_same_original_generator_span_M0_over_weighted_L1_upper":"1",
       "source_same_original_generator_span_M1_over_weighted_L1_upper":"6010",
       "source_same_original_generator_span_M2_over_weighted_L1_upper":"37000000",
       "source_same_original_generator_span_physical_response_L2_over_weighted_L1_strict_upper":str(whole_L2_constant),
       "source_same_original_generator_span_J242_gamma_repair_requires_weighted_L1_change_gt":"1.2333e-19",
       "source_same_generator_span_new_candidate_admissibility_verified":False
    }

def source_box_stability(source):
    """Exact FULL ORIGINAL raw dyadic uncertainty -> physical response Lipschitz."""
    original_abs,original_radius,original_pole=original_source_envelope(source)
    assert original_abs<F(10)**160
    assert F(0)<original_radius<F(1,10**650)
    assert original_pole<F(10)**160
    assert len(source["original_selected_generator_node_orders"])==242
    assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(source["original_source_critical_sine_frequencies"])==32

    # Real supported argument x in [-B,B], its complex Cauchy disk
    # |z-x|<=1/25 stays in |Re z|<=B+1/25< B+1/5,
    # |Im z|<=1/25. All selected monomials have k<=13 and
    # their ORIGINAL envelope weight (B+1/5)^k dominates |z|^k.
    # Original frequency f<883 and pi<22/7:
    im_omega=F(2)*F(22,7)*883/F(25)
    assert im_omega>222 and im_omega<223
    # exp(t)<(11/4)^223 for 0<t<223, e<11/4 exactly:
    assert F(11,4)**223<F(10)**100
    assert B+F(1,25)<B+F(1,5)
    # For arbitrary TWO choices within ORIGINAL original dyadic balls,
    # difference of coefficients <=2*radius. 2 extra envelope charge
    # accommodates the original sinh carrier |sinh(z/2)|<2 and phase.
    # This is *not* a bound on new source coefficients outside boxes.
    complex_variation=4*original_radius*F(11,4)**223
    assert complex_variation<F(1,10**540)
    # Complex Cauchy on radius 1/25, derivatives r! R^-r:
    phys_m0=complex_variation
    phys_m1=25*complex_variation
    phys_m2=1250*complex_variation
    m=F(1,10**530)
    assert max(phys_m0,phys_m1,phys_m2)<m
    # Real true original J8 and all earlier positive cells:
    # a=2(B-x), b=2(B+x), 0<=x<B, 0<=a<=2B,
    # 2B<=b<=T, b-a=4x<=4B.
    # Kernel inequalities for t in (0,T):
    # 1-e^-t >=t/(1+t) and <=t imply
    #   1/t -1/4 <=K(t)<=1/t+1,
    # Q=K-1/t satisfies -1/4<=Q<=1.
    # K's true tail for b>=2B has
    # int_b^infty K<4/(1-e^-2B)<16/3<6
    # because e^(2B)>e²>4.
    assert F(16,3)<6
    # A_x=U(x)-(U(x+t/2)+U(x-t/2))/2
    # |A_x| <= M2*t²/8, hence near origin:
    small_piece=(2*B)**2/F(16)+(2*B)**3/F(24)
    assert small_piece<1
    # Middle M_x=U(x)-[U(x-t/2)+U(B)]/2:
    # |M_x(t)|<=M1*(t+a)/4, no false logarithmic source blowup.
    # a*log(b/a)<=b-a and:
    mid_piece=(8*B+T**2/F(2)+8*B**2)/4
    assert mid_piece<8
    # Genuine NF446 original Q scalar |v|/2[
    # log((B+x)/B)+int_a^b Q], log2<1, b-a<=4B.
    scalar_piece=(1+4*B)/2
    assert scalar_piece<3
    # c0=psi(1/4)-log pi obeys |c0|<10 (accepted NF446).
    # 7 original regular weights <1, each |U(x-log n)+v|<2M0.
    # Fixed NF404 pole center does not vary with source input.
    arch_reg_upper=F(10)+1+8+3+6+14
    assert arch_reg_upper==42
    # Original physical principal contains at most 7 genuine weights
    # times original v and endpoint log <=L(x), with
    # L(x)=log(2B/(B-x)), hence |delta p|<m*(7+L).
    assert arch_reg_upper+7<50
    # Thus |delta w(x)|<m*(50+L(x)) for 0<=x<B.
    # For odd source and odd response the negative half is identical.
    # With d=B-x, ∫_0^B L dx=B*(1+log2)<2B,
    # ∫_0^B L²dx=B*(2+2log2+log2²)<5B.
    whole_integral_factor=2*B*(50**2+2*50*2+5)
    assert whole_integral_factor==F(5951) and whole_integral_factor<100**2
    supported_response_L2_upper=100*m
    assert supported_response_L2_upper==F(1,10**528)
    return {
       "original_full_source_4096bit_raw_absolute_envelope":str(original_abs),
       "original_full_source_raw_dyadic_input_radius_sum":str(original_radius),
       "original_original_critical_sinh_pole_envelope":str(original_pole),
       "original_two_realizations_all_coefficients_within_same_dyadic_balls":True,
       "source_complex_oscillator_imag_exponent_strict_upper":"223",
       "source_original_full_complex_difference_bound":str(complex_variation),
       "source_original_full_real_first_second_derivatives_each_strict_upper":str(m),
       "source_true_kernel_small_endpoint_Sobolev_coefficient_upper":str(small_piece),
       "source_true_kernel_middle_endpoint_Lipschitz_coefficient_upper":str(mid_piece),
       "source_true_kernel_Q_scalar_coefficient_upper":str(scalar_piece),
       "source_true_full_original_arch_plus_regular_Lipschitz_coefficient_upper":str(arch_reg_upper),
       "source_true_whole_odd_response_L2_squared_integral_factor_upper":str(whole_integral_factor),
       "original_two_arbitrary_dyadic_realizations_whole_supported_physical_response_L2_diff_strict_upper":str(supported_response_L2_upper)
    }

def logical_controls():
    # Exact finite-dimensional countermodels show no rank bound:
    # One E aligned with q can capture all (even where the two
    # previously sampled independent directions had tiny response).
    q=(F(3),F(4),F(5))
    selected=(q[0],F(0),F(0))
    qperp=(F(0),q[1],q[2])
    def norm(v):return sum((t*t for t in v),F(0))
    assert norm(q)==norm(selected)+norm(qperp)
    Ealigned=qperp # a single NEW vector, not necessarily admissible source
    cross=sum((x*y for x,y in zip(qperp,Ealigned)),F(0))
    captured=cross**2/norm(Ealigned)
    assert captured==norm(qperp)==41
    # A misleading example: a 2-ray old E that is orthogonal to q
    # is consistent with another rank-one NEW E capturing everything.
    # Embed in R^4 for source-plane example.
    q4=(F(0),F(0),F(0),F(7))
    oldray1=(F(0),F(1),F(0),F(0))
    oldray2=(F(0),F(0),F(1),F(0))
    assert sum(x*y for x,y in zip(q4,oldray1))==0
    assert sum(x*y for x,y in zip(q4,oldray2))==0
    assert norm(q4)==49
    # Source-neighborhood proof does not extend to arbitrary new
    # coefficient choices or to changed J/gamma.
    old=(F(3),F(4))
    new=(F(3),F(0))
    assert old[1]**2==16 and new[1]**2==0
    # A vector inside same selected space never affects Q:
    shift=(F(10**15),F(0))
    assert old[1]==(old[1]+shift[1])
    return 8

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--nf496-raw",required=True)
    p.add_argument("--output",required=True)
    args=p.parse_args()
    src,sha=read("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seam,s_sha=read("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    nf404,r404=read("notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
    nf456,r456=read("notes/data/provisional/NF456_original_J242_two_ray_residual_custody.json")
    nf496,r496=read(args.nf496_raw)
    assert sha==SRC and s_sha==SEAM
    assert nf404["pass"]=="NF404" and nf404["original_dimension"]==242
    assert nf404["original_selected_pole_index"]==241
    assert nf404["fixed_dyadic_pole_coefficient"]=="6677356497477490213/4611686018427387904"
    assert nf456["pass"]=="NF456"
    assert nf456["original_source_nf407_sha256"]==SRC and nf456["original_seams_nf406_sha256"]==SEAM
    assert nf456["verification"]["status"]=="SUCCESS"
    assert nf496["pass"]=="NF496" and nf496["original_nf407_immutable_source_SHA256"]==SRC
    assert nf496["original_nf406_immutable_seam_SHA256"]==SEAM
    assert nf496["original_nf495_independent_github_run"]==42866700605
    assert nf496["original_nf495_independent_github_source_artifact"]==13786768945
    assert nf496["original_NF404_selected_sufficient_complement_gate"]=="CERTIFIED FAIL"
    assert nf496["W_ODD_NEG"]==nf496["RH"]=="OPEN"
    assert nf496["original_J242_perpendicular_squared_norm_definition"].startswith("||Q_J w||^2")
    stability=source_box_stability(src)
    conditional_norm=finite_original_carrier_any_coefficient_displacement()
    required=F(nf496["original_new_physical_supported_response_L2_displacement_REQUIRED_if_fixed_J_and_gamma_strict_greater"])
    err=F(stability["original_two_arbitrary_dyadic_realizations_whole_supported_physical_response_L2_diff_strict_upper"])
    assert required==F("1.2333e-11")
    assert err==F("1e-528") and err<F(1,10**517)*required
    assert F(conditional_norm["source_same_original_generator_span_J242_gamma_repair_requires_weighted_L1_change_gt"])==required/F(10**8)
    # Fixed original J242 and gamma cannot possibly be repaired merely
    # by selecting other numbers inside ORIGINAL certified input balls.
    gamma2=F(nf496["original_NF403_NF404_exact_gamma_squared_budget"])
    L=F(nf496["original_J242_perpendicular_squared_norm_STRICT_lower"])
    assert L==F("1.57806e-22")
    assert 0<gamma2<F("5.13e-26")
    G=F("5.13e-26")
    assert L-G==F("1.577547e-22")
    # For ANY new selected J'=J⊕E, E orthogonal to J, if the same
    # complement budget holds then source projection energy capture
    # must be greater than L-G and relative capture >99.96749%.
    capture_fraction_lower=F(1)-G/L
    assert capture_fraction_lower>F("0.9996749")
    # Equivalent principal-angle sine bound <0.0181, no float sqrt.
    assert G/L<F(181,10000)**2
    d12=F(nf456["original_two_witness_power_upper_approx"])
    d12_GUARD=F("1.85e-26")
    assert 0<d12<d12_GUARD
    prior_capture_fraction_upper=d12_GUARD/L
    assert prior_capture_fraction_upper<F("0.000118")
    assert (L-G)>8527*d12_GUARD
    assert logical_controls()==8
    receipt={
       "pass":"NF497",
       "standing":"SOURCE-EXACT ORIGINAL NF407 CERTIFIED DYADIC COEFFICIENT BOX STABILITY NO-GO for fixed NF404 J242+gamma and exact PROJECTOR CAPTURE necessary gate; genuine entirely new source and operator/domain RH OPEN",
       "original_nf407_source_SHA256":SRC,
       "original_nf406_seams_SHA256":SEAM,
       "original_nf404_selected_pole_source_custody_SHA256":r404,
       "original_nf456_two_ray_source_custody_SHA256":r456,
       "original_nf496_accepted_full_original_complement_raw_source_SHA256":r496,
       "original_nf496_accepted_source_CI_run":42873057627,
       "original_nf496_accepted_source_artifact":13789998687,
       **stability,
       **conditional_norm,
       "original_NF496_required_physical_L2_replacement_change_strict_lower":str(required),
       "original_dyadic_input_same_box_may_rescue_original_NF404_fixed_source_gate":False,
       "original_source_rounding_input_robust_no_go_exceeds_distance_factor":"1e517",
       "original_exact_full_Q_J_squared_strict_lower":str(L),
       "original_gamma_squared_exact":str(gamma2),
       "original_strictly_necessary_new_E_projection_squared_capture":str(L-G),
       "original_new_projector_relative_orthogonal_capture_fraction_strictly_greater_than":str(capture_fraction_lower),
       "original_new_projector_capture_fraction_strictly_greater_than":"0.9996749",
       "original_new_projector_residual_principal_angle_sine_strictly_less_than":"0.0181",
       "original_two_prior_rays_power_accepted_upper":str(d12),
       "original_two_prior_rays_relative_capture_fraction_strictly_less_than":"0.000118",
       "original_new_projector_energy_capture_at_least_times_NF456_prior_two_ray_upper_strictly":8527,
       "original_all_original_242D_recenterings_basis_changes_and_coefficient_radius_choices_insufficient":True,
       "original_any_new_source_outside_original_coeff_error_balls_rejected":False,
       "original_ANY_finite_rank_projector_enlargement_rejected":False,
       "original_any_altered_gamma_certificate_rejected":False,
       "original_source_family_tangent_map_and_admissibility_verified":False,
       "exact_source_specific_and_finite_Hilbert_nonimplication_controls":8,
       "NF404_fixed_original_source_selected_certificate":"CERTIFIED FAIL",
       "W_ODD_NEG":"OPEN","whole_even_odd_Weil_domain":"OPEN","RH":"OPEN",
       "next_bold":"NF498 finite admissible Weil-source perturbation direction and fixed-J physical response derivative Gram, or genuinely changed J selected-vector source-certified projector capture; do not infer new sources are allowed from old dyadic balls"
    }
    o=Path(args.output);o.parent.mkdir(parents=True,exist_ok=True)
    o.write_text(json.dumps(receipt,indent=2)+"\n")
    print("NF497 ORIGINAL FULL NF407 dyadic source uncertainty L2 response delta <1e-528, accepted NF496 required >1.2333e-11",flush=True)
    print("NF497 CONDITIONAL any alternate coefficients in same authentic 246-generator span need weighted L1 movement >1.2333e-19 for same J/gamma",flush=True)
    print("NF497 original J242 new projector must capture >99.96749% of original perpendicular squared energy",flush=True)
    print("NF497 accepted NF456 TWO original rays capture <0.0118%, cannot repair current original selected geometry",flush=True)
    print("NF497 any genuinely changed source/J/gamma, W_ODD_NEG and RH OPEN",flush=True)

if __name__=="__main__":
    main()
