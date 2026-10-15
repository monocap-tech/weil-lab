"""RC300: extend certified RC299 original P8 action through output 2048.

Reuses the exact RC279 prime/endpoint projection engine on a *new*
degree-eight native input and attaches the rank-317 augmentation
only at physical degree eight. Full high-output D tail remains paid.
This is one certified input action column, not an arbitrary-vector
native operator evaluator, inverse-response proof, or Stage I closure.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import validate_rpb108_rc279_six_mode_gate as high

ROOT = Path(__file__).resolve().parents[1]
B = F(11, 10)
up = high.up
down = high.down
root = high.root
orig = high.orig

PINS = {
    "certificates/rpb108_rc129_four_vector_joint_moment.json":
        "33e681e688450c987993603354544fe3919b435f",
    "certificates/rpb108_rc43_native_prime_head.json":
        "b4893953109e6fdc55d52b505c2bcfbf0d38281e",
    "certificates/rpb108_rc283_reduced_reference.json":
        "1dc4bba375af6bfd7a274fccc07638e0eead56e6",
    "certificates/rpb108_rc296_native_p6_action.json":
        "ff03088daa67d681e0371e92c40576d8c3219b4b",
    "certificates/rpb108_rc297_native_p6_high_projection.json":
        "228a2cd9cb8f92324cce7f686f2539b8ddf8f412",
    "certificates/rpb108_rc299_native_p8_action.json":
        "755dab2b4ab9e62b3f6a26be139ed29942647021",
    "scripts/validate_rpb108_rc279_six_mode_gate.py":
        "02ff6e1b70e79ede5691aa55bc98c877939cce23",
    "scripts/validate_rpb108_rc273_projection_original_tail.py":
        "4f6163f36097a97190ba50b5e032d942106122ef",
    "scripts/validate_rpb108_rc299_native_p8_action.py":
        "886c517603d56c67107b46382b3d6b31b5be68eb",
}


def run(reverse=False):
    data = {}
    for path, sha in sorted(PINS.items(), reverse=reverse):
        raw = (ROOT/path).read_bytes()
        digest = hashlib.sha1(
            b"blob " + str(len(raw)).encode() + b"\0" + raw
        ).hexdigest()
        assert digest == sha, (path, "pinned input changed")
        if path.endswith(".json"):
            data[path] = json.loads(raw)

    def get(i):
        return data["certificates/rpb108_rc"+i+".json"]

    p8pre = get("299_native_p8_action")
    p6pre = get("297_native_p6_high_projection")
    p8 = p8pre["new_native_P8_original_action"]
    assert p8pre["P4_full_low_original_action_regression_exact"]
    assert p8pre["P6_full_low_original_action_regression_exact"]
    assert p8pre["P8_output_degrees_65_through_2048_available"] is False
    assert p8pre["rank317_augmented_P8_action_available"] is False
    assert p6pre["four_native_input_columns_now_with_complete_p6_high_output"]
    assert p8["input"] == "P8" and p8["input_degree"] == 8
    assert len(p8["finite_original_D_action"]) == 65
    assert p8["all_omitted_outputs_paid"]

    mom = get("129_four_vector_joint_moment")
    ref = get("283_reduced_reference")
    assert ref["proposed_buffered_reference_rank"] == 317
    preferred = ref["reduced_reference_options"][0]
    selection = preferred["reduced_reference_options"][1]
    assert selection["new_low_reference_rank"] == 122
    assert selection["first_discarded_matching_degree"] == 244
    lam = F(preferred["parameter_lambda"])
    sl = F(mom["actual_D_Gram_entry_lower"][0][0])/(2*B)
    sh = F(mom["actual_D_Gram_entry_upper"][0][0])/(2*B)
    assert 0 < sl <= sh and lam > 0
    prime = get("43_native_prime_head")
    assert len(prime["active_prime_powers"]) == 7

    H = [F(0)]
    for n in range(1, 2051):
        H.append(H[-1]+F(1, n))
    action = high.secondary_action(
        8, p8, prime, sl, sh, H, reverse)
    modes = action["finite_original_D_action"]
    assert action["source"] == "P8"
    assert action["input_degree"] == 8
    assert action["retained_old_center_length"] == 65
    assert len(modes) == 2049
    assert [r["degree"] for r in modes] == list(range(2049))
    for n in range(65):
        assert modes[n]["coefficient"] == (
            p8["finite_original_D_action"][n]["coefficient"])
    assert all(r["coefficient"] == "0" for r in modes if r["degree"]%2)
    assert any(F(modes[n]["coefficient"]) != 0
               for n in range(66, 2049, 2))
    assert action["prime_projection_certificate"][
        "prime_projection_cutoff"] == 2048
    assert action["prime_projection_certificate"][
        "all_cross_prime_and_input_terms_preserved"]
    assert F(action["global_D_fault_norm_upper"]) > 0
    assert F(action["model_D_energy_beyond_2048_upper"]) > 0

    # Rank-317 even reference includes P8. P_low P8=P8, hence:
    # N_new P8 = N_original P8 + lambda/(H8+s) P8.
    # The coefficient patch is supported only at n=8; it does not
    # alter the original operator's infinite high-output tail.
    lo = lam/(H[8]+sh)
    hi = lam/(H[8]+sl)
    center = down((lo+hi)/2)
    radius = up(max(center-lo, hi-center))
    assert radius > 0 and center-radius <= lo <= hi <= center+radius
    added = up(root(up(orig.mass(8)*(H[8]+sh)*radius*radius)))
    fault = up(F(action["global_D_fault_norm_upper"])+added)
    assert fault >= F(action["global_D_fault_norm_upper"])
    assert F(modes[8]["coefficient"])+center != F(modes[8]["coefficient"])

    return dict(
        milestone="RC300",
        starting_commit="83b6bab10b6a342102c33b461cabda3c10288c9c",
        input_git_blob_pins=PINS,
        original_input_degree=8,
        complete_native_P8_original_high_output_action=action,
        original_output_last_degree=2048,
        all_output_degrees_65_to_2048_materialized=True,
        low_65_coefficients_reproduce_RC299=True,
        complete_original_infinite_D_tail_paid=True,
        preferred_augmented_reference_rank=317,
        even_reference_rank=122,
        first_omitted_even_reference_degree=244,
        rank317_physical_augmented_P8_patch=dict(
            degree=8,
            exact_lambda=str(lam),
            added_coefficient_lower=str(lo),
            added_coefficient_upper=str(hi),
            rational_center=str(center),
            rational_radius=str(radius),
            complete_augmented_degree8_center=str(
                F(modes[8]["coefficient"])+center),
            additional_D_fault_norm_upper=str(added)),
        complete_rank317_augmented_P8_D_fault_norm_upper=str(fault),
        complete_P8_original_infinite_output_tail_D_energy_upper=action[
            "model_D_energy_beyond_2048_upper"],
        five_native_even_input_action_columns_available=[
            0, 2, 4, 6, 8],
        five_column_RC292_signed_inverse_test_executed=False,
        arbitrary_input_operator_action_executed=False,
        five_column_Galerkin_inverse_optimized=False,
        five_column_dual_obstruction_certified=False,
        original_Weil_form_positivity_certified=False,
        Stage_I_closed=False, RH=False, F4=False, Lean=False,
        next_cursor=(
            "RC301: test all five native original action input columns "
            "against unchanged RC292 strict signed residual budgets; "
            "compute exact six-output dual annihilators and pay all "
            "remaining source and original action uncertainties."))
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--replay", action="store_true")
    args = parser.parse_args()
    result = run(args.replay)
    if args.replay:
        assert result == json.loads(
            args.output.read_text(encoding="utf-8"))
    else:
        args.output.write_text(json.dumps(
            result, sort_keys=True, indent=2)+"\n",
            encoding="utf-8")
    print("RC300 VALIDATED: complete native P8 action and rank317 "
          "physical patch; Stage I OPEN", flush=True)
