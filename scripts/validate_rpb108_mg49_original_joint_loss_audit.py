#!/usr/bin/env python3
"""MG49 exact decomposition of the accepted MG48 original source certificate.

The output is a *certificate loss audit*, not a new valid operator upper.
All diagnostic zero-fee trials are explicitly counterfactual, not proofs.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    deserialize, original_H24_from_physical_source)
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,T,mm,plus,sub,mul,gersh_lower,psd)
from validate_rpb108_mg23_physical_metric_matrix_envelope import KAPPA
N=24;P=23
COMPONENTS=("measured_direct","H_omitted_upper","H_omitted_lower_credit",
            "strong_high_tail","G_center_signed",
            "G_uncertainty_P0","G_uncertainty_B","pole_uncertainty")
FEES=("G_uncertainty_P0","G_uncertainty_B","pole_uncertainty","strong_high_tail")
def mat(x):
    z=deserialize(x)
    assert len(z)==N and all(len(r)==N for r in z)
    return z
def enc(a):return [[str(x) for x in r] for r in a]
def diag(vals):
    a=[[Q(0)]*N for _ in range(N)]
    for i,v in enumerate(vals):a[i][i]=v
    return a
def sand(a,x):return mm(mm(T(x),a),x)
def cross(a,x,y):return plus(mm(mm(T(x),a),y),mm(mm(T(y),a),x))
def qf(v,a):return sum((v[i]*a[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def fold(xs):
    out=[[Q(0)]*N for _ in range(N)]
    for x in xs:out=plus(out,x)
    return out
def construct(a24,a46,a47,a48,hm,hr,he):
    b=[hm[i][P] for i in range(N)]
    br=[hr[i][P] for i in range(N)]
    hlow=sub(hm,mul(he,Id(N)))
    results=[]
    for s47,s46,s48 in zip(a47["scenarios"],a46["scenarios"],a48["scenarios"]):
        mesh,k=s48["mesh_cells"],s48["cutoff_k"]
        assert (mesh,k)==(s47["mesh_cells"],s47["cutoff_k"])==(s46["mesh_cells"],s46["cutoff_k"])
        p=s48["best_joint_parameters"]
        L=mat(s47["original_G_lower_candidate_matrices"][p["G_lower"]])
        U=mat(s47["original_G_upper_candidate_matrices"][p["G_upper"]])
        assert psd(sub(U,L))
        gc=mul(Q(1,2),plus(L,U))
        E=mul(Q(1,2),sub(U,L))
        B=mat(s47["full_original_rational_response_B"])
        hdu=mat(s46["original_complete_omitted_H_upper"])
        hdl=mul(1/KAPPA,mat(s47["original_G_lower_candidate_matrices"]["mass_kappa"]))
        assert psd(sub(hdu,hdl))
        m=Q(17)+Q(347*k,500)
        row24=next(x for x in a24["cases"] if x["cutoff_k"]==k)
        assert Q(row24["original_global_lowband_majorant_M"])==m
        tau=Q(row24["complete_original_strong_tail_rational"])
        assert tau>=0
        eta=Q(p["eta"]);gamma=Q(p["gamma"])
        assert eta>0 and gamma>0
        cb=[sum((b[i]*B[i][j] for i in range(N)),Q(0)) for j in range(N)]
        C0=[[Q(i==j)+(2*cb[j] if i==P else Q(0))
             for j in range(N)] for i in range(N)]
        P0=sub(C0,mul((KAPPA+m)/2,B))
        ds=[sum((br[i]*abs(B[i][j]) for i in range(N)),Q(0))
            for j in range(N)]
        ww=hdu[P][P];assert ww>=0
        assert p["pole_fee"] in ("isotropic","diagonal")
        W=(mul(4*ww*sum((d*d for d in ds),Q(0)),Id(N))
           if p["pole_fee"]=="isotropic"
           else diag([4*ww*sum(ds,Q(0))*d for d in ds]))
        parts={
          "measured_direct":mat(s46["original_MG32_direct_band_24D_upper"]),
          "H_omitted_upper":mul(1+gamma,sand(hdu,C0)),
          "H_omitted_lower_credit":mul(-(1+gamma)*KAPPA*m,sand(hdl,B)),
          "strong_high_tail":mul((1+gamma)*tau,mm(T(B),B)),
          "G_center_signed":mul(-(1+gamma),cross(gc,P0,B)),
          "G_uncertainty_P0":mul((1+gamma)*eta,sand(E,P0)),
          "G_uncertainty_B":mul((1+gamma)/eta,sand(E,B)),
          "pole_uncertainty":mul(1+1/gamma,W)
        }
        assert tuple(parts)==COMPONENTS
        for key,a in parts.items():assert a==T(a),key
        for x in ("H_omitted_upper","strong_high_tail","G_uncertainty_P0",
                  "G_uncertainty_B","pole_uncertainty"):assert psd(parts[x])
        expected=mat(s48["best_joint_complete_24D_upper"])
        assert fold(parts.values())==expected
        assert sub(expected,parts["measured_direct"])==mat(s48["best_joint_omitted_24D_upper"])
        U43=mat(s47["selected_complete_24D_source_upper"])
        assert mat(s48["selected_complete_24D_upper"])==U43
        assert mat(s48["selected_complete_24D_lower"])==sub(hlow,U43)
        assert s48["selected_method"]=="MG43_whole"
        ray_info=s47["selected_exact_inertia_witness"]
        v=[Q(x) for x in ray_info["rational_vector"]]
        assert len(v)==N and any(v)
        ray43=qf(v,sub(hlow,U43))
        assert ray43==Q(ray_info["exact_negative_quadratic"])<0
        ray48=qf(v,sub(hlow,expected))
        terms={name:qf(v,parts[name]) for name in COMPONENTS}
        assert sum(terms.values(),Q(0))==qf(v,expected)
        assert ray48==qf(v,hlow)-sum(terms.values(),Q(0))
        fees={key:terms[key] for key in FEES}
        assert all(x>=0 for x in fees.values())
        counterfactual={
          "discard_G_interval_Young_fees":ray48+fees["G_uncertainty_P0"]+fees["G_uncertainty_B"],
          "discard_pole_uncertainty":ray48+fees["pole_uncertainty"],
          "discard_high_tail":ray48+fees["strong_high_tail"],
          "discard_all_four_listed_fees":ray48+sum(fees.values(),Q(0))}
        result={
          "mesh_cells":mesh,"cutoff_k":k,
          "original_24D_joint_candidate_reconstruction_exact":True,
          "selected_MG48_parameters":p,
          "same_MG43_exact_negative_rational_ray":ray_info["rational_vector"],
          "ray_physical_Hlo":str(qf(v,hlow)),
          "ray_MG43_source_lower":str(ray43),
          "ray_MG48_joint_source_lower":str(ray48),
          "ray_MG48_minus_MG43_upper":str(qf(v,sub(expected,U43))),
          "ray_component_signed_contributions":{k:str(v) for k,v in terms.items()},
          "positive_fee_rank_on_MG43_ray":[
            {"fee":key,"exact_ray_fee":str(value)} for key,value
            in sorted(fees.items(),key=lambda kv:(-kv[1],kv[0]))],
          "counterfactual_zero_fee_ray_lowers_NOT_CERTIFICATES":{
             key:str(v) for key,v in counterfactual.items()},
          "counterfactual_disclaimers":
            "Removing fees violates the established complete-original Loewner certificate and is only an arithmetic diagnostic.",
          "ray_minimum_upper_reduction_needed_for_nonnegative":
            str(max(Q(0),-ray48)),
          "all_complete_original_frequencies_retained_in_actual_candidate":True,
          "no_true_operator_negative_index_claim":True,
          "matrix_components_exact":{name:enc(parts[name]) for name in COMPONENTS}}
        results.append(result)
        print("MG49 original witness diagnostic",mesh,k,{
          "mg43_ray":float(ray43),"mg48_ray":float(ray48),
          "largest_pos_fee":result["positive_fee_rank_on_MG43_ray"][0]["fee"],
          "counterfactual_all_fees_removed":float(
             counterfactual["discard_all_four_listed_fees"])},flush=True)
    return results
def main():
    p=argparse.ArgumentParser()
    for n in ("mg24","mg46","mg47","mg48"):
        p.add_argument("--verified-"+n+"-json",required=True)
    p.add_argument("--output",default="artifacts/mg49_original_joint_loss_audit.json")
    args=p.parse_args()
    load=lambda n:json.loads((ROOT/getattr(args,"verified_"+n+"_json")).read_text())
    a24,a46,a47,a48=(load(n) for n in ("mg24","mg46","mg47","mg48"))
    assert a48["status"]=="ORIGINAL_MG48_COMPLETE_FREQUENCY_JOINT_MULTIPLIER_24D_RESIDUAL"
    assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in (a24,a46,a47,a48))
    hm,hr,he=original_H24_from_physical_source()
    assert he==Q(a24["physical_Gram_Loewner_row_error"])
    assert [str(hm[i][P]) for i in range(N)]==a24["original_pole_b_center"]
    assert [str(hr[i][P]) for i in range(N)]==a24["original_pole_b_radii"]
    cases=construct(a24,a46,a47,a48,hm,hr,he)
    assert len(cases)==4
    obj={
      "status":"ORIGINAL_MG49_EXACT_COMPLETE_SOURCE_JOINT_CERTIFICATE_LOSS_AUDIT",
      "canonical_W_ODD_NEG":"OPEN",
      "accepted_input_runs":{"MG24":39378465438,"MG46":39638393721,
                             "MG47":39663431182,"MG48":39685179933},
      "all_four_original_joint_uppers_exactly_decomposed":True,
      "all_original_complete_source_witness_ray_comparisons_exact":True,
      "counterfactual_fee_removals_prove_no_new_upper":True,
      "original_24D_new_contraction":False,
      "original_470D_inverse_certified":False,
      "signed_original_51over56_cap_certified":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "complete_even_Weil_CC27_RH":"OPEN",
      "cases":cases}
    out=ROOT/args.output
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(obj,indent=2)+"\n")
    print("MG49 original exact source 4-case loss audit GENERATED",flush=True)
if __name__=="__main__":main()
