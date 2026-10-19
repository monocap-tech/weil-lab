#!/usr/bin/env python3
"""SM59A: rigorous original 25-source SIGNED NEGATIVE INDEX <=23.

Actions-verified SM57 diagonal lower has inertia (0+,25-) and
SM58 full physical 25x25 coupled negative Fourier upper yields
SIGNED reference lower inertia (1+,24-). Neither is actual original
form inertia, and no negative lower pivot is an actual witness.

INDEPENDENT, STRONGER actual-index theorem: SM52's complete
original signed physical 2x2 Loewner LOWER on genuine supported
original SI10 functions g2=sin(2 pi c x),g17=x cos(2 pi c x)
is POSITIVE DEFINITE. Original 25-source SI10 physical Gram is
also rigorously SPD (original SM42 interval-preconditioned rational
Gershgorin). Hence these 2 sources are independent and belong to a
25D genuine physical span V. An actual negative definite subspace N
of Wodd|V is disjoint from the original positive plane P, since a
nonzero common vector cannot have Q>0 and Q<0. Thus
  dim(N)+dim(P)<=dim(V)=25,
so n_minus(Wodd|V)<=23, even though SM58's conservative LOWER
alone gives only n_minus(Wodd|V)<=24. No complementary spectral
classification is inferred; complete original odd infinite-dim
negative index may be larger.

This proof avoids attempting to replace the 2x2 block of a
25x25 LOWER with SM52's sharper block without rigorous control
of all cross terms; that would NOT preserve Loewner order.

An anchored Schur acceptance condition is recorded:
If original Q|V in a basis (P,Pperp_H) is [A B;B^T C], A>0,
then n_-(Q|V)=n_-(C-B^T A^-1 B).
The actual signed B,C and entire infinite orthogonal remainder
are NOT yet certified. This is the next operator-level gate.
"""
import json,argparse
from fractions import Fraction as F
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows)
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    original_full_25_physical_interval_gram,
    exact_verified_preconditioned_gram)

def main():
    arg=argparse.ArgumentParser()
    arg.add_argument("--output",default="artifacts/sm59a_original_25source_rank_aware_negative_index.json")
    a=arg.parse_args()
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in manifest["obligations"] if x["id"]=="W-ODD-NEG")
    assert manifest["active_obligation"]=="W-ODD-NEG"
    assert manifest["objective"]["status"]==odd["status"]=="open"
    assert manifest["governance"]["no_automatic_promotion"]
    assert all(z in odd["evidence"] for z in ("SM52","SM57","SM58","SM59"))
    pin=json.loads((ROOT/"certificates/rpb108_sm58_full25_signed_summary.json").read_text())
    assert pin["actions_run_id"]==39281588617
    assert pin["artifact_id"]==12201213066
    assert pin["whole_negative_original_leaves"]==973
    assert pin["original_supported_source_count"]==25
    assert pin["best_original_25x25_signed_LOWER_selected_mix"]=="0"
    assert pin["source_positive_lower_original_2x2_indices"]==[2,17]
    assert pin["original_25x25_signed_lower_inertia_for_each_diagonal_mix"]["0"]=={
        "positive":1,"negative":24,"zero":0}
    assert pin["original_25x25_signed_lower_inertia_for_each_diagonal_mix"]["1"]=={
        "positive":0,"negative":25,"zero":0}
    ref=[[F(x) for x in row] for row in pin["best_original_25x25_signed_LOWER_projected_2x2"]]
    assert ref[0][0]<0 and ref[0][1]==ref[1][0]
    assert ref[0][0]*ref[1][1]-ref[0][1]**2==F(
       pin["best_original_25x25_signed_LOWER_projected_2x2_det"])
    assert F(pin["negative_entire_upper_trace_coupled"]) < F(
       pin["negative_entire_upper_trace_SM57_diagonal"])
    sm52=json.loads((ROOT/"certificates/rpb108_sm52_original_coupled_source_matrix.json").read_text())
    assert sm52["source_indices"]==[2,17]
    assert sm52["original_head"]=="45780c198f066c8f5934721e16244136940152b2"
    assert "39205091881" in sm52["source"]
    a2=[[F(x) for x in row] for row in sm52["matrix"]]
    assert a2[0][1]==a2[1][0]
    determinant=a2[0][0]*a2[1][1]-a2[0][1]**2
    assert a2[0][0]>0 and determinant>0
    assert determinant==F(sm52["original_sylvester_determinant"])
    assert F(sm52["rounding_fee"])==F(7597,10**12)
    # Replay the entire 25 original supported physical Gram SPD
    # rather than silently assuming the basis has dimension 25.
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==25
    assert sources[2][0]=="cluster" and sources[17][0]=="cluster"
    assert sources[2][2]==0 and sources[17][2]==1
    assert centers[sources[2][1]]==centers[sources[17][1]]==F(1845,128)
    H,actual,pole=original_full_25_physical_interval_gram()
    assert actual==sources
    gram=exact_verified_preconditioned_gram(H)
    assert gram["certified_entire_original_25x25_physical_gram_SPD"]
    assert gram["original_source_dimension"]==25
    # This is a dimension/inertia argument, NOT Loewner gluing.
    positive_dimension=2
    ambient_dimension=gram["original_source_dimension"]
    actual_source_negative_index_upper=ambient_dimension-positive_dimension
    assert actual_source_negative_index_upper==23
    assert pin["original_25x25_signed_lower_inertia_for_each_diagonal_mix"]["0"]["negative"]==24
    assert actual_source_negative_index_upper < 24
    # SM52C additionally provides a normalized physical coercivity
    # constant on P: Q(h)>=69/200 ||h||². No information about B,C.
    ell=min(a2[i][i]-abs(a2[i][1-i]) for i in range(2))
    trace_H=2*F(11,10)+2*F(11,10)**3/3
    assert trace_H==F(4631,1500)
    assert ell>F(69,200)*trace_H
    out={
      "status":"CERTIFIED_SCOPED_ORIGINAL_25SOURCE_RANK_AWARE_NEGATIVE_INDEX_CEILING_23",
      "canonical_W_ODD_NEG":"OPEN",
      "original_physical_25source_gram_SPD_certified":True,
      "original_physical_25source_independent_dimension":25,
      "source_gram_exact_preconditioned_margin":gram["outward_preconditioned_gershgorin_lower"],
      "sm58_entire_negative_coupled_upper_accepted_Actions_id":39281588617,
      "sm57_entire_negative_diagonal_upper_accepted_Actions_id":39275848672,
      "sm58_complete_lower_reference_exact_inertia":{"positive":1,"negative":24,"zero":0},
      "sm52_original_positive_physical_source_indices":[2,17],
      "sm52_original_exact_sylvester_2x2_determinant":str(determinant),
      "sm52_2source_signed_positive_definite":True,
      "sm52_2source_physical_L2_coercivity":str(F(69,200)),
      "original_true_signed_25source_positive_subspace_dimension_AT_LEAST":2,
      "original_true_signed_25source_negative_index_upper_bound":23,
      "improvement_vs_only_SM58_lower_negative_index_ceiling":1,
      "sm58_lower_projected_2source_reference_diagonal":[str(ref[i][i]) for i in range(2)],
      "sm52_strict_positive_2source_lower_diagonal":[str(a2[i][i]) for i in range(2)],
      "sm58_lower_misses_strict_positive_2source_inequality":True,
      "source_25D_actual_negative_index_exact_classification":False,
      "actual_odd_infinite_dimensional_negative_index_bound":None,
      "actual_complete_source_eliminated_odd_O1O2":False,
      "original_470_Astar_inverse_strong_residual":False,
      "even_Weil_CC27_RH":False,
      "independent_original_source_Fourier_domain_premise_audit":"OPEN",
      "next_acceptance":"Certify actual signed 23D physically Gram-orthogonal Schur residual C-B^T A^-1 B with complete cross B and complement C (not lower-block splice); then certify infinite orthogonal remainder."
    }
    p=ROOT/a.output;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2)+"\n")
    print("SM59A actual original signed 25D source rank-aware index:",json.dumps({
       "SM58_reference_negative_inertia":24,
       "verified_independent_positive_plane":2,
       "actual_original_25D_negative_index_upper":23,
       "SM52_actual_physical_L2_positive_coercivity":"69/200",
       "full_original_odd_operator_negative_index":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
