#!/usr/bin/env python3
"""MG42: exact relative PSD source uncertainty budget for original nonscalar B.

Start with independently accepted MG41: for every one of 24 original
nonscalar MG40 responses B, M_ideal=Hlo-Ucore is strictly PD by
exact 24-pivot rational LDL, while M_actual=M_ideal-F has a strictly
negative rational Rayleigh witness (F is the chosen valid PSD
mixed-G moment uncertainty fee).

For each of the four original k12/k16 x 16/32-mesh BEST nonscalar B,
compute an exact dyadic certificate for the continuum of scaled fees:
   M(s) = M_ideal - s F,   s >= 0.
F >=0 and M_ideal>0. Thus M(s) decreases in Loewner order as s grows.
At s_low prove M(s_low)>0 by exact rational LDL (ALL pivots positive).
At s_high prove M(s_high) has a true negative rational Rayleigh ray.
Then ANY s<=s_low preserves strict positivity of this 24D SOURCE
certificate matrix (hypothetical reduced F), while ANY s>=s_high is
infeasible with this fixed optimistic core + proportional F.
The true threshold s* is between the two certified dyadics. This
is NOT an estimator of actual signed Weil spectrum.

Bisection uses numerical eigenvectors ONLY to propose a rational ray,
never for acceptance. With no exact witness at a step, fail closed as
INCONCLUSIVE and preserve the last exact valid bracket.

The analyzed scaling F -> s F is a COUNTERFACTUAL CERTIFICATE BUDGET:
it is not a valid replacement for the original bound unless new source
moments rigorously prove that reduced uncertainty fee. The real
accepted bound is s=1 and remains nonpositive for these four B.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    deserialize,original_H24_from_physical_source)
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,T,mm,plus,sub,mul,gersh_lower,psd,norm_upper)
from validate_rpb108_mg41_ideal_cross_error_feasibility import (
    classify_ideal,exact_spd_ldl,dot,synthetic_regression)
from validate_rpb108_mg40_anisotropic_source_cross_error import (
    core_and_error,source_B_is_nonscalar)
N=24
MESHES=(16,32)
CUTS=(12,16)
MAX_ROUNDS=5
def encode(A):return [[str(y) for y in row] for row in A]
def recovered_data(mg24,mg29,mg40,mg41):
    assert all(x["canonical_W_ODD_NEG"]=="OPEN"
               for x in (mg24,mg29,mg40,mg41))
    assert mg41["status"]=="ORIGINAL_MG41_NONSCALE_IDEAL_G_CROSS_FEE_FEASIBILITY"
    assert mg40["status"]=="ORIGINAL_MG40_ANISOTROPIC_FULL_SOURCE_G_CROSS_ERROR_GATE"
    assert mg41["total_tested_nonscalar_B"]==24
    assert [mg41["verified_MG24_run"],mg41["verified_MG29_run"],
            mg41["verified_MG40_run"]]==[39378465438,39440914565,39513403010]
    assert not mg41["source_24D_strict_residual_contraction_certified"]
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==Q(mg24["physical_Gram_Loewner_row_error"])
    Hlo=sub(Hmid,mul(Herr,Id(N)))
    Hup=plus(Hmid,mul(Herr,Id(N)))
    jobs=[]
    for mesh in MESHES:
        for k in CUTS:
            s40=next(s for s in mg40["scenarios"]
                     if s["mesh_cells"]==mesh and s["cutoff_k"]==k)
            s41=next(s for s in mg41["scenarios"]
                     if s["mesh_cells"]==mesh and s["cutoff_k"]==k)
            assert s41["classification_counts"]=={
                "NEGATIVE_EXACT_RATIONAL_RAYLEIGH":0,
                "POSITIVE_EXACT_RATIONAL_LDL":6,"INCONCLUSIVE":0}
            assert s41["actual_MG40_certificate_inertia_counts"]=={
                "NEGATIVE_EXACT_RATIONAL_RAYLEIGH":6,
                "POSITIVE_EXACT_RATIONAL_LDL":0,"INCONCLUSIVE":0}
            best=s40["best_nonscalar_name"]
            trial40=next(x for x in s40["all_rational_candidate_results"]
                         if x["name"]==best)
            trial41=next(x for x in s41["trials"] if x["name"]==best)
            m=next(x for x in mg29["meshes"] if x["mesh_cells"]==mesh)
            src=next(x for x in m["full_original_frequency_scenarios"]
                     if x["cutoff_k"]==k)
            LG=deserialize(src["full_original_Gstar_lower"])
            UG=deserialize(src["full_original_Gstar_upper"])
            US=deserialize(src["full_original_Sstar_upper"])
            E=mul(Q(1,2),sub(UG,LG))
            assert psd(E) and psd(US)
            B=deserialize(trial40["B_original_exact_rational"])
            t=Q(trial40["source_anchor_t"])
            assert source_B_is_nonscalar(B)
            core,E2,D=core_and_error(Hup,LG,UG,US,t,B)
            assert E==E2
            ideal=sub(Hlo,core)
            if trial40["selected_method"]=="matrix_Young":
                eta=Q(trial40["selected_eta"])
                F=plus(mul(eta,E),
                       mul(1/eta,mm(mm(T(D),E),D)))
            else:
                assert trial40["selected_method"]=="MG30_isotropic"
                F=mul(Q(trial40["old_isotropic_fee"]),Id(N))
            assert psd(F) and F==T(F)
            actual=sub(ideal,F)
            assert gersh_lower(actual)==Q(trial40["selected_original_signed_Gersh"])
            assert trial41["ideal_zero_G_cross_fee_status"]=="POSITIVE_EXACT_RATIONAL_LDL"
            assert trial41["actual_MG40_source_certificate_inertia_gate"]=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH"
            assert trial41["actual_MG40_source_certificate_exact_witness"][
                "nonzero_rational_24D_source_direction"]
            ray=[Q(x) for x in trial41["actual_MG40_source_certificate_exact_witness"][
                "rational_vector"]]
            assert dot(ray,actual)==Q(trial41[
                "actual_MG40_source_certificate_exact_witness"][
                "exact_negative_quadratic"])<0
            pivots=exact_spd_ldl(ideal)
            assert pivots is not None and len(pivots)==N
            assert [str(x) for x in pivots]==trial41["exact_rational_ideal_witness"][
                "exact_positive_schur_pivots"]
            jobs.append((mesh,k,best,trial40,ideal,F,ray,pivots))
    assert len(jobs)==4
    return jobs

def certify_candidate(s,ideal,fee):
    A=sub(ideal,mul(s,fee))
    piv=exact_spd_ldl(A)
    if piv is not None and len(piv)==N:
        return "EXACT_POSITIVE_LDL",{
            "scalar":str(s),"positive_exact_rational_pivots":[str(p) for p in piv],
            "certified_strict_full24_source_positive":True}
    kind,w=classify_ideal(A)
    if kind=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
        ray=[Q(x) for x in w["rational_vector"]]
        assert len(ray)==N and any(ray)
        assert dot(ray,A)==Q(w["exact_negative_quadratic"])<0
        return "EXACT_NEGATIVE_RAYLEIGH",{
            "scalar":str(s),"rational_source_direction":w["rational_vector"],
            "exact_negative_quadratic":w["exact_negative_quadratic"],
            "source_matrix_fails_positive_definiteness":True}
    return "INCONCLUSIVE",{"scalar":str(s)}

def run_case(mesh,k,name,trial,ideal,fee,ray,pivots):
    low=Q(0);high=Q(1)
    lo_cert={"scalar":"0","positive_exact_rational_pivots":[str(x) for x in pivots],
             "certified_strict_full24_source_positive":True}
    actual=sub(ideal,fee)
    hi_cert={"scalar":"1","rational_source_direction":[str(x) for x in ray],
             "exact_negative_quadratic":str(dot(ray,actual)),
             "source_matrix_fails_positive_definiteness":True}
    assert Q(hi_cert["exact_negative_quadratic"])<0
    checks=[]
    for i in range(MAX_ROUNDS):
        middle=(low+high)/2
        kind,w=certify_candidate(middle,ideal,fee)
        checks.append({"round":i+1,"tested_scale":str(middle),
                       "classification":kind,"certificate":w})
        if kind=="EXACT_POSITIVE_LDL":
            low=middle;lo_cert=w
        elif kind=="EXACT_NEGATIVE_RAYLEIGH":
            high=middle;hi_cert=w
        else:
            break
    assert 0<=low<high<=1
    assert (high-low)<=Q(1) and all(
        x["classification"] in ("EXACT_POSITIVE_LDL","EXACT_NEGATIVE_RAYLEIGH",
                                "INCONCLUSIVE") for x in checks)
    assert len(checks)<=MAX_ROUNDS
    return {
       "mesh_cells":mesh,"cutoff_k":k,"original_nonscalar_B":name,
       "selected_MG40_mixed_G_fee_type":trial["selected_method"],
       "exact_ratio_fee_scale_positive_below_or_equal":str(low),
       "exact_ratio_fee_scale_negative_above_or_equal":str(high),
       "certified_fee_scale_threshold_width":str(high-low),
       "sufficient_relative_fee_reduction_at_least":str(1-low),
       "necessary_relative_fee_reduction_more_than":str(1-high),
       "lower_exact_positive_LDL_certificate":lo_cert,
       "upper_exact_negative_Rayleigh_certificate":hi_cert,
       "exact_dyadic_bisection_checks":checks,
       "bisection_rounds_resolved":sum(x["classification"]!="INCONCLUSIVE"
                                    for x in checks),
       "complete_24D_ideal_source_matrix":encode(ideal),
       "complete_24D_PSD_mixed_G_fee_matrix":encode(fee),
       "actual_current_fee_scale_one_has_negative_direction":True,
       "hypothetically_reduced_fee_not_currently_rigorous_for_original_G":True,
       "full_470D_inverse_and_RH_not_proved":True}

def self_test():
    assert synthetic_regression()
    m=[[Q(i==j) for j in range(N)] for i in range(N)]
    F=[[Q((i==j)*(i+1)) for j in range(N)] for i in range(N)]
    assert psd(F)
    assert certify_candidate(Q(1,32),m,F)[0]=="EXACT_POSITIVE_LDL"
    assert certify_candidate(Q(1,16),m,F)[0]=="EXACT_NEGATIVE_RAYLEIGH"
    assert certify_candidate(Q(0),m,F)[0]=="EXACT_POSITIVE_LDL"
    assert certify_candidate(Q(1),m,F)[0]=="EXACT_NEGATIVE_RAYLEIGH"
    return True

def main():
    p=argparse.ArgumentParser()
    for name in ("mg24","mg29","mg40","mg41"):
        p.add_argument("--verified-"+name+"-json")
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--output",default=
        "artifacts/mg42_original_relative_uncertainty_budget.json")
    args=p.parse_args()
    assert self_test()
    if args.self_test:
        print("MG42 relative PSD fee budget exact LDL/ray synthetic regression PASS")
        return
    assert all(getattr(args,"verified_"+n+"_json") for n in
               ("mg24","mg29","mg40","mg41"))
    load=lambda n:json.loads((ROOT/getattr(args,"verified_"+n+"_json")).read_text())
    jobs=recovered_data(*(load(n) for n in ("mg24","mg29","mg40","mg41")))
    cases=[run_case(*job) for job in jobs]
    assert [(x["mesh_cells"],x["cutoff_k"]) for x in cases]==[
        (16,12),(16,16),(32,12),(32,16)]
    out={
      "status":"ORIGINAL_MG42_EXACT_RELATIVE_SOURCE_G_ERROR_FEE_BUDGET",
      "canonical_W_ODD_NEG":"OPEN",
      "MG24_verified_original_run":39378465438,
      "MG29_verified_original_run":39440914565,
      "MG40_verified_original_run":39513403010,
      "MG41_verified_original_run":39519080670,
      "original_SI10_25physical_23adapted_plus_true_sinh_pole24D":True,
      "signed_arch_seven_prime_complete_original_frequency_inherited":True,
      "exact_ideal_source_SPD_and_actual_fee_bearing_negative_replayed":True,
      "scaled_fee_PSD_monotone_source_matrix_family":True,
      "rational_LDL_and_negative_Rayleigh_bracket_endpoints":True,
      "all_four_best_MG40_nonscalar_responses_accounted":True,
      "all_24_MG41_original_nonscalar_ideal_positive_actual_negative":True,
      "counterfactual_fee_scaling_not_proof_of_real_strict_contraction":True,
      "real_original_24D_source_strict_contraction_certified":False,
      "true_original_470D_strong_inverse_certified":False,
      "signed_original_51over56_negative_cap_certified":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "complete_even_Weil_CC27_RH":"OPEN",
      "scenarios":cases,
      "next":"Reduce actual coupled Gstar mixed uncertainty so its valid full matrix fee fits below exact relative source budget; alternatively change original B or source moment enclosure. Never promote scaled counterfactual fees to actual full-source positivity without a certified new original upper."
    }
    path=ROOT/args.output;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("MG42 exact original mixed G uncertainty relative source budgets:",
          json.dumps({"cases":[{
             "mesh":x["mesh_cells"],"k":x["cutoff_k"],"B":x["original_nonscalar_B"],
             "strict_source_budget_lower":float(Q(x[
                 "exact_ratio_fee_scale_positive_below_or_equal"])),
             "strict_source_budget_upper":float(Q(x[
                 "exact_ratio_fee_scale_negative_above_or_equal"])),
             "rounds":x["bisection_rounds_resolved"]}
             for x in cases],
             "current_source_contraction":False,
             "true_470D_and_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
