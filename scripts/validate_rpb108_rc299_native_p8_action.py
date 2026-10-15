"""RC299: new degree-eight native original Weil action through degree 2048.

Extend the tested RC296 generic signed original-action formula from
d=6 to d=8, reconstruct output with RC279 high-prime and endpoint
projector, and attach the rank-317 physical augmentation only at P8.

The old P6 action is recomputed exactly before constructing P8.
This is a fourth->fifth native INPUT action-column extension; not a
certified arbitrary-input operator evaluator or RH positivity theorem.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

import validate_rpb108_rc296_native_p6_action as native
import validate_rpb108_rc279_six_mode_gate as high

ROOT = Path(__file__).resolve().parents[1]
B = F(11, 10)
o = native.o
legacy = native.legacy
up = native.up
down = native.down
root = native.root

PINS = {
    "certificates/rpb108_rc43_native_prime_head.json":
        "b4893953109e6fdc55d52b505c2bcfbf0d38281e",
    "certificates/rpb108_rc46_native_archimedean_head.json":
        "be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
    "certificates/rpb108_rc129_four_vector_joint_moment.json":
        "33e681e688450c987993603354544fe3919b435f",
    "certificates/rpb108_rc283_reduced_reference.json":
        "1dc4bba375af6bfd7a274fccc07638e0eead56e6",
    "certificates/rpb108_rc296_native_p6_action.json":
        "ff03088daa67d681e0371e92c40576d8c3219b4b",
    "certificates/rpb108_rc297_native_p6_high_projection.json":
        "228a2cd9cb8f92324cce7f686f2539b8ddf8f412",
    "scripts/validate_rpb108_rc237_two_trial_signed_response.py":
        "d13e909c8aa8b91d5b55ec5e5e5179cdaf9325d2",
    "scripts/validate_rpb108_rc240_three_trial_signed_response.py":
        "9e1f46907a3c96d2f916d709163d0dea0db5190a",
    "scripts/validate_rpb108_rc279_six_mode_gate.py":
        "02ff6e1b70e79ede5691aa55bc98c877939cce23",
    "scripts/validate_rpb108_rc296_native_p6_action.py":
        "e0707fde1acc8cb12af9e54cf4aad6f15ed154df",
    "scripts/validate_rpb108_rc297_native_p6_high_projection.py":
        "681eed826ee5be571b94fb51611e1fc81430834a",
}


def source_action(d, reg, prime, eps, sl, sh, reverse=False):
    """RC296 formula applied to the new d=8, with P6 regression."""
    assert d in (6, 8) and 65 > 3*d+1 and sl > 0
    regpoly = legacy.trial.regular_poly(d, reg)
    rc = [o.project(regpoly, n) for n in range(len(regpoly))]
    assert len(rc) > 64
    pc, pt, pfault, segments = legacy.trial.prime_poly(
        d, prime, reverse)
    assert len(pc) == 65 and len(segments) == 15
    rtail = up(sum(
        (o.mass(n)*v*v for n, v in enumerate(rc) if n > 64),
        F(0)))
    phi = [F(11, 20)**k/factorial(k) if k%2 == d%2 else F(0)
           for k in range(41)]
    moment = B*o.integral(o.product(o.legendre(d), phi))
    pole = [2*(-1)**d*moment*v for v in phi]
    oc = [o.project(pole, n) for n in range(65)]
    tau = 2*F(11, 20)**41/factorial(41)
    polefault = up(16*B*tau*root(o.mass(d)))
    ll = 2*sum(
        (F(1, 3)**(2*k+1)/F(2*k+1) for k in range(100)),
        F(0))
    lh = ll+2*F(1, 3)**201/(201*(1-F(1, 9)))
    out = []
    rnd = F(0)
    for n in range(65):
        if n%2 != d%2:
            out.append(dict(
                degree=n, coefficient="0", radius="0"))
            continue
        h = (2*o.H(2*n)-2*o.H(n)+F(1, 2*n+1)
             if n == d else
             F(2*n+1, abs(n-d)*(n+d+1)))
        lo = (h-(lh if n == d else 0)-rc[n]+pc[n]+oc[n]
              -(F(789, 125) if n == d else 0))
        hi = (h-(ll if n == d else 0)-rc[n]+pc[n]+oc[n]
              -(F(789, 125) if n == d else 0))
        vals = [
            q/(o.H(n)+s)+F(n == d)
            for q in (lo, hi) for s in (sl, sh)]
        c = down((min(vals)+max(vals))/2)
        r = max(c-min(vals), max(vals)-c)
        rnd += o.mass(n)*(o.H(n)+sh)*r*r
        out.append(dict(
            degree=n, coefficient=str(c), radius=str(up(r))))
    first = 66  # d=6 and d=8 both even.
    components = dict(
        finite_rounding=up(rnd),
        endpoint_omitted_output=up(
            3*B/((o.H(first)+sl)*(64-d)**2)),
        regular_omitted_output=up(rtail/(o.H(first)+sl)),
        prime_omitted_output=up(pt/(o.H(first)+sl)),
        regular_kernel=up((2*B*eps)**2*o.mass(d)/sl),
        prime_arithmetic=up(pfault**2/sl),
        pole_Taylor=up(polefault**2/sl))
    total = up(sum((root(v) for v in components.values()),
                   F(0))**2)
    return dict(
        input="P"+str(d),
        input_degree=d,
        parity="even",
        finite_original_D_action=out,
        D_energy_component_squared_errors={
            k: str(v) for k, v in components.items()},
        complete_original_action_D_error_squared_upper=str(total),
        original_output_cutoff=64,
        first_omitted_even_degree=first,
        complete_active_prime_pairs=7,
        all_omitted_outputs_paid=True)


def run(reverse=False):
    data = {}
    for path, pin in sorted(PINS.items(), reverse=reverse):
        raw = (ROOT/path).read_bytes()
        got = hashlib.sha1(
            b"blob "+str(len(raw)).encode()+b"\0"+raw
        ).hexdigest()
        assert got == pin, (path, "source pin")
        if path.endswith(".json"):
            data[path] = json.loads(raw)

    def get(i):
        return data["certificates/rpb108_rc"+i+".json"]

    metric = get("129_four_vector_joint_moment")
    regcert = get("46_native_archimedean_head")
    reg = list(map(F, regcert["regular_kernel_coefficients"]))
    eps = F(regcert["regular_kernel_uniform_error_upper"])
    prime = get("43_native_prime_head")
    p6 = get("296_native_p6_action")["new_native_P6_original_action"]
    old = get("297_native_p6_high_projection")
    ref = get("283_reduced_reference")
    assert old["four_native_input_columns_now_with_complete_p6_high_output"]
    assert ref["proposed_buffered_reference_rank"] == 317
    preferred = ref["reduced_reference_options"][0]
    choice = preferred["reduced_reference_options"][1]
    assert choice["new_low_reference_rank"] == 122
    assert choice["first_discarded_matching_degree"] == 244
    lam = F(preferred["parameter_lambda"])
    sl = F(metric["actual_D_Gram_entry_lower"][0][0])/(2*B)
    sh = F(metric["actual_D_Gram_entry_upper"][0][0])/(2*B)
    assert 0 < sl <= sh and lam > 0
    assert len(prime["active_prime_powers"]) == 7

    # Same generic signed source formula MUST reproduce all RC296
    # P6 original output and uncertainty components without change.
    regression = source_action(6, reg, prime, eps, sl, sh, reverse)
    for key in (
            "finite_original_D_action",
            "D_energy_component_squared_errors",
            "complete_original_action_D_error_squared_upper"):
        assert regression[key] == p6[key], ("P6 regression", key)
    print("RC299: P6 original-action formula regression passed",
          flush=True)

    # Fresh actual original input P8; no interpolation from prior
    # columns and no imaginary arbitrary-input operator evaluation.
    p8 = source_action(8, reg, prime, eps, sl, sh, reverse)
    assert p8["finite_original_D_action"][8]["coefficient"] != "0"
    assert all(
        row["coefficient"] == row["radius"] == "0"
        for row in p8["finite_original_D_action"]
        if row["degree"]%2)
    print("RC299: new native P8 low original response resolved",
          flush=True)

    H = [F(0)]
    for n in range(1, 2051):
        H.append(H[-1]+F(1, n))
    prof = high.secondary_action(
        8, p8, prime, sl, sh, H, reverse)
    coeff = prof["finite_original_D_action"]
    assert prof["source"] == "P8"
    assert len(coeff) == 2049
    assert all(v["degree"] == i for i, v in enumerate(coeff))
    assert all(v["coefficient"] == p8[
        "finite_original_D_action"][n]["coefficient"]
        for n, v in enumerate(coeff[:65]))
    assert all(v["coefficient"] == "0"
               for v in coeff if v["degree"]%2)
    assert any(F(coeff[n]["coefficient"]) != 0
               for n in range(66, 2049, 2))
    assert F(prof["global_D_fault_norm_upper"]) > 0
    assert F(prof["model_D_energy_beyond_2048_upper"]) > 0
    assert prof["prime_projection_certificate"][
        "prime_projection_cutoff"] == 2048

    # Rank-317 projection retains P8; D^-1 lambda P_low adds
    # lambda/(H8+s) P8 and NO other mode.
    lo = lam/(H[8]+sh)
    hi = lam/(H[8]+sl)
    center = down((lo+hi)/2)
    radius = up(max(center-lo, hi-center))
    assert radius > 0 and center-radius <= lo <= hi <= center+radius
    aug8 = F(coeff[8]["coefficient"])+center
    addnorm = up(root(up(o.mass(8)*(H[8]+sh)*radius**2)))
    newfault = up(F(prof["global_D_fault_norm_upper"])+addnorm)
    assert newfault > 0
    assert F(prof["model_D_energy_beyond_2048_upper"]) > 0
    return dict(
        milestone="RC299",
        starting_commit="acb7ce39ff7f354fcc4e155870eb0a4bc5ddaa94",
        input_git_blob_pins=PINS,
        RC296_P6_formula_regression_exact=True,
        native_P8_low_original_action=p8,
        new_native_P8_complete_high_original_action=prof,
        original_output_last_degree=2048,
        all_p8_prime_endpoint_outputs_through_2048_paid=True,
        p8_original_infinite_output_tail_paid=True,
        reference_rank=317,
        reference_even_rank=122,
        exact_rank317_physical_P8_patch=dict(
            output_degree=8,
            lambda_exact=str(lam),
            coefficient_lower=str(lo),
            coefficient_upper=str(hi),
            coefficient_center=str(center),
            coefficient_radius=str(radius),
            augmented_degree8_center=str(aug8),
            augmentation_D_error_norm_upper=str(addnorm)),
        augmented_P8_global_D_fault_norm_upper=str(newfault),
        augmented_P8_infinite_tail_D_energy_upper=prof[
            "model_D_energy_beyond_2048_upper"],
        five_original_even_input_columns_available=[
            0, 2, 4, 6, 8],
        RC292_signed_residual_acceptance_test_executed_on_five_columns=False,
        arbitrary_input_Weil_action_certified=False,
        five_column_Galerkin_seed_optimized=False,
        five_column_dual_obstruction_test_executed=False,
        no_new_source_positivity_claim=True,
        Stage_I_closed=False,
        RH=False, F4=False, Lean=False,
        next_cursor=(
            "RC300: test five-column signed inverse seeds, "
            "then compute rigorous six-output dual obstructions "
            "using the new P8 action. If they remain strongly "
            "obstructed, prioritize operator-wide action rules."))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path, required=True)
    parser.add_argument("--replay", action="store_true")
    args = parser.parse_args()
    outcome = run(reverse=args.replay)
    if args.replay:
        assert outcome == json.loads(
            args.output.read_text(encoding="utf-8"))
    else:
        args.output.write_text(
            json.dumps(outcome, indent=2, sort_keys=True)+"\n",
            encoding="utf-8")
    print("RC299 VALIDATED: fifth native even input P8; "
          "Stage I OPEN", flush=True)
