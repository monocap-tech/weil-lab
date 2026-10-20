#!/usr/bin/env python3
"""MG31: coordinate-independent, exact-rational signed 24D residual gate.

Take genuinely accepted MG30 original 24D anchored source trials and rebuild
A = H_lower - R_upper on the ORIGINAL 23 boundary + sinh pole source basis.
MG30's negative Gershgorin criterion does not determine inertia of A.

For a rational grid A0 with |A_ij-A0_ij|<=1/(2d), derive
   A0 - 12/d I <= A <= A0 + 12/d I (n=24).
A floating eigenbasis proposes an INVERTIBLE rational Q; exact Fraction
Gershgorin of Q^T(A0-12/d I)Q > 0 proves A positive definite. Alternatively
an exact rational v with v^T(A0+12/d I)v < 0 proves the *residual lower
certificate matrix A itself* has a negative direction. This NEVER proves
a negative direction of the actual operator, residual R*R, or zeta.

For the original four MG30 scenarios inspect the MG24 scalar baseline,
the accepted MG30 best signed-Gershgorin candidate, and the best tested
nonscalar trial; independently replay the exact MG30 anchored uncertainty.
The finite candidate family is NOT exhaustive and this cannot show 470D
source invariance/global inverse or signed odd 51/56.

Every final certificate uses exact Fraction proof inequalities, with
floating eigensolver allowed only to propose rational vectors/bases.
"""
import argparse,json,sys
from fractions import Fraction as Q
import numpy as np
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    deserialize,original_H24_from_physical_source,
)
from validate_rpb108_mg25_robust_source_aware_residual import (
    T,mm,sub,plus,mul,Id,gersh_lower,
)
from validate_rpb108_mg30_anchored_nonscalar_residual import (
    N,case_candidates,anchored_upper,
)
GRIDS=(10**18,10**24)
Q_DEN=2**20

def nearest(x,d):
    """Round only to construct a witnessed outward enclosing grid."""
    z=Q(x)*d
    return Q((2*z.numerator+z.denominator)//(2*z.denominator),d)

def rational_grid(A,d):
    assert len(A)==N and A==T(A)
    S=[[nearest(A[i][j],d) for j in range(N)] for i in range(N)]
    assert S==T(S)
    err=Q(1,2*d)
    # Exact entrywise checks on the original giant-rational values,
    # independent of the floating proposal.
    assert all(abs(A[i][j]-S[i][j])<=err
               for i in range(N) for j in range(N))
    # Symmetric entrywise bound has induced infinity/operator norm
    # <= N*err, so the scalar Loewner fee is valid.
    fee=N*err
    return S,fee

def dot(v,A):
    return sum((v[i]*sum((A[i][j]*v[j] for j in range(N)),Q(0))
                for i in range(N)),Q(0))

def eig_proposals(A):
    arr=np.array([[float(x) for x in row] for row in A],
                 dtype=float)
    if not np.isfinite(arr).all():return None
    arr=(arr+arr.T)/2
    try:
        values,vec=np.linalg.eigh(arr)
    except np.linalg.LinAlgError:
        return None
    if not np.isfinite(values).all() or not np.isfinite(vec).all():
        return None
    W=[[Q(int(np.rint(vec[i,j]*Q_DEN)),Q_DEN)
        for j in range(N)] for i in range(N)]
    v=[W[i][0] for i in range(N)]
    assert any(v)
    return float(values[0]),W,v

def exact_gersh_via_congruence(lower,W):
    """Rational matrix only; Q^T lower Q diagonally dominant is proof."""
    C=mm(mm(T(W),lower),W)
    assert C==T(C)
    return gersh_lower(C)

def assess(A,trial):
    assert A==T(A) and len(A)==N
    naive=gersh_lower(A)
    trials=[]
    for d in GRIDS:
        grid,fee=rational_grid(A,d)
        eig=eig_proposals(grid)
        if eig is None:
            trials.append({"precision_denominator":str(d),
                           "floating_eigenvector_proposal_available":False,
                           "classification":"INCONCLUSIVE"})
            continue
        lam,W,v=eig
        low=sub(grid,mul(fee,Id(N)))
        high=plus(grid,mul(fee,Id(N)))
        # Negative upper quadratic witness is conclusive even though
        # high is an upper Loewner bound and not the true matrix.
        negative_upper=dot(v,high)
        certificate={
           "precision_denominator":str(d),
           "float_smallest_eigenvalue_diagnostic_only":lam,
           "symmetric_grid_loewner_fee":str(fee),
           "negative_rayleigh_upper_bound":str(negative_upper),
           "negative_vector_has_24_original_coordinates":True,
           "floating_diagnostic_not_used_as_proof":True}
        if negative_upper<0:
            certificate.update({
              "classification":"CERTIFIED_NEGATIVE_DIRECTION_OF_RESIDUAL_BOUND_MATRIX",
              "negative_direction_vector":[str(x) for x in v],
              "negative_direction_exact_upper":str(negative_upper),
              "operator_negative_mode_proved":False})
            trials.append(certificate)
            break
        # If this succeeds, the positivity of Q^T low Q also
        # guarantees invertibility of Q, no numerical rank assumption.
        m=exact_gersh_via_congruence(low,W)
        certificate["rational_congruence_Gershgorin_lower"]=str(m)
        if m>0:
            certificate.update({
                "classification":"CERTIFIED_POSITIVE_RESIDUAL_BOUND_MATRIX",
                "rational_change_of_basis":[[str(x) for x in row] for row in W],
                "full_rank_basis_proved_by_positive_congruence":True,
                "source_squared_residual_gap_requires_metric_normalization":True})
            trials.append(certificate)
            break
        certificate["classification"]="INCONCLUSIVE"
        trials.append(certificate)
    end=trials[-1]
    return {
      "candidate_name":trial,
      "original_Gershgorin_margin":str(naive),
      "rational_matrix_congruence_outcome":end["classification"],
      "coordinate_dependent_Gershgorin_not_inertia":True,
      "strict_source_residual_contraction_certified":
         end["classification"]=="CERTIFIED_POSITIVE_RESIDUAL_BOUND_MATRIX",
      "original_true_operator_spectral_index_proved":False,
      "attempts":trials}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--verified-mg24-json",required=True)
    p.add_argument("--verified-mg29-json",required=True)
    p.add_argument("--verified-mg30-json",required=True)
    p.add_argument("--output",default=
        "artifacts/mg31_original_residual_rational_congruence.json")
    opt=p.parse_args()
    mg24=json.loads((ROOT/opt.verified_mg24_json).read_text())
    mg29=json.loads((ROOT/opt.verified_mg29_json).read_text())
    mg30=json.loads((ROOT/opt.verified_mg30_json).read_text())
    assert mg24["status"]=="ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES"
    assert mg29["status"]=="ORIGINAL_ADAPTED_THIRD_FOURIER_SOURCE_MOMENT_REFINEMENT"
    assert mg30["status"]=="ORIGINAL_24D_ANCHORED_NONSCALE_MIXED_RESIDUAL_GATE"
    assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in (mg24,mg29,mg30))
    assert mg30["verified_original_MG24_run_id"]==39378465438
    assert mg30["verified_original_MG29_run_id"]==39440914565
    assert mg30["exact_Fraction_matrix_acceptance"]
    assert not mg30["actual_full_original_470D_strong_residual_certified"]
    assert [(x["mesh_cells"],x["cutoff_k"]) for x in mg30["scenarios"]]==[
           (16,12),(16,16),(32,12),(32,16)]
    Hmid,hrad,Herr=original_H24_from_physical_source()
    assert Herr==Q(mg24["physical_Gram_Loewner_row_error"])
    assert [str(Hmid[i][23]) for i in range(N)]==mg24["original_pole_b_center"]
    Hlo=sub(Hmid,mul(Herr,Id(N)))
    Hup=plus(Hmid,mul(Herr,Id(N)))
    report=[]
    for mesh in mg29["meshes"]:
        for case in mesh["full_original_frequency_scenarios"]:
            k=case["cutoff_k"]
            old=next((x for x in mg30["scenarios"]
                      if x["mesh_cells"]==mesh["mesh_cells"]
                       and x["cutoff_k"]==k),None)
            assert old is not None
            LG=deserialize(case["full_original_Gstar_lower"])
            UG=deserialize(case["full_original_Gstar_upper"])
            US=deserialize(case["full_original_Sstar_upper"])
            Gc=mul(Q(1,2),plus(LG,UG))
            baseline=next(x for x in mg24["cases"] if x["cutoff_k"]==k)
            anchor=Q(baseline["scalar_trial_t"])
            candidates={name:(t,B) for name,t,B
                        in case_candidates(Gc,US,anchor)}
            # Exhaust the ENTIRE accepted MG30 finite candidate family,
            # not just scalar/best/best-nonscalar summaries. A proof of
            # negative A for each does not extend to untested matrices B.
            selected=[trial["name"] for trial in old["trials"]]
            assert len(selected)==old["candidate_count"]==9
            assert len(selected)==len(set(selected))
            tests=[]
            for name in selected:
                assert name in candidates,("MG30 candidate drift",name)
                t,B=candidates[name]
                exact=anchored_upper(Hlo,Hup,LG,UG,US,t,B)
                historical=next(x for x in old["trials"] if x["name"]==name)
                assert str(exact["margin"])==historical["gershgorin_margin"]
                assert str(exact["gap"])==historical[
                    "certified_source_residual_squared_gap"]
                assert not exact["positive"],"MG30 reported no strict original contraction"
                A=sub(Hlo,exact["Rupper"]) if "Rupper" in exact else None
                # MG30 has so far returned only margin, not the complete
                # rational upper. Build the EXACT same 24D formula here.
                E=mul(Q(1,2),sub(UG,LG))
                D=sub(B,mul(t,Id(N)))
                cross=plus(mm(Gc,D),mm(T(D),Gc))
                action=mm(mm(T(B),US),B)
                from validate_rpb108_mg25_robust_source_aware_residual import shift
                from validate_rpb108_mg25_robust_source_aware_residual import norm_upper
                Rupper=shift(plus(sub(sub(Hup,mul(2*t,LG)),cross),
                                    action),
                             2*norm_upper(E)*norm_upper(D))
                A=sub(Hlo,Rupper)
                assert gersh_lower(A)==exact["margin"]
                diagnostic=assess(A,name)
                diagnostic["MG30_anchor_t"]=str(t)
                diagnostic["verified_MG30_margin_replayed"]=True
                tests.append(diagnostic)
            report.append({
                "mesh_cells":mesh["mesh_cells"],"cutoff_k":k,
                "actual_original_24D_complete_frequency":True,
                "original_SI10_23_boundary_plus_sinh_pole":True,
                "MG30_accepted_trial_exact_replayed":True,
                "tested_candidate_count":len(tests),
                "tests":tests})
    assert [(x["mesh_cells"],x["cutoff_k"]) for x in report]==[
        (16,12),(16,16),(32,12),(32,16)]
    assert sum(x["tested_candidate_count"] for x in report)==36
    certpos=sum(t["strict_source_residual_contraction_certified"]
                for x in report for t in x["tests"])
    neg=sum(t["rational_matrix_congruence_outcome"]==
              "CERTIFIED_NEGATIVE_DIRECTION_OF_RESIDUAL_BOUND_MATRIX"
            for x in report for t in x["tests"])
    incon=sum(t["rational_matrix_congruence_outcome"]=="INCONCLUSIVE"
             for x in report for t in x["tests"])
    out={
      "status":"ORIGINAL_24D_RATIONAL_CONGRUENCE_AND_NEGATIVE_WITNESS_AUDIT",
      "canonical_W_ODD_NEG":"OPEN",
      "mg24_original_accepted_run":39378465438,
      "mg29_original_accepted_run":39440914565,
      "mg30_original_accepted_run":39442984941,
      "actual_24D_original_residual_matrix_reconstructed":True,
      "signed_original_complete_frequency_Gstar_Sstar_inherited":True,
      "full_original_physical_Gram_and_pole_inherited":True,
      "rational_grid_error_charged_by_exact_Loewner_diagonal":True,
      "rational_congruence_positive_only_if_exact_Gersh_positive":True,
      "negative_direction_only_if_exact_rational_Rayleigh_upper_negative":True,
      "floating_eigenvectors_merely_rationalized_proposals":True,
      "number_certified_positive_residual_bounds":certpos,
      "number_certified_negative_directions_of_bound_matrix":neg,
      "number_unresolved_coordinate_tests":incon,
      "tested_original_scenarios":report,
      "actual_original_470D_resolvent_certified":False,
      "signed_original_negative_51over56_cap_certified":False,
      "complete_original_operator_spectral_inertia_certified":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "even_Weil_CC27_RH":"OPEN",
      "next":"If certified positive, verify source-metric gap and 470D extension separately. If negative rational witness, no congruence can save THIS bound matrix; improve source Loewner information or trial. If inconclusive, try stronger interval LDL without spectral promotion."}
    dst=ROOT/opt.output
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(out,indent=2)+"\n")
    print("MG31 original rational congruence:",json.dumps({
      "positive_bound_matrices":certpos,
      "negative_bound_witnesses":neg,
      "inconclusive":incon,
      "tests":[{"cells":x["mesh_cells"],"k":x["cutoff_k"],
                "results":[(t["candidate_name"],
                            t["rational_matrix_congruence_outcome"])
                            for t in x["tests"]]} for x in report],
      "full470_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
