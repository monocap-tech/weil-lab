#!/usr/bin/env python3
"""MG25B: apply exact rational robust nonscalar source trials to verified MG24 ORIGINAL brackets.

Input MUST be the archived original full-frequency MG24 Actions 39378465438
artifact. Reconstruct exact physical 25D SI10 Gram and genuine adapted
24-channel 23+pole basis independently; keep real interval H errors.

Tests scalar MG24 tI and rationalized 24x24 source-aware B proposals,
EVERY coupled G error charged by exact rigorous opnorm bound.

A failure to find positive margin is a failure of this enclosure/trial
method, NOT evidence of negative spectral directions in Astar.
No finite source frame invariance or global 470D inverse is inferred.
"""
import argparse,json,sys
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,plus,mul,sub,norm_upper,residual_upper,serialize,
)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import (
    ROOT,P,interval_frac,pair_coefficients,
    original_transformed_gram,pole_crosses,
    original_full_25_physical_interval_gram,
    protected_inner_cover,geometry,select_sources,
    boundary_intervals,derivative_intervals_and_D3,
    positive_gap,interval_out,centers_and_diag_error
)

def deserialize(data):
    return [[Q(x) for x in row] for row in data]

def original_H24_from_physical_source():
    clusters,_,_,_,_=protected_inner_cover()
    infos,*_=geometry()
    sources=select_sources(infos)
    assert len(sources)==25 and sources[P][0]=="pole"
    raw,physical,_=original_full_25_physical_interval_gram()
    assert physical==sources
    H25=[[interval_frac(x) for x in row] for row in raw]
    bt=[interval_out(x) for x in boundary_intervals(sources,clusters)]
    dt,_=derivative_intervals_and_D3(sources,clusters)
    pivots=[]
    for q in range(24):
        gap=positive_gap(bt[P]*dt[q]-bt[q]*dt[P])
        if gap>0:pivots.append((gap,q))
    _,pivot=max(pivots,key=lambda p:(p[0],-p[1]))
    assert pivot==23
    free=tuple(i for i in range(25) if i not in (P,pivot))
    assert len(free)==23
    det,a,c=pair_coefficients(bt,dt,pivot,free)
    assert positive_gap(det)>0
    H23=original_transformed_gram(H25,free,pivot,a,c)
    b=pole_crosses(H25,free,pivot,a,c)
    H24=[[None]*24 for _ in range(24)]
    for i in range(23):
        for j in range(23):H24[i][j]=H23[i][j]
        H24[i][23]=H24[23][i]=b[i]
    H24[23][23]=H25[P][P]
    center,radii,err=centers_and_diag_error(H24)
    return center,radii,err

def candidate_float_rationalized(Gcenter,Supper,lam,den=64):
    """Floating conditioning estimates only propose rational B, never certify."""
    try:
        g=np.array([[float(x) for x in row] for row in Gcenter],dtype=float)
        s=np.array([[float(x) for x in row] for row in Supper],dtype=float)
        if not np.all(np.isfinite(g)) or not np.all(np.isfinite(s)):
            return None
        s=(s+s.T)/2
        scale=max(1.,float(np.max(np.abs(np.diag(s)))))
        z=np.linalg.solve(s+(lam*scale)*np.eye(24),g)
        if not np.all(np.isfinite(z)) or float(np.max(np.abs(z)))>16:
            return None
        B=[[Q(int(np.rint(float(z[i,j])*den)),den)
               for j in range(24)] for i in range(24)]
        if all(all(x==0 for x in row) for row in B):return None
        return B
    except (ValueError,OverflowError,ZeroDivisionError,
            np.linalg.LinAlgError):
        return None

def validate_input(data):
    assert data["status"]=="ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES"
    assert data["canonical_W_ODD_NEG"]=="OPEN"
    assert data["original_physical_SI10_source_count"]==25
    assert data["physical_23D_plus_genuine_pole_channel_dimension"]==24
    assert data["original_24D_physical_Gram_verified_positive"]
    assert Q(data["original_24D_Gram_ell"])>0
    assert data["true_original_source_pole_response_c_enclosed"]
    assert data["true_complete_original_pole_Gstar_Sstar_Loewner_bracket"]
    assert data["selected_MG19_original_source_lower_replayed"]
    assert data["unselected_lowband_paid_by_global_multiplier_majorant"]
    assert data["whole_real_highband_paid_by_SM41_source_tails"]
    assert not data["actual_full_original_Gstar_Sstar_matrices_evaluated_exactly"]
    assert not data["MG07_actual_full470_source_residual_certified"]
    assert not data["signed_original_negative_cap_51over56"]
    assert data["even_Weil_CC27_RH"]=="OPEN"
    assert data["independent_original_Fourier_form_domain_audit"]=="OPEN"
    assert [x["cutoff_k"] for x in data["cases"]]==[12,16,20]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--verified-mg24-json",required=True)
    p.add_argument("--output",default=
        "artifacts/mg25_original24_robust_source_aware_gate.json")
    args=p.parse_args()
    src=ROOT/args.verified_mg24_json
    data=json.loads(src.read_text())
    validate_input(data)
    Hcenter,Hradii,Herr=original_H24_from_physical_source()
    assert Herr==Q(data["physical_Gram_Loewner_row_error"])
    assert [str(Hcenter[i][23]) for i in range(24)]==data["original_pole_b_center"]
    assert [str(Hradii[i][23]) for i in range(24)]==data["original_pole_b_radii"]
    Hlo=sub(Hcenter,mul(Herr,Id(24)))
    Hup=plus(Hcenter,mul(Herr,Id(24)))
    assert Herr>=0
    all_results=[]
    for case in data["cases"]:
        k=case["cutoff_k"]
        LG=deserialize(case["complete_Gstar_lower"])
        UG=deserialize(case["complete_Gstar_upper"])
        US=deserialize(case["complete_Sstar_upper"])
        Gc=mul(Q(1,2),plus(LG,UG))
        candidates=[("mg24_scalar_fallback",mul(Q(case["scalar_trial_t"]),Id(24)))]
        for regularizer in (Q(1,1000),Q(1,100),Q(1,10),Q(1)):
            B=candidate_float_rationalized(Gc,US,float(regularizer),den=64)
            if B is not None:
                candidates.append(("source_aware_ridge_"+str(regularizer),B))
        seen=set()
        outcomes=[]
        for name,B in candidates:
            encoded=tuple(x for row in B for x in row)
            if encoded in seen:continue
            seen.add(encoded)
            check=residual_upper(Hlo,Hup,LG,UG,US,B)
            outcomes.append({
               "trial":name,
               "original_complete_frequency_pole_corrected":True,
               "rational_B_verified":True,
               "B_opnorm_upper":str(check["candidate_B_opnorm_upper"]),
               "G_Loewner_halfwidth_opnorm_upper":str(
                   check["G_error_opnorm_upper"]),
               "relative_residual_squared_gap_certified":str(check["gap"]),
               "strict_source_one_step_contraction_passed":
                   check["positive_contraction_certified"],
               "Hlo_minus_Rupper_Gershgorin":str(check["margin"]),
               "not_full470_inverse":True
            })
        assert outcomes and outcomes[0]["trial"]=="mg24_scalar_fallback"
        best=max(outcomes,key=lambda o:Q(o["relative_residual_squared_gap_certified"]))
        all_results.append({
          "cutoff_k":k,"trial_count":len(outcomes),
          "original_24D_true_physical_Gram_reconstructed":True,
          "original_MG24_brackets_are_complete_frequency":True,
          "best_trial":best["trial"],
          "best_source_aware_strict_gap":best["relative_residual_squared_gap_certified"],
          "best_strict_one_step_contraction_passed":
             best["strict_source_one_step_contraction_passed"],
          "cases":outcomes
        })
    best_all=max(all_results,key=lambda o:Q(o["best_source_aware_strict_gap"]))
    out={
        "status":"ORIGINAL_24D_ROBUST_NONSCALE_SOURCE_TRIAL_METHOD_GATE",
        "canonical_W_ODD_NEG":"OPEN",
        "verified_MG24_run_id":39378465438,
        "genuine_complete_frequency_original_Gstar_Sstar_brackets_used":True,
        "actual_25D_physical_Gram_reconstructed":True,
        "true_original_24_channel_basis":True,
        "matrix_mixed_Loewner_uncertainty_paid_in_all_trials":True,
        "original_24D_weak_strict_contraction_obtained":
            best_all["best_strict_one_step_contraction_passed"],
        "best_original_24D_source_gap":
            best_all["best_source_aware_strict_gap"],
        "best_original_24D_source_cutoff_k":best_all["cutoff_k"],
        "actual_original_470D_resolvent":False,
        "full_original_signed_51over56_cap":False,
        "finite_source_subspace_invariant":False,
        "independent_Fourier_form_domain_audit":"OPEN",
        "even_Weil_CC27_RH":"OPEN",
        "dyadic_cases":all_results,
        "decision":"Test verified original 24D MG24 full-frequency Loewner brackets against exact rational source-aware mixed trials. Nonpositive margin is a failure of this enclosure method, not a negative spectral mode or an obstruction theorem. No full470 inverse or RH promotion."
    }
    dst=ROOT/args.output;dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(out,indent=2)+"\n")
    print("MG25B original full-frequency source-aware method:",
      json.dumps({
       "best_cutoff":out["best_original_24D_source_cutoff_k"],
       "best_gap":float(Q(out["best_original_24D_source_gap"])),
       "original24_contraction":out["original_24D_weak_strict_contraction_obtained"],
       "trials":[(x["cutoff_k"],x["trial_count"]) for x in all_results],
       "signed470_even_Weil_RH":"OPEN"
      }),flush=True)
if __name__=="__main__":main()
