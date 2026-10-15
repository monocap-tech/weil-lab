"""RC298: paid finite-output dual exclusion for all native P0/P2/P4/P6 inverse seeds.

A rational five-row functional nearly annihilates the four nominal
original-action columns. Its exact nonzero annihilation defect, every
column's global D-error, physical projection s-interval variation,
and source RHS variation are all charged. Infinite tails pair to
zero exactly with the finitely supported functional, NOT by assuming
the tails vanish in D. This excludes only this finite input span
under RC292's strict sufficient residual tolerances.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
B = F(11, 10)
SCALE = 10**15
DEGREES = (0, 2, 4, 6)
PINS = {
    "certificates/rpb108_rc129_four_vector_joint_moment.json":
        "33e681e688450c987993603354544fe3919b435f",
    "certificates/rpb108_rc279_six_mode_gate.json":
        "bd729c0f5a41debac61a0f3c37276bb94e7834e5",
    "certificates/rpb108_rc283_reduced_reference.json":
        "1dc4bba375af6bfd7a274fccc07638e0eead56e6",
    "certificates/rpb108_rc290_soft_source_decomposition.json":
        "c0d90be6ea686141f088f70eb4cf3821354671be",
    "certificates/rpb108_rc292_signed_inverse_action_contract.json":
        "a4e19528ab5b12d9651a29dbeb478d7844e05470",
    "certificates/rpb108_rc295_three_column_dual_obstruction.json":
        "41994217d0d59553180cd82f60993f8f3a3e07d0",
    "certificates/rpb108_rc297_native_p6_high_projection.json":
        "228a2cd9cb8f92324cce7f686f2539b8ddf8f412",
}
# Float discovery was only a proposal mechanism. These decimal strings
# are exact rationals, and all claims below use Fraction arithmetic.
WITNESSES = (
    ("hard_P0", 8,
     ("-0.019851856035", "-0.032795050897", "-0.049150869785",
      "-0.067327811278", "1"),
     F(100)),
    ("soft_P4_minus_tP0", 14,
     ("0.009304431182", "0.003073478179", "-0.023149401078",
      "-0.061391152055", "1"),
     F(1000)),
)


def sqrt_up(x):
    """Rational upper bound on sqrt(x), with an explicit 10^-15 grid."""
    assert x >= 0
    if x == 0:
        return F(0)
    return F(isqrt(x.numerator*SCALE*SCALE // x.denominator)+1, SCALE)


def down(x):
    return F(x.numerator*SCALE//x.denominator, SCALE)


def run(reverse=False):
    data = {}
    for path, sha in sorted(PINS.items(), reverse=reverse):
        raw = (ROOT/path).read_bytes()
        digest = hashlib.sha1(
            b"blob " + str(len(raw)).encode() + b"\0" + raw
        ).hexdigest()
        assert digest == sha, (path, "pinned input changed")
        data[path] = json.loads(raw)

    def get(s):
        return data["certificates/rpb108_rc"+s+".json"]

    mom = get("129_four_vector_joint_moment")
    original = get("279_six_mode_gate")[
        "coupled_six_mode_gate_certificates"][0][
        "actual_polynomial_action_certificates"]
    red = get("283_reduced_reference")["reduced_reference_options"][0]
    prior = get("295_three_column_dual_obstruction")
    p6 = get("297_native_p6_high_projection")
    targets = get("292_signed_inverse_action_contract")[
        "integer_sufficient_Chebyshev_action_budgets"]
    t = F(get("290_soft_source_decomposition")[
        "exact_soft_mixing_parameter"])
    assert prior["three_column_universal_acceptance_exclusion_for_both"]
    assert p6["four_native_input_columns_now_with_complete_p6_high_output"]
    assert not p6["Stage_I_closed"]
    assert [r["source"] for r in original[:3]] == [
        "P0", "P2", "P4"]
    actions = list(original[:3]) + [
        p6["new_original_P6_full_high_output_action"]]
    assert [r["source"] for r in actions] == [
        "P0", "P2", "P4", "P6"]
    assert all(len(r["finite_original_D_action"]) == 2049 for r in actions)
    assert p6["rank317_augmented_action_adds_only_one_coordinate"]
    assert p6["augmented_action_single_coordinate_patch"]["degree"] == 6

    sl = F(mom["actual_D_Gram_entry_lower"][0][0])/(2*B)
    sh = F(mom["actual_D_Gram_entry_upper"][0][0])/(2*B)
    sm = (sl+sh)/2
    lam = F(red["parameter_lambda"])
    mu = F(red["reduced_reference_options"][1][
        "certified_D_reference_floor_lower"])
    assert 0 < sl <= sm <= sh and lam > 0 and mu > F(1, 200)
    assert red["reduced_reference_options"][1][
        "new_low_reference_rank"] == 122

    H = [F(0)]
    for n in range(1, 15):
        H.append(H[-1]+F(1, n))

    def mass(n):
        return 2*B/F(2*n+1)

    # N_new P_d = N_original P_d + lambda/(H_d+s) P_d.
    # Actual original profile D-faults are paid for all four inputs.
    errors = [F(a["global_D_fault_norm_upper"]) for a in actions]
    assert all(e > 0 for e in errors)
    assert all(F(a["model_D_energy_beyond_2048_upper"]) > 0
               for a in actions)

    rows = []
    for idx, (label, extra, dual_strings, claim) in enumerate(WITNESSES):
        tar = targets[idx]
        assert label == tar["source"]
        modes = (0, 2, 4, 6, extra)
        q = [F(v) for v in dual_strings]
        assert len(q) == 5 and all(n % 2 == 0 for n in modes)
        source = {int(k): F(v) for k, v in tar[
            "original_source_Legendre_coefficients"].items()}
        assert source == ({0: F(1)} if idx == 0
                          else {0: -t, 4: F(1)})
        tol = F(tar[
            "required_total_approximation_residual_D_norm_squared_strict"])
        assert tol > 0
        # The real operator's *finite* dual action is bounded by
        # its exact rational nominal rows plus pinned global D faults.
        nominal = [
            [F(actions[j]["finite_original_D_action"][n]["coefficient"])
             + (lam/(H[n]+sm) if n == d else F(0))
             for j, d in enumerate(DEGREES)]
            for n in modes
        ]
        eta = [sum((q[i]*nominal[i][j] for i in range(5)), F(0))
               for j in range(4)]
        # The duals are rational proposals, NOT exact annihilators.
        # This term is mandatory: every residual eta_j is charged.
        inverse_dual_norm = sqrt_up(sum(
            (q[i]**2/(mass(n)*(H[n]+sl))
             for i, n in enumerate(modes)), F(0)))
        rhs_mid = sum((q[i]*source.get(n, F(0))/(H[n]+sm)
                       for i, n in enumerate(modes)), F(0))
        variation = {
            d: max(abs(1/(H[d]+s)-1/(H[d]+sm))
                   for s in (sl, sh)) for d in DEGREES
        }
        rhs_error = sum((abs(q[i]*source.get(n, F(0))) *
                         variation[n] for i, n in enumerate(modes)
                         if n in source), F(0))
        rhs_norm = sqrt_up(sum(
            (mass(d)*v*v/(H[d]+sl)
             for d, v in source.items()), F(0)))
        assumed_seed_D_norm = (
            rhs_norm + sqrt_up(tol))/mu

        # For ||r||_D < sqrt(tol), coercivity N_new >= mu I
        # bounds ALL seed coefficients in the four-dimensional span.
        # The individual input column budget then covers its finite
        # nominal defect, global original D-error, and augmentation
        # s-interval uncertainty in the corresponding output mode.
        charges = []
        for j, d in enumerate(DEGREES):
            seed_coeff_abs_max = (
                assumed_seed_D_norm *
                sqrt_up(1/(mass(d)*(H[d]+sl))))
            model_defect = abs(eta[j])
            global_fault = inverse_dual_norm*errors[j]
            augment_error = abs(q[modes.index(d)])*lam*variation[d]
            charges.append(seed_coeff_abs_max*(
                model_defect + global_fault + augment_error))
        strict_gap = abs(rhs_mid)-rhs_error-sum(charges, F(0))
        required = claim*inverse_dual_norm*sqrt_up(tol)
        # Exact rational inequality: since claim > 1, this
        # contradicts EVERY four-column seed meeting RC292's
        # strictly smaller D-residual norm tolerance.
        assert strict_gap > required, (
            label, "four-column no-go criterion not established")
        rows.append({
            "source": label,
            "finite_dual_row_degrees": list(modes),
            "rational_dual_coefficients": list(dual_strings),
            "nominal_nonannihilation_defect_paid_exactly": True,
            "every_original_column_global_D_fault_paid": True,
            "physical_rank317_augmentation_interval_paid": True,
            "source_RHS_s_interval_paid": True,
            "infinite_output_tail_dual_pairing_zero_by_support": True,
            "lower_dual_obstruction_ratio_strictly_greater_than":
                str(claim),
            "certified_all_four_column_RC292_residual_accepted_seeds_excluded":
                True,
            # A compact diagnostic, outward-truncated downward;
            # mathematical acceptance uses the exact inequality above.
            "witness_ratio_down_15_digits": str(down(
                strict_gap/(inverse_dual_norm*sqrt_up(tol)))),
        })

    return {
        "milestone": "RC298",
        "starting_commit":
            "57c81e17b994c5f349c64836d862fe79f1a96013",
        "input_git_blob_pins": PINS,
        "reference_rank": 317,
        "certified_original_input_basis": list(DEGREES),
        "finite_dual_witnesses": rows,
        "four_column_universal_RC292_acceptance_exclusion_for_both": True,
        "strict_RC292_residual_tolerance_used_without_relaxation": True,
        "all_seed_projection_caps_ignored_for_stronger_no_go": True,
        "actual_negative_Weil_direction_proved": False,
        "complete_original_arbitrary_input_operator_evaluation": False,
        "native_full_Chebyshev_inverse_executed": False,
        "remaining_314_principal_Schur_positive": False,
        "Stage_I_closed": False, "RH": False, "F4": False, "Lean": False,
        "next_cursor": (
            "RC299: enlarge native source-action span beyond P6, "
            "or build a certified operator-wide recurrence action. "
            "Do not optimize the already excluded four-column family.")
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--replay", action="store_true")
    args = parser.parse_args()
    obj = run(args.replay)
    if args.replay:
        assert obj == json.loads(args.output.read_text(encoding="utf-8"))
    else:
        args.output.write_text(json.dumps(
            obj, sort_keys=True, indent=2)+"\n", encoding="utf-8")
    print("RC298 VALIDATED: both four-column RC292 residual gates "
          "universally excluded; Stage I OPEN", flush=True)
