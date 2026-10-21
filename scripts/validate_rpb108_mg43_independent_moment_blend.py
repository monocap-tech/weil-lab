#!/usr/bin/env python3
"""MG43 — original full-spectrum independent G/S Loewner bracket combinations.

This is an independent ORIGINAL-source method diagnostic and a source
certificate trial, NOT new independently measured Fourier information.
We exploit the fact that original MG24 and MG29 both supply complete-
frequency Loewner-valid G and S moments on the SAME 24D genuine
SI10/MG11 23-adapted + true sinh-pole physical source basis.

For arbitrary independent alpha,beta in [0,1], preserve the two exact
valid matrix inequalities:
  L_G(alpha) = (1-alpha)L24 + alpha L29 <= Gstar
  Gstar <= U_G(alpha) = (1-alpha)U24 + alpha U29
  Sstar <= U_S(beta) = (1-beta)U_S24 + beta U_S29.

For original nonscalar B=tI+D and positive rational eta,
Gc=(LG+UG)/2, E=(UG-LG)/2 >= 0,
U=Hup-2t LG-Gc D-D^T Gc+B^T U_S B+
     eta E + eta^-1 D^T E D.
This is a valid full original 24D Loewner residual upper. It mixes
the independently accepted FIRST and SECOND source moments in
independent directions, beyond the single blend in MG39.

Vary alpha,beta and eta on an explicit finite rational grid for each
of MG42's four BEST original nonscalar B; keep the archived MG40 exact
upper as a fallback. Numerical min eigenvalues rank candidates ONLY.
Exact rational LDL pivots alone can certify positive-definiteness,
and exact rational Rayleigh vectors alone can certify negativity of
a particular lower-bound certificate matrix. A failed signed
Gershgorin margin is never treated as a negative eigenvalue.

The grid is not a proof of optimality or that the actual operator is
negative. The original 470D source inverse, signed 51/56 odd cap,
even/Weil/CC27/RH remain OPEN even if a narrow source trial succeeds.
"""
import argparse,json,sys
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    deserialize,original_H24_from_physical_source)
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,T,mm,plus,sub,mul,gersh_lower,psd,norm_upper)
from validate_rpb108_mg41_ideal_cross_error_feasibility import (
    classify_ideal,exact_spd_ldl,dot)
from validate_rpb108_mg40_anisotropic_source_cross_error import (
    core_and_error,source_B_is_nonscalar)

N=24
CUTS=(12,16)
MESHES=(16,32)
G_GRID=(Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1))
S_GRID=(Q(0),Q(1,2),Q(1))
ETA_GRID=(Q(1,64),Q(1,16),Q(1,4),Q(1,2),Q(1),
          Q(2),Q(4),Q(16),Q(64))

def enc(A):
    return [[str(x) for x in row] for row in A]

def tr(A):
    assert A==T(A)
    return sum((A[i][i] for i in range(N)),Q(0))

def sym_gersh(A):
    assert A==T(A)
    return gersh_lower(A)

def interpolation(A,B,alpha):
    return plus(mul(1-alpha,A),mul(alpha,B))

def min_float_eig(A):
    f=np.asarray([[float(v) for v in row] for row in A],
                 dtype=float)
    if not np.isfinite(f).all():return -float("inf")
    return float(np.linalg.eigvalsh((f+f.T)/2)[0])

def matrix_pieces(LG,UG,US,t,B):
    assert LG==T(LG) and UG==T(UG) and US==T(US)
    assert t>=0
    Gc=mul(Q(1,2),plus(LG,UG))
    E=mul(Q(1,2),sub(UG,LG))
    assert psd(E) and psd(US)
    D=sub(B,mul(t,Id(N)))
    Gcore=sub(mul(-2*t,LG),
        plus(mm(Gc,D),mm(T(D),Gc)))
    Scong=mm(mm(T(B),US),B)
    E_d=mm(mm(T(D),E),D)
    assert E_d==T(E_d) and psd(E_d)
    return Gcore,Scong,E,E_d

def synthetic_regression():
    H=[[Q(i==j)*Q(3) for j in range(N)] for i in range(N)]
    Glo=[[Q(i==j) for j in range(N)] for i in range(N)]
    Ghi=[[Q(i==j)*2 for j in range(N)] for i in range(N)]
    Sup=[[Q(i==j)*4 for j in range(N)] for i in range(N)]
    B=[[Q(i==j,2) for j in range(N)] for i in range(N)]
    X,Y,E,K=matrix_pieces(Glo,Ghi,Sup,Q(1,2),B)
    assert all(x==0 for row in K for x in row)
    assert E==[[Q(i==j,2) for j in range(N)] for i in range(N)]
    assert interpolation(X,X,Q(1,3))==X
    assert psd(E)
    U=plus(plus(H,X),plus(Y,E))
    assert U==T(U)
    return True

def reconstruct_case(mg24,mg29,mg40,mg41,mg42,mesh,k,Hlo,Hup):
    s40=next(s for s in mg40["scenarios"]
             if s["mesh_cells"]==mesh and s["cutoff_k"]==k)
    s41=next(s for s in mg41["scenarios"]
             if s["mesh_cells"]==mesh and s["cutoff_k"]==k)
    s42=next(s for s in mg42["scenarios"]
             if s["mesh_cells"]==mesh and s["cutoff_k"]==k)
    assert s41["classification_counts"]["POSITIVE_EXACT_RATIONAL_LDL"]==6
    assert s41["actual_MG40_certificate_inertia_counts"][
        "NEGATIVE_EXACT_RATIONAL_RAYLEIGH"]==6
    assert s42["original_nonscalar_B"]==s40["best_nonscalar_name"]
    chosen=next(x for x in s40["all_rational_candidate_results"]
                if x["name"]==s42["original_nonscalar_B"])
    archived=next(x for x in s41["trials"] if x["name"]==chosen["name"])
    B=deserialize(chosen["B_original_exact_rational"])
    assert source_B_is_nonscalar(B)
    t=Q(chosen["source_anchor_t"])
    # MG24 and MG29 accepted exact FIRST/SECOND original moments.
    c24=next(c for c in mg24["cases"] if c["cutoff_k"]==k)
    m=next(c for c in mg29["meshes"] if c["mesh_cells"]==mesh)
    c29=next(c for c in m["full_original_frequency_scenarios"]
             if c["cutoff_k"]==k)
    L0=deserialize(c24["complete_Gstar_lower"])
    U0=deserialize(c24["complete_Gstar_upper"])
    S0=deserialize(c24["complete_Sstar_upper"])
    L1=deserialize(c29["full_original_Gstar_lower"])
    U1=deserialize(c29["full_original_Gstar_upper"])
    S1=deserialize(c29["full_original_Sstar_upper"])
    for A in (L0,U0,S0,L1,U1,S1):
        assert A==T(A)
    for L,U,S in ((L0,U0,S0),(L1,U1,S1)):
        assert psd(sub(U,L)) and psd(S)
    # Exact consistency with the entire original MG40 source matrix.
    old_core,Eold,D=core_and_error(Hup,L1,U1,S1,t,B)
    if chosen["selected_method"]=="matrix_Young":
        eta=Q(chosen["selected_eta"])
        oldfee=plus(mul(eta,Eold),
                     mul(1/eta,mm(mm(T(D),Eold),D)))
    else:
        assert chosen["selected_method"]=="MG30_isotropic"
        oldfee=mul(Q(chosen["old_isotropic_fee"]),Id(N))
    old_upper=plus(old_core,oldfee)
    assert tr(old_upper)==Q(chosen["selected_original_full_upper_trace"])
    old_M=sub(Hlo,old_upper)
    assert gersh_lower(old_M)==Q(chosen["selected_original_signed_Gersh"])
    assert archived["actual_MG40_source_certificate_inertia_gate"]==(
        "NEGATIVE_EXACT_RATIONAL_RAYLEIGH")
    ray=[Q(x) for x in archived[
        "actual_MG40_source_certificate_exact_witness"]["rational_vector"]]
    assert dot(ray,old_M)==Q(archived[
        "actual_MG40_source_certificate_exact_witness"][
        "exact_negative_quadratic"])<0

    # Precompute exact original matrix products. Affine blending
    # separately for G- and S-moment certificates is an identity.
    Gpieces=[matrix_pieces(L,U,S1,t,B) for L,U in
             ((L0,U0),(L1,U1))]
    Smats=[matrix_pieces(L1,U1,S,t,B)[1] for S in (S0,S1)]
    proposals=[]
    best=None
    for alpha in G_GRID:
        pg=interpolation(Gpieces[0][0],Gpieces[1][0],alpha)
        E=interpolation(Gpieces[0][2],Gpieces[1][2],alpha)
        Ed=interpolation(Gpieces[0][3],Gpieces[1][3],alpha)
        assert psd(E)
        for beta in S_GRID:
            sg=interpolation(Smats[0],Smats[1],beta)
            core=plus(plus(Hup,pg),sg)
            for eta in ETA_GRID:
                F=plus(mul(eta,E),mul(1/eta,Ed))
                U=plus(core,F)
                M=sub(Hlo,U)
                assert M==T(M)
                signed=sym_gersh(M)
                sample={
                    "original_G_blend_alpha":str(alpha),
                    "original_S_blend_beta":str(beta),
                    "valid_matrix_Young_eta":str(eta),
                    "exact_signed_Gershgorin_lower":str(signed),
                    "full_original_24D_upper_trace":str(tr(U))}
                proposals.append(sample)
                approx=min_float_eig(M)
                # Float ranks proposals, NEVER certifies the result.
                if best is None or approx>best[0]:
                    best=(approx,alpha,beta,eta,U,M,sample)
    assert len(proposals)==len(G_GRID)*len(S_GRID)*len(ETA_GRID)==135
    _,alpha,beta,eta,U,M,sample=best
    # Exact acceptance for proposed best sampled parameters.
    status,witness=classify_ideal(M)
    assert status in ("POSITIVE_EXACT_RATIONAL_LDL",
                      "NEGATIVE_EXACT_RATIONAL_RAYLEIGH","INCONCLUSIVE")
    if status=="POSITIVE_EXACT_RATIONAL_LDL":
        assert len(witness["exact_positive_schur_pivots"])==N
    elif status=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
        v=[Q(x) for x in witness["rational_vector"]]
        assert dot(v,M)==Q(witness["exact_negative_quadratic"])<0
    baseline_m=Q(chosen["selected_original_signed_Gersh"])
    actualG=gersh_lower(M)
    assert actualG==Q(sample["exact_signed_Gershgorin_lower"])
    # A float-ranked candidate can have worse exact Gersh than MG40.
    # Record that as observed, not claim universal improvement.
    return {
       "mesh_cells":mesh,"cutoff_k":k,
       "source_response_name":chosen["name"],
       "exact_original_rational_B":enc(B),
       "source_anchor_t":str(t),
       "MG40_accepted_best_nonscalar_Gersh_margin":str(baseline_m),
       "MG40_original_full24_upper_trace":str(tr(old_upper)),
       "new_G_blend_alpha":str(alpha),
       "new_S_blend_beta":str(beta),
       "new_matrix_eta":str(eta),
       "new_signed_Gershgorin_lower":str(actualG),
       "Gersh_improvement_vs_MG40":str(actualG-baseline_m),
       "new_original_full24_upper_trace":str(tr(U)),
       "independent_first_and_second_moment_blending":True,
       "all_three_positive_rational_parameters_certified":True,
       "full24_exact_inertia_classification":status,
       "full24_exact_inertia_witness":witness,
       "narrow_actual_original_24D_source_contraction_certified":
             status=="POSITIVE_EXACT_RATIONAL_LDL",
       "source_MG40_negative_original_ray_on_previous_enclosure":[
             str(x) for x in ray],
       "new_certificate_on_prior_negative_source_ray":str(dot(ray,M)),
       "original_24D_new_upper_matrix":enc(U),
       "original_24D_new_source_lower_matrix":enc(M),
       "candidate_full24_matrices_not_selected_by_trace":True,
       "number_valid_rational_parameter_grid_trials":len(proposals),
       "all_grid_candidate_trace_and_Gersh_diagnostics":proposals,
       "approximate_eigenvalue_only_a_candidate_ordering":True,
       "original_470D_inverse_not_proved":True}

def main():
    p=argparse.ArgumentParser()
    for name in ("mg24","mg29","mg40","mg41","mg42"):
        p.add_argument("--verified-"+name+"-json")
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--output",default=
       "artifacts/mg43_original_independent_G_S_matrix_blend.json")
    a=p.parse_args()
    assert synthetic_regression()
    if a.self_test:
        print("MG43 exact valid independently interpolated Loewner source moments algebra PASS")
        return
    assert all(getattr(a,"verified_"+name+"_json") for name in
               ("mg24","mg29","mg40","mg41","mg42"))
    load=lambda name:json.loads((ROOT/getattr(a,"verified_"+name+"_json")).read_text())
    mg24,mg29,mg40,mg41,mg42=(
        load(name) for name in ("mg24","mg29","mg40","mg41","mg42"))
    assert mg24["status"]=="ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES"
    assert mg29["status"]=="ORIGINAL_ADAPTED_THIRD_FOURIER_SOURCE_MOMENT_REFINEMENT"
    assert mg40["status"]=="ORIGINAL_MG40_ANISOTROPIC_FULL_SOURCE_G_CROSS_ERROR_GATE"
    assert mg41["status"]=="ORIGINAL_MG41_NONSCALE_IDEAL_G_CROSS_FEE_FEASIBILITY"
    assert mg42["status"]=="ORIGINAL_MG42_EXACT_RELATIVE_SOURCE_G_ERROR_FEE_BUDGET"
    assert all(d["canonical_W_ODD_NEG"]=="OPEN" for d in
               (mg24,mg29,mg40,mg41,mg42))
    assert mg42["MG41_verified_original_run"]==39519080670
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==Q(mg24["physical_Gram_Loewner_row_error"])
    Hlo=sub(Hmid,mul(Herr,Id(N)))
    Hup=plus(Hmid,mul(Herr,Id(N)))
    result=[reconstruct_case(mg24,mg29,mg40,mg41,mg42,mesh,k,Hlo,Hup)
            for mesh in MESHES for k in CUTS]
    assert [(s["mesh_cells"],s["cutoff_k"]) for s in result]==[
        (16,12),(16,16),(32,12),(32,16)]
    out={
      "status":"ORIGINAL_MG43_INDEPENDENT_COUPLED_G_S_LOEWNER_PARAMETER_RECOMBINATION",
      "canonical_W_ODD_NEG":"OPEN",
      "MG24_verified_original_run":39378465438,
      "MG29_verified_original_run":39440914565,
      "MG40_verified_original_run":39513403010,
      "MG41_verified_original_run":39519080670,
      "MG42_verified_original_run":39520549337,
      "original_25physical_23adapted_plus_true_sinh_pole24D":True,
      "same_original_full_frequency_seven_prime_arch_and_pole_basis":True,
      "G_first_and_S_second_Loewner_brackets_independently_mixed":True,
      "all_540_grid_candidates_exact_rational_source_uppers":True,
      "new_independent_original_Fourier_measurements_added":False,
      "float_candidate_ranking_never_used_as_proof":True,
      "all_reported_matrix_signs_require_exact_rational_LDL_or_Rayleigh":True,
      "any_strict_original_24D_source_contraction":any(
         x["narrow_actual_original_24D_source_contraction_certified"]
         for x in result),
      "full_original_470D_strong_inverse_certified":False,
      "signed_original_51over56_negative_cap_certified":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "complete_even_Weil_CC27_RH":"OPEN",
      "scenarios":result,
      "next":"If all exact full matrices remain nonpositive, MG44 must generate NEW source-specific original G/S correlation information rather than retune MG24/MG29 complete-frequency brackets; a restricted positive 24D source residual is not a full original 470D strong inverse."
    }
    path=ROOT/a.output;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("MG43 exact original coupled G/S 24D independent mixing:",
      json.dumps({"cases":[{
         "mesh":r["mesh_cells"],"k":r["cutoff_k"],
         "B":r["source_response_name"],
         "alpha_G":r["new_G_blend_alpha"],
         "beta_S":r["new_S_blend_beta"],
         "eta":r["new_matrix_eta"],
         "old_gersh":float(Q(r["MG40_accepted_best_nonscalar_Gersh_margin"])),
         "new_gersh":float(Q(r["new_signed_Gershgorin_lower"])),
         "full_exact_matrix_sign":r["full24_exact_inertia_classification"]}
         for r in result],
         "source_24D_pos":out["any_strict_original_24D_source_contraction"],
         "470D_Weil_RH":"OPEN"}),flush=True)

if __name__=="__main__":
    main()
