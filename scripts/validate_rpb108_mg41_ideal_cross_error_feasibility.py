#!/usr/bin/env python3
"""MG41 — original complete-spectrum nonscalar ideal mixed-G-error gate.

Exact genuine original 24D source system (MG11 23 adapted + true sinh
pole from SI10 25 physical catalog) and independent accepted MG24, MG29,
MG40 original full-frequency H/G/S matrices.

For fixed original nonscalar B=tI+D, the MG40 rigorously valid source
residual UPPER is U_core+F, where the chosen F is PSD:
  U_core = Hup-2t LG-Gc D-D^T Gc+B^T US B
  F_eta  = eta E+eta^-1 D^T E D >=0 (matrix Young)
  F_old  = 2||E||||D|| I >=0 (original MG30 fallback).
G=(LG+UG)/2+Delta, -E<=Delta<=E, E>=0.

M_ideal = Hlo-U_core is deliberately OPTIMISTIC, not itself a certified
lower bound for the actual residual (it pretends cross uncertainty
has zero cost). Any fixed-source certificate M_actual=M_ideal-F, F>=0.
Consequently if an exact rational vector v has
  v^T M_ideal v <0,
then that exact same v obstructs a strictly POSITIVE source certificate
for every nonnegative mixed-G-error penalty, including unrealistically
zero penalty. A rational negative Rayleigh witness is a no-go for that
particular fixed B AND the currently frozen LG,UG,US,H error envelope,
not a negative mode of the actual original signed operator.

Floating eigenvectors are candidate suggestions ONLY. All proof signs
are exact Fraction. When the idealized matrix has no found negative
ray, optionally give an exact positive-definiteness certificate using
rational LDL, otherwise classify INCONCLUSIVE. Do not use a failed
Gershgorin test to infer a negative quadratic.
"""
import argparse,json,sys
from fractions import Fraction as F
from pathlib import Path
import numpy as np
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    deserialize, original_H24_from_physical_source)
from validate_rpb108_mg25_robust_source_aware_residual import (
    T,mm,plus,sub,mul,Id,gersh_lower,psd,norm_upper)
from validate_rpb108_mg40_anisotropic_source_cross_error import (
    core_and_error,source_B_is_nonscalar)
N=24
MESHES=(16,32)
CUTS=(12,16)
DENOMS=(2**14,2**20,2**28)
def enc(A):return [[str(v) for v in row] for row in A]
def dot(v,A):
    return sum((v[i]*A[i][j]*v[j] for i in range(N)
                for j in range(N)),F(0))
def candidate_rays(A):
    """Numerical eigenvectors propose candidates; signs proved rationally."""
    assert A==T(A)
    for i in range(N):
        v=[F(0)]*N;v[i]=F(1);yield v
    for i in range(N):
        for j in (i+1,23):
            if j==i or j>=N:continue
            for sg in (-1,1):
                v=[F(0)]*N;v[i]=F(1);v[j]=F(sg)
                yield v
    try:
        f=np.array([[float(v) for v in row] for row in A],dtype=float)
        if not np.isfinite(f).all():return
        vals,basis=np.linalg.eigh((f+f.T)/2)
        if not np.isfinite(vals).all() or not np.isfinite(basis).all():return
        for index in list(range(min(6,N))):
            for den in DENOMS:
                v=[F(int(round(float(basis[i,index])*den)),den)
                   for i in range(N)]
                if any(v):yield v
    except (OverflowError,ValueError,np.linalg.LinAlgError):
        return
def exact_spd_ldl(A):
    """Prove strict positive-definiteness by exact rational Schur pivots.

    Returns a complete positive pivot list or None. No numerical
    eigenvalue is ever used to certify SPD.
    """
    assert len(A)==N and A==T(A)
    W=[list(r) for r in A]
    pivots=[]
    for k in range(N):
        d=W[k][k]
        if d<=0:return None
        pivots.append(d)
        for i in range(k+1,N):
            for j in range(i,N):
                W[j][i]-=W[i][k]*W[j][k]/d
                W[i][j]=W[j][i]
    return pivots
def classify_ideal(A):
    assert A==T(A)
    for v in candidate_rays(A):
        z=dot(v,A)
        if z<0:
            return "NEGATIVE_EXACT_RATIONAL_RAYLEIGH",{
                "rational_vector":[str(x) for x in v],
                "exact_negative_quadratic":str(z),
                "nonzero_rational_24D_source_direction":True}
    pivots=exact_spd_ldl(A)
    if pivots is not None:
        return "POSITIVE_EXACT_RATIONAL_LDL",{
           "exact_positive_schur_pivots":[str(x) for x in pivots],
           "strict_full_ideal_24D_matrix_positive":True}
    return "INCONCLUSIVE",{}
def synthetic_regression():
    M=[[F(0)]*N for _ in range(N)]
    for i in range(N):M[i][i]=F(1)
    assert classify_ideal(M)[0]=="POSITIVE_EXACT_RATIONAL_LDL"
    M[7][7]=F(-1,11)
    kind,w=classify_ideal(M)
    assert kind=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH"
    v=[F(q) for q in w["rational_vector"]]
    assert dot(v,M)==F(w["exact_negative_quadratic"])<0
    # Source-positive mixed G penalty on noncommuting toy matrices.
    E=[[F(0)]*N for _ in range(N)]
    D=[[F(0)]*N for _ in range(N)]
    for i in range(N):E[i][i]=F(i+1);D[i][(i+1)%N]=F(1,10)
    Fmat=plus(mul(F(1,2),E),mul(F(2),mm(mm(T(D),E),D)))
    assert psd(Fmat)
    return True
def main():
    p=argparse.ArgumentParser()
    for key in ("mg24","mg29","mg40"):
        p.add_argument("--verified-"+key+"-json")
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--output",default=
        "artifacts/mg41_original_ideal_cross_error_feasibility.json")
    a=p.parse_args()
    assert synthetic_regression()
    if a.self_test:
        print("MG41 independent exact rational ideal cross-error classification regression PASS")
        return
    assert all(getattr(a,"verified_"+key+"_json") for key in ("mg24","mg29","mg40"))
    archive={key:json.loads((ROOT/getattr(a,"verified_"+key+"_json")).read_text())
             for key in ("mg24","mg29","mg40")}
    mg24,mg29,mg40=(archive[key] for key in ("mg24","mg29","mg40"))
    assert mg24["status"]=="ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES"
    assert mg29["status"]=="ORIGINAL_ADAPTED_THIRD_FOURIER_SOURCE_MOMENT_REFINEMENT"
    assert mg40["status"]=="ORIGINAL_MG40_ANISOTROPIC_FULL_SOURCE_G_CROSS_ERROR_GATE"
    assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in (mg24,mg29,mg40))
    assert [mg40["MG24_accepted_run"],mg40["MG29_accepted_run"],
            mg40["MG30_accepted_run"]]==[
                39378465438,39440914565,39442984941]
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==F(mg24["physical_Gram_Loewner_row_error"])
    Hlo=sub(Hmid,mul(Herr,Id(N)))
    Hup=plus(Hmid,mul(Herr,Id(N)))
    scenarios=[]
    for mesh in MESHES:
        for k in CUTS:
            src=next(x for x in mg40["scenarios"]
                     if x["mesh_cells"]==mesh and x["cutoff_k"]==k)
            m=next(x for x in mg29["meshes"] if x["mesh_cells"]==mesh)
            c=next(x for x in m["full_original_frequency_scenarios"]
                    if x["cutoff_k"]==k)
            LG=deserialize(c["full_original_Gstar_lower"])
            UG=deserialize(c["full_original_Gstar_upper"])
            US=deserialize(c["full_original_Sstar_upper"])
            E=mul(F(1,2),sub(UG,LG))
            assert E==T(E) and psd(E) and psd(US)
            trials=[]
            assert len(src["all_rational_candidate_results"])==9
            for item in src["all_rational_candidate_results"]:
                if not item["nonscalar_original_B"]:continue
                name=item["name"]
                B=deserialize(item["B_original_exact_rational"])
                t=F(item["source_anchor_t"])
                assert source_B_is_nonscalar(B)
                core,Echeck,D=core_and_error(Hup,LG,UG,US,t,B)
                assert Echeck==E
                ideal=sub(Hlo,core)
                assert ideal==T(ideal)
                kind,w=classify_ideal(ideal)
                assert kind in ("NEGATIVE_EXACT_RATIONAL_RAYLEIGH",
                                "POSITIVE_EXACT_RATIONAL_LDL","INCONCLUSIVE")
                actual_margin=F(item["selected_original_signed_Gersh"])
                # Reconstruct accepted MG40 selected PSD mixed-G fee.
                if item["selected_method"]=="matrix_Young":
                    eta=F(item["selected_eta"])
                    fee=plus(mul(eta,E),
                             mul(1/eta,mm(mm(T(D),E),D)))
                else:
                    assert item["selected_method"]=="MG30_isotropic"
                    fee=mul(F(item["old_isotropic_fee"]),Id(N))
                assert psd(fee)
                actual=sub(ideal,fee)
                assert gersh_lower(actual)==actual_margin
                # Independently classify the ACTUAL certified source
                # matrix: a negative Gersh lower is NOT an eigenvalue.
                actual_kind,actual_witness=classify_ideal(actual)
                assert actual_kind in ("NEGATIVE_EXACT_RATIONAL_RAYLEIGH",
                   "POSITIVE_EXACT_RATIONAL_LDL","INCONCLUSIVE")
                # For exact negative witness quantify the maximum
                # unavoidable obstruction and the separately
                # charged uncertainty on its same source direction.
                decomposition=None
                if kind=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
                    v=[F(z) for z in w["rational_vector"]]
                    neg=dot(v,ideal)
                    cost=dot(v,fee)
                    assert neg==F(w["exact_negative_quadratic"])<0
                    assert cost>=0 and dot(v,sub(ideal,fee))==neg-cost
                    decomposition={
                       "optimistic_ideal_signed_quadratic":str(neg),
                       "accepted_extra_mixed_G_PSD_fee_on_witness":str(cost),
                       "actual_certified_matrix_quadratic":str(neg-cost),
                       "even_zero_cross_error_fee_cannot_rescue_this_fixed_B":True}
                trials.append({
                    "name":name,
                    "anchor_t":str(t),
                    "original_24D_nonscalar_response":True,
                    "MG40_selected_method":item["selected_method"],
                    "MG40_selected_Gersh_margin":str(actual_margin),
                    "optimistic_zero_G_cross_fee_Gersh_margin":str(
                        gersh_lower(ideal)),
                    "ideal_zero_G_cross_fee_status":kind,
                    "exact_rational_ideal_witness":w,
                    "witness_decomposition":decomposition,
                    "MG40_mixed_error_fee_is_PSD":True,
                    "actual_MG40_source_certificate_inertia_gate":actual_kind,
                    "actual_MG40_source_certificate_exact_witness":actual_witness,
                    "actual_MG40_source_strict_positive_LDL_certified":
                          actual_kind=="POSITIVE_EXACT_RATIONAL_LDL",
                    "original_complete_operator_negative_mode_proved":False})
            assert len(trials)==src["accepted_candidate_count"]-3==6
            counts={
                kind:sum(x["ideal_zero_G_cross_fee_status"]==kind for x in trials)
                for kind in ("NEGATIVE_EXACT_RATIONAL_RAYLEIGH",
                             "POSITIVE_EXACT_RATIONAL_LDL","INCONCLUSIVE")}
            actual_counts={
                kind:sum(x["actual_MG40_source_certificate_inertia_gate"]==kind
                         for x in trials)
                for kind in ("NEGATIVE_EXACT_RATIONAL_RAYLEIGH",
                             "POSITIVE_EXACT_RATIONAL_LDL","INCONCLUSIVE")}
            scenarios.append({
               "mesh_cells":mesh,"cutoff_k":k,
               "actual_MG40_certificate_inertia_counts":actual_counts,
               "true_original_23adapted_plus_sinh_pole":True,
               "all_real_frequency_source_H_G_S_enclosed":True,
               "original_signed_arch_seven_prime_pole_retained":True,
               "MG40_full_24D_selected_margins_exactly_replayed":True,
               "tested_original_nonscalar_B_count":len(trials),
               "classification_counts":counts,
               "every_tested_nonscalar_B_fee_only_refinement_obstructed":
                   counts["NEGATIVE_EXACT_RATIONAL_RAYLEIGH"]==len(trials),
               "trials":trials})
    assert len(scenarios)==4
    out={
      "status":"ORIGINAL_MG41_NONSCALE_IDEAL_G_CROSS_FEE_FEASIBILITY",
      "canonical_W_ODD_NEG":"OPEN",
      "verified_MG24_run":39378465438,
      "verified_MG29_run":39440914565,
      "verified_MG40_run":39513403010,
      "original_true_SI10_25physical_23adapted_plus_sinh_pole24D":True,
      "complete_original_frequency_pole_corrected_source":True,
      "mixed_original_G_error_fee_PSD_and_exact":True,
      "zero_fee_only_necessary_feasibility_gate":True,
      "no_negative_original_operator_mode_inferred":True,
      "total_tested_nonscalar_B":sum(s["tested_original_nonscalar_B_count"]
                                     for s in scenarios),
      "all_tested_nonscalar_B_fee_only_refinement_obstructed":
          all(s["every_tested_nonscalar_B_fee_only_refinement_obstructed"]
              for s in scenarios),
      "source_24D_strict_residual_contraction_certified":any(
          x["actual_MG40_source_strict_positive_LDL_certified"]
          for scenario in scenarios for x in scenario["trials"]),
      "full_original_470D_strong_inverse_certified":False,
      "signed_original_51over56_negative_cap_certified":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "complete_even_Weil_CC27_RH":"OPEN",
      "scenarios":scenarios,
      "next_gate":"If the exact ideal-core matrices carry negative rational rays, improving only mixed G uncertainty fee cannot rescue these fixed nonscalar B. Identify how much source-metric H/Gstar/Sstar CENTER uncertainty or response B direction must change. If some ideal cores admit exact positive LDL, prioritize tighter G cross fees for those responses."}
    path=ROOT/a.output;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("MG41 original nonscalar zero-cross-fee necessary gate:",
      json.dumps({"scenarios":[{"mesh":s["mesh_cells"],"k":s["cutoff_k"],
        "nonscalar_trials":s["tested_original_nonscalar_B_count"],
        "witnessed_negative":s["classification_counts"][
              "NEGATIVE_EXACT_RATIONAL_RAYLEIGH"],
        "ideal_positive":s["classification_counts"][
              "POSITIVE_EXACT_RATIONAL_LDL"],
        "inconclusive":s["classification_counts"]["INCONCLUSIVE"],
        "actual_fee_bearing_negative":s[
            "actual_MG40_certificate_inertia_counts"]["NEGATIVE_EXACT_RATIONAL_RAYLEIGH"],
        "actual_fee_bearing_positive":s[
            "actual_MG40_certificate_inertia_counts"]["POSITIVE_EXACT_RATIONAL_LDL"],
        "actual_fee_bearing_inconclusive":s[
            "actual_MG40_certificate_inertia_counts"]["INCONCLUSIVE"]}
        for s in scenarios],
        "all_nonscalar_fee_only_obstructed":
         out["all_tested_nonscalar_B_fee_only_refinement_obstructed"],
        "any_actual_24D_source_LDL_positive":
         out["source_24D_strict_residual_contraction_certified"],
        "original_470D_even_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
