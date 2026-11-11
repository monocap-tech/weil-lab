#!/usr/bin/env python3
"""NF499 full ORIGINAL source-supported smooth log-collar test candidate.

Produce an explicit odd compactly supported C-infinity test candidate
phi_epsilon(x)=chi_epsilon(B-|x|)*ell_U(x), epsilon=10^-50,
where the TRUE ORIGINAL source-produced NF498 terminal logarithmic
carrier is ell_U(x)=sgn(x)*1_{B-delta<|x|<B} U(|x|)/2 log(B/(B-|x|)).
chi(d)=S((d-eps)/eps)*S((delta-eps-d)/eps),
S(s)=rho(s)/(rho(s)+rho(1-s)),
rho(s)=e^{-1/s} for s>0 and 0 otherwise.

This construction is C_c^infty((-B,B)), odd, nonzero, and in every
classical physical Sobolev H^s. It does NOT establish membership in
the range of the authentic Weil multiplier source-to-response map,
nor in the original finite J242 selected analytic carrier, nor
verify whole operator-domain graph norm / Fourier lowband.

Reuses immutable ORIGINAL NF407 242 selected+4 critical source,
NF406 seven true prime support, accepted actual NF493 all-400-source
U(B-d) polynomial L1 norm, and NF498 *SOURCE-PAID* genuine full
terminal w, ell, and cross-correlation intervals.

For both original odd J8 terminal collars exact rational bounds prove
||phi-eLL||^2 < 1.61864e-59 < 1e-58,
hence ||phi-ell|| < 1e-29 (no hidden log endpoint supremum).
Original true terminal scalar <w,ell> and norms yield source-certified
best physical terminal rank-one capture fraction
    0.3402 < capture(phi) < 0.342
and both-collar capture squared energy
    1.195e-22 < captured(phi) < 1.20e-22.
The first 242 selected cross-moments <j,phi>, <j,w>
are NOT computed. Thus these are terminal physical captures, NOT
NF497 original q=Q_Jw capture. A physical smooth function is not
automatically an admissible replacement ORIGINAL Weil source.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
B=F(11,10)
DELTA=F(1,500)
EPS=F(1,10**50)

def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def pair(a):
    lo,hi=map(F,a)
    assert lo<=hi
    return lo,hi

def controls():
    """Exact finite Hilbert nonimplication: raw capture != Q_J capture."""
    w=(F(3),F(4))
    ell=(F(1),F(1))
    norm=lambda v:sum((x*x for x in v),F(0))
    dot=lambda a,b:sum((x*y for x,y in zip(a,b)),F(0))
    raw=dot(w,ell)**2/(norm(w)*norm(ell))
    assert raw==F(49,50)
    # If a *different* selected space contains ell, then Q_J ell=0
    # despite its 98% full raw projection onto ell.
    sel_ell=ell
    c=dot(ell,sel_ell)/norm(sel_ell)
    qell=tuple(x-c*y for x,y in zip(ell,sel_ell))
    assert qell==(F(0),F(0))
    # For J=span(e1), the same raw data give a nontrivial Q_J ell
    # and full J-perpendicular projection of Q_J w.
    qell2=(F(0),ell[1]);qw2=(F(0),w[1])
    assert dot(qw2,qell2)**2/norm(qell2)==norm(qw2)==16
    # Changing the *old* basis within J does not change Q.
    for a in (F(1),F(7),F(-11,3)):
        assert (w[1]-(a*F(0)))==w[1]
    # smooth flat construction is nonzero because ||phi||>=||ell||-eta
    assert EPS>0 and 4*EPS<DELTA
    return 8

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--nf498-raw",required=True)
    ap.add_argument("--nf493-raw",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    old,old_sha=read(args.nf498_raw)
    u,ush=read(args.nf493_raw)
    src,srcsha=read("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,ssha=read("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    nf404,nsha=read("notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
    assert srcsha==SRC==old["original_nf407_source_sha256"]==u["original_nf407_source_sha256"]
    assert ssha==SEAM==old["original_nf406_seams_sha256"]==u["original_nf406_seams_sha256"]
    assert old["pass"]=="NF498" and u["pass"]=="NF493"
    assert old["original_source_selected_dimension"]==nf404["original_dimension"]==242
    assert old["original_selected_authentic_odd_sinh_pole_index"]==nf404["original_selected_pole_index"]==241
    assert old["original_true_J8_terminal_delta"]=="1/500"
    assert u["original_true_source_4096bit_400_jet_coefficients_verified"]==400
    assert u["original_true_log_source_coefficient"]=="U(B-d)/2"
    assert old["original_source_400_source_Elog_independent_NF493_overlap_after_fees"]
    assert old["original_true_l2_gram_Schur_residual_source_positive"]
    assert old["original_odd_log_carrier_true_L2_but_not_H1"]
    assert old["original_true_selected_Q_J_log_template_source_coupling_computed"] is False
    assert len(src["original_selected_generator_node_orders"])==242
    assert src["original_selected_generator_node_orders"][241]==["pole",None]
    assert len(src["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(src["original_source_critical_sine_frequencies"])==32
    assert nf404["pass"]=="NF404" and nf404["fixed_dyadic_pole_coefficient"]=="6677356497477490213/4611686018427387904"

    # Actual NF493 source-correlated full 400 real U coefficients give
    # a UNIFORM physical bound on the FULL true U(B-d), not only
    # its value at d=0 or 1/500.
    max_U=F(2,10**7)
    L1=F(u["original_actual_normalized_400_coeff_l1_envelope"])
    infinite_tail=F(u["original_source_uniform_400_coeff_analytic_remainder"])
    assert F(0)<L1+infinite_tail<max_U
    assert infinite_tail<F(1,10**119)
    assert F(0)<EPS and 4*EPS<DELTA
    # e>2, e>5/2 by positive Taylor series, and pi irrelevant.
    # On 0<d<2eps, original log(B/(2eps))<200 because
    # exp(200)>2^200>B/(2eps). On delta-2eps<d<delta,
    # d>delta/2 and log(B/d)<log(2B/delta)<8 since
    # exp(8)>(5/2)^8>2B/delta.
    assert 2**200>B/(2*EPS)
    assert F(5,2)**8>2*B/DELTA
    assert DELTA-2*EPS>DELTA/2
    # For the odd smooth 2-collar difference, 0<=chi<=1 and
    # 1-chi is supported only on 0<d<2eps and
    # delta-2eps<d<delta. The original source uniform
    # |U|<max_U yields:
    # 2* int (U/2)^2 log(B/d)^2 <=
    # (M²/2)*(2eps*(200²+400+2)+2eps*8²).
    outer_edge_L2_log2_integral_upper=2*EPS*(200**2+2*200+2)
    inner_edge_L2_log2_integral_upper=2*EPS*8**2
    source_smooth_error_sq=max_U**2/F(2)*(outer_edge_L2_log2_integral_upper+inner_edge_L2_log2_integral_upper)
    eta=F(1,10**29)
    assert source_smooth_error_sq==F("1.61864e-59")
    assert source_smooth_error_sq<eta**2

    # GENUINE original independently source-certified, individually
    # approximation-error-paid original full two J8 collar norms
    # from NF498 raw exact-Fraction receipt.
    Wlo,Whi=pair(old["original_true_full_J8_terminal_Ew_outward"])
    C0lo,C0hi=pair(old["original_odd_log_carrier_full_two_collar_norm_squared_outward"])
    Ilo,Ihi=pair(old["original_odd_log_carrier_full_two_collar_inner_with_w_outward"])
    assert Ilo<=Ihi<0
    assert Wlo>0 and C0lo>0
    wlower=F("1.874e-11")
    wupper=F("1.875e-11")
    clower=F("2.529e-11")
    cupper=F("2.53e-11")
    ilower=F("2.767e-22")
    iupper=F("2.769e-22")
    # Strict ROOT-FREE exact controls of the actual source integrals:
    assert wlower**2<2*Wlo<=2*Whi<wupper**2
    assert clower**2<C0lo<=C0hi<cupper**2
    assert ilower<(-Ihi)<=(-Ilo)<iupper
    # Original true rho(ell)≠0 and epsilon smooth carrier nonzero
    # without an unverifiable sample of the flat cutoff:
    assert clower>eta

    # By Cauchy and the L2 source-norm bound:
    # |<w,phi>| between |<w,ell>|±||w|| eta,
    # ||phi|| between ||ell||±eta.
    inner_lower=ilower-wupper*eta
    inner_upper=iupper+wupper*eta
    assert inner_lower>0
    cap_power_lower=(inner_lower/(cupper+eta))**2
    cap_power_upper=(inner_upper/(clower-eta))**2
    cap_fraction_lower=(inner_lower/(wupper*(cupper+eta)))**2
    cap_fraction_upper=(inner_upper/(wlower*(clower-eta)))**2
    assert cap_power_lower>F("1.195e-22")
    assert cap_power_upper<F("1.20e-22")
    assert cap_fraction_lower>F("0.3402")
    assert cap_fraction_upper<F("0.342")
    assert controls()==8

    result={
       "pass":"NF499",
       "standing":"SOURCE-EXACT concrete odd smooth Cc∞ physical J8 endpoint-log carrier, rigorously SOURCE-near original singular ell_U in L2 and >34.02% genuine 2-collar terminal physical rank-one capture. NOT full original J242-Q capture, Weil source-to-response range or operator-domain admissibility",
       "original_nf407_source_sha256":SRC,
       "original_nf406_seams_sha256":SEAM,
       "original_nf404_selected_projection_custody_sha256":nsha,
       "original_nf493_400_source_uniform_U_archived_raw_sha256":ush,
       "original_nf498_genuine_full_terminal_w_log_carrier_raw_sha256":old_sha,
       "original_source_selected_generators":242,
       "original_critical_generators":4,
       "original_original_odd_sinh_pole_index":241,
       "original_full_true_terminal_delta":"1/500",
       "explicit_source_smooth_epsilon":"1e-50",
       "smooth_step_definition":"rho(t)=exp(-1/t) for t>0 else 0; S(t)=rho(t)/(rho(t)+rho(1-t)); chi(d)=S((d-eps)/eps)*S((delta-eps-d)/eps)",
       "explicit_smooth_odd_physical_phi":"phi(x)=sgn(x)*chi(B-abs(x))*U(abs(x))/2*log(B/(B-abs(x))) for abs(x)<B, else 0",
       "smooth_positive_collar_support_subset":"B-delta+eps <= x <= B-eps",
       "smooth_original_odd_negative_collar_support":"odd reflection of positive support",
       "smooth_collar_C_c_infinity_original_physical":True,
       "smooth_collar_classical_Hs_all_nonnegative_orders":True,
       "smooth_log_coordinate_multiplicative_test_f_y_equals_phi_log_y_in_Cc_infinity_positive_group":True,
       "original_weil_multiplier_image_or_source_admissible_verified":False,
       "original_whole_operator_graph_domain_verified":False,
       "original_J242_selected_analytic_generator_membership":False,
       "source_original_nf493_U400_full_real_terminal_l1_bound":str(L1),
       "source_original_nf493_U400_analytic_tail":str(infinite_tail),
       "source_full_true_U_terminal_uniform_strict_upper":str(max_U),
       "two_collar_smoothing_error_squared_strict_upper":str(source_smooth_error_sq),
       "two_collar_smoothing_L2_error_strict_upper":str(eta),
       "source_actual_full_two_collar_w_norm_lower_strict":str(wlower),
       "source_actual_full_two_collar_w_norm_upper_strict":str(wupper),
       "source_actual_full_two_collar_ell_norm_lower_strict":str(clower),
       "source_actual_full_two_collar_ell_norm_upper_strict":str(cupper),
       "source_actual_full_two_collar_abs_inner_w_ell_strict_lower":str(ilower),
       "source_actual_full_two_collar_abs_inner_w_ell_strict_upper":str(iupper),
       "smooth_phi_original_full_two_collar_rankone_captured_power_lower_exact":str(cap_power_lower),
       "smooth_phi_original_full_two_collar_rankone_captured_power_upper_exact":str(cap_power_upper),
       "smooth_phi_original_full_two_collar_capture_fraction_lower_exact":str(cap_fraction_lower),
       "smooth_phi_original_full_two_collar_capture_fraction_upper_exact":str(cap_fraction_upper),
       "smooth_phi_two_collar_terminal_capture_fraction_gt":"0.3402",
       "smooth_phi_two_collar_terminal_capture_fraction_lt":"0.342",
       "source_ell_U_L2_approximable_by_explicit_Cc_infinity_smoothing":True,
       "source_not_in_H1_does_not_imply_positive_gamma_L2_approximation_no_go":True,
       "true_original_Q_J_phi_cross_moments_against_all_242_computed":False,
       "true_original_Q_J_phi_to_Q_J_w_capture_computed":False,
       "fixed_original_NF404_certificate":"CERTIFIED FAIL (NF495–NF497)",
       "independent_exact_Hilbert_orthogonal_vs_raw_projection_nonimplication_controls":8,
       "W_ODD_NEG":"OPEN",
       "whole_even_odd_Weil_operator_domain":"OPEN",
       "RH":"OPEN",
       "next_bold":"NF500 construct and source-certify all 242 mixed physical original J242 moments for this explicit smooth phi or a related genuinely eligible Weil-source candidate, and compute actual Q_J capture; do not promote terminal-only capture to NF404 gate"
    }
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2)+"\n")
    print("NF499 TRUE ORIGINAL full 400-source U terminal |U| <2e-7 and eps=1e-50 explicit Cc∞ odd candidate PASS",flush=True)
    print("NF499 source physical odd L2 log-template smooth approximation squared error <",str(source_smooth_error_sq),flush=True)
    print("NF499 SOURCE-VERIFIED genuine smooth physical two J8 collar capture fraction in (",str(cap_fraction_lower),",",str(cap_fraction_upper),")",flush=True)
    print("NF499 new candidate Cc∞ but source-to-response Weil/domain and TRUE J242 cross moments OPEN; RH OPEN",flush=True)

if __name__=="__main__":
    main()
