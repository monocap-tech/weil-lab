#!/usr/bin/env python3
"""MG40: original complete-spectrum anisotropic nonscalar mixed G error.

Real original 24D source: SI10's 25 physical functions, MG11's
23 two-boundary adapted sources and true odd sinh pole. Original
Gstar and Sstar include signed seven-prime/digamma and full-frequency
SM41 high tails through independently accepted MG29/MG24.

The exact source residual R=F-Astar F B satisfies
 R*R=H-GB-B^tG+B^tSB.
For B=tI+D and original full-frequency brackets LG<=G<=UG, S<=US,
write Gc=(LG+UG)/2, E=(UG-LG)/2, Delta=G-Gc.
Then -E<=Delta<=E, E>=0. For ANY real vectors x,y,
 |x^t Delta y| <= sqrt((x^t E x)(y^t E y)).
Proof: [[E,Delta],[Delta,E]] PSD by an orthogonal congruence
to diag(E+Delta,E-Delta); apply PSD block Cauchy-Schwarz.
Thus, for any rational eta>0,
 -(Delta D+D^t Delta) <= eta E + eta^-1 D^t E D.
This is a genuine complete ORIGINAL 24x24 Loewner upper, rather than
MG30's global isotropic 2||E|| ||D|| I uncertainty payment.

For each exact MG30 B, compare independently valid U_MG30 and
U_MG40(eta) at eta in fixed rational grid, selecting the strongest
exact Gershgorin sufficient lower margin of Hlo-U. The baseline
is included, hence the selected Gersh lower never decreases.
Do not infer actual signed operator negativity from a failed
Gersh lower. If positivity is obtained, it is only a 24D source
contraction, not full 470D strong inverse, odd 51/56, or RH.

Report both trace and signed source sufficient margins separately,
and export rational matrices for independent best-nonscalar replay.
"""
import argparse,json,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    original_H24_from_physical_source,deserialize)
from validate_rpb108_mg25_robust_source_aware_residual import (
    T,mm,plus,sub,mul,Id,shift,gersh_lower,norm_upper,psd)
from validate_rpb108_mg30_anchored_nonscalar_residual import (
    case_candidates,anchored_upper,independent_pole_regression)

N=24
MESHES=(16,32)
CUTS=(12,16)
ETA_GRID=(F(1,64),F(1,16),F(1,4),F(1,2),F(1),
          F(2),F(4),F(16),F(64))
def tr(M):
    assert M==T(M)
    return sum((M[i][i] for i in range(N)),F(0))
def encode(M):
    return [[str(x) for x in row] for row in M]
def zero(M):
    return all(x==0 for row in M for x in row)
def source_B_is_nonscalar(B):
    return any(B[i][j]!=(B[0][0] if i==j else F(0))
               for i in range(N) for j in range(N))
def exact_anisotropic_fee(E,D,eta):
    assert eta>0 and E==T(E)
    ED=mm(E,D)
    M=mm(T(D),ED)
    assert M==T(M)
    return plus(mul(eta,E),mul(1/eta,M))
def core_and_error(Hup,LG,UG,US,t,B):
    assert t>=0 and LG==T(LG) and UG==T(UG)
    E=mul(F(1,2),sub(UG,LG))
    Gc=mul(F(1,2),plus(UG,LG))
    D=sub(B,mul(t,Id(N)))
    core=plus(
      sub(sub(Hup,mul(2*t,LG)),
          plus(mm(Gc,D),mm(T(D),Gc))),
      mm(mm(T(B),US),B))
    assert core==T(core) and E==T(E)
    return core,E,D
def independent_2D_block_regression():
    """A 3x3 exact noncommuting example of the analytic block lemma."""
    A=[[F(3),F(1),F(0)],[F(1),F(2),F(0)],[F(0),F(0),F(1)]]
    Delta=[[F(1),F(1,2),F(0)],[F(1,2),F(-1,2),F(0)],[F(0),F(0),F(1,4)]]
    D=[[F(1),F(0),F(1)],[F(0),F(1,2),F(-1)],
       [F(1,3),F(0),F(1)]]
    assert psd(A) and psd(sub(A,Delta)) and psd(plus(A,Delta))
    for eta in (F(1,4),F(1),F(4)):
        bound=plus(mul(eta,A),mul(1/eta,mm(mm(T(D),A),D)))
        actual=plus(mm(Delta,D),mm(T(D),Delta))
        assert psd(sub(bound,actual))
        assert psd(plus(bound,actual))
    return True
def candidate_result(name,t,B,Hlo,Hup,LG,UG,US,accepted):
    baseline=anchored_upper(Hlo,Hup,LG,UG,US,t,B)
    assert str(baseline["margin"])==accepted["gershgorin_margin"]
    core,E,D=core_and_error(Hup,LG,UG,US,t,B)
    oldfee=2*norm_upper(E)*norm_upper(D)
    old=shift(core,oldfee)
    assert gersh_lower(sub(Hlo,old))==baseline["margin"]
    old_margin=baseline["margin"]
    old_trace=tr(old)
    rows=[]
    selected={"method":"MG30_isotropic","eta":None,
              "margin":old_margin,"upper":old,"fee":shift(mul(0,E),oldfee)}
    # When D is zero, zero is an EXACT mixed error penalty, no eta E.
    if not zero(D):
        DE=mm(T(D),mm(E,D))
        assert DE==T(DE)
        for eta in ETA_GRID:
            fee=plus(mul(eta,E),mul(1/eta,DE))
            U=plus(core,fee)
            m=gersh_lower(sub(Hlo,U))
            rows.append({"eta":str(eta),
                "exact_Gershgorin_margin":str(m),
                "full_original_24D_upper_trace":str(tr(U)),
                "uncertainty_fee_trace":str(tr(fee)),
                "strict_source_contraction":m>0})
            if m>selected["margin"] or (
                  m==selected["margin"] and tr(U)<tr(selected["upper"])):
                selected={"method":"matrix_Young","eta":eta,
                          "margin":m,"upper":U,"fee":fee}
    assert selected["margin"]>=old_margin
    U=selected["upper"]
    info={
       "name":name,"source_anchor_t":str(t),
       "nonscalar_original_B":source_B_is_nonscalar(B),
       "B_original_exact_rational":encode(B),
       "old_MG30_original_signed_Gersh":str(old_margin),
       "old_MG30_original_upper_trace":str(old_trace),
       "old_isotropic_fee":str(oldfee),
       "selected_method":selected["method"],
       "selected_eta":str(selected["eta"]) if selected["eta"] else None,
       "selected_original_signed_Gersh":str(selected["margin"]),
       "signed_Gersh_improvement":str(selected["margin"]-old_margin),
       "selected_original_full_upper_trace":str(tr(U)),
       "selected_uncertainty_fee_trace":str(tr(selected["fee"])),
       "strict_24D_original_source_contraction":selected["margin"]>0,
       "tested_nonscalar_matrix_Young_etas":rows,
       "true_470D_signed_negative_cap":False,
    }
    return info,U
def main():
    p=argparse.ArgumentParser()
    for k in ("mg24","mg29","mg30"):
        p.add_argument("--verified-"+k+"-json")
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--output",default="artifacts/mg40_original_anisotropic_cross_error.json")
    a=p.parse_args()
    assert independent_2D_block_regression()
    if a.self_test:
        print("MG40 exact block-PSD anisotropic source lemma regression PASS")
        return
    assert all(getattr(a,"verified_"+k+"_json") for k in ("mg24","mg29","mg30"))
    original24=json.loads((ROOT/a.verified_mg24_json).read_text())
    original29=json.loads((ROOT/a.verified_mg29_json).read_text())
    original30=json.loads((ROOT/a.verified_mg30_json).read_text())
    assert independent_pole_regression()
    assert original24["status"]=="ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES"
    assert original29["status"]=="ORIGINAL_ADAPTED_THIRD_FOURIER_SOURCE_MOMENT_REFINEMENT"
    assert original30["status"]=="ORIGINAL_24D_ANCHORED_NONSCALE_MIXED_RESIDUAL_GATE"
    assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in
               (original24,original29,original30))
    assert original30["verified_original_MG24_run_id"]==39378465438
    assert original30["verified_original_MG29_run_id"]==39440914565
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==F(original24["physical_Gram_Loewner_row_error"])
    Hlo=sub(Hmid,mul(Herr,Id(N)))
    Hup=plus(Hmid,mul(Herr,Id(N)))
    scenarios=[]
    for mesh in MESHES:
        m=next(x for x in original29["meshes"] if x["mesh_cells"]==mesh)
        for k in CUTS:
            c=next(x for x in m["full_original_frequency_scenarios"]
                   if x["cutoff_k"]==k)
            o=next(x for x in original30["scenarios"]
                   if x["mesh_cells"]==mesh and x["cutoff_k"]==k)
            g24=next(x for x in original24["cases"] if x["cutoff_k"]==k)
            LG=deserialize(c["full_original_Gstar_lower"])
            UG=deserialize(c["full_original_Gstar_upper"])
            US=deserialize(c["full_original_Sstar_upper"])
            Gc=mul(F(1,2),plus(LG,UG))
            E=mul(F(1,2),sub(UG,LG))
            # Original Loewner brackets must define a PSD error radius.
            assert E==T(E) and psd(E)
            assert psd(US)
            candidates=case_candidates(Gc,US,F(g24["scalar_trial_t"]))
            assert len(candidates)==o["candidate_count"]
            assert [x[0] for x in candidates]==[x["name"] for x in o["trials"]]
            result=[];matrices={}
            for (name,t,B),accepted in zip(candidates,o["trials"]):
                one,U=candidate_result(name,t,B,Hlo,Hup,LG,UG,US,accepted)
                result.append(one);matrices[name]=U
            best=max(result,key=lambda x:F(x["selected_original_signed_Gersh"]))
            nons=[x for x in result if x["nonscalar_original_B"]]
            assert nons and len(nons)==o["nonscalar_candidate_count"]
            best_non=max(nons,key=lambda x:F(x["selected_original_signed_Gersh"]))
            B=deserialize(best_non["B_original_exact_rational"])
            assert source_B_is_nonscalar(B)
            selected=matrices[best_non["name"]]
            A=sub(Hlo,selected)
            assert gersh_lower(A)==F(best_non["selected_original_signed_Gersh"])
            scenarios.append({
              "mesh_cells":mesh,"cutoff_k":k,
              "true_original_25physical_23adapted_plus_pole_channels":True,
              "original_full_real_frequency_pole_correction_inherited":True,
              "MG30_all_original_candidate_margins_replayed_exactly":True,
              "original_G_error_E_exact_PSD":True,
              "original_Sstar_upper_exact_PSD":True,
              "accepted_candidate_count":len(result),
              "old_best_nonscalar_margin":o["best_nonscalar_Gershgorin_margin"],
              "best_nonscalar_name":best_non["name"],
              "best_nonscalar_margin":best_non["selected_original_signed_Gersh"],
              "best_nonscalar_selected_method":best_non["selected_method"],
              "best_nonscalar_upper_FULL24":encode(selected),
              "best_nonscalar_Hlo_minus_upper_FULL24":encode(A),
              "best_any_name":best["name"],
              "best_any_signed_Gersh":best["selected_original_signed_Gersh"],
              "all_rational_candidate_results":result})
    assert [(x["mesh_cells"],x["cutoff_k"]) for x in scenarios]==[
       (16,12),(16,16),(32,12),(32,16)]
    best=max((c for s in scenarios for c in s["all_rational_candidate_results"]),
        key=lambda x:F(x["selected_original_signed_Gersh"]))
    out={
      "status":"ORIGINAL_MG40_ANISOTROPIC_FULL_SOURCE_G_CROSS_ERROR_GATE",
      "canonical_W_ODD_NEG":"OPEN",
      "MG24_accepted_run":39378465438,"MG29_accepted_run":39440914565,
      "MG30_accepted_run":39442984941,
      "true_original_SI10_25physical_23adapted_plus_sinh_pole24D":True,
      "full_original_real_frequency_Gstar_Sstar_enclosed":True,
      "original_signed_arch_prime7_multiplier_and_pole_inherited":True,
      "true_original_block_PSD_cross_uncertainty_lemma":True,
      "source_uncertainty_full_matrix_not_isotropic_only":True,
      "baseline_MG30_candidate_selection_kept_as_fallback":True,
      "exact_rational_full_24D_source_Gersh_decisions":True,
      "any_strict_original_24D_source_contraction":any(
          F(x["selected_original_signed_Gersh"])>0
          for s in scenarios for x in s["all_rational_candidate_results"]),
      "best_source_candidate_name":best["name"],
      "best_source_candidate_Gersh":best["selected_original_signed_Gersh"],
      "all_original_470D_inverse_certified":False,
      "signed_original_negative_51over56_cap_certified":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "even_Weil_CC27_RH":"OPEN",
      "scenarios":scenarios,
      "next_gate":"If matrix Young reduces MG30 anisotropic nonscalar penalty yet no positive original 24D margin, classify limiting directions of coupled source G/S moment enclosures. A narrow 24D source success would still need full-470 inverse and signed spectral cap separately."}
    dest=ROOT/a.output
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("MG40 original anisotropic nonscalar:",json.dumps({
      "cases":[{
        "mesh":s["mesh_cells"],"k":s["cutoff_k"],
        "best_nonscalar_old":float(F(s["old_best_nonscalar_margin"])),
        "best_nonscalar_new":float(F(s["best_nonscalar_margin"])),
        "best_any_new":float(F(s["best_any_signed_Gersh"])),
        "best_nonscalar_method":s["best_nonscalar_selected_method"],
        "improved_candidates":sum(F(x["signed_Gersh_improvement"])>0 for x
           in s["all_rational_candidate_results"]),
        "strict":any(x["strict_24D_original_source_contraction"] for x
           in s["all_rational_candidate_results"])}
        for s in scenarios],
      "global_source_strict":out["any_strict_original_24D_source_contraction"],
      "full470_and_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
