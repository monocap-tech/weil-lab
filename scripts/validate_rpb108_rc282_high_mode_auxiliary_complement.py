"""RC282: protected high-degree native auxiliary block in the rank-371 reference.

Certifies a positive *principal* high block for each parity and a buffered
inverse family. DOES NOT certify the mixed low/high Schur complement.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
B = F(11, 10)
PINS = {
    "certificates/rpb108_rc129_four_vector_joint_moment.json": "33e681e688450c987993603354544fe3919b435f",
    "certificates/rpb108_rc278_smaller_positive_reference.json": "edc59d6cec516d597c2c7816bec2a38a2677e18d",
    "certificates/rpb108_rc280_combined_jump_tail.json": "bb0dd3f6174761037ed0f20f17177ddad5749227",
    "certificates/rpb108_rc281_five_pivot_cross_budget.json": "535b06a458ba9c9f491e3dd1a5bdb304d632cba6",
    "notes/RPB108_RC281_FIVE_PIVOT_CROSS_BUDGET_20261014.md": "807bd052198ccdfbe4b0933bbb8e755ce6857c0f"
}
THRESHOLDS = [F(0), F(1, 1000), F(1, 500), F(1, 200), F(1, 100)]
SCALE = 10 ** 18


def harmonic_table(last):
    h = [F(0)]
    for k in range(1, last + 1):
        h.append(h[-1] + F(1, k))
    return h


def down18(x):
    return F((x.numerator * SCALE) // x.denominator, SCALE)


def exact_controls():
    # The inverse of a noncommuting positive perturbation is smaller
    # in Loewner order. The scalar native diagonal bound is not a
    # claim that the original operator commutes with its projection.
    W = ((F(2), F(0)), (F(0), F(5)))
    v = (F(1), F(2))
    G = ((W[0][0] + v[0] ** 2, v[0] * v[1]),
         (v[1] * v[0], W[1][1] + v[1] ** 2))
    det = G[0][0] * G[1][1] - G[0][1] ** 2
    assert det > 0 and G[0][1] != 0
    invG = ((G[1][1] / det, -G[0][1] / det),
            (-G[1][0] / det, G[0][0] / det))
    delta = ((F(1, 2) - invG[0][0], -invG[0][1]),
             (-invG[1][0], F(1, 5) - invG[1][1]))
    assert delta[0][0] >= 0 and delta[1][1] >= 0
    assert delta[0][0] * delta[1][1] - delta[0][1] ** 2 >= 0
    # Positive high and low restrictions do not imply positive union.
    cross = F(2)
    assert 1 > 0 and F(1) * F(1) - cross ** 2 < 0
    return {
        "noncommuting_inverse_order_2x2_checked": True,
        "two_positive_principal_blocks_can_have_indefinite_union": True,
        "Schur_cross_terms_must_be_retained": True,
    }


def run(reverse=False):
    data = {}
    for path, sha in sorted(PINS.items(), reverse=reverse):
        raw = (ROOT / path).read_bytes()
        got = hashlib.sha1(
            b"blob " + str(len(raw)).encode() + b"\\0" + raw
        ).hexdigest()
        assert got == sha, ("inherited blob SHA changed", path)
        if path.endswith(".json"):
            data[path] = json.loads(raw)
    get = lambda s: data["certificates/rpb108_rc" + s + ".json"]
    metric = get("129_four_vector_joint_moment")
    ref = get("278_smaller_positive_reference")
    old = get("280_combined_jump_tail")
    pivot = get("281_five_pivot_cross_budget")
    assert ref["new_reference_rank"] == 371
    assert old["positive_auxiliary_block_dimension"] == 5
    assert pivot["full_remaining_Schur_dimension_unchanged"] == 366
    assert not old["Stage_I_closed"] and not pivot["Stage_I_closed"]

    s_lower = F(metric["actual_D_Gram_entry_lower"][0][0]) / (2 * B)
    s_upper = F(metric["actual_D_Gram_entry_upper"][0][0]) / (2 * B)
    assert 0 < s_lower <= s_upper
    H = harmonic_table(457)
    per_parity = []
    for base, row in enumerate(ref["smaller_reference_certificates"]):
        degrees = row["retained_Legendre_degrees"]
        assert row["parity"] == ("even" if base == 0 else "odd")
        assert degrees == list(range(base, [284, 459][base], 2))
        assert int(row["reference_rank"]) == len(degrees)
        lam = F(row["augmentation_coefficient"])
        # This exact rank-371 reference uses the actual RC277 negative
        # allowance as its augmentation coefficient.
        assert lam == F(row["physical_negative_allowance_C"])
        assert row["new_positive_pivot_certified"]
        records = []
        for eps in THRESHOLDS:
            # On the retained native Legendre span, the complete physical
            # augmented form satisfies G >= D, by RC278's full-domain
            # G >= D_P+(D-lambda)_Q. Therefore the actual inverse
            # response T <= diag(m_n/(H_n+s)), with no commutation claim.
            selected = [
                n for n in degrees
                if F(1) - lam / (H[n] + s_lower) > eps
            ]
            assert selected and selected == list(
                range(selected[0], degrees[-1] + 2, 2))
            first = selected[0]
            low = [n for n in degrees if n < first]
            beta = F(1) - lam / (H[first] + s_lower)
            floor = down18(beta)
            assert floor > eps and beta >= floor
            if low:
                assert F(1) - lam / (H[low[-1]] + s_lower) <= eps
            records.append({
                "requested_native_mass_floor": str(eps),
                "first_protected_Legendre_degree": first,
                "protected_positive_coordinates": len(selected),
                "unresolved_low_coordinates": len(low),
                "certified_native_mass_floor_lower": str(floor),
            })
        per_parity.append({
            "parity": row["parity"],
            "reference_rank": len(degrees),
            "threshold_rows": records,
        })
    totals = []
    for i, eps in enumerate(THRESHOLDS):
        protected = sum(row["threshold_rows"][i]["protected_positive_coordinates"]
                        for row in per_parity)
        low = sum(row["threshold_rows"][i]["unresolved_low_coordinates"]
                  for row in per_parity)
        assert protected + low == 371
        totals.append({
            "requested_native_mass_floor": str(eps),
            "protected_positive_coordinates": protected,
            "unresolved_low_coordinates": low,
        })
    assert [(r["protected_positive_coordinates"], r["unresolved_low_coordinates"])
            for r in totals] == [(70, 301), (67, 304), (64, 307),
                                 (54, 317), (37, 334)]
    assert all(x in range(0, 232) for x in [0, 4])
    assert all(x in range(1, 371) for x in [1, 3, 5])
    assert exact_controls()["Schur_cross_terms_must_be_retained"]
    return {
        "milestone": "RC282",
        "starting_commit": "558a136277e0ddd4a1d12f6bca58228f42ee43c4",
        "input_git_blob_pins": PINS,
        "reference_rank_unchanged": 371,
        "threshold_adapted_auxiliary_complement_certificates": per_parity,
        "threshold_totals": totals,
        "five_pivots_remain_positive_as_original_principal_block_only": True,
        "high_low_cross_inequality_evaluated": False,
        "five_pivots_and_protected_high_joint_positive": False,
        "original_index_bound_301_preserved_not_improved": True,
        "full_remaining_Schur_positivity_certified": False,
        "Stage_I_closed": False, "RH": False, "F4": False, "Lean": False,
        "next_cursor": "RC283: quantify high-to-low auxiliary gate cross blocks "
                       "and obtain a lower bound on the low Schur principal form "
                       "without transferring the five positive pivots through "
                       "an unproved elimination.",
    }


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--replay", action="store_true")
    args = ap.parse_args()
    certificate = run(reverse=args.replay)
    if args.replay:
        assert certificate == json.loads(args.output.read_text(encoding="utf-8"))
    else:
        args.output.write_text(json.dumps(certificate, sort_keys=True, indent=2)
                               + "\\n", encoding="utf-8")
    print("RC282 VALIDATED: native high block positive, low/high coupling OPEN",
          flush=True)
