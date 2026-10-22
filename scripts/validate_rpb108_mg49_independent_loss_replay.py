#!/usr/bin/env python3
"""MG49 independent exact accounting audit.

No import of MG49 producer. Rebuild each complete 24D source upper
through MG48's independently written ungrouped-polynomial replay and
verify additive source loss identities and the certified MG43 witness.
Counterfactual fee removals are explicitly noncertifying.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
import validate_rpb108_mg48_independent_joint_replay as independent48
N=24;P=23
PARTS=("measured_direct","H_omitted_upper","H_omitted_lower_credit",
       "strong_high_tail","G_center_signed",
       "G_uncertainty_P0","G_uncertainty_B","pole_uncertainty")
FEES=("G_uncertainty_P0","G_uncertainty_B","pole_uncertainty","strong_high_tail")
rd=independent48.rd
add=independent48.add
minus=independent48.minus
scale=independent48.scale
eye=independent48.eye
quadratic=independent48.quadratic
gersh=independent48.gersh
def fold(matrices):
    out=scale(Q(0),eye())
    for a in matrices:out=add(out,a)
    return out
def main():
    a=argparse.ArgumentParser()
    for n in ("mg24","mg46","mg47","mg48","mg49"):
        a.add_argument("--verified-"+n+"-json",required=True)
    opt=a.parse_args()
    load=lambda n:json.loads((ROOT/getattr(opt,"verified_"+n+"_json")).read_text())
    a24,a46,a47,a48,a49=[load(n) for n in ("mg24","mg46","mg47","mg48","mg49")]
    assert a49["status"]=="ORIGINAL_MG49_EXACT_COMPLETE_SOURCE_JOINT_CERTIFICATE_LOSS_AUDIT"
    assert a49["canonical_W_ODD_NEG"]=="OPEN"
    assert a49["counterfactual_fee_removals_prove_no_new_upper"]
    hm,hr,he=original_H24_from_physical_source()
    assert he==Q(a24["physical_Gram_Loewner_row_error"])
    hlow=minus(hm,scale(he,eye()))
    bc=[hm[i][P] for i in range(N)]
    br=[hr[i][P] for i in range(N)]
    count=0
    for s24,s46,s47,s48,s49 in zip(
          [next(y for y in a24["cases"] if y["cutoff_k"]==x["cutoff_k"])
           for x in a49["cases"]],
          a46["scenarios"],a47["scenarios"],a48["scenarios"],a49["cases"]):
        mesh,k=s49["mesh_cells"],s49["cutoff_k"]
        assert (mesh,k)==(s46["mesh_cells"],s46["cutoff_k"])==(s47["mesh_cells"],s47["cutoff_k"])==(s48["mesh_cells"],s48["cutoff_k"])
        # Independent complete original ungrouped-polynomial reconstruction.
        all_candidates,best=independent48.replay(s47,s46,s24,bc,br,hlow)
        assert len(all_candidates)==216
        _,_,ln,un,eta,gamma,pn,whole,omitted=best
        assert s49["selected_MG48_parameters"]=={"G_lower":ln,
           "G_upper":un,"eta":str(eta),"gamma":str(gamma),"pole_fee":pn}
        assert whole==rd(s48["best_joint_complete_24D_upper"])
        components={name:rd(s49["matrix_components_exact"][name]) for name in PARTS}
        assert tuple(s49["matrix_components_exact"])==PARTS
        assert fold(components.values())==whole
        assert components["measured_direct"]==rd(s46["original_MG32_direct_band_24D_upper"])
        assert minus(whole,components["measured_direct"])==omitted
        # Independently rederive the signed centered G term in the
        # ungrouped physical-multiplier form.
        from validate_rpb108_mg23_physical_metric_matrix_envelope import KAPPA
        m=Q(17)+Q(347*k,500)
        b=rd(s47["full_original_rational_response_B"])
        glo=rd(s47["original_G_lower_candidate_matrices"][ln])
        gup=rd(s47["original_G_upper_candidate_matrices"][un])
        gc=scale(Q(1,2),add(glo,gup))
        E=scale(Q(1,2),minus(gup,glo))
        c=[sum((bc[i]*b[i][j] for i in range(N)),Q(0)) for j in range(N)]
        C=[[Q(i==j)+(2*c[j] if i==P else Q(0)) for j in range(N)] for i in range(N)]
        pmat=minus(C,scale((KAPPA+m)/2,b))
        crossUngrouped=add(
            scale(-1,independent48.matmul(independent48.matmul(independent48.trans(C),gc),b)),
            scale(-1,independent48.matmul(independent48.matmul(independent48.trans(b),gc),C)))
        crossUngrouped=add(crossUngrouped,scale(KAPPA+m,independent48.conjugate(gc,b)))
        assert components["G_center_signed"]==scale(1+gamma,crossUngrouped)
        assert components["G_uncertainty_P0"]==scale(
             (1+gamma)*eta,independent48.conjugate(E,pmat))
        assert components["G_uncertainty_B"]==scale(
             (1+gamma)/eta,independent48.conjugate(E,b))
        assert components["strong_high_tail"]==scale(
             (1+gamma)*Q(s24["complete_original_strong_tail_rational"]),
             independent48.matmul(independent48.trans(b),b))
        # Pole fee is computed from archived true source interval and H_D upper.
        hdu=rd(s46["original_complete_omitted_H_upper"])
        ds=[sum((br[i]*abs(b[i][j]) for i in range(N)),Q(0)) for j in range(N)]
        if pn=="isotropic":
            W=scale(4*hdu[P][P]*sum((z*z for z in ds),Q(0)),eye())
        else:
            W=independent48.diag([4*hdu[P][P]*sum(ds,Q(0))*d for d in ds])
        assert components["pole_uncertainty"]==scale(1+1/gamma,W)
        assert components["H_omitted_upper"]==scale(
             1+gamma,independent48.conjugate(hdu,C))
        hdl=scale(1/KAPPA,rd(s47["original_G_lower_candidate_matrices"]["mass_kappa"]))
        assert components["H_omitted_lower_credit"]==scale(
             -(1+gamma)*KAPPA*m,independent48.conjugate(hdl,b))
        ray=[Q(x) for x in s49["same_MG43_exact_negative_rational_ray"]]
        assert ray==[Q(x) for x in s47["selected_exact_inertia_witness"]["rational_vector"]]
        u43=rd(s47["selected_complete_24D_source_upper"])
        r43=quadratic(minus(hlow,u43),ray)
        r48=quadratic(minus(hlow,whole),ray)
        assert r43<0
        assert str(r43)==s49["ray_MG43_source_lower"]
        assert str(r48)==s49["ray_MG48_joint_source_lower"]
        assert str(quadratic(hlow,ray))==s49["ray_physical_Hlo"]
        assert str(quadratic(minus(whole,u43),ray))==s49["ray_MG48_minus_MG43_upper"]
        actual={name:quadratic(components[name],ray) for name in PARTS}
        assert {name:str(actual[name]) for name in PARTS}==s49["ray_component_signed_contributions"]
        assert sum(actual.values(),Q(0))==quadratic(whole,ray)
        fees={name:actual[name] for name in FEES}
        assert all(v>=0 for v in fees.values())
        rank=[{"fee":key,"exact_ray_fee":str(val)}
              for key,val in sorted(fees.items(),key=lambda x:(-x[1],x[0]))]
        assert rank==s49["positive_fee_rank_on_MG43_ray"]
        computed={
          "discard_G_interval_Young_fees":r48+fees["G_uncertainty_P0"]+fees["G_uncertainty_B"],
          "discard_pole_uncertainty":r48+fees["pole_uncertainty"],
          "discard_high_tail":r48+fees["strong_high_tail"],
          "discard_all_four_listed_fees":r48+sum(fees.values(),Q(0))}
        assert {key:str(val) for key,val in computed.items()}==s49["counterfactual_zero_fee_ray_lowers_NOT_CERTIFICATES"]
        assert str(max(Q(0),-r48))==s49["ray_minimum_upper_reduction_needed_for_nonnegative"]
        assert s49["all_complete_original_frequencies_retained_in_actual_candidate"]
        assert s49["no_true_operator_negative_index_claim"]
        count+=1
    assert count==4
    assert a49["all_four_original_joint_uppers_exactly_decomposed"]
    assert a49["all_original_complete_source_witness_ray_comparisons_exact"]
    assert not a49["original_24D_new_contraction"]
    assert not a49["original_470D_inverse_certified"]
    assert not a49["signed_original_51over56_cap_certified"]
    assert a49["independent_original_Fourier_form_domain_audit"]=="OPEN"
    assert a49["complete_even_Weil_CC27_RH"]=="OPEN"
    print("MG49 INDEPENDENT original complete 24D certificate-loss replay PASS",
          {"source_cases":count,"counterfactuals":"NOT_CERTIFICATES",
           "470D_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
