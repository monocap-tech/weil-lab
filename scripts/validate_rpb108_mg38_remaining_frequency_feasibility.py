#!/usr/bin/env python3
"""MG38: rigorous original whole-spectrum source-remainder feasibility audit.

MG37 proved that adding measured [4,8] upper V to an UNCHANGED omitted
frequency upper U0 gives Unew=UMG32+V >= UMG32 in Loewner order.
MG38 reintroduces the independent, previously accepted MG30 original
full-frequency H/G/S moment source enclosure to test the genuinely
different full-frequency upper *at the MATRIX level*, and derives an
exact source-metric feasibility threshold for any future remainder.

Every result concerns genuine SI10 physical source 23 adapted + sinh
pole (dimension 24), original 7-prime/digamma and all real frequencies;
it does NOT classify the actual signed operator or prove original 470D
invertibility.

True original source R*R <= U30 (anchored full-frequency MG30) and
R*R <= U36 (direct MG36 [0,4]+[4,8]+original omitted-tail upper).
Each is independently proved. Comparing exact 24x24 matrices:
 * U36-U30 PSD proof -> MG30 matrix Loewner dominates MG36.
 * rational v with v^T(U36-U30)v<0 -> this direction does NOT
   permit a matrix Loewner dominance claim (does not compare operators).
 * otherwise report INCONCLUSIVE, without inferring order from TRACE.

MG36 directly measured-band upper V is itself PSD, so any future
unmeasured/prefix upper P>=0 satisfying Hlo-(V+P)>0 requires
 Hlo-V >0. A rational Rayleigh vector with v^T(Hlo-V)v<=0
is a true NO-GO for source contraction using that particular V,
even with the mathematically impossible ideal P=0. If no negative
witness appears, this necessary condition is inconclusive.

Real spectral vectors are ONLY proposed using float eigensolvers;
all conclusions are exact Fraction-based Rayleigh/congruence tests.
"""
import argparse,json,sys
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import deserialize
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,T,mm,plus,sub,mul,shift,norm_upper,gersh_lower)
from validate_rpb108_mg30_anchored_nonscalar_residual import (
    case_candidates,anchored_upper)

N=24
DEN=2**20

def tm(A):
    return [[x for x in row] for row in A]

def trace(A):
    assert A==T(A)
    return sum((A[i][i] for i in range(N)),Q(0))

def raw_rational(M):
    A=deserialize(M)
    assert len(A)==N and all(len(row)==N for row in A)
    assert A==T(A)
    return A

def quantize_float(v,den):
    return [Q(int(round(float(x)*den)),den) for x in v]

def quadratic(A,v):
    assert len(v)==N and len(A)==N
    return sum((v[i]*A[i][j]*v[j] for i in range(N)
                 for j in range(N)),Q(0))

def eig_proposal(A):
    try:
        af=np.array([[float(x) for x in row] for row in A],
                    dtype=float)
        if not np.isfinite(af).all():return None
        af=(af+af.T)/2
        values,W=np.linalg.eigh(af)
        if not np.isfinite(values).all() or not np.isfinite(W).all():
            return None
        return values,W
    except (OverflowError,ValueError,np.linalg.LinAlgError):
        return None

def signed_exact_matrix_gate(A):
    """Never infer inertia from unproven floating eigenvalue signs."""
    assert A==T(A)
    negative=None;positive=None
    trial=eig_proposal(A)
    if trial is not None:
        _,W=trial
        for idx in range(N):
            for den in (2**16,2**24,2**32):
                v=quantize_float(W[:,idx],den)
                if not any(v):continue
                q=quadratic(A,v)
                if q<0:
                    negative={"vector":[str(x) for x in v],
                        "strict_exact_negative_quadratic":str(q),
                        "original_24D_vector":True}
                    break
            if negative is not None:break
        if negative is None:
            # Exact congruence via rationalized full eigenbasis.
            for den in (2**16,2**24):
                R=[[Q(int(round(float(W[i,j])*den)),den)
                     for j in range(N)] for i in range(N)]
                congr=mm(mm(T(R),A),R)
                m=gersh_lower(congr)
                if m>0:
                    positive={"exact_congruence_Gershgorin_positive":str(m),
                        "rational_basis_full_rank_by_positivity":True,
                        "exact_rational_congruence_basis":[
                            [str(v) for v in row] for row in R]}
                    break
    if negative is not None:return "NEGATIVE_RATIONAL_RAYLEIGH_WITNESS",negative
    if positive is not None:return "POSITIVE_RATIONAL_CONGRUENCE_WITNESS",positive
    if gersh_lower(A)>0:
        return "POSITIVE_EXACT_GERSHGORIN",{
          "exact_Gershgorin_lower":str(gersh_lower(A))}
    return "INCONCLUSIVE",{}

def rebuild_mg30_original_upper(Hlo,Hup,LG,UG,US,t,B):
    """The accepted MG30 original anchored matrix inequality exactly."""
    E=mul(Q(1,2),sub(UG,LG))
    Gc=mul(Q(1,2),plus(LG,UG))
    D=sub(B,mul(t,Id(N)))
    cross=plus(mm(Gc,D),mm(T(D),Gc))
    action=mm(mm(T(B),US),B)
    U=shift(plus(sub(sub(Hup,mul(2*t,LG)),cross),action),
            2*norm_upper(E)*norm_upper(D))
    assert U==T(U)
    return U

def analysis(old24,old29,old30,old36):
    assert old24["status"]=="ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES"
    assert old29["status"]=="ORIGINAL_ADAPTED_THIRD_FOURIER_SOURCE_MOMENT_REFINEMENT"
    assert old30["status"]=="ORIGINAL_24D_ANCHORED_NONSCALE_MIXED_RESIDUAL_GATE"
    assert old36["status"]=="ORIGINAL_MG36_DIRECT_BAND_RESIDUAL_FULL24_MATRIX_GATE"
    assert all(x["canonical_W_ODD_NEG"]=="OPEN"
               for x in (old24,old29,old30,old36))
    assert old36["verified_MG24_run_id"]==39378465438
    assert old36["verified_MG29_run_id"]==39440914565
    assert old36["verified_MG30_run_id"]==39442984941
    assert old36["verified_MG32_run_id"]==39459624082
    assert old36["verified_MG33_run_id"]==39462301107
    assert old36["verified_MG35_run_id"]==39488378664
    assert old36["new_complete_24D_original_residual_UPPER_matrices_exported"]
    assert old36["PSD_monotone_full_matrix_original_remainder_reuse"]
    assert all(s["strict_original_source_contraction"] is False
               for s in old36["scenarios"])
    hcharge=Q(old24["physical_Gram_Loewner_row_error"])
    cases=[]
    for s in old36["scenarios"]:
        k=s["cutoff_k"]; name=s["source_trial"]
        assert k in (12,16)
        U36=raw_rational(s["full_original_Rupper_FULL24"])
        A36=raw_rational(s["full_original_Hlo_minus_Rupper_FULL24"])
        V=raw_rational(s["new_direct_band_FULL24_upper"])
        Hlo=plus(U36,A36)
        Hup=shift(Hlo,2*hcharge)
        assert trace(U36)==Q(s["MG36_complete_original_Rupper_trace"])
        assert trace(V)==Q(s["new_MG36_joint_4to8_upper_trace"])
        assert gersh_lower(A36)==Q(s["full_original_24D_strict_Gershgorin_margin"])
        assert s["original_23adapted_plus_true_pole_channels"]
        assert s["complete_real_frequency_and_original_multiplier"]
        mg30=next(x for x in old30["scenarios"] if
                  x["mesh_cells"]==32 and x["cutoff_k"]==k)
        mg29m=next(x for x in old29["meshes"]
                   if x["mesh_cells"]==32)
        mg29c=next(x for x in mg29m["full_original_frequency_scenarios"]
                   if x["cutoff_k"]==k)
        mg24c=next(x for x in old24["cases"]
                   if x["cutoff_k"]==k)
        LG=raw_rational(mg29c["full_original_Gstar_lower"])
        UG=raw_rational(mg29c["full_original_Gstar_upper"])
        US=raw_rational(mg29c["full_original_Sstar_upper"])
        Gc=mul(Q(1,2),plus(LG,UG))
        t0=Q(mg24c["scalar_trial_t"])
        allB={name2:(tt,B) for name2,tt,B
              in case_candidates(Gc,US,t0)}
        assert len(allB)==mg30["candidate_count"]==9
        assert name in allB
        t,B=allB[name]
        U30=rebuild_mg30_original_upper(Hlo,Hup,LG,UG,US,t,B)
        replay=anchored_upper(Hlo,Hup,LG,UG,US,t,B)
        original=next(x for x in mg30["trials"] if x["name"]==name)
        assert str(replay["margin"])==original["gershgorin_margin"]
        assert gersh_lower(sub(Hlo,U30))==replay["margin"]
        compare=sub(U36,U30)
        order,witness=signed_exact_matrix_gate(compare)
        # A necessary condition for residual source contraction
        # even with zero remaining/prefix cost. If the exact source
        # Hlo-V has a negative ray, ANY actual PSD prefix/remainder
        # upper P still satisfies Hlo-(V+P) <= Hlo-V.
        ideal=sub(Hlo,V)
        ideal_status,ideal_witness=signed_exact_matrix_gate(ideal)
        if ideal_status=="NEGATIVE_RATIONAL_RAYLEIGH_WITNESS":
            assert Q(ideal_witness["strict_exact_negative_quadratic"])<0
        if order=="POSITIVE_RATIONAL_CONGRUENCE_WITNESS":
            assert Q(witness["exact_congruence_Gershgorin_positive"])>0
        cases.append({
          "cutoff_k":k,"original_MG30_source_trial":name,
          "original_source_23adapted_plus_genuine_pole":True,
          "MG30_complete_original_frequency_first_second_moments":True,
          "MG36_complete_original_frequency_pole_residual":True,
          "MG30_original_24D_full_residual_UPPER_trace":str(trace(U30)),
          "MG36_original_24D_full_residual_UPPER_trace":str(trace(U36)),
          "MG36_to_MG30_full_upper_trace_ratio":str(trace(U36)/trace(U30))
               if trace(U30)>0 else None,
          "MG30_original_Hlo_minus_Rupper_Gershgorin":str(replay["margin"]),
          "MG36_original_Hlo_minus_Rupper_Gershgorin":str(gersh_lower(A36)),
          "MG36_minus_MG30_upper_full24_trace":str(trace(compare)),
          "MG36_minus_MG30_upper_full24_inertia_gate":order,
          "MG36_minus_MG30_witness":witness,
          "MG36_minus_MG30_upper_FULL24":[
              [str(q) for q in row] for row in compare],
          "no_trace_to_Loewner_promotion":True,
          "new_MG36_band_only_upper_trace":str(trace(V)),
          "necessary_Hlo_minus_band_alone_inertia_gate":ideal_status,
          "necessary_Hlo_minus_band_alone_witness":ideal_witness,
          "necessary_Hlo_minus_band_alone_FULL24":[
              [str(q) for q in row] for row in ideal],
          "new_band_upper_itself_original_PSD":True,
          "original_complete_operator_negative_mode_proved":False,
          "new_full_470D_inverse_proved":False})
    assert [(c["cutoff_k"],c["original_MG30_source_trial"]) for c in cases]==[
       (12,"MG24_scalar_t"),(12,"matrix_ridge_1/10_blend_1/4"),
       (16,"MG24_scalar_t"),(16,"matrix_ridge_1/10_blend_1/4")]
    return {
      "status":"ORIGINAL_MG38_WHOLE_FREQUENCY_REMAINDER_FEASIBILITY_GATE",
      "canonical_W_ODD_NEG":"OPEN",
      "original_MG24_accepted_run":39378465438,
      "original_MG29_accepted_run":39440914565,
      "original_MG30_accepted_run":39442984941,
      "original_MG36_accepted_run":39495457084,
      "original_TRUE_25physical_23adapted_plus_genuine_pole":True,
      "original_all_real_frequency_moment_enclosure_independent_of_MG36":True,
      "original_full_24D_rational_upper_matrices_compared":True,
      "actual_original_pole_and_arch_prime7_source_retained":True,
      "no_trace_to_Loewner_claim":True,
      "rational_rayleigh_or_congruence_required_for_inertia":True,
      "all_four_MG30_original_anchored_margins_replayed_exactly":True,
      "original_zero_remainder_best_case_is_only_a_necessary_gate":True,
      "original_470D_strong_inverse_proved":False,
      "original_signed_51over56_negative_cap_proved":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "complete_even_Weil_CC27_RH":"OPEN",
      "cases":cases,
      "next":"If MG30 full-frequency moments still dominate the direct frequency-residual upper, focus on improving original Gstar/Sstar coupled uncertainty and residual matrix instead of adding direct-band upper costs. If Hlo-band has an exact negative rational witness, the current band upper itself must also be improved; a perfect remainder alone could not help."}

def main():
    p=argparse.ArgumentParser()
    for k in ("mg24","mg29","mg30","mg36"):
        p.add_argument("--verified-"+k+"-json",required=True)
    p.add_argument("--output",default=
        "artifacts/mg38_original_remaining_frequency_feasibility.json")
    a=p.parse_args()
    load=lambda k:json.loads((ROOT/getattr(a,"verified_"+k+"_json")).read_text())
    out=analysis(*(load(k) for k in ("mg24","mg29","mg30","mg36")))
    dest=ROOT/a.output
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("MG38 original whole-frequency source feasibility:",json.dumps({
       "scenarios":[{
          "k":c["cutoff_k"],"B":c["original_MG30_source_trial"],
          "MG30_trace":float(Q(c["MG30_original_24D_full_residual_UPPER_trace"])),
          "MG36_trace":float(Q(c["MG36_original_24D_full_residual_UPPER_trace"])),
          "upper_comparison":c["MG36_minus_MG30_upper_full24_inertia_gate"],
          "band_only_ideal":c["necessary_Hlo_minus_band_alone_inertia_gate"]}
          for c in out["cases"]],
       "source_gap_and_signed470_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
