"""RC281: paid five-pivot cross-column covariance in the rank-371 reference.

Uses the immutable RC278/RC280 certificates; no uncomputed Schur principal
block is declared positive. All acceptance comparisons are exact Fractions.
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
    "certificates/rpb108_rc129_four_vector_joint_moment.json":
        "33e681e688450c987993603354544fe3919b435f",
    "certificates/rpb108_rc278_smaller_positive_reference.json":
        "edc59d6cec516d597c2c7816bec2a38a2677e18d",
    "certificates/rpb108_rc280_combined_jump_tail.json":
        "bb0dd3f6174761037ed0f20f17177ddad5749227",
    "notes/RPB108_RC280_COMBINED_JUMP_TAIL_20261014.md":
        "a0700fd140f4ec1e13dee9fe99bdd36e5e3c11f8",
}
BUDGETS = [
    dict(parity="even", pivots=[0, 4], remaining=140,
         first_remaining=2, lower_D=F(5), theta=F(3),
         center_trace_ceiling=F(1, 550),
         covariance_trace_ceiling=F(3, 200),
         cross_mass_ceiling=F(3)),
    dict(parity="odd", pivots=[1, 3, 5], remaining=226,
         first_remaining=7, lower_D=F(6), theta=F(13),
         center_trace_ceiling=F(1, 800),
         covariance_trace_ceiling=F(41, 200),
         cross_mass_ceiling=F(26)),
]


def transpose(A):
    return list(map(list, zip(*A)))


def matrix_inverse(A):
    n = len(A)
    assert n and all(len(row) == n for row in A)
    X = [list(row) + [F(i == j) for j in range(n)]
         for i, row in enumerate(A)]
    # SPD input: positive successive unpivoted Schur pivots.
    for k in range(n):
        p = X[k][k]
        assert p > 0, ("nonpositive pivot in inherited gate", k)
        X[k] = [v / p for v in X[k]]
        for i in range(n):
            if i != k:
                a = X[i][k]
                X[i] = [v - a * w for v, w in zip(X[i], X[k])]
    R = [row[n:] for row in X]
    for i in range(n):
        for j in range(n):
            assert sum(A[i][k] * R[k][j] for k in range(n)) == F(i == j)
    return R


def trace_product(A, B):
    assert len(A) == len(B)
    n = len(A)
    return sum((A[i][j] * B[j][i]
                for i in range(n) for j in range(n)), F(0))


def harmonic(n):
    return sum((F(1, k) for k in range(1, n + 1)), F(0))


def certificate(reverse=False):
    data = {}
    for path, sha in sorted(PINS.items(), reverse=reverse):
        raw = (ROOT / path).read_bytes()
        got = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()
        assert got == sha, ("inherited immutable blob mismatch", path)
        if path.endswith(".json"):
            data[path] = json.loads(raw)
    metric = data["certificates/rpb108_rc129_four_vector_joint_moment.json"]
    smaller = data["certificates/rpb108_rc278_smaller_positive_reference.json"]
    old = data["certificates/rpb108_rc280_combined_jump_tail.json"]
    sl = F(metric["actual_D_Gram_entry_lower"][0][0]) / (2 * B)
    assert sl > F(7, 2)
    assert smaller["new_reference_rank"] == old["reference_rank_unchanged"] == 371
    assert old["positive_auxiliary_block_dimension"] == 5
    assert old["remaining_exact_Schur_dimension"] == 366
    assert old["Stage_I_closed"] is False
    assert old["new_block_to_remaining_cross_columns_paid"] is False
    results = []
    for budget in BUDGETS:
        parity = budget["parity"]
        ref = next(x for x in smaller["smaller_reference_certificates"]
                   if x["parity"] == parity)
        item = next(x for x in old["combined_jump_tail_gate_certificates"]
                    if x["parity"] == parity)
        pivot = budget["pivots"]
        degrees = ref["retained_Legendre_degrees"]
        assert item["positive_block_degrees"] == pivot
        assert len(degrees) == ref["reference_rank"]
        assert len(degrees) - len(pivot) == budget["remaining"]
        remaining_degrees = [d for d in degrees if d not in pivot]
        assert remaining_degrees[0] == budget["first_remaining"]
        assert harmonic(remaining_degrees[0]) + sl > budget["lower_D"]
        assert max(degrees) <= 457 and max(pivot) <= 5
        lam = F(ref["augmentation_coefficient"])
        base = 0 if parity == "even" else 1
        indices = [(d - base) // 2 for d in pivot]
        raw_gamma = [[F(x) for x in row]
                     for row in item["actual_native_gate_Loewner_lower"]]
        raw_s = [[F(x) for x in row]
                 for row in item["complete_inverse_residual_covariance_upper"]]
        assert len(raw_gamma) == len(raw_s) == 3
        assert all(len(row) == 3 for row in raw_gamma + raw_s)
        assert raw_gamma == transpose(raw_gamma)
        assert raw_s == transpose(raw_s)
        gamma = [[raw_gamma[i][j] for j in indices] for i in indices]
        covariance = [[raw_s[i][j] for j in indices] for i in indices]
        gi = matrix_inverse(gamma)
        # The inherited residual upper bound is Loewner, not entrywise.
        # Its principal block must be positive semidefinite; it is SPD here.
        matrix_inverse(covariance)
        trials = {row["source"]: [F(v) for v in
                  row["exact_trial_Legendre_coefficients"]]
                  for row in item["combined_trial_tail_certificates"]}
        z = [trials["P" + str(d)] for d in pivot]
        assert all(len(v) == 65 for v in z)
        # Center cross map has exact physical mass-normalized coefficients
        # -lambda * mass_j * [z_{i,j}]. It vanishes beyond degree 64.
        GZ = [[sum((F(2) * B / (2 * d + 1) * u[d] * v[d]
                    for d in remaining_degrees if d < 65), F(0))
               for v in z] for u in z]
        tc = trace_product(gi, GZ)
        tr = trace_product(gi, covariance)
        assert F(0) <= tc < budget["center_trace_ceiling"]
        assert F(0) <= tr / budget["lower_D"] < budget["covariance_trace_ceiling"]
        theta = budget["theta"]
        weighted = lam ** 2 * (
            (1 + theta) * budget["center_trace_ceiling"] +
            (1 + 1 / theta) * budget["covariance_trace_ceiling"])
        assert weighted < budget["cross_mass_ceiling"]
        # For the actual Schur cross block C, and native remaining Mass:
        # C*Gamma_actual^-1 C <= weighted * Mass
        #   < cross_mass_ceiling * Mass.
        # No bound on the unevaluated principal Schur block is asserted.
        results.append({
            "parity": parity,
            "certified_positive_pivot_degrees": pivot,
            "remaining_auxiliary_coordinates": budget["remaining"],
            "first_remaining_degree": remaining_degrees[0],
            "retained_D_floor_used": str(budget["lower_D"]),
            "chosen_matrix_Young_parameter": str(theta),
            "weighted_trial_center_trace_strict_upper":
                str(budget["center_trace_ceiling"]),
            "weighted_residual_covariance_trace_over_D_strict_upper":
                str(budget["covariance_trace_ceiling"]),
            "entire_true_cross_Schur_payment_native_mass_strict_upper":
                str(budget["cross_mass_ceiling"]),
            "remaining_cross_column_centers_supported_through_degree": 64,
            "cross_covariance_preserves_full_selected_pivot_matrix": True,
        })
    return {
        "milestone": "RC281",
        "starting_commit": "e0a6cfe6e639a112111804a29fb9ac8e1aabe427",
        "input_git_blob_pins": PINS,
        "reference_rank_unchanged": 371,
        "certified_positive_block_dimension_unchanged": 5,
        "full_remaining_Schur_dimension_unchanged": 366,
        "cross_column_budget_certificates": results,
        "original_full_principal_remaining_response_evaluated": False,
        "full_Schur_positivity_certified": False,
        "Stage_I_closed": False, "RH": False, "F4": False, "Lean": False,
        "next_cursor": "RC282: improve correlated cross-column payments or bound "
                       "the full remaining principal Schur response; numerical "
                       "mass bound here is not positivity evidence.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--replay", action="store_true")
    args = parser.parse_args()
    outcome = certificate(reverse=args.replay)
    if args.replay:
        assert outcome == json.loads(args.output.read_text(encoding="utf-8"))
    else:
        args.output.write_text(json.dumps(outcome, sort_keys=True, indent=2)
                               + "\\n", encoding="utf-8")
    print("RC281 VALIDATED: full five-pivot cross columns paid in remaining "
          "Mass; remaining principal Schur gate OPEN", flush=True)
