"""RC301: exact six-output dual obstruction to five-column RC292 inverse seeds.

Four known even action columns come from RC279/297; the fifth genuinely
new native P8 action column comes from RC300. Two rational finite-support
dual witnesses test all REAL input seeds in span{P0,P2,P4,P6,P8}.
Each witness pays its exact (nonzero) nominal annihilation defect, the
complete five original global D-action faults, source and projection
s-interval errors, and the coercive seed bound. Infinite-output tails
pair exactly zero with the finitely supported witness. The result is a
restricted-input impossibility for RC292's strict *sufficient* tolerance;
not a negative Weil form, true inverse failure, Stage I or RH claim.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
B = F(11, 10)
SCALE = 10**15
DEGREES = (0, 2, 4, 6, 8)
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
    "certificates/rpb108_rc298_four_column_dual_obstruction.json":
        "609eb6c0a411f0f171b4704d952309b5d906f85d",
    "certificates/rpb108_rc297_native_p6_high_projection.json":
        "228a2cd9cb8f92324cce7f686f2539b8ddf8f412",
    "certificates/rpb108_rc300_native_p8_high_projection.json":
        "e40c90234bc0d03631f250f710e2a8eb0ac10176",
}

# Floating-point search ONLY proposed these rational witnesses.
# All conclusions are from Fraction arithmetic below. In particular,
# their small, nonzero nominal annihilation defects are NOT discarded.
WITNESSES = (
    ("hard_P0", 16,
     ("-0.02195481493350", "-0.02590091346292",
      "-0.01524376283263", "0.00440434724155",
      "0.01433147776488", "1"),
     F(100)),
    ("soft_P4_minus_tP0", 14,
     ("0.01071441581073", "0.00540275749568",
      "-0.01965844432521", "-0.05660917203156",
      "-0.07102533013776", "1"),
     F(1000)),
)


def sqrt_up(x):
    assert x >= 0
    if x == 0:
        return F(0)
    return F(isqrt(x.numerator*SCALE*SCALE//x.denominator)+1, SCALE)


def down(x):
    return F(x.numerator*SCALE//x.denominator, SCALE)


def run(reverse=False):
    data = {}
    for path, sha in sorted(PINS.items(), reverse=reverse):
        raw = (ROOT/path).read_bytes()
        digest = hashlib.sha1(
            b"blob "+str(len(raw)).encode()+b"\0"+raw
        ).hexdigest()
        assert digest == sha, (path, "inherited content pin changed")
        data[path] = json.loads(raw)

    def get(s):
        return data["certificates/rpb108_rc"+s+".json"]

    mom = get("129_four_vector_joint_moment")
    orig = get("279_six_mode_gate")[
        "coupled_six_mode_gate_certificates"][0][
        "actual_polynomial_action_certificates"]
    ref = get("283_reduced_reference")
    soft = F(get("290_soft_source_decomposition")[
        "exact_soft_mixing_parameter"])
    prior = get("298_four_column_dual_obstruction")
    p6 = get("297_native_p6_high_projection")
    p8 = get("300_native_p8_high_projection")
    targets = get("292_signed_inverse_action_contract")[
        "integer_sufficient_Chebyshev_action_budgets"]
    assert prior["four_column_universal_RC292_acceptance_exclusion_for_both"]
    assert p6["four_native_input_columns_now_with_complete_p6_high_output"]
    assert p8["all_output_degrees_65_to_2048_materialized"]
    assert p8["low_65_coefficients_reproduce_RC299"]
    assert p8["complete_original_infinite_D_tail_paid"]
    assert p8["five_native_even_input_action_columns_available"] == list(DEGREES)
    assert [r["source"] for r in orig[:3]] == ["P0", "P2", "P4"]
    actions = list(orig[:3])+[
        p6["new_original_P6_full_high_output_action"],
        p8["complete_native_P8_original_high_output_action"]]
    assert [r["source"] for r in actions] == [
        "P0", "P2", "P4", "P6", "P8"]
    assert all(len(r["finite_original_D_action"]) == 2049
               for r in actions)
    assert p8["rank317_physical_augmented_P8_patch"]["degree"] == 8
    assert p6["augmented_action_single_coordinate_patch"]["degree"] == 6
    assert ref["proposed_buffered_reference_rank"] == 317

    selected = ref["reduced_reference_options"][0]
    assert selected["reduced_reference_options"][1][
        "new_low_reference_rank"] == 122
    assert selected["reduced_reference_options"][1][
        "first_discarded_matching_degree"] == 244
    sl = F(mom["actual_D_Gram_entry_lower"][0][0])/(2*B)
    sh = F(mom["actual_D_Gram_entry_upper"][0][0])/(2*B)
    sm = (sl+sh)/2
    lam = F(selected["parameter_lambda"])
    mu = F(selected["reduced_reference_options"][1][
        "certified_D_reference_floor_lower"])
    assert 0 < sl <= sm <= sh and lam > 0 and mu > F(1, 200)
    H = [F(0)]
    for n in range(1, 17):
        H.append(H[-1]+F(1, n))

    def mass(n):
        return 2*B/F(2*n+1)

    # Original global faults can include all finite original coefficient
    # rounding and imported native prime/endpoint arithmetic uncertainty.
    # They are conservatively charged even though the dual support is
    # finite. This uses original (unaugmented) actions only.
    errors = [F(a["global_D_fault_norm_upper"]) for a in actions]
    assert all(v > 0 for v in errors)
    assert all(F(a["model_D_energy_beyond_2048_upper"]) > 0
               for a in actions)

    results = []
    for idx, (label, extra, qstrings, claim) in enumerate(
            reversed(WITNESSES) if reverse else WITNESSES):
        target = next(tar for tar in targets if tar["source"] == label)
        modes = (*DEGREES, extra)
        q = [F(x) for x in qstrings]
        assert len(q) == 6 and modes[-1] > 8
        assert all(n%2 == 0 for n in modes)
        source = {
            int(k): F(v) for k, v in target[
                "original_source_Legendre_coefficients"].items()}
        assert source == (
            {0: F(1)} if label == "hard_P0"
            else {0: -soft, 4: F(1)})
        tol = F(target[
            "required_total_approximation_residual_D_norm_squared_strict"])
        assert tol > 0

        # Nominal original Weil action + exact physical rank-317
        # augmentation at n=d ONLY. All rational and no float inputs.
        nominal = [
            [F(actions[j]["finite_original_D_action"][n][
                "coefficient"])+(
                lam/(H[d]+sm) if n == d else F(0))
             for j, d in enumerate(DEGREES)]
            for n in modes]
        eta = [sum((q[i]*nominal[i][j] for i in range(6)), F(0))
               for j in range(5)]
        assert any(v != 0 for v in eta)  # DO NOT assume annihilation.

        Q = sqrt_up(sum(
            (q[i]*q[i]/(mass(n)*(H[n]+sl))
             for i, n in enumerate(modes)), F(0)))
        assert Q > 0
        mid_signal = sum((q[i]*source.get(n, F(0))/(H[n]+sm)
                          for i, n in enumerate(modes)), F(0))
        variation = {
            d: max(abs(1/(H[d]+s)-1/(H[d]+sm))
                   for s in (sl, sh)) for d in DEGREES
        }
        rhs_error = sum((
            abs(q[i]*source.get(n, F(0)))*variation[n]
            for i, n in enumerate(modes) if n in source), F(0))

        bnorm = sqrt_up(sum((
            mass(d)*v*v/(H[d]+sl) for d, v in source.items()),
            F(0)))
        ybound = (bnorm+sqrt_up(tol))/mu
        components = []
        charges = []
        for j, d in enumerate(DEGREES):
            coefficient_max = ybound*sqrt_up(
                1/(mass(d)*(H[d]+sl)))
            nominal_defect = abs(eta[j])
            original_fault = Q*errors[j]
            augmented_error = (
                abs(q[modes.index(d)])*lam*variation[d])
            charge = coefficient_max*(
                nominal_defect+original_fault+augmented_error)
            components.append(dict(
                original_input_degree=d,
                rational_nominal_nonannihilation=str(eta[j]),
                global_original_D_fault_norm_upper=str(errors[j]),
                seed_coefficient_upper_if_accepted=str(coefficient_max),
                full_Dual_error_charge_upper=str(charge)))
            charges.append(charge)
        gap = abs(mid_signal)-rhs_error-sum(charges, F(0))
        required = claim*Q*sqrt_up(tol)
        assert gap > required, (
            label, "universal five-column obstruction not certified")
        diagnostic = down(gap/(Q*sqrt_up(tol)))
        assert diagnostic > claim
        results.append(dict(
            source=label,
            witness_degree_rows=list(modes),
            exact_rational_dual=list(qstrings),
            all_five_nominal_defects_paid_exactly=True,
            all_five_original_global_D_action_faults_paid=True,
            native_s_interval_rhs_and_projection_paid=True,
            q_finite_support_annihilates_beyond_output_2048_exactly=True,
            original_infinite_D_tails_not_declared_zero=True,
            source_RHS_model_dual_value=str(mid_signal),
            source_RHS_interval_error_upper=str(rhs_error),
            exact_component_charges=components,
            dual_inverse_D_norm_upper=str(Q),
            strict_positive_dual_gap_lower=str(gap),
            rigorous_ratio_lower_down_15_digits=str(diagnostic),
            RC292_strict_residual_squared_target=str(tol),
            claimed_strict_obstruction_ratio_gt=str(claim),
            all_real_five_column_seeds_below_RC292_threshold_excluded=True,
            actual_original_Weil_negative_mode_found=False,
        ))

    results.sort(key=lambda x: x["source"])
    assert len(results) == 2
    return dict(
        milestone="RC301",
        starting_commit="a129ecab91665fb87aabc93a51348016bf0eb051",
        input_git_blob_pins=PINS,
        reference_rank=317,
        certified_even_original_input_basis=list(DEGREES),
        five_column_finite_dual_obstruction_certificates=results,
        all_real_five_column_RC292_accepted_seeds_excluded_both_sources=True,
        original_Weil_action_evaluated_only_on_five_input_columns=True,
        signed_true_inverse_response_certified=False,
        no_original_operator_negative_direction_claim=True,
        remaining_314_principal_Schur_positive=False,
        original_Weil_form_positive=False,
        Stage_I_closed=False, RH=False, F4=False, Lean=False,
        next_cursor=(
            "RC302: do not further optimize P0/P2/P4/P6/P8 seeds. "
            "Develop and certify a reusable original Weil action-on-"
            "arbitrary-polynomial input interface, or extend actual "
            "native source columns and retest a larger paid dual.")
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--replay", action="store_true")
    args = parser.parse_args()
    obj = run(reverse=args.replay)
    if args.replay:
        assert obj == json.loads(args.output.read_text(encoding="utf-8"))
    else:
        args.output.write_text(
            json.dumps(obj, indent=2, sort_keys=True)+"\n",
            encoding="utf-8")
    print("RC301 VALIDATED: all five-input native seeds fail the "
          "unchanged strict RC292 residual tolerance; Stage I OPEN",
          flush=True)
