"""RC302: paid native action for EVERY even polynomial in the known V5 input span.

The five independent native original action columns P0..P8 are pinned.
Linearity supplies an arbitrary rational-input API *within V5*, with a
uniform norm bound on its 2049 finite-output approximation including
all original high-output tails and the physical rank-317 augmentations.

A separately paid finite-mode witness proves N_new(V5) is not contained
in V5, so the API CANNOT run even a second Chebyshev recurrence action.
This is an interface theorem and a noninvariance obstruction; no true
inverse, Stage I, original Weil positivity or RH conclusion is claimed.
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
END = 2048
PINS = {
    "certificates/rpb108_rc129_four_vector_joint_moment.json":
        "33e681e688450c987993603354544fe3919b435f",
    "certificates/rpb108_rc279_six_mode_gate.json":
        "bd729c0f5a41debac61a0f3c37276bb94e7834e5",
    "certificates/rpb108_rc283_reduced_reference.json":
        "1dc4bba375af6bfd7a274fccc07638e0eead56e6",
    "certificates/rpb108_rc297_native_p6_high_projection.json":
        "228a2cd9cb8f92324cce7f686f2539b8ddf8f412",
    "certificates/rpb108_rc300_native_p8_high_projection.json":
        "e40c90234bc0d03631f250f710e2a8eb0ac10176",
    "certificates/rpb108_rc301_five_column_dual_obstruction.json":
        "7da305dcbdb5f95d5d12ec4eabbd8f8adde04269",
}


def sqrt_up(x):
    assert x >= 0
    if x == 0:
        return F(0)
    return F(isqrt(x.numerator*SCALE*SCALE//x.denominator)+1, SCALE)


def sqrt_down(x):
    assert x >= 0
    if x == 0:
        return F(0)
    return F(isqrt(x.numerator*SCALE*SCALE//x.denominator), SCALE)


def norm_weight(n, s):
    return 2*B/F(2*n+1)*s


def run(reverse=False):
    data = {}
    for path, sha in sorted(PINS.items(), reverse=reverse):
        raw = (ROOT/path).read_bytes()
        digest = hashlib.sha1(
            b"blob "+str(len(raw)).encode()+b"\0"+raw
        ).hexdigest()
        assert digest == sha, (path, "inherited blob pin mismatch")
        data[path] = json.loads(raw)

    def get(s):
        return data["certificates/rpb108_rc"+s+".json"]

    orig = get("279_six_mode_gate")[
        "coupled_six_mode_gate_certificates"][0][
        "actual_polynomial_action_certificates"]
    p6 = get("297_native_p6_high_projection")
    p8 = get("300_native_p8_high_projection")
    prior = get("301_five_column_dual_obstruction")
    assert prior["all_real_five_column_RC292_accepted_seeds_excluded_both_sources"]
    assert p8["five_native_even_input_action_columns_available"] == list(DEGREES)
    assert p6["rank317_augmented_action_adds_only_one_coordinate"]
    assert p8["rank317_physical_augmented_P8_patch"]["degree"] == 8
    profiles = list(orig[:3])+[
        p6["new_original_P6_full_high_output_action"],
        p8["complete_native_P8_original_high_output_action"]]
    assert [v["source"] for v in profiles] == [
        "P0", "P2", "P4", "P6", "P8"]
    assert all(len(v["finite_original_D_action"]) == END+1
               for v in profiles)
    assert all(all(row["degree"] == i for i, row in enumerate(
        v["finite_original_D_action"])) for v in profiles)
    assert all(all(row["coefficient"] == "0" for row in
        v["finite_original_D_action"] if row["degree"]%2) for v in profiles)

    mom = get("129_four_vector_joint_moment")
    reduced = get("283_reduced_reference")
    assert reduced["proposed_buffered_reference_rank"] == 317
    preferred = reduced["reduced_reference_options"][0]
    selection = preferred["reduced_reference_options"][1]
    assert selection["new_low_reference_rank"] == 122
    assert selection["first_discarded_matching_degree"] == 244
    lam = F(preferred["parameter_lambda"])
    sl = F(mom["actual_D_Gram_entry_lower"][0][0])/(2*B)
    sh = F(mom["actual_D_Gram_entry_upper"][0][0])/(2*B)
    sm = (sl+sh)/2
    assert 0 < sl <= sm <= sh and lam > 0
    H = [F(0)]
    for n in range(1, END+1):
        H.append(H[-1]+F(1, n))

    # The finite-output coefficient center for arbitrary y in V5.
    # y may be ANY rational 5-vector, without bounded coefficients.
    # The same formula extends to real coefficients by continuity.
    # It cannot accept P10 or a general polynomial input.
    finite_centers = [
        [F(profile["finite_original_D_action"][n]["coefficient"])
         for n in range(END+1)]
        for profile in profiles]

    def center_at(y, n):
        assert len(y) == 5 and 0 <= n <= END
        return sum((
            y[j]*finite_centers[j][n] +
            (y[j]*lam/(H[d]+sm) if n == d else F(0))
            for j, d in enumerate(DEGREES)), F(0))

    # Since ||e_d||_D <= E_d, Minkowski and then Cauchy give
    # ||N_new y - hatN_new y||_D <= sum |y_d|E_d <= C ||y||_D.
    # C^2 >= sum E_d^2 /[m_d(H_d+s_lower)], exact and universal
    # for ALL y in the supported five-dimensional domain.
    columns = []
    E = []
    for j,d in enumerate(DEGREES):
        act = profiles[j]
        fault = F(act["global_D_fault_norm_upper"])
        tail_sq = F(act["model_D_energy_beyond_2048_upper"])
        assert fault > 0 and tail_sq > 0
        alo = lam/(H[d]+sh)
        ahi = lam/(H[d]+sl)
        am = lam/(H[d]+sm)
        arad = max(am-alo, ahi-am)
        assert 0 <= arad and alo <= am <= ahi
        aug_D = sqrt_up(norm_weight(d,H[d]+sh)*arad*arad)
        tail_D = sqrt_up(tail_sq)
        total = fault + tail_D + aug_D
        input_weight_lower = norm_weight(d,H[d]+sl)
        assert total > 0 and input_weight_lower > 0
        E.append(total)
        columns.append(dict(
            degree=d,
            original_D_fault_norm_upper=str(fault),
            original_high_output_D_energy_upper=str(tail_sq),
            original_high_output_D_norm_upper=str(tail_D),
            augmented_coefficient_exact_midpoint=str(am),
            augmented_coefficient_interval_radius=str(arad),
            added_projection_D_norm_upper=str(aug_D),
            complete_action_model_D_error_upper=str(total),
            physical_input_D_weight_lower=str(input_weight_lower)))
    C = sqrt_up(sum((
        E[j]*E[j]/F(columns[j]["physical_input_D_weight_lower"])
        for j in range(5)), F(0)))
    assert F(0) < C < F(1, 2)

    # Two nontrivial POLYNOMIAL INPUTS, not just the five basis inputs.
    samples = [
        ("mixed_signed_A", [F(1), F(-1,2), F(1,3), F(-1,4), F(1,5)]),
        ("mixed_signed_B", [F(-2,3), F(1,7), F(3,5), F(-1,9), F(1,11)]),
    ]
    sample_out = []
    for name,y in (reversed(samples) if reverse else samples):
        assert len(y)==5
        action_error = sum((abs(y[j])*E[j] for j in range(5)),F(0))
        physical_input_weight_lower = sum(
            (y[j]*y[j]*F(columns[j]["physical_input_D_weight_lower"])
             for j in range(5)), F(0))
        assert action_error*action_error <= C*C*physical_input_weight_lower
        # Sums, scaling, and parity must hold directly at all 2049
        # finite-output coordinates, not merely a low-mode example.
        for n in range(END+1):
            val = center_at(y,n)
            rhs = sum((
                y[j]*center_at(
                    [F(k==j) for k in range(5)],n)
                for j in range(5)),F(0))
            assert val == rhs, ("polynomial action linearity",n)
            if n%2:assert val == 0
        sample_out.append(dict(
            name=name,
            exact_input_legendre_coefficients={
                str(d):str(y[j]) for j,d in enumerate(DEGREES)},
            finite_output_center_selected_even_modes={
                str(n):str(center_at(y,n))
                for n in (0,2,4,6,8,10,12,14,16)},
            complete_2049_degree_linear_action_verified=True,
            supported_input_physical_D_norm_squared_lower=str(
                physical_input_weight_lower),
            actual_original_plus_augmentation_action_D_error_upper=str(
                action_error),
            universal_bound_verified=True))
    sample_out.sort(key=lambda x:x["name"])

    # ACTUAL NEW FACT: P0 is mapped outside V5 by the original-plus-
    # reference action. This uses finite coefficient n=10, which is
    # unaffected by the rank317 augmentation on P0. Its difference
    # from the pinned model center is bounded by the FULL ORIGINAL
    # global D-fault, already containing all original coefficient
    # rounding and other analytic arithmetic faults. No infinity-
    # tail assumption is needed since the witness is at n=10.
    exterior = []
    for j in (0,4):
        d = DEGREES[j]
        n = 10
        coeff = finite_centers[j][n]
        fault = F(profiles[j]["global_D_fault_norm_upper"])
        weight = norm_weight(n,H[n]+sl)
        assert weight*coeff*coeff > fault*fault, (
            "no certified exterior nonzero output",d)
        # A rational positive lower bound on the D-distance to V5:
        # projected |coeff| sqrt(weight) exceeds global fault.
        gap = abs(coeff)*sqrt_down(weight)-fault
        assert gap > 0
        exterior.append(dict(
            input_degree=d,
            exterior_output_degree=10,
            original_high_output_coefficient_center=str(coeff),
            original_global_D_fault_norm_upper=str(fault),
            actual_exterior_D_distance_lower=str(gap),
            original_plus_augmentation_action_outside_V5=True))
    assert len(exterior)==2

    return dict(
        milestone="RC302",
        starting_commit="197e0ede552e633d7cb661158451164aca4a632f",
        input_git_blob_pins=PINS,
        actual_even_input_domain_supported=list(DEGREES),
        exact_linear_native_operator_action_for_every_rational_vector_in_V5=True,
        real_coefficient_extension_by_linearity_and_continuity=True,
        original_action_output_cutoff=END,
        original_prime_arch_pole_endpoint_imported_columns_retained=True,
        physical_augmentation_on_matching_retained_degree_only=True,
        all_original_infinite_output_tails_paid=True,
        column_error_components=columns,
        uniform_supported_input_action_relative_D_error_upper=str(C),
        universal_operator_norm_bound_only_on_V5=True,
        mixed_polynomial_input_tests=sample_out,
        certified_noninvariance_output_witnesses=exterior,
        N_new_V5_not_subset_V5_certified=True,
        full_N_new_square_on_V5_not_evaluated=True,
        Chebyshev_recurrence_not_executable_from_five_columns=True,
        arbitrary_even_polynomial_input_degree_above_eight_supported=False,
        arbitrary_input_uniform_prime_endpoint_tail_bound_certified=False,
        true_inverse_signed_response_certified=False,
        original_Weil_form_positivity_certified=False,
        remaining_314_principal_Schur_positive=False,
        Stage_I_closed=False, RH=False, F4=False, Lean=False,
        next_cursor=(
            "RC303: extend the native linear polynomial-action API "
            "beyond degree 8 with source-degree uniform analytic "
            "prime/endpoint/arithmetic estimates; do not represent "
            "the supported V5 domain as a Chebyshev-invariant carrier.")
    )


if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",required=True,type=Path)
    p.add_argument("--replay",action="store_true")
    args=p.parse_args()
    result=run(reverse=args.replay)
    if args.replay:
        assert result==json.loads(
            args.output.read_text(encoding="utf-8"))
    else:
        args.output.write_text(json.dumps(
            result,sort_keys=True,indent=2)+"\n",
            encoding="utf-8")
    print("RC302 VALIDATED: all V5 rational polynomial inputs supported "
          "with uniform paid D-action error; V5 NOT invariant; "
          "Stage I OPEN",flush=True)
