#!/usr/bin/env python3
"""MG06 exact original 25D signed-LOWER Schur-method inertia no-go.

SM62's exact genuine original source25 signed Loewner LOWER L has
inertia (2 positive, 23 negative, 0 zero). The entire SM65 method
forms an ACTUAL source22 Schur LOWER by taking L_R and subtracting
a positive semidefinite mixed-coupling penalty D. Since R has
codimension three, n_-(L_R)>=n_-(L)-3=20. For every D>=0,
n_-(L_R-D)>=n_-(L_R)>=20.

This says nothing about the negative index of the true signed form:
the lower reference L_R-D is simply incapable of proving PSD.
A low-rank positive PATCH Delta_R must have rank>=n_-(L_R)
to render that same lower reference PSD. Tighter B bounds
without revising L_R cannot make a non-PSD lower PSD.
Independent physical/Fourier/domain verification remains OPEN.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows)
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    original_full_25_physical_interval_gram)
from validate_rpb108_sm57_original_25source_negative_upper import (
    original_positive_low_25,pole_outer_upper,outward_compact_matrix,
    exact_symmetric_25source_inertia)
from validate_rpb108_sm58_original_coupled_25negative import (
    original_complete_coupled_negative)
from validate_rpb108_sm62_full25_338signed_positive import (
    all_338_disjoint_original_signed_positive,
    selected_full25_source_extra,exact_inertia_general)

N=25
P=(1,2,17)
R=tuple(i for i in range(N) if i not in P)
SM62_HASH="87594b103a0575f1d5945e37cf16917c5184573acb6d305709b09d9eafb9971c"

def hash_matrix(A):
    serial=json.dumps([[str(z) for z in row] for row in A],
                      separators=(",",":"),ensure_ascii=True)
    return hashlib.sha256(serial.encode("utf-8")).hexdigest()
def sub(A,ix):
    return [[A[i][j] for j in ix] for i in ix]
def neg_inertia(A):
    p,n,z=exact_inertia_general(A)
    return {"positive":p,"negative":n,"zero":z}
def exact_algebra_regression():
    # In a toy 5D signed lower with 3 negative directions,
    # the 4D coordinate complement of a 1D anchor has >=2 negative.
    L=[[F(0) for j in range(5)] for i in range(5)]
    for i,v in enumerate((F(-4),F(-3),F(-2),F(1),F(2))):
        L[i][i]=v
    r=sub(L,(1,2,3,4))
    assert neg_inertia(L)["negative"]==3
    assert neg_inertia(r)["negative"]==2
    # Subtraction of PSD D cannot eliminate either negative direction.
    for v in (F(0),F(1,100),F(100)):
        minus=[[r[i][j]-(v if i==j else 0)
                for j in range(4)] for i in range(4)]
        assert neg_inertia(minus)["negative"]>=2
    # A positive patch on fewer than two directions cannot cure R.
    for gain in (F(5),F(50)):
        patch=[[r[i][j]+(gain if i==0 and j==0 else 0)
                for j in range(4)] for i in range(4)]
        assert neg_inertia(patch)["negative"]>=1
    return True

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",default="artifacts/mg06_sm65_original_22D_schur_inertia_no_go.json")
    opts=ap.parse_args()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open"
    assert m["governance"]["no_automatic_promotion"]
    assert exact_algebra_regression()
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==25 and sources[24][0]=="pole"
    gram,actual,_=original_full_25_physical_interval_gram()
    assert actual==sources
    neg,stats=original_complete_coupled_negative(centers,sources)
    assert stats["whole_original_negative_frequency_leaves"]==973
    pin=json.loads((ROOT/"certificates/rpb108_sm58_full25_signed_summary.json").read_text())
    assert pin["actions_run_id"]==39281588617
    assert hash_matrix(neg)==pin[
        "original_full25_coupled_negative_upper_all_625_entries_sha256"]
    pos,_=original_positive_low_25(centers,sources,gram)
    pole,_=pole_outer_upper(gram)
    exact=[[pos[i][j]-neg[i][j]-pole[i][j] for j in range(N)]
           for i in range(N)]
    L0,fee0=outward_compact_matrix(exact)
    assert hash_matrix(L0)==pin[
        "original_full25_signed_lower_all_625_entries_sha256"]
    windows,_=all_338_disjoint_original_signed_positive(centers,sources)
    assert len(windows)==338
    ck,_=selected_full25_source_extra(centers,sources,windows)
    X=ck[338]["matrix"]
    eps=ck[338]["total_extra_error_fee"]
    full=[[L0[i][j]+X[i][j]-(eps if i==j else F(0))
          for j in range(N)] for i in range(N)]
    L,fee=outward_compact_matrix(full)
    assert hash_matrix(L)==SM62_HASH
    all25=exact_symmetric_25source_inertia(L)
    assert (all25["positive"],all25["negative"],all25["zero"])==(2,23,0)
    assert len(P)==3 and len(R)==22 and len(set(P).intersection(R))==0
    complement=neg_inertia(sub(L,R))
    assert sum(complement.values())==22
    dimension_floor=max(0,all25["negative"]-len(P))
    assert dimension_floor==20
    assert complement["negative"]>=dimension_floor
    # Even a perfect exact calculation of B (D>=0) has D=0
    # as its MOST OPTIMISTIC result in this SM65 lower architecture.
    # Because L_R is indefinite, no B penalty tightening can
    # produce a positive semidefinite LOWER with this fixed L.
    assert complement["negative"]>0
    result={
        "status":"CERTIFIED_METHOD_ONLY_SM65_FULL22_COMPLEMENT_SCHUR_LOWER_NO_GO",
        "canonical_W_ODD_NEG":"OPEN",
        "SM58_original_all625_negative_and_signed_hashes_replayed":True,
        "SM62_original_all625_signed_lower_hash_replayed":True,
        "SM62_original_full25_lower_inertia":{
            k:all25[k] for k in ("positive","negative","zero")},
        "SM63_independent_true_signed_positive_anchor":list(P),
        "SM65_remaining_original_source_coordinates":list(R),
        "original_Schur_complement_dimension":len(R),
        "SM62_coordinate_complement_lower_inertia":complement,
        "forced_negative_lower_reference_dimension_from_codimension":
            dimension_floor,
        "actual_forced_negative_lower_reference_dimension":
            complement["negative"],
        "all_PSD_Schur_subtractions_preserve_at_least_forced_negative_lower_count":True,
        "even_zero_Schur_compensation_cannot_certify_PSD_with_SM62_lower":True,
        "minimal_rank_of_added_PSD_corrective_lower_gain_needed_to_reach_PSD":
            complement["negative"],
        "SM65_actual_negative_mode_identified":False,
        "SM65_actual_signed_Schur_PSD_certified":False,
        "original_actual_source25_negative_index_upper_from_SM63":22,
        "complete_original_470_source_Astar_inverse_and_infinite_remainder":"OPEN",
        "odd_even_Weil_CC27_RH":"OPEN",
        "independent_original_Fourier_closed_domain_premise_audit":"OPEN",
        "interpretation":"Original source25 SM62 signed LOWER has 23 negative reference directions. Any 22D coordinate restriction complementary to three source coordinates has >=20 negative reference directions by dimension. Any PSD Schur penalty only subtracts from this indefinite reference, so improved SM65 cross estimates alone cannot prove the actual signed Schur PSD. No inference of actual negative modes, RH, or whole odd positivity."
    }
    out=ROOT/opts.output
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n")
    print("MG06 ORIGINAL actual 22D Schur certificate method no-go:",json.dumps({
        "full25_LOWER_negative_inertia":all25["negative"],
        "forced_22D_LOWER_negative_inertia_floor":dimension_floor,
        "exact_22D_coordinate_LOWER_negative_inertia":complement["negative"],
        "minimal_positive_patch_rank":complement["negative"],
        "actual_odd_index22_ceiling":22,
        "whole_odd_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":
    main()
