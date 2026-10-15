"""RC297: exact P6 high original response and rank-317 augmented input column.

Reuses the pinned RC279 general prime/endpoint high-output projector,
the newly constructed RC296 P6 original action through degree 64,
and the certified RC283 physical Legendre projection reference.
Produces a fully paid original response through degree 2048 and one
exact supported projection-augmentation patch at output degree 6.
No arbitrary-input inverse action and no original Weil positivity claim.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import validate_rpb108_rc279_six_mode_gate as replay

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
SCALE=10**20
PINS={
 "certificates/rpb108_rc296_native_p6_action.json":"ff03088daa67d681e0371e92c40576d8c3219b4b",
 "certificates/rpb108_rc43_native_prime_head.json":"b4893953109e6fdc55d52b505c2bcfbf0d38281e",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc283_reduced_reference.json":"1dc4bba375af6bfd7a274fccc07638e0eead56e6",
 "scripts/validate_rpb108_rc279_six_mode_gate.py":"02ff6e1b70e79ede5691aa55bc98c877939cce23",
 "scripts/validate_rpb108_rc273_projection_original_tail.py":"4f6163f36097a97190ba50b5e032d942106122ef",
 "scripts/validate_rpb108_rc296_native_p6_action.py":"e0707fde1acc8cb12af9e54cf4aad6f15ed154df",
}

def down(x):return F(x.numerator*SCALE//x.denominator,SCALE)
def up(x):return -down(-x)
def root_up(x):
    assert x>=0
    if x==0:return F(0)
    from math import isqrt
    n=isqrt(x.numerator*SCALE*SCALE//x.denominator)
    return F(n+1,SCALE)

def run(reverse=False):
    data={}
    for path,sha in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        assert hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()==sha,(path,"inherited content changed")
        if path.endswith(".json"):data[path]=json.loads(raw)
    get=lambda s:data["certificates/rpb108_rc"+s+".json"]
    parent=get("296_native_p6_action")
    metric=get("129_four_vector_joint_moment")
    prime=get("43_native_prime_head")
    refs=get("283_reduced_reference")
    assert parent["milestone"]=="RC296"
    assert parent["certified_input_columns_after"]==[0,2,4,6]
    assert parent["new_original_Weil_action_performed"]
    assert not parent["new_P6_high_output_65_to_2048_reconstructed"]
    assert not parent["rank317_augmented_P6_action_certified"]
    assert not parent["Stage_I_closed"]
    assert refs["proposed_buffered_reference_rank"]==317
    ref=refs["reduced_reference_options"][0]
    choice=ref["reduced_reference_options"][1]
    assert ref["parity"]=="even" and choice["new_low_reference_rank"]==122
    assert choice["first_discarded_matching_degree"]==244
    assert F(choice["certified_D_reference_floor_lower"])>F(1,200)
    lam=F(ref["parameter_lambda"])
    sl=F(metric["actual_D_Gram_entry_lower"][0][0])/(2*B)
    sh=F(metric["actual_D_Gram_entry_upper"][0][0])/(2*B)
    assert 0<sl<=sh and lam>0
    H=[F(0)]
    for n in range(1,2051):H.append(H[-1]+F(1,n))
    old=parent["new_native_P6_original_action"]
    assert old["input"]=="P6" and old["input_degree"]==6
    assert len(old["finite_original_D_action"])==65
    assert all(c["degree"]==i for i,c in enumerate(old["finite_original_D_action"]))
    assert all(c["coefficient"]=="0" for c in old["finite_original_D_action"] if c["degree"]%2)
    assert len(prime["active_prime_powers"])==7
    # Actual new ORIGINAL prime and endpoint projection through 2048.
    prof=replay.secondary_action(6,old,prime,sl,sh,H,reverse)
    coeff=prof["finite_original_D_action"]
    assert prof["source"]=="P6" and prof["input_degree"]==6
    assert prof["retained_old_center_length"]==65
    assert len(coeff)==2049 and all(v["degree"]==n for n,v in enumerate(coeff))
    assert all(v["coefficient"]=="0" for v in coeff if v["degree"]%2)
    assert all(coeff[n]["coefficient"]==old["finite_original_D_action"][n]["coefficient"] for n in range(65))
    assert any(F(coeff[n]["coefficient"])!=0 for n in range(66,2049,2))
    assert F(prof["global_D_fault_norm_upper"])>0
    assert F(prof["model_D_energy_beyond_2048_upper"])>0
    assert prof["prime_projection_certificate"]["prime_projection_cutoff"]==2048
    assert prof["prime_projection_certificate"]["all_cross_prime_and_input_terms_preserved"]
    # Rank317 augmentation on physical input P6: P_low P6=P6.
    # D^-1 lambda P_low adds ONLY degree-6 coefficient lambda/(H6+s).
    lo=lam/(H[6]+sh)
    hi=lam/(H[6]+sl)
    assert 0<lo<=hi
    center=down((lo+hi)/2)
    radius=up(max(center-lo,hi-center))
    assert radius>0 and center-radius<=lo<=hi<=center+radius
    aug6=F(coeff[6]["coefficient"])+center
    addnorm=up(root_up(up(replay.orig.mass(6)*(H[6]+sh)*radius*radius)))
    newfault=up(F(prof["global_D_fault_norm_upper"])+addnorm)
    assert newfault>=F(prof["global_D_fault_norm_upper"])
    assert aug6!=F(coeff[6]["coefficient"])
    # Original omitted output is unchanged by a finite supported patch.
    return dict(
        milestone="RC297",
        starting_commit="b48fc40439ba8ecfbbfa9dad04a0f26578ee6553",
        input_git_blob_pins=PINS,
        original_input_degree=6,
        new_original_P6_full_high_output_action=prof,
        original_output_last_degree=2048,
        all_prime_and_endpoint_outputs_65_to_2048_certified=True,
        all_original_infinite_tails_preserved=True,
        reduced_reference_rank=317,
        even_reference_rank=122,
        reference_first_omitted_even_degree=244,
        rank317_augmented_action_adds_only_one_coordinate=True,
        augmented_action_single_coordinate_patch=dict(
            degree=6,
            exact_lambda=str(lam),
            exact_added_coefficient_lower=str(lo),
            exact_added_coefficient_upper=str(hi),
            outward_rational_center=str(center),
            outward_rational_radius=str(radius),
            augmented_degree6_original_plus_patch_center=str(aug6),
            augmented_projection_D_error_norm_upper=str(addnorm),
        ),
        complete_rank317_augmented_action_global_D_fault_norm_upper=str(newfault),
        complete_original_infinite_output_tail_D_energy_upper=prof["model_D_energy_beyond_2048_upper"],
        four_native_input_columns_now_with_complete_p6_high_output=True,
        full_four_column_signed_inverse_seed_optimized=False,
        arbitrary_input_operator_action_certified=False,
        new_original_Weil_action_performed=False,
        additional_input_action_high_output_reconstruction_performed=True,
        Stage_I_closed=False,RH=False,F4=False,Lean=False,
        next_cursor="RC298: construct and test true four-input-column signed Galerkin inverse seeds on P0,P2,P4,P6, with RC297 complete original actions, full errors, and RC295 finite-output dual constraints."
    )
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",required=True,type=Path)
    p.add_argument("--replay",action="store_true")
    args=p.parse_args()
    result=run(args.replay)
    print("RC297_CANDIDATE_JSON="+json.dumps(result,sort_keys=True),flush=True)
    if args.replay:assert result==json.loads(args.output.read_text())
    else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("RC297 VALIDATED: new P6 original output and rank317 augmentation; Stage I OPEN",flush=True)
