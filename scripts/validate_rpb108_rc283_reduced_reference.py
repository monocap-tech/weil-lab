"""RC283: certify reduced positive references and exact high/low Schur identity.

The inherited exact-rational RC278 and RC282 certificates establish
the original-form global bounds. No newly computed original action or
rank-317 inverse-response positivity is claimed.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PINS = {
    "certificates/rpb108_rc129_four_vector_joint_moment.json": "33e681e688450c987993603354544fe3919b435f",
    "certificates/rpb108_rc278_smaller_positive_reference.json": "edc59d6cec516d597c2c7816bec2a38a2677e18d",
    "certificates/rpb108_rc282_high_mode_auxiliary_complement.json": "e07256b79b9e5c4062f5d44eff552f800af6b8f7",
    "notes/RPB108_RC282_HIGH_MODE_AUXILIARY_COMPLEMENT_20261014.md": "b22d562cb4d2d435628c246426a320f5fd76381d",
}
THRESHOLDS = (F(0), F(1, 200), F(1, 100))


def inverse2(a):
    x, y = a[0]
    z, w = a[1]
    det = x * w - y * z
    assert y == z and x > 0 and det > 0
    return [[w / det, -y / det], [-z / det, x / det]]


def exact_controls():
    # Old low and high positive pivots do not imply positive reduced gate.
    lam, a, b, d = F(3), F(1, 5), F(2, 5), F(1, 10)
    old = inverse2([[a + lam, b], [b, d + lam]])
    new = inverse2([[a + lam, b], [b, d]])
    kll = 1 - lam * old[0][0]
    khh = 1 - lam * old[1][1]
    klh = -lam * old[0][1]
    reduced = 1 - lam * new[0][0]
    assert kll == F(23, 488) and khh == F(1, 61)
    assert reduced == F(-7, 8) == kll - klh * klh / khh
    assert a * d - b * b < 0
    return {"exact_Schur_identity_checked": True,
            "old_positive_pivots_do_not_transfer": True}


def run(reverse=False):
    data = {}
    for path, expected in sorted(PINS.items(), reverse=reverse):
        raw = (ROOT / path).read_bytes()
        actual = hashlib.sha1(
            b"blob " + str(len(raw)).encode() + bytes([0]) + raw
        ).hexdigest()
        assert actual == expected, ("source blob changed", path)
        if path.endswith(".json"):
            data[path] = json.loads(raw)
    metric = data["certificates/rpb108_rc129_four_vector_joint_moment.json"]
    old = data["certificates/rpb108_rc278_smaller_positive_reference.json"]
    prev = data["certificates/rpb108_rc282_high_mode_auxiliary_complement.json"]
    s_lower = F(metric["actual_D_Gram_entry_lower"][0][0]) / F(11, 5)
    s_upper = F(metric["actual_D_Gram_entry_upper"][0][0]) / F(11, 5)
    assert 0 < s_lower <= s_upper
    assert old["new_reference_rank"] == prev["reference_rank_unchanged"] == 371
    assert not old["Stage_I_closed"] and not prev["Stage_I_closed"]
    harmonic = [F(0)]
    for n in range(1, 460):
        harmonic.append(harmonic[-1] + F(1, n))
    entries = []
    for base, (ref, record) in enumerate(zip(
        old["smaller_reference_certificates"],
        prev["threshold_adapted_auxiliary_complement_certificates"],
    )):
        parity = ("even", "odd")[base]
        assert ref["parity"] == record["parity"] == parity
        degrees = ref["retained_Legendre_degrees"]
        assert degrees == list(range(base, (284, 459)[base], 2))
        lam = F(ref["augmentation_coefficient"])
        assert lam == F(ref["physical_negative_allowance_C"])
        assert F(ref["full_D_reference_upper"]) > 1
        choices = []
        for threshold in THRESHOLDS:
            row = next(x for x in record["threshold_rows"]
                       if F(x["requested_native_mass_floor"]) == threshold)
            first = row["first_protected_Legendre_degree"]
            low = [n for n in degrees if n < first]
            high = [n for n in degrees if n >= first]
            mu = 1 - lam / (harmonic[first] + s_lower)
            floor = F(row["certified_native_mass_floor_lower"])
            assert first % 2 == base and threshold < floor <= mu
            assert 1 - lam / (harmonic[first - 2] + s_lower) <= threshold
            assert len(low) == row["unresolved_low_coordinates"]
            assert len(high) == row["protected_positive_coordinates"]
            choices.append({
                "protected_high_mass_floor_target": str(threshold),
                "first_discarded_matching_degree": first,
                "discarded_high_rank": len(high),
                "new_low_reference_rank": len(low),
                "certified_D_reference_floor_lower": str(floor),
            })
        entries.append({
            "parity": parity,
            "old_reference_rank": len(degrees),
            "upper_D_reference_bound_reused": ref["full_D_reference_upper"],
            "parameter_lambda": ref["augmentation_coefficient"],
            "reduced_reference_options": choices,
        })
    assert [sum(x["reduced_reference_options"][k]["new_low_reference_rank"]
                for x in entries) for k in range(3)] == [301, 317, 334]
    return {
        "milestone": "RC283",
        "parent": "92e0d7876a38a85deee5fa4282118ef9dd059563",
        "input_git_blob_pins": PINS,
        "old_reference_rank": 371,
        "reduced_reference_options": entries,
        "controls": exact_controls(),
        "proposed_buffered_reference_rank": 317,
        "minimal_positive_reference_rank": 301,
        "exact_schur_elimination_identity": True,
        "old_five_pivot_margins_not_transferred": True,
        "full_new_auxiliary_response_evaluated": False,
        "Stage_I_closed": False, "RH": False, "F4": False, "Lean": False,
        "next_cursor": "RC284: compute fresh paid inverse responses for rank-317 reference",
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--output", required=True, type=Path)
    p.add_argument("--replay", action="store_true")
    args = p.parse_args()
    result = run(args.replay)
    if args.replay:
        assert result == json.loads(args.output.read_text())
    else:
        args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("RC283 VALIDATED: reduced positive references; Stage I OPEN", flush=True)
